# Microsoft Azure DevOps

Indhold:

* [Resumé](#resumé)
  * [Problemstilling](#problemstilling)
  * [Beslutning](#beslutning)
  * [Status](#status)
* [Detaljer](#detaljer)
  * [Antagelser](#antagelser)
  * [Begrænsninger](#begrænsninger)
  * [Standpunkter](#standpunkter)
  * [Argument](#argument)
  * [Implikationer](#implikationer)
* [Relateret](#relateret)
  * [Relaterede beslutninger](#relaterede-beslutninger)
  * [Relaterede krav](#relaterede-krav)
  * [Relaterede artefakter](#relaterede-artefakter)
  * [Relaterede principper](#relaterede-principper)
* [Noter](#noter)
  * [Microsoft Devops CI: et utilfredsstillende eventyr](#microsoft-devops-ci-et-utilfredsstillende-eventyr)
  * [Højdepunkter fra diskussionen på Hacker News](#højdepunkter-fra-diskussionen-på-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Resumé af Edward Thomson (Azure PM)](#resumé-af-edward-thomson-azure-pm)


## Resumé


### Problemstilling

Vi vil bruge devops til at bygge, integrere, deploye og hoste vores projekter. Vi overvejer Microsoft Azure DevOps.

  * Vi vil have, at udvikleroplevelsen er hurtig og pålidelig, både for opsætningen af devops, f.eks. konfiguration, og for den løbende brug, f.eks. hurtige byggetider.
  
  * Vi vil overveje at bruge Microsoft Azure som helhed til at hoste projektets apps, databaser osv.


### Beslutning

Besluttet imod Microsoft Azure DevOps.


### Status

Besluttet. Åben for at gense, hvis/når væsentlig ny information kommer.


## Detaljer


### Antagelser

Alle de sædvanlige devops-antagelser, såsom i bogen Accelerate.

  * Hurtige builds er en væsentlig hjælp. Det fremskynder feedbackløkkerne.

  * Vi kan skifte dele ind og ud fra alternative leverandører, dvs. vi vil måske medbringe vores egne hurtigere byggeservere, bruge vores eget valg af versionsstyringssystem eller koordinere med en selvhostet kontinuerlig integrationsserver.
  
  * Strømlinet brugervenlighed er en væsentlig hjælp, for udvikleroplevelsen og dermed for subtile områder som konsistens, klarhed, sikkerhed og indlæringskurvens lethed.

  * Når noget er i stykker eller problematisk, vil vi have en effektiv måde at rapportere problemet på. Det er især vigtigt for sikkerhedsrelaterede problemer.


### Begrænsninger

Ingen kendte. Azure har en offentliggjort forpligtelse til at fungere godt sammen med eksterne værktøjer.


### Standpunkter

Vi overvejede at bruge Microsoft Azure Devops versus AWS, som er den nuværende leverandør.

Vi eksperimenterede med Azure DevOps, Azure Pipelines, Azure Repo og opstart af en ny server i Azure via Terraform.

Vi eksperimenterede med at få support fra Microsoft-repræsentanter.

Vi indsamlede oplysninger fra kolleger på blogs og Hacker News.


### Argument

Azure DevOps reklamerer med et fremragende sæt tilbud, men de lever ikke op til det, de fungerer ikke godt sammen, og supporten er dårlig.

Vores førstehåndserfaring:

  * Azure-opsætningen er et rod af UI'er, hvoraf nogle overlapper med Microsoft-konti og nogle ikke. F.eks. er der en Azure-login, en Microsoft.com-login, en Live.com-login osv., og alle er i spil samtidig.

  * Vi stødte på et mindre sikkerhedsproblem under opsætningen og fandt ingen løsning. Vi forsøgte mange måder at rapportere det på til mange Microsoft-repræsentanter uden held. Vi rapporterede det med succes til Microsoft Security, som svarede, at det ikke vil blive rettet (won't fix).

  * Dokumentationen er ofte enten forkert eller forældet. I det mindste noget af det skyldes Microsofts dårlige søgemaskine, og noget skyldes middelmådig SEO.
  
  * Terraform-opsætningen er veldokumenteret og virker. Terraform-understøttelsen er dog svag sammenlignet med AWS, fordi Microsoft opbygger forretningsrelationer med leverandører for at lave gennemgående Terraform-opsætningseksempler.

Vores kollegers erfaringer:

  * Efter vores egen blinde vurdering ledte vi efter kollegers erfaringer. Det, vi fandt, bekræftede vores erfaringer.

  * Kolleger rapporterede yderligere problemer med byggetider og problemer med medbragt byggeserver. Disse problemer er væsentligt mere alvorlige end UI-problemer, fordi det at udføre builds er en byggepipelines kerneformål, og vi forventer at udføre mange om dagen.

  * Vi fandt fremragende deltagelse fra Azure-kolleger i diskussionsområderne. Ros til Microsoft for det. Vi er især imponerede over Edward Thomson, Azure PM og programmør, på grund af hans deltagelse, direkthed og tekniske forklaringer.


### Implikationer

At vælge Microsoft Azure DevOps ser ud til at være dyrere (~3x) i tid og omkostninger end ikke at vælge Azure.


## Relateret


### Relaterede beslutninger

Hvis vi vælger Azure DevOps, er der mange relaterede tilbud, herunder Azure Repo, Azure Pipeline osv. Vi tror, at hvis vi vælger Azure Devops, kan det gøre det lettere at bruge flere Azure-funktioner eller gøre det sværere at bruge andre leverandørers funktioner.

Vi tror, at Microsoft gør store fremskridt i udvikleroplevelse, og vi ser Microsoft foretage store opkøb af udviklerværktøjer (f.eks. GitHub) og afhængigheder (f.eks. Citus).

Hvis vi vælger Azure DevOps, vil vi måske lægge vægt på at vælge Microsofts opkøbstilbud, og vi vil måske også gribe opkøbstilbuddene an med mere omhu/vurdering på grund af potentiel vævsafstødning, f.eks. risiko for personaleomsætning.


### Relaterede krav

Vi vil have, at byggetiderne er meget hurtige. Vi accepterer at betale en høj præmie for det. Det skyldes, at vi vil iterere meget hurtigt.

Vi vil have, at pålideligheden er meget høj. Vi accepterer at betale en høj præmie for det. Det skyldes, at vi tester anvendelsestilfælde med høj værdi, herunder finansielle transaktioner, fortrolige transaktioner osv.

Vores top 4 devops-KPI'er omfatter gennemsnitlig gendannelsestid, hvilket kræver hurtige builds og høj pålidelighed.


### Relaterede artefakter

Vi vil have, at byggesystemet udsender artefakter, der er egnede til brug i andre systemer, såsom Artifactory.


### Relaterede principper

Let at gøre om. Vi kan evaluere Azure DevOps parallelt med den nuværende leverandør AWS.


## Noter


### Microsoft Devops CI: et utilfredsstillende eventyr

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Blogindlæg.

"Som softwareudvikler ved jeg af egen erfaring, hvor svært det er at bygge kvalitetsprodukter hurtigt og billigt. Det er en kunstform, som vi nogle gange får rigtig, og andre gange udarter til noget i retning af regeringens sundhedsside fra Obama-æraen. Vores kontrolniveau over det resulterende produkt varierer, og skylden for fiasko falder ofte på de forkerte personer i beslutningshierarkiet. Microsofts Azure DevOps (tidligere kendt som Visual Studio Team Services) er trods klart gode intentioner en perfekt storm af dårlige beslutninger og dårlig udførelse."


### Højdepunkter fra diskussionen på Hacker News

https://news.ycombinator.com/item?id=18983586

"Vi bruger Azure DevOps i stor udstrækning på mit arbejde, og efter at have brugt GitHub, Gitlab, selvhostede løsninger, Jenkins, TeamCity... er Azure DevOps helt i bund."

"UI'en er forfærdeligt klodset overalt. Det værste for mig er pull requests. Utroligt svært at arbejde sammen med folk på en pull request. Jeg kan ikke engang pege på "ét" bestemt problem - hos os er det i stykker overalt."

"Azure Devops er noget, jeg gerne vil elske. UI'en bliver ved med at ændre sig, men retter ikke de underliggende fejl, der har eksisteret i evigheder."

"Værktøjerne er ikke godt integreret, UI'en er virkelig langsom, der er ingen dashboardvisning af aktive pull requests, builds, releases osv. for mine yndlingsrepositories. Bygge-/deploymenttider er sindssygt langsomme."

"Vi forsøgte også at bruge Azure Boards (arbejdsopgaver, boards, backlogs osv.). Av. Det er et komplet UI-rod af usammenhængende idéer. I stedet for at implementere én ting godt har de implementeret to dusin ting dårligt."


### Windows Development MVP

Windows Development MVP her. Jeg føler, at jeg må bære noget af ansvaret for ikke at have været højere i stemmen om disse problemer. Men jeg må sige, at jeg er skuffet over at høre, at I er "overraskede" over UX-problemerne. Jeg har fortalt jeres folk, at UX'en er forfærdelig (f.eks. helt tilbage før lanceringen) og blev ved med at høre "vi ved det, vi retter det". Jeg vil begynde at formalisere feedbacken og sende den gennem rørene, hold øje. Jeg er også lokal (Bellevue) og ville gerne komme forbi og prøve at sende vores relativt enkle open source .net/wpf/uwp-app gennem pipelinen. Jeg formoder, at det vil være en øjenåbner for os begge.

Nogle eksempler:

* Man kan ikke bygge en pipeline med et git-repo, der indeholder submoduler

* Jeg fandt det umuligt at redigere PATH til noget brugerdefineret værktøj

* Oplevelsen med New Pipeline giver bare ikke meget mening; nye brugere, der klikker rundt, ender til sidst i den forkerte dokumentation.


### Resumé af Edward Thomson (Azure PM)

Jeg skrev koden, der fletter dine pull requests. Program Manager hos Microsoft for Azure DevOps; tidligere softwareingeniør på versionsstyringsværktøjer hos GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

Medvedligeholder af libgit2. https://libgit2.github.io

Medvært på All Things Git, podcasten om Git. https://www.allthingsgit.com/

Kurator af Developer Tools Weekly, et nyhedsbrev om udviklingsværktøjer. https://developertoolsweekly.com/
