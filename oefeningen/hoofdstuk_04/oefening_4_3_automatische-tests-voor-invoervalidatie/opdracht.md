# Oefening 4.3 - automatische tests voor invoervalidatie

**Niveau:** Basis    Geschatte tijd: 25 tot 35 minuten    Benodigd package: pytest

## Doel

Leren hoe unit tests controleren of een functie correct reageert op geldige en ongeldige invoer.

Voorbereiding

Installeer pytest:

Sla de validatiefunctie op in een bestand met de naam:

risicoscore.py

Inhoud van risicoscore.py:

Maak daarna een tweede bestand:

test_risicoscore.py

## Opdracht

Schrijf tests voor:

een geldige score;

een negatieve score;

tekstinvoer;

grenswaarde 0;

grenswaarde 100.

Uitwerking in Python

Tests uitvoeren

Open een terminal in de map met beide bestanden en voer uit:

Wat gebeurt er in de tests?

Geldige score

Deze test controleert of een normale geldige score correct wordt verwerkt.

Negatieve score

Deze test controleert of een negatieve score een ValueError veroorzaakt.

De test slaagt alleen wanneer de verwachte exception daadwerkelijk wordt gegeven.

Tekstinvoer

Deze test controleert of tekst wordt geweigerd met een TypeError.

Grenswaarden

Met parametrize wordt dezelfde test uitgevoerd voor meerdere waarden.

De test wordt eenmaal uitgevoerd voor 0 en eenmaal voor 
100. Hierdoor hoef je geen twee bijna gelijke testfuncties te schrijven.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
