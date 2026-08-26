# Uitwerking 9.2

## Hoe werkt de code?

Bij weinig positieve voorbeelden kan een willekeurige testset te veel of te weinig positieven bevatten. stratify houdt de labelverdeling ongeveer gelijk. Het lost andere afhankelijkheden, zoals meerdere records van dezelfde klant, niet op. Daarvoor is groepssplitsing nodig.


## Verwachte uitvoer

Met stratify bevat de testset ongeveer 5 procent positieve records. Zonder stratify kan dit afwijken.


## Controleer je uitkomst

- Stratify gebruikt het label en niet een willekeurige feature.
- Groepsafhankelijkheden worden apart beoordeeld.
- De testset blijft groot genoeg voor betrouwbare metrics.

## Verdiepingsopdracht

Herhaal de split voor twintig random seeds en plot de positieve percentages.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
