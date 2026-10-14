# Monorepo eller multirepo

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


## Sammanfattning


### Problem

Vårt projekt innebär att utveckla tre huvudkategorier av programvara:

  * Frontend-GUI:n
  * Mellanvarutjänster
  * Backend-servrar

När vi utvecklar är vårt versionshanteringssystem (VCS) för källkodshantering (SCM) git.

Vi behöver välja hur vi använder git för att organisera vår kod.

Valet på toppnivå är att organisera som ”monorepo” eller ”polyrepo” eller ”hybrid”:

  * Monorepo innebär att vi lägger alla delar i ett stort repo
  * Polyrepo innebär att vi lägger varje del i sitt eget repo
  * Hybrid innebär någon blandning av monorepo och polyrepo

För mer information, se https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Beslut

Monorepo när en organisation/ett team/ett projekt är relativt litet och snabb iteration har högre prioritet än att upprätthålla stabilitet.

Polyrepo när en organisation/ett team/ett projekt är relativt stort och att upprätthålla stabilitet har högre prioritet än snabb iteration.


### Status

Beslutat. Öppet för omprövning om/när nya verktyg blir tillgängliga för att hantera monorepon och/eller polyrepon.


## Detaljer


### Antaganden

All kod som vi utvecklar är för en organisations erbjudanden och inte för allmänheten. Det vill säga att Broker-Dealer inte siktar på att ha något som liknar frivilliga utvecklare från allmänheten.


### Begränsningar

Begränsningar är väldokumenterade på https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Ståndpunkter

Vi övervägde monorepon i stil med Google, Facebook osv. Vi tror att eventuella skalningsproblem med monorepon ligger så långt fram i tiden att vi kommer att kunna utnyttja samma metoder som Google och Facebook när vi behöver dem.

Vi övervägde polyrepon i stil med typiska Git-projekt med öppen källkod, som Google Android, Facebook React osv. Vi tror att dessa är det bästa valet för allmänhetens deltagande (t.ex. vem som helst i världen kan arbeta med koden) och individuell tillgänglighet (t.ex. projektet används fristående, utan några andra delar).


### Argument

När en organisation/ett team/ett projekt är relativt litet väljer vi monorepo, eftersom snabb iteration har betydligt högre prioritet än att upprätthålla stabilitet

När en organisation/ett team/ett projekt är relativt stort väljer vi polyrepo, eftersom att upprätthålla stabilitet har betydligt högre prioritet än snabb iteration.


### Implikationer

Om det redan finns en pipeline för CI+CD kan vi behöva justera den för att testa flera projekt i ett repo.

CI+CD kan ta mer tid för ett fullständigt bygge för ett monorepo, eftersom CI+CD kan bygga alla projekt i monorepot.

Om en organisation/ett team/ett projekt växer kommer ett monorepo att få skalningsproblem.

Skalningsproblem med monorepon kan göra det alltmer värdefullt att övergå till ett polyrepo.

Övergången från monorepo till polyrepo är en betydande devops-uppgift och måste planeras, hanteras och programmeras.


## Relaterat


### Relaterade beslut

Vi kommer att skapa beslut för relaterade verktyg för att hantera monorepon (t.ex. Google Bazel) och polyrepon (t.ex. Lyft Refactorator).


### Relaterade krav

Vi behöver utveckla CI+CD-pipelinen så att den fungerar väl med git.


### Relaterade artefakter

Vi förväntar oss att repoorganisationen har relaterade artefakter för provisionering, konfigurationshantering, testning och liknande devops-områden. 


### Relaterade principer

Lätt att ångra. Om monorepot inte fungerar i praktiken, eller inte önskas av ledningen, är det enkelt att byta till polyrepo.

Kundfixering. Vi värdesätter att få projektet i kundernas händer, och vi tror att ett monorepo kan få oss dit snabbare än ett polyrepo, och även hjälpa oss att iterera snabbare.

Tänk stort. Google och Facebook är mycket starka förespråkare för monorepon framför polyrepon, eftersom alla kärnerbjudanden kan utvecklas/testas/driftsättas i samklang.


## Anteckningar

Lägg till eventuella anteckningar här.
