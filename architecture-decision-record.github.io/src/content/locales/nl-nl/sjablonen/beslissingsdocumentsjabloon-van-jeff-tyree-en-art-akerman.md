# Beslissingsdocumentsjabloon van Jeff Tyree en Art Akerman

Dit is het sjabloon voor het beschrijven van architectuurbeslissingen uit ["Architecture Decisions: Demystifying Architecture", Jeff Tyree en Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Kwestie (Issue)**: Beschrijf het architectuurontwerpprobleem dat wordt aangepakt, zodat er geen twijfel overblijft over waarom je het nu aanpakt. Volgens een minimalistische aanpak behandel en documenteer je alleen de kwesties die op bepaalde momenten in de levenscyclus aandacht nodig hebben.

* **Beslissing (Decision)**: Geef duidelijk de architectuurrichting aan, dat wil zeggen het standpunt dat is gekozen.

* **Status**: De status van de beslissing, bijvoorbeeld pending, decided, approved.

* **Groep (Group)**: Je kunt eenvoudige groeperingen gebruiken, zoals integratie, presentatie, data enz., om een set beslissingen te organiseren. Je kunt ook een verfijndere architectuurontologie gebruiken, zoals die van John Kyaruzi en Jan van Katwijk, met abstractere categorieën zoals gebeurtenissen, kalenders en locaties. Met deze ontologie zou je bijvoorbeeld beslissingen die situaties behandelen waarin het systeem informatie nodig heeft, onder gebeurtenissen groeperen.

* **Aannames (Assumptions)**: Beschrijf duidelijk de onderliggende aannames in de omgeving waarin de beslissing wordt genomen: kosten, planning, technologie enzovoort. Let op dat beperkingen in de omgeving (zoals geaccepteerde technologiestandaarden, bedrijfsarchitectuur, algemeen gebruikte patronen) de overwogen alternatieven kunnen beperken.

* **Beperkingen (Constraints)**: Leg alle extra beperkingen vast die het gekozen alternatief (de beslissing) aan de omgeving kan opleggen.

* **Standpunten (Positions)**: Vermeld de overwogen standpunten (haalbare opties of alternatieven). Dit vereist vaak een lange uitleg en soms zelfs modellen en diagrammen. Dit is niet noodzakelijk een uitputtende lijst. Je wilt echter niet bij de eindbeoordeling de vraag horen "Heb je aan ... gedacht?". Dat leidt tot verlies van vertrouwen en twijfel aan andere architectuurbeslissingen. Deze sectie helpt ook om te bevestigen dat je naar de meningen van anderen hebt geluisterd. Het expliciet maken van andere meningen helpt om hun voorstanders bij jouw beslissing te betrekken.

* **Argument**: Schets waarom je een standpunt hebt gekozen, met onderwerpen zoals implementatiekosten, totale eigendomskosten, time to market en beschikbaarheid van benodigde ontwikkelmiddelen. Dit is waarschijnlijk net zo belangrijk als de beslissing zelf.

* **Implicaties (Implications)**: Een beslissing heeft vele implicaties, zoals het REMAP-metamodel laat zien. Een beslissing kan bijvoorbeeld de noodzaak creëren om andere beslissingen te nemen, nieuwe eisen creëren of bestaande wijzigen, extra beperkingen aan de omgeving opleggen, heronderhandeling met de klant over scope of planning vereisen, of extra opleiding van personeel nodig maken. Het duidelijk begrijpen en benoemen van de implicaties van een beslissing kan zeer effectief zijn om instemming te krijgen en een stappenplan voor de uitvoering van de architectuur op te stellen.

* **Gerelateerde beslissingen**: Het is duidelijk dat veel beslissingen met elkaar verband houden; je kunt ze hier vermelden. In de praktijk vinden we echter dat een traceerbaarheidsmatrix, beslissingsboom of metamodel nuttiger is. Metamodellen zijn nuttig om complexe relaties in diagrammen weer te geven (bijvoorbeeld Rose-modellen).

* **Gerelateerde eisen**: Beslissingen moeten bedrijfsgedreven zijn. Om verantwoording aan te tonen, koppel je beslissingen expliciet aan doelen of eisen. Je kunt deze gerelateerde eisen hier opsommen, maar we vinden het handiger om naar een traceerbaarheidsmatrix te verwijzen. Je beoordeelt de mate waarin elke architectuurbeslissing bijdraagt aan het vervullen van elke eis, en vervolgens hoe goed de eisen over alle beslissingen heen zijn vervuld. Als een beslissing niet bijdraagt aan het vervullen van een eis, neem die beslissing dan niet.

* **Gerelateerde artefacten**: Vermeld de relevante architectuur-, ontwerp- of scopedocumenten waarop deze beslissing van invloed is.

* **Gerelateerde principes**: Als het bedrijf een overeengekomen set principes heeft, zorg er dan voor dat de beslissing consistent is met een of meer ervan. Dit helpt om afstemming over domeinen of systemen heen te waarborgen.

* **Notities**: Omdat beslissingsprocessen weken kunnen duren, vinden we het nuttig om de notities en kwesties vast te leggen die het team tijdens het voorafgaande delen bespreekt.

