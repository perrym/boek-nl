def kies_techniek(actuele_kennis: bool, vaste_stijl: bool, taak_is_nieuw: bool) -> str:
    if actuele_kennis:
        return "RAG"
    if vaste_stijl and not taak_is_nieuw:
        return "fine-tuning"
    return "prompting"

scenarios = [
    (True, False, False, "Vragen over actuele procedures"),
    (False, True, False, "Steeds dezelfde rapportagestijl"),
    (False, False, True, "Eenmalige samenvatting"),
    (True, True, False, "Actuele kennis in vaste stijl"),
    (False, False, False, "Algemene brainstorm"),
]

for actueel, stijl, nieuw, omschrijving in scenarios:
    advies = kies_techniek(actueel, stijl, nieuw)
    print(f"{omschrijving}: {advies}")
