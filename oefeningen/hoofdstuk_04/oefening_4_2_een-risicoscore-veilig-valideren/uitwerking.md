# Uitwerking 4.2

## Hoe werkt de code?

De functie voert drie controles uit.

Controle 1: boolean

Python behandelt True en False als een speciale vorm van een integer. Zonder deze aparte controle zou True als de waarde 1 kunnen worden geaccepteerd.

Daarom worden booleans eerst expliciet geweigerd.

Controle 2: datatype

Hier wordt gecontroleerd of de invoer een integer of float is. Tekst en None worden geweigerd.

Bij een verkeerd datatype wordt een TypeError gebruikt.

Controle 3: bereik

Hier wordt gecontroleerd of de waarde binnen het toegestane bereik ligt.

Een waarde zoals -1 is wel een getal, maar geen geldige risicoscore. Daarom wordt een ValueError gebruikt.

Voorspelbare uitvoer

De functie retourneert altijd een float. Daardoor ontvangt vervolgcode steeds hetzelfde datatype.


## Controleer je uitkomst

- Controleer of jouw functie aan de volgende punten voldoet:
- 0 wordt geaccepteerd;
- 100 wordt geaccepteerd;
- 50.5 wordt geaccepteerd;
- 1 wordt geweigerd;
- 100.01 wordt geweigerd;
- "hoog" wordt geweigerd;
- None wordt geweigerd;
- True wordt geweigerd;
- geldige invoer geeft altijd een float terug;
- foutmeldingen leggen duidelijk uit wat er mis is.

## Verdiepingsopdracht

Voeg een optionele parameter toe waarmee de maximale score kan worden ingesteld.

Voorbeeld:

Uitvoer:

8.0


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
