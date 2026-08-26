import numpy as np
from sklearn.model_selection import train_test_split

X = np.arange(1000).reshape(-1, 1)
y = np.array([0] * 950 + [1] * 50)

_, X_test_a, _, y_test_a = train_test_split(
    X, y, test_size=0.1, random_state=8
)
_, X_test_b, _, y_test_b = train_test_split(
    X, y, test_size=0.1, random_state=8, stratify=y
)

print(f"Totaal positief: {y.mean():.1%}")
print(f"Zonder stratify: {y_test_a.mean():.1%}")
print(f"Met stratify: {y_test_b.mean():.1%}")
