import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
dagen = pd.date_range("2026-06-01", periods=30, freq="D")
df = pd.DataFrame({
    "datum": dagen,
    "faithfulness": np.clip(rng.normal(0.93, 0.03, 30), 0, 1),
    "latency_ms": rng.normal(850, 140, 30),
    "kosten_eur": rng.normal(110, 18, 30),
    "security_blocks": rng.poisson(2, 30),
})

df["faithfulness_7d"] = df["faithfulness"].rolling(7).mean()
df["latency_7d"] = df["latency_ms"].rolling(7).mean()
df["alert"] = (
    (df["faithfulness"] < 0.88)
    | (df["latency_ms"] > 1200)
    | (df["kosten_eur"] > 150)
)

print(df.tail(10).round(3).to_string(index=False))
print("Aantal alertdagen:", int(df["alert"].sum()))
