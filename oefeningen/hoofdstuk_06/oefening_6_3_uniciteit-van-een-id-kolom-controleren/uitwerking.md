# Uitwerking 6.3

## Hoe werkt de code?

duplicated(keep=False) markeert alle voorkomens van een dubbele waarde. Daardoor zie je niet alleen de tweede rij, maar ook de eerste rij waarmee deze botst. Een niet-nul exitcode is bruikbaar in een pipeline, omdat de verwerking dan automatisch kan worden geblokkeerd.


## Verwachte uitvoer

Het script toont beide rijen met ID 1002 en de rij zonder ID. Daarna eindigt het met exitcode 1.


## Controleer je uitkomst

- Alle voorkomens van duplicaten worden getoond.
- Lege ID’s gelden als fout.
- De controle kan een pipeline laten falen.

## Verdiepingsopdracht

Vervang SystemExit door een eigen DataQualityError-exception en schrijf een unit test.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
