import pandas as pd

levenscyclus = [

{"fase": "Probleemdefinitie", "eigenaar": "Product owner", "product": "Use-casebeschrijving", "exitcriterium": "Doel en scope goedgekeurd"},

{"fase": "Data", "eigenaar": "Data owner", "product": "Bronregister", "exitcriterium": "Rechten en kwaliteit beoordeeld"},

{"fase": "Ontwikkeling", "eigenaar": "AI-team", "product": "Werkend prototype", "exitcriterium": "Unit- en securitytests geslaagd"},

{"fase": "Evaluatie", "eigenaar": "Model validator", "product": "Evaluatierapport", "exitcriterium": "Drempelwaarden behaald"},

{"fase": "Productie", "eigenaar": "Service owner", "product": "Release", "exitcriterium": "Go/no-go akkoord"},

{"fase": "Monitoring", "eigenaar": "Operations", "product": "Dashboard", "exitcriterium": "Alerts en incidentproces actief"},

]

df = pd.DataFrame(levenscyclus)

print(df.to_string(index=False))
