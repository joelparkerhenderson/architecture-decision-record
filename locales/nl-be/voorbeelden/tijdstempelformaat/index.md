# Tijdstempelformaat

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

We willen kunnen bijhouden wanneer dingen gebeuren met behulp van tijdstempels en met een consistent tijdstempelformaat dat goed werkt in al onze systemen en systemen van derden.

We werken samen met systemen die verschillende tijdstempelformaten hebben:

* JSON-berichten hebben geen native tijdstempelformaat, dus we moeten kiezen hoe we een tijdstempel naar een tekenreeks converteren en een tekenreeks naar een tijdstempel, dat wil zeggen hoe we serialiseren/deserialiseren.

* Sommige applicaties zijn ingesteld om lokale tijd te gebruiken in plaats van UTC-tijd. Dit kan handig zijn voor projecten die zich moeten aanpassen aan de lokale tijd, zoals projecten die gebeurtenissen activeren op basis van lokale tijd.

* Sommige systemen hebben verschillende behoeften en mogelijkheden voor tijdprecisie, zoals een tijdresolutie van seconden versus milliseconden versus nanoseconden. Het commando `date` van het Linux-besturingssysteem gebruikt bijvoorbeeld standaard een tijdprecisie van seconden, terwijl de Nasdaq-beurs standaard een tijdprecisie van nanoseconden wil.


### Beslissing

We kiezen het standaard tijdstempelformaat ISO 8601 met nanoseconde-precisie, specifiek "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

Het formaat toont het jaar, de maand, de dag, het uur, de minuut, de seconde, de nanoseconden en de Zulu-tijdzone, ook wel UTC, GMT.


### Status

Besloten.


## Details


### Aannames

We moeten deze tijdstempeltekenreeksen verwerken: van een tijdstempel naar een tekenreeks converteren (ook wel serialiseren) en van een tekenreeks naar een tijdstempel converteren (ook wel deserialiseren).

We willen een formaat dat over het algemeen gemakkelijk te gebruiken is, gemakkelijk te converteren en gemakkelijk leesbaar voor mensen.

We willen compatibiliteit met een breed scala aan externe systemen die we niet kunnen controleren, zoals analysesystemen, databasesystemen en financiële systemen.


### Beperkingen

Sommige systemen hebben beperkingen in tijdprecisie. Het commando `date` van het macOS-besturingssysteem kan bijvoorbeeld tijdprecisie in seconden afdrukken, maar niet in nanoseconden.


### Standpunten

We hebben een reeks opties overwogen:

* Unix-epoch, dat wil zeggen één oplopend getal.

* Beknopt tekstformaat "YYYYMMDDTHHMMSSNNNNNNNNN".

* Een lokale tijdzone gebruiken versus de UTC-tijdzone.


### Argument

Voor typisch gebruik hechten we meer waarde aan gemakkelijk lezen/schrijven door mensen dan aan pure snelheid/grootte.

Voor typisch gebruik willen we een formaat dat prima werkt in machinesystemen en ook goed handmatig werkt, zoals bij het schrijven van voorbeelddata, het lezen van JSON-uitvoer, het grep-pen van een logbestand enz.

Voor atypisch gebruik, zoals high performance computing, verwachten we dat we elk gekozen tekstformaat willen optimaliseren door de tekst te converteren naar een sneller formaat, zoals het ingebouwde datumobjecttype van een programmeertaal. Het tekstformaat doet er dus niet veel toe voor HPC.


### Implicaties

Onze verschillende tekstsystemen en tijdsystemen zullen naar dit formaat convergeren.


## Gerelateerd


### Gerelateerde beslissingen

We willen misschien ook een snelle/eenvoudige manier om tijdsverschillen, ook wel duren, bij te houden. Die zijn eenvoudig met Unix-epoch-tijdstempels.


### Gerelateerde eisen

We willen onze beslissing misschien aanpassen, bijvoorbeeld als we een gerelateerde eis hebben voor een specifiek soort loggingberichtstempel, zoals voor Splunk, Sumo, ELK enz.


### Gerelateerde artefacten

Formatters en parsers per taal:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Voorbeelden van Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Voorbeelden van SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Gerelateerde principes

Gemakkelijk omkeerbaar. We kunnen vrij gemakkelijk overstappen op een ander formaat, zoals Unix-epoch.

Voortijdige optimalisatie uitstellen. Voor typisch gebruik geven we niet veel om een handvol extra tekens, zoals bij een formaat met streepjes en dubbele punten.


## Notities

Voeg hier notities toe.
