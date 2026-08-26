import pandas as pd

register = pd.DataFrame([
    {
        "app_id": "AI-001",
        "naam": "Kennisassistent",
        "eigenaar": "Kennisbeheer",
        "doel": "Documenten doorzoeken en conceptanalyses maken",
        "model": "LLM-X",
        "data_classificatie": "Vertrouwelijk",
        "risicoklasse": "Hoog",
        "laatste_review": "2026-06-01",
    },
    {
        "app_id": "AI-002",
        "naam": "Ticketclassificatie",
        "eigenaar": "IT Operations",
        "doel": "Tickets routeren",
        "model": "Classifier-v2",
        "data_classificatie": "Intern",
        "risicoklasse": "Middel",
        "laatste_review": "2026-05-15",
    },
])

assert register["app_id"].is_unique, "app_id moet uniek zijn"
assert register["eigenaar"].notna().all(), "Iedere toepassing heeft een eigenaar nodig"
print(register.to_string(index=False))
