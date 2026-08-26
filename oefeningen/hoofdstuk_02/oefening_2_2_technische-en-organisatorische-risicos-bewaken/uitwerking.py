import pandas as pd

risicos = [
    {"fase": "Data", "type": "Technisch", "risico": "Verouderde documenten", "kans": 4, "impact": 4},
    {"fase": "Data", "type": "Organisatorisch", "risico": "Geen data-eigenaar", "kans": 3, "impact": 5},
    {"fase": "Ontwikkeling", "type": "Technisch", "risico": "Prompt injection", "kans": 4, "impact": 5},
    {"fase": "Productie", "type": "Organisatorisch", "risico": "Geen incidentproces", "kans": 2, "impact": 5},
]

df = pd.DataFrame(risicos)
df["score"] = df["kans"] * df["impact"]
df = df.sort_values("score", ascending=False)
print(df.to_string(index=False))
