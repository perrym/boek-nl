import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

y_werkelijk = np.array([10, 20, 30, 40, 50])
y_voorspeld_a = np.array([12, 18, 31, 39, 48])
y_voorspeld_b = np.array([10, 20, 30, 40, 100])

for naam, voorspelling in {
    "A - kleine fouten": y_voorspeld_a,
    "B - een grote fout": y_voorspeld_b,
}.items():
    mae = mean_absolute_error(y_werkelijk, voorspelling)
    mse = mean_squared_error(y_werkelijk, voorspelling)
    print(f"{naam}: MAE={mae:.2f}, MSE={mse:.2f}")

fouten = np.abs(y_werkelijk - y_voorspeld_b)
posities = np.arange(len(fouten))
plt.bar(posities - 0.18, fouten, width=0.36, label="Absolute fout")
plt.bar(posities + 0.18, fouten ** 2, width=0.36, label="Gekwadrateerde fout")
plt.xlabel("Waarneming")
plt.ylabel("Foutbijdrage")
plt.title("Effect van een zeer grote fout")
plt.legend()
plt.tight_layout()
plt.show()
