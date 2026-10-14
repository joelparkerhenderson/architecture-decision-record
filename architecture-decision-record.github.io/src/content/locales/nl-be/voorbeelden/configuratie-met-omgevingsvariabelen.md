# Configuratie met omgevingsvariabelen

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

We willen dat onze applicaties configureerbaar zijn buiten artefacten/binaries/broncode om, zodat één build zich anders kan gedragen afhankelijk van de deploymentomgeving.

  * Hiervoor willen we configuratie met omgevingsvariabelen gebruiken.

  * We willen de configuratie beheren met bestanden die we onder versiebeheer kunnen plaatsen.

  * We willen enige ergonomie voor de ontwikkelaarservaring bieden, zoals weten wat er kan worden geconfigureerd en wat de relevante standaardwaarden zijn.


### Beslissing

Gekozen voor .env-bestanden met een bijbehorend standaardwaardenbestand en schemabestand.


### Status

Besloten. Open voor nieuwe mogelijkheden zodra die zich aandienen.


## Details


### Aannames

We geven de voorkeur aan het scheiden van applicatiecode en omgevingscode. We nemen aan dat de app in verschillende omgevingen anders moet werken, zoals in een ontwikkelomgeving, testomgeving, demo-omgeving, productieomgeving enz.

We geven de voorkeur aan de branchepraktijk "12 factor app" en nog meer aan de verwante praktijk "15 factor app".

Veel van onze eerdere projecten hebben de conventie van een `.env`-bestand of vergelijkbare `.env`-map gebruikt. Het is gebruikelijk om deze buiten versiebeheer te houden en ze op een andere manier te deployen, van versies te voorzien en te beheren.


### Beperkingen

We willen geheimen buiten ons versiebeheersysteem (VCS) voor broncodebeheer (SCM) houden.

We streven naar compatibiliteit met populaire softwareframeworks en -bibliotheken. Node heeft bijvoorbeeld een module "dotenv" voor het lezen van configuratie met omgevingsvariabelen.


### Standpunten

We hebben een paar aanpakken overwogen:

  * Configuratie opslaan in de app, zoals in een bestand `config.js`.

  * Configuratie opslaan in de omgeving, zoals in een bestand `.env`.

  * Configuratie ophalen van een bekende locatie, zoals een licentieserver.


### Argument

We hebben gekozen voor de aanpak van een .env-bestand omdat:

  * Het populair is, ook onder experts.

  * Het het patroon van `.env`-bestanden volgt dat onze teams vaak en succesvol in veel projecten hebben gebruikt.

  * Het eenvoudig is. Met name kunnen we voorlopig leven met de aanzienlijke afwegingen die we zien, zoals het ontbreken van auditmogelijkheden in vergelijking met een aanpak met een licentieserver.


### Implicaties

We moeten een manier bedenken om configuratie met omgevingsvariabelen die openbaar is te scheiden van geheimenbeheer.


## Gerelateerd


### Gerelateerde beslissingen

We verwachten dat al onze applicaties deze aanpak gebruiken.

We zullen plannen elke applicatie die een minder capabele aanpak gebruikt, zoals hardcoden in een binary of in broncode, te upgraden.

We laten elke applicatie die een capabelere aanpak gebruikt, zoals een licentieserver, ongewijzigd.


### Gerelateerde eisen

We zullen devops-mogelijkheden voor de bestanden toevoegen, waaronder hooks, tests en continue integratie.

We moeten alle ontwikkelaars in het team over deze beslissing trainen.



### Gerelateerde artefacten

Elk gebied waar we deployen heeft zijn eigen .env-bestand en gerelateerde bestanden nodig.


### Gerelateerde principes

Gemakkelijk omkeerbaar.


## Notities


Voorbeeldbestand `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Voorbeeldbestand `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Voorbeeldbestand `.env.schema` met alleen de sleutels:

```env
NAME
EMAIL
```
