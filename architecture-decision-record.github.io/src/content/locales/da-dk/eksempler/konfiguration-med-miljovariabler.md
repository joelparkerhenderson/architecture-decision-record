# Konfiguration med miljøvariabler

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

Vi ønsker, at vores applikationer kan konfigureres ud over artefakter/binærfiler/kildekode, så ét build kan opføre sig forskelligt afhængigt af sit deploymentmiljø.

  * For at opnå dette vil vi bruge konfiguration med miljøvariabler.

  * Vi vil styre konfigurationen ved hjælp af filer, som vi kan versionsstyre.

  * Vi vil give noget udvikleroplevelsesergonomi, såsom at vide, hvad der kan konfigureres, og eventuelle relevante standardværdier.


### Beslutning

Besluttet: .env-filer med tilhørende standardværdifil og skemafil.


### Status

Besluttet. Åben for at overveje nye muligheder, efterhånden som de dukker op.


## Detaljer


### Antagelser

Vi foretrækker at adskille applikationskode og miljøkode. Vi antager, at appen skal fungere forskelligt i forskellige miljøer, såsom et udviklingsmiljø, testmiljø, demomiljø, produktionsmiljø osv.

Vi foretrækker brancheprincippet "12 factor app" og endnu mere den relaterede praksis "15 factor app".

Mange af vores tidligere projekter har brugt konventionen med en `.env`-fil eller en lignende `.env`-mappe. Det er almindelig praksis at holde disse uden for versionsstyring og i stedet bruge en anden måde at deploye, versionere og administrere dem på.


### Begrænsninger

Vi vil holde hemmeligheder uden for vores versionsstyringssystem (VCS) til kildekodestyring (SCM).

Vi stræber efter kompatibilitet med populære softwareframeworks og -biblioteker. For eksempel har Node et modul "dotenv" til at læse konfiguration med miljøvariabler.


### Standpunkter

Vi overvejede nogle tilgange:

  * Gem konfigurationen i appen, f.eks. i en fil `config.js`.

  * Gem konfigurationen i miljøet, f.eks. i en fil `.env`.

  * Hent konfigurationen fra en kendt lokation, f.eks. en licensserver.


### Argument

Vi valgte tilgangen med en .env-fil, fordi:

  * Den er populær, også blandt eksperter.

  * Den følger mønsteret med `.env`-filer, som vores teams har brugt med succes mange gange i mange projekter.

  * Den er enkel. Navnlig er vi indtil videre trygge ved de væsentlige afvejninger, vi ser, såsom mangel på revisionsfunktioner sammenlignet med en tilgang med en licensserver.


### Implikationer

Vi skal finde en måde at adskille miljøvariabelkonfiguration, der er offentlig, fra enhver hemmelighedsstyring.


## Relateret


### Relaterede beslutninger

Vi forventer, at alle vores applikationer bruger denne tilgang.

Vi vil planlægge at opgradere alle vores applikationer, der bruger en mindre kapabel tilgang, såsom hardcoding i en binærfil eller i kildekode.

Vi lader alle vores applikationer, der bruger en mere kapabel tilgang, såsom en licensserver, forblive uændrede.


### Relaterede krav

Vi tilføjer devops-funktioner til filerne, herunder hooks, tests og kontinuerlig integration.

Vi skal uddanne alle udviklerkolleger i denne beslutning.



### Relaterede artefakter

Hvert område, hvor vi deployer, har brug for sin egen .env-fil og relaterede filer.


### Relaterede principper

Let at gøre om.


## Noter


Eksempelfil `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Eksempelfil `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Eksempelfil `.env.schema` med kun nøglerne:

```env
NAME
EMAIL
```
