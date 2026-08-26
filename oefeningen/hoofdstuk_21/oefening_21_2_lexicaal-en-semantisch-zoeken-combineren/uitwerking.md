# Uitwerking 21.2

## Hoe werkt de code?

Lexicaal zoeken is sterk bij exacte termen, productcodes en controlereferenties. Semantisch zoeken vindt verwante formuleringen, zoals "alleen eigen record" bij objectautorisatie. Hybrid search combineert beide signalen. De gewichten moeten met echte vragen worden geëvalueerd.


## Verwachte uitvoer

De chunk met de exacte term BOLA krijgt een extra lexicale bijdrage en hoort bovenaan.


## Controleer je uitkomst

- Scores worden eerst op vergelijkbare schaal gebracht.
- Gewichten zijn getest met een evaluatieset.
- Exacte termmatches overschrijven geen autorisatie.

## Verdiepingsopdracht

Gebruik meerdere zoektermen en voeg een bonus toe voor actuele documenten.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
