# Lagring av hemligheter

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Sammanfattning


### Problem

Vi behöver lagra hemligheter, som lösenord, privata nycklar, autentiseringstoken osv.

Vissa av hemligheterna är användarorienterade. Till exempel vill vår utvecklare kunna använda sin mobiltelefon för att slå upp ett lösenord till en tjänst.

Vissa av hemligheterna är systemorienterade. Till exempel behöver vår pipeline för kontinuerlig leverans kunna slå upp inloggningsuppgifterna för vår molnhosting.


### Beslut

Bitwarden för användarorienterade hemligheter

Vault by HashiCorp för systemorienterade hemligheter.


### Status

Beslutat. Vi är öppna för nya alternativ när de dyker upp.


## Detaljer


### Antaganden

För det här ändamålet och vårt nuvarande läge värdesätter vi användarorienterad bekvämlighet, som användbara mobilappar.

  * Vi vill säkerställa snabb, enkel åtkomst på språng, till exempel för en utvecklare som gör jourarbete inom tillförlitlighetsteknik.

  * Vi vill kunna dela vissa hemligheter mellan utvalda personer, till exempel ett team.

Vi försöker inte lösa för en enskild leverantör, till exempel att lagra alla hemligheter uteslutande hos Amazon eller Azure eller Google.

Vi vill inte ha ad hoc-tillvägagångssätt som ”kom ihåg det” eller ”skriv det på en lapp” eller ”lista ut ditt eget sätt att lagra det”.

Vår säkerhetsmodell för det här ändamålet är nöjd med att använda välansedda COTS-leverantörer, till exempel SaaS-verktyg för lösenordshantering.


### Begränsningar

Just nu vill vi ha något som är enkelt, dvs. inget behov av att skriva kod, inget behov av att installera servrar, inget behov av att göra ett stort åtagande, inget behov av att standardisera alla.


### Ståndpunkter

Vi övervägde:

1. Användarorienterade färdiga lösenordshanterare: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG osv.

2. Systemorienterade COTS-lösenordshanterare: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Delningsorienterade tillvägagångssätt: att använda ett delat Google-dokument, en delad Slack-kanal, en delad nätverksmapp osv.

4. Lågteknologiska ad hoc-tillvägagångssätt, som att komma ihåg, skriva en lapp eller förlita sig på att varje användare listar ut sitt eget sätt.


### Argument

Bitwarden, LastPass, 1Password och Dashlane är alla kommersiella färdiga produkter.

  * Liknande typer av funktioner för användare, team, organisationer osv.

  * Skrivbordsförmåga för Windows och Mac, och mobilförmåga för Android och iOS.

  * Webbläsartillägg för Chrome och Firefox, för automatisk ifyllning av formulär osv.

Bitwarden har två fördelar jämfört med de andra:

  * Bitwarden har öppen källkod, vilket innebär att säkerheten kan granskas av kollegor och att företaget också är allmänt uppskattat av säkerhetsinriktade utvecklare.

  * Anekdoter från programvarufolk beskriver en betydande preferens för Bitwarden framför de andra.

Ett typiskt bra reportage: https://jcs.org/2017/11/17/bitwarden

En typisk omröstningssajt med jämförelse sida vid sida: https://stackshare.io/stackups/bitwarden-vs-dashlane

Vi skjuter upp KeyPass, pass, GPG osv. eftersom det finns ytterligare komplexitet. Alla ser ut som bra lösningar för tekniska användare. GPG ser särskilt bra ut för tekniska användare som vill ha kommandoorienterade förmågor över system.

Vi skjuter upp KMS eftersom det har inlåsning till en enskild leverantör.

Vi väljer Vault för systemorienterade behov, eftersom recensionerna är förvånansvärt positiva, och eftersom HashiCorp har en utmärkt meritlista när det gäller förstklassig programvara och support.

Vi lägger in veto mot tillvägagångssätten med delning, till exempel via delade dokument, delade kanaler, delade nätverksmappar osv. Dessa ger inte de säkerhetskvaliteter vi vill ha.

Vi lägger in veto mot de lågteknologiska ad hoc-tillvägagångssätten, eftersom vi alla är överens om att det inte är en långsiktig väg framåt.


### Implikationer

Utvecklare kan behöva hålla reda på hemligheter på två ställen: Bitwarden för användarorienterad åtkomst och Vault för systemorienterad åtkomst.


## Relaterat


### Relaterade beslut

Beslutet om vilken CI/CD-server som ska väljas måste inkludera bevis på förmåga att komma åt hemligheter.

Vi kommer att behöva besluta hur hemligheterna ska hanteras, när det gäller policyer, rotationer, organisationer osv.


### Relaterade krav

Hemligheterna kommer att ha relaterade krav för efterlevnad, granskning och HR-introduktion/avslutning.


### Relaterade artefakter

Vi förväntar oss att vi kan exportera vissa hemligheter till miljövariabler.


### Relaterade principer

Lätt att ångra.

