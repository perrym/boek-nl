# Uitwerking 32.3

## Hoe werkt de code?

Harde blokkades mogen nooit worden gecompenseerd door een hoge gemiddelde kwaliteit. De functie verzamelt alle afwijkingen en geeft pas een GO wanneer geen blokkades of drempeloverschrijdingen meer aanwezig zijn. Drempels moeten vooraf zijn vastgesteld en mogen niet achteraf worden aangepast om een release alsnog mogelijk te maken. Restrisico dat niet automatisch kan worden beoordeeld, vereist expliciete menselijke goedkeuring.


## Verwachte uitvoer

Met de voorbeeldwaarden is het besluit “GO” en is de lijst met redenen leeg.


## Controleer je uitkomst

- Drempelwaarden zijn vooraf vastgesteld en goedgekeurd.
- Harde blokkades en kwaliteits- of performancedrempels zijn duidelijk onderscheiden.
- Restrisico is expliciet beoordeeld en goedgekeurd.
- Een GO vereist daarnaast duidelijk operationeel eigenaarschap en een getest rollbackmechanisme.

## Verdiepingsopdracht

Maak drie scenario's: GO, kwaliteit NO-GO en security NO-GO. Schrijf voor ieder scenario een unit test en controleer dat een securityblokkade nooit door hoge kwaliteit kan worden gecompenseerd.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
