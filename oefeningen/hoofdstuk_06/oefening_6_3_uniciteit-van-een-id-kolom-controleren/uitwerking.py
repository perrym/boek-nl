import pandas as pd

gegevens = pd.DataFrame({
    "incident_id": [1001, 1002, 1002, None],
    "omschrijving": ["MFA", "Firewall", "Firewall kopie", "Onbekend"],
})

problemen = gegevens[
    gegevens["incident_id"].isna()
    | gegevens["incident_id"].duplicated(keep=False)
]

if problemen.empty:
    print("Controle geslaagd: alle ID's zijn uniek en gevuld")
else:
    print("Controle mislukt:")
    print(problemen.to_string(index=False))
    raise SystemExit(1)
