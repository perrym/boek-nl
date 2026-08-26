import numpy as np
from sklearn.metrics import accuracy_score, log_loss

y_true = np.array([1, 1, 0, 0])
proba_oud = np.array([0.51, 0.55, 0.49, 0.45])
proba_nieuw = np.array([0.80, 0.70, 0.20, 0.10])

for naam, proba in {"Oud": proba_oud, "Nieuw": proba_nieuw}.items():
    voorspelling = (proba >= 0.5).astype(int)
    print(
        f"{naam}: accuracy={accuracy_score(y_true, voorspelling):.2f}, "
        f"log_loss={log_loss(y_true, proba):.3f}"
    )
