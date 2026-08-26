scenario_a = {
    "false_positives": 120,
    "false_negatives": 8,
    "kosten_false_positive": 25,
    "kosten_false_negative": 2500,
}

scenario_b = {
    "false_positives": 40,
    "false_negatives": 16,
    "kosten_false_positive": 25,
    "kosten_false_negative": 2500,
}


def totale_kosten(scenario: dict) -> int:
    fp_kosten = scenario["false_positives"] * scenario["kosten_false_positive"]
    fn_kosten = scenario["false_negatives"] * scenario["kosten_false_negative"]
    return fp_kosten + fn_kosten

for naam, scenario in {"A": scenario_a, "B": scenario_b}.items():
    print(f"Scenario {naam}: EUR {totale_kosten(scenario):,}")
