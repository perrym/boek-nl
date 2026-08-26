import pandas as pd

categorieen = (
    ["functioneel"] * 6
    + ["kwaliteit"] * 4
    + ["performance"] * 3
    + ["betrouwbaarheid"] * 2
    + ["security"] * 5
)

namen = [
    "Vraag met bekende bron", "Onbekende vraag", "Bronverwijzing", "Rolfilter", "Meertalige vraag", "Export rapport",
    "Faithfulness boven drempel", "Context precision", "Juiste versie", "Geen ongegronde conclusie",
    "Latency normaal", "Latency piek", "Gelijktijdige gebruikers",
    "Fallback bij LLM-fout", "Vectorstore tijdelijk niet beschikbaar",
    "Directe prompt injection", "Indirecte prompt injection", "Cross-user leakage", "Ongeautoriseerde toolcall", "Secret in output",
]

tests = pd.DataFrame({
    "test_id": [f"AT-{i:02d}" for i in range(1, 21)],
    "naam": namen,
    "categorie": categorieen,
    "verwacht": ["Te specificeren meetbaar resultaat"] * 20,
    "status": ["Niet uitgevoerd"] * 20,
})

assert len(tests) == 20
assert (tests["categorie"] == "security").sum() >= 5
assert tests[["test_id", "naam", "categorie", "verwacht"]].notna().all().all()
print(tests.to_string(index=False))
