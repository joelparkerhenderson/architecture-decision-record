# Saladuste salvestamine

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Kokkuvõte


### Küsimus

Peame salvestama saladusi, nagu paroolid, privaatvõtmed, autentimistokenid jne.

Mõned saladused on kasutajale suunatud. Näiteks tahab meie arendaja saada kasutada oma mobiiltelefoni teenuse parooli otsimiseks.

Mõned saladused on süsteemile suunatud. Näiteks vajab meie pidevtarne torujuhe võimalust otsida üles meie pilvehostimise sisselogimisandmed.


### Otsus

Bitwarden kasutajale suunatud saladuste jaoks.

Vault by HashiCorp süsteemile suunatud saladuste jaoks.


### Olek

Otsustatud. Oleme avatud uutele valikutele, kui need ilmnevad.


## Üksikasjad


### Eeldused

Selle eesmärgi ja meie praeguse olukorra jaoks hindame kasutajale suunatud mugavust, nagu kasulikud mobiilirakendused.

  * Tahame tagada kiire, lihtsa juurdepääsu liikvel olles, näiteks töökindlusinseneeria valveülesandeid täitva arendaja jaoks.

  * Tahame suuta jagada mõnda saladust valitud inimeste, näiteks meeskonna vahel.

Me ei püüa lahendada ühe tarnija jaoks, näiteks salvestada kõik saladused eranditult Amazonis või Azure'is või Google'is.

Me ei taha ad hoc lähenemisi nagu "jäta meelde" või "kirjuta paberile" või "mõtle ise välja, kuidas seda salvestada".

Meie turvamudel selle eesmärgi jaoks on rahul hea mainega COTS-tarnijate kasutamisega, näiteks SaaS-i paroolihalduse tööriistadega.


### Piirangud

Praegu tahame midagi lihtsat, st pole vaja koodi kirjutada, pole vaja servereid paigaldada, pole vaja suurt kohustust võtta, pole vaja kõiki standardiseerida.


### Seisukohad

Kaalusime:

1. Kasutajale suunatud kasutusvalmis paroolihaldureid: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG jne.

2. Süsteemile suunatud COTS paroolihaldureid: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Jagamisele suunatud lähenemisi: jagatud Google'i dokumendi, jagatud Slacki kanali, jagatud võrgukausta jne kasutamine.

4. Madala tehnoloogiaga ad hoc lähenemisi, nagu meelde jätmine, paberile kirjutamine või lootmine, et iga kasutaja mõtleb ise välja, kuidas seda salvestada.


### Argument

Bitwarden, LastPass, 1Password ja Dashlane on kõik kommertslikud kasutusvalmis tooted.

  * Sarnased funktsioonid kasutajatele, meeskondadele, organisatsioonidele jne.

  * Töölaua võimalused Windowsile ja Macile ning mobiilivõimalused Androidile ja iOS-ile.

  * Brauserilaiendused Chrome'ile ja Firefoxile vormide automaatseks täitmiseks jne.

Bitwardenil on kaks eelist teiste ees:

  * Bitwarden on avatud lähtekoodiga, mis tähendab, et turvalisust saavad kolleegid üle vaadata ja ettevõtet austavad ka üldiselt turvateadlikud arendajad.

  * Tarkvarainimeste anekdoodid kirjeldavad märkimisväärset eelistust Bitwardeni vastu teiste ees.

Tüüpiline hea ülevaade: https://jcs.org/2017/11/17/bitwarden

Tüüpiline hääletussait kõrvuti võrdlusega: https://stackshare.io/stackups/bitwarden-vs-dashlane

Lükkame KeyPassi, passi, GPG jne edasi, sest on täiendav keerukus. Kõik tunduvad head lahendused tehnilistele kasutajatele. GPG tundub eriti hea tehnilistele kasutajatele, kes tahavad käsule suunatud võimalusi süsteemide lõikes.

Lükkame KMS-i edasi, sest sellel on seotus ühe tarnijaga.

Valime Vaulti süsteemile suunatud vajaduste jaoks, sest arvustused on üllatavalt positiivsed ja sest HashiCorpil on suurepärane ajalugu tippklassi tarkvara ja toe osas.

