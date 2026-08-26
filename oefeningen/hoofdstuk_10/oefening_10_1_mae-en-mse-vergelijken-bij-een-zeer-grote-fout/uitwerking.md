# Uitwerking 10.1

## Hoe werkt de code?

MAE neemt van iedere voorspelling de absolute fout en middelt die. MSE kwadrateert iedere fout voordat het gemiddelde wordt berekend. De fout van 50 draagt daarom 50 bij aan de MAE-som, maar 2500 aan de MSE-som. MSE is geschikt wanneer grote fouten echt disproportioneel schadelijk zijn. MAE is robuuster wanneer uitschieters voorkomen en iedere fout ongeveer lineair kost.


## Verwachte uitvoer

Scenario A heeft MAE 1,60 en MSE 2,80. Scenario B heeft MAE 10,00 en MSE 500,00. De enkele grote fout domineert dus vooral de MSE.


## Controleer je uitkomst

- Dezelfde werkelijke waarden worden in beide scenario’s gebruikt.
- De metriek wordt gekozen op basis van bedrijfsimpact.
- Een hoge MSE leidt tot onderzoek naar uitschieters en niet automatisch tot verwijderen daarvan.

## Verdiepingsopdracht

Voeg RMSE toe en maak de grote fout instelbaar met een variabele. Plot hoe MAE, MSE en RMSE veranderen bij fouten van 0 tot 100.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
