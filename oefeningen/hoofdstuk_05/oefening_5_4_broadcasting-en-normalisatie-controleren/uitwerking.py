import numpy as np

X = np.array([
    [10.0, 2.0, 120.0],
    [14.0, 4.0, 100.0],
    [18.0, 6.0, 140.0],
])

mean = X.mean(axis=0)
X_centered = X - mean

print("Gemiddelde:", mean)
print("Gecentreerde matrix:\n", X_centered)
print("Controle:", X_centered.mean(axis=0))
