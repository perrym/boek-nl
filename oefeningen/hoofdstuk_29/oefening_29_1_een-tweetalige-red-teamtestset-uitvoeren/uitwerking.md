# Uitwerking 29.1

## Hoe werkt de code?

De testharness maakt herhaalbare tests en systematische bewijsopbouw mogelijk. Gebruik uitsluitend synthetische canarywaarden en nooit echte secrets. Een veilige weigering is een positief resultaat, maar controleer ook toolcalls, logs, netwerkverkeer en eventuele gedeeltelijke datalekken.


## Verwachte uitvoer

Alle tests leiden tot een veilige weigering en tonen geen lekkage van canarywaarden. Canarywaarden zijn bewust toegevoegde herkenbare testgegevens waarmee kan worden gecontroleerd of gevoelige informatie onbedoeld uit het systeem lekt.


## Controleer je uitkomst

- Tests draaien in een afgescheiden omgeving.
- Er worden geen echte persoonsgegevens of sleutels gebruikt.
- Resultaten bevatten prompt, antwoord, toolcalls en timestamp.

## Verdiepingsopdracht

Lees tests uit een CSV-bestand en schrijf resultaten als JSON Lines.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
