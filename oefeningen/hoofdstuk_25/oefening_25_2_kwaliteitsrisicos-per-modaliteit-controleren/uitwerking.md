# Uitwerking 25.2

## Hoe werkt de code?

Kwaliteitsrisico's verschillen per modaliteit. Een beeld kan voldoende resolutie hebben maar gevoelige EXIF-metadata bevatten. Audio kan verstaanbaar lijken, maar een slechte signaal-ruisverhouding verhoogt transcriptiefouten. De controlelijst maakt gaten zichtbaar voordat de pipeline wordt vrijgegeven.


## Verwachte uitvoer

Bij beeld ontbreekt metadata en bij video ontbreekt tijdssynchronisatie.


## Controleer je uitkomst

- Controles hebben meetbare drempelwaarden.
- Onbekende of ongeldige input wordt veilig afgewezen.
- Menselijke review is beschikbaar bij lage confidence.

## Verdiepingsopdracht

Voeg prioriteit en automatisch blokkeren voor kritieke ontbrekende checks toe.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
