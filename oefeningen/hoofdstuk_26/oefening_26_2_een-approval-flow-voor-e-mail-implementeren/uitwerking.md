# Uitwerking 26.2

## Hoe werkt de code?

De agent mag een concept maken, maar de uiteindelijke actie wordt door een lokale control afgedwongen. Alleen in de prompt schrijven dat goedkeuring nodig is, is onvoldoende. De echte tool moet weigeren wanneer het goedkeuringsattribuut ontbreekt.


## Verwachte uitvoer

De eerste verzendpoging wordt geblokkeerd. Na goedkeuring volgt alleen een gesimuleerde verzending.


## Controleer je uitkomst

- Goedkeuring is gekoppeld aan de exacte inhoud.
- Wijziging na goedkeuring maakt de goedkeuring ongeldig.
- Ontvanger en bijlagen worden apart gecontroleerd.

## Verdiepingsopdracht

Voeg een SHA-256-hash van ontvanger, onderwerp en tekst toe aan het goedkeuringsrecord.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
