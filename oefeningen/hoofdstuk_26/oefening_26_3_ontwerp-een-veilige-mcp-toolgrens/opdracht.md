# Oefening 26.3 - Ontwerp een veilige MCP-toolgrens

## Opdracht

Ontwerp een fictieve MCP-server met drie tools: document zoeken, ticket aanmaken en accountstatus wijzigen. Leg per tool inputschema, identiteit, scope, toegestane parameters, logging, approval en foutgedrag vast. Beschrijf hoe je voorkomt dat kwaadaardige tekst uit een document de agent een gevoelige tool laat uitvoeren.

## Controleer je uitkomst

- Toolrechten zijn technisch begrensd.
- Onbetrouwbare tooloutput kan geen autorisatiebeslissing overschrijven.
- Schrijfacties gebruiken approval en een idempotency-key.
- De workflow heeft een maximum aantal stappen en een stopconditie.

## Werkwijze

1. Probeer de opdracht eerst zelf.
2. Voer de code uit en controleer de tussenresultaten.
3. Voeg minimaal één randgeval toe.
4. Open pas daarna `uitwerking.py` en `uitwerking.md`.
