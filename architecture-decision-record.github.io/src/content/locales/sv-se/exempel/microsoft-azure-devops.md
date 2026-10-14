# Microsoft Azure DevOps

Innehåll:

* [Sammanfattning](#sammanfattning)
  * [Problem](#problem)
  * [Beslut](#beslut)
  * [Status](#status)
* [Detaljer](#detaljer)
  * [Antaganden](#antaganden)
  * [Begränsningar](#begränsningar)
  * [Ståndpunkter](#ståndpunkter)
  * [Argument](#argument)
  * [Implikationer](#implikationer)
* [Relaterat](#relaterat)
  * [Relaterade beslut](#relaterade-beslut)
  * [Relaterade krav](#relaterade-krav)
  * [Relaterade artefakter](#relaterade-artefakter)
  * [Relaterade principer](#relaterade-principer)
* [Anteckningar](#anteckningar)
  * [Microsoft Devops CI: An Unsatisfying Adventure](#microsoft-devops-ci-an-unsatisfying-adventure)
  * [Höjdpunkter från diskussionen på Hacker News](#höjdpunkter-från-diskussionen-på-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Sammanfattning av Edward Thomson (Azure PM)](#sammanfattning-av-edward-thomson-azure-pm)


## Sammanfattning


### Problem

Vi vill använda devops för att bygga, integrera, driftsätta och hosta våra projekt. Vi överväger Microsoft Azure DevOps.

  * Vi vill att utvecklarupplevelsen ska vara snabb och pålitlig, både för uppsättningen av devops, t.ex. konfigurering, och för fortlöpande användning, t.ex. snabba byggtider.
  
  * Vi vill överväga att använda Microsoft Azure som helhet, för att hosta projektens appar, databaser osv.


### Beslut

Beslutade oss emot Microsoft Azure DevOps.


### Status

Beslutat. Öppna för omprövning om/när ny betydande information kommer in.


## Detaljer


### Antaganden

Alla de vanliga devops-antagandena, som i boken Accelerate.

  * Snabba byggen är till stor hjälp. Det påskyndar återkopplingsslingorna.

  * Vi kan byta in/ut delar från alternativa leverantörer, dvs. vi kanske vill ta med våra egna snabbare byggservrar, eller använda vårt eget val av versionshanteringssystem, eller samordna med en egenhostad server för kontinuerlig integration.
  
  * Strömlinjeformad användbarhet är till stor hjälp, för utvecklarupplevelsen och i sin tur för subtila områden som konsekvens, tydlighet, säkerhet och en lätt inlärningskurva.

  * När något är trasigt eller problematiskt vill vi ha ett effektivt sätt att rapportera problemet. Det här är särskilt viktigt för alla säkerhetsrelaterade problem.


### Begränsningar

Inga kända. Azure har ett publicerat åtagande om att samspela väl med externa verktyg.


### Ståndpunkter

Vi övervägde att använda Microsoft Azure Devops kontra AWS som är den etablerade aktören.

Vi experimenterade med Azure DevOps, Azure Pipelines, Azure Repo och att starta upp nya servrar i Azure via Terraform.

Vi experimenterade med att få support från Microsofts representanter.

Vi samlade information från kollegor på bloggar och Hacker News.


### Argument

Azure DevOps marknadsför ett utmärkt utbud av erbjudanden, men de håller inte måttet, de fungerar inte bra tillsammans och supporten är dålig.

Vår förstahandserfarenhet:

  * Uppsättningen av Azure är en röra av UI:n, av vilka några överlappar med Microsoft-konton och andra inte. Det finns t.ex. en Azure-inloggning, en Microsoft.com-inloggning, en Live.com-inloggning osv. och alla är i spel samtidigt.

  * Vi stötte på ett mindre säkerhetsproblem under uppsättningen och hittade ingen lösning. Vi försökte rapportera det på många sätt, till många Microsoft-representanter, utan framgång. Vi rapporterade det framgångsrikt till Microsofts säkerhetsavdelning, som svarade med won't fix.

  * Dokumentationen är ofta antingen fel eller föråldrad. Åtminstone en del av detta beror på Microsofts dåliga sökmotor, och en del beror på undermålig SEO.
  
  * Uppsättningen av Terraform är väldokumenterad och fungerar. Stödet för Terraform är dock svagt jämfört med AWS eftersom Microsoft bygger affärsrelationer med leverantörer för att göra kedjade exempel på Terraform-uppsättning.

Våra kollegors erfarenheter:

  * Efter att vi gjort vår egen blindbedömning letade vi efter kollegors erfarenheter. Det vi fann bekräftade våra erfarenheter.

  * Kollegor rapporterade ytterligare problem med byggtider och problem med att ta med egen byggserver. Dessa problem är betydligt allvarligare än UI-problem, eftersom att göra byggen är den centrala uppgiften för en byggpipeline, och vi förväntar oss att göra många per dag.

  * Vi fann utmärkt deltagande av Azure-kollegor i diskussionsområdena. Beröm till Microsoft för detta. Vi är särskilt imponerade av Edward Thomson, Azure-PM och kodare, på grund av hans deltagande, rättframhet och tekniska förklaringar.


### Implikationer

Att välja Microsoft Azure DevOps ser ut att bli dyrare (~3x) i tid och kostnad än att inte välja Azure.


## Relaterat


### Relaterade beslut

Om vi väljer Azure DevOps finns det många relaterade erbjudanden, inklusive Azure Repo, Azure Pipeline osv. Vi tror att om vi väljer Azure Devops kan det göra det enklare att använda fler Azure-förmågor, eller svårare att använda andra leverantörers förmågor.

Vi tror att Microsoft gör stora framsteg inom utvecklarupplevelse, och vi ser Microsoft göra stora förvärv av utvecklarverktyg (t.ex. GitHub) och beroenden (t.ex. Citus).

Om vi väljer Azure DevOps kanske vi vill betona att välja de erbjudanden Microsoft förvärvat, och vi kanske också vill närma oss de förvärvade erbjudandena med mer omsorg/bedömning på grund av potentiell vävnadsavstötning, t.ex. risk för personalomsättning.


### Relaterade krav

Vi vill ha mycket snabba byggtider. Vi accepterar att betala en hög premie för detta. Det beror på att vi vill iterera mycket snabbt.

Vi vill ha mycket hög tillförlitlighet. Vi accepterar att betala en hög premie för detta. Det beror på att vi testar användningsfall med högt värde, inklusive finansiella transaktioner, konfidentiella transaktioner osv.

Våra fyra främsta devops-KPI:er inkluderar genomsnittlig återställningstid, vilket kräver snabba byggen och hög tillförlitlighet.


### Relaterade artefakter

Vi vill att byggsystemet ska producera artefakter som lämpar sig för användning i andra system, som Artifactory.


### Relaterade principer

Lätt att ångra. Vi kan utvärdera Azure DevOps parallellt med den etablerade AWS.


## Anteckningar


### Microsoft Devops CI: An Unsatisfying Adventure

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Blogginlägg.

”Som programvaruutvecklare vet jag av egen erfarenhet hur svårt det är att bygga kvalitetsprodukter snabbt och billigt. Det är en konstform som vi ibland får rätt, och andra gånger urartar den till något som liknar Obama-erans statliga webbplats för sjukvård. Vår nivå av kontroll över den resulterande produkten varierar, och skulden för misslyckande faller ofta på fel personer i beslutshierarkin. Microsofts Azure DevOps (tidigare känt som Visual Studio Team Services) är, trots tydligt goda avsikter, en perfekt storm av dåliga beslut och dåligt genomförande.”


### Höjdpunkter från diskussionen på Hacker News

https://news.ycombinator.com/item?id=18983586

”Vi använder Azure DevOps flitigt på mitt jobb och efter att ha använt GitHub, Gitlab, egenhostade lösningar, Jenkins, TeamCity... hamnar Azure DevOps sist.”

”UI:t är förfärligt klumpigt överallt. Värst för mig är pull requests. Otroligt svårt att arbeta med folk på en pull request. Jag kan inte ens peka på ”ett” särskilt problem – för oss är det trasigt överallt.”

”Azure Devops är något jag vill älska. UI:t fortsätter att ändras, men åtgärdar inte de underliggande buggar som funnits i evigheter.”

”Verktygen är inte väl integrerade, UI:t är riktigt långsamt, det finns ingen instrumentpanelsvy över aktiva pull requests, byggen, releaser osv. för mina favoritrepon. Bygg-/driftsättningstiderna är vansinnigt långsamma.”

”Vi försökte också använda Azure Boards (Work Items, Boards, Backlogs osv.). Aj. Det är en fullständig UI-röra av osammanhängande idéer. I stället för att implementera en sak bra implementerade de två dussin saker dåligt.”


### Windows Development MVP

Windows Development MVP här. Jag känner att jag måste ta på mig en del av ansvaret för att jag inte varit högljuddare om de här problemen. Men jag måste säga att jag är besviken över att höra att ni är ”förvånade” över UX-problemen. Jag har sagt till era folk att UX:en är förskräcklig (t.ex. redan före lanseringen) och fortsatt att höra ”vi vet, vi fixar det”. Jag ska börja formalisera återkopplingen och driva den genom rören, håll ögonen öppna. Jag är också lokal (Bellevue) och skulle gärna komma in och försöka bygga en pipeline för vår relativt enkla .net/wpf/uwp-app med öppen källkod. Jag misstänker att det blir en ögonöppnare för oss båda.

Några exempel:

* Man kan inte bygga en pipeline med ett git-repo som innehåller undermoduler

* Jag fann det omöjligt att redigera PATH för vissa egna verktyg

* Upplevelsen av Ny pipeline är helt enkelt inte särskilt vettig, nya användare som klickar runt hamnar så småningom i fel dokumentation.


### Sammanfattning av Edward Thomson (Azure PM)

Jag skrev koden som slår ihop dina pull requests. Programchef på Microsoft för Azure DevOps; tidigare programvaruutvecklare på verktyg för versionshantering på GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

Medunderhållare av libgit2. https://libgit2.github.io

Medvärd för All Things Git, podcasten om Git. https://www.allthingsgit.com/

Kurator för Developer Tools Weekly, ett nyhetsbrev om utvecklingsverktyg. https://developertoolsweekly.com/
