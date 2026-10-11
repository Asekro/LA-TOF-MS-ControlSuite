# ADR-005: Gerätekonfiguration

## Status
Accepted

## Kontext
Geräte benötigen Verbindungsparameter. Einige sind gerätespezifisch, andere hängen vom verwendeten Computer oder Aufbau ab.

## Entscheidung
- **Gerätespezifische Standardwerte** (Baudrate, Daten-Bits, Parität, Stop-Bits, Handshake) werden im Treiber definiert.
- **Installationsabhängige Werte** (z. B. COM-Port) werden von außen übergeben.
- Sinnvolle Standardwerte (z. B. Baudrate und Timeout) können bei der Initialisierung überschrieben werden.
- Eine spätere GUI oder Konfigurationsdatei kann diese Werte zentral verwalten.

## Begründung
Die Treiber bleiben einfach und unabhängig vom verwendeten Computer. Änderungen an der Gerätekonfiguration erfordern keine Anpassung des Treibercodes.
