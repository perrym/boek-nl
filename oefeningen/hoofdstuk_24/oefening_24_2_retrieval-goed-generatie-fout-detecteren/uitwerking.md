# Uitwerking 24.2

## Hoe werkt de code?

Het juiste document is opgehaald, dus retrieval werkt voor deze vraag. Toch neemt de generator 90 in plaats van 30 over. Wanneer alleen de eindscore wordt bekeken, is onduidelijk waar de fout ontstaat. Gescheiden metrics maken gerichte verbetering mogelijk.


## Verwachte uitvoer

Retrieval hit is True, answer exact is False en de conclusie is generatiefout.


## Controleer je uitkomst

- Retrieval en generatie worden afzonderlijk gelogd.
- Het uiteindelijke antwoord toont bronnen.
- Getallen en kritieke feiten krijgen extra verificatie.

## Verdiepingsopdracht

Gebruik een reguliere expressie om getallen uit bron en antwoord te vergelijken.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
