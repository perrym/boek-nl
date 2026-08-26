# Oefening 4.2 - een risicoscore veilig valideren

**Niveau:** Basis    Geschatte tijd: 25 tot 35 minuten

## Doel

Leren hoe je invoer controleert voordat deze in een analyse, rapportage of AI-model wordt gebruikt.

Situatie

Een toepassing ontvangt een risicoscore. De score moet een geheel of decimaal getal van 0 tot en met 100 zijn.

De volgende waarden zijn geldig:

0
42
72.5
100

De volgende waarden zijn ongeldig:

-1
100.01
"hoog"
None
True
False

## Opdracht

Schrijf een functie met de naam valideer_risicoscore().

De functie moet:

gehele getallen accepteren;

decimale getallen accepteren;

alleen waarden van 0 tot en met 100 accepteren;

booleans weigeren;

tekst weigeren;

None weigeren;

altijd een float teruggeven bij geldige invoer;

een duidelijke exception geven bij ongeldige invoer.

Stap 1: maak de functie

Stap 2: test geldige waarden

Verwachte uitvoer:

72.0
42.5
0.0
100.0

Stap 3: test ongeldige waarden

Verwachte fout:

ValueError: Risicoscore moet tussen 0 en 100 liggen

Test daarna ook:

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
