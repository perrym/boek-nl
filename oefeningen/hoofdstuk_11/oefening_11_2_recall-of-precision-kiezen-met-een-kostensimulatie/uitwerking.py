modellen = {
    "Model Hoog-Recall": {"tp": 95, "fp": 80, "fn": 5},
    "Model Hoog-Precision": {"tp": 75, "fp": 15, "fn": 25},
}

kosten_fp = 40
kosten_fn = 5000

for naam, m in modellen.items():
    precision = m["tp"] / (m["tp"] + m["fp"])
    recall = m["tp"] / (m["tp"] + m["fn"])
    totale_kosten = m["fp"] * kosten_fp + m["fn"] * kosten_fn
    print(
        f"{naam}: precision={precision:.2%}, recall={recall:.2%}, "
        f"kosten=EUR {totale_kosten:,}"
    )
