# Uitwerking 27.3

## Controleer je uitkomst

- Een fout in één agent wordt niet automatisch een uiteindelijke conclusie.
- Herhaalpogingen zijn begrensd en veroorzaken geen dubbele schrijfacties.
- Overdrachten tussen agents bevatten alleen de noodzakelijke context.
- De uiteindelijke conclusie bevat herkomstinformatie over de gebruikte bron en agentstap.
- Voor kosten en aantallen stappen zijn expliciete grenzen ingesteld.

## Verdiepingsopdracht

Voeg een circuit breaker toe die een specialistische agent na herhaalde fouten tijdelijk blokkeert. Laat vervolgens zien onder welke voorwaarden de agent weer gecontroleerd beschikbaar wordt gemaakt.

Nog belangrijk: ook deze oefening kan volledig zonder API-key worden uitgevoerd wanneer je de agents en fouten in gewone Python simuleert. Voor je boek zou ik er daarom nog een korte Python-oplossing bij zetten die puur met functies, try/except, een teller voor retries en één trace_id werkt. Dan blijft hoofdstuk 27 volledig lokaal uitvoerbaar.

27.11 De toekomst van AI-agents: van nu tot 2050

AI-agents staan nog aan het begin van hun ontwikkeling. De huidige generatie agents kan informatie verzamelen, redeneren over een taak, softwaretools gebruiken en meerdere stappen achter elkaar uitvoeren. De belangrijkste ontwikkeling voor de komende decennia is waarschijnlijk niet dat agents simpelweg slimmer worden, maar dat zij steeds beter worden geïntegreerd in software, organisaties en fysieke systemen.

Een mogelijke ontwikkeling kan in vier perioden worden beschreven. Hoe verder we vooruitkijken, hoe groter de onzekerheid. De periode richting 2050 moet daarom worden gelezen als een scenario en niet als een voorspelling.

2026-2030: van chatbot naar digitale uitvoerder

In deze periode verschuift generatieve AI steeds meer van het beantwoorden van vragen naar het daadwerkelijk uitvoeren van taken. Een gebruiker vraagt dan niet alleen om informatie, maar geeft een doel.

Een agent kan bijvoorbeeld documenten verzamelen, gegevens analyseren, een concept maken, informatie uit verschillende systemen combineren en een workflow voorbereiden. Daarbij gebruikt de agent tools, API's, databases en andere applicaties.

Standaarden zoals MCP maken het mogelijk om AI-systemen op een meer uniforme manier met tools en informatiebronnen te verbinden. Agent-to-agentprotocollen maken daarnaast samenwerking tussen afzonderlijke agents mogelijk.

De belangrijkste uitdaging in deze periode is waarschijnlijk niet alleen technische capaciteit, maar vooral beheersing. Zodra een AI-systeem acties kan uitvoeren, ontstaan vragen over toegangsrechten, identiteit, menselijke goedkeuring, herstelbaarheid en verantwoordelijkheid. Daarom worden identity, authorization, logging, sandboxing, human-in-the-loop en technische begrenzing steeds belangrijker.

2030-2035: agents als onderdeel van bedrijfsprocessen

Wanneer agents betrouwbaarder worden, kunnen zij steeds vaker onderdeel worden van reguliere bedrijfsprocessen. In plaats van één algemene AI-assistent kunnen organisaties gespecialiseerde agents gebruiken voor bijvoorbeeld softwareontwikkeling, cybersecurity, financiële analyse, klantenservice, onderzoek en administratieve processen.

Een medewerker kan dan samenwerken met meerdere digitale specialisten. Een mogelijke workflow wordt:

Mens → coördinerende agent → specialistische agents → tools en bedrijfsdata → controle → menselijke goedkeuring → uitvoering

Hierdoor verandert ook de rol van software. Traditionele applicaties bestaan uit vooraf geprogrammeerde schermen, regels en workflows. Agentic software kan binnen vooraf vastgestelde grenzen dynamisch bepalen welke stappen nodig zijn om een doel te bereiken.

Dat betekent niet dat traditionele software verdwijnt. Kritieke onderdelen zoals authenticatie, autorisatie, transacties, validatie en logging zullen juist deterministisch moeten blijven. Een belangrijk architectuurprincipe is daarom: gebruik AI voor interpretatie en besluitondersteuning, maar gebruik gewone software voor harde veiligheidsgrenzen.

