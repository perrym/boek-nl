import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(42)
inkomen = rng.normal(100_000, 20_000, 500)
risicoscore = rng.uniform(0, 1, 500)
y = (risicoscore > 0.65).astype(int)
X = np.column_stack([inkomen, risicoscore])

zonder_scaling = KNeighborsClassifier(n_neighbors=7)
met_scaling = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier(n_neighbors=7)),
])

for naam, model in {"Zonder scaling": zonder_scaling, "Met scaling": met_scaling}.items():
    score = cross_val_score(model, X, y, cv=5).mean()
    print(f"{naam}: {score:.3f}")
