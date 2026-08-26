# Uitwerking 9.1

## Hoe werkt de code?

De Pipeline zorgt dat scaling alleen op de trainingsdata wordt geleerd en daarna identiek op testdata wordt toegepast. Dit vermindert het risico op leakage en voorkomt verschillen tussen notebook en productiecode.


## Verwachte uitvoer

De exacte accuracy is reproduceerbaar door random_state=42.


## Controleer je uitkomst

- De testdata wordt niet gebruikt tijdens fit.
- Preprocessing staat in dezelfde pipeline als het model.
- De datasetverdeling blijft door stratify vergelijkbaar.

## Verdiepingsopdracht

Voeg cross-validation en een confusion matrix toe.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
