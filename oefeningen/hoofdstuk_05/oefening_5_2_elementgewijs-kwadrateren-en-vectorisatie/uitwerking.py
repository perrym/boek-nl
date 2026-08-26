import numpy as np

waarden = np.arange(-3, 4)
kwadraten_numpy = waarden ** 2
kwadraten_python = np.array([waarde * waarde for waarde in waarden])

print("Waarden:", waarden)
print("Kwadraten:", kwadraten_numpy)
print("Gelijk:", np.array_equal(kwadraten_numpy, kwadraten_python))
