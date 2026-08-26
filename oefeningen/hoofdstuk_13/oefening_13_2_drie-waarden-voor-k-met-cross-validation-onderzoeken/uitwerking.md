# Uitwerking 13.2

## Hoe werkt de code?

Een kleine k maakt het model flexibel en mogelijk gevoelig voor ruis. Een grote k maakt de beslisgrens gladder, maar kan lokale patronen missen. De standaardafwijking laat zien of de prestatie stabiel is over folds. Kies niet automatisch de hoogste score wanneer het verschil verwaarloosbaar is.


## Verwachte uitvoer

De tabel toont voor k=3, 5 en 9 de gemiddelde F1-score en spreiding.


## Controleer je uitkomst

- Dezelfde cross-validationmethode wordt gebruikt.
- De metric past bij de klasseverdeling.
- De uiteindelijke testset blijft apart.

## Verdiepingsopdracht

Gebruik GridSearchCV voor k van 1 tot en met 25 en plot de resultaten.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
