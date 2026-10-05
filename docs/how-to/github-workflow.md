# Einfacher GitHub-Workflow

Dieser Ablauf setzt einen ersten Commit auf `main`, ein GitHub-Repository und ein
Remote namens `origin` voraus. Im neu angelegten Projekt wurde noch kein Remote
verbunden und nichts gepusht. Git-Befehle im Projektordner ausführen.

1. **`main` aktualisieren.** Zuerst sicherstellen, dass keine ungespeicherten
   Änderungen vorliegen:

   ```powershell
   git status
   git switch main
   git pull --ff-only
   ```

2. **Neuen Branch erstellen.** Einen kurzen Namen für die geplante Änderung wählen:

   ```powershell
   git switch -c feature/device-example
   ```

3. **Änderungen durchführen.** Dateien in VS Code bearbeiten und speichern.
   Passende Dokumentation ebenfalls aktualisieren.

4. **Änderungen testen.** Für den aktuellen GUI-Platzhalter die Umgebung aktivieren
   und das Fenster starten; anschließend wieder schließen:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   $env:PYTHONPATH = "$PWD\src"
   python -m la_tof_ms.main
   ```

   Für spätere Änderungen zusätzlich passende Funktionstests durchführen.
   [Hinweise zu Tests](../../tests/README.md).

5. **Status und Änderungen prüfen.**

   ```powershell
   git status
   git diff
   ```

   Neue Dateien zusätzlich im Editor prüfen; `git diff` zeigt sie vor `git add`
   noch nicht an. Keine lokalen Umgebungen oder Zugangsdaten aufnehmen.

6. **Änderungen committen.** Die gewünschten Dateien vormerken, prüfen und speichern:

   ```powershell
   git add .
   git diff --cached
   git commit -m "Add device example"
   ```

7. **Branch pushen.**

   ```powershell
   git push -u origin feature/device-example
   ```

8. **Pull Request auf GitHub erstellen.** Im Repository auf GitHub den gepushten
   Branch auswählen und einen Pull Request mit Zielbranch `main` öffnen.
   Kurz beschreiben, was geändert und getestet wurde.

9. **Pull Request prüfen und in `main` mergen.** Änderungen auf GitHub durchsehen,
   offene Fragen klären und den Pull Request anschließend über die Merge-Schaltfläche
   übernehmen. Dafür ist kein weiterer lokaler Git-Befehl nötig.

10. **Lokal zu `main` wechseln und aktualisieren.**

    ```powershell
    git switch main
    git pull --ff-only
    git status
    ```

    Die nächste Änderung beginnt wieder bei Schritt 1 mit einem neuen Branch.
