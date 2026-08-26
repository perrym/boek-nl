import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

X, _ = make_blobs(
    n_samples=600, centers=4, cluster_std=1.2, random_state=42
)

resultaten = []
for k in range(2, 7):
    model = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = model.fit_predict(X)
    resultaten.append({
        "k": k,
        "silhouette": silhouette_score(X, labels),
        "inertia": model.inertia_,
        "domein_beoordeling": "te bepalen met proceseigenaar",
    })

print(pd.DataFrame(resultaten).round(3).to_string(index=False))
