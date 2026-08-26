import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=700, n_features=8, n_informative=5,
    weights=[0.65, 0.35], random_state=42
)

resultaten = []
for k in [3, 5, 9]:
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=k)),
    ])
    scores = cross_val_score(model, X, y, cv=5, scoring="f1")
    resultaten.append({
        "k": k,
        "gemiddelde_f1": scores.mean(),
        "standaardafwijking": scores.std(),
    })

print(pd.DataFrame(resultaten).round(3).to_string(index=False))
