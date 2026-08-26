# Uitwerking 10.2

## Hoe werkt de code?

R-kwadraat vergelijkt de kwadratische fout van het model met de variatie rond het gemiddelde van de testwaarden. Een waarde van 1 betekent perfect, 0 betekent ongeveer gelijk aan steeds het testgemiddelde voorspellen en een negatieve waarde betekent slechter dan die eenvoudige baseline. In dit voorbeeld verandert de relatie tussen train en test. Dat lijkt op concept drift of een niet-representatieve trainingsset.


## Verwachte uitvoer

De R-kwadraat is sterk negatief, omdat het model een stijgende lijn heeft geleerd terwijl de testwaarden dalen. De MSE van het model is groter dan de MSE van de gemiddelde baseline.


## Controleer je uitkomst

- R-kwadraat wordt op ongeziene testdata berekend.
- Een baseline wordt expliciet vergeleken.
- Een negatieve score leidt tot onderzoek naar drift, datafouten en modelaannames.

## Verdiepingsopdracht

Maak een tweede dataset waarin train en test hetzelfde patroon volgen. Vergelijk beide R-kwadraatscores in een tabel.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
