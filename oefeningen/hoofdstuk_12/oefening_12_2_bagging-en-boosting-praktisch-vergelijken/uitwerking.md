# Uitwerking 12.2

## Hoe werkt de code?

Random forest traint veel bomen relatief onafhankelijk op bootstrap-samples. Dat is bagging en vermindert variantie. Gradient boosting bouwt modellen na elkaar, waarbij ieder nieuw model eerdere fouten probeert te corrigeren. Dat kan krachtig zijn, maar is gevoeliger voor instellingen en kan minder parallel worden getraind.


## Verwachte uitvoer

Beide modellen tonen een gemiddelde F1-score en uitvoeringstijd. De precieze winnaar hangt af van data en instellingen.


## Controleer je uitkomst

- Dezelfde folds en metric worden gebruikt.
- Trainingstijd is niet de enige operationele maatstaf.
- Modelcomplexiteit en uitlegbaarheid worden meegewogen.

## Verdiepingsopdracht

Voeg AdaBoost toe en vergelijk ook modelgrootte na serialisatie met joblib.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
