context = {
    "beleid_versie": "2026.3",
    "mfa_verplicht": True,
    "eigenaar": "Identity & Access Management",
}


def beantwoord(vraag: str, context: dict) -> str:
    vraag_lager = vraag.lower()
    if "versie" in vraag_lager:
        return f"De beleidsversie is {context['beleid_versie']}."
    if "mfa" in vraag_lager:
        return "MFA is verplicht." if context["mfa_verplicht"] else "MFA is niet verplicht."
    if "eigenaar" in vraag_lager:
        return f"De eigenaar is {context['eigenaar']}."
    return "Niet te beantwoorden op basis van de beschikbare context."

for vraag in ["Welke versie geldt?", "Is MFA verplicht?", "Wanneer is het beleid goedgekeurd?"]:
    print(vraag, "->", beantwoord(vraag, context))
