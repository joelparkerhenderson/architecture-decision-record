# Opbevaring af hemmeligheder

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Resumé


### Problemstilling

Vi skal gemme hemmeligheder, såsom adgangskoder, private nøgler, autentificeringstokens osv.

Nogle af hemmelighederne er brugerorienterede. For eksempel vil vores udvikler gerne kunne bruge sin mobiltelefon til at slå en adgangskode til en tjeneste op.

Nogle af hemmelighederne er systemorienterede. For eksempel skal vores pipeline til kontinuerlig levering kunne slå loginoplysningerne til vores cloudhosting op.


### Beslutning

Bitwarden til brugerorienterede hemmeligheder.

Vault by HashiCorp til systemorienterede hemmeligheder.


### Status

Besluttet. Vi er åbne for nye muligheder, efterhånden som de dukker op.


## Detaljer


### Antagelser

Til dette formål og vores nuværende situation sætter vi pris på brugerorienteret bekvemmelighed, såsom brugbare mobilapps.

  * Vi vil sikre hurtig, nem adgang på farten, for eksempel for en udvikler, der har vagtdienst inden for pålidelighedsteknik.

  * Vi vil kunne dele nogle hemmeligheder mellem udvalgte personer, for eksempel et team.

Vi forsøger ikke at løse for én enkelt leverandør, for eksempel at gemme alle hemmeligheder udelukkende hos Amazon eller Azure eller Google.

Vi vil ikke have ad hoc-tilgange som "husk det" eller "skriv det på en seddel" eller "find selv ud af, hvordan du gemmer det".

Vores sikkerhedsmodel til dette formål er tilfreds med at bruge velansete COTS-leverandører, for eksempel SaaS-værktøjer til administration af adgangskoder.


### Begrænsninger

Lige nu vil vi have noget, der er enkelt, dvs. intet behov for at skrive kode, intet behov for at installere servere, intet behov for at foretage en stor forpligtelse, intet behov for at standardisere alle.


### Standpunkter

Vi overvejede:

1. Brugerorienterede færdige adgangskodeadministratorer: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG osv.

2. Systemorienterede COTS-adgangskodeadministratorer: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Delingsorienterede tilgange: brug af et delt Google-dokument, en delt Slack-kanal, en delt netværksmappe osv.

4. Lavteknologiske ad hoc-tilgange, såsom at huske, skrive en seddel eller stole på, at hver bruger selv finder ud af, hvordan det gemmes.


### Argument

Bitwarden, LastPass, 1Password og Dashlane er alle kommercielle færdige produkter.

  * Lignende typer funktioner til brugere, teams, organisationer osv.

  * Desktopfunktioner til Windows og Mac og mobilfunktioner til Android og iOS.

  * Browserudvidelser til Chrome og Firefox til automatisk udfyldning af formularer osv.

Bitwarden har to fordele i forhold til de andre:

  * Bitwarden er open source, hvilket betyder, at sikkerheden kan gennemgås af kolleger, og at virksomheden også generelt er respekteret af sikkerhedsbevidste udviklere.

  * Anekdoter fra softwarefolk beskriver en betydelig præference for Bitwarden frem for de andre.

En typisk god artikel: https://jcs.org/2017/11/17/bitwarden

En typisk afstemningsside med side-om-side-sammenligning: https://stackshare.io/stackups/bitwarden-vs-dashlane

Vi udskyder KeyPass, pass, GPG osv., fordi der er yderligere kompleksitet. Alle ser ud som gode løsninger til tekniske brugere. GPG ser især godt ud til tekniske brugere, der vil have kommandoorienterede funktioner på tværs af systemer.

Vi udskyder KMS, fordi det har leverandørbinding til én enkelt leverandør.

Vi vælger Vault til systemorienterede behov, fordi anmeldelserne er overraskende positive, og fordi HashiCorp har en fremragende meritliste inden for software og support i topklasse.

Vi nedlægger veto mod tilgangene med deling, for eksempel via delte dokumenter, delte kanaler, delte netværksmapper osv. Disse giver ikke de sikkerhedskvaliteter, vi ønsker.

Vi nedlægger veto mod de lavteknologiske ad hoc-tilgange, fordi vi alle er enige om, at det ikke er en langsigtet vej frem.


### Implikationer

Udviklere kan have brug for at holde styr på hemmeligheder to steder: Bitwarden til brugerorienteret adgang og Vault til systemorienteret adgang.


## Relateret


### Relaterede beslutninger

Beslutningen om, hvilken CI/CD-server der skal vælges, skal inkludere beviser for evnen til at få adgang til hemmeligheder.

Vi skal beslutte, hvordan hemmelighederne skal administreres med hensyn til politikker, rotationer, organisationer osv.


### Relaterede krav

Hemmelighederne vil have relaterede krav til compliance, revision og HR-onboarding/offboarding.


### Relaterede artefakter

Vi forventer, at vi kan eksportere nogle hemmeligheder til miljøvariabler.


### Relaterede principper

Let at gøre om.