Vetostame jagamisega lähenemised, näiteks jagatud dokumentide, jagatud kanalite, jagatud võrgukaustade jne kaudu. Need ei paku turvakvaliteete, mida me tahame.

Vetostame madala tehnoloogiaga ad hoc lähenemised, sest oleme kõik nõus, et see ei ole pikaajaline tee edasi.


### Tagajärjed

Arendajad võivad vajada saladuste jälgimist kahes kohas: Bitwarden kasutajale suunatud juurdepääsuks ja Vault süsteemile suunatud juurdepääsuks.


## Seotud


### Seotud otsused

Otsus, millist CI/CD serverit valida, peab sisaldama tõendit saladustele juurdepääsu võime kohta.

Peame otsustama, kuidas saladusi hallata poliitikate, rotatsioonide, organisatsioonide jne osas.


### Seotud nõuded

Saladustel on seotud nõuded vastavuse, auditeerimise ja personali sisseelamise/väljaviimise kohta.


### Seotud artefaktid

Eeldame, et saame mõned saladused keskkonnamuutujatesse eksportida.


### Seotud põhimõtted

Hõlpsasti tagasipööratav.

Hõlpsasti paralleelselt käitatav, st on lihtne kasutada mitmesuguseid paroolihaldureid.

Odav proovida, st on tasuta prooviperiood ja kohustust pole.


## Märkmed

Hindamismärkmed siin. Märkmed on kõik avalikud kommentaarid erinevatel devopsi arutelufoorumitel.


### Vault by HashiCorp

Vault on täpselt see, mida siin tahad. 

Aga ära viska Vaulti lihtsalt tootmisse, sea see kõigepealt testkeskkonnas üles, sest HashiCorpi dokumentatsioon võib olla üsna puudulik, kuigi nende tooted on fantastilised.

Väga järsk õppimiskõver ja seda pole triviaalne seadistada. 

Esialgne seadistus on veidi tüütu. See on kindlasti seda väärt ja kogukond toetab seda piisavalt hästi, et sa läbi saad.

Kohutav dokumentatsioon, kuid on palju veebijuhendeid inimestelt, kes on selle üles seadnud, ja kui mõned neist kombineerid, on sul töötav seadistus.

Esialgne seadistus nõudis nende helm-diagrammide (vault ja consul) näppimist. Tehniliselt saad kasutada paljusid teisi taustasüsteeme, aga ma tõesti, tõesti ei soovita seda. Taustasüsteem/consul võib olla pisike, kui sul pole palju andmeid salvestada.

Tutvu kindlasti CLI kasutamisega, sest GUI on pigem kontseptsiooni tõestus/reklaamiportaal nende ettevõttevälja jaoks.

Asjaolu, et seda ei saa lihtsalt "täita", on tüütu. Näiteks kui sul on 5 välja, pead iga kirje jaoks käsitsi iga välja lisama. Seega ei ole nii, et määratled eelnevalt väljad konkreetse kategooria jaoks ja täidad need väljad kõigi selle kategooria kirjete jaoks, vaid pigem "genereerid kõik iga kord", mis on (minu arvates) tüütu.

Võid vaadata ka goldfishi kui UI-d vaulti peal. See teeb meeskonna kaasamise üsna mõnusaks. Neil on ka demo. 1. Sea üles consul. 2. Sea üles vault, mis osutab consulile. 3. Sea üles goldfish, mis osutab vaultile. 3. Sea üles mingi cron-töö, mis käitab consul snapshot'i varukoopiate jaoks.



### LastPass

LastPass Teams. Me kasutame seda, meil on kohandatud mallid, ACL-id ja minu arvates ei puudu midagi.

Teostasin LastPassi oma organisatsioonis ja annan sellele hinde C+/B-. Suurim probleem viimasel ajal on töökindluse puudumine. Viimase 90 päeva jooksul on olnud mitu tundi, mil hoidlad sunniti võrguühenduseta režiimi. See ei ole minu organisatsiooni jaoks ideaalne, sest meil on sõna otseses mõttes 4000+ parooli salvestatud 20+ jagatud kaustas. Nagu võid ette kujutada nii paljude paroolidega, uuendatakse või lisatakse iga päev vähemalt mõned. Meil on DR-plaan, kui probleemid kestavad üle tunni või kahe: skript allkirjastab ja krüpteerib igal ööl hoidla CSV-tõmmise, mida saab keepassi importida.

