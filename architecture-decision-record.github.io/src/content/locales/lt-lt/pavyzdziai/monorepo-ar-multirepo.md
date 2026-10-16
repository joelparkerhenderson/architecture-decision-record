# Monorepo ar multirepo

Turinys:

* [Santrauka](#santrauka)
  * [Problema](#problema)
  * [Sprendimas](#sprendimas)
  * [Būsena](#būsena)
* [Detalės](#detalės)
  * [Prielaidos](#prielaidos)
  * [Apribojimai](#apribojimai)
  * [Pozicijos](#pozicijos)
  * [Argumentas](#argumentas)
  * [Implikacijos](#implikacijos)
* [Susiję](#susiję)
  * [Susiję sprendimai](#susiję-sprendimai)
  * [Susiję reikalavimai](#susiję-reikalavimai)
  * [Susiję artefaktai](#susiję-artefaktai)
  * [Susiję principai](#susiję-principai)
* [Pastabos](#pastabos)


## Santrauka


### Problema

Mūsų projektas apima trijų pagrindinių programinės įrangos kategorijų kūrimą:

  * Priekinės dalies grafinės sąsajos (GUI)
  * Tarpinės programinės įrangos paslaugos
  * Galinės dalies serveriai

Kurdami naudojame git kaip šaltinio kodo valdymo (SCM) versijų valdymo sistemą (VCS).

Turime pasirinkti, kaip naudosime git savo kodui organizuoti.

Aukščiausio lygio pasirinkimas yra organizuoti kaip „monorepo“, „polyrepo“ arba „hibridą“:

  * Monorepo reiškia, kad visas dalis dedame į vieną didelę saugyklą
  * Polyrepo reiškia, kad kiekvieną dalį dedame į jos pačios saugyklą
  * Hibridas reiškia monorepo ir polyrepo mišinį

Daugiau žr. https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Sprendimas

Monorepo, kai organizacija / komanda / projektas yra gana mažas, o greita iteracija yra svarbesnė už stabilumo išlaikymą.

Polyrepo, kai organizacija / komanda / projektas yra gana didelis, o stabilumo išlaikymas yra svarbesnis už greitą iteraciją.


### Būsena

Nuspręsta. Atviri pakartotiniam svarstymui, jei / kai atsiras naujų įrankių monorepo ir (arba) polyrepo valdymui.


## Detalės


### Prielaidos

Visas kodas, kurį kuriame, skirtas vienos organizacijos pasiūlymams, o ne plačiajai visuomenei. T. y. Brokerių-dilerių įmonė (Broker-Dealer) nesiekia turėti nieko panašaus į plačiosios visuomenės savanorius programuotojus.


### Apribojimai

Apribojimai gerai dokumentuoti adresu https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Pozicijos

Svarstėme monorepo Google, Facebook ir kt. stiliumi. Manome, kad bet kokios monorepo mastelio keitimo problemos yra taip toli ateityje, kad kai jų prireiks, galėsime pasinaudoti tomis pačiomis praktikomis kaip Google ir Facebook.

Svarstėme polyrepo tipinių Git atvirojo kodo projektų stiliumi, pavyzdžiui, Google Android, Facebook React ir kt. Manome, kad tai geriausias pasirinkimas plačiosios visuomenės dalyvavimui (pvz., kiekvienas pasaulyje gali dirbti su kodu) ir atskiram prieinamumui (pvz., projektas naudojamas atskirai, be jokių kitų dalių).


### Argumentas

Kai organizacija / komanda / projektas yra gana mažas, renkamės monorepo, nes greita iteracija yra žymiai svarbesnė už stabilumo išlaikymą

Kai organizacija / komanda / projektas yra gana didelis, renkamės polyrepo, nes stabilumo išlaikymas yra žymiai svarbesnis už greitą iteraciją.


### Implikacijos

Jei jau yra CI+CD konvejeris, gali tekti jį pritaikyti keleto projektų testavimui vienoje saugykloje.

CI+CD pilnam monorepo kūrimui gali užtrukti ilgiau, nes CI+CD gali kurti visus monorepo projektus.

Jei organizacija / komanda / projektas auga, monorepo turės mastelio keitimo problemų.

Dėl monorepo mastelio keitimo problemų pereiti prie polyrepo gali tapti vis vertingiau.

Perėjimas nuo monorepo prie polyrepo yra reikšminga devops užduotis, kurią reikės suplanuoti, valdyti ir užprogramuoti.


## Susiję


### Susiję sprendimai

Sukursime sprendimus dėl susijusių įrankių monorepo (pvz., Google Bazel) ir polyrepo (pvz., Lyft Refactorator) valdymui.


### Susiję reikalavimai

Turime sukurti CI+CD konvejerį, kad jis gerai veiktų su git.


### Susiję artefaktai

Tikimės, kad saugyklos organizavimas turės susijusių artefaktų aprūpinimui, konfigūracijos valdymui, testavimui ir panašioms devops sritims. 


### Susiję principai

Lengvai atšaukiama. Jei monorepo praktikoje neveikia arba vadovybė jo nenori, lengva pereiti prie polyrepo.

Klientų apsėstumas. Vertiname projekto pateikimą klientams ir manome, kad monorepo gali mus ten nuvesti greičiau nei polyrepo, taip pat padėti greičiau iteruoti.

Mąstyk plačiai. Google ir Facebook labai stipriai pasisako už monorepo, o ne polyrepo, nes visus pagrindinius pasiūlymus galima kurti / testuoti / diegti kartu.


## Pastabos

Čia pridėkite bet kokias pastabas.