2035-2040: ecosystemen van mensen, agents en machines

In een verder ontwikkeld scenario kunnen agents langduriger actief blijven en samenwerken met andere digitale en fysieke systemen. Een agent kan bijvoorbeeld een proces gedurende weken volgen, veranderingen detecteren, nieuwe informatie verzamelen en alleen een mens inschakelen wanneer een beslissing buiten zijn bevoegdheid valt.

Agents kunnen dan functioneren als digitale vertegenwoordigers van personen, teams of organisaties. Dit vereist sterkere vormen van digitale identiteit. Een systeem moet niet alleen kunnen vaststellen welke agent een actie uitvoerde, maar ook namens welke persoon of organisatie, met welke bevoegdheid, voor welk doel, op basis van welke informatie en welke andere agents betrokken waren.

Provenance wordt hierdoor essentieel. Besluiten moeten achteraf reconstrueerbaar blijven. Ook kan de grens tussen digitale en fysieke agents kleiner worden. Robots, voertuigen, industriële installaties en slimme gebouwen kunnen agenttechnologie gebruiken om zelfstandig beslissingen te nemen binnen hun operationele grenzen. De gevolgen van fouten worden daardoor groter.

2040-2050: mogelijke autonome digitale organisaties

Vanaf dit punt wordt voorspellen aanzienlijk onzekerder. Een denkbaar scenario is dat groepen agents een groot deel van bepaalde organisatorische processen zelfstandig uitvoeren. Mensen bepalen dan vooral doelstellingen, budgetten, beleid en grenzen, terwijl agents operationele taken verdelen en uitvoeren.

Een toekomstige architectuur kan bestaan uit een menselijke doelstelling, een governance- en policylaag, een orchestrator, gespecialiseerde agents, tools en fysieke systemen, met continue monitoring en onafhankelijke controle.

Agents kunnen daarbij mogelijk zelf plannen maken, taken verdelen, specialistische agents inschakelen, resultaten beoordelen en voorstellen doen voor verbetering. Dat betekent echter niet automatisch dat organisaties volledig autonoom worden. Voor belangrijke juridische, financiële, medische, maatschappelijke of veiligheidsbeslissingen kan menselijke verantwoordelijkheid juist belangrijker worden.

Van human-in-the-loop naar human-on-the-loop

De verhouding tussen mens en AI kan hierdoor veranderen. Bij human-in-the-loop moet een mens actief deelnemen aan bepaalde beslissingen. Bij human-on-the-loop kan een systeem binnen vastgestelde grenzen zelfstandig functioneren, terwijl mensen toezicht houden en kunnen ingrijpen.

Voor sommige laag-risicotaken kan uiteindelijk vrijwel volledig geautomatiseerde uitvoering ontstaan. Voor hoog-risicotaken zal waarschijnlijk behoefte blijven bestaan aan expliciete menselijke bevoegdheden en controles. De belangrijkste vraag wordt daarom niet alleen wat een agent zelfstandig kan uitvoeren, maar vooral wat we een agent zelfstandig willen en mogen laten uitvoeren.

Security wordt belangrijker naarmate agents autonomer worden

Meer autonomie betekent ook een grotere potentiële impact van misbruik. Een traditionele chatbot kan een verkeerd antwoord produceren. Een agent met toegang tot e-mail, databases, cloudomgevingen, financiële systemen of industriële apparatuur kan daadwerkelijk veranderingen veroorzaken.

Een bruikbaar uitgangspunt is:

Toekomstige agentsecurity zal daarom waarschijnlijk steeds meer draaien om identity, least privilege, delegated authorization, isolation, provenance, continuous monitoring, transaction controls, anomaly detection en automatische noodstops.

Ook nieuwe aanvalsvormen worden belangrijk. Een aanvaller hoeft niet noodzakelijk het AI-model zelf aan te vallen. Het kan effectiever zijn om informatie te manipuleren die een agent vertrouwt, een externe tool te compromitteren, geheugen te vergiftigen of een andere agent verkeerde informatie te laten doorgeven. De trust boundary verschuift daarmee van één AI-model naar een volledig agentecosysteem.

