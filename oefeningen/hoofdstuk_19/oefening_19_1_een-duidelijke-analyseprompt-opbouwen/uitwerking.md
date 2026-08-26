# Uitwerking 19.1

## Hoe werkt de code?

De functie maakt prompts consistent en voorkomt dat ieder endpoint met andere instructies wordt beoordeeld. De regel over ontbrekende informatie beperkt ongefundeerde conclusies. In productie moeten gebruikersdata en opgehaalde documenten duidelijk worden afgebakend van systeeminstructies.


## Verwachte uitvoer

De prompt bevat alle verplichte secties en de assertions slagen.


## Controleer je uitkomst

- Instructies en context zijn gescheiden.
- De prompt vraagt om bewijs en onbekenden.
- Gevoelige data wordt niet onnodig opgenomen.

## Verdiepingsopdracht

Voeg een parameter toe voor taal en laat de functie Nederlands of Engels genereren.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
