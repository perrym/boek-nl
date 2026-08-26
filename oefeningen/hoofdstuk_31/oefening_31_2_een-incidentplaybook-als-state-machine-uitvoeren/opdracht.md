# Oefening 31.2 - Een incident playbook als state machine uitvoeren

**Niveau:** Verdieping  
**Geschatte tijd:** 45 tot 75 minuten

## Doel

Cross-userdatalekken via vaste stappen afhandelen en bewijs vastleggen.

## Opdracht

Modelleer de incidentfasen detectie, containment, onderzoek, herstel en evaluatie. Blokkeer een overgang wanneer een verplichte actie ontbreekt.



Werk stap voor stap:


1. Definieer de toestanden detectie, containment, onderzoek, herstel en evaluatie.

2. Leg per overgang vast welk bewijs of welke actie verplicht is.

3. Implementeer de state machine en blokkeer een overgang wanneer bewijs ontbreekt.

4. Simuleer een cross-userlek en controleer dat containment niet wordt overgeslagen.

5. Bewaar statusgeschiedenis en motiveer welke juridische, privacy- of security-escalatie parallel nodig is.

Hint: Een incident mag niet alleen administratief naar een volgende fase gaan; de vereiste containment- en bewijsstappen moeten technisch controleerbaar zijn.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
