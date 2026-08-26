from dataclasses import dataclass

@dataclass
class Component:
    naam: str
    eigenaar: str
    classificatie: str

@dataclass
class Datastroom:
    bron: str
    doel: str
    data: str
    versleuteld: bool

componenten = [
    Component("Webinterface", "AI Product Team", "Intern"),
    Component("Retriever", "AI Platform", "Vertrouwelijk"),
    Component("Vectorstore", "Data Platform", "Vertrouwelijk"),
    Component("LLM-gateway", "AI Platform", "Vertrouwelijk"),
    Component("Activiteitenlog", "Security Operations", "Vertrouwelijk"),
]

stromen = [
    Datastroom("Webinterface", "Retriever", "gebruikersvraag", True),
    Datastroom("Retriever", "Vectorstore", "zoekvector en filters", True),
    Datastroom("Retriever", "LLM-gateway", "vraag en toegestane context", True),
    Datastroom("LLM-gateway", "Activiteitenlog", "metadata zonder volledige prompt", True),
]

fouten = []
for c in componenten:
    if not c.eigenaar or not c.classificatie:
        fouten.append(f"Onvolledige component: {c.naam}")
for s in stromen:
    if not s.versleuteld:
        fouten.append(f"Onversleutelde stroom: {s.bron} -> {s.doel}")

print("Architectuurfouten:", fouten)
