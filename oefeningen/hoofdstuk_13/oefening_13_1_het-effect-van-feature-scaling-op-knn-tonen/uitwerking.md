# Uitwerking 13.1

## Hoe werkt de code?

KNN gebruikt afstanden. Een verschil van duizenden euro’s kan daardoor veel zwaarder meetellen dan een verschil van 0,5 in risicoscore, ook wanneer inkomen inhoudelijk niet voorspellend is. StandardScaler zet features op een vergelijkbare schaal en wordt binnen de Pipeline per trainingsfold geleerd.


## Verwachte uitvoer

De versie met scaling presteert doorgaans duidelijk beter, omdat risicoscore het echte patroon bevat.


## Controleer je uitkomst

- Scaling wordt binnen cross-validation uitgevoerd.
- Niet iedere algoritmefamilie heeft scaling even hard nodig.
- Outliers worden gecontroleerd voordat StandardScaler wordt toegepast.

## Verdiepingsopdracht

Vergelijk StandardScaler met RobustScaler.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
