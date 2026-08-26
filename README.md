# Praktische Artificial Intelligence - oefeningen

Deze repository bevat de Python-oefeningen bij het boek **Praktische Artificial Intelligence** van Perry Mertens.

De oefeningen zijn per hoofdstuk en per oefening gescheiden. Iedere oefening bevat:

- `opdracht.md`: de opdracht zonder oplossing;
- `starter.py`: een leeg Python-startpunt;
- `opdracht.ipynb`: Jupyter Notebook om de oefening zelf uit te werken;
- `uitwerking.py`: een voorbeeldoplossing;
- `uitwerking.ipynb`: Jupyter Notebook met de voorbeeldoplossing;
- `uitwerking.md`: uitleg, controlepunten en eventuele verdieping.

## Aanbevolen werkwijze

1. Maak een virtuele Python-omgeving.
2. Installeer de packages uit `requirements.txt`.
3. Open `opdracht.ipynb` in JupyterLab, of gebruik `opdracht.md` met `starter.py`.
4. Maak de oefening zelfstandig.
5. Voer het notebook uit met **Restart Kernel and Run All**.
6. Vergelijk daarna met `uitwerking.ipynb` of `uitwerking.py`.
7. Verander de data en voeg minimaal één randgeval toe.

## Installatie

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## JupyterLab starten

Na activatie van de virtuele omgeving:

```powershell
jupyter lab
```

Open daarna in JupyterLab de map `oefeningen` en kies de gewenste `opdracht.ipynb`.

## Oefeningen

