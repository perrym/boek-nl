# Uitwerking 1.2

## Hoe werkt de code?

De code berekent de financiële gevolgen van twee soorten fouten: false positives en false negatives. Voor ieder scenario wordt het aantal fouten vermenigvuldigd met de kosten per fouttype. Daarna worden deze bedragen bij elkaar opgeteld.

Scenario B heeft minder false positives, maar meer false negatives. Omdat een gemist fraudegeval in dit voorbeeld veel duurder is dan een onterechte fraudemelding, zijn de totale kosten van scenario B hoger. Dit laat zien dat bij de beoordeling van een model niet alleen naar het aantal fouten of een algemene metric zoals accuracy moet worden gekeken, maar ook naar de impact van verschillende soorten fouten.

In een echte toepassing spelen naast financiële schade ook juridische, operationele en reputatierisico's een rol.

Uitvoer

Scenario A: EUR 23,000

Scenario B: EUR 41,000

Scenario A kost €23.000 en scenario B €41.000. Scenario B heeft in dit voorbeeld dus het grootste geschatte financiële risico.


## Controleer je uitkomst

- Kosten per fouttype zijn expliciet vastgelegd.
- De conclusie volgt uit de berekening en niet uit gevoel.
- Niet-financiële impact wordt apart benoemd.

## Verdiepingsopdracht

Voeg een derde scenario toe. Bereken ook voor dit scenario de totale kosten en maak daarna met Python een staafdiagram waarin je de kosten van de drie scenario's vergelijkt.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
