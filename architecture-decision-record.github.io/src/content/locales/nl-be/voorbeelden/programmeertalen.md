# Programmeertalen

Inhoud:

* [Samenvatting](#samenvatting)
  * [Kwestie](#kwestie)
  * [Beslissing](#beslissing)
  * [Status](#status)
* [Details](#details)
  * [Aannames](#aannames)
  * [Beperkingen](#beperkingen)
  * [Standpunten](#standpunten)
  * [Argument](#argument)
  * [Implicaties](#implicaties)
* [Gerelateerd](#gerelateerd)
  * [Gerelateerde beslissingen](#gerelateerde-beslissingen)
  * [Gerelateerde eisen](#gerelateerde-eisen)
  * [Gerelateerde artefacten](#gerelateerde-artefacten)
  * [Gerelateerde principes](#gerelateerde-principes)
* [Notities](#notities)


## Samenvatting


### Kwestie

We moeten programmeertalen kiezen voor onze software. We hebben twee grote behoeften: een frontend-programmeertaal die geschikt is voor webapplicaties en een backend-programmeertaal die geschikt is voor serverapplicaties.


### Beslissing

We kiezen TypeScript voor de frontend.

We kiezen Rust voor de backend.


### Status

Besloten. We staan open voor nieuwe alternatieven zodra ze zich aandienen.


## Details


### Aannames

De frontend-applicaties zijn typisch:

  * Typische gebruikers en interacties

  * Typische browsers en systemen

  * Typische ontwikkelingen en deployments

De frontend-applicaties zullen waarschijnlijk snel evolueren:

  * We willen snelle, eenvoudige ontwikkelingen, deployments, iteraties enz. waarborgen.

  * We hechten waarde aan bewijsbaarheid, zoals typeveiligheid, en vinden het prima om iets meer werk te doen om dit te bereiken.

  * We hebben geen legacycompatibiliteit nodig.

De backend-applicaties zijn hoger dan typisch:

  * Hoger dan typische doelen voor kwaliteit, vooral bewijsbaarheid, betrouwbaarheid, beveiliging enz.

  * Hoger dan typische doelen voor bijna-realtime, dat wil zeggen dat we geen pauzes willen door garbage collection van virtuele machines.

  * Hoger dan typische doelen voor functioneel programmeren, vooral voor parallellisatie, multicoreverwerking en geheugenveiligheid.

We accepteren lagere compileersnelheden ten gunste van veiligheid tijdens het compileren en runtimesnelheden.


### Beperkingen

We hebben een sterke beperking op talen die bruikbaar zijn met de functiediensten van grote cloudproviders, zoals Amazon Lambda.


### Standpunten

We hebben deze talen overwogen:

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

Samenvatting per taal:

  * C: afgewezen vanwege lage veiligheid; Rust kan bijna alles beter.

  * C++: afgewezen omdat het een rommeltje is; Rust kan bijna alles beter.

  * Clojure: uitstekende modellering; beste benadering van Lisp; geweldige runtime op de JVM.
  
  * Elixir: uitstekende runtime inclusief deploybaarheid en concurrency; uitstekende ontwikkelaarservaring; relatief klein ecosysteem.

  * Erlang: uitstekende runtime inclusief deploybaarheid en concurrency; uitdagende ontwikkelaarservaring; relatief klein ecosysteem.

  * Elm: ziet er zeer veelbelovend uit; IBM publiceert belangrijke casestudy's met goede resultaten; kleiner ecosysteem.

  * Flow: interessante verbetering ten opzichte van JavaScript; ontwikkelaars stappen er echter van af.

  * Go: uitstekende ontwikkelaarservaring; uitstekende concurrency; maar een staat van dienst van slechte beslissingen die de taal verlammen.

  * Haskell: beste functionele taal; kleinere ontwikkelaarsgemeenschap; heeft niet genoeg gepubliceerde productiesuccessen behaald.

  * Java: uitstekende runtime; uitstekend ecosysteem; ondermaatse ontwikkelaarservaring.

  * JavaScript: populairste taal ooit; meest wijdverbreid ecosysteem.

  * Kotlin: lost zoveel van Java op; uitstekende ondersteuning door JetBrains; goede gepubliceerde gevallen van porteren van Java naar Kotlin.
  
  * Python: populairste taal voor systeembeheer; geweldige analysetools; goede webframeworks; maar door Google verlaten ten gunste van Go.

  * Ruby: beste ontwikkelaarservaring ooit; beste webframeworks; aardigste gemeenschap; maar erg traag; enigszins lastig te verpakken.

  * Rust: beste nieuwe taal; nadruk op zero-abstraction; nadruk op concurrency; echter een relatief klein ecosysteem; en heeft bewuste beperkingen op sommige soorten compilerversnellingen, bijv. directe geheugentoegang moet expliciet unsafe zijn.

  * TypeScript: voegt types toe aan JavaScript; geweldige transpiler; groeiende nadruk van ontwikkelaars op het porteren van JavaScript naar TypeScript; sterke steun van Microsoft.

We hebben besloten dat VM's een set afwegingen hebben die we nu niet nodig hebben, zoals extra complexiteit die runtimemogelijkheden biedt.

We geloven dat onze kernbeslissing wordt gedreven door twee transversale zorgen:

  * Voor de hoogste runtimesnelheid en de strakste systeemtoegang zouden we JavaScript en C kiezen.

  * Voor bijna de hoogste runtimesnelheid en bijna de strakste systeemtoegang kiezen we TypeScript en Rust.

Eervolle vermeldingen gaan naar de VM-talen en webframeworks die we zouden kiezen als we een VM-taal wilden:

  * Clojure en Luminus

  * Java en Spring

  * Elixir en Phoenix


### Implicaties

Frontend-ontwikkelaars moeten TypeScript leren. Dit is waarschijnlijk een gemakkelijke leercurve als de primaire ervaring van de ontwikkelaar JavaScript is.

Backend-ontwikkelaars moeten Rust leren. Dit is waarschijnlijk een gematigde leercurve als de primaire ervaring van de ontwikkelaar C/C++ is, en een moeilijke leercurve als de primaire ervaring Java, Python, Ruby of vergelijkbare talen met geheugenbeheer is. 

TypeScript en Rust zijn beide relatief nieuw. Dit betekent dat veel tools nog geen documentatie voor deze talen hebben. De devops-pijplijn moet bijvoorbeeld voor deze talen worden ingericht, en tot nu toe heeft geen van de devops-tools die we evalueren standaardvoorbeelden voor deze talen.

De compileertijden voor TypeScript en Rust zijn vrij traag. Een deel daarvan kan te maken hebben met de nieuwheid van de talen. We willen misschien kijken hoe we trage compileertijden kunnen verzachten, zoals door compile-on-demand, compile-concurrency enz.

IDE-ondersteuning voor deze talen is nog niet alomtegenwoordig en nog niet eersteklas. JetBrains verkoopt bijvoorbeeld de PyCharm-IDE voor eersteklas ondersteuning van Python, maar verkoopt geen IDE met eersteklas ondersteuning voor Rust; in plaats daarvan kan JetBrains een Rust-plug-in gebruiken die misschien 80% van de Rust-taalondersteuning biedt ten opzichte van de Python-taalondersteuning.


## Gerelateerd


### Gerelateerde beslissingen

We zullen streven naar ecosysteemkeuzes die aansluiten bij deze talen.

We willen bijvoorbeeld een IDE kiezen met goede mogelijkheden voor deze talen.

Voor ons frontend-webframework kiezen we bijvoorbeeld eerder voor een framework dat zich richt op TypeScript (bijv. Vue) dan voor een framework dat zich richt op gewoon JavaScript (bijv. React).


### Gerelateerde eisen

Onze hele toolchain moet deze talen ondersteunen.


### Gerelateerde artefacten

We verwachten dat we sommige geheimen naar omgevingsvariabelen exporteren.


### Gerelateerde principes

Twee keer meten, één keer bouwen. We geven prioriteit aan enige veiligheid boven enige snelheid.

Runtime is waardevoller dan compileertijd. We geven prioriteit aan gebruik door klanten boven gebruik door ontwikkelaars.


## Notities

Eventuele notities hier.
