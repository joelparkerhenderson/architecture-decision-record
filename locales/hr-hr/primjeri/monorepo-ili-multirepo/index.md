# Monorepo ili multirepo

Sadržaj:

* [Sažetak](#sažetak)
  * [Problem](#problem)
  * [Odluka](#odluka)
  * [Status](#status)
* [Pojedinosti](#pojedinosti)
  * [Pretpostavke](#pretpostavke)
  * [Ograničenja](#ograničenja)
  * [Pozicije](#pozicije)
  * [Argument](#argument)
  * [Implikacije](#implikacije)
* [Povezano](#povezano)
  * [Povezane odluke](#povezane-odluke)
  * [Povezani zahtjevi](#povezani-zahtjevi)
  * [Povezani artefakti](#povezani-artefakti)
  * [Povezana načela](#povezana-načela)
* [Bilješke](#bilješke)


## Sažetak


### Problem

Naš projekt uključuje razvoj triju glavnih kategorija softvera:

  * Front-end GUI-jevi
  * Middleware usluge
  * Back-end poslužitelji

Kada razvijamo, naš sustav kontrole verzija (VCS) za upravljanje izvornim kodom (SCM) je git.

Moramo odabrati kako ćemo koristiti git za organizaciju našeg koda.

Najviša razina izbora je organizirati kao „monorepo“, „polyrepo“ ili „hybrid“:

  * Monorepo znači da sve dijelove stavljamo u jedan veliki repozitorij
  * Polyrepo znači da svaki dio stavljamo u vlastiti repozitorij
  * Hybrid znači neku kombinaciju monorepa i polyrepa

Za više pogledajte https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Odluka

Monorepo kada je organizacija/tim/projekt relativno malen, a brza iteracija ima viši prioritet od održavanja stabilnosti.

Polyrepo kada je organizacija/tim/projekt relativno velik, a održavanje stabilnosti ima viši prioritet od brze iteracije.


### Status

Odlučeno. Otvoreni smo za ponovno razmatranje ako/kada postanu dostupni novi alati za upravljanje monorepozitorijima i/ili polyrepozitorijima.


## Pojedinosti


### Pretpostavke

Sav kod koji razvijamo namijenjen je ponudama jedne organizacije, a ne široj javnosti. Tj. Broker-Dealer ne cilja imati ništa poput volonterskih programera iz šire javnosti.


### Ograničenja

Ograničenja su dobro dokumentirana na https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Pozicije

Razmatrali smo monorepoe u stilu Googlea, Facebooka itd. Mislimo da su svi problemi skaliranja monorepa toliko daleko u budućnosti da ćemo do trenutka kada nam zatrebaju moći iskoristiti iste prakse kao Google i Facebook.

Razmatrali smo polyrepoe u stilu tipičnih Git projekata otvorenog koda, kao što su Google Android, Facebook React itd. Mislimo da su oni najbolji izbor za sudjelovanje šire javnosti (npr. bilo tko na svijetu može raditi na kodu) i individualnu dostupnost (npr. projekt se koristi samostalno, bez ikakvih drugih dijelova).


### Argument

Kada je organizacija/tim/projekt relativno malen, biramo monorepo jer je brza iteracija znatno višeg prioriteta od održavanja stabilnosti

Kada je organizacija/tim/projekt relativno velik, biramo polyrepo jer je održavanje stabilnosti znatno višeg prioriteta od brze iteracije.


### Implikacije

Ako postoji postojeći cjevovod za CI+CD, možda ćemo ga morati prilagoditi za testiranje više projekata unutar jednog repozitorija.

CI+CD može trebati više vremena za potpunu izgradnju monorepa jer CI+CD može graditi sve projekte u monorepu.

Ako organizacija/tim/projekt raste, monorepo će imati probleme sa skaliranjem.

Problemi sa skaliranjem monorepa mogu prijelaz na polyrepo činiti sve vrednijim.

Prijelaz s monorepa na polyrepo značajan je devops zadatak i morat će se planirati, voditi i programirati.


## Povezano


### Povezane odluke

Stvorit ćemo odluke za povezane alate za upravljanje monorepoima (npr. Google Bazel) i polyrepoima (npr. Lyft Refactorator).


### Povezani zahtjevi

Moramo razviti CI+CD cjevovod da dobro radi s gitom.


### Povezani artefakti

Očekujemo da će organizacija repozitorija imati povezane artefakte za osiguravanje resursa (provisioning), upravljanje konfiguracijom, testiranje i slična devops područja. 


### Povezana načela

Lako reverzibilno. Ako monorepo ne radi u praksi ili ga vodstvo ne želi, jednostavno je prijeći na polyrepo.

Opsjednutost kupcem. Cijenimo dovođenje projekta u ruke kupaca i vjerujemo da nas monorepo tamo može dovesti brže od polyrepa te nam također pomoći da brže iteriramo.

Misli veliko. Google i Facebook vrlo su snažni zagovornici monorepoa nad polyrepoima jer se sve temeljne ponude mogu razvijati/testirati/implementirati zajednički.


## Bilješke

Ovdje dodajte bilješke.
