# Oefening 28.2 - Indirecte bronnen van prompt injection automatisch inventariseren

**Niveau:** Verdieping  
**Geschatte tijd:** 45 tot 75 minuten

## Doel

Onbetrouwbare externe inhoud herkennen voordat deze tools of modellen beïnvloedt.

## Opdracht

Maak een scanner die tekstbronnen markeert wanneer verdachte instructiepatronen voorkomen. Test vijf verschillende bronsoorten.



Werk stap voor stap:

Maak vijf tekstbronnen, bijvoorbeeld een PDF-fragment, webpagina, e-mail, ticket en codecommentaar.

Definieer enkele herkenbare verdachte instructiepatronen.

Laat de scanner per bron rapporteren welke patronen zijn gevonden en of de bron als verdacht wordt gemarkeerd.

Test zowel verdachte als onschuldige tekst en vergelijk de resultaten.

Leg uit waarom patroonherkenning alleen onvoldoende is en waarom autorisatie en toolbeperkingen buiten het model noodzakelijk blijven.

Hint: Gebruik de scanner als detectielaag, niet als autorisatiemechanisme. Externe tekst blijft onbetrouwbare data, ook wanneer geen patroon wordt gevonden.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
