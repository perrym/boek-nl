# Uitwerking 5.4

## Hoe werkt de code?

X.mean(axis=0) berekent één gemiddelde per kolom. De array mean heeft daardoor shape (3,). NumPy gebruikt broadcasting om deze drie waarden van iedere rij in X af te trekken. De laatste regel controleert of de gecentreerde kolommen gemiddeld ongeveer nul zijn.


## Controleer je uitkomst

- De oorspronkelijke matrix heeft shape (3, 3).
- Het kolomgemiddelde heeft shape (3,).
- De controle levert waarden op die nul of zeer dicht bij nul liggen.

## Verdiepingsopdracht

Voeg een kolom met constante waarden toe en onderzoek wat er gebeurt wanneer je daarna ook door de standaardafwijking deelt.

Van NumPy naar data-analyse

In dit hoofdstuk hebben we geleerd hoe NumPy numerieke data opslaat en verwerkt. We kunnen nu arrays maken, shapes en datatypes controleren, gegevens selecteren, vectoriseren en bewust omgaan met views, kopieën en broadcasting.

In de volgende stap gaan we deze rekenbasis gebruiken voor datasets met kolomnamen, ontbrekende waarden en verschillende soorten gegevens. Daarvoor is Pandas bijzonder geschikt. Pandas bouwt voort op veel ideeën uit NumPy, maar voegt datastructuren toe die beter aansluiten op tabellen zoals CSV- en Excelbestanden.

De centrale vraag verschuift daarmee van: Hoe reken ik efficiënt met numerieke arrays? naar: Hoe lees, controleer, bewerk en analyseer ik een echte dataset op een betrouwbare manier?


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
