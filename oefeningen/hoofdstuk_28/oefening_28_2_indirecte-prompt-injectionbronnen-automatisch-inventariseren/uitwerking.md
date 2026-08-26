# Uitwerking 28.2

## Hoe werkt de code?

Indirecte prompt injection kan voorkomen in inhoud die het systeem ophaalt, zoals documenten, websites, e-mail, tickets of code. De scanner zoekt met reguliere expressies naar herkenbare instructiepatronen. Wanneer één of meer patronen worden gevonden, wordt de bron als verdacht gemarkeerd.

Een patroonfilter is slechts een eerste verdedigingslaag. Het kan kwaadaardige instructies missen en ook onschuldige tekst ten onrechte markeren. Externe inhoud moet daarom altijd als onbetrouwbare data worden behandeld en mag nooit zelfstandig bepalen welke tools of rechten mogen worden gebruikt.


## Verwachte uitvoer

De PDF, e-mail en het codecommentaar worden als verdacht gemarkeerd. De webpagina en het ticket bevatten geen patroon dat door de huidige regels wordt herkend.

Dat laatste is technisch preciezer dan “waarschijnlijk gemarkeerd”, want met deze vaste code is de uitkomst voorspelbaar.

.


## Controleer je uitkomst

- De PDF wordt als verdacht gemarkeerd.
- De e-mail wordt als verdacht gemarkeerd.
- Het codecommentaar wordt als verdacht gemarkeerd.
- De webpagina en het ticket worden niet gemarkeerd.
- Per bron is zichtbaar welke patronen zijn gevonden.
- De scanner wordt alleen als detectielaag gebruikt en niet als autorisatiemechanisme..

## Verdiepingsopdracht

Voeg Unicode-normalisatie toe en test versluierde varianten van verdachte instructies. Voeg ook enkele voorbeelden toe die bewust een fout-positieve of fout-negatieve detectie veroorzaken.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
