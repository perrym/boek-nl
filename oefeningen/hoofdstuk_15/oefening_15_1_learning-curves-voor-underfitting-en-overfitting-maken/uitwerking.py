import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

X, y = make_moons(n_samples=800, noise=0.25, random_state=42)

modellen = {
    "Logistische regressie": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000)),
    ]),
    "Diepe beslissingsboom": DecisionTreeClassifier(max_depth=None, random_state=42),
}

for naam, model in modellen.items():
    groottes, train_scores, val_scores = learning_curve(
        model, X, y, cv=5, train_sizes=np.linspace(0.1, 1.0, 8), scoring="accuracy"
    )
    plt.figure()
    plt.plot(groottes, train_scores.mean(axis=1), marker="o", label="Training")
    plt.plot(groottes, val_scores.mean(axis=1), marker="o", label="Validatie")
    plt.xlabel("Aantal trainingsvoorbeelden")
    plt.ylabel("Accuracy")
    plt.title(naam)
    plt.legend()
    plt.tight_layout()
    plt.show()
