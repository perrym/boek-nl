import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

rng = np.random.default_rng(42)
n = 500
ernst = rng.integers(1, 6, size=n)
doorlooptijd = rng.normal(8, 3, size=n)
label = (ernst >= 4).astype(int)
afsluitcode = np.where(label == 1, "ESCALATED", "NORMAL")

df = pd.DataFrame({
    "ernst": ernst,
    "doorlooptijd": doorlooptijd,
    "afsluitcode": afsluitcode,
})

zonder_leakage = df[["ernst", "doorlooptijd"]]
met_leakage = pd.get_dummies(df, columns=["afsluitcode"], dtype=int)

model = LogisticRegression(max_iter=1000)
score_zonder = cross_val_score(model, zonder_leakage, label, cv=5).mean()
score_met = cross_val_score(model, met_leakage, label, cv=5).mean()

print(f"Zonder leakage: {score_zonder:.3f}")
print(f"Met leakage: {score_met:.3f}")