Lätt att köra parallellt, dvs. det är enkelt att använda en mängd olika lösenordshanterare.

Billigt att prova, dvs. det finns en gratis provperiod och inget åtagande.


## Anteckningar

Utvärderingsanteckningar här. Anteckningarna är alla offentliga kommentarer på olika devops-diskussionsforum.


### Vault by HashiCorp

Vault är exakt vad du vill ha här. 

Men släng inte bara in Vault i produktion, sätt upp det i en testmiljö först, eftersom HashiCorps dokumentation kan vara ganska bristfällig även om deras produkter är fantastiska.

Mycket brant inlärningskurva och det är inte trivialt att sätta upp. 

Den första uppsättningen är lite av en plåga. Det är absolut värt det, och gemenskapen kommer att stödja det tillräckligt bra för att du ska klara dig.

Hemsk dokumentation, men det finns massor av guider online från folk som har satt upp det och om du kombinerar några av dem kommer du att ha en fungerande uppsättning.

Den första uppsättningen krävde pill med deras helm-diagram (vault och consul). Tekniskt sett kan du använda många andra backends, men jag rekommenderar verkligen, verkligen inte det. Backend/consul kan vara pytteliten om du inte har massor av data att lagra.

Bekanta dig definitivt med att använda CLI:t, eftersom GUI:t är mer som en proof-of-concept/reklamportal för deras enterprise-utgåva.

Det faktum att du inte bara kan ”fylla på det” är en plåga. Om du till exempel har 5 fält måste du manuellt lägga till varje fält för varje objekt. Det är alltså inte så att du fördefinierar fält för en specifik kategori och fyller i dessa fält för alla objekt i den kategorin, utan det är mer som att ”du genererar allt varje gång”, vilket (enligt mig) är en plåga.

Du kanske också vill titta på goldfish som ett UI ovanpå vault. Det gör det ganska trevligt att få ditt team med på det. De har också en demo. 1. Sätt upp consul. 2. Sätt upp vault som pekar på consul. 3. Sätt upp goldfish som pekar på vault. 3. Sätt upp något cron-jobb som kör consul snapshot för säkerhetskopior.



### LastPass

LastPass Teams. Vi använder det, har anpassade mallar, ACL, inget saknas enligt mig.

Jag implementerade LastPass i min organisation och ger det ett C+/B-. Det största problemet på sistone är brist på tillförlitlighet. Under de senaste 90 dagarna har det funnits flera timmar då valv tvingades in i offline-läge. Det här är inte idealiskt för min organisation eftersom vi bokstavligen har 4 000+ lösenord lagrade i 20+ delade mappar. Som du kan föreställa dig med så många lösenord uppdateras eller läggs minst några till varje dag. Vi har en DR-plan om problem varar mer än en timme eller två: ett skript signerar och krypterar en CSV-dump av valvet varje natt som kan importeras till keepass.

LastPass har haft orapporterade glimtar av försämrad tjänst: inloggningen ”fungerar” men hämtar inga webbplatser, slumpmässiga funktioner i administratörspanelen är trasiga och nycklar delas inte korrekt för nya delade mappar på toppnivå. Jag har en särskild ”key push”-/säkerhetskopieringsanvändare som finns i varje grupp. Vanligtvis löser inloggning som den användaren alla problem med nyckeldelning men inte när tjänsten är försämrad oavsett vad statussidan säger...

För integration kan det vara enkelt om du har ordentliga ACL med en modell med minsta möjliga behörighet, t.ex. om en användare har både läs & skriv och endast läs på en post eller mapp får de bara läsbehörigheter. Tyvärr är min organisations ACL inte de bästa, så jag slutade med att använda JSON-provisionerings-API:et och ~500 rader python eftersom det beroende i våra hundratals ACL inte mappade väl till modellen med minsta möjliga behörighet. Till slut hämtade jag alla ACL en användare fanns i och gjorde en sorts beroendevandring.

Om din ACL- eller gruppstruktur redan är byggd med en struktur med minsta möjliga behörighet i åtanke fungerar AD/LDAP-synkroniseringsverktyget för Windows bra.

Kontakta deras säljteam så kan de ordna en längre Enterprise-provperiod. Se till att du fullt ut förstår dess begränsningar innan du trycker på avtryckaren. Vi hade en hel del växtvärk, men bortsett från avbrott eller försämringar på serversidan har det varit otroligt smidigt.


### Bitwarden

Bitwarden har bra verktyg runt omkring (WebUI, CLI, mobil, skrivbord). Kan egenhostas och är ganska enkelt att sätta upp. Ganska bra dokumentation och ett verktyg som rekommenderas av PrivacyTools.


### EnvKey

https://www.envkey.com/ är en saas. Riktigt enkelt att implementera, integrera och hantera.

Funktioner:

  * Skydda API-nycklar och inloggningsuppgifter.

  * Håll konfigurationen synkroniserad överallt.

  * Smart, end-to-end-krypterad hantering av konfiguration och hemligheter. 

  * Förhindra osäker delning och konfigurationsspridning. 

  * Integrera på minuter.