Wat blijft de rol van de mens?

Een veelgemaakte aanname is dat steeds betere agents uiteindelijk automatisch betekenen dat de mens uit processen verdwijnt. Dat hoeft niet het geval te zijn.

De menselijke rol kan juist verschuiven van het uitvoeren van individuele handelingen naar het bepalen van doelen en grenzen, het beoordelen van uitzonderingen, het controleren van resultaten, het maken van ethische en maatschappelijke afwegingen en het dragen van verantwoordelijkheid.

De professional van de toekomst hoeft daardoor niet iedere stap zelf uit te voeren, maar moet wel begrijpen wat de agent doet, waarop beslissingen zijn gebaseerd en wanneer het systeem niet vertrouwd mag worden.

Van prompting naar governance

Ook de vaardigheden die nodig zijn om met AI te werken zullen waarschijnlijk veranderen. Rond 2026 ligt veel aandacht op het schrijven van goede prompts. Naarmate agents zelfstandiger worden, verschuift het zwaartepunt naar het ontwerpen en beheersen van complete systemen:

De kernvraag verandert daarmee van: 'Hoe krijg ik het beste antwoord van een AI-model?' naar: 'Hoe ontwerp ik een AI-systeem dat zelfstandig nuttig werk kan uitvoeren zonder buiten de bedoelde grenzen te handelen?'

Conclusie

De ontwikkeling richting 2050 is niet met zekerheid te voorspellen. Technologie, regelgeving, economie en maatschappelijke acceptatie zullen bepalen hoeveel autonomie agents uiteindelijk krijgen.

Wel is een duidelijke richting zichtbaar: AI ontwikkelt zich van systemen die voornamelijk informatie genereren naar systemen die steeds vaker waarnemen, plannen, tools gebruiken, samenwerken en handelen. Daarmee verschuift het belangrijkste vraagstuk van alleen intelligentie naar vertrouwen en beheersing.

De succesvolste agents van de toekomst hoeven daarom niet de agents te zijn die alles zelfstandig kunnen. Waarschijnlijk zijn het de systemen waarvan mensen en organisaties precies weten wat ze mogen doen, waarom ze iets doen, welke informatie ze gebruiken, wanneer ze moeten stoppen en wie uiteindelijk verantwoordelijk blijft.

DEEL VIII - Veilige, beheersbare en verantwoorde AI

28. AI-security en threat-modeling

Leerdoelen
• Een AI-systeem als volledige aanvalsketen modelleren.
• Belangrijkste LLM- en RAG-risico's benoemen.
• Securitytests vertalen naar bewijs.

Het model is slechts één onderdeel van een AI-systeem en vaak niet eens het eenvoudigste aanvalspunt. Gebruikersinput, opgehaalde documenten, identiteiten, tools, API's, vectorstores, logging, dependencies en infrastructuur vormen samen het aanvalsoppervlak. Tussen deze onderdelen kunnen trust boundaries liggen waar gegevens of bevoegdheden van het ene vertrouwensniveau naar het andere gaan. AI-security moet daarom de volledige keten omvatten en niet stoppen bij de prompt of het model..

Threat modeling begint bij het systeem zelf. Bepaal welke gegevens, systemen en bevoegdheden waardevol of gevoelig zijn, waar gegevens of rechten een trust boundary passeren en hoe een aanvaller, gebruiker, model, tool of foutief proces deze route kan misbruiken.

28.1 Assets en trust boundaries

Identificeer gevoelige data, systeeminstructies, secrets, modellen, tools en belangrijke beslissingen. Breng vervolgens in kaart waar gegevens tussen gebruikers, services en verschillende vertrouwensniveaus worden uitgewisseld.

28.2 Prompt injection

Kwaadaardige instructies kunnen rechtstreeks door een gebruiker of indirect via documenten, websites, e-mails en andere externe bronnen worden aangeleverd. Externe inhoud moet als onbetrouwbare data worden behandeld en niet als vertrouwde instructie.

28.3 Sensitive information disclosure

Een model kan secrets, persoonlijke data, systeeminstructies of informatie van andere gebruikers teruggeven wanneer isolatie en filtering tekortschieten.

