# Format tat-timestamp

Werrej:

* [Sommarju](#sommarju)
  * [Kwistjoni](#kwistjoni)
  * [Deċiżjoni](#deċiżjoni)
  * [Stat](#stat)
* [Dettalji](#dettalji)
  * [Suppożizzjonijiet](#suppożizzjonijiet)
  * [Restrizzjonijiet](#restrizzjonijiet)
  * [Pożizzjonijiet](#pożizzjonijiet)
  * [Argument](#argument)
  * [Implikazzjonijiet](#implikazzjonijiet)
* [Relatati](#relatati)
  * [Deċiżjonijiet relatati](#deċiżjonijiet-relatati)
  * [Rekwiżiti relatati](#rekwiżiti-relatati)
  * [Artefatti relatati](#artefatti-relatati)
  * [Prinċipji relatati](#prinċipji-relatati)
* [Noti](#noti)


## Sommarju


### Kwistjoni

Irridu nkunu nistgħu nittraċċaw meta jiġru l-affarijiet billi nużaw timestamps u billi nużaw format konsistenti tat-timestamp li jaħdem tajjeb fuq is-sistemi kollha tagħna u s-sistemi ta' partijiet terzi.

Nintaraġixxu ma' sistemi li għandhom formati differenti tat-timestamp:

* Il-messaġġi JSON m'għandhomx format nattiv tat-timestamp, għalhekk neħtieġu nagħżlu kif nikkonvertu timestamp għal string, u nikkonvertu string għal timestamp, jiġifieri kif nserjalizzaw/nideserjalizzaw.

* Xi applikazzjonijiet huma ssettjati biex jużaw il-ħin lokali, aktar milli l-ħin UTC. Dan jista' jkun konvenjenti għal proġetti li jridu jaġġustaw għall-ħin lokali, bħal proġetti li jqanqlu avvenimenti li huma bbażati fuq il-ħin lokali.

* Xi sistemi għandhom bżonnijiet u kapaċitajiet differenti ta' preċiżjoni tal-ħin, bħall-użu ta' riżoluzzjoni tal-ħin ta' sekondi vs. millisekondi vs. nanosekondi. Pereżempju, il-kmand Sat Oct 17 08:13:25 BST 2026 tas-sistema operattiva Linux juża preċiżjoni default tal-ħin ta' sekondi, filwaqt li l-borża tal-ishma Nasdaq trid preċiżjoni default tal-ħin ta' nanosekondi.


### Deċiżjoni

Nagħżlu l-format standard tat-timestamp ISO 8601 bi preċiżjoni ta' nanosekondi, speċifikament "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

Il-format juri s-sena, ix-xahar, il-jum, is-siegħa, il-minuta, is-sekonda, in-nanosekondi, u ż-żona tal-ħin Zulu magħrufa wkoll bħala UTC, GMT.


### Stat

Deċiż.


## Dettalji


### Suppożizzjonijiet

Neħtieġu nimmaniġġjaw dawn l-istrings tat-test tat-timestamp, biex nikkonvertu minn timestamp għal string (magħruf ukoll bħala serjalizzazzjoni) u nikkonvertu minn string għal timestamp (magħruf ukoll bħala deserjalizzazzjoni).

Irridu format li ġeneralment huwa faċli biex jintuża, faċli biex jiġi kkonvertit, u faċli biex persuna taqrah.

Irridu kompatibbiltà ma' firxa wiesgħa ta' sistemi esterni li ma nistgħux nikkontrollaw, bħal sistemi ta' analitika, sistemi ta' databases, sistemi finanzjarji.


### Restrizzjonijiet

Xi sistemi għandhom limitazzjonijiet ta' preċiżjoni tal-ħin. Pereżempju, il-kmand Sat Oct 17 08:13:25 BST 2026 tas-sistema operattiva macOS jista' jistampa preċiżjoni tal-ħin f'sekondi, iżda mhux f'nanosekondi.


### Pożizzjonijiet

Ikkunsidrajna firxa ta' għażliet:

* Unix epoch jiġifieri numru wieħed li jiżdied.

* Format tat-test fil-qosor "YYYYMMDDTHHMMSSNNNNNNNNN".

* L-użu ta' żona tal-ħin lokali vs. iż-żona tal-ħin UTC.


### Argument

Għall-użu tipiku, napprezzaw li jkun faċli għall-bnedmin biex jaqraw/jiktbu, aktar mill-veloċità/id-daqs mhux ipproċessat.

Għall-użu tipiku, irridu format li jaħdem tajjeb f'sistemi tal-magni, u jaħdem tajjeb ukoll manwalment, bħal meta tikteb data ta' kampjun, taqra output JSON, tagħmel grep ta' fajl tal-log, eċċ.

Għal użu atipiku, bħal high performance computing, nistennew li se nixtiequ nottimizzaw kwalunkwe format tat-test li nagħżlu billi nikkonvertu t-test għal format aktar mgħaġġel, bħat-tip ta' oġġett tad-data integrat ta' lingwa tal-programmazzjoni. Għalhekk il-format tat-test ma jimpurtax wisq għall-HPC.


### Implikazzjonijiet

Is-sistemi differenti tagħna tat-test u tal-ħin se jikkonverġu fuq dan il-format.


## Relatati


### Deċiżjonijiet relatati

Jista' jkun li rridu mod mgħaġġel/faċli biex nittraċċaw ukoll id-delta tal-ħin magħrufa wkoll bħala durati. Dawn huma faċli b'timestamps Unix epoch.


### Rekwiżiti relatati

Jista' jkun li rridu naġġustaw id-deċiżjoni tagħna eż. jekk ikollna rekwiżit relatat għal tip speċifiku ta' timbru tal-messaġġ tal-logging, bħal għal Splunk, Sumo, ELK, eċċ.


### Artefatti relatati

Formatters u parsers tal-lingwi:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Eżempji ta' Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Eżempji ta' SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Prinċipji relatati

Faċilment riversibbli. Nistgħu nbiddlu pjuttost faċilment għal format differenti, bħal Unix epoch.

Iddefferixxi l-ottimizzazzjoni prematura. Għall-użu tipiku ma jimpurtax ħafna minn ftit karattri żejda bħal format li juża trattini u żewġ punti.


## Noti

Żid noti hawn.
