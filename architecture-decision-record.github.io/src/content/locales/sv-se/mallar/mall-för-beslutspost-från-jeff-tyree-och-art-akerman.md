# Mall för beslutspost från Jeff Tyree och Art Akerman

Det här är mallen för beskrivning av arkitekturbeslut som publicerades i ["Architecture Decisions: Demystifying Architecture" av Jeff Tyree och Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Fråga (Issue)**: Beskriv den arkitekturdesignfråga du adresserar, utan att lämna några frågetecken om varför du adresserar den här frågan just nu. Följ en minimalistisk ansats och adressera och dokumentera endast de frågor som behöver adresseras vid olika punkter i livscykeln.

* **Beslut (Decision)**: Ange tydligt arkitekturens riktning, det vill säga den ståndpunkt du har valt.

* **Tillstånd (Status)**: Beslutets tillstånd, till exempel pending, decided eller approved.

* **Grupp (Group)**: Du kan använda en enkel gruppering – till exempel integration, presentation, data och så vidare – för att hjälpa till att organisera uppsättningen beslut. Du kan också använda en mer sofistikerad arkitekturontologi, till exempel John Kyaruzi och Jan van Katwijks, som innehåller mer abstrakta kategorier som händelse, kalender och plats. Med den här ontologin skulle du till exempel gruppera beslut som handlar om förekomster där systemet kräver information under händelse.

* **Antaganden (Assumptions)**: Beskriv tydligt de underliggande antagandena i den miljö där du fattar beslutet – kostnad, tidplan, teknik och så vidare. Observera att miljöbegränsningar (såsom accepterade tekniska standarder, företagsarkitektur, vanligt förekommande mönster och så vidare) kan begränsa de alternativ du överväger.

* **Begränsningar (Constraints)**: Fånga eventuella ytterligare begränsningar för miljön som det valda alternativet (beslutet) kan medföra.

* **Ståndpunkter (Positions)**: Lista de ståndpunkter (genomförbara val eller alternativ) du övervägde. Dessa kräver ofta långa förklaringar, ibland till och med modeller och diagram. Detta är ingen uttömmande lista. Du vill dock inte höra frågan ”Har du tänkt på...?” under en slutlig granskning; det leder till förlorad trovärdighet och ifrågasättande av andra arkitekturbeslut. Det här avsnittet hjälper också till att säkerställa att du har hört andras åsikter; att uttryckligen ange andra åsikter hjälper till att få med deras förespråkare i ditt beslut.

* **Argument (Argument)**: Beskriv varför du valde en ståndpunkt, inklusive saker som implementationskostnad, total ägandekostnad, tid till marknad och tillgång till nödvändiga utvecklingsresurser. Det här är förmodligen lika viktigt som själva beslutet.

* **Konsekvenser (Implications)**: Ett beslut medför många konsekvenser, som REMAP-metamodellen anger. Ett beslut kan till exempel skapa ett behov av att fatta andra beslut, skapa nya krav eller ändra befintliga krav, ställa ytterligare begränsningar på miljön, kräva omförhandling av omfattning eller tidplan med kunder eller kräva ytterligare personalutbildning. Att tydligt förstå och ange konsekvenserna av ditt beslut kan vara mycket effektivt för att få gehör och skapa en färdplan för arkitekturens genomförande.

* **Relaterade beslut**: Det är uppenbart att många beslut hänger ihop; du kan lista dem här. Vi har dock funnit att en spårbarhetsmatris, beslutsträd eller metamodeller i praktiken är mer användbara. Metamodeller är användbara för att visa komplexa samband diagrammatiskt (till exempel Rose-modeller).

* **Relaterade krav**: Beslut bör vara affärsdrivna. För att visa ansvarsskyldighet, koppla uttryckligen dina beslut till målen eller kraven. Du kan räkna upp dessa relaterade krav här, men vi har funnit det bekvämare att hänvisa till en spårbarhetsmatris. Du kan bedöma varje arkitekturbesluts bidrag till att uppfylla varje krav och sedan bedöma hur väl kravet uppfylls över alla beslut. Om ett beslut inte bidrar till att uppfylla ett krav, fatta inte det beslutet.

* **Relaterade artefakter**: Lista de relaterade arkitektur-, design- eller omfattningsdokument som det här beslutet påverkar.

* **Relaterade principer**: Om företaget har en överenskommen uppsättning principer, se till att beslutet är förenligt med en eller flera av dem. Det hjälper till att säkerställa samstämmighet mellan domäner eller system.

* **Anteckningar**: Eftersom beslutsprocessen kan ta veckor har vi funnit det användbart att fånga anteckningar och frågor som teamet diskuterar under förankringsprocessen.

