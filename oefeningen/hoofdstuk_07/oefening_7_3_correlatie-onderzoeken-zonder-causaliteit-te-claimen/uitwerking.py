import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(7)
wijzigingen = rng.integers(5, 80, size=60)
incidenten = 2 + 0.18 * wijzigingen + rng.normal(0, 3, size=60)

correlatie = np.corrcoef(wijzigingen, incidenten)[0, 1]
print(f"Correlatie: {correlatie:.2f}")
print("Verklaring 1: grotere systemen hebben zowel meer wijzigingen als meer incidenten.")
print("Verklaring 2: slechte change-controls veroorzaken een deel van beide waarden.")

plt.scatter(wijzigingen, incidenten)
plt.xlabel("Aantal wijzigingen")
plt.ylabel("Aantal incidenten")
plt.title("Wijzigingen en incidenten")
plt.tight_layout()
plt.show()
