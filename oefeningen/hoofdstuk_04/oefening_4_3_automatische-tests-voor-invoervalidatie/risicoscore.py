def valideer_risicoscore(waarde: object) -> float:
    if isinstance(waarde, bool):
        raise TypeError("Risicoscore mag geen boolean zijn")

    if not isinstance(waarde, (int, float)):
        raise TypeError("Risicoscore moet een getal zijn")

    if not 0 <= waarde <= 100:
        raise ValueError("Risicoscore moet tussen 0 en 100 liggen")

    return float(waarde)
