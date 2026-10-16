# Zapis arhitekturne odločitve: ogrodje CSS

Vsebina:

- [Povzetek](#povzetek)
  - [Vprašanje](#vprašanje)
  - [Odločitev](#odločitev)
  - [Stanje](#stanje)
- [Podrobnosti](#podrobnosti)
  - [Predpostavke](#predpostavke)
  - [Omejitve](#omejitve)
  - [Stališča](#stališča)
  - [Argument](#argument)
  - [Posledice](#posledice)
- [Povezano](#povezano)
  - [Povezane odločitve](#povezane-odločitve)
  - [Povezane zahteve](#povezane-zahteve)
  - [Povezani artefakti](#povezani-artefakti)
  - [Povezana načela](#povezana-načela)
- [Opombe](#opombe)


## Povzetek


### Vprašanje

Za ustvarjanje naših spletnih aplikacij želimo uporabiti ogrodje CSS:

  * Želimo, da je uporabniška izkušnja hitra in zanesljiva v vseh priljubljenih brskalnikih in velikostih zaslonov.

  * Želimo hitro iteracijo oblikovanja, postavitve, UI/UX itd.

  * Želimo odzivne aplikacije, zlasti za manjše zaslone, kot so mobilne naprave, večje zaslone, kot so širokozaslonski 4K, in dinamične zaslone, kot so vrtljivi zasloni.  


### Odločitev

Odločili smo se za Bulmo.


### Stanje

Odločili smo se za Bulmo. Odprti smo za nove izbire ogrodij CSS, ko se pojavijo.


## Podrobnosti


### Predpostavke

Želimo ustvariti spletne aplikacije, ki so sodobne, hitre, zanesljive, odzivne itd.

Tipične sodobne spletne aplikacije zmanjšujejo/odpravljajo uporabo jQuery zaradi več razlogov: 

  * Sodobni JavaScript postopno uvaja mnoge zmožnosti, ki jih je zagotavljal jQuery, zato je jQuery manj potreben, obstajajo pa boljši/hitrejši/manjši moduli, ki zagotavljajo posebne izvedbe

  * Široki pristop jQuery je neposredno upravljanje DOM, kar je protivzorec za sodobna ogrodja JavaScript (npr. React, Vue, Svelte)

  * jQuery moti samega sebe, če je naložen dvakrat itd.


### Omejitve

Če izberemo ogrodje CSS, ki uporablja jQuery, smo prisiljeni uvoziti jQuery. Na primer, Semantic UI uporablja jQuery, Tachyons pa ne.

Če izberemo ogrodje CSS, ki je minimalno, se odpovemo komponentam ogrodja, ki jih morda želimo zdaj ali kmalu. Na primer, Semantic UI ponuja vrtiljak slik, Tachyons pa ne.


### Stališča

Preučili smo možnost brez ogrodja. To se še vedno zdi izvedljivo, zlasti ker CSS grid zagotavlja velik del tega, kar potrebujemo za naš projekt..

Preučili smo mnoga ogrodja CSS s hitrim razvrščanjem v ožji izbor: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons itd. Naši dve izbiri za podrobnejši pregled sta Semantic UI (ker ima najsemantičnejši pristop) in Bulma (ker ima najlažji pristop, ki zagotavlja komponente, ki jih želimo zdaj).

Preučili smo Semantic UI. Ta ponuja veliko komponent, tudi tiste, ki jih želimo za svoj projekt: zavihke, mreže, gumbe itd. Izvedli smo pilotni preizkus s Semantic UI na dva načina: z uporabo tipičnih datotek CDN in z uporabo repozitorijev NPM. V statični strani HTML smo s Semantic UI uspeli, v okviru svojega časovnega okvirja za gradnjo JavaScript SPA pa ne (predvsem zaradi težav z nalaganjem jQuery). Ugotovili smo, da drugi programerji razvijalce Semantic UI prosijo, naj ustvarijo različico brez jQuery, iz enakih razlogov kot mi. Drugi programerji že veliko let zahtevajo različico brez jQuery, a razvijalci so odgovorili ne in navedli, da bi bila vsaka različica brez jQuery pretežka za pisanje, npr. ~»projekt Semantic UI ima več kot 22.000 stičnih točk, ki uporabljajo jQuery«.

Primer s Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Preučili smo Bulmo. Bulma ima mnoge podobne zmožnosti kot Semantic UI, čeprav ne toliko dovršenih komponent. Bulma je zgrajena s sodobnimi tehnikami, na primer brez jQuery. Bulma ima nekaj komponent tretjih oseb, nekatere med njimi bomo morda želeli uporabiti.


Primer z Bulmo:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Kot zgoraj.

Natančneje, Semantic UI ima videti opozorilno zastavico tako glede tehnologije (tj. toliko stičnih točk jQuery) kot glede vodenja (tj. različica brez jQuery je bila trda zavrnitev, namesto da bi poskusili načrt razvoja, nenehno izboljševanje, zbiranje donacij itd.).


### Posledice

Če najdemo dobro ogrodje CSS brez jQuery, je to na splošno koristno in dobro.


## Povezano


### Povezane odločitve

Ogrodje CSS, ki ga izberemo, lahko vpliva na testabilnost.


### Povezane zahteve

Želimo hitro dostaviti povsem sodobno aplikacijo. 

Ne želimo porabljati časa za delo s starejšimi ogrodji (zlasti Semantic UI), ki uporabljajo starejše odvisnosti (zlasti jQuery).


### Povezani artefakti

Vpliva na ves tipični HTML, ki bo uporabljal CSS.


### Povezana načela

Lahko povratljivo.

Potreba po hitrosti.


## Opombe

Tu so vse opombe.