LastPassil on olnud teatamata hetki halvenenud teenusest: sisselogimine "töötab", kuid ei too ühtegi saiti, haldurpaneeli juhuslikud funktsioonid on katki ja võtmeid ei jagata õigesti uute kõrgeima taseme jagatud kaustade jaoks. Mul on eriline "key push"/varukoopia kasutaja, kes on igas rühmas. Tavaliselt lahendab selle kasutajana sisselogimine kõik võtmejagamise probleemid, kuid mitte siis, kui teenus on halvenenud, olenemata sellest, mida olekuleht ütleb...

Integratsiooni jaoks võib see olla lihtne, kui sul on korralikud ACL-id vähimate õiguste mudeliga, nt kui kasutajal on nii lugemis- ja kirjutamis- kui ka ainult lugemisõigus kirjele või kaustale, saab ta ainult lugemisõigused. Kahjuks pole minu organisatsiooni ACL-id parimad, nii et lõpuks kasutasin JSON-i varustamise API-d ja ~500 rida pythonit, sest sõltuvus meie sadades ACL-ides ei kaardistunud hästi vähimate õiguste mudelile. Lõpuks tõin kõik ACL-id, milles kasutaja oli, ja tegin omamoodi sõltuvuste läbikäimise.

Kui sinu ACL- või rühmastruktuur on juba ehitatud vähimate õiguste struktuuri silmas pidades, töötab Windowsi AD/LDAP sünkroonimistööriist hästi.

Võta ühendust nende müügimeeskonnaga, nad saavad korraldada pikema Enterprise'i prooviperioodi. Veendu, et mõistad selle piiranguid täielikult, enne kui päästikule vajutad. Meil oli üsna palju kasvuvalusid, kuid serveripoolsete katkestuste või halvenemiste kõrval on see olnud uskumatult sujuv.


### Bitwarden

Bitwardenil on head tööriistad ümber (WebUI, CLI, mobiil, töölaud). Saab ise hostida ja on üsna lihtne seadistada. Üsna hea dokumentatsioon ja tööriist, mida PrivacyTools soovitab.


### EnvKey

https://www.envkey.com/ on saas. Tõeliselt lihtne teostada, integreerida ja hallata.

Funktsioonid:

  * Kaitse API võtmeid ja sisselogimisandmeid.

  * Hoia seadistus kõikjal sünkroonis.

  * Nutikas, otsast-otsani krüpteeritud seadistuse ja saladuste haldus. 

  * Hoia ära ebaturvaline jagamine ja seadistuse laialivalgumine. 

  * Integreeri minutitega.

Võimalused:

  * Halda kõigi oma rakenduste, keskkondade ja meeskondade seadistust ja juurdepääsutasemeid ühes kohas.

  * Seadista mis tahes arendus- või serverikeskkond vaid ühe keskkonnamuutujaga.

Plussid:

  * Suurepärane sihtleht.

  * Selge väärtuspakkumine.

  * Visuaalselt suurepärane veebirakendus.

  * Ülim näidisandmed, nt Algolia, AWS, Datadog, GitHub, Stripe jne.

  * Rääkisin asutajaga 30 minutit ettevõtte, UI jne kohta. Dane kõlab hästi informeerituna, ausana plusside ja miinuste osas ning teostatava partnerina.

  * Ettevõte on sisuliselt tüüpiline Y Combinatori ettevõte ühe asutajaga. Kogus 2018-01 $120K.

  * Fookus on ettevõtte funktsioonideni jõudmisel, eriti EnvKey pilvehostimiselt kas kohapealsele või BYOC-le liikumisel.

  * Võimalik tee edasi: alusta EnvKeyga lihtsuse huvides ja lisa siis hiljem (või paralleelselt) Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant on avatud lähtekoodiga saladuste haldusteenus, mis pakub kasutajasõbralikku saladuste salvestamist ja neile juurdepääsu turvalisel viisil, Lyfti arendajatelt.

