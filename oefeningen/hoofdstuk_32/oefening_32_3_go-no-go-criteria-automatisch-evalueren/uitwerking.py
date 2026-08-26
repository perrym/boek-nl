def beoordeel_release(metrics: dict) -> tuple[str, list[str]]:
    redenen = []

    # Harde blokkades
    if metrics["kritieke_securitytests_mislukt"] > 0:
        redenen.append("Kritieke securitytest mislukt")
    if not metrics["privacy_goedgekeurd"]:
        redenen.append("Privacygoedkeuring ontbreekt")
    if not metrics["autorisatie_getest"]:
        redenen.append("Autorisatie is niet aantoonbaar getest")

    # Kwaliteits- en operationele drempels
    if metrics["faithfulness"] < 0.90:
        redenen.append("Faithfulness onder 0,90")
    if metrics["p95_latency_ms"] > 2000:
        redenen.append("P95 latency boven 2000 ms")
    if metrics["bronverwijzing_percentage"] < 0.98:
        redenen.append("Te weinig antwoorden met bronverwijzing")

    return ("GO" if not redenen else "NO-GO", redenen)

release_metrics = {
    "kritieke_securitytests_mislukt": 0,
    "privacy_goedgekeurd": True,
    "autorisatie_getest": True,
    "faithfulness": 0.92,
    "p95_latency_ms": 1750,
    "bronverwijzing_percentage": 0.99,
}

besluit, redenen = beoordeel_release(release_metrics)
print("Besluit:", besluit)
print("Redenen:", redenen)
