# Uitwerking 15.2

## Hoe werkt de code?

Wanneer dezelfde klant in training en validatie voorkomt, kan het model klant-specifieke patronen herkennen in plaats van generaliseren naar nieuwe klanten. Gewone KFold voorkomt die dataleakage niet. GroupKFold houdt alle records van een groep bij elkaar.


## Verwachte uitvoer

Gewone KFold toont meestal veel overlappende klanten. GroupKFold toont telkens een lege overlaplijst.


## Controleer je uitkomst

- De groep vertegenwoordigt de echte afhankelijkheid.
- Er zijn genoeg groepen voor het aantal folds.
- De testset is zo nodig ook op groepen gescheiden.

## Verdiepingsopdracht

Vervang klant door tijdsperiode en vergelijk met TimeSeriesSplit.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
