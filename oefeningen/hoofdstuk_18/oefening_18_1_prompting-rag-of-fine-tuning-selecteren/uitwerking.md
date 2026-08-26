# Uitwerking 18.1

## Hoe werkt de code?

De beslisregel is bewust eenvoudig. RAG is logisch wanneer externe of actuele kennis nodig is. Fine-tuning kan gedrag, formaat of stijl consistenter maken, maar is geen betrouwbare manier om vaak veranderende feiten bij te houden. Prompting is meestal de eerste en goedkoopste stap.


## Verwachte uitvoer

Scenario’s met actuele kennis krijgen RAG. Een vaste bekende taak kan fine-tuning krijgen. Overige scenario’s starten met prompting.


## Controleer je uitkomst

- De regel wordt gezien als startpunt en niet als automatisch besluit.
- Kosten, privacy en latency worden later toegevoegd.
- Eerst wordt een eenvoudige baseline getest.

## Verdiepingsopdracht

Maak een gewogen scoremodel met kosten, privacy, actualiteit en onderhoudbaarheid.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
