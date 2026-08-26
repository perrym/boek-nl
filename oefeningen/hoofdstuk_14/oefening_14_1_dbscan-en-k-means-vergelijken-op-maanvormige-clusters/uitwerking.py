import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN, KMeans
from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler

X, _ = make_moons(n_samples=500, noise=0.07, random_state=42)
X = StandardScaler().fit_transform(X)

modellen = {
    "K-Means": KMeans(n_clusters=2, n_init=10, random_state=42),
    "DBSCAN": DBSCAN(eps=0.25, min_samples=5),
}

for naam, model in modellen.items():
    labels = model.fit_predict(X)
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=18)
    plt.title(naam)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.tight_layout()
    plt.show()
