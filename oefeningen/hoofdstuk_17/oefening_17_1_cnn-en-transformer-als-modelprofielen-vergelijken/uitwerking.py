import pandas as pd

vergelijking = pd.DataFrame([
    {
        "model": "CNN",
        "lokale_patronen": 5,
        "lange_afstandsrelaties": 2,
        "databehoefte": 3,
        "rekencapaciteit": 3,
        "typische_toepassing": "beeldclassificatie",
    },
    {
        "model": "Transformer",
        "lokale_patronen": 3,
        "lange_afstandsrelaties": 5,
        "databehoefte": 5,
        "rekencapaciteit": 5,
        "typische_toepassing": "tekst en multimodale modellen",
    },
])

print(vergelijking.to_string(index=False))
print("\nGemiddelde technische zwaarte:")
print(vergelijking.set_index("model")[["databehoefte", "rekencapaciteit"]].mean(axis=1))
