import pandas as pd

gegevens = pd.DataFrame({
    "doorlooptijd": ["4.5", "8", "onbekend", "2"],
    "datum": ["2026-01-10", "2026-02-15", "geen datum", "2026-04-01"],
})

gegevens["doorlooptijd_num"] = pd.to_numeric(
    gegevens["doorlooptijd"], errors="coerce"
)
gegevens["datum_clean"] = pd.to_datetime(
    gegevens["datum"], errors="coerce"
)

print(gegevens)
print("Ongeldige doorlooptijden:", gegevens["doorlooptijd_num"].isna().sum())
print("Ongeldige datums:", gegevens["datum_clean"].isna().sum())
