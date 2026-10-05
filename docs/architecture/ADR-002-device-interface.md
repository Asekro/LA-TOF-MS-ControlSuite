# ADR-002: Geräteschnittstelle

## Status
Accepted

## Kontext
Verschiedene Laborgeräte haben unterschiedliche Befehle und Verbindungen.
Der zugehörige Code soll leicht auffindbar und verständlich bleiben.

## Entscheidung
Laborgeräte werden durch eigene Python-Klassen gekapselt. Jede Geräteklasse wird
grundsätzlich in drei Bereiche gegliedert:

- Initialisierung: `__init__` speichert die benötigten Einstellungen.
- Fundamentale Gerätefunktionen: Methoden bilden einzelne einfache Gerätebefehle ab.
- Komfortfunktionen: Methoden dürfen mehrere fundamentale Funktionen kombinieren.

Es wird noch keine komplexe abstrakte Klassenhierarchie implementiert.
`base_device.py` enthält zunächst nur eine einfache Grundlage; Vererbung ist optional.

## Begründung
Gerätespezifischer Code bleibt an einem Ort. Einfache Befehle können wiederverwendet
und später zu verständlichen Abläufen kombiniert werden, ohne unnötige Abstraktionen.