28.4 Excessieve agency

Een agent met te ruime bevoegdheden, te krachtige tools of onvoldoende menselijke goedkeuring kan ongewenste of schadelijke acties uitvoeren.

28.5 Model en supply chain

Risico’s omvatten gemanipuleerde modellen, onveilige deserialisatie, kwetsbare dependencies en datasets waarvan herkomst of integriteit onvoldoende bekend is..

Canary test
Plaats een unieke, fictieve test secret in een testdocument dat alleen voor een geautoriseerde test rol toegankelijk is. Controleer vervolgens of andere rollen deze waarde via directe vragen, samenvattingen of prompt injection kunnen achterhalen. Als de test secret buiten de toegestane context wordt teruggegeven, is dat aantoonbaar bewijs van een mogelijk datalek of autorisatieprobleem.

Belangrijk is dat je voor zo'n canarytest altijd een fictieve waarde gebruikt en nooit een echte secret.

Praktische aandachtspunten
Gebruik een threat model met assets, actoren, aanvalspaden, bestaande beheersmaatregelen, restrisico, testcases en bewijs. Herhaal de analyse bij grote wijzigingen in de architectuur.

Verdieping en voorbeelden

Kernvraag: Welke assets, trust boundaries en misbruikscenario's ontstaan of veranderen door het toevoegen van AI?

Figuur 28. Threat modeling over gebruiker, applicatie, model, data en infrastructuur.

Threat modeling en securitykaders voor AI

Threat modeling voor AI bouwt voort op klassieke security, maar voegt nieuwe risico's toe rond modellen, data, context, retrieval en toolgebruik. Het model is slechts één onderdeel van het totale systeem. Een AI-toepassing bestaat daarnaast vaak uit een webapplicatie, API's, identiteiten, databases, vectorstores, externe modelproviders en tools. Een kwetsbaarheid in één van deze onderdelen kan uiteindelijk ook de AI-functionaliteit beïnvloeden.

Breng daarom eerst de belangrijkste assets in kaart, zoals prompts, brondata, embeddings, modeloutput, secrets, toegangstokens, logs en beslissingen. Teken vervolgens de trust boundaries tussen gebruikers, applicaties, API's, modelproviders, vectordatabases en externe tools. Analyseer daarna hoe een aanvaller of foutief proces invoer, context, autorisatie of toolgebruik kan manipuleren. STRIDE kan hierbij worden gebruikt om klassieke systeemdreigingen systematisch te onderzoeken, terwijl MITRE ATLAS aanvullende aanvalstechnieken en scenario's voor AI-systemen beschrijft.

Gebruik daarnaast verschillende OWASP-bronnen, omdat iedere lijst een ander deel van het aanvalsoppervlak behandelt. De OWASP Top 10:2025 richt zich op algemene web- en applicatierisico's, zoals gebrekkige toegangscontrole, verkeerde beveiligingsconfiguraties, supply-chainproblemen, injectie en authenticatiefouten. Deze risico's blijven volledig relevant wanneer AI aan een bestaande applicatie wordt toegevoegd.

Voor systemen die via API's met modellen, databronnen en tools communiceren, vormt de OWASP API Security Top 10 2023 een aanvullende controlebron. Deze behandelt onder andere gebrekkige object- en functieautorisatie, authenticatiefouten, onbeperkt resourcegebruik, Server-Side Request Forgery en onveilig gebruik van externe API's. Juist bij RAG- en agentsystemen is deze laag belangrijk, omdat de AI-toepassing of agent via API's toegang kan krijgen tot andere systemen en gegevens. Deze risico's staan inderdaad in de officiële OWASP Top 10 for Agentic Applications 2026.

De OWASP GenAI LLM Top 10 2026 vult deze klassieke beveiligingskaders aan met risico's die specifiek samenhangen met LLM- en GenAI-toepassingen. Voor systemen waarin agents zelfstandig plannen, tools aanroepen en acties uitvoeren, is daarnaast de OWASP Top 10 for Agentic Applications 2026 beschikbaar. Deze agentic lijst richt zich onder andere op risico's zoals goal hijacking, toolmisbruik, misbruik van identiteiten en privileges en kwetsbaarheden in de agentic supply chain.

Specifieke risico's van LLM-systemen

