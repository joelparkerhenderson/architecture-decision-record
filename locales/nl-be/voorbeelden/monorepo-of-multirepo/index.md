# Monorepo of multirepo

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

Ons project omvat de ontwikkeling van drie hoofdcategorieën software:

  * Frontend-GUI's
  * Middlewareservices
  * Backendservers

Bij ontwikkeling is ons versiebeheersysteem (VCS) voor broncodebeheer (SCM) git.

We moeten kiezen hoe we git gebruiken om onze code te organiseren.

De keuze op het hoogste niveau is organiseren als "monorepo", "polyrepo" of "hybride":

  * Monorepo betekent dat we alle onderdelen in één grote repository zetten
  * Polyrepo betekent dat we elk onderdeel in een eigen repository zetten
  * Hybride betekent een mix van monorepo en polyrepo

Zie voor meer https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Beslissing

Monorepo wanneer een organisatie/team/project relatief klein is en snelle iteratie een hogere prioriteit heeft dan het behouden van stabiliteit.

Polyrepo wanneer een organisatie/team/project relatief groot is en het behouden van stabiliteit een hogere prioriteit heeft dan snelle iteratie.


### Status

Besloten. Open voor heroverweging als en wanneer nieuwe tooling beschikbaar komt voor het beheren van monorepo's en/of polyrepo's.


## Details


### Aannames

Alle code die we ontwikkelen is voor het aanbod van één organisatie en niet voor het grote publiek. Dat wil zeggen dat de broker-dealer er niet naar streeft iets als vrijwillige ontwikkelaars uit het grote publiek te hebben.


### Beperkingen

Beperkingen zijn goed gedocumenteerd op https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Standpunten

We hebben monorepo's overwogen in de stijl van Google, Facebook enz. We denken dat eventuele schaalproblemen van monorepo's zo ver in de toekomst liggen dat we tegen de tijd dat we ze nodig hebben dezelfde praktijken kunnen benutten als Google en Facebook.

We hebben polyrepo's overwogen in de stijl van typische Git-open-sourceprojecten, zoals Google Android, Facebook React enz. We denken dat dit de beste keuze is voor deelname van het grote publiek (bijv. iedereen ter wereld kan aan de code werken) en voor individuele beschikbaarheid (bijv. het project wordt zelfstandig gebruikt, zonder andere onderdelen).


### Argument

Wanneer een organisatie/team/project relatief klein is, kiezen we monorepo, omdat snelle iteratie een aanzienlijk hogere prioriteit heeft dan het behouden van stabiliteit

Wanneer een organisatie/team/project relatief groot is, kiezen we polyrepo, omdat het behouden van stabiliteit een aanzienlijk hogere prioriteit heeft dan snelle iteratie.


### Implicaties

Als er al een pijplijn voor CI+CD bestaat, moeten we die mogelijk aanpassen om meerdere projecten binnen één repository te testen.

CI+CD kan meer tijd kosten voor een volledige build van een monorepo, omdat CI+CD alle projecten in de monorepo kan bouwen.

Als een organisatie/team/project groeit, krijgt een monorepo schaalproblemen.

Schaalproblemen van een monorepo kunnen een overgang naar een polyrepo steeds waardevoller maken.

Overgang van monorepo naar polyrepo is een aanzienlijke devops-taak en moet worden gepland, beheerd en geprogrammeerd.


## Gerelateerd


### Gerelateerde beslissingen

We zullen beslissingen opstellen voor gerelateerde tooling om monorepo's (bijv. Google Bazel) en polyrepo's (bijv. Lyft Refactorator) te beheren.


### Gerelateerde eisen

We moeten de CI+CD-pijplijn ontwikkelen zodat die goed met git werkt.


### Gerelateerde artefacten

We verwachten dat de organisatie van de repository gerelateerde artefacten heeft voor provisioning, configuratiebeheer, testen en vergelijkbare devops-gebieden. 


### Gerelateerde principes

Gemakkelijk omkeerbaar. Als de monorepo in de praktijk niet werkt of niet door het leiderschap gewenst is, is het eenvoudig over te stappen op polyrepo.

Klantgerichtheid. We hechten waarde aan het zo snel mogelijk in handen van klanten krijgen van het project, en we geloven dat een monorepo ons daar sneller kan brengen dan een polyrepo en ons ook helpt sneller te itereren.

Denk groot. Google en Facebook zijn zeer sterke voorstanders van monorepo's boven polyrepo's, omdat alle kernproducten gezamenlijk kunnen worden ontwikkeld/getest/gedeployd.


## Notities

Voeg hier eventuele notities toe.
