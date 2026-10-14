# Zapis arhitekturne odluke: CSS okvir

Sadržaj:

- [Sažetak](#sažetak)
  - [Problem](#problem)
  - [Odluka](#odluka)
  - [Status](#status)
- [Pojedinosti](#pojedinosti)
  - [Pretpostavke](#pretpostavke)
  - [Ograničenja](#ograničenja)
  - [Pozicije](#pozicije)
  - [Argument](#argument)
  - [Implikacije](#implikacije)
- [Povezano](#povezano)
  - [Povezane odluke](#povezane-odluke)
  - [Povezani zahtjevi](#povezani-zahtjevi)
  - [Povezani artefakti](#povezani-artefakti)
  - [Povezana načela](#povezana-načela)
- [Bilješke](#bilješke)


## Sažetak


### Problem

Želimo koristiti CSS okvir za izradu naših web aplikacija:

  * Želimo da korisničko iskustvo bude brzo i pouzdano u svim popularnim preglednicima i veličinama zaslona.

  * Želimo brzu iteraciju dizajna, rasporeda, UI/UX-a itd.

  * Želimo responzivne aplikacije, osobito za manje zaslone poput mobilnih uređaja, veće zaslone poput 4K širokih zaslona i dinamične zaslone poput okretnih zaslona.  


### Odluka

Odlučili smo se za Bulmu.


### Status

Odlučili smo se za Bulmu. Otvoreni smo za nove izbore CSS okvira kad se pojave.


## Pojedinosti


### Pretpostavke

Želimo stvarati web aplikacije koje su moderne, brze, pouzdane, responzivne itd.

Tipične moderne web aplikacije smanjuju/uklanjaju upotrebu jQueryja iz više razloga: 

  * Moderni JavaScript postupno uvodi mnoge mogućnosti koje je pružao jQuery, pa je jQuery manje potreban, a postoje bolji/brži/manji moduli koji pružaju specifične implementacije

  * jQueryjev širok pristup je izravna manipulacija DOM-om, što je antiobrazac za moderne JavaScript okvire (npr. React, Vue, Svelte)

  * jQuery smeta sam sebi ako se učita dvaput itd.


### Ograničenja

Ako odaberemo CSS okvir koji koristi jQuery, moramo uvoziti jQuery. Na primjer, Semantic UI koristi jQuery, a Tachyons ne.

Ako odaberemo CSS okvir koji je minimalan, odričemo se komponenti okvira koje možda želimo sada ili uskoro. Na primjer, Semantic UI pruža vrtuljak slika, a Tachyons ne.


### Pozicije

Razmatrali smo korištenje bez okvira. To se i dalje čini izvedivim, osobito jer CSS grid pruža velik dio onoga što trebamo za naš projekt..

Razmatrali smo mnoge CSS okvire brzim odabirom u uži izbor: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons itd. Naša dva izbora za dublji pregled su Semantic UI (jer ima najsemantičniji pristup) i Bulma (jer ima najlakši pristup koji pruža komponente koje sada želimo).

Razmatrali smo Semantic UI. On pruža mnoge komponente, uključujući one koje želimo za naš projekt: kartice, mreže, gumbe itd. Napravili smo pilot sa Semantic UI na dva načina: pomoću tipičnih CDN datoteka i pomoću NPM repozitorija. Postigli smo uspjeh sa Semantic UI u statičnoj HTML stranici, ali nismo postigli uspjeh u okviru svojeg vremenskog okvira za izgradnju JavaScript SPA-a (prvenstveno zbog problema s učitavanjem jQueryja). Otkrili smo da drugi programeri traže od razvijatelja Semantic UI-ja da stvore verziju bez jQueryja, iz istih razloga kao i mi. Drugi programeri traže verziju bez jQueryja već godinama, no razvijatelji su odbili i izjavili da bi svaka verzija bez jQueryja bila preteška za pisanje, npr. ~„projekt Semantic UI ima više od 22 000 dodirnih točaka koje koriste jQuery“.

Primjer sa Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Razmatrali smo Bulmu. Bulma ima mnoge slične mogućnosti kao Semantic UI, iako ne toliko sofisticiranih komponenti. Bulma je izgrađena modernim tehnikama, primjerice bez jQueryja. Bulma ima neke komponente trećih strana, od kojih bismo neke možda željeli koristiti.


Primjer s Bulmom:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Kao gore.

Konkretno, Semantic UI ima oznaku opreza kako u pogledu tehnologije (tj. toliko dodirnih točaka s jQueryjem) tako i u pogledu vodstva (tj. verzija bez jQueryja bila je odlučno ne, umjesto pokušaja izrade plana razvoja, kontinuiranog poboljšanja, prikupljanja donacija itd.).


### Implikacije

Ako pronađemo dobar CSS okvir bez jQueryja, to je općenito korisno i dobro.


## Povezano


### Povezane odluke

CSS okvir koji odaberemo može utjecati na mogućnost testiranja.


### Povezani zahtjevi

Želimo brzo isporučiti isključivo modernu aplikaciju. 

Ne želimo trošiti vrijeme na rad sa starijim okvirima (osobito Semantic UI) koji koriste starije ovisnosti (osobito jQuery).


### Povezani artefakti

Utječe na sav tipični HTML koji će koristiti CSS.


### Povezana načela

Lako reverzibilno.

Potreba za brzinom.


## Bilješke

Sve bilješke ovdje.