Let at køre parallelt, dvs. det er enkelt at bruge en række forskellige adgangskodeadministratorer.

Billigt at prøve, dvs. der er en gratis prøveperiode og ingen forpligtelse.


## Noter

Evalueringsnoter her. Noterne er alle offentlige kommentarer på forskellige devops-diskussionsfora.


### Vault by HashiCorp

Vault er præcis, hvad du vil have her. 

Men smid ikke bare Vault i produktion, sæt det først op i et testmiljø, fordi HashiCorps dokumentation kan være ret mangelfuld, selv om deres produkter er fantastiske.

Meget stejl indlæringskurve, og det er ikke trivielt at sætte op. 

Den første opsætning er lidt af en plage. Det er helt klart det værd, og fællesskabet vil støtte det godt nok til, at du kan klare dig igennem.

Forfærdelig dokumentation, men der er masser af guider online fra folk, der har sat det op, og hvis du kombinerer nogle af dem, har du en fungerende opsætning.

Den første opsætning krævede rod med deres helm-charts (vault og consul). Teknisk set kan du bruge mange andre backends, men jeg anbefaler virkelig, virkelig ikke det. Backend/consul kan være lillebitte, hvis du ikke har masser af data at gemme.

Gør dig under alle omstændigheder fortrolig med at bruge CLI'en, fordi GUI'en er mere som en proof-of-concept/reklameportal for deres enterprise-udgave.

Det faktum, at du ikke bare kan "fylde det op", er en plage. Hvis du for eksempel har 5 felter, skal du manuelt tilføje hvert felt for hvert element. Så det er ikke sådan, at du foruddefinerer felter for en bestemt kategori og udfylder disse felter for alle elementer i den kategori, men mere at "du genererer alt hver gang", hvilket (efter min mening) er en plage.

Du kan også se på goldfish som en UI oven på vault. Det gør det ret rart at få dit team med. De har også en demo. 1. Sæt consul op. 2. Sæt vault op, der peger på consul. 3. Sæt goldfish op, der peger på vault. 3. Sæt et cron-job op, der kører consul snapshot til sikkerhedskopier.



### LastPass

LastPass Teams. Vi bruger det, har brugerdefinerede skabeloner, ACL'er, og efter min mening mangler der ikke noget.

Jeg implementerede LastPass i min organisation og giver det et C+/B-. Det største problem på det seneste er mangel på pålidelighed. I de seneste 90 dage har der været flere timer, hvor bokse blev tvunget i offlinetilstand. Det er ikke ideelt for min organisation, fordi vi bogstaveligt talt har 4.000+ adgangskoder gemt i 20+ delte mapper. Som du kan forestille dig med så mange adgangskoder, bliver mindst nogle få opdateret eller tilføjet hver dag. Vi har en DR-plan, hvis problemer varer mere end en time eller to: et script signerer og krypterer hver nat et CSV-dump af boksen, som kan importeres til keepass.

LastPass har haft urapporterede glimt af forringet service: login "virker", men henter ingen websteder, tilfældige funktioner i administratorpanelet er i stykker, og nøgler deles ikke korrekt for nye delte mapper på øverste niveau. Jeg har en særlig "key push"-/sikkerhedskopibruger, der findes i hver gruppe. Normalt løser login som den bruger alle problemer med nøgledeling, men ikke når tjenesten er forringet, uanset hvad statussiden siger...

Til integration kan det være enkelt, hvis du har ordentlige ACL'er med en model med mindst mulige rettigheder, f.eks. hvis en bruger har både læse- og skrive- og kun læserettigheder på et element eller en mappe, får vedkommende kun læserettigheder. Desværre er min organisations ACL'er ikke de bedste, så jeg endte med at bruge JSON-provisionerings-API'et og ~500 linjer python, fordi afhængigheden i vores hundredvis af ACL'er ikke kortlagde godt til modellen med mindst mulige rettigheder. Til sidst hentede jeg alle ACL'er, en bruger var i, og lavede en slags afhængighedsvandring.

Hvis din ACL- eller gruppestruktur allerede er bygget med en struktur med mindst mulige rettigheder for øje, fungerer AD/LDAP-synkroniseringsværktøjet til Windows fint.

Kontakt deres salgsteam, så kan de arrangere en længere Enterprise-prøveperiode. Sørg for, at du fuldt ud forstår dets begrænsninger, før du trykker på aftrækkeren. Vi havde en del vækstsmerter, men bortset fra serversideafbrydelser eller forringelser har det været utroligt glat.


### Bitwarden

Bitwarden har gode værktøjer omkring sig (WebUI, CLI, mobil, desktop). Kan selvhostes og er ret nemt at sætte op. Ret god dokumentation og et værktøj, der anbefales af PrivacyTools.


### EnvKey

https://www.envkey.com/ er en saas. Virkelig nem at implementere, integrere og administrere.

Funktioner:

  * Beskyt API-nøgler og loginoplysninger.

  * Hold konfigurationen synkroniseret overalt.

  * Smart, end-to-end-krypteret administration af konfiguration og hemmeligheder. 

  * Forhindr usikker deling og konfigurationsspredning. 

  * Integrér på minutter.

