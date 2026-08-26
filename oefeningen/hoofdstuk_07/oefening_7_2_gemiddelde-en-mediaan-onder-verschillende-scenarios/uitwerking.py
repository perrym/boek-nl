import pandas as pd

normaal = [4, 5, 6, 6, 7, 8, 9]
met_uitschieter = normaal + [100]

resultaten = pd.DataFrame([
    {"scenario": "Normaal", "gemiddelde": sum(normaal) / len(normaal), "mediaan": pd.Series(normaal).median()},
    {"scenario": "Met uitschieter", "gemiddelde": sum(met_uitschieter) / len(met_uitschieter), "mediaan": pd.Series(met_uitschieter).median()},
])

print(resultaten.round(2).to_string(index=False))
