# Tests

Hier werden später Tests für Gerätefunktionen und Programmabläufe abgelegt.
Aktuell gibt es noch keine automatisierten Testdateien und keine zusätzliche
Testbibliothek. Für den Projektstart genügen eine Syntaxprüfung und ein kurzer
Start der Platzhalter-GUI.

## Python-Syntax prüfen

Aus dem Projektordner, ohne Cache-Dateien zu erzeugen:

```powershell
.\.venv\Scripts\python.exe -c "import ast, pathlib; files = list(pathlib.Path('src').rglob('*.py')); [ast.parse(p.read_text(encoding='utf-8'), filename=str(p)) for p in files]; print(f'{len(files)} Python files: syntax OK')"
```

## GUI manuell prüfen

Nach Installation der Abhängigkeiten:

```powershell
$env:PYTHONPATH = "$PWD\src"
.\.venv\Scripts\python.exe -m la_tof_ms.main
```

Prüfen, ob das Fenster mit Titel und Platzhaltertext erscheint und sich wieder
schließen lässt. Es wird keine Hardware angesprochen. Für neue Funktionen später
geeignete Tests ergänzen; dafür kann zunächst Pythons eingebautes `unittest` dienen.
