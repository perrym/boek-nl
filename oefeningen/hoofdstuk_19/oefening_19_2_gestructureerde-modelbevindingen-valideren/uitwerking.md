# Uitwerking 19.2

## Hoe werkt de code?

Gestructureerde output is pas veilig bruikbaar nadat deze lokaal is gevalideerd. Het schema controleert verplichte velden, toegestane prioriteiten en minimale inhoud. additionalProperties=False voorkomt dat onverwachte velden stil worden geaccepteerd.


## Verwachte uitvoer

Het geldige voorbeeld slaagt. Het ongeldige voorbeeld geeft een validatiefout.


## Controleer je uitkomst

- Validatie gebeurt buiten het taalmodel.
- Foutieve output wordt niet automatisch in rapportages verwerkt.
- Het schema heeft een versie.

## Verdiepingsopdracht

Voeg een veld confidence tussen 0 en 1 toe en test grenswaarden.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
