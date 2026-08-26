import pandas as pd

gegevens = pd.DataFrame({
    "incident_id": [1, 2, 2, 4],
    "categorie": ["IAM", "Netwerk", "Netwerk", None],
    "doorlooptijd": [4.5, 8.0, None, 2.0],
})

rapport = pd.DataFrame({
    "datatype": gegevens.dtypes.astype(str),
    "ontbrekend": gegevens.isna().sum(),
    "percentage_ontbrekend": gegevens.isna().mean().mul(100).round(1),
    "uniek": gegevens.nunique(dropna=True),
})

print(rapport)
print("Dubbele rijen:", gegevens.duplicated().sum())
