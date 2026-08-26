# Uitwerking 21.1

## Hoe werkt de code?

F-IDF is geen moderne embeddingtechniek, maar een eenvoudige manier om tekst om te zetten in getallen. Daarbij krijgen woorden een hogere waarde wanneer ze belangrijk zijn in een document, maar niet in alle documenten even vaak voorkomen. De vraag en de tekstfragmenten worden zo voorgesteld als vectoren.

Met cosine similarity wordt vervolgens berekend hoe sterk de vector van de vraag lijkt op de vector van ieder tekstfragment. Hoe hoger de score, hoe groter de woordelijke overeenkomst.

Daarna selecteert top-k de k best scorende tekstfragmenten, bijvoorbeeld de twee meest relevante stukken. Deze vormen de context die later aan een taalmodel kan worden meegegeven.

Een echte RAG-oplossing gaat meestal verder. Daarin worden vaak moderne embeddings gebruikt om ook betekenisverwantschap te herkennen, worden bron metadata en toegangsrechten meegenomen en wordt de geselecteerde context uiteindelijk door een taalmodel gebruikt om een antwoord te genereren.


## Verwachte uitvoer

De MFA-chunk hoort bovenaan te staan. De tweede uitkomst kan door woordoverlap minder relevant zijn.


## Controleer je uitkomst

- Bronrechten worden voor retrieval afgedwongen.
- Top-k is getest en niet willekeurig gekozen.
- Geen antwoord wordt gegenereerd zonder voldoende context.

## Verdiepingsopdracht

Voeg een minimale score van 0,15 toe en geef een onbekendmelding wanneer niets voldoet.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
