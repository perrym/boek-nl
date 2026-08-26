# Oefening 23.2 - Schaalbaarheid van cross-encoding berekenen

## Doel

Inzicht krijgen in het verschil tussen ophalen en reranken.

## Opdracht

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
