import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = make_classification(
    n_samples=700, n_features=20, n_informative=6,
    flip_y=0.08, random_state=42
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)

dieptes = range(1, 21)
train_scores = []
test_scores = []
for diepte in dieptes:
    model = DecisionTreeClassifier(max_depth=diepte, random_state=42)
    model.fit(X_train, y_train)
    train_scores.append(model.score(X_train, y_train))
    test_scores.append(model.score(X_test, y_test))

plt.plot(dieptes, train_scores, marker="o", label="Training")
plt.plot(dieptes, test_scores, marker="o", label="Test")
plt.xlabel("Maximale diepte")
plt.ylabel("Accuracy")
plt.title("Boomdiepte en overfitting")
plt.legend()
plt.tight_layout()
plt.show()
