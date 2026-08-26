def classificeer(impact: int, autonomie: int, gevoeligheid: int) -> tuple[str, list[str]]:
    score = impact + autonomie + gevoeligheid
    if score >= 12:
        return "Hoog", ["onafhankelijke validatie", "menselijke goedkeuring", "continue monitoring"]
    if score >= 7:
        return "Middel", ["periodieke review", "logging", "fallbackprocedure"]
    return "Laag", ["basisdocumentatie", "eigenaar", "jaarlijkse review"]

toepassingen = {
    "Tekstsamenvatting": (2, 1, 2),
    "Kredietadvies": (5, 4, 5),
    "Ticketroutering": (3, 2, 2),
}

for naam, scores in toepassingen.items():
    klasse, controles = classificeer(*scores)
    print(f"{naam}: {klasse} -> {', '.join(controles)}")
