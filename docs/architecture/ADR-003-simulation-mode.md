# ADR-003: Simulationsmodus

## Status
Accepted

## Kontext
Die Laborhardware ist während der Entwicklung nicht immer verfügbar.
GUI und Programmabläufe sollen später auch ohne angeschlossene Geräte testbar sein.

## Entscheidung
Die Architektur soll langfristig einen Simulationsmodus ermöglichen.
Gerätekommunikation wird in den Geräteklassen gebündelt, sodass später simulierte
Antworten ergänzt werden können. Dieses ADR dokumentiert zunächst nur die Entscheidung;
eine Simulation wird jetzt noch nicht implementiert.

## Begründung
Die Entwicklung von GUI und Messabläufen wird unabhängiger von der Verfügbarkeit
der Apparatur. Der konkrete Aufbau wird erst bei Bedarf festgelegt.
