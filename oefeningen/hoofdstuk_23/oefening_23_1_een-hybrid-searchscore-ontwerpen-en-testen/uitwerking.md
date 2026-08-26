# Uitwerking 23.1

## Hoe werkt de code?

De drie scores liggen al tussen 0 en 1. In echte systemen moeten scores van verschillende zoekmachines vaak eerst worden genormaliseerd. Actualiteit is alleen nuttig wanneer recentere documenten ook inhoudelijk de voorkeur verdienen. Een verouderd maar formeel geldend beleid mag niet automatisch lager eindigen.

Een cross-encoder leest vraag en document samen en is nauwkeurig, maar moet voor ieder paar worden uitgevoerd. Bij miljoenen documenten is dat te duur en te traag. Daarom haalt een snelle bi-encoder of zoekmachine eerst een beperkte kandidatenlijst op. De cross-encoder rerankt alleen die top-k.


## Verwachte uitvoer

De tabel is gesorteerd op de gewogen hybrid score.

De volledige vergelijking groeit lineair met het aantal documenten. De top-100 rerank blijft voor iedere collectiegrootte gelijk.


## Controleer je uitkomst

- Gewichten tellen op tot 1.
- Scoreberekening is reproduceerbaar.
- Geldigheid en autorisatie zijn harde filters, geen zachte bonus.
- Latency en throughput worden beide gemeten.
- Top-k bevat voldoende recall.
- Reranking heeft time-outs en fallbackgedrag.

## Verdiepingsopdracht

Voer een gevoeligheidsanalyse uit voor semantisch gewicht van 0,3 tot 0,8.

Niveau: Gemiddeld tot gevorderd  |  Geschatte tijd: 40 tot 60 minuten

Bereken hoeveel parallelle workers nodig zijn om de top-100 rerank binnen 300 milliseconden te voltooien.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
