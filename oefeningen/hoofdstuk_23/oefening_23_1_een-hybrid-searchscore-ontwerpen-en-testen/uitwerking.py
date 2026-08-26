import pandas as pd

resultaten = pd.DataFrame([
    {"document": "A", "semantisch": 0.88, "lexicaal": 0.20, "actualiteit": 0.90},
    {"document": "B", "semantisch": 0.72, "lexicaal": 1.00, "actualiteit": 0.70},
    {"document": "C", "semantisch": 0.81, "lexicaal": 0.40, "actualiteit": 0.30},
    {"document": "D", "semantisch": 0.55, "lexicaal": 0.80, "actualiteit": 1.00},
    {"document": "E", "semantisch": 0.60, "lexicaal": 0.10, "actualiteit": 0.60},
])

gewichten = {"semantisch": 0.6, "lexicaal": 0.3, "actualiteit": 0.1}
resultaten["hybrid"] = sum(resultaten[k] * w for k, w in gewichten.items())
resultaten = resultaten.sort_values("hybrid", ascending=False)

print(resultaten.round(3).to_string(index=False))

collecties = [100, 100_000, 10_000_000]
vragen_per_dag = 5_000
top_k = 100
milliseconden_per_paar = 4

for documenten in collecties:
    volledig_per_dag = documenten * vragen_per_dag
    rerank_per_dag = top_k * vragen_per_dag
    tijd_volledig_uur = volledig_per_dag * milliseconden_per_paar / 1000 / 3600
    tijd_rerank_uur = rerank_per_dag * milliseconden_per_paar / 1000 / 3600
    print(
        f"Documenten={documenten:,}: volledig={tijd_volledig_uur:,.1f} uur, "
        f"top-{top_k} rerank={tijd_rerank_uur:,.1f} uur"
    )
