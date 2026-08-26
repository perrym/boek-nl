import pandas as pd

incidenten = pd.DataFrame({
    "incident_id": [1, 2, 3, 3],
    "team": ["A", "B", None, None],
    "ernst": [2, 4, 5, 5],
    "doorlooptijd": [3.0, 9.5, 21.0, 21.0],
})


def eda_rapport(df: pd.DataFrame) -> dict:
    return {
        "shape": df.shape,
        "datatypes": df.dtypes.astype(str).to_dict(),
        "ontbrekend": df.isna().sum().to_dict(),
        "dubbele_rijen": int(df.duplicated().sum()),
        "beschrijving": df.describe(include="all").to_dict(),
    }

rapport = eda_rapport(incidenten)
for onderdeel, waarde in rapport.items():
    print(f"\n{onderdeel}:\n{waarde}")
