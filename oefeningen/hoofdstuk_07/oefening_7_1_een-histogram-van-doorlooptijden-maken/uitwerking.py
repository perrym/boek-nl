import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)
doorlooptijden = np.concatenate([
    rng.normal(loc=8, scale=2, size=180),
    np.array([20, 28, 35]),
])
doorlooptijden = np.clip(doorlooptijden, 0, None)

gemiddelde = doorlooptijden.mean()
mediaan = np.median(doorlooptijden)

plt.hist(doorlooptijden, bins=20, edgecolor="black")
plt.axvline(gemiddelde, linestyle="--", label=f"Gemiddelde: {gemiddelde:.1f}")
plt.axvline(mediaan, linestyle=":", label=f"Mediaan: {mediaan:.1f}")
plt.xlabel("Doorlooptijd in dagen")
plt.ylabel("Aantal")
plt.title("Verdeling van doorlooptijden")
plt.legend()
plt.tight_layout()
plt.show()
