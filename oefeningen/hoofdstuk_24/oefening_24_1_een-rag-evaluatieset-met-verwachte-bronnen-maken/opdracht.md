# Oefening 24.1 - Een RAG-evaluatieset met verwachte bronnen maken

**Niveau:** Gemiddeld tot gevorderd  
**Geschatte tijd:** 40 tot 60 minuten  
**Benodigde packages:** pandas

## Doel

Testvragen, ground truth en bronverwachtingen gestructureerd vastleggen.

## Opdracht

Maak vijf vragen met een verwacht antwoord en verwachte document-ID’s. Schrijf een controle die ontbrekende velden en dubbele vraag-ID’s meldt.



Werk stap voor stap:


1. Maak een kleine evaluatieset met vragen, toegestane bron-ID's en verwachte kernpunten.

2. Voeg minimaal één vraag toe waarvoor bewust onvoldoende informatie beschikbaar is.

3. Voer retrieval uit en registreer welke bronnen daadwerkelijk worden geselecteerd.

4. Bereken minimaal context precision en context recall of een eenvoudige equivalent daarvan.

5. Controleer apart of het gegenereerde antwoord door de gevonden context wordt ondersteund.

Hint: Leg de verwachte bronnen vooraf vast. Anders kan een overtuigend antwoord ten onrechte als goed worden beoordeeld.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
