import pandas as pd

TOOLS = [
    {"tool": "Zoek documentatie", "schrijven": 0, "gevoeligheid": 2, "niet_omkeerbaar": 0},
    {"tool": "Lees e-mail", "schrijven": 0, "gevoeligheid": 5, "niet_omkeerbaar": 0},
    {"tool": "Stuur e-mail", "schrijven": 5, "gevoeligheid": 4, "niet_omkeerbaar": 4},
    {"tool": "Maak ticket", "schrijven": 3, "gevoeligheid": 2, "niet_omkeerbaar": 1},
    {"tool": "Verwijder account", "schrijven": 5, "gevoeligheid": 5, "niet_omkeerbaar": 5},
]

df = pd.DataFrame(TOOLS)
df["score"] = df[["schrijven", "gevoeligheid", "niet_omkeerbaar"]].sum(axis=1)
df["klasse"] = pd.cut(df["score"], bins=[-1, 4, 9, 15], labels=["Laag", "Middel", "Hoog"])
print(df.sort_values("score", ascending=False).to_string(index=False))
