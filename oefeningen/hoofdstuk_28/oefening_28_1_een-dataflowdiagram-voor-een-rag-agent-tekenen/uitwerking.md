# Uitwerking 28.1

## Hoe werkt de code?

Het diagram maakt zichtbaar welke onderdelen met elkaar communiceren en welke componenten intern of extern zijn. De LLM-provider en de ontvanger zijn externe entiteiten. Dit betekent dat gegevens bij communicatie met deze componenten de interne omgeving kunnen verlaten. Daarom is extra aandacht nodig voor dataminimalisatie, autorisatie en controle op uitgaande gegevens.

De e-mailtool voert bovendien een actieve handeling uit. Daarom moet deze niet automatisch dezelfde rechten krijgen als componenten die alleen documenten ophalen of doorzoeken.


## Verwachte uitvoer

De figuur toont de belangrijkste onderdelen van de RAG-agent en de gerichte datastromen tussen deze onderdelen. Bij iedere component is zichtbaar of deze intern of extern is.


## Controleer je uitkomst

- Alle beschreven componenten zijn als node opgenomen.
- Interne en externe componenten zijn herkenbaar gemarkeerd.
- De belangrijkste datastromen zijn als gerichte verbindingen weergegeven.
- De LLM-provider en ontvanger zijn als externe componenten herkenbaar.
- De route van de gebruiker via de RAG-agent naar de verschillende componenten is in het diagram te volgen.

## Verdiepingsopdracht

Breid het diagram uit met trust boundaries en geef bij kritieke datastromen aan welke gegevens worden overgedragen. Voeg daarna per kritieke verbinding minimaal één STRIDE-dreiging en een bijpassende technische maatregel toe.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
