# Entwicklungsumgebung unter Windows und VS Code

Voraussetzungen: Python (dieses Projekt wurde mit Python 3.12 eingerichtet), Git
und VS Code mit der Python-Erweiterung von Microsoft. Befehle in PowerShell ausführen.

## 1. Repository klonen

Sobald das Projekt auf GitHub liegt, die Beispieladresse durch die tatsächliche
Repository-Adresse ersetzen:

```powershell
git clone https://github.com/DEIN-NAME/LA-TOF-MS-ControlSuite.git
cd LA-TOF-MS-ControlSuite
```

Wenn der Projektordner bereits lokal vorhanden ist, diesen direkt öffnen.
Der gerade erstellte Projektstand hat noch kein GitHub-Remote.

## 2. Projekt in VS Code öffnen

```powershell
code .
```

Alternativ in VS Code über **Datei > Ordner öffnen** den Projektordner wählen.
Dann über **Terminal > Neues Terminal** ein PowerShell-Terminal öffnen.

## 3. Virtuelle Umgebung erstellen und aktivieren

Im Projektordner:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Eine bereits vorhandene `.venv` muss nicht neu erstellt werden. Nach Aktivierung
erscheint üblicherweise `(.venv)` am Anfang der Terminalzeile. Die Umgebung wird von
Git ignoriert; jeder erstellt sie lokal selbst.

Falls PowerShell das Aktivierungsskript blockiert, kann die Umgebung auch ohne
Aktivierung direkt über `.\.venv\Scripts\python.exe` verwendet werden. Eine Änderung
der systemweiten Ausführungsrichtlinie ist dafür nicht nötig.

## 4. Python-Interpreter in VS Code auswählen

Mit `Strg+Umschalt+P` die Befehlspalette öffnen und `Python: Select Interpreter`
auswählen. Den Interpreter `.venv\Scripts\python.exe` verwenden. Falls er nicht
angezeigt wird, über **Enter interpreter path** die Datei auswählen.

## 5. Abhängigkeiten installieren

Mit aktivierter Umgebung:

```powershell
python -m pip install -r requirements.txt
```

Dies entspricht `pip install -r requirements.txt`; `python -m pip` stellt sicher,
dass pip zum ausgewählten Python gehört. Ohne Aktivierung:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Die Datei enthält nur PySide6, pyvisa und pyserial. pip installiert deren notwendige
Unterabhängigkeiten automatisch. Gerätespezifische Treiber werden erst bei der
Anbindung konkreter Hardware geklärt.

## 6. Platzhalter-GUI starten

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m la_tof_ms.main
```

Ohne Aktivierung die zweite Zeile durch
`.\.venv\Scripts\python.exe -m la_tof_ms.main` ersetzen.
Es erscheint ein einfaches Fenster ohne Gerätekommunikation.
Der Python-Suchpfad gilt nur für diese Terminalsitzung und muss in einem neuen
Terminal erneut gesetzt werden.

Mit `deactivate` kann eine aktivierte Umgebung im Terminal wieder verlassen werden.
