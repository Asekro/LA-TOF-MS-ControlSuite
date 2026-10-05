"""Provide a minimal starting point for device classes."""


class BaseDevice:
    """Store a device name without opening a hardware connection."""

    def __init__(self, name: str) -> None:
        self.name = name
