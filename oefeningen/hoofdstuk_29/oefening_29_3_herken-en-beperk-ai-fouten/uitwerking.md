# Uitwerking 29.3

## Controleer je uitkomst

- Ontbrekende feiten worden niet zelf aangevuld.
- Iedere belangrijke conclusie verwijst naar beschikbaar bewijs.
- Een retrievalfout wordt niet automatisch als een hallucinatie van het model beschreven.
- Onvoldoende bewijs leidt tot abstention (geen antwoord geven) of menselijke beoordeling.
- Dezelfde cases kunnen na een wijziging in de beoordelingsregels, prompt of het model opnieuw worden getest.

## Verdiepingsopdracht

Laat dezelfde cases eventueel door een lokaal of extern taalmodel beoordelen en vergelijk de resultaten met je eigen classificatie.

30. AI Governance, privacy en modelrisico

Leerdoelen
• Rollen en verantwoordelijkheden voor AI definiëren.
• Risicoklassen en controles koppelen.
• Privacy en wettelijke eisen vroeg meenemen.

Governance moet meegroeien met de mogelijke impact van een AI-toepassing. Een interne samenvattingsfunctie vraagt niet dezelfde mate van beheersing en bewijslast als een systeem dat invloed heeft op klanten, medewerkers of medische beslissingen. Wat altijd nodig blijft, zijn duidelijk eigenaarschap, vastgelegde risicobesluiten en voldoende bewijs om gemaakte keuzes later te kunnen toetsen.

Governance maakt van een AI-experiment een beheersbare dienst waarvoor duidelijk is wie verantwoordelijk is. Je moet kunnen vaststellen wie de eigenaar is, welk risico is geaccepteerd, welke beheersmaatregelen gelden en welk bewijs de genomen beslissingen gedurende de levenscyclus ondersteunt.

30.1 Inventaris en classificatie

Houd een register bij met het doel, de eigenaar, het gebruikte model, de provider, de gebruikte data, de gebruikersgroep, de impact, het risiconiveau en de actuele status.

Voor organisaties in de Europese Unie is deze inventarisatie ook relevant voor de AI Act. Sinds 2 augustus 2026 is een groot deel van de verordening van toepassing en gelden onder andere nieuwe transparantieverplichtingen. De Europese Commissie en nationale autoriteiten zijn vanaf die datum ook met de handhaving van toepasselijke regels begonnen. Niet alle verplichtingen kennen echter dezelfde ingangsdatum.

Leg daarom naast het technische risicoprofiel ook de juridische rol en toepasselijke verplichtingen vast, bijvoorbeeld aanbieder (provider) of gebruiksverantwoordelijke (deployer).

Controleer voor AI-systemen met een hoog risico en GPAI-modellen altijd de actuele verplichtingen, overgangstermijnen en richtlijnen. De termen aanbieder en gebruiksverantwoordelijke zijn de officiële Nederlandse termen uit de AI Act

30.2 Rollen

De business owner bepaalt het doel en accepteert het restrisico. De model owner is verantwoordelijk voor de prestaties van het model. De data owner ziet toe op correct en toegestaan datagebruik. Security, Privacy, Legal en control voeren een onafhankelijke toets uit en leveren waar nodig kritische tegenspraak.

30.3 Privacy by design

Minimaliseer persoonsgegevens, bepaal de verwerkingsgrondslag, beperk bewaartermijnen en ondersteun de rechten van betrokkenen, zoals inzage en verwijdering waar deze van toepassing zijn. Beoordeel ook eventuele internationale doorgifte van persoonsgegevens.

30.4 Model Risk Management

Documenteer aannames, beperkingen, validatie, wijzigingen, monitoring, afwijkingen en uitfasering.

30.5 Human oversight

Menselijke controle moet betekenisvol zijn. De beoordelaar moet voldoende tijd, informatie, bevoegdheid en deskundigheid hebben om een AI-uitkomst kritisch te beoordelen, te corrigeren of te verwerpen.

Risicogestuurde controle

Laag risico: interne tekstsuggesties zonder persoonsgegevens.

Middelgroot risico: RAG op basis van interne procedures.

Hoog risico: geautomatiseerde besluitvorming met financiële of personele gevolgen. Naarmate het risico toeneemt, worden ook de eisen aan validatie, logging, monitoring en goedkeuring strenger.

Praktische aandachtspunten
Leg vast hoe beleid in de praktijk wordt toegepast, bijvoorbeeld via registers, beoordelingen, goedkeuringen, monitoring en incidentafhandeling.

Verdieping en voorbeelden

Kernvraag: Wie mag welk besluit nemen, op basis van welk bewijs en met welke onafhankelijke challenge?

Figuur 30. Verdeling van verantwoordelijkheden over drie verdedigingslijnen.

AI-governance verbindt strategie, eigenaarschap, risico en verantwoording. Classificeer use-cases op basis van hun impact en bepaal welke goedkeuring, documentatie en monitoring per klasse nodig zijn. Een interne samenvattingstool stelt bijvoorbeeld andere eisen dan een systeem dat klanten selecteert of medewerkers beoordeelt.

Leg verantwoordelijkheden vast voor de business owner, model owner, data owner, security, privacy, compliance en operations. Beheer modelkaarten, datasheets, evaluaties, risicobesluiten en uitzonderingen. Governance moet niet alleen op papier bestaan: toegangsrechten, technische waarborgen en releaseprocessen moeten aansluiten op de afgesproken verantwoordelijkheden.

Voorbeeld: minimaal dossier voor een hoog-impact use-case

Het dossier maakt besluitvorming en latere beoordeling herleidbaar.

Document

Inhoud

Eigenaar

Use-casebeschrijving

Doel, gebruikers, beslissingen en verboden gebruik.

Business owner.

Data assessment

Herkomst, kwaliteit, rechtmatigheid en representativiteit.

Data owner en privacy.

Model evaluation

Metrics, subgroepen, foutanalyse en beperkingen.

Model owner.

Security assessment

Threat model, tests en open risico's.

Security.

Go-livebesluit

Acceptatiecriteria, monitoring en rollback.

Bevoegde besluitnemer.

In de praktijk

Controleer zowel opzet, bestaan als werking. Een beleid kan volledig zijn terwijl teams modelupdates buiten het formele releaseproces uitvoeren.

Waar het vaak misgaat

Governance beperken tot een beleidsdocument.

Een leveranciersevaluatie eenmalig uitvoeren.

Human-in-the-loop noemen zonder echte beslissingsruimte.

Oefeningen

Aanpak. Probeer de oefening eerst zelf. Vergelijk daarna je oplossing met de uitwerking, verander de data, voeg minimaal één randgeval toe en controleer of de conclusie echt door de uitvoer wordt gedragen.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
