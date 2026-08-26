import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
G.add_edges_from([
    ("Gebruiker", "Orchestrator"),
    ("Orchestrator", "Code-agent"),
    ("Orchestrator", "Dependency-agent"),
    ("Orchestrator", "Policy-agent"),
    ("Code-agent", "Reviewer"),
    ("Dependency-agent", "Reviewer"),
    ("Policy-agent", "Reviewer"),
    ("Reviewer", "Orchestrator"),
    ("Orchestrator", "Rapport"),
])

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=2600, font_size=8, arrows=True)
plt.title("Multi-agentarchitectuur voor software-securityreview")
plt.margins(0.15)
plt.show()
