# Uitwerking 26.1

## Hoe werkt de code?

Een tool die alleen openbare informatie leest heeft een ander risicoprofiel dan een tool die accounts verwijdert. De score is een startpunt. Authenticatie, autorisatie, scope, transactielimieten en menselijke goedkeuring moeten als afzonderlijke controls worden ontworpen.


## Verwachte uitvoer

Account verwijderen krijgt de hoogste score. Documentatie zoeken krijgt de laagste.


## Controleer je uitkomst

- Toolrechten volgen least-privilege.
- Schrijfacties zijn traceerbaar.
- Niet-omkeerbare acties hebben extra goedkeuring.

## Verdiepingsopdracht

Voeg een kolom "menselijke goedkeuring vereist" toe op basis van klasse en actie.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
