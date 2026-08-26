def bouw_analyseprompt(endpoint: str, methode: str, authenticatie: str) -> str:
    return f"""Je bent een ervaren API-securityspecialist.

Taak:
Beoordeel het endpoint op mogelijke OWASP API Security Top 10-risico's.

Context:
- Endpoint: {endpoint}
- Methode: {methode}
- Authenticatie: {authenticatie}

Regels:
- Gebruik alleen de aangeleverde informatie.
- Benoem ontbrekende informatie expliciet.
- Maak onderscheid tussen bewijs en aanname.

Uitvoer:
1. Bevinding
2. Risico
3. Bewijs
4. Ontbrekende informatie
5. Aanbeveling
6. Prioriteit
"""

prompt = bouw_analyseprompt("/api/users/{id}", "GET", "Bearer token")
print(prompt)

for verplicht in ["Taak:", "Context:", "Regels:", "Uitvoer:"]:
    assert verplicht in prompt
