# Programmeringssprog

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


## Resumé


### Problemstilling

Vi skal vælge programmeringssprog til vores software. Vi har to store behov: et frontend-programmeringssprog, der er egnet til webapplikationer, og et backend-programmeringssprog, der er egnet til serverapplikationer.


### Beslutning

Vi vælger TypeScript til frontend.

Vi vælger Rust til backend.


### Status

Besluttet. Vi er åbne for nye alternativer, efterhånden som de dukker op.


## Detaljer


### Antagelser

Frontend-applikationerne er typiske:

  * Typiske brugere og interaktioner

  * Typiske browsere og systemer

  * Typiske udviklinger og deployments

Frontend-applikationerne vil sandsynligvis udvikle sig hurtigt:

  * Vi vil sikre hurtige, nemme udviklinger, deployments, iterationer osv.

  * Vi sætter pris på bevisbarhed, såsom typesikkerhed, og vi er fine med at gøre lidt mere arbejde for at opnå det.

  * Vi har ikke brug for ældre kompatibilitet.

Backend-applikationerne er højere end typisk:

  * Højere end typiske mål for kvalitet, især bevisbarhed, pålidelighed, sikkerhed osv.

  * Højere end typiske mål for næsten-realtid, dvs. vi vil ikke have pauser på grund af garbage collection i virtuelle maskiner.

  * Højere end typiske mål for funktionel programmering, især til parallelisering, multikernebehandling og hukommelsessikkerhed.

Vi accepterer lavere kompileringshastigheder til fordel for sikkerhed ved kompilering og kørselshastigheder.


### Begrænsninger

Vi har en stærk begrænsning på sprog, der kan bruges med større cloududbyderes funktionstjenester, såsom Amazon Lambda.


### Standpunkter

Vi overvejede disse sprog:

  * C

  * C++

  * Clojure
  
  * Elixir
  
  * Erlang
  
  * Elm
  
  * Flow
  
  * Go
  
  * Haskell
  
  * Java
  
  * JavaScript
  
  * Kotlin
  
  * Python
  
  * Ruby
  
  * Rust
  
  * TypeScript



### Argument

Resumé pr. sprog:

  * C: afvist på grund af lav sikkerhed; Rust kan næsten alt bedre.

  * C++: afvist, fordi det er noget rod; Rust kan næsten alt bedre.

  * Clojure: fremragende modellering; bedste tilnærmelse til Lisp; fremragende kørselsmiljø på JVM.
  
  * Elixir: fremragende kørselsmiljø inklusive deployerbarhed og samtidighed; fremragende udvikleroplevelse; relativt lille økosystem.

  * Erlang: fremragende kørselsmiljø inklusive deployerbarhed og samtidighed; udfordrende udvikleroplevelse; relativt lille økosystem.

  * Elm: ser meget lovende ud; IBM udgiver større casestudier med gode resultater; mindre økosystem.

  * Flow: interessant forbedring i forhold til JavaScript; udviklere bevæger sig dog væk fra det.

  * Go: fremragende udvikleroplevelse; fremragende samtidighed; men en historik med dårlige beslutninger, der lammer sproget.

  * Haskell: bedste funktionelle sprog; mindre udviklerfællesskab; har ikke opnået nok offentliggjorte produktionssucceser.

  * Java: fremragende kørselsmiljø; fremragende økosystem; middelmådig udvikleroplevelse.

  * JavaScript: det mest populære sprog nogensinde; det mest udbredte økosystem.

  * Kotlin: retter så meget af Java; fremragende opbakning fra JetBrains; gode offentliggjorte tilfælde af portering fra Java til Kotlin.
  
  * Python: mest populære sprog til systemadministration; fremragende analyseværktøjer; gode webframeworks; men opgivet af Google til fordel for Go.

  * Ruby: bedste udvikleroplevelse nogensinde; bedste webframeworks; flotteste fællesskab; men meget langsomt; noget svært at pakke.

  * Rust: bedste nye sprog; vægt på nulabstraktion; vægt på samtidighed; dog relativt lille økosystem; og har bevidste begrænsninger på nogle former for compileraccelerationer, f.eks. skal direkte hukommelsesadgang eksplicit være unsafe.

  * TypeScript: tilføjer typer til JavaScript; fremragende transpiler; voksende udviklerfokus på portering fra JavaScript til TypeScript; stærk opbakning fra Microsoft.

Vi besluttede, at VM'er har et sæt afvejninger, som vi ikke har brug for lige nu, såsom ekstra kompleksitet, der giver kørselsfunktioner.

Vi tror, at vores kernebeslutning drives af to tværgående hensyn:

  * For hurtigste kørselshastighed og tætteste systemadgang ville vi vælge JavaScript og C.

  * For næsten hurtigste kørselshastighed og næsten tætteste systemadgang vælger vi TypeScript og Rust.

Hæderlige omtaler går til de VM-sprog og webframeworks, vi ville vælge, hvis vi ville have et VM-sprog:

  * Clojure og Luminus

  * Java og Spring

  * Elixir og Phoenix


### Implikationer

Frontend-udviklere skal lære TypeScript. Det er sandsynligvis en nem indlæringskurve, hvis udviklerens primære erfaring er med JavaScript.

Backend-udviklere skal lære Rust. Det er sandsynligvis en moderat indlæringskurve, hvis udviklerens primære erfaring er med C/C++, og en svær indlæringskurve, hvis udviklerens primære erfaring er med Java, Python, Ruby eller lignende sprog med hukommelsesstyring. 

TypeScript og Rust er begge relativt nye. Det betyder, at mange værktøjer endnu ikke har dokumentation for disse sprog. For eksempel skal devops-pipelinen sættes op til disse sprog, og indtil videre har ingen af de devops-værktøjer, vi evaluerer, standardeksempler for disse sprog.

Kompileringstiderne for TypeScript og Rust er ret langsomme. Noget af det kan skyldes sprogenes nyhed. Vi vil måske se på, hvordan vi kan afbøde langsomme kompileringstider, f.eks. ved kompilering efter behov, kompileringssamtidighed osv.

IDE-understøttelse for disse sprog er endnu ikke allestedsnærværende og endnu ikke førsteklasses. For eksempel sælger JetBrains PyCharm IDE til førsteklasses understøttelse af Python, men sælger ikke en IDE med førsteklasses understøttelse af Rust; i stedet kan JetBrains bruge et Rust-plugin, der giver måske 80 % af Rust-sprogunderstøttelsen i forhold til Python-sprogunderstøttelsen.


## Relateret


### Relaterede beslutninger

Vi vil stræbe efter økosystemvalg, der stemmer overens med disse sprog.

For eksempel vil vi vælge en IDE, der har gode funktioner til disse sprog.

For eksempel er det mere sandsynligt, at vi til vores frontend-webframework beslutter os for et framework, der har tendens til at sigte mod TypeScript (f.eks. Vue), end et framework, der har tendens til at sigte mod almindelig JavaScript (f.eks. React).


### Relaterede krav

Vores hele værktøjskæde skal understøtte disse sprog.


### Relaterede artefakter

Vi forventer, at vi kan eksportere nogle hemmeligheder til miljøvariabler.


### Relaterede principper

Mål to gange, byg én gang. Vi prioriterer en vis sikkerhed over en vis hastighed.

Kørselstid er mere værdifuld end kompileringstid. Vi prioriterer kundebrug over udviklerbrug.


## Noter

Eventuelle noter her.
