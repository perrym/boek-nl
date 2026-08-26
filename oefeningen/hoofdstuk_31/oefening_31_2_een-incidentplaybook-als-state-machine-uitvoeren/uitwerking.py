FASEN = ["detectie", "containment", "onderzoek", "herstel", "evaluatie", "gesloten"]
VERPLICHT = {
    "detectie": {"incident_id", "tijd", "melder"},
    "containment": {"toegang_geblokkeerd", "logs_veiliggesteld"},
    "onderzoek": {"scope_bepaald", "betrokken_systemen"},
    "herstel": {"oorzaak_opgelost", "hertest_geslaagd"},
    "evaluatie": {"lessons_learned", "maatregel_eigenaar"},
}


def volgende_fase(huidig: str, bewijs: dict) -> str:
    vereist = VERPLICHT.get(huidig, set())
    ontbrekend = vereist - bewijs.keys()
    if ontbrekend:
        raise ValueError(f"Fase {huidig} mist bewijs: {sorted(ontbrekend)}")
    return FASEN[FASEN.index(huidig) + 1]

bewijs_detectie = {
    "incident_id": "INC-AI-2026-004",
    "tijd": "2026-07-20T14:20:00",
    "melder": "SOC",
}
print("Volgende fase:", volgende_fase("detectie", bewijs_detectie))
