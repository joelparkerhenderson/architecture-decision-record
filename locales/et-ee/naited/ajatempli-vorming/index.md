# Ajatempli vorming

Sisukord:

* [Kokkuvõte](#kokkuvõte)
  * [Küsimus](#küsimus)
  * [Otsus](#otsus)
  * [Olek](#olek)
* [Üksikasjad](#üksikasjad)
  * [Eeldused](#eeldused)
  * [Piirangud](#piirangud)
  * [Seisukohad](#seisukohad)
  * [Argument](#argument)
  * [Tagajärjed](#tagajärjed)
* [Seotud](#seotud)
  * [Seotud otsused](#seotud-otsused)
  * [Seotud nõuded](#seotud-nõuded)
  * [Seotud artefaktid](#seotud-artefaktid)
  * [Seotud põhimõtted](#seotud-põhimõtted)
* [Märkmed](#märkmed)


## Kokkuvõte


### Küsimus

Tahame suuta jälgida, millal asjad juhtuvad, kasutades ajatempleid ja järjepidevat ajatempli vormingut, mis töötab hästi kõigis meie süsteemides ja kolmandate osapoolte süsteemides.

Suhtleme süsteemidega, millel on erinevad ajatempli vormingud:

* JSON-sõnumitel puudub natiivne ajatempli vorming, seega peame valima, kuidas teisendada ajatempel stringiks ja string ajatempliks, st kuidas serialiseerida/deserialiseerida.

* Mõned rakendused on seatud kasutama kohalikku aega UTC-aja asemel. See võib olla mugav projektide jaoks, mis peavad kohanduma kohaliku ajaga, näiteks projektid, mis käivitavad sündmusi kohaliku aja alusel.

* Mõnel süsteemil on erinevad ajatäpsuse vajadused ja võimalused, näiteks ajaresolutsioon sekundites versus millisekundites versus nanosekundites. Näiteks Linuxi operatsioonisüsteemi käsk `date` kasutab vaikimisi sekundite täpsust, samas kui Nasdaqi börs tahab vaikimisi nanosekundite täpsust.


### Otsus

Valime standardse ajatempli vormingu ISO 8601 nanosekundilise täpsusega, täpsemalt "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

Vorming näitab aastat, kuud, päeva, tundi, minutit, sekundit, nanosekundeid ja Zulu ajavööndit ehk UTC-d, GMT-d.


### Olek

Otsustatud.


## Üksikasjad


### Eeldused

Peame neid ajatempli tekstistringe käsitlema, et teisendada ajatempel stringiks (ehk serialiseerida) ja teisendada string ajatempliks (ehk deserialiseerida).

Tahame vormingut, mida on üldiselt lihtne kasutada, lihtne teisendada ja inimesel lihtne lugeda.

Tahame ühilduvust laia valiku väliste süsteemidega, mida me ei saa kontrollida, nagu analüüsisüsteemid, andmebaasisüsteemid, finantssüsteemid.


### Piirangud

Mõnel süsteemil on ajatäpsuse piirangud. Näiteks macOS-i operatsioonisüsteemi käsk `date` suudab ajatäpsust printida sekundites, kuid mitte nanosekundites.


### Seisukohad

Kaalusime mitmeid valikuid:

* Unixi epohh, st üks kasvav arv.

* Lühike tekstivorming "YYYYMMDDTHHMMSSNNNNNNNNN".

* Kohaliku ajavööndi kasutamine versus UTC ajavöönd.


### Argument

Tüüpilises kasutuses hindame inimestele lihtsat lugemist/kirjutamist rohkem kui toorkiirust/suurust.

Tüüpilises kasutuses tahame vormingut, mis töötab hästi masinsüsteemides ja ka käsitsi, näiteks näidisandmete kirjutamisel, JSON-väljundi lugemisel, logifaili grep'imisel jne.

Ebatüüpilises kasutuses, nagu suure jõudlusega arvutus, eeldame, et tahame iga valitud tekstivormingut optimeerida, teisendades teksti kiiremaks vorminguks, näiteks programmeerimiskeele sisseehitatud kuupäevaobjekti tüübiks. Seega ei ole tekstivorming HPC jaoks eriti oluline.


### Tagajärjed

Meie erinevad tekstisüsteemid ja ajasüsteemid koonduvad selle vormingu suunas.


## Seotud


### Seotud otsused

Võime tahta ka kiiret/lihtsat viisi ajavahede ehk kestuste jälgimiseks. Need on Unixi epohhi ajatemplitega lihtsad.


### Seotud nõuded

Võime tahta oma otsust kohandada, nt kui meil on seotud nõue teatud liiki logisõnumi templi jaoks, näiteks Splunki, Sumo, ELK-i jne jaoks.


### Seotud artefaktid

Keelte vormindajad ja parserid:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Rosetta Code'i näited:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

SixArmi näited:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Seotud põhimõtted

Hõlpsasti tagasipööratav. Saame üsna hõlpsasti üle minna teisele vormingule, näiteks Unixi epohhile.

Lükka enneaegne optimeerimine edasi. Tüüpilises kasutuses ei hooli me eriti käputäiest lisamärkidest, näiteks sidekriipse ja koolonitega vormingust.


## Märkmed

Lisa siia märkmed.
