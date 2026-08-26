# Uitwerking 5.2

## Hoe werkt de code?

De operator ** werkt elementgewijs op een NumPy-array. Dit heet vectorisatie. De code is meestal korter en bij grote arrays sneller dan een Python-lus. array_equal controleert zowel de waarden als de vorm.


## Verwachte uitvoer

De kwadraten zijn [9, 4, 1, 0, 1, 4, 9] en de vergelijking geeft True.


## Controleer je uitkomst

- Negatieve waarden worden correct gekwadrateerd.
- De nul blijft nul.
- Beide methoden leveren hetzelfde resultaat.

## Verdiepingsopdracht

Meet met timeit het snelheidsverschil bij een miljoen waarden.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
