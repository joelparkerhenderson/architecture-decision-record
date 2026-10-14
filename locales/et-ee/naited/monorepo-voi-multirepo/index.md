# Monorepo või multirepo

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

Meie projekt hõlmab kolme põhikategooria tarkvara arendamist:

  * Kasutajaliidese GUI-d
  * Vahevaara teenused
  * Taustasüsteemi serverid

Arendamisel on meie lähtekoodihalduse (SCM) versioonihaldussüsteem (VCS) git.

Peame valima, kuidas kasutame gitti oma koodi korraldamiseks.

Kõrgeima taseme valik on korraldada "monorepona", "polyrepona" või "hübriidina":

  * Monorepo tähendab, et paneme kõik osad ühte suurde hoidlasse
  * Polyrepo tähendab, et paneme iga osa oma hoidlasse
  * Hübriid tähendab monorepo ja polyrepo segu

Lisateabe saamiseks vaata https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Otsus

Monorepo, kui organisatsioon/meeskond/projekt on suhteliselt väike ja kiire iteratsioon on kõrgema prioriteediga kui stabiilsuse säilitamine.

Polyrepo, kui organisatsioon/meeskond/projekt on suhteliselt suur ja stabiilsuse säilitamine on kõrgema prioriteediga kui kiire iteratsioon.


### Olek

Otsustatud. Oleme avatud uuesti läbivaatamisele, kui/kui monorepode ja/või polyrepode haldamiseks tekivad uued tööriistad.


## Üksikasjad


### Eeldused

Kogu kood, mida arendame, on ühe organisatsiooni pakkumiste jaoks, mitte laiale avalikkusele. St et maakler-diiler ei püüa omada midagi sellist nagu avalikkuse vabatahtlikud arendajad.


### Piirangud

Piirangud on hästi dokumenteeritud aadressil https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Seisukohad

Kaalusime monorepoisid Google'i, Facebooki jt stiilis. Arvame, et monorepode skaleerimisprobleemid on nii kaugel tulevikus, et suudame kasutada samu tavasid kui Google ja Facebook, kui neid vajame.

Kaalusime polyrepoisid tüüpiliste Giti avatud lähtekoodiga projektide stiilis, nagu Google Android, Facebook React jne. Arvame, et need on parim valik avalikkuse osalemiseks (nt igaüks maailmas saab koodiga töötada) ja individuaalseks kättesaadavuseks (nt projekti kasutatakse eraldi, ilma teiste osadeta).


### Argument

Kui organisatsioon/meeskond/projekt on suhteliselt väike, valime monorepo, sest kiire iteratsioon on märkimisväärselt kõrgema prioriteediga kui stabiilsuse säilitamine

Kui organisatsioon/meeskond/projekt on suhteliselt suur, valime polyrepo, sest stabiilsuse säilitamine on märkimisväärselt kõrgema prioriteediga kui kiire iteratsioon.


### Tagajärjed

Kui CI+CD torujuhe juba olemas on, peame seda võib-olla kohandama mitme projekti testimiseks ühes hoidlas.

CI+CD võib monorepo täisehituseks rohkem aega võtta, sest CI+CD võib ehitada kõik monorepos olevad projektid.

Kui organisatsioon/meeskond/projekt kasvab, tekivad monorepol skaleerimisprobleemid.

Monorepo skaleerimisprobleemid võivad muuta üleminekut polyrepole üha väärtuslikumaks.

Üleminek monorepolt polyrepole on märkimisväärne devopsi ülesanne ning seda tuleb planeerida, hallata ja programmeerida.


## Seotud


### Seotud otsused

Loome otsused seotud tööriistade kohta monorepode (nt Google Bazel) ja polyrepode (nt Lyft Refactorator) haldamiseks.


### Seotud nõuded

Peame arendama CI+CD torujuhtme nii, et see töötaks gitiga hästi.


### Seotud artefaktid

Eeldame, et hoidla korraldusel on seotud artefakte varustamiseks, seadistuste haldamiseks, testimiseks ja sarnastes devopsi valdkondades. 


### Seotud põhimõtted

Hõlpsasti tagasipööratav. Kui monorepo praktikas ei tööta või juhtkond seda ei soovi, on polyrepole üleminek lihtne.

Kliendikesksus. Hindame projekti kliendi kätte jõudmist ja usume, et monorepo võib meid sinna kiiremini viia kui polyrepo ning aidata ka kiiremini iteratsioone teha.

Mõtle suurelt. Google ja Facebook on monorepode väga tugevad pooldajad polyrepode ees, sest kõiki põhipakkumisi saab arendada/testida/kasutusele võtta koos.


## Märkmed

Lisa siia mis tahes märkmed.
