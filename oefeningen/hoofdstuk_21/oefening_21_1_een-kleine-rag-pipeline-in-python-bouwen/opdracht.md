# Oefening 21.1 - Een kleine RAG-pipeline in Python bouwen

**Niveau:** Gemiddeld tot gevorderd  
**Geschatte tijd:** 40 tot 60 minuten  
**Benodigde packages:** scikit-learn

## Doel

De stappen chunking, retrieval en antwoordcontext concreet uitvoeren.

## Opdracht

Gebruik TF-IDF als eenvoudige lokale retriever. Zoek de twee meest relevante documenten voor een vraag en toon de context die naar een taalmodel zou gaan.



Werk stap voor stap:


1. Maak een kleine documentverzameling en geef ieder document een unieke bron-ID.

2. Vectoriseer de documenten en de zoekvraag met TF-IDF en bereken de overeenkomst.

3. Selecteer de twee beste resultaten en toon zowel de score als de gekozen brontekst.

4. Bouw de context die naar een taalmodel zou gaan en houd retrieval en generatie als aparte stappen zichtbaar.

5. Test ook een vraag zonder passende bron en bepaal welk abstention- of fallbackgedrag veilig is.

Hint: Toon bron-ID, score en geselecteerde tekst. Zonder die gegevens is later niet vast te stellen waarom een antwoord ontstond.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
