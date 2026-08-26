from datetime import date

VERPLICHT = {"document_id", "titel", "eigenaar", "classificatie", "versie", "geldig_vanaf"}
CLASSIFICATIES = {"Intern", "Vertrouwelijk", "Openbaar"}


def valideer_metadata(metadata: dict) -> list[str]:
    fouten = []
    ontbrekend = VERPLICHT - metadata.keys()
    if ontbrekend:
        fouten.append(f"Ontbrekende velden: {sorted(ontbrekend)}")
    if metadata.get("classificatie") not in CLASSIFICATIES:
        fouten.append("Ongeldige classificatie")
    try:
        date.fromisoformat(metadata.get("geldig_vanaf", ""))
    except ValueError:
        fouten.append("geldig_vanaf moet YYYY-MM-DD zijn")
    return fouten

record = {
    "document_id": "DOC-2026-014",
    "titel": "Identity Access Review",
    "eigenaar": "Kennisbeheer",
    "classificatie": "Vertrouwelijk",
    "versie": "1.2",
    "geldig_vanaf": "2026-05-01",
    "toegestane_rollen": ["reviewer", "review_manager"],
}

print(valideer_metadata(record))
