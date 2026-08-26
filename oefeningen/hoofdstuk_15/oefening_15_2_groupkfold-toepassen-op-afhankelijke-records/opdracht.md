# Oefening 15.2 - GroupKFold toepassen op afhankelijke records

**Niveau:** Gemiddeld  
**Geschatte tijd:** 35 tot 50 minuten  
**Benodigde packages:** numpy, scikit-learn

## Doel

Voorkomen dat records van dezelfde persoon of organisatie in train en validatie terechtkomen.

## Opdracht

Maak data met tien klanten en twintig records per klant. Vergelijk gewone KFold met GroupKFold en controleer of klanten in beide delen voorkomen.



Werk stap voor stap:


1. Maak een dataset met meerdere records per klant en leg de klant-id apart vast als groepsvariabele.

2. Voer eerst gewone KFold uit en controleer welke klanten tegelijk in training en validatie voorkomen.

3. Herhaal de splitsing met GroupKFold en gebruik dezelfde klant-id als groups-parameter.

4. Vergelijk de overlap tussen beide methoden en leg uit waarom groepsscheiding dataleakage kan voorkomen.

5. Bepaal welke entiteit in een echte toepassing als groep moet worden gebruikt, bijvoorbeeld klant, applicatie of apparaat.

Hint: De juiste groep volgt uit de afhankelijkheid in de praktijk. Records die informatie over dezelfde entiteit delen, horen meestal niet over training en validatie te worden verdeeld.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
