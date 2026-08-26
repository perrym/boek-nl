from time import perf_counter

from sklearn.datasets import make_classification
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import cross_val_score

X, y = make_classification(
    n_samples=1200, n_features=15, n_informative=8, random_state=42
)

modellen = {
    "Random forest - bagging": RandomForestClassifier(n_estimators=200, random_state=42),
    "Gradient boosting": GradientBoostingClassifier(random_state=42),
}

for naam, model in modellen.items():
    start = perf_counter()
    score = cross_val_score(model, X, y, cv=5, scoring="f1").mean()
    duur = perf_counter() - start
    print(f"{naam}: gemiddelde F1={score:.3f}, duur={duur:.2f}s")