LLM-toepassingen introduceren risico's die bij traditionele applicaties minder of op een andere manier voorkomen. Denk aan prompt injection, het onbedoeld prijsgeven van gevoelige informatie, manipulatie van trainings- of retrievaldata, onveilige verwerking van modeloutput, te ruime bevoegdheden voor agents, lekkage van systeeminstructies, zwakheden in vectorstores en embeddings, misleidende of onjuiste modeloutput en onbeheerst verbruik van tokens, rekencapaciteit of externe diensten. De OWASP GenAI LLM Top 10 2026 biedt hiervoor een praktisch controlekader.

De belangrijkste LLM-risico's volgens de OWASP GenAI LLM Top 10 2026 zijn:

Prompt injection: invoer probeert het gedrag of de instructies van het systeem te manipuleren.

Sensitive information disclosure: gevoelige of vertrouwelijke gegevens worden ongewenst prijsgegeven.

Supply-chainrisico's: kwetsbaarheden of manipulatie in modellen, datasets, libraries of externe diensten.

Data- en modelpoisoning: gegevens of modellen worden bewust beïnvloed om ongewenst gedrag te veroorzaken.

Improper output handling: modeloutput wordt zonder voldoende controle door andere systemen verwerkt.

Excessive agency: een model of agent beschikt over meer rechten of mogelijkheden dan noodzakelijk.

System prompt leakage: interne systeeminstructies worden zichtbaar voor onbevoegde gebruikers.

Vector- en embeddingzwakheden: retrieval kan verkeerde, gemanipuleerde of onbevoegde informatie teruggeven.

Misinformation: overtuigende maar onjuiste of onvoldoende onderbouwde informatie wordt gebruikt.

Unbounded consumption: ongecontroleerd gebruik kan leiden tot hoge kosten, uitputting van resources of denial-of-serviceachtige situaties.

De 2026-versie zet Excessive Agency dus nu op nummer 3 en Unbounded Consumption op nummer 6. OWASP geeft ook expliciet aan dat System Prompt Leakage in 2026 is verbreed en hernoemd naar Hidden Context Exposure.

Deze kaders moeten niet afzonderlijk worden gezien. Een moderne AI-toepassing kan tegelijkertijd kwetsbaar zijn voor een klassieke autorisatiefout, een onveilige API, prompt injection en ongewenst toolgebruik door een agent. Gebruik de verschillende lijsten daarom als aanvullende controlebronnen en vertaal relevante dreigingen naar concrete testcases en technische beheersmaatregelen. Geen van deze Top 10-lijsten vervangt een systeemspecifiek threat model; OWASP beschrijft de Top 10 zelf als een awarenessdocument en startpunt, niet als een volledige beveiligingsstandaard.

Voorbeeld: belangrijkste assets van een RAG-agent

Dezelfde component kan meerdere soorten waarde en risico bevatten.

Asset

Dreiging

Maatregel

Documentcollectie

Ongeautoriseerde retrieval.

ACL-filtering en bronautorisatie.

System prompt

Disclosure of manipulatie.

Niet als geheim vertrouwen; gedrag technisch begrenzen.

Tooltoken

Misbruik voor brede acties.

Short-lived token en minimale scope.

Conversation memory

Cross-user leakage.

Tenant- en sessie-isolatie.

Activiteitenlog

Manipulatie of privacyverlies.

Integrity, retentie en filtering.

In de praktijk

Vraag om misbruikscenario's vanuit aanvaller, interne gebruiker en foutieve integratie. Een threat model zonder eigenaar, prioriteit en testbare controls heeft weinig operationele waarde.

Waar het vaak misgaat

Alleen jailbreak prompts testen.

Securityfilters verwarren met autorisatie.

Een modelweigering als enige beheersmaatregel gebruiken.

Oefeningen

Aanpak. Probeer de oefening eerst zelf. Vergelijk daarna je oplossing met de uitwerking, verander de data, voeg minimaal één randgeval toe en controleer of de conclusie echt door de uitvoer wordt gedragen.


## Zelf verder testen

Verander minimaal één invoerwaarde en voeg een randgeval toe. Controleer daarna of de conclusie nog steeds door de uitvoer wordt ondersteund.
