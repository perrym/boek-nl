import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
nodes = {
    "Gebruiker": {"type": "extern"},
    "RAG-agent": {"type": "intern"},
    "Documentopslag": {"type": "intern"},
    "Vectorstore": {"type": "intern"},
    "LLM-provider": {"type": "extern"},
    "E-mailtool": {"type": "intern"},
    "Ontvanger": {"type": "extern"},
}
G.add_nodes_from((naam, attrs) for naam, attrs in nodes.items())
G.add_edges_from([
    ("Gebruiker", "RAG-agent"),
    ("Documentopslag", "Vectorstore"),
    ("RAG-agent", "Vectorstore"),
    ("Vectorstore", "RAG-agent"),
    ("RAG-agent", "LLM-provider"),
    ("LLM-provider", "RAG-agent"),
    ("RAG-agent", "E-mailtool"),
    ("E-mailtool", "Ontvanger"),
])

pos = nx.spring_layout(G, seed=3)
labels = {n: f"{n}\n({G.nodes[n]['type']})" for n in G.nodes}
nx.draw(G, pos, labels=labels, with_labels=True, node_size=3000, font_size=7, arrows=True)
plt.title("Dataflow RAG-agent met e-mailtool")
plt.margins(0.15)
plt.show()
