# Oefening 10.1 - MAE en MSE vergelijken bij een zeer grote fout

**Niveau:** Gemiddeld  
**Geschatte tijd:** 35 tot 50 minuten  
**Benodigde packages:** numpy, matplotlib, scikit-learn

## Doel

Met Python aantonen waarom MSE extreme fouten zwaarder bestraft dan MAE.

## Opdracht

Bereken MAE en MSE voor twee voorspellingen. In scenario A zijn alle fouten klein. In scenario B is bijna alles correct, maar bevat de voorspelling één zeer grote fout. Vergelijk de uitkomsten en visualiseer de absolute en gekwadrateerde fouten.



Werk stap voor stap:


1. Maak of laad de dataset en bepaal welke kolom de target is.

2. Splits de data voordat je preprocessing of modeltraining uitvoert.

3. Bouw eerst een eenvoudige baseline en daarna het gevraagde model.

4. Bereken de relevante metric of maak de gevraagde grafiek.

5. Vergelijk de uitkomsten en benoem minimaal één beperking of foutscenario.

Hint: Gebruik een vaste random_state waar dat kan. Dan kun je jouw resultaat eerlijk vergelijken met de voorbeelduitwerking.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
