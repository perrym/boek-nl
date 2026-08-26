# Uitwerking 2.1

## Hoe werkt de code?

De code legt de belangrijkste fasen van een AI-project vast in een lijst met dictionaries. Voor iedere fase worden vier onderdelen beschreven: de fase, de eigenaar, het op te leveren product en het exitcriterium.

Met:

Python

df = pd.DataFrame(levenscyclus)

wordt deze lijst omgezet naar een Pandas DataFrame. Daardoor ontstaat een overzichtelijke tabel waarin de verschillende fasen eenvoudig kunnen worden bekeken, gecontroleerd en later uitgebreid.

Met:

print(df.to_string(index=False))

wordt de volledige tabel weergegeven zonder de standaard rijnummers van Pandas.

Een levenscyclus wordt bestuurbaar wanneer iedere fase een eigenaar, concreet op te leveren product en exitcriterium heeft. Exitcriteria helpen voorkomen dat een project te vroeg doorgaat naar een volgende fase, bijvoorbeeld van ontwikkeling naar productie.


## Verwachte uitvoer

Een tabel met zes fasen, elk met een verantwoordelijke, product en controleerbaar exitcriterium. Voor iedere fase worden de eigenaar, het product en het exitcriterium weergegeven.


## Controleer je uitkomst

- Iedere fase heeft precies een eigenaar.
- Exitcriteria zijn meetbaar of aantoonbaar.
- Monitoring staat als volwaardige fase in het plan.

## Verdiepingsopdracht

Voeg een kolom status toe, bijvoorbeeld met de waarden Niet gestart, Bezig en Afgerond. Schrijf daarna een functie die controleert of een fase pas mag starten wanneer de voorgaande fase is afgerond.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