KMS-i autentimine: Confidant lahendab autentimise "kana ja muna" probleemi, kasutades AWS KMS-i ja IAM-i, et lasta IAM-i rollidel genereerida turvalisi autentimistokeneid, mida Confidant saab kontrollida. Confidant haldab ka KMS-i grante teie IAM-i rollide jaoks, mis võimaldab IAM-i rollidel genereerida tokeneid, mida saab kasutada teenustevaheliseks autentimiseks või krüpteeritud sõnumite saatmiseks teenuste vahel.

Versioonitud saladuste puhkeoleku krüpteerimine: Confidant salvestab saladusi DynamoDB-sse ainult-lisamise viisil ja genereerib iga saladuse iga redaktsiooni jaoks unikaalse KMS-i andmevõtme, kasutades sümmeetrilist autenditud krüptograafiat Fernet.

Kasutajasõbralik veebiliides saladuste haldamiseks: Confidant pakub AngularJS veebiliidest, mis võimaldab lõppkasutajatel hõlpsasti hallata saladusi, saladuste kaardistusi teenustele ja muudatuste ajalugu.


### Devolutions Password Server

https://server.devolutions.net/

Kaitse, halda ja jälgi juurdepääsu privilegeeritud kontodele ja seanssidele.

Põhjalik, väga turvaline paroolihoidla, mis võimaldab sul kontrollida juurdepääsu oma privilegeeritud kontodele, parandades samal ajal süsteemiadministraatorite üldist võrgunähtavust ja pakkudes lõppkasutajatele sujuvat kogemust.

Funktsioonid: tsentraliseeritud organisatsiooni paroolihoidla, kasutajaspetsiifiline privaatne hoidla, paroolihaldur, volituste süstimine,
Active Directory integratsioon, rollipõhine juurdepääsukontroll, kaheastmeline autentimine, ettevõtteks valmis, IP-piirangud, haldusvõimalused, automaatne paroolide generaator, juurdepääs mobiilirakenduse kaudu, paroolide ajalugu, juurdepääsuaruanded, e-posti hoiatused.

  * toetab andmete krüpteerimist

  * toetab mitut autentimisskeemi, sealhulgas LDAP, O365 ja kohalikud kasutajad MFA toega mitmest allikast

  * mitu hoidlat/kassat üksikasjalike juurdepääsukontrollidega mitmele meeskonnale

  * kaasaegne veebi-UI

  * privaatsed hoidlad volituste ja ühenduste jaoks isiklike volituste/ühenduste jaoks

  * mobiilirakendused iOS-ile/Androidile

  * auditilogid iga kirje jaoks, kes/mis/millal koos valikulise küsimusega, miks nad sellele ligi pääsevad

  * kohandatavad mallid (kuigi need toetavad natiivselt sadu ühendustüüpe)

  * hulgaliselt rohkem funktsioone ja paks klient Windowsile/Macile (Remote Desktop Manager), millega saad sünkroonida ja mis laiendab suuresti valikuid... ühe klõpsuga ühendused

  * hind pole paha - kuni 15 kasutajani maksab parooliserver $500 aastas


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Kohapealse versiooni funktsioonid: 

  * Täielik kontroll oma otsast-otsani turvasüsteemide ja taristu üle

  * Võta tarkvara kasutusele oma kohapealses andmekeskuses või oma virtuaalse privaatpilve eksemplaris

  * Täida juriidilised ja regulatiivsed kohustused, mis nõuavad, et kõik andmed ja süsteemid oleksid kohapeal

Pilveversiooni funktsioonid:

  * Tarkvara teenusena mudel lubab sul registreeruda ja kohe alustada

  * Elastne skaleeritavus kasvamisel

  * Azure'i pakutavad kontrollid ja koondamine 99,9% tööaja SLA-ga

Kasutajate tagasiside:

  * Kasutasime seda toodet varem. See oli nii lihtne mööda minna ja reeglid töötavad ainult targadele inimestele. Laisad või rumalad kasutajad saavad selle meeskonnaalas kergesti rikkuda. Hinnad on läbiräägitavad, kui nendega räägid.

  * Seda saab käitada SQL expressi ja Win 7 arvutiga. 

  * Odav.
