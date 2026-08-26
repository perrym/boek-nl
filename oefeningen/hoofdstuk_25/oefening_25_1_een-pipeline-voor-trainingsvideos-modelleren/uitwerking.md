# Uitwerking 25.1

## Hoe werkt de code?

Multimodale verwerking is beheersbaarder wanneer iedere modaliteit en transformatie expliciet is. Dan kun je per stap kwaliteit, kosten, fouten en autorisatie controleren. In productie moeten tijdelijke audio en frames volgens bewaartermijnen worden verwijderd.


## Verwachte uitvoer

Voor iedere pipeline-stap wordt een logrecord met tijd en status getoond.


## Controleer je uitkomst

- Persoonsgegevens in beeld en audio worden vooraf beoordeeld.
- Tijdelijke bestanden hebben een bewaartermijn.
- Fouten in een stap leiden niet tot oncontroleerbare vervolgoutput.

## Verdiepingsopdracht

Voeg duur, modelversie en een content-hash toe.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
