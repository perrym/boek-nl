# Uitwerking 8.2

## Hoe werkt de code?

De afsluitcode wordt pas na de afhandeling bekend en mag dus niet worden gebruikt om vooraf escalatie te voorspellen. Een zeer hoge score kan daardoor misleidend zijn. Leakage wordt niet alleen door kolomnamen ontdekt. Je moet ook weten wanneer en hoe iedere feature ontstaat.


## Verwachte uitvoer

De score met leakage is zeer hoog en meestal hoger dan de score zonder de verdachte feature.


## Controleer je uitkomst

- De feature is op voorspeltijd beschikbaar.
- Cross-validation voorkomt dataleakage niet automatisch.
- De feature lineage wordt gedocumenteerd.

## Verdiepingsopdracht

Voeg een tweede leakage-feature toe, bijvoorbeeld einddatum, en maak een lijst met toegestane features.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
