from jsonschema import ValidationError, validate

schema = {
    "type": "object",
    "required": ["bevinding", "risico", "bewijs", "aanbeveling", "prioriteit"],
    "properties": {
        "bevinding": {"type": "string", "minLength": 10},
        "risico": {"type": "string", "minLength": 5},
        "bewijs": {"type": "array", "items": {"type": "string"}, "minItems": 1},
        "aanbeveling": {"type": "string", "minLength": 10},
        "prioriteit": {"enum": ["Laag", "Middel", "Hoog", "Kritiek"]},
    },
    "additionalProperties": False,
}

geldig = {
    "bevinding": "Endpoint controleert objecteigendom niet aantoonbaar.",
    "risico": "Een gebruiker kan mogelijk gegevens van anderen lezen.",
    "bewijs": ["GET /api/users/{id}", "Alleen Bearer token vermeld"],
    "aanbeveling": "Voer server-side objectautorisatie uit voor ieder verzoek.",
    "prioriteit": "Hoog",
}

ongeldig = {"bevinding": "Onveilig", "prioriteit": "Zeer hoog"}

validate(instance=geldig, schema=schema)
print("Geldig voorbeeld: akkoord")
try:
    validate(instance=ongeldig, schema=schema)
except ValidationError as fout:
    print("Ongeldig voorbeeld:", fout.message)
