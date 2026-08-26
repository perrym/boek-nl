# Uitwerking 4.3

## Verwachte uitvoer

Pytest voert vijf testgevallen uit:

1. geldige score;

2. negatieve score;

3. tekstinvoer;

4. grenswaarde 0;

5. grenswaarde 100.

De uitvoer eindigt normaal met:

5 passed

Waarom zijn meerdere tests nodig?

Alleen testen met de waarde 75 bewijst niet dat de functie veilig omgaat met:

negatieve waarden;

te hoge waarden;

tekst;

booleans;

lege waarden;

grenswaarden.

Een goede testset bevat daarom normale gevallen, grenswaarden en foutscenario's.


## Controleer je uitkomst

- Controleer of:
- iedere test één duidelijke verwachting controleert;
- de tests onafhankelijk van elkaar kunnen worden uitgevoerd;
- het juiste fouttype wordt gecontroleerd;
- de grenswaarden afzonderlijk worden getest;
- de functienaam duidelijk is;
- de tests geen handmatige invoer nodig hebben.

## Verdiepingsopdracht

Voeg tests toe voor:

None;

True;

False;

100.01;

een decimale score zoals 42.5.

Mogelijke uitwerking:


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
