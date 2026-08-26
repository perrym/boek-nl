import pandas as pd

cases = [
    {"test": "Normale scherpe afbeelding", "categorie": "functioneel", "verwacht": "juiste klasse"},
    {"test": "Donkere afbeelding", "categorie": "robuustheid", "verwacht": "confidence daalt gecontroleerd"},
    {"test": "Beschadigd bestand", "categorie": "foutafhandeling", "verwacht": "veilige foutmelding"},
    {"test": "Afbeelding met verborgen metadata", "categorie": "security", "verwacht": "metadata wordt niet vertrouwd"},
    {"test": "Onbekende objectklasse", "categorie": "out-of-distribution", "verwacht": "onzeker of weigering"},
]

verplicht = {"functioneel", "robuustheid", "foutafhandeling", "security", "out-of-distribution"}
df = pd.DataFrame(cases)
aanwezig = set(df["categorie"])
ontbrekend = verplicht - aanwezig

print(df.to_string(index=False))
print("Ontbrekende categorieën:", sorted(ontbrekend))
assert not ontbrekend, f"Testmatrix is onvolledig: {ontbrekend}"
