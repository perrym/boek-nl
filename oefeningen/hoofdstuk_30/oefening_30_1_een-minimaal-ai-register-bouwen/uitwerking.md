# Uitwerking 30.1

## Hoe werkt de code?

en AI-register maakt zichtbaar waar AI wordt gebruikt, met welk doel, door wie en met welk risicoprofiel. De twee assert-controles bewaken twee eenvoudige basisvoorwaarden: iedere applicatie-ID moet uniek zijn en iedere toepassing moet een eigenaar hebben.

Een AI-register is geen eenmalige inventaris. Het moet worden bijgewerkt bij bijvoorbeeld modelwijzigingen, nieuwe databronnen, gewijzigde risico's, incidenten en relevante veranderingen in wet- en regelgeving.


## Verwachte uitvoer

De twee geregistreerde AI-toepassingen worden weergegeven. Omdat de applicatie-ID's uniek zijn en beide toepassingen een eigenaar hebben, slagen de basisvalidaties.


## Controleer je uitkomst

- Iedere toepassing heeft een unieke applicatie-ID.
- Iedere toepassing heeft een eigenaar.
- Doel, model, dataclassificatie en risicoklasse zijn vastgelegd.
- De laatste reviewdatum is geregistreerd.

## Verdiepingsopdracht

Voeg een controle toe die waarschuwt wanneer de laatste review ouder is dan 365 dagen. Voeg daarna eventueel velden toe voor modelversie, dataversie en status.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
