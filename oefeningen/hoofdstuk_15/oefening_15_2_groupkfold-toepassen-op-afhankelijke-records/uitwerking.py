import numpy as np
from sklearn.model_selection import GroupKFold, KFold

n_klanten = 10
records_per_klant = 20
X = np.arange(n_klanten * records_per_klant).reshape(-1, 1)
y = np.tile([0, 1], n_klanten * records_per_klant // 2)
groepen = np.repeat(np.arange(n_klanten), records_per_klant)

print("Gewone KFold")
for train_idx, val_idx in KFold(n_splits=5, shuffle=True, random_state=42).split(X):
    overlap = set(groepen[train_idx]) & set(groepen[val_idx])
    print("Overlappende klanten:", sorted(overlap))

print("\nGroupKFold")
for train_idx, val_idx in GroupKFold(n_splits=5).split(X, y, groups=groepen):
    overlap = set(groepen[train_idx]) & set(groepen[val_idx])
    print("Overlappende klanten:", sorted(overlap))
