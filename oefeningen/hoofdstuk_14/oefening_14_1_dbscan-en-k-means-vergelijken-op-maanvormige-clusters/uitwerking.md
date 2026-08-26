# Uitwerking 14.1

## Hoe werkt de code?

K-Means zoekt compacte clusters rond centroïden en snijdt de ruimte daardoor grofweg in bolvormige gebieden. DBSCAN gebruikt dichtheid en kan de twee maanvormen volgen. Label -1 bij DBSCAN betekent ruis. De uitkomst hangt sterk af van eps, min_samples en scaling.


## Verwachte uitvoer

DBSCAN volgt meestal de twee maanvormen beter. K-Means maakt een minder natuurlijke rechte verdeling.


## Controleer je uitkomst

- Data is geschaald voor afstandsberekening.
- Ruispunten worden niet automatisch weggegooid.
- De parameters zijn met visualisatie en domeinkennis beoordeeld.

## Verdiepingsopdracht

Varieer eps van 0,1 tot 0,5 en tel per instelling het aantal clusters en ruispunten.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