Förmågor:

  * Hantera konfiguration och åtkomstnivåer för alla dina appar, miljöer och team på ett ställe.

  * Konfigurera vilken utvecklings- eller servermiljö som helst med bara en enda miljövariabel.

Fördelar:

  * Bra startsida.

  * Tydligt värdeerbjudande.

  * Visuellt utmärkt webbapp.

  * Överlägsen exempeldata, t.ex. Algolia, AWS, Datadog, GitHub, Stripe osv.

  * Pratade med grundaren i 30 minuter om företaget, UI:t osv. Dane låter välinformerad, ärlig om för-/nackdelarna och en gångbar partner.

  * Företaget är i grunden ett typiskt Y Combinator-företag med 1 grundare. Samlade in $120K i 2018-01.

  * Fokus ligger på att nå företagsfunktioner, särskilt att gå från EnvKey-molnhosting till antingen on-prem eller BYOC.

  * Möjlig väg framåt: börja med EnvKey för enkelhetens skull, och sedan senare (eller parallellt) lägga till Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant är en tjänst för hantering av hemligheter med öppen källkod som erbjuder användarvänlig lagring av och åtkomst till hemligheter på ett säkert sätt, från utvecklarna på Lyft.

KMS-autentisering: Confidant löser autentiseringens ”hönan och ägget”-problem genom att använda AWS KMS och IAM för att låta IAM-roller generera säkra autentiseringstoken som kan verifieras av Confidant. Confidant hanterar också KMS-grants för dina IAM-roller, vilket gör att IAM-rollerna kan generera token som kan användas för autentisering mellan tjänster, eller för att skicka krypterade meddelanden mellan tjänster.

Kryptering i vila av versionshanterade hemligheter: Confidant lagrar hemligheter på ett enbart-tilläggs-sätt i DynamoDB och genererar en unik KMS-datanyckel för varje revision av varje hemlighet, med hjälp av den symmetriska autentiserade kryptografin Fernet.

Ett användarvänligt webbgränssnitt för att hantera hemligheter: Confidant tillhandahåller ett AngularJS-webbgränssnitt som gör att slutanvändare enkelt kan hantera hemligheter, mappningar av hemligheter till tjänster och ändringshistoriken.


### Devolutions Password Server

https://server.devolutions.net/

Säkra, hantera och övervaka åtkomst till privilegierade konton och sessioner.

Ett omfattande, högsäkrat lösenordsvalv som låter dig kontrollera åtkomsten till dina privilegierade konton, samtidigt som det förbättrar den övergripande nätverkssynligheten för systemadministratörer och ger en sömlös upplevelse för slutanvändare.

Funktioner: centraliserat organisationsvalv för lösenord, användarspecifikt privat valv, lösenordshanterare, injicering av inloggningsuppgifter,
Active Directory-integration, rollbaserad åtkomstkontroll, tvåfaktorsautentisering, företagsredo, IP-begränsningar, hanteringsförmågor, automatisk lösenordsgenerator, åtkomst via mobilapp, lösenordshistorik, åtkomstrapporter, e-postlarm.

  * stöder datakryptering

  * stöder flera autentiseringsscheman inklusive LDAP, O365 och lokala användare MED stöd för MFA från flera källor

  * flera repon/valv med detaljerade åtkomstkontroller för flera team

  * modernt webb-UI

  * privata valv för inloggningsuppgifter och anslutningar för personliga uppgifter/anslutningar

  * mobilappar för iOS/Android

  * granskningsloggar för varje post, vem/vad/när med en valfri fråga om varför de kommer åt den

  * anpassningsbara mallar (även om de nativt stöder hundratals anslutningstyper)

  * massor av fler funktioner och en tjock klient för Windows/Mac (Remote Desktop Manager) som du kan synkronisera med och som kraftigt utökar alternativen... enklicksanslutningar

  * priset är inte så illa – upp till 15 användare kostar $500 per år för lösenordsservern


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Funktioner i versionen för installation på plats: 

  * Total kontroll över dina end-to-end-säkerhetssystem och din infrastruktur

  * Driftsätt programvaran i ditt eget datacenter på plats eller din egen instans av ett virtuellt privat moln

  * Uppfyll juridiska och regulatoriska skyldigheter som kräver att alla data och system finns på plats

Funktioner i molnversionen:

  * Programvara-som-en-tjänst-modellen låter dig registrera dig och komma igång direkt

  * Elastisk skalbarhet när du växer

  * Kontroller och redundans som levereras av Azure med 99,9 % SLA för drifttid

Användarfeedback:

  * Vi använde den produkten förut. Den var så lätt att kringgå och reglerna fungerar bara för smarta människor. Lata eller dumma användare kan lätt förstöra den i ett teamområde. Priserna är förhandlingsbara när du pratar med dem.

  * Du kan köra den med SQL express och en Win 7-dator. 

  * Billigt.
