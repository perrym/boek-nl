# Oefening 23.1 - Een hybrid-searchscore ontwerpen en testen

**Niveau:** Gemiddeld tot gevorderd  
**Geschatte tijd:** 40 tot 60 minuten  
**Benodigde packages:** pandas

## Doel

Semantische, lexicale en metadata-signalen gecontroleerd combineren.

Inzicht krijgen in het verschil tussen ophalen en reranken.

## Opdracht

Maak vijf zoekresultaten met drie deelscores. Normaliseer de scores en bereken een gewogen hybrid score. Sorteer de resultaten.



Werk stap voor stap:


1. Maak een kleine en controleerbare documentverzameling.

2. Splits retrieval, selectie van context en antwoordgeneratie in aparte stappen.

3. Voer de zoek- of chunkingmethode uit en toon welke bronnen worden geselecteerd.

4. Controleer het antwoord tegen de bron en test ook een vraag zonder passend document.

5. Leg uit of een fout uit retrieval of uit generatie ontstaat.

Hint: Houd bron-ID, score en geselecteerde tekst zichtbaar. Anders is later niet te bepalen waarom een antwoord ontstond.

Bereken hoeveel cross-encoderbeoordelingen nodig zijn voor 100, 100.000 en 10 miljoen documenten. Vergelijk dit met reranking van alleen top-100 resultaten.



Werk stap voor stap:


1. Bereken hoeveel document-queryparen een cross-encoder moet beoordelen bij 100, 100.000 en 10 miljoen documenten.

2. Bereken daarna dezelfde aantallen wanneer eerst retrieval plaatsvindt en alleen de top-100 wordt gererankt.

3. Zet beide scenario's in een tabel en bereken de reductiefactor.

4. Voeg een eenvoudige aanname voor gemiddelde beoordelingstijd of kosten per paar toe.

5. Leg uit waarom retrieval gevolgd door reranking schaalbaarder is dan cross-encoding van de volledige collectie.

Hint: Scheid kandidaatselectie en reranking. De kracht van een cross-encoder zit in nauwkeurige beoordeling van een beperkte kandidatenlijst.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
