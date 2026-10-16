# Monorepo vai multirepo

Saturs:

* [Kopsavilkums](#kopsavilkums)
  * [Jautājums](#jautājums)
  * [Lēmums](#lēmums)
  * [Statuss](#statuss)
* [Detaļas](#detaļas)
  * [Pieņēmumi](#pieņēmumi)
  * [Ierobežojumi](#ierobežojumi)
  * [Pozīcijas](#pozīcijas)
  * [Arguments](#arguments)
  * [Sekas](#sekas)
* [Saistītais](#saistītais)
  * [Saistītie lēmumi](#saistītie-lēmumi)
  * [Saistītās prasības](#saistītās-prasības)
  * [Saistītie artefakti](#saistītie-artefakti)
  * [Saistītie principi](#saistītie-principi)
* [Piezīmes](#piezīmes)


## Kopsavilkums


### Jautājums

Mūsu projekts ietver trīs galveno programmatūras kategoriju izstrādi:

  * Priekšpuses GUI
  * Starpprogrammatūras (middleware) pakalpojumi
  * Aizmugures serveri

Izstrādes laikā mūsu pirmkoda pārvaldības (SCM) versiju kontroles sistēma (VCS) ir git.

Mums jāizvēlas, kā mēs izmantojam git sava koda organizēšanai.

Augstākā līmeņa izvēle ir organizēt kā „monorepo” vai „polyrepo” vai „hibrīdu”:

  * Monorepo nozīmē, ka mēs visas daļas ievietojam vienā lielā repozitorijā
  * Polyrepo nozīmē, ka mēs katru daļu ievietojam savā repozitorijā
  * Hibrīds nozīmē kādu monorepo un polyrepo sajaukumu

Plašāku informāciju skatiet https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Lēmums

Monorepo, kad organizācija/komanda/projekts ir samērā mazs un ātra iterācija ir augstāka prioritāte nekā stabilitātes uzturēšana.

Polyrepo, kad organizācija/komanda/projekts ir samērā liels un stabilitātes uzturēšana ir augstāka prioritāte nekā ātra iterācija.


### Statuss

Izlemts. Atvērti pārskatīšanai, ja un kad parādīsies jauni rīki monorepo un/vai polyrepo pārvaldībai.


## Detaļas


### Pieņēmumi

Viss kods, ko mēs izstrādājam, ir vienas organizācijas piedāvājumiem, nevis plašai sabiedrībai. T. i., brokeris-dīleris nemērķē uz kaut ko līdzīgu plašas sabiedrības brīvprātīgajiem izstrādātājiem.


### Ierobežojumi

Ierobežojumi ir labi dokumentēti vietnē https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Pozīcijas

Mēs apsvērām monorepo Google, Facebook utt. stilā. Mēs domājam, ka jebkuras monorepo mērogošanas problēmas ir tik tālā nākotnē, ka līdz brīdim, kad tās mums būs vajadzīgas, mēs varēsim izmantot tās pašas prakses kā Google un Facebook.

Mēs apsvērām polyrepo tipisko Git atvērtā pirmkoda projektu stilā, piemēram, Google Android, Facebook React utt. Mēs domājam, ka tās ir labākā izvēle plašas sabiedrības līdzdalībai (piem., ikviens pasaulē var strādāt pie koda) un individuālai pieejamībai (piem., projektu izmanto atsevišķi, bez citām daļām).


### Arguments

Kad organizācija/komanda/projekts ir samērā mazs, mēs izvēlamies monorepo, jo ātra iterācija ir ievērojami augstāka prioritāte nekā stabilitātes uzturēšana

Kad organizācija/komanda/projekts ir samērā liels, mēs izvēlamies polyrepo, jo stabilitātes uzturēšana ir ievērojami augstāka prioritāte nekā ātra iterācija.


### Sekas

Ja jau pastāv CI+CD cauruļvads, mums, iespējams, tas būs jāpielāgo vairāku projektu testēšanai vienā repozitorijā.

CI+CD monorepo pilnai būvēšanai var prasīt vairāk laika, jo CI+CD var būvēt visus monorepo projektus.

Ja organizācija/komanda/projekts aug, monorepo būs mērogošanas problēmas.

Monorepo mērogošanas problēmas var padarīt arvien vērtīgāku pāreju uz polyrepo.

Pāreja no monorepo uz polyrepo ir nozīmīgs DevOps uzdevums, un tas būs jāplāno, jāpārvalda un jāprogrammē.


## Saistītais


### Saistītie lēmumi

Mēs izveidosim lēmumus par saistītajiem rīkiem monorepo (piem., Google Bazel) un polyrepo (piem., Lyft Refactorator) pārvaldībai.


### Saistītās prasības

Mums jāizstrādā CI+CD cauruļvads, lai tas labi darbotos ar git.


### Saistītie artefakti

Mēs sagaidām, ka repozitoriju organizācijai būs saistīti artefakti nodrošināšanai, konfigurācijas pārvaldībai, testēšanai un līdzīgām DevOps jomām. 


### Saistītie principi

Viegli atgriezenisks. Ja monorepo praksē nedarbojas vai vadība to nevēlas, ir vienkārši pāriet uz polyrepo.

Klientu apsēstība. Mēs vērtējam projekta nonākšanu klientu rokās, un mēs uzskatām, ka monorepo mūs tur var nogādāt ātrāk nekā polyrepo, kā arī palīdzēt mums ātrāk iterēt.

Domā lielā mērogā. Google un Facebook ir ļoti spēcīgi monorepo aizstāvji pret polyrepo, jo visus pamatpiedāvājumus var izstrādāt/testēt/izvietot saskaņoti.


## Piezīmes

Šeit pievienojiet jebkādas piezīmes.
