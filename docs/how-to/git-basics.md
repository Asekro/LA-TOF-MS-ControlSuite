# Git-Grundlagen

Alle Befehle werden im Terminal im Projektordner ausgeführt. Ein Commit ist ein
gespeicherter Stand ausgewählter Änderungen. Ein Branch ist ein eigener Arbeitszweig.

## `git status`: aktuellen Zustand prüfen

Zeigt den aktuellen Branch sowie neue und geänderte Dateien:

```powershell
git status
```

`Untracked files` sind neue Dateien. `Changes to be committed` sind bereits für den
nächsten Commit vorgemerkte Änderungen.

## `git pull`: Änderungen herunterladen

Holt Änderungen vom verbundenen Remote und übernimmt sie in den aktuellen Branch:

```powershell
git switch main
git pull --ff-only
```

`--ff-only` verhindert einen unbeabsichtigten Merge-Commit. Wenn Git dabei abbricht,
zuerst die abweichenden lokalen Änderungen prüfen. Vor einem Pull eigene Änderungen
committen. Pull und Push funktionieren erst nach Einrichtung eines Remotes und
einer Branch-Verknüpfung; im frisch angelegten Projekt ist noch kein Remote eingerichtet.

## `git add`: Änderungen für den Commit auswählen

Eine Datei oder nach Prüfung alle Änderungen vormerken:

```powershell
git add README.md
git add .
```

Die zweite Zeile ist eine Alternative, wenn alle Änderungen in den Commit gehören.
Ignorierte Dateien wie `.venv` werden dabei nicht aufgenommen.

## `git commit`: ausgewählte Änderungen speichern

```powershell
git commit -m "Add initial project structure"
```

Die Nachricht beschreibt kurz die Änderung. Ein Commit speichert den Stand lokal.
Falls Git nach Name und E-Mail fragt, einmalig für dieses Repository setzen:

```powershell
git config user.name "Dein Name"
git config user.email "deine-adresse@example.com"
```

## `git push`: Commits hochladen

Den neuen Branch erstmals zum Remote `origin` hochladen und verknüpfen:

```powershell
git push -u origin feature/device-example
```

Für weitere Commits auf diesem Branch genügt `git push`.

## `git switch`: zu einem bestehenden Branch wechseln

```powershell
git switch main
```

Vorher `git status` prüfen und eigene Änderungen committen, damit sie beim Wechsel
nicht versehentlich auf einem anderen Branch weiterbearbeitet werden.

## `git switch -c`: neuen Branch erstellen und wechseln

Nach dem Aktualisieren von `main`:

```powershell
git switch -c feature/device-example
```

Vor dem ersten Branch-Wechsel im frisch initialisierten Projekt muss mindestens
ein Commit auf `main` existieren.

## `git log`: bisherige Commits ansehen

```powershell
git log --oneline -5
```

Zeigt die letzten fünf Commits mit kurzer Kennung und Nachricht. Bei der längeren
Ansicht mit `git log` kann die Anzeige gegebenenfalls mit `q` geschlossen werden.
