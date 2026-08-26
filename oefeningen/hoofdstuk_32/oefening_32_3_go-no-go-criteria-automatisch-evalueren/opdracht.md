# Oefening 32.3 - Go/no-go-criteria automatisch evalueren

**Niveau:** Verdieping  
**Geschatte tijd:** 45 tot 75 minuten

## Doel

Een productieadvies baseren op expliciete harde en zachte drempels.

## Opdracht

Maak een releasefunctie met harde blokkades voor security, privacy en autorisatie. Voeg kwaliteits- en performancedrempels toe en print alle redenen voor no-go.



Werk stap voor stap:


1. Definieer harde blokkades voor security, privacy en autorisatie en aparte drempels voor kwaliteit en performance.

2. Maak meerdere releasescenario's, waaronder één met een hoge kwaliteitscore maar een securityblokkade.

3. Implementeer de releasefunctie en laat deze alle redenen voor no-go verzamelen in plaats van alleen de eerste fout.

4. Controleer dat harde blokkades niet door een hoge totaalscore kunnen worden gecompenseerd.

5. Voeg een handmatige goedkeuringsstap toe voor restrisico dat niet automatisch kan worden beoordeeld.

Hint: Een gewogen score mag een fundamentele security- of privacyfout nooit wegmiddelen. Harde gates moeten altijd voorrang krijgen.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
