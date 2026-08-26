import numpy as np

origineel = np.array([10, 20, 30, 40, 50])
view = origineel[1:4]
kopie = origineel[1:4].copy()

view[0] = 999
kopie[1] = 777

print("Origineel:", origineel)
print("View:", view)
print("Kopie:", kopie)
