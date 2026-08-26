# Uitwerking 27.2

## Hoe werkt de code?

Observability maakt prestaties en gebeurtenissen binnen een systeem traceerbaar. Het volledig loggen van prompts of gebruikersinput kan nieuwe privacy- en beveiligingsrisico's veroorzaken. In dit voorbeeld wordt daarom alleen een SHA-256-hash van de invoer opgeslagen. Een hash kan helpen om invoer te vergelijken zonder de oorspronkelijke tekst rechtstreeks op te slaan, maar vervangt geen goede toegangscontrole en dataminimalisatie..


## Verwachte uitvoer

Het script print een JSON-event met een unieke trace-ID en een SHA-256-hash.


## Controleer je uitkomst

- De volledige gebruikersinput wordt niet opgeslagen.
- Het event bevat een unieke trace-ID.
- Agent, actie, status, duur, modelversie en tokenaantallen zijn opgenomen.
- De uitvoer is geldige JSON.

## Verdiepingsopdracht

Maak een tweede event met dezelfde trace-ID en simuleer daarin een fout. Voeg vervolgens een error_type en een herstelactie toe.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
