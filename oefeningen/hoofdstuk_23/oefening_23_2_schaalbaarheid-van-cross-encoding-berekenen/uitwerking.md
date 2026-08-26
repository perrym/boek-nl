# Uitwerking 23.2

## Hoe werkt de code?

Een cross-encoder leest vraag en document samen en is nauwkeurig, maar moet voor ieder paar worden uitgevoerd. Bij miljoenen documenten is dat te duur en te traag. Daarom haalt een snelle bi-encoder of zoekmachine eerst een beperkte kandidatenlijst op. De cross-encoder rerankt alleen die top-k.


## Verwachte uitvoer

De volledige vergelijking groeit lineair met het aantal documenten. De top-100 rerank blijft voor iedere collectiegrootte gelijk.


## Controleer je uitkomst

- Latency en throughput worden beide gemeten.
- Top-k bevat voldoende recall.
- Reranking heeft time-outs en fallbackgedrag.

## Verdiepingsopdracht

Bereken hoeveel parallelle workers nodig zijn om de top-100 rerank binnen 300 milliseconden te voltooien.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
