"""Voorbeeld voor oefening 19.3.

Deze uitwerking bouwt de prompts op zonder een specifieke LLM-provider.
Vervang run_model() later door de API of het lokale model dat je gebruikt.
"""

SOURCE_TEXT = """
De webapplicatie heeft MFA voor beheerders. Logging is actief, maar logs worden
slechts zeven dagen bewaard. Er is geen periodieke controle op mislukte logins.
""".strip()


def run_model(prompt: str) -> str:
    raise NotImplementedError("Koppel hier je eigen LLM of lokale model.")


single_prompt = f"""
Analyseer de onderstaande tekst.
1. Noem de feiten.
2. Geef een analyse.
3. Geef aanbevelingen.
Gebruik alleen informatie uit de tekst en benoem ontbrekende informatie.

TEKST:
{SOURCE_TEXT}
""".strip()

fact_prompt = f"""
Haal uitsluitend controleerbare feiten uit de tekst.
Geef per feit een korte bronverwijzing naar de zin waarop het feit is gebaseerd.
Voeg geen interpretatie toe.

TEKST:
{SOURCE_TEXT}
""".strip()

analysis_prompt = """
Analyseer uitsluitend de aangeleverde feiten.
Benoem:
- mogelijke risico's;
- ontbrekende informatie;
- welke conclusies nog niet bewezen zijn.

FEITEN:
{facts}
""".strip()

review_prompt = """
Controleer de analyse op:
- nieuwe feiten die niet in de feitenlijst staan;
- conclusies zonder bewijs;
- ontbrekende onzekerheden;
- aanbevelingen die niet uit de analyse volgen.

Geef per punt PASS of FAIL met een korte reden.

FEITEN:
{facts}

ANALYSE:
{analysis}
""".strip()


def build_chain_prompts(facts: str, analysis: str) -> dict[str, str]:
    return {
        "fact_extractie": fact_prompt,
        "analyse": analysis_prompt.format(facts=facts),
        "review": review_prompt.format(facts=facts, analysis=analysis),
    }


if __name__ == "__main__":
    print("Single prompt:\n")
    print(single_prompt)
    print("\nPrompt chain start:\n")
    print(fact_prompt)