| Oefening | Hoofdstuk | Onderwerp |
|---|---|---|
| 1.1 | 1. Wat is kunstmatige intelligentie (AI)? | [Taken classificeren als AI-probleem](oefeningen/hoofdstuk_01/oefening_1_1_taken-classificeren-als-ai-probleem/opdracht.md) |
| 1.2 | 1. Wat is kunstmatige intelligentie (AI)? | [Bedrijfsrisico van een fout analyseren](oefeningen/hoofdstuk_01/oefening_1_2_bedrijfsrisico-van-een-fout-analyseren/opdracht.md) |
| 2.1 | 2. De AI-levenscyclus | [Een AI-levenscyclus als projectplan modelleren](oefeningen/hoofdstuk_02/oefening_2_1_een-ai-levenscyclus-als-projectplan-modelleren/opdracht.md) |
| 2.2 | 2. De AI-levenscyclus | [Technische en organisatorische risico's bewaken](oefeningen/hoofdstuk_02/oefening_2_2_technische-en-organisatorische-risicos-bewaken/opdracht.md) |
| 3.1 | 3. Ontwikkelomgeving met Python en Jupyter | [Een reproduceerbare Python-omgeving controleren](oefeningen/hoofdstuk_03/oefening_3_1_een-reproduceerbare-python-omgeving-controleren/opdracht.md) |
| 3.2 | 3. Ontwikkelomgeving met Python en Jupyter | [Een notebook met systeeminformatie maken](oefeningen/hoofdstuk_03/oefening_3_2_een-notebook-met-systeeminformatie-maken/opdracht.md) |
| 4.1 | 4. Python-basis voor data en AI | [risicoscores classificeren](oefeningen/hoofdstuk_04/oefening_4_1_risicoscores-classificeren/opdracht.md) |
| 4.2 | 4. Python-basis voor data en AI | [een risicoscore veilig valideren](oefeningen/hoofdstuk_04/oefening_4_2_een-risicoscore-veilig-valideren/opdracht.md) |
| 4.3 | 4. Python-basis voor data en AI | [automatische tests voor invoervalidatie](oefeningen/hoofdstuk_04/oefening_4_3_automatische-tests-voor-invoervalidatie/opdracht.md) |
| 5.1 | 5. NumPy: rekenen met arrays en matrices | [Een matrix en hoofddiagonaal onderzoeken](oefeningen/hoofdstuk_05/oefening_5_1_een-matrix-en-hoofddiagonaal-onderzoeken/opdracht.md) |
| 5.2 | 5. NumPy: rekenen met arrays en matrices | [Elementgewijs kwadrateren en vectorisatie](oefeningen/hoofdstuk_05/oefening_5_2_elementgewijs-kwadrateren-en-vectorisatie/opdracht.md) |
| 5.3 | 5. NumPy: rekenen met arrays en matrices | [View en copy aantoonbaar vergelijken](oefeningen/hoofdstuk_05/oefening_5_3_view-en-copy-aantoonbaar-vergelijken/opdracht.md) |
| 5.4 | 5. NumPy: rekenen met arrays en matrices | [Broadcasting en normalisatie controleren](oefeningen/hoofdstuk_05/oefening_5_4_broadcasting-en-normalisatie-controleren/opdracht.md) |
| 6.1 | 6. Pandas: tabellen onderzoeken en opschonen | [Een datakwaliteitsrapport maken](oefeningen/hoofdstuk_06/oefening_6_1_een-datakwaliteitsrapport-maken/opdracht.md) |
| 6.2 | 6. Pandas: tabellen onderzoeken en opschonen | [Records per categorie tellen](oefeningen/hoofdstuk_06/oefening_6_2_records-per-categorie-tellen/opdracht.md) |
| 6.3 | 6. Pandas: tabellen onderzoeken en opschonen | [Uniciteit van een ID-kolom controleren](oefeningen/hoofdstuk_06/oefening_6_3_uniciteit-van-een-id-kolom-controleren/opdracht.md) |
| 6.4 | 6. Pandas: tabellen onderzoeken en opschonen | [Datatypes en datums valideren](oefeningen/hoofdstuk_06/oefening_6_4_datatypes-en-datums-valideren/opdracht.md) |
| 7.1 | 7. Datavisualisatie en statistisch denken | [Een histogram van doorlooptijden maken](oefeningen/hoofdstuk_07/oefening_7_1_een-histogram-van-doorlooptijden-maken/opdracht.md) |
| 7.2 | 7. Datavisualisatie en statistisch denken | [Gemiddelde en mediaan onder verschillende scenario’s](oefeningen/hoofdstuk_07/oefening_7_2_gemiddelde-en-mediaan-onder-verschillende-scenarios/opdracht.md) |
| 7.3 | 7. Datavisualisatie en statistisch denken | [Correlatie onderzoeken zonder causaliteit te claimen](oefeningen/hoofdstuk_07/oefening_7_3_correlatie-onderzoeken-zonder-causaliteit-te-claimen/opdracht.md) |
| 8.1 | 8. Exploratory Data Analysis en datakwaliteit | [Een herbruikbare EDA-checklist uitvoeren](oefeningen/hoofdstuk_08/oefening_8_1_een-herbruikbare-eda-checklist-uitvoeren/opdracht.md) |
| 8.2 | 8. Exploratory Data Analysis en datakwaliteit | [Data leakage met een eenvoudige proef aantonen](oefeningen/hoofdstuk_08/oefening_8_2_data-leakage-met-een-eenvoudige-proef-aantonen/opdracht.md) |
| 9.1 | 9. De machine-learningworkflow | [Een volledige ML-pipeline bouwen](oefeningen/hoofdstuk_09/oefening_9_1_een-volledige-ml-pipeline-bouwen/opdracht.md) |
| 9.2 | 9. De machine-learningworkflow | [Het effect van stratify meten](oefeningen/hoofdstuk_09/oefening_9_2_het-effect-van-stratify-meten/opdracht.md) |
| 10.1 | 10. Regressie | [MAE en MSE vergelijken bij een zeer grote fout](oefeningen/hoofdstuk_10/oefening_10_1_mae-en-mse-vergelijken-bij-een-zeer-grote-fout/opdracht.md) |
| 10.2 | 10. Regressie | [Negatieve R-kwadraat op testdata onderzoeken](oefeningen/hoofdstuk_10/oefening_10_2_negatieve-r-kwadraat-op-testdata-onderzoeken/opdracht.md) |
| 11.1 | 11. Classificatie en evaluatiemetrics | [Precision en recall berekenen en controleren](oefeningen/hoofdstuk_11/oefening_11_1_precision-en-recall-berekenen-en-controleren/opdracht.md) |
| 11.2 | 11. Classificatie en evaluatiemetrics | [Recall of precision kiezen met een kostensimulatie](oefeningen/hoofdstuk_11/oefening_11_2_recall-of-precision-kiezen-met-een-kostensimulatie/opdracht.md) |
| 12.1 | 12. Beslissingsbomen, random forests en boosting | [Overfitting van een diepe beslissingsboom zichtbaar maken](oefeningen/hoofdstuk_12/oefening_12_1_overfitting-van-een-diepe-beslissingsboom-zichtbaar-maken/opdracht.md) |
| 12.2 | 12. Beslissingsbomen, random forests en boosting | [Bagging en boosting praktisch vergelijken](oefeningen/hoofdstuk_12/oefening_12_2_bagging-en-boosting-praktisch-vergelijken/opdracht.md) |
| 13.1 | 13. K-nearest neighbors en support vector machines | [Het effect van feature scaling op KNN tonen](oefeningen/hoofdstuk_13/oefening_13_1_het-effect-van-feature-scaling-op-knn-tonen/opdracht.md) |
| 13.2 | 13. K-nearest neighbors en support vector machines | [Drie waarden voor k met cross-validation onderzoeken](oefeningen/hoofdstuk_13/oefening_13_2_drie-waarden-voor-k-met-cross-validation-onderzoeken/opdracht.md) |
| 14.1 | 14. Clustering: K-Means, hiërarchisch en DBSCAN | [DBSCAN en K-Means vergelijken op maanvormige clusters](oefeningen/hoofdstuk_14/oefening_14_1_dbscan-en-k-means-vergelijken-op-maanvormige-clusters/opdracht.md) |
| 14.2 | 14. Clustering: K-Means, hiërarchisch en DBSCAN | [Clusterkwaliteit met meerdere maatstaven beoordelen](oefeningen/hoofdstuk_14/oefening_14_2_clusterkwaliteit-met-meerdere-maatstaven-beoordelen/opdracht.md) |
| 15.1 | 15. Underfitting, overfitting en modelselectie | [Learning curves voor underfitting en overfitting maken](oefeningen/hoofdstuk_15/oefening_15_1_learning-curves-voor-underfitting-en-overfitting-maken/opdracht.md) |
| 15.2 | 15. Underfitting, overfitting en modelselectie | [GroupKFold toepassen op afhankelijke records](oefeningen/hoofdstuk_15/oefening_15_2_groupkfold-toepassen-op-afhankelijke-records/opdracht.md) |
| 16.1 | 16. Neurale netwerken in eenvoudige taal | [Epoch, batch en learning rate zichtbaar simuleren](oefeningen/hoofdstuk_16/oefening_16_1_epoch-batch-en-learning-rate-zichtbaar-simuleren/opdracht.md) |
| 16.2 | 16. Neurale netwerken in eenvoudige taal | [Loss laten verbeteren terwijl accuracy gelijk blijft](oefeningen/hoofdstuk_16/oefening_16_2_loss-laten-verbeteren-terwijl-accuracy-gelijk-blijft/opdracht.md) |
| 17.1 | 17. Deep learning voor beeld, tekst en sequenties | [CNN en transformer als modelprofielen vergelijken](oefeningen/hoofdstuk_17/oefening_17_1_cnn-en-transformer-als-modelprofielen-vergelijken/opdracht.md) |
| 17.2 | 17. Deep learning voor beeld, tekst en sequenties | [Een testmatrix voor beeldclassificatie automatiseren](oefeningen/hoofdstuk_17/oefening_17_2_een-testmatrix-voor-beeldclassificatie-automatiseren/opdracht.md) |
| 18.1 | 18. Generatieve AI en foundation models | [Prompting, RAG of fine-tuning selecteren](oefeningen/hoofdstuk_18/oefening_18_1_prompting-rag-of-fine-tuning-selecteren/opdracht.md) |
| 18.2 | 18. Generatieve AI en foundation models | [Modelkennis en contextkennis zichtbaar scheiden](oefeningen/hoofdstuk_18/oefening_18_2_modelkennis-en-contextkennis-zichtbaar-scheiden/opdracht.md) |
| 19.1 | 19. Prompt engineering voor betrouwbare uitvoer | [Een duidelijke analyseprompt opbouwen](oefeningen/hoofdstuk_19/oefening_19_1_een-duidelijke-analyseprompt-opbouwen/opdracht.md) |
| 19.2 | 19. Prompt engineering voor betrouwbare uitvoer | [Gestructureerde modelbevindingen valideren](oefeningen/hoofdstuk_19/oefening_19_2_gestructureerde-modelbevindingen-valideren/opdracht.md) |
| 19.3 | 19. Prompt engineering voor betrouwbare uitvoer | [Van single prompt naar prompt chain met feedback loop](oefeningen/hoofdstuk_19/oefening_19_3_van-single-prompt-naar-prompt-chain-met-feedback-loop/opdracht.md) |
| 20.1 | 20. Werken met LLM-API's en lokale modellen | [Cloud en lokaal als gewogen beslismatrix vergelijken](oefeningen/hoofdstuk_20/oefening_20_1_cloud-en-lokaal-als-gewogen-beslismatrix-vergelijken/opdracht.md) |
| 20.2 | 20. Werken met LLM-API's en lokale modellen | [Maandelijkse tokenkosten berekenen](oefeningen/hoofdstuk_20/oefening_20_2_maandelijkse-tokenkosten-berekenen/opdracht.md) |
| 21.1 | 21. RAG en semantisch zoeken | [Een kleine RAG-pipeline in Python bouwen](oefeningen/hoofdstuk_21/oefening_21_1_een-kleine-rag-pipeline-in-python-bouwen/opdracht.md) |
| 21.2 | 21. RAG en semantisch zoeken | [Lexicaal en semantisch zoeken combineren](oefeningen/hoofdstuk_21/oefening_21_2_lexicaal-en-semantisch-zoeken-combineren/opdracht.md) |
| 22.1 | 22. Documentverwerking, chunking en metadata | [Metadata voor interne documenten ontwerpen en valideren](oefeningen/hoofdstuk_22/oefening_22_1_metadata-voor-interne-documenten-ontwerpen-en-valideren/opdracht.md) |
| 22.2 | 22. Documentverwerking, chunking en metadata | [Chunkgrootte van 200 en 1200 woorden vergelijken](oefeningen/hoofdstuk_22/oefening_22_2_chunkgrootte-van-200-en-1200-woorden-vergelijken/opdracht.md) |
| 23.1 | 23. Vectorstores, hybrid search en reranking | [Een hybrid-searchscore ontwerpen en testen](oefeningen/hoofdstuk_23/oefening_23_1_een-hybrid-searchscore-ontwerpen-en-testen/opdracht.md) |
| 23.2 | 23. Vectorstores, hybrid search en reranking | [Schaalbaarheid van cross-encoding berekenen](oefeningen/hoofdstuk_23/oefening_23_2_schaalbaarheid-van-cross-encoding-berekenen/opdracht.md) |
| 24.1 | 24. RAG evalueren met meetbare criteria | [Een RAG-evaluatieset met verwachte bronnen maken](oefeningen/hoofdstuk_24/oefening_24_1_een-rag-evaluatieset-met-verwachte-bronnen-maken/opdracht.md) |
| 24.2 | 24. RAG evalueren met meetbare criteria | [Retrieval goed, generatie fout detecteren](oefeningen/hoofdstuk_24/oefening_24_2_retrieval-goed-generatie-fout-detecteren/opdracht.md) |
| 25.1 | 25. Multimodale AI | [Een pipeline voor trainingsvideo’s modelleren](oefeningen/hoofdstuk_25/oefening_25_1_een-pipeline-voor-trainingsvideos-modelleren/opdracht.md) |
| 25.2 | 25. Multimodale AI | [Kwaliteitsrisico's per modaliteit controleren](oefeningen/hoofdstuk_25/oefening_25_2_kwaliteitsrisicos-per-modaliteit-controleren/opdracht.md) |
| 26.1 | 26. AI-agents en toolgebruik | [Een risicomatrix voor agenttools berekenen](oefeningen/hoofdstuk_26/oefening_26_1_een-risicomatrix-voor-agenttools-berekenen/opdracht.md) |
| 26.2 | 26. AI-agents en toolgebruik | [Een approval flow voor e-mail implementeren](oefeningen/hoofdstuk_26/oefening_26_2_een-approval-flow-voor-e-mail-implementeren/opdracht.md) |
| 26.3 | 26. AI-agents en toolgebruik | [Ontwerp een veilige MCP-toolgrens](oefeningen/hoofdstuk_26/oefening_26_3_ontwerp-een-veilige-mcp-toolgrens/opdracht.md) |
| 27.1 | 27. Multi-agentarchitecturen en observability | [Een multi-agentarchitectuur als graaf tekenen](oefeningen/hoofdstuk_27/oefening_27_1_een-multi-agentarchitectuur-als-graaf-tekenen/opdracht.md) |
| 27.2 | 27. Multi-agentarchitecturen en observability | [Gestructureerde observability-events vastleggen](oefeningen/hoofdstuk_27/oefening_27_2_gestructureerde-observability-events-vastleggen/opdracht.md) |
| 27.3 | 27. Multi-agentarchitecturen en observability | [Test foutpropagatie en herstel](oefeningen/hoofdstuk_27/oefening_27_3_test-foutpropagatie-en-herstel/opdracht.md) |
| 28.1 | 28. AI-security en threat modeling | [Een dataflowdiagram voor een RAG-agent tekenen](oefeningen/hoofdstuk_28/oefening_28_1_een-dataflowdiagram-voor-een-rag-agent-tekenen/opdracht.md) |
| 28.2 | 28. AI-security en threat modeling | [Indirecte prompt-injectionbronnen automatisch inventariseren](oefeningen/hoofdstuk_28/oefening_28_2_indirecte-prompt-injectionbronnen-automatisch-inventariseren/opdracht.md) |
| 29.1 | 29. Prompt injection, datalekken en veilige RAG | [Een tweetalige red-teamtestset uitvoeren](oefeningen/hoofdstuk_29/oefening_29_1_een-tweetalige-red-teamtestset-uitvoeren/opdracht.md) |
| 29.2 | 29. Prompt injection, datalekken en veilige RAG | [Informatiedisclosure automatisch scoren van 0 tot 5](oefeningen/hoofdstuk_29/oefening_29_2_informatiedisclosure-automatisch-scoren-van-0-tot-5/opdracht.md) |
| 29.3 | 29. Prompt injection, datalekken en veilige RAG | [Herken en beperk AI-fouten](oefeningen/hoofdstuk_29/oefening_29_3_herken-en-beperk-ai-fouten/opdracht.md) |
| 30.1 | 30. AI-governance, privacy en modelrisico | [Een minimaal AI-register bouwen](oefeningen/hoofdstuk_30/oefening_30_1_een-minimaal-ai-register-bouwen/opdracht.md) |
| 30.2 | 30. AI-governance, privacy en modelrisico | [AI-toepassingen op risico classificeren](oefeningen/hoofdstuk_30/oefening_30_2_ai-toepassingen-op-risico-classificeren/opdracht.md) |
| 31.1 | 31. Monitoring, incidenten en continue verbetering | [Kernmetrics voor een AI-monitoringdashboard berekenen](oefeningen/hoofdstuk_31/oefening_31_1_kernmetrics-voor-een-ai-monitoringdashboard-berekenen/opdracht.md) |
| 31.2 | 31. Monitoring, incidenten en continue verbetering | [Een incidentplaybook als state machine uitvoeren](oefeningen/hoofdstuk_31/oefening_31_2_een-incidentplaybook-als-state-machine-uitvoeren/opdracht.md) |
| 32.1 | 32. Praktijkproject: een beveiligde AI-kennisassistent | [Componenten en datastromen als uitvoerbare specificatie vastleggen](oefeningen/hoofdstuk_32/oefening_32_1_componenten-en-datastromen-als-uitvoerbare-specificatie-vastleggen/opdracht.md) |
| 32.2 | 32. Praktijkproject: een beveiligde AI-kennisassistent | [Twintig acceptatietests als Python-testcatalogus maken](oefeningen/hoofdstuk_32/oefening_32_2_twintig-acceptatietests-als-python-testcatalogus-maken/opdracht.md) |
| 32.3 | 32. Praktijkproject: een beveiligde AI-kennisassistent | [Go/no-go-criteria automatisch evalueren](oefeningen/hoofdstuk_32/oefening_32_3_go-no-go-criteria-automatisch-evalueren/opdracht.md) |



Licentie en gebruik
De Python-code en Jupyter-code in deze repository zijn beschikbaar onder de MIT License.

De oefeningen, teksten en uitgewerkte opdrachten zijn © 2026 Perry Mertens en beschikbaar onder de Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) licentie. Hergebruik en aanpassing voor niet-commerciële onderwijsdoeleinden is toegestaan, mits de auteur wordt vermeld.

Deze licenties hebben uitsluitend betrekking op het materiaal in deze repository. Het boek Praktische Artificial Intelligence valt onder het afzonderlijke auteursrecht van de auteur.