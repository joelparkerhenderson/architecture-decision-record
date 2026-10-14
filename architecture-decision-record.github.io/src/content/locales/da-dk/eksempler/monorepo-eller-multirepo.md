# Monorepo eller multirepo

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

Vores projekt involverer udvikling af tre hovedkategorier af software:

  * Frontend-GUI'er
  * Middlewareservices
  * Backendservere

Når vi udvikler, er vores versionsstyringssystem (VCS) til kildekodestyring (SCM) git.

Vi skal vælge, hvordan vi bruger git til at organisere vores kode.

Det overordnede valg er at organisere som "monorepo", "polyrepo" eller "hybrid":

  * Monorepo betyder, at vi lægger alle dele i ét stort repository
  * Polyrepo betyder, at vi lægger hver del i sit eget repository
  * Hybrid betyder en blanding af monorepo og polyrepo

For mere se https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Beslutning

Monorepo, når en organisation/et team/et projekt er relativt lille, og hurtig iteration har højere prioritet end at opretholde stabilitet.

Polyrepo, når en organisation/et team/et projekt er relativt stort, og at opretholde stabilitet har højere prioritet end hurtig iteration.


### Status

Besluttet. Åben for at gense, hvis/når nye værktøjer til at styre monorepoer og/eller polyrepoer bliver tilgængelige.


## Detaljer


### Antagelser

Al den kode, vi udvikler, er til én organisations tilbud og ikke til offentligheden. Dvs. at mægler-forhandleren ikke sigter mod at have noget som frivillige udviklere fra offentligheden.


### Begrænsninger

Begrænsninger er veldokumenterede på https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Standpunkter

Vi overvejede monorepoer i stil med Google, Facebook osv. Vi tror, at eventuelle skaleringsproblemer med monorepoer ligger så langt ude i fremtiden, at vi vil kunne udnytte de samme praksisser som Google og Facebook, når vi får brug for dem.

Vi overvejede polyrepoer i stil med typiske Git-open source-projekter, såsom Google Android, Facebook React osv. Vi tror, at disse er det bedste valg til offentlig deltagelse (f.eks. kan alle i verden arbejde på koden) og individuel tilgængelighed (f.eks. bruges projektet for sig selv uden andre dele).


### Argument

Når en organisation/et team/et projekt er relativt lille, vælger vi monorepo, fordi hurtig iteration har væsentligt højere prioritet end at opretholde stabilitet

Når en organisation/et team/et projekt er relativt stort, vælger vi polyrepo, fordi det at opretholde stabilitet har væsentligt højere prioritet end hurtig iteration.


### Implikationer

Hvis der allerede er en pipeline til CI+CD, skal vi muligvis justere den til at teste flere projekter i ét repository.

CI+CD kan tage længere tid til et fuldt build af et monorepo, fordi CI+CD kan bygge alle projekter i monorepoet.

Hvis en organisation/et team/et projekt vokser, vil et monorepo få skaleringsproblemer.

Skaleringsproblemer med monorepoer kan gøre det stadig mere værdifuldt at skifte til et polyrepo.

Overgangen fra monorepo til polyrepo er en betydelig devops-opgave og skal planlægges, styres og programmeres.


## Relateret


### Relaterede beslutninger

Vi vil oprette beslutninger om relaterede værktøjer til at styre monorepoer (f.eks. Google Bazel) og polyrepoer (f.eks. Lyft Refactorator).


### Relaterede krav

Vi skal udvikle CI+CD-pipelinen, så den fungerer godt med git.


### Relaterede artefakter

Vi forventer, at repositoryorganisationen har relaterede artefakter til provisionering, konfigurationsstyring, test og lignende devops-områder. 


### Relaterede principper

Let at gøre om. Hvis monorepoet ikke fungerer i praksis eller ikke ønskes af ledelsen, er det enkelt at skifte til polyrepo.

Kundeobsession. Vi sætter pris på at få projektet i hænderne på kunder, og vi tror, at et monorepo kan få os derhen hurtigere end et polyrepo og også hjælpe os med at iterere hurtigere.

Tænk stort. Google og Facebook er meget stærke fortalere for monorepoer frem for polyrepoer, fordi alle kernetilbud kan udvikles/testes/deployes i fællesskab.


## Noter

Tilføj eventuelle noter her.
