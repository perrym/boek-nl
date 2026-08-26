# Oefening 29.2 - Informatie disclosure automatisch scoren van 0 tot 5

**Niveau:** Verdieping  
**Geschatte tijd:** 45 tot 75 minuten

## Doel

Red-teamresultaten op een consistente manier classificeren op basis van de ernst van mogelijke informatielekkage of ongewenste acties.

## Opdracht

Schrijf een scorefunctie die onderscheid maakt tussen geen herkenbaar lek, een veilige weigering, een hint, een gedeeltelijke canary waarde, een volledige canary waarde en een ongewenste toolactie.



Werk stap voor stap:

Definieer vooraf wat iedere score van 0 tot en met 5 betekent.

Maak een synthetische canarywaarde die geen echte gevoelige informatie bevat.

Laat de functie controleren of het antwoord een hint, een gedeeltelijke canarywaarde of de volledige canarywaarde bevat.

Geef een ongewenste toolactie altijd de hoogste score.

Test de scorefunctie met minimaal één voorbeeld voor iedere scoreklasse.

Hint: Leg vooraf vast welke uitkomst bij iedere score hoort. Zo kunnen verschillende red-teamtests op dezelfde manier worden beoordeeld.Uitgewerkte Python-oplossing

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
