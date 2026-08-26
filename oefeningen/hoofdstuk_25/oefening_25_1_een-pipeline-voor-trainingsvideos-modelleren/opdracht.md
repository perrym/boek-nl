# Oefening 25.1 - Een pipeline voor trainingsvideo’s modelleren

**Niveau:** Verdieping  
**Geschatte tijd:** 45 tot 75 minuten

## Doel

Video, audio, transcript en beeldframes als afzonderlijke verwerkingsstappen ontwerpen.

## Opdracht

Maak met dataclasses een pipelineconfiguratie. Simuleer de stappen en registreer per stap invoer, uitvoer en status.



Werk stap voor stap:


1. Definieer de afzonderlijke stappen voor video, audio, transcript en beeldframes.

2. Leg per stap vast welke invoer, uitvoer en status wordt verwacht.

3. Implementeer de pipelineconfiguratie met dataclasses en simuleer de normale route.

4. Simuleer minimaal één fout, bijvoorbeeld ontbrekende audio of een mislukt transcript.

5. Controleer of de status en fallback per modaliteit traceerbaar worden vastgelegd.

Hint: Behandel video, audio, tekst en beeld als afzonderlijke verwerkingsstromen. Een fout in één modaliteit hoeft niet de hele pipeline ongeldig te maken.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
