import numpy as np

matrix = np.arange(1, 26).reshape(5, 5)
diagonaal = np.diag(matrix)

print(matrix)
print("Hoofddiagonaal:", diagonaal)
print("Som:", diagonaal.sum())
