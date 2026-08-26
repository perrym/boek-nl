# Uitwerking 27.1

## Hoe werkt de code?

Een graaf maakt zichtbaar welke agents met elkaar communiceren en waar resultaten samenkomen. Iedere agent heeft bij voorkeur één duidelijk afgebakende taak en alleen toegang tot de tools en informatie die daarvoor nodig zijn. De reviewer-agent kan resultaten van verschillende agents vergelijken en conflicten of ontbrekend bewijs signaleren, maar vervangt geen menselijke beoordeling.


## Verwachte uitvoer

De figuur toont de orchestrator als centraal coördinatiepunt. De specialistische agents leveren hun resultaten aan de reviewer, waarna de uitkomst teruggaat naar de orchestrator en uiteindelijk in een rapport kan worden verwerkt..


## Controleer je uitkomst

- De orchestrator vormt het centrale coördinatiepunt.
- Specialistische agents hebben alleen de verbindingen die voor hun taak nodig zijn.
- De resultaten van de specialistische agents komen samen bij de reviewer.
- Je kunt in de graaf volgen hoe informatie van de gebruiker naar het uiteindelijke rapport stroomt.

## Verdiepingsopdracht

Voeg externe systemen en trust boundaries als aparte nodes toe. Leg vervolgens per verbinding vast welke informatie mag worden uitgewisseld en simuleer één foutpad, bijvoorbeeld een agent die geen resultaat teruggeeft.

Opmerking: deze oefening simuleert alleen de architectuur. Er worden geen echte AI-agents of taalmodellen aangeroepen en er is geen API-key nodig.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
