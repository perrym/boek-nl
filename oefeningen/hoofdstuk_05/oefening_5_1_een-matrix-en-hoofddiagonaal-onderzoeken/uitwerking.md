# Uitwerking 5.1

## Hoe werkt de code?

reshape verandert alleen de vorm en niet de volgorde van de getallen. np.diag haalt in dit geval de elementen op posities [0,0], [1,1] enzovoort op. Zulke diagonalen spelen een belangrijke rol in lineaire algebra en machine learning.


## Verwachte uitvoer

De diagonaal is [1, 7, 13, 19, 25] en de som is 65.


## Controleer je uitkomst

- De matrix heeft shape (5, 5).
- De diagonaal bevat precies vijf waarden.
- De som wordt met NumPy berekend.

## Verdiepingsopdracht

Haal ook de diagonaal boven de hoofddiagonaal op met np.diag(matrix, k=1).


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
