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
