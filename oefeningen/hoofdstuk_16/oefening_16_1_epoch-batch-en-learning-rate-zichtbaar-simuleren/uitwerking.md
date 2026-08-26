# Uitwerking 16.1

## Hoe werkt de code?

Een epoch is hier een volledige update-ronde. De learning rate bepaalt de stapgrootte. Bij 0,1 beweegt het gewicht geleidelijk naar 3. Bij een te hoge learning rate kan het gewicht heen en weer schieten of verder van het doel raken. In echte neurale netwerken wordt een batch gebruikt om de gradient op een deel van de voorbeelden te schatten.


## Verwachte uitvoer

De rustige learning rate verlaagt de loss. De hoge learning rate veroorzaakt instabiel gedrag.


## Controleer je uitkomst

- De loss wordt na iedere update berekend.
- Dezelfde startwaarde maakt de vergelijking eerlijk.
- Een analogie wordt gekoppeld aan de echte berekening.

## Verdiepingsopdracht

Voeg een batch_size-parameter toe en simuleer ruis in de gradient.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
