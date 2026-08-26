vraag = "Hoe lang worden back-ups bewaard?"
retrieved_docs = [
    {"id": "POL-BCM-02", "tekst": "Back-ups worden 30 dagen bewaard."},
    {"id": "POL-BCM-01", "tekst": "Back-ups worden iedere nacht gemaakt."},
]
verwachte_bron = "POL-BCM-02"
verwacht_antwoord = "30 dagen"
model_antwoord = "Back-ups worden 90 dagen bewaard."

retrieval_hit = any(doc["id"] == verwachte_bron for doc in retrieved_docs)
answer_exact = verwacht_antwoord.lower() in model_antwoord.lower()

print("Retrieval hit:", retrieval_hit)
print("Antwoord bevat ground truth:", answer_exact)
print("Conclusie:", "generatiefout" if retrieval_hit and not answer_exact else "nader onderzoeken")
