import pandas as pd

criteria = pd.DataFrame([
    {"criterium": "Dataprivacy", "gewicht": 5, "cloud": 3, "lokaal": 5},
    {"criterium": "Schaalbaarheid", "gewicht": 4, "cloud": 5, "lokaal": 3},
    {"criterium": "Beheerlast", "gewicht": 3, "cloud": 5, "lokaal": 2},
    {"criterium": "Offline beschikbaar", "gewicht": 2, "cloud": 1, "lokaal": 5},
    {"criterium": "Modelkwaliteit", "gewicht": 5, "cloud": 5, "lokaal": 3},
])

for optie in ["cloud", "lokaal"]:
    criteria[f"gewogen_{optie}"] = criteria["gewicht"] * criteria[optie]

print(criteria.to_string(index=False))
print("Cloud totaal:", criteria["gewogen_cloud"].sum())
print("Lokaal totaal:", criteria["gewogen_lokaal"].sum())
