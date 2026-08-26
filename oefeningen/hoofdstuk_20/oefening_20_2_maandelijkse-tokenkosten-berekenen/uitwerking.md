# Uitwerking 20.2

## Hoe werkt de code?

Input- en outputtokens hebben vaak verschillende tarieven. Een kostencalculator voorkomt dat alleen naar de prijs per verzoek wordt gekeken. Productiekosten omvatten daarnaast embeddings, opslag, logging, netwerk, monitoring, support en eventuele gereserveerde capaciteit.


## Verwachte uitvoer

Met de voorbeeldtarieven komt de berekening uit op EUR 675,00 per maand.


## Controleer je uitkomst

- Tarieven en datum worden vastgelegd.
- Piekgebruik en retry’s worden meegenomen.
- De berekening bevat een marge voor groei.

## Verdiepingsopdracht

Voeg caching toe: 40 procent van de inputtokens kost slechts 20 procent van het normale inputtarief.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
