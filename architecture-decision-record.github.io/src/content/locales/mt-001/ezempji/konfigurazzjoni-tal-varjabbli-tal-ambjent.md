# Konfigurazzjoni tal-varjabbli tal-ambjent

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
  * [Implikazzjonijiet ](#implikazzjonijiet)
* [Relatati](#relatati)
  * [Deċiżjonijiet relatati](#deċiżjonijiet-relatati)
  * [Rekwiżiti relatati](#rekwiżiti-relatati)
  * [Artefatti relatati](#artefatti-relatati)
  * [Prinċipji relatati](#prinċipji-relatati)
* [Noti](#noti)


## Sommarju


### Kwistjoni

Irridu li l-applikazzjonijiet tagħna jkunu konfigurabbli lil hinn mill-artefatti/binaries/sors, b'tali mod li bini wieħed jista' jaġixxi b'mod differenti skont l-ambjent tad-deployment tiegħu.

  * Biex nilħqu dan, irridu nużaw konfigurazzjoni bil-varjabbli tal-ambjent.

  * Irridu nimmaniġġjaw il-konfigurazzjoni bl-użu ta' fajls li nistgħu nikkontrollaw il-verżjonijiet tagħhom.

  * Irridu nipprovdu xi ergonomija tal-esperjenza tal-iżviluppatur, bħal li wieħed ikun jaf x'jista' jiġi kkonfigurat u liema huma d-defaults rilevanti.


### Deċiżjoni

Iddeċidejna fuq fajls .env b'fajl default relatat u fajl tal-iskema.


### Stat

Deċiż. Miftuħin biex nikkunsidraw kapaċitajiet ġodda hekk kif jinqalgħu.


## Dettalji


### Suppożizzjonijiet

Nippreferu nifirdu l-kodiċi tal-applikazzjoni mill-kodiċi tal-ambjent. Nassumu li l-app teħtieġ taħdem b'mod differenti f'ambjenti differenti, bħal ambjent tal-iżvilupp, ambjent tat-test, ambjent tad-demo, ambjent tal-produzzjoni, eċċ.

Nippreferu l-prattika tal-industrija ta' "12 factor app" u saħansitra aktar il-prattika relatata ta' "15 factor app".

Ħafna mill-proġetti preċedenti tagħna użaw il-konvenzjoni ta' fajl `.env` jew direttorju simili `.env`. Hemm prattika tipika li dawn jinżammu barra mill-kontroll tal-verżjonijiet, u minflok jintuża mod ieħor biex jitqiegħdu, jiġu vverżjonati, u jiġu mmaniġġjati.


### Restrizzjonijiet

Irridu nżommu s-sigrieti barra mis-sistema tal-kontroll tal-verżjonijiet (VCS) tal-ġestjoni tal-kodiċi sors (SCM) tagħna.

Irridu nimmiraw għall-kompatibbiltà ma' frameworks u librerijiet popolari tas-software. Pereżempju, Node għandu modulu "dotenv" biex jaqra l-konfigurazzjoni bil-varjabbli tal-ambjent.


### Pożizzjonijiet

Ikkunsidrajna ftit approċċi:

  * Naħżnu l-konfigurazzjoni fl-app bħal f'fajl `config.js`.

  * Naħżnu l-konfigurazzjoni fl-ambjent bħal f'fajl `.env`.

  * Nirkupraw il-konfigurazzjoni minn post magħruf bħal server tal-liċenzji.


### Argument

Għażilna l-approċċ ta' fajl .env għax:

  * Huwa popolari inkluż fost l-esperti.

  * Isegwi x-xejra ta' fajls `.env` li t-timijiet tagħna użaw b'suċċess ħafna drabi f'ħafna proġetti.

  * Huwa sempliċi. Notevolment, aħna tajbin għalissa mal-kompromessi sinifikanti li naraw, bħal nuqqas ta' kapaċitajiet ta' awditjar meta mqabbel ma' approċċ ta' server tal-liċenzji.


### Implikazzjonijiet 

Neħtieġu nsibu mod kif nifirdu l-konfigurazzjoni pubblika tal-varjabbli tal-ambjent mill-ġestjoni tas-sigrieti kollha.


## Relatati


### Deċiżjonijiet relatati

Nistennew li l-applikazzjonijiet tagħna kollha jużaw dan l-approċċ.

Se nippjanaw li naġġornaw kwalunkwe waħda mill-applikazzjonijiet tagħna li tuża approċċ inqas kapaċi, bħal hardcoding f'binary jew fil-kodiċi sors.

Se nħallu kif inhi kwalunkwe waħda mill-applikazzjonijiet tagħna li tuża approċċ aktar kapaċi, bħal server tal-liċenzjar.


### Rekwiżiti relatati

Se nżidu kapaċitajiet devops għall-fajls, inklużi hooks, testijiet, u integrazzjoni kontinwa.

Neħtieġu nħarrġu lill-membri kollha tat-tim tal-iżvilupp dwar din id-deċiżjoni.



### Artefatti relatati

Kull qasam fejn nagħmlu deployment se jeħtieġ il-fajl .env tiegħu stess u fajls relatati.


### Prinċipji relatati

Faċilment riversibbli.


## Noti


Fajl `.env` bħala eżempju:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Fajl `.env.defaults` bħala eżempju:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Fajl `.env.schema` bħala eżempju bil-keys biss:

```env
NAME
EMAIL
```
