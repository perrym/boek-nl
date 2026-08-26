import pandas as pd

set_data = [
    {"vraag_id": "Q1", "vraag": "Is MFA verplicht voor admins?", "verwacht_antwoord": "Ja", "verwachte_bronnen": ["POL-IAM-01"]},
    {"vraag_id": "Q2", "vraag": "Hoe lang worden back-ups bewaard?", "verwacht_antwoord": "30 dagen", "verwachte_bronnen": ["POL-BCM-02"]},
    {"vraag_id": "Q3", "vraag": "Wie is eigenaar van incidentbeheer?", "verwacht_antwoord": "SOC manager", "verwachte_bronnen": ["PROC-IR-03"]},
    {"vraag_id": "Q4", "vraag": "Welke API-controle voorkomt BOLA?", "verwacht_antwoord": "Objectautorisatie", "verwachte_bronnen": ["STD-API-04"]},
    {"vraag_id": "Q5", "vraag": "Wat is de minimale wachtwoordlengte?", "verwacht_antwoord": "14", "verwachte_bronnen": ["POL-IAM-01"]},
]

df = pd.DataFrame(set_data)
verplichte_velden = {"vraag_id", "vraag", "verwacht_antwoord", "verwachte_bronnen"}

assert verplichte_velden <= set(df.columns)
assert df["vraag_id"].is_unique
assert df["verwachte_bronnen"].map(bool).all()
print(df.to_string(index=False))
