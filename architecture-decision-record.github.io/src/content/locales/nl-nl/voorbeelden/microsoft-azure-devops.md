# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: een onbevredigend avontuur](#microsoft-devops-ci-een-onbevredigend-avontuur)
  * [Hoogtepunten uit de discussie op Hacker News](#hoogtepunten-uit-de-discussie-op-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Samenvatting van Edward Thomson (Azure PM)](#samenvatting-van-edward-thomson-azure-pm)


## Samenvatting


### Kwestie

We willen devops gebruiken om onze projecten te bouwen, te integreren, te deployen en te hosten. We overwegen Microsoft Azure DevOps.

  * We willen dat de ontwikkelaarservaring snel en betrouwbaar is, zowel voor de inrichting van de devops, bijvoorbeeld configureren, als voor het voortdurende gebruik, bijvoorbeeld snelle buildtijden.
  
  * We willen overwegen Microsoft Azure als geheel te gebruiken, voor het hosten van de projectapps, databases enz.


### Beslissing

Besloten tegen Microsoft Azure DevOps.


### Status

Besloten. Open voor heroverweging als en wanneer er nieuwe significante informatie komt.


## Details


### Aannames

Alle gebruikelijke devops-aannames, zoals in het boek Accelerate.

  * Snelle builds zijn een aanzienlijke hulp. Dit versnelt de feedbackloops.

  * We kunnen onderdelen van alternatieve leveranciers in- of uitwisselen, dat wil zeggen dat we misschien onze eigen snellere buildservers willen meebrengen, ons eigen versiebeheersysteem willen kiezen of willen afstemmen met een zelfgehoste continue-integratieserver.
  
  * Gestroomlijnde bruikbaarheid is een aanzienlijke hulp, voor de ontwikkelaarservaring en op zijn beurt voor subtiele gebieden zoals consistentie, duidelijkheid, beveiliging en gemak van de leercurve.

  * Wanneer iets kapot is of problematisch, willen we een effectieve manier om het probleem te melden. Dit is vooral belangrijk voor beveiligingsgerelateerde problemen.


### Beperkingen

Geen bekend. Azure heeft een gepubliceerde toezegging om goed samen te werken met externe tools.


### Standpunten

We hebben overwogen Microsoft Azure Devops te gebruiken versus AWS, dat de huidige leverancier is.

We hebben geëxperimenteerd met Azure DevOps, Azure Pipelines, Azure Repo en het opstarten van een nieuwe server in Azure via Terraform.

We hebben geëxperimenteerd met het krijgen van ondersteuning van Microsoft-vertegenwoordigers.

We hebben informatie verzameld van vakgenoten op blogs en Hacker News.


### Argument

Azure DevOps adverteert met een uitstekende set aanbiedingen, maar die houden geen stand, werken niet goed samen en de ondersteuning is slecht.

Onze eigen ervaring:

  * De Azure-inrichting is een warboel van UI's, waarvan sommige overlappen met Microsoft-accounts en sommige niet. Er is bijvoorbeeld een Azure-aanmelding, een Microsoft.com-aanmelding, een Live.com-aanmelding enz. en ze zijn allemaal tegelijkertijd in het spel.

  * We kwamen tijdens de inrichting een klein beveiligingsprobleem tegen en vonden geen oplossing. We hebben op veel manieren geprobeerd het te melden bij veel Microsoft-vertegenwoordigers, zonder succes. We hebben het met succes gemeld bij Microsoft Security, dat antwoordde dat het niet wordt opgelost (won't fix).

  * Documentatie is vaak onjuist of verouderd. Althans een deel hiervan komt door de slechte zoekmachine van Microsoft en een deel door ondermaatse SEO.
  
  * De Terraform-inrichting is goed gedocumenteerd en werkt. De Terraform-ondersteuning is echter zwak vergeleken met AWS, omdat Microsoft zakelijke relaties met leveranciers opbouwt om doorlopende Terraform-inrichtingsvoorbeelden te maken.

Ervaringen van vakgenoten:

  * Nadat we onze eigen blinde beoordeling hadden gedaan, zochten we naar ervaringen van vakgenoten. Wat we vonden bevestigde onze ervaringen.

  * Vakgenoten meldden extra problemen met buildtijden en problemen met het meenemen van een eigen buildserver. Deze problemen zijn aanzienlijk ernstiger dan UI-problemen, omdat het uitvoeren van builds het kerndoel van een buildpijplijn is en we verwachten er veel per dag uit te voeren.

  * We vonden uitstekende deelname van Azure-teamleden in de discussiegebieden. Hulde aan Microsoft hiervoor. We zijn vooral onder de indruk van Edward Thomson, Azure PM en programmeur, vanwege zijn deelname, directheid en technische uitleg.


### Implicaties

Het kiezen van Microsoft Azure DevOps lijkt waarschijnlijk duurder (~3x) in tijd en kosten dan het niet kiezen van Azure.


## Gerelateerd


### Gerelateerde beslissingen

Als we Azure DevOps kiezen, zijn er veel gerelateerde aanbiedingen, waaronder Azure Repo, Azure Pipeline enz. We geloven dat als we Azure Devops kiezen, dit het gemakkelijker kan maken meer Azure-mogelijkheden te gebruiken, of het moeilijker kan maken de mogelijkheden van andere leveranciers te gebruiken.

We geloven dat Microsoft grote stappen zet in ontwikkelaarservaring, en we zien dat Microsoft grote overnames doet van ontwikkelaarstools (bijv. GitHub) en afhankelijkheden (bijv. Citus).

Als we Azure DevOps kiezen, willen we misschien de nadruk leggen op het kiezen van de aanbiedingen uit Microsoft-overnames, en willen we de overgenomen aanbiedingen mogelijk ook met meer zorg/beoordeling benaderen vanwege mogelijke afstoting, bijv. het risico op personeelsverloop.


### Gerelateerde eisen

We willen dat buildtijden zeer snel zijn. We accepteren daarvoor een hoge meerprijs. Dit komt doordat we zeer snel willen itereren.

We willen dat de betrouwbaarheid zeer hoog is. We accepteren daarvoor een hoge meerprijs. Dit komt doordat we gebruiksscenario's met hoge waarde testen, waaronder financiële transacties, vertrouwelijke transacties enz.

Onze top 4 devops-KPI's omvatten de gemiddelde hersteltijd, wat snelle builds en hoge betrouwbaarheid noodzakelijk maakt.


### Gerelateerde artefacten

We willen dat het buildsysteem artefacten uitvoert die geschikt zijn voor gebruik in andere systemen, zoals Artifactory.


### Gerelateerde principes

Gemakkelijk omkeerbaar. We kunnen Azure DevOps parallel evalueren met de huidige leverancier AWS.


## Notities


### Microsoft Devops CI: een onbevredigend avontuur

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Blogpost.

"Als softwareontwikkelaar weet ik uit eerste hand hoe moeilijk het is om snel en goedkoop kwaliteitsproducten te bouwen. Het is een kunstvorm die we soms goed doen en die soms ontaardt in iets als de overheidswebsite voor de gezondheidszorg uit het Obama-tijdperk. Ons niveau van controle over het resulterende product varieert, en de schuld voor mislukking valt vaak op de verkeerde mensen in de besluitvormingshiërarchie. Microsofts Azure DevOps (voorheen bekend als Visual Studio Team Services) is, ondanks duidelijk goede bedoelingen, een perfecte storm van slechte beslissingen en slechte uitvoering."


### Hoogtepunten uit de discussie op Hacker News

https://news.ycombinator.com/item?id=18983586

"We gebruiken Azure DevOps uitgebreid op mijn werk en, na GitHub, Gitlab, zelfgehoste oplossingen, Jenkins en TeamCity te hebben gebruikt... staat Azure DevOps absoluut onderaan."

"De UI is overal vreselijk onhandig. Het ergst voor mij zijn pull requests. Ongelooflijk moeilijk om met mensen aan een pull request te werken. Ik kan je niet eens op één specifiek probleem wijzen - bij ons is het overal kapot."

"Azure Devops is iets waar ik van wil houden. De UI blijft veranderen, maar lost onderliggende bugs die al eeuwen bestaan niet op."

"De tools zijn niet goed geïntegreerd, de UI is erg traag, er is geen dashboardweergave van actieve pull requests, builds, releases enz. voor mijn favoriete repo's. Build-/deploytijden zijn waanzinnig traag."

"We probeerden ook Azure Boards te gebruiken (werkitems, borden, backlogs enz.). Au. Het is een complete UI-rommel van onsamenhangende ideeën. In plaats van één ding goed te implementeren, hebben ze twee dozijn dingen vreselijk geïmplementeerd."


### Windows Development MVP

Windows Development MVP hier. Ik heb het gevoel dat ik een deel van de verantwoordelijkheid moet dragen omdat ik niet luider ben geweest over deze problemen. Maar ik moet zeggen dat ik teleurgesteld ben te horen dat jullie "verrast" zijn over de UX-problemen. Ik heb jullie mensen verteld dat de UX afschuwelijk is (bijv. al vóór de lancering) en kreeg steeds te horen "we weten het, we zijn het aan het oplossen". Ik ga de feedback formaliseren en door de pijplijn sturen, blijf op de hoogte. Ik ben ook lokaal (Bellevue) en zou graag langskomen om te proberen onze relatief eenvoudige open-source .net/wpf/uwp-app door de pijplijn te halen. Ik vermoed dat het een eye-opener zal zijn voor ons allebei.

Enkele voorbeelden:

* Je kunt geen pijplijn bouwen met een git-repo die submodules bevat

* Ik vond het onmogelijk om het PATH te bewerken voor wat aangepaste tooling

* De ervaring met een nieuwe pijplijn slaat gewoon nergens op; nieuwe gebruikers die rondklikken, belanden uiteindelijk bij de verkeerde documentatie.


### Samenvatting van Edward Thomson (Azure PM)

Ik schreef de code die je pull requests samenvoegt. Program Manager bij Microsoft voor Azure DevOps; voorheen softwareontwikkelaar aan versiebeheertools bij GitHub, Microsoft en SourceGear.

https://www.edwardthomson.com/

Co-maintainer van libgit2. https://libgit2.github.io

Co-host van All Things Git, de podcast over Git. https://www.allthingsgit.com/

Curator van Developer Tools Weekly, een nieuwsbrief over ontwikkeltools. https://developertoolsweekly.com/
