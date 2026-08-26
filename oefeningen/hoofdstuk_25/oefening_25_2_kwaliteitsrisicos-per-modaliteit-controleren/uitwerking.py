vereiste_controles = {
    "tekst": {"taaldetectie", "prompt_injection"},
    "beeld": {"resolutie", "metadata"},
    "audio": {"signaal_ruis", "taal"},
    "video": {"framerate", "tijdssynchronisatie"},
}

geimplementeerd = {
    "tekst": {"taaldetectie", "prompt_injection"},
    "beeld": {"resolutie"},
    "audio": {"signaal_ruis", "taal"},
    "video": {"framerate"},
}

for modaliteit, vereist in vereiste_controles.items():
    ontbrekend = vereist - geimplementeerd.get(modaliteit, set())
    status = "OK" if not ontbrekend else f"Ontbreekt: {sorted(ontbrekend)}"
    print(f"{modaliteit}: {status}")
