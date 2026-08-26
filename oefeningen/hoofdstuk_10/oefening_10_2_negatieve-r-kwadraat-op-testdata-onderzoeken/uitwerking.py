import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Training: positieve relatie
X_train = np.arange(0, 10).reshape(-1, 1)
y_train = 2 * X_train.ravel() + 1

# Test: de relatie is omgekeerd
X_test = np.arange(10, 15).reshape(-1, 1)
y_test = -3 * X_test.ravel() + 50

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

baseline = np.full_like(y_test, fill_value=y_test.mean(), dtype=float)

print("Modelvoorspellingen:", np.round(y_pred, 1))
print(f"R-kwadraat model: {r2_score(y_test, y_pred):.3f}")
print(f"MSE model: {mean_squared_error(y_test, y_pred):.3f}")
print(f"MSE testgemiddelde: {mean_squared_error(y_test, baseline):.3f}")
