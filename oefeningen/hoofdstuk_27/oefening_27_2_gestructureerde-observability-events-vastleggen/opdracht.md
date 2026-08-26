# Oefening 27.2 - Gestructureerde observability-events vastleggen

**Niveau:** Verdieping  
**Geschatte tijd:** 45 tot 75 minuten

## Doel

Per agentstap voldoende gegevens vastleggen voor monitoring en analyse, zonder gevoelige inhoud onnodig in logs op te nemen.

## Opdracht

Maak een logfunctie met een trace-ID, agentnaam, actie, duur, status, modelversie en tokenaantallen. Sla gebruikersinput niet volledig op, maar leg alleen een hash vast.



Werk stap voor stap:

Definieer een vast eventschema met trace-ID, agent, actie, status, duur, modelversie en tokenaantallen.

Bepaal welke gevoelige informatie niet in logs mag worden opgeslagen.

Maak één voorbeeld-event met een unieke trace-ID.

Hash de gebruikersinput voordat deze in het event wordt opgenomen.

Controleer of het event als geldige JSON wordt weergegeven.

Hint: Observability moet herleidbaarheid bieden zonder van het logplatform een nieuwe bron van datalekken te maken.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