Muligheder:

  * Administrér konfiguration og adgangsniveauer for alle dine apps, miljøer og teams ét sted.

  * Konfigurér ethvert udviklings- eller servermiljø med blot én enkelt miljøvariabel.

Fordele:

  * Fantastisk landingsside.

  * Klart værdiløfte.

  * Visuelt fremragende webapp.

  * Overlegne eksempeldata, f.eks. Algolia, AWS, Datadog, GitHub, Stripe osv.

  * Talte med grundlæggeren i 30 minutter om virksomheden, UI'en osv. Dane lyder velinformeret, ærlig om fordele og ulemper og en brugbar partner.

  * Virksomheden er grundlæggende en typisk Y Combinator-virksomhed med 1 grundlægger. Rejste $120K i 2018-01.

  * Fokus er på at nå virksomhedsfunktioner, især at gå fra EnvKey-cloudhosting til enten on-prem eller BYOC.

  * Mulig vej frem: start med EnvKey for enkelhedens skyld, og tilføj så senere (eller parallelt) Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant er en open source-tjeneste til hemmelighedsstyring, der tilbyder brugervenlig lagring af og adgang til hemmeligheder på en sikker måde, fra udviklerne hos Lyft.

KMS-autentificering: Confidant løser autentificeringens "hønen og ægget"-problem ved at bruge AWS KMS og IAM til at lade IAM-roller generere sikre autentificeringstokens, der kan verificeres af Confidant. Confidant administrerer også KMS-grants til dine IAM-roller, hvilket gør det muligt for IAM-rollerne at generere tokens, der kan bruges til autentificering mellem services eller til at sende krypterede beskeder mellem services.

Kryptering i hvile af versionerede hemmeligheder: Confidant gemmer hemmeligheder på en kun-tilføj-måde i DynamoDB og genererer en unik KMS-datanøgle for hver revision af hver hemmelighed ved hjælp af den symmetriske autentificerede kryptografi Fernet.

En brugervenlig webgrænseflade til administration af hemmeligheder: Confidant leverer en AngularJS-webgrænseflade, der gør det muligt for slutbrugere nemt at administrere hemmeligheder, kortlægninger af hemmeligheder til services og ændringshistorikken.


### Devolutions Password Server

https://server.devolutions.net/

Sikr, administrér og overvåg adgang til privilegerede konti og sessioner.

En omfattende, højsikker adgangskodeboks, der lader dig kontrollere adgangen til dine privilegerede konti og samtidig forbedrer den samlede netværkssynlighed for systemadministratorer og giver en problemfri oplevelse for slutbrugere.

Funktioner: centraliseret organisationsadgangskodeboks, brugerspecifik privat boks, adgangskodeadministrator, indsprøjtning af legitimationsoplysninger,
Active Directory-integration, rollebaseret adgangskontrol, tofaktorautentificering, virksomhedsklar, IP-begrænsninger, administrationsfunktioner, automatisk adgangskodegenerator, adgang via mobilapp, adgangskodehistorik, adgangsrapporter, e-mailadvarsler.

  * understøtter datakryptering

  * understøtter flere autentificeringsskemaer, herunder LDAP, O365 og lokale brugere MED MFA-understøttelse fra flere kilder

  * flere repos/bokse med detaljerede adgangskontroller til flere teams

  * moderne web-UI

  * private bokse til legitimationsoplysninger og forbindelser til personlige legitimationsoplysninger/forbindelser

  * mobilapps til iOS/Android

  * revisionslogs for hvert element, hvem/hvad/hvornår med et valgfrit spørgsmål om, hvorfor de tilgår det

  * tilpasselige skabeloner (selv om de nativt understøtter hundredvis af forbindelsestyper)

  * masser af flere funktioner og en tyk klient til Windows/Mac (Remote Desktop Manager), du kan synkronisere med, og som i høj grad udvider mulighederne... enklikforbindelser

  * prisen er ikke så ringe – op til 15 brugere koster adgangskodeserveren $500 om året


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Funktioner i on-premises-versionen: 

  * Total kontrol over dine end-to-end-sikkerhedssystemer og din infrastruktur

  * Deploy softwaren i dit eget on-premises-datacenter eller din egen instans af en virtuel privat cloud

  * Opfyld juridiske og regulatoriske forpligtelser, der kræver, at alle data og systemer er on-premises

Funktioner i cloudversionen:

  * Software-som-en-tjeneste-modellen lader dig tilmelde dig og komme i gang med det samme

  * Elastisk skalerbarhed, når du vokser

  * Kontroller og redundans leveret af Azure med 99,9 % SLA for oppetid

Brugerfeedback:

  * Vi brugte det produkt før. Det var så nemt at omgå, og reglerne virker kun for kloge mennesker. Dovne eller dumme brugere kan nemt ødelægge det i et teamområde. Priserne kan forhandles, når du taler med dem.

  * Du kan køre det med SQL express og en Win 7-computer. 

  * Billigt.
