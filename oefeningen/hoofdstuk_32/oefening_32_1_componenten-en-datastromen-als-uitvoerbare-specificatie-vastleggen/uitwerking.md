# Uitwerking 32.1

## Hoe werkt de code?

Een architectuur wordt beter controleerbaar wanneer belangrijke eigenschappen als machineleesbare objecten zijn vastgelegd. De code controleert automatisch of componenten een eigenaar en classificatie hebben en of datastromen versleuteld zijn. Zulke controles kunnen later onderdeel worden van een architectuur- of CI/CD-pipeline.

Encryptie is slechts één basiscontrole. In een productieomgeving moeten per datastroom ook authenticatie, autorisatie, dataminimalisatie, logging en bewaartermijnen worden beoordeeld.


## Verwachte uitvoer

De uitvoer toont de bewust aangebrachte architectuurfouten, zodat zichtbaar wordt dat de controles daadwerkelijk werken


## Controleer je uitkomst

- Alle componenten hebben een eigenaar.
- Gevoelige datastromen zijn versleuteld.
- De LLM ontvangt alleen context waarvoor de gebruiker is geautoriseerd..

## Verdiepingsopdracht

Teken de objecten met networkx en voeg trust boundaries toe.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
