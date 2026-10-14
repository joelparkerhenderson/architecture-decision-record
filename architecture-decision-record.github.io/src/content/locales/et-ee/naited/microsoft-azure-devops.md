# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: rahuldamatu seiklus](#microsoft-devops-ci-rahuldamatu-seiklus)
  * [Hacker Newsi arutelu esiletõstud](#hacker-newsi-arutelu-esiletõstud)
  * [Windows Development MVP](#windows-development-mvp)
  * [Edward Thomsoni (Azure PM) kokkuvõte](#edward-thomsoni-azure-pm-kokkuvõte)


## Kokkuvõte


### Küsimus

Tahame kasutada devopsi oma projektide ehitamiseks, integreerimiseks, kasutuselevõtuks ja hostimiseks. Kaalume Microsoft Azure DevOpsi.

  * Tahame, et arendajakogemus oleks kiire ja töökindel, nii devopsi seadistamisel, nt konfigureerimisel, kui ka jätkuval kasutamisel, nt kiired ehitusajad.
  
  * Tahame kaaluda Microsoft Azure'i kasutamist tervikuna projekti rakenduste, andmebaaside jms hostimiseks.


### Otsus

Otsustatud Microsoft Azure DevOpsi vastu.


### Olek

Otsustatud. Oleme avatud uuesti läbivaatamisele, kui/kui saabub uut olulist teavet.


## Üksikasjad


### Eeldused

Kõik tavalised devopsi eeldused, nagu raamatus Accelerate.

  * Kiired ehitused on märkimisväärne abi. See kiirendab tagasisideringe.

  * Saame vahetada osi alternatiivsete tarnijate vastu sisse/välja, st võime tahta tuua oma kiiremaid ehitusservereid, kasutada oma valitud versioonihaldussüsteemi või koordineerida isehostitava pideva integratsiooni serveriga.
  
  * Sujuv kasutatavus on märkimisväärne abi arendajakogemusele ja omakorda peenetele valdkondadele nagu järjepidevus, selgus, turvalisus ja õppimiskõvera lihtsus.

  * Kui midagi on katki või problemaatiline, tahame tõhusat viisi probleemist teatamiseks. See on eriti oluline turvaga seotud probleemide puhul.


### Piirangud

Teadaolevaid pole. Azure'il on avaldatud kohustus hästi väliste tööriistadega koos töötada.


### Seisukohad

Kaalusime Microsoft Azure Devopsi kasutamist versus AWS, mis on praegune tarnija.

Katsetasime Azure DevOpsi, Azure Pipelines'i, Azure Repo ja uue serveri käivitamist Azure'is Terraformi kaudu.

Katsetasime toe saamist Microsofti esindajatelt.

Kogusime teavet kolleegidelt blogides ja Hacker Newsis.


### Argument

Azure DevOps reklaamib suurepärast pakkumiste komplekti, kuid need ei pea vastu, ei tööta hästi koos ja tugi on kehv.

Meie otsene kogemus:

  * Azure'i seadistus on UI-de segadus, millest mõned kattuvad Microsofti kontodega ja mõned mitte. Näiteks on Azure'i sisselogimine, Microsoft.com sisselogimine, Live.com sisselogimine jne ja kõik on korraga mängus.

  * Puutusime seadistuse ajal kokku väikese turvaprobleemiga ega leidnud lahendust. Püüdsime sellest paljudel viisidel paljudele Microsofti esindajatele teatada, edutult. Teatasime sellest edukalt Microsofti turvalisusele, kes vastas, et seda ei paranda (won't fix).

  * Dokumentatsioon on sageli kas vale või vananenud. Vähemalt osa sellest on tingitud Microsofti kehvast otsingumootorist ja osa keskpärasest SEO-st.
  
  * Terraformi seadistus on hästi dokumenteeritud ja töötab. Terraformi tugi on aga AWS-iga võrreldes nõrk, sest Microsoft rajab äriseoseid tarnijatega, et teha läbiva Terraformi seadistuse näiteid.

Meie kolleegide kogemused:

  * Pärast oma pimehindamist otsisime kolleegide kogemusi. See, mida leidsime, kinnitas meie kogemusi.

  * Kolleegid teatasid lisaprobleemidest ehitusaegadega ja probleemidest oma ehitusserveri toomisega. Need probleemid on märkimisväärselt tõsisemad kui UI probleemid, sest ehituste tegemine on ehitustorujuhtme põhieesmärk ja eeldame, et teeme neid päevas palju.

  * Leidsime suurepärase Azure'i meeskonnaliikmete osaluse aruteluvaldkondades. Kiitus Microsoftile selle eest. Oleme eriti muljet avaldanud Edward Thomsonist, Azure PM-ist ja programmeerijast, tema osaluse, otsekohesuse ja tehniliste selgituste tõttu.


### Tagajärjed

Microsoft Azure DevOpsi valimine näib olevat tõenäoliselt kallim (~3x) ajas ja kulus kui Azure'i mitte valimine.


## Seotud


### Seotud otsused

Kui valime Azure DevOpsi, on palju seotud pakkumisi, sealhulgas Azure Repo, Azure Pipeline jne. Usume, et kui valime Azure Devopsi, võib see muuta rohkemate Azure'i võimaluste kasutamise lihtsamaks või teiste tarnijate võimaluste kasutamise raskemaks.

Usume, et Microsoft astub arendajakogemuses suuri samme ning näeme, kuidas Microsoft teeb suuri arendajatööriistade (nt GitHub) ja sõltuvuste (nt Citus) ülevõtmisi.

Kui valime Azure DevOpsi, võime tahta rõhutada Microsofti ülevõetud pakkumiste valimist ning võime tahta ka läheneda ülevõetud pakkumistele suurema hoolega/hindamisega võimaliku koe tagasilükkamise tõttu, nt töötajate voolavuse risk.


### Seotud nõuded

Tahame, et ehitusajad oleksid väga kiired. Aktsepteerime selle eest kõrget lisatasu. See on sellepärast, et tahame väga kiiresti iteratsioone teha.

Tahame, et töökindlus oleks väga kõrge. Aktsepteerime selle eest kõrget lisatasu. See on sellepärast, et testime kõrge väärtusega kasutusjuhte, sealhulgas finantstehinguid, konfidentsiaalseid tehinguid jne.

Meie top 4 devopsi KPI-d sisaldavad keskmist taastumisaega, mis nõuab kiireid ehitusi ja kõrget töökindlust.


### Seotud artefaktid

Tahame, et ehitussüsteem väljastaks artefakte, mis sobivad kasutamiseks teistes süsteemides, nagu Artifactory.


### Seotud põhimõtted

Hõlpsasti tagasipööratav. Saame Azure DevOpsi hinnata paralleelselt praeguse tarnija AWS-iga.


## Märkmed


### Microsoft Devops CI: rahuldamatu seiklus

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Blogipostitus.

"Tarkvaraarendajana tean omast käest, kui raske on kvaliteetseid tooteid kiiresti ja odavalt ehitada. See on kunstivorm, mille me mõnikord õigesti saame ja mõnikord laguneb see millekski, mis sarnaneb Obama-ajastu valitsuse tervishoiu veebisaidiga. Meie kontrolli tase tekkiva toote üle varieerub ja ebaõnnestumise süü langeb sageli otsustushierarhia valedele inimestele. Microsofti Azure DevOps (varem tuntud kui Visual Studio Team Services) on vaatamata selgelt headele kavatsustele halbade otsuste ja kehva teostuse täiuslik torm."


### Hacker Newsi arutelu esiletõstud

https://news.ycombinator.com/item?id=18983586

"Kasutame oma töökohas Azure DevOpsi ulatuslikult ja pärast GitHubi, Gitlabi, isehostitavate lahenduste, Jenkinsi, TeamCity kasutamist... on Azure DevOps päris viimane."

"UI on kõikjal kohutavalt kohmakas. Kõige hullem on minu jaoks pull requestid. Uskumatult raske inimestega pull requesti kallal töötada. Ma ei saa isegi ühele "konkreetsele" probleemile osutada - meie jaoks on see kõikjal katki."

"Azure Devops on miski, mida ma tahaksin armastada. UI muutub pidevalt, kuid ei paranda aluseks olevaid vigu, mis on olnud ammu."

"Tööriistad ei ole hästi integreeritud, UI on tõesti aeglane, puudub armatuurlaua vaade aktiivsetele pull requestidele, ehitustele, väljalasetele jne minu lemmikhoidlate jaoks. Ehitus-/kasutuselevõtuajad on hullumeelselt aeglased."

"Proovisime kasutada ka Azure Boardsi (tööelemendid, tahvlid, tagavarad jne). Au. See on täielik UI segadus lahtiühendatud ideedest. Ühe asja hästi teostamise asemel teostasid nad kaks tosinat asja kohutavalt."


### Windows Development MVP

Windows Development MVP siin. Tunnen, et pean kandma osa vastutusest, et ma pole nendest probleemidest valjemalt rääkinud. Aga pean ütlema, et olen pettunud, kuuldes, et olete UX-i probleemidest "üllatunud". Olen teie inimestele öelnud, et UX on kohutav (nt juba enne turuletulekut) ja kuulsin pidevalt "me teame, parandame". Hakkan tagasisidet vormistama ja torude kaudu edasi suunama, püsige lainel. Olen ka kohalik (Bellevue) ja tuleksin hea meelega kohale ja proovin oma suhteliselt lihtsa avatud lähtekoodiga .net/wpf/uwp rakenduse torujuhtmesse panna. Kahtlustan, et see on mõlemale meist silmiavaja.

Mõned näited:

* Torujuhet ei saa ehitada git-hoidlaga, mis sisaldab alammooduleid

* Leidsin, et on võimatu muuta PATH-i mõne kohandatud tööriistastiku jaoks

* Uus torujuhtme kogemus lihtsalt ei ole eriti mõistlik; uued kasutajad, kes ringi klõpsavad, jõuavad lõpuks vale dokumentatsioonini.


### Edward Thomsoni (Azure PM) kokkuvõte

Kirjutasin koodi, mis liidab sinu pull requestid. Programmijuht Microsoftis Azure DevOpsi jaoks; varem tarkvarainsener versioonihaldustööriistade kallal GitHubis, Microsoftis, SourceGearis.

https://www.edwardthomson.com/

libgit2 kaashooldaja. https://libgit2.github.io

All Things Git'i, Giti-teemalise podcasti kaasjuht. https://www.allthingsgit.com/

Developer Tools Weekly kuraator, arendustööriistade uudiskiri. https://developertoolsweekly.com/
