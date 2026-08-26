# Oefening 27.3 - Test foutpropagatie en herstel

**Niveau:** Verdieping  
**Geschatte tijd:** 45 tot 75 minuten

## Doel

Controleren hoe een multi-agentsysteem fouten gecontroleerd doorgeeft, begrenst, herstelt en traceerbaar afhandelt.

## Opdracht

Breid de architectuur uit oefening 27.1 uit met drie gesimuleerde fouten: een time-out, een ongeldige gestructureerde respons en een resultaat zonder voldoende bewijs. Bepaal per fout of de orchestrator opnieuw probeert, een alternatief pad kiest, stopt of menselijke beoordeling vraagt. Leg de volledige beslisroute vast onder één trace-ID.

Werk stap voor stap:

Definieer de drie fouttypen en het verwachte herstelgedrag voordat je de simulatie uitvoert.

Stel een maximum in voor herhaalpogingen en definieer duidelijke stopvoorwaarden en een route voor menselijke escalatie.

Simuleer ieder fouttype afzonderlijk en leg alle stappen vast onder dezelfde trace-ID.

Controleer dat een foutief of onvoldoende onderbouwd resultaat nooit automatisch als uiteindelijke conclusie wordt gebruikt.

Controleer dat herhaalpogingen geen dubbele schrijfacties veroorzaken en dat grenzen voor kosten en aantallen stappen worden gerespecteerd.

Hint: Maak foutafhandeling expliciet in de orchestrator. Vertrouw niet op een model om zelf te bepalen wanneer een fout veilig kan worden genegeerd.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
