# Uitwerking 30.2

## Hoe werkt de code?

De functie telt de scores voor impact, autonomie en datagevoeligheid op. Op basis van de totaalscore krijgt een toepassing de klasse Laag, Middel of Hoog. Aan iedere klasse wordt vervolgens een aantal beheersmaatregelen gekoppeld.

Deze somscore is alleen bedoeld als eenvoudige eerste triage. Een dergelijke score is geen juridische classificatie. Wettelijke verplichtingen, fundamentele rechten of sectorspecifieke eisen moeten afzonderlijk worden beoordeeld en kunnen zwaardere maatregelen noodzakelijk maken.

een zwaardere categorie plaatsen. De code maakt de redenering zichtbaar en herhaalbaar.


## Verwachte uitvoer

Tekstsamenvatting: Laag -> basisdocumentatie, eigenaar, jaarlijkse review

Kredietadvies: Hoog -> onafhankelijke validatie, menselijke goedkeuring, continue monitoring

Ticketroutering: Middel -> periodieke review, logging, fallbackprocedure

Dus niet “waarschijnlijk Middel”: met 3 + 2 + 2 = 7 is Ticketroutering volgens jouw functie gewoon Middel.


## Controleer je uitkomst

- De drie criteria worden voor iedere toepassing beoordeeld.
- Dezelfde scores leiden steeds tot dezelfde classificatie.
- Iedere risicoklasse heeft passende beheersmaatregelen.
- De somscore wordt gebruikt als eerste risico-inschatting en niet als juridische classificatie.

## Verdiepingsopdracht

Voeg een hard criterium toe waardoor bepaalde toepassingen nooit automatisch als Laag kunnen worden geclassificeerd, ongeacht hun somscore. Beschrijf waarom zo'n aanvullende regel nodig kan zijn.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
