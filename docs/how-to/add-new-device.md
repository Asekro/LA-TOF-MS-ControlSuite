# Ein neues Gerät hinzufügen

1. Eine Datei unter `src/la_tof_ms/devices/` anlegen, zum Beispiel
   `example_device.py`. Datei- und Modulnamen auf Englisch und in `snake_case` wählen.
2. Eine eigene Geräteklasse erstellen, zum Beispiel `ExampleDevice`.
3. In `__init__` die benötigten Einstellungen speichern, etwa Gerätename oder
   Anschlussadresse. Benötigte Verbindungen erst ergänzen, wenn das konkrete Gerät
   bekannt ist.
4. Fundamentale Funktionen ergänzen. Jede Methode bildet einen einfachen
   Gerätebefehl ab, zum Beispiel einen einzelnen Messwert lesen.
5. Komfortfunktionen ergänzen, wenn sie benötigt werden. Diese dürfen mehrere
   fundamentale Funktionen zu einem verständlichen Ablauf kombinieren.
6. Unter `docs/devices/` eine passende deutsche Dokumentation anlegen. Gerät,
   Anschluss, Voraussetzungen und unterstützte Funktionen beschreiben.

Ein einfacher Ausgangspunkt, noch ohne Gerätekommunikation:

```python
class ExampleDevice:
    """Store settings for a future device integration."""

    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address

    # Fundamental device functions will be added here.

    # Convenience functions will be added here when needed.
```

`base_device.py` enthält lediglich eine einfache Grundlage. Neue Geräte müssen
vorerst nicht davon erben. Quellcode, Kommentare und Docstrings bleiben auf Englisch.
Gerätebefehle gehören in die Geräteklasse, damit die GUI später auch mit simulierten
Geräten arbeiten kann. Eine Simulation wird jetzt noch nicht eingebaut.

Vor einer GUI-Anbindung die benötigten Funktionen einzeln überprüfen und später
passende Tests unter `tests/` ergänzen. Siehe
[ADR-002](../architecture/ADR-002-device-interface.md).
