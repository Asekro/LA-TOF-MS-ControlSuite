"""Leybold GRAPHIX ONE RS232 driver.

Reference: GA300550402_001_C2 (2017), chapter 8, pages 97-107.
Serial settings: 8 data bits, no parity, 1 stop bit, no handshake.
The selected device baud rate and displayed pressure unit must match expectations.
"""

import math
import serial


class GraphixError(Exception):
    """Base exception for GRAPHIX ONE communication and device errors."""


class GraphixOne:
    """Communicate with a GRAPHIX ONE over RS232 (without RS485 addressing)."""

    # NACK error codes from manual, table 69, page 100.
    ERRORS = {
        -6: "Checksum error",
        -8: "Invalid command format",
        -9: "Parameter group does not exist",
        -10: "Parameter is not available for this sensor type",
        -11: "Parameter is read-only",
        -12: "Invalid parameter value",
        -13: "Invalid number of parameter values",
        -14: "Parameter cannot be changed right now",
        -15: "Parameter does not exist",
        -16: "USB file handling error",
    }

    # ---------------------------------------------------------------
    # 1. INITIALIZATION AND CONNECTION
    # ---------------------------------------------------------------

    def __init__(self, port, baudrate=9600, timeout=2):
        """Save connection settings; do not open the port yet."""
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None

    def connect(self):
        """Open the serial connection (RS232, 8N1, no handshake)."""
        if self.ser is not None and self.ser.is_open:
            return
        self.ser = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=self.timeout,
            write_timeout=self.timeout,
            xonxoff=False,
            rtscts=False,
            dsrdtr=False,
        )

    def disconnect(self):
        """Close the connection when it is no longer needed."""
        if self.ser is not None:
            self.ser.close()
            self.ser = None

    # ---------------------------------------------------------------
    # 2. FUNDAMENTAL DEVICE FUNCTIONS
    # ---------------------------------------------------------------

    @staticmethod
    def _checksum(data):
        """Compute the one-byte GRAPHIX checksum (manual, page 100)."""
        crc = 255 - (sum(data) % 256)
        if crc < 32:
            crc += 32  # Avoid ASCII control characters.
        return crc

    def _exchange(self, message):
        """Send a command and return its checked ASCII payload.

        Successful reply: ACK (0x06) + value + CRC + EOT (0x04).
        Error reply:      NACK (0x15) + error code + CRC + EOT.
        """
        if self.ser is None or not self.ser.is_open:
            raise GraphixError("Not connected. Call connect() first.")

        # EOT terminates every request and response (manual, pages 98-99).
        command = message + bytes([self._checksum(message), 0x04])
        try:
            self.ser.reset_input_buffer()  # Discard stale bytes from earlier requests.
            sent = self.ser.write(command)
            if sent != len(command):
                raise GraphixError("Command was not transmitted completely")
            response = self.ser.read_until(b"\x04", size=512)
        except serial.SerialTimeoutException as exc:
            raise GraphixError("Serial write timeout") from exc
        except serial.SerialException as exc:
            raise GraphixError(f"Serial communication error: {exc}") from exc

        if not response:
            raise GraphixError("Timeout: device did not respond")
        if not response.endswith(b"\x04"):
            raise GraphixError(f"Incomplete response (no EOT): {response!r}")
        if len(response) < 3:
            raise GraphixError(f"Response too short: {response!r}")
        if response[-2] != self._checksum(response[:-2]):
            raise GraphixError(f"Invalid response checksum: {response!r}")

        # Strip the first byte (ACK/NACK), CRC, and EOT.
        try:
            payload = response[1:-2].decode("ascii")
        except UnicodeDecodeError as exc:
            raise GraphixError(f"Response contains non-ASCII data: {response!r}") from exc

        if response[0] == 0x15:  # NACK: device rejected the request.
            try:
                code = int(payload.strip())
            except ValueError as exc:
                raise GraphixError(f"Malformed device error code: {payload!r}") from exc
            description = self.ERRORS.get(code, "Unknown device error")
            raise GraphixError(f"GRAPHIX error {code}: {description}")
        if response[0] != 0x06:  # ACK: successful request.
            raise GraphixError(f"Unexpected response prefix: 0x{response[0]:02X}")
        return payload.strip()

    @staticmethod
    def _validate_parameter(group, number):
        """Restrict identifiers to the documented groups and positive numbers."""
        if type(group) is not int or group not in range(1, 6):
            raise ValueError("Parameter group must be an integer from 1 to 5")
        if type(number) is not int or number < 1:
            raise ValueError("Parameter number must be a positive integer")

    def read_parameter(self, group, number):
        """Read a parameter, e.g. group 1, number 29 for pressure."""
        self._validate_parameter(group, number)
        # SI = 0x0F (read); semicolon = 0x3B (separator).
        message = f"\x0f{group};{number}".encode("ascii")
        return self._exchange(message)

    def write_parameter(self, group, number, value):
        """Write a parameter (use only with documented writable parameters)."""
        self._validate_parameter(group, number)
        if not isinstance(value, (str, int, float)) or isinstance(value, bool):
            raise ValueError("Parameter value must be text or a number")
        text = str(value)
        if not text or any(ord(ch) < 32 or ord(ch) > 126 for ch in text):
            raise ValueError("Parameter value must contain printable ASCII")
        # SO = 0x0E (write); trailing space is required by the write frame.
        message = f"\x0e{group};{number};{text} ".encode("ascii")
        return self._exchange(message)  # Returns an empty string on ACK.

    # ---------------------------------------------------------------
    # 3. CONVENIENCE FUNCTIONS
    # ---------------------------------------------------------------

    def get_pressure(self):
        """Read channel 1 pressure as float, in the device's configured unit.

        Group 1 = channel 1; parameter 29 = rounded, unit-corrected pressure.
        Reference: manual, table 71, page 103.
        """
        value = self.read_parameter(1, 29)
        try:
            pressure = float(value)
        except ValueError as exc:
            raise GraphixError(f"No numeric pressure value: {value!r}") from exc
        if not math.isfinite(pressure):
            raise GraphixError(f"Invalid pressure value: {value!r}")
        return pressure
