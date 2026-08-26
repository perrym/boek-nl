import pandas as pd

werkzaamheden = [
    {"taak": "Doorlooptijd van een project voorspellen", "categorie": "regressie"},
    {"taak": "Phishingmail herkennen", "categorie": "classificatie"},
    {"taak": "Vergelijkbare incidenten groeperen", "categorie": "clustering"},
    {"taak": "Conceptbevinding schrijven", "categorie": "generatieve AI"},
    {"taak": "Factuurbedrag optellen", "categorie": "geen AI"},
    {"taak": "Risicoklasse van een API bepalen", "categorie": "classificatie"},
]

df = pd.DataFrame(werkzaamheden)
print(df)
print("\nAantal per categorie:")
print(df["categorie"].value_counts())
