# Uitwerking 22.2

## Hoe werkt de code?

Kleine chunks geven meestal specifiekere zoekresultaten, maar kunnen context over sectiegrenzen verliezen. Grote chunks bewaren meer samenhang, maar voegen mogelijk irrelevante tekst toe en kosten meer tokens. De beste keuze hangt af van documentstructuur, vraagtype en embeddingmodel.


## Verwachte uitvoer

De 200-woordinstelling produceert veel meer chunks dan de 1200-woordinstelling.


## Controleer je uitkomst

- Overlap is kleiner dan de chunkgrootte.
- Koppen en tabellen worden waar mogelijk structureel behandeld.
- De vergelijking gebruikt echte evaluatievragen.

## Verdiepingsopdracht

Voeg een functie toe die chunks bij koppen splitst en metadata met sectienaam bewaart.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
