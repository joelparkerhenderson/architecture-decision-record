# Monorepo ali multirepo

Vsebina:

* [Povzetek](#povzetek)
  * [Vprašanje](#vprašanje)
  * [Odločitev](#odločitev)
  * [Stanje](#stanje)
* [Podrobnosti](#podrobnosti)
  * [Predpostavke](#predpostavke)
  * [Omejitve](#omejitve)
  * [Stališča](#stališča)
  * [Argument](#argument)
  * [Posledice](#posledice)
* [Povezano](#povezano)
  * [Povezane odločitve](#povezane-odločitve)
  * [Povezane zahteve](#povezane-zahteve)
  * [Povezani artefakti](#povezani-artefakti)
  * [Povezana načela](#povezana-načela)
* [Opombe](#opombe)


## Povzetek


### Vprašanje

Naš projekt vključuje razvoj treh glavnih kategorij programske opreme:

  * Grafični uporabniški vmesniki
  * Storitve vmesne programske opreme (middleware)
  * Zaledni strežniki

Pri razvoju je naš sistem za upravljanje izvorne kode (SCM) oziroma nadzor različic (VCS) git.

Odločiti se moramo, kako z gitom organiziramo svojo kodo.

Izbira na najvišji ravni je organizacija kot »monorepo«, »polyrepo« ali »hibrid«:

  * Monorepo pomeni, da vse dele damo v en velik repozitorij
  * Polyrepo pomeni, da vsak del damo v svoj repozitorij
  * Hibrid pomeni neko mešanico monorepa in polyrepa

Za več glejte https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Odločitev

Monorepo, kadar je organizacija/ekipa/projekt razmeroma majhen in je hitra iteracija večja prednostna naloga kot ohranjanje stabilnosti.

Polyrepo, kadar je organizacija/ekipa/projekt razmeroma velik in je ohranjanje stabilnosti večja prednostna naloga kot hitra iteracija.


### Stanje

Odločeno. Odprti smo za ponovno preučitev, če in ko bodo na voljo nova orodja za upravljanje monorepov in/ali polyrepov.


## Podrobnosti


### Predpostavke

Vsa koda, ki jo razvijamo, je za ponudbe ene organizacije in ne za splošno javnost. Tj. posrednik-trgovec (Broker-Dealer) ne namerava imeti nečesa takega, kot so prostovoljni razvijalci iz splošne javnosti.


### Omejitve

Omejitve so dobro dokumentirane na https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Stališča

Preučili smo monorepe v slogu Googla, Facebooka itd. Menimo, da so morebitne težave s skaliranjem monorepa tako daleč v prihodnosti, da bomo do časa, ko jih bomo potrebovali, lahko izkoristili enake prakse kot Google in Facebook.

Preučili smo polyrepe v slogu tipičnih odprtokodnih projektov Git, kot sta Google Android, Facebook React itd. Menimo, da so to najboljša izbira za sodelovanje splošne javnosti (npr. na kodi lahko dela kdor koli na svetu) in samostojno razpoložljivost (npr. projekt se uporablja samostojno, brez drugih delov).


### Argument

Kadar je organizacija/ekipa/projekt razmeroma majhen, izberemo monorepo, ker je hitra iteracija občutno višja prednostna naloga kot ohranjanje stabilnosti

Kadar je organizacija/ekipa/projekt razmeroma velik, izberemo polyrepo, ker je ohranjanje stabilnosti občutno višja prednostna naloga kot hitra iteracija.


### Posledice

Če že obstaja cevovod za CI+CD, ga bomo morda morali prilagoditi za testiranje več projektov znotraj enega repozitorija.

CI+CD lahko za monorepo potrebuje več časa za polno gradnjo, ker lahko CI+CD zgradi vse projekte v monorepu.

Če organizacija/ekipa/projekt raste, bo imel monorepo težave s skaliranjem.

Težave s skaliranjem monorepa lahko vedno bolj upravičujejo prehod na polyrepo.

Prehod z monorepa na polyrepo je pomembna naloga DevOps in jo bo treba načrtovati, upravljati in programirati.


## Povezano


### Povezane odločitve

Ustvarili bomo odločitve za sorodna orodja za upravljanje monorepov (npr. Google Bazel) in polyrepov (npr. Lyft Refactorator).


### Povezane zahteve

Cevovod CI+CD moramo razviti tako, da bo dobro deloval z gitom.


### Povezani artefakti

Pričakujemo, da bo organizacija repozitorijev imela sorodne artefakte za zagotavljanje virov, upravljanje konfiguracije, testiranje in podobna področja DevOps. 


### Povezana načela

Lahko povratljivo. Če monorepo v praksi ne deluje ali ga vodstvo ne želi, je prehod na polyrepo preprost.

Obsedenost s strankami. Cenimo, da projekt pride v roke strankam, in verjamemo, da nas lahko monorepo tja pripelje hitreje kot polyrepo ter nam tudi pomaga hitreje iterirati.

Razmišljajte veliko. Google in Facebook sta zelo močna zagovornika monorepov pred polyrepi, ker je mogoče vse temeljne ponudbe razvijati/testirati/uvajati usklajeno.


## Opombe

Tu dodajte vse opombe.
