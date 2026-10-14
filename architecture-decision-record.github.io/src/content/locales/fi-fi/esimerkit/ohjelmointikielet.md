# Ohjelmointikielet

Sisällys:

* [Yhteenveto](#yhteenveto)
  * [Ongelma](#ongelma)
  * [Päätös](#päätös)
  * [Tila](#tila)
* [Yksityiskohdat](#yksityiskohdat)
  * [Oletukset](#oletukset)
  * [Rajoitteet](#rajoitteet)
  * [Kannat](#kannat)
  * [Perustelu](#perustelu)
  * [Seuraukset](#seuraukset)
* [Liittyvät](#liittyvät)
  * [Liittyvät päätökset](#liittyvät-päätökset)
  * [Liittyvät vaatimukset](#liittyvät-vaatimukset)
  * [Liittyvät artefaktit](#liittyvät-artefaktit)
  * [Liittyvät periaatteet](#liittyvät-periaatteet)
* [Huomiot](#huomiot)


## Yhteenveto


### Ongelma

Meidän on valittava ohjelmointikielet ohjelmistoillemme. Meillä on kaksi pääasiallista tarvetta: verkkosovelluksiin sopiva käyttöliittymäohjelmointikieli ja palvelinsovelluksiin sopiva taustajärjestelmän ohjelmointikieli.


### Päätös

Valitsemme TypeScriptin käyttöliittymälle.

Valitsemme Rustin taustajärjestelmälle.


### Tila

Päätetty. Olemme avoimia uusille vaihtoehdoille niiden ilmaantuessa.


## Yksityiskohdat


### Oletukset

Käyttöliittymäsovellukset ovat tyypillisiä:

  * Tyypilliset käyttäjät ja vuorovaikutukset

  * Tyypilliset selaimet ja järjestelmät

  * Tyypilliset kehitys- ja käyttöönottotyöt

Käyttöliittymäsovellukset todennäköisesti kehittyvät nopeasti:

  * Haluamme varmistaa nopean ja helpon kehityksen, käyttöönotot, iteraatiot jne.

  * Arvostamme todistettavuutta, kuten tyyppiturvallisuutta, ja olemme valmiita tekemään hieman enemmän työtä sen saavuttamiseksi.

  * Emme tarvitse vanhan yhteensopivuutta.

Taustajärjestelmäsovellukset ovat tavallista vaativampia:

  * Tavallista korkeammat tavoitteet laadulle, erityisesti todistettavuudelle, luotettavuudelle, tietoturvalle jne.

  * Tavallista korkeammat tavoitteet lähes reaaliaikaisuudelle, eli emme halua taukoja virtuaalikoneen roskienkeruun vuoksi.

  * Tavallista korkeammat tavoitteet funktionaaliselle ohjelmoinnille, erityisesti rinnakkaistamiselle, moniydinprosessoinnille ja muistiturvallisuudelle.

Hyväksymme hitaammat käännösaikanopeudet käännösaikaisen turvallisuuden ja ajonaikaisten nopeuksien hyväksi.


### Rajoitteet

Meillä on vahva rajoite kielille, joita voidaan käyttää suurten pilvipalveluntarjoajien palvelujen funktioiden kanssa, kuten Amazon Lambda.


### Kannat

Harkitsimme näitä kieliä:

  * C

  * C++

  * Clojure
  
  * Elixir
  
  * Erlang
  
  * Elm
  
  * Flow
  
  * Go
  
  * Haskell
  
  * Java
  
  * JavaScript
  
  * Kotlin
  
  * Python
  
  * Ruby
  
  * Rust
  
  * TypeScript



### Perustelu

Yhteenveto kielittäin:

  * C: hylätty heikon turvallisuuden vuoksi; Rust osaa tehdä lähes kaiken paremmin.

  * C++: hylätty, koska se on sotku; Rust osaa tehdä lähes kaiken paremmin.

  * Clojure: erinomainen mallinnus; paras Lisp-approksimaatio; loistava ajoympäristö JVM:llä.
  
  * Elixir: erinomainen ajoympäristö mukaan lukien käyttöönotettavuus ja rinnakkaisuus; erinomainen kehittäjäkokemus; suhteellisen pieni ekosysteemi.

  * Erlang: erinomainen ajoympäristö mukaan lukien käyttöönotettavuus ja rinnakkaisuus; haastava kehittäjäkokemus; suhteellisen pieni ekosysteemi.

  * Elm: näyttää hyvin lupaavalta; IBM julkaisee merkittäviä tapaustutkimuksia hyvin tuloksin; pienempi ekosysteemi.

  * Flow: kiinnostava parannus JavaScriptiin; kehittäjät kuitenkin siirtyvät pois siitä.

  * Go: erinomainen kehittäjäkokemus; erinomainen rinnakkaisuus; mutta huonojen päätösten historia, joka vammauttaa kieltä.

  * Haskell: paras funktionaalinen kieli; pienempi kehittäjäyhteisö; ei ole saavuttanut tarpeeksi julkaistuja tuotantomenestyksiä.

  * Java: erinomainen ajoympäristö; erinomainen ekosysteemi; keskinkertainen kehittäjäkokemus.

  * JavaScript: kaikkien aikojen suosituin kieli; laajin ekosysteemi.

  * Kotlin: korjaa niin paljon Javasta; erinomainen JetBrainsin tuki; hyviä julkaistuja tapauksia siirtymisestä Javasta Kotliniin.
  
  * Python: suosituin kieli järjestelmänhallintaan; loistavat analytiikkatyökalut; hyvät verkkokehykset; mutta Google hylkäsi sen Gon hyväksi.

  * Ruby: paras kehittäjäkokemus koskaan; parhaat verkkokehykset; mukavin yhteisö; mutta erittäin hidas; jossain määrin vaikea paketoida.

  * Rust: paras uusi kieli; nollaabstraktion painotus; rinnakkaisuuden painotus; kuitenkin suhteellisen pieni ekosysteemi; ja sillä on tarkoituksellisia rajoja joillekin kääntäjän kiihdytyksille, esim. suora muistiin pääsy täytyy olla nimenomaisesti turvaton.

  * TypeScript: lisää tyypit JavaScriptiin; loistava transpiloija; kasvava kehittäjien painotus siirtymiseen JavaScriptistä TypeScriptiin; vahva Microsoftin tuki.

Päätimme, että virtuaalikoneilla on joukko kompromisseja, joita emme tarvitse juuri nyt, kuten lisäkompleksisuus, joka tarjoaa ajonaikaisia ominaisuuksia.

Uskomme, että ydinpäätöksemme perustuu kahteen läpileikkaavaan huolenaiheeseen:

  * Nopeimman ajonaikaisen nopeuden ja tiukimman järjestelmäpääsyn saavuttamiseksi valitsisimme JavaScriptin ja C:n.

  * Lähes nopeimman ajonaikaisen nopeuden ja lähes tiukimman järjestelmäpääsyn saavuttamiseksi valitsemme TypeScriptin ja Rustin.

Kunniamaininnat menevät virtuaalikonekielille ja verkkokehyksille, jotka valitsisimme, jos haluaisimme virtuaalikonekielen:

  * Clojure ja Luminus

  * Java ja Spring

  * Elixir ja Phoenix


### Seuraukset

Käyttöliittymäkehittäjien on opeteltava TypeScript. Tämä on todennäköisesti helppo oppimiskäyrä, jos kehittäjän ensisijainen kokemus on JavaScriptin käytöstä.

Taustajärjestelmäkehittäjien on opeteltava Rust. Tämä on todennäköisesti kohtalainen oppimiskäyrä, jos kehittäjän ensisijainen kokemus on C/C++:n käytöstä, ja vaikea oppimiskäyrä, jos kehittäjän ensisijainen kokemus on Javan, Pythonin, Rubyn tai vastaavien muistinhallittujen kielten käytöstä. 

TypeScript ja Rust ovat molemmat suhteellisen uusia. Tämä tarkoittaa, että monilla työkaluilla ei vielä ole dokumentaatiota näille kielille. Esimerkiksi devops-putki on perustettava näille kielille, ja toistaiseksi mikään arvioimistamme devops-työkaluista ei sisällä oletusesimerkkejä näille kielille.

TypeScriptin ja Rustin käännösajat ovat melko hitaita. Osa tästä voi johtua kielten uutuudesta. Meidän kannattaa ehkä tutkia, miten hitaita käännösaikoja voidaan lieventää, esimerkiksi tarpeenmukaisella kääntämisellä, rinnakkaisella kääntämisellä jne.

IDE-tuki näille kielille ei ole vielä kaikkialla eikä vielä ensiluokkaista. Esimerkiksi JetBrains myy PyCharm-IDE:tä ensiluokkaiseen Python-tukeen, mutta ei myy IDE:tä, jossa on ensiluokkainen Rust-tuki; sen sijaan JetBrains voi käyttää Rust-liitännäistä, joka tarjoaa ehkä 80 % Rust-kielen tuesta verrattuna Python-kielen tukeen.


## Liittyvät


### Liittyvät päätökset

Pyrimme ekosysteemivalintoihin, jotka ovat linjassa näiden kielten kanssa.

Esimerkiksi haluamme valita IDE:n, jolla on hyvät ominaisuudet näille kielille.

Esimerkiksi käyttöliittymän verkkokehykselle olemme todennäköisemmin päättämässä kehyksestä, joka pyrkii TypeScriptiin (esim. Vue), kuin kehyksestä, joka pyrkii tavalliseen JavaScriptiin (esim. React).


### Liittyvät vaatimukset

Koko työkaluketjumme on tuettava näitä kieliä.


### Liittyvät artefaktit

Odotamme, että saatamme viedä joitakin salaisuuksia ympäristömuuttujiin.


### Liittyvät periaatteet

Mittaa kahdesti, rakenna kerran. Priorisoimme jonkin verran turvallisuutta jonkin nopeuden edelle.

Ajoaika on arvokkaampi kuin käännösaika. Priorisoimme asiakkaiden käytön kehittäjien käytön edelle.


## Huomiot

Mahdolliset huomiot tähän.
