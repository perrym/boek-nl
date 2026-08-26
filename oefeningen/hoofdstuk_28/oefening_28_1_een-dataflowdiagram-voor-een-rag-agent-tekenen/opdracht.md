# Oefening 28.1 - Een dataflowdiagram voor een RAG-agent tekenen

**Niveau:** Verdieping  
**Geschatte tijd:** 45 tot 75 minuten  
**Benodigde packages:** networkx, matplotlib

## Doel

Assets, externe entiteiten en datastromen van een RAG-agent identificeren en zichtbaar maken waar gegevens de interne omgeving kunnen verlaten.

## Opdracht

Gebruik NetworkX om een RAG-agent met documentopslag, vectorstore, LLM-provider en e-mailtool te modelleren. Markeer bij iedere node of deze intern of extern is..



Werk stap voor stap:

Inventariseer de belangrijkste componenten: gebruiker, RAG-agent, documentopslag, vectorstore, LLM-provider, e-mailtool en ontvanger.

Modelleer deze componenten als nodes in een gerichte graaf.

Geef iedere node het attribuut intern of extern.

Voeg de belangrijkste datastromen als gerichte verbindingen toe.

Bekijk welke verbindingen naar externe componenten lopen en daarom extra beveiligingsaandacht vereisen.

Hint: Een dataflowdiagram helpt zichtbaar te maken welke componenten met elkaar communiceren en waar gegevens de interne omgeving kunnen verlaten.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
