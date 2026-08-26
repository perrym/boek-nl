# Uitwerking 5.3

## Hoe werkt de code?

Een slice is vaak een view op hetzelfde geheugen. De wijziging view[0] = 999 verandert daarom ook origineel[1]. De echte kopie heeft eigen geheugen, waardoor kopie[1] = 777 het origineel niet wijzigt. Dit is belangrijk bij datapreprocessing, omdat onbedoelde mutaties moeilijk te vinden fouten veroorzaken.


## Verwachte uitvoer

Origineel bevat 999 op de tweede positie, maar bevat geen 777. De 777 staat alleen in de kopie.


## Controleer je uitkomst

- Het effect van de view is zichtbaar in het origineel.
- De kopie is onafhankelijk.
- De uitgangsarray wordt vooraf opnieuw aangemaakt.

## Verdiepingsopdracht

Gebruik np.shares_memory om programmatisch te controleren of arrays geheugen delen.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
