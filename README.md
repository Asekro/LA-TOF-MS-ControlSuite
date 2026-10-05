# LA-TOF-MS-ControlSuite

Die LA-TOF-MS-ControlSuite ist ein Python-Projekt zur Steuerung und Automatisierung
einer LA-TOF-MS-Apparatur. Verschiedene Laborgeräte sollen über eigene Python-Klassen
angebunden werden. Langfristig entstehen eine gemeinsame GUI und automatisierte
Messabläufe. Ein späterer Simulationsmodus soll die Entwicklung ohne Hardware erlauben.

Aktuell enthält das Projekt nur ein einfaches GUI-Fenster und einen Platzhalter für
Geräteklassen. Gerätekommunikation und Simulation sind noch nicht implementiert.

## Entwicklungsumgebung einrichten

Voraussetzungen: Python (erstellt und geprüft mit Python 3.12), Git und VS Code mit
der Python-Erweiterung. Im Projektordner in einem PowerShell-Terminal:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Die bereits angelegte `.venv` kann direkt aktiviert werden. In VS Code über
`Python: Select Interpreter` den Interpreter `.venv\Scripts\python.exe` auswählen.
Details und eine Alternative ohne Aktivierung stehen in der
[Einrichtungsanleitung](docs/how-to/setup-development-environment.md).

## Anwendung starten

Mit aktivierter Umgebung, aus dem Projektordner:

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m la_tof_ms.main
```

Das Fenster kann über das normale Schließen-Symbol beendet werden. `src` wird für
diese Terminalsitzung zum Python-Suchpfad hinzugefügt; ein zusätzliches Paketierungs-
oder Build-System ist für den aktuellen Projektstart nicht nötig.

## Orientierung

- `src/la_tof_ms/`: Quellcode für Programmstart, Geräte, GUI und spätere Hilfsfunktionen.
- [Architekturentscheidungen](docs/architecture/README.md): kurze ADRs.
- [Git-Grundlagen](docs/how-to/git-basics.md) und [GitHub-Workflow](docs/how-to/github-workflow.md).
- [Neues Gerät hinzufügen](docs/how-to/add-new-device.md) und [Gerätedokumentation](docs/devices/README.md).
- [Tests](tests/README.md): Hinweise für spätere Tests.

Dokumentation wird auf Deutsch geschrieben, Quellcode einschließlich Kommentaren
und Docstrings auf Englisch. `.venv` und lokale Cache-Dateien werden von Git ignoriert.
