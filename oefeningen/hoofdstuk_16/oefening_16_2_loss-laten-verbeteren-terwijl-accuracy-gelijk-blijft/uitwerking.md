# Uitwerking 16.2

## Hoe werkt de code?

Beide sets plaatsen alle voorbeelden aan de juiste kant van de threshold 0,5 en hebben daardoor dezelfde accuracy. De nieuwe waarschijnlijkheden zijn echter veel zekerder in de juiste richting, waardoor log loss lager is. Loss bevat dus meer informatie over modelvertrouwen dan alleen goed of fout.


## Verwachte uitvoer

Accuracy is in beide gevallen 1,00. De log loss van de nieuwe waarschijnlijkheden is lager.


## Controleer je uitkomst

- Waarschijnlijkheden liggen strikt tussen 0 en 1.
- De threshold is expliciet.
- Kalibratie wordt naast accuracy onderzocht.

## Verdiepingsopdracht

Voeg een overmoedige fout toe, bijvoorbeeld kans 0,99 voor een verkeerd label, en bekijk het effect op log loss.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
