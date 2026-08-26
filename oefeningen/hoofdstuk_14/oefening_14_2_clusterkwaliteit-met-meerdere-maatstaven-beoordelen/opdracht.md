# Oefening 14.2 - Clusterkwaliteit met meerdere maatstaven beoordelen

**Niveau:** Gemiddeld  
**Geschatte tijd:** 35 tot 50 minuten  
**Benodigde packages:** pandas, scikit-learn

## Doel

Silhouette, stabiliteit en bruikbaarheid combineren.

## Opdracht

Train K-Means met k=2 tot en met 
6. Bereken silhouette score en inertia. Voeg daarnaast handmatig een bruikbaarheidsbeoordeling toe.



Werk stap voor stap:


1. Maak of laad de dataset en bepaal welke features de afstand of overeenkomst beschrijven.

2. Schaal de numerieke features wanneer de gekozen afstandsmaat dat vereist.

3. Pas de clusteringmethode toe zonder een targetlabel te gebruiken voor de training.

4. Beoordeel de oplossing met visualisatie, passende clustermaatstaven en gevoeligheidsanalyse.

5. Geef clusters pas een inhoudelijke betekenis nadat de kenmerken en stabiliteit zijn onderzocht.

Hint: Bij unsupervised learning is er geen target om de clusterlabels direct mee te trainen. Technische kwaliteit en inhoudelijke bruikbaarheid moeten daarom apart worden beoordeeld.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
