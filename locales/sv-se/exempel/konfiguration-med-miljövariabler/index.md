# Konfiguration med miljövariabler

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
  * [Implikationer ](#implikationer)
* [Relaterat](#relaterat)
  * [Relaterade beslut](#relaterade-beslut)
  * [Relaterade krav](#relaterade-krav)
  * [Relaterade artefakter](#relaterade-artefakter)
  * [Relaterade principer](#relaterade-principer)
* [Anteckningar](#anteckningar)


## Sammanfattning


### Problem

Vi vill att våra applikationer ska kunna konfigureras utöver artefakter/binärfiler/källkod, så att ett bygge kan bete sig olika beroende på sin driftsättningsmiljö.

  * För att åstadkomma detta vill vi använda konfiguration med miljövariabler.

  * Vi vill hantera konfigurationen med filer som vi kan versionshantera.

  * Vi vill erbjuda viss ergonomi för utvecklarupplevelsen, till exempel att veta vad som kan konfigureras och vilka standardvärden som är relevanta.


### Beslut

Beslutade oss för .env-filer med tillhörande standardfil och schemafil.


### Status

Beslutat. Öppna för att överväga nya förmågor när de dyker upp.


## Detaljer


### Antaganden

Vi föredrar att separera applikationskod och miljökod. Vi antar att appen behöver fungera olika i olika miljöer, till exempel i en utvecklingsmiljö, testmiljö, demomiljö, produktionsmiljö osv.

Vi föredrar branschpraxisen ”12 factor app” och ännu mer den relaterade praxisen ”15 factor app”.

Många av våra tidigare projekt har använt konventionen med en `.env`-fil eller en liknande `.env`-katalog. Det är vanligt att hålla dessa utanför versionshanteringen och i stället använda något annat sätt att driftsätta, versionshantera och hantera dem.


### Begränsningar

Vi vill hålla hemligheter utanför vårt versionshanteringssystem (VCS) för källkodshantering (SCM).

Vi vill sträva efter kompatibilitet med populära programvaruramverk och bibliotek. Till exempel har Node en modul ”dotenv” för att läsa konfiguration med miljövariabler.


### Ståndpunkter

Vi övervägde några tillvägagångssätt:

  * Lagra konfigurationen i appen, till exempel i en fil `config.js`.

  * Lagra konfigurationen i miljön, till exempel i en fil `.env`.

  * Hämta konfigurationen från en känd plats, till exempel en licensserver.


### Argument

Vi valde tillvägagångssättet med en .env-fil eftersom:

  * Det är populärt, även bland experter.

  * Det följer mönstret med `.env`-filer som våra team framgångsrikt har använt många gånger i många projekt.

  * Det är enkelt. Framför allt är vi tills vidare nöjda med de betydande avvägningar vi ser, till exempel avsaknad av granskningsförmåga jämfört med ett tillvägagångssätt med licensserver.


### Implikationer 

Vi behöver hitta ett sätt att skilja konfiguration med miljövariabler som är offentlig från all hantering av hemligheter.


## Relaterat


### Relaterade beslut

Vi förväntar oss att alla våra applikationer använder det här tillvägagångssättet.

Vi planerar att uppgradera alla våra applikationer som använder ett mindre kapabelt tillvägagångssätt, till exempel hårdkodning i en binärfil eller i källkod.

Vi låter alla våra applikationer som använder ett mer kapabelt tillvägagångssätt, till exempel en licensserver, vara som de är.


### Relaterade krav

Vi lägger till devops-förmågor för filerna, inklusive hookar, tester och kontinuerlig integration.

Vi behöver utbilda alla utvecklarkollegor om det här beslutet.



### Relaterade artefakter

Varje område där vi driftsätter kommer att behöva sin egen .env-fil och tillhörande filer.


### Relaterade principer

Lätt att ångra.


## Anteckningar


Exempelfil `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Exempelfil `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Exempelfil `.env.schema` med bara nycklarna:

```env
NAME
EMAIL
```
