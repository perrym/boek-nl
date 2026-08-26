import pandas as pd

gegevens = pd.DataFrame({
    "categorie": ["IAM", "Netwerk", "IAM", None, "Applicatie", "IAM"]
})

categorie = gegevens["categorie"].fillna("Onbekend")
samenvatting = categorie.value_counts().rename_axis("categorie").reset_index(name="aantal")
samenvatting["percentage"] = (samenvatting["aantal"] / len(gegevens) * 100).round(1)

print(samenvatting)
