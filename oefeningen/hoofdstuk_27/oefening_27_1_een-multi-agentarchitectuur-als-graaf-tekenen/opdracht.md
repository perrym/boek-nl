# Oefening 27.1 - Een multi-agentarchitectuur als graaf tekenen

**Niveau:** Verdieping  
**Geschatte tijd:** 45 tot 75 minuten  
**Benodigde packages:** networkx, matplotlib

## Doel

Rollen, datastromen en grenzen tussen agents zichtbaar maken.

## Opdracht

Gebruik NetworkX om een multi-agentarchitectuur voor een software-securityreview te tekenen met een orchestrator, code-agent, dependency-agent, policy-agent en reviewer.

Werk stap voor stap:

Bepaal welke rollen een afzonderlijke agent nodig hebben en welke taken beter deterministisch kunnen worden uitgevoerd.

Modelleer de orchestrator, specialistische agents, reviewer en relevante externe systemen als nodes.

Voeg gerichte verbindingen toe om zichtbaar te maken welke informatie tussen de onderdelen wordt uitgewisseld.

Controleer of geen enkele specialistische agent onnodig toegang heeft tot alle tools of tot de volledige gesprekscontext.

Beschrijf één mogelijk foutpad en leg uit hoe de orchestrator deze fout kan detecteren en begrenzen.

Hint: Meer agents betekent ook meer overdrachtsmomenten en mogelijke foutpaden. Voeg daarom alleen een agent toe wanneer deze scheiding aantoonbare meerwaarde biedt.

uitgewerkte Python-oplossing

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
