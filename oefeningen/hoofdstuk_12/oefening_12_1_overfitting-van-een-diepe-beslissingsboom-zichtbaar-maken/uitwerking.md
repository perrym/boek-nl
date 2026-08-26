# Uitwerking 12.1

## Hoe werkt de code?

Een diepe boom kan trainingsvoorbeelden bijna uit het hoofd leren. De trainingsscore stijgt dan naar 1, terwijl de testscore stabiliseert of daalt. Het verschil tussen beide lijnen is een generalisatiekloof. De optimale diepte moet met validatie worden gekozen en niet met de test set.


## Verwachte uitvoer

Bij grotere dieptes wordt de trainingsscore zeer hoog. De testscore bereikt eerder een maximum en kan daarna dalen.


## Controleer je uitkomst

- De testset wordt niet gebruikt om hyperparameters definitief te kiezen.
- random_state maakt de proef reproduceerbaar.
- Naast accuracy worden bij onbalans andere metrics bekeken.

## Verdiepingsopdracht

Herhaal met min_samples_leaf en vergelijk de generalisatiekloof.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
