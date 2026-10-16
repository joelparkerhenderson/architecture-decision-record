# Shranjevanje skrivnosti

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Povzetek


### Vprašanje

Shraniti moramo skrivnosti, kot so gesla, zasebni ključi, žetoni za preverjanje pristnosti itd.

Nekatere skrivnosti so usmerjene v uporabnike. Na primer, naš razvijalec želi s svojim mobilnim telefonom poiskati geslo za storitev.

Nekatere skrivnosti so usmerjene v sisteme. Na primer, naš cevovod za neprekinjeno dostavo mora poiskati poverilnice za naše oblačno gostovanje.


### Odločitev

Bitwarden za skrivnosti, usmerjene v uporabnike

Vault by HashiCorp za skrivnosti, usmerjene v sisteme.


### Stanje

Odločeno. Odprti smo za nove alternative, ko se pojavijo.


## Podrobnosti


### Predpostavke

Za ta namen in naše trenutno stanje cenimo priročnost, usmerjeno v uporabnike, kot so uporabne mobilne aplikacije.

  * Želimo zagotoviti hiter in enostaven dostop na poti, na primer za razvijalca, ki opravlja dežurno inženirstvo zanesljivosti sistemov.

  * Želimo imeti možnost deliti nekatere skrivnosti med izbranimi osebami, na primer ekipo.

Ne poskušamo rešiti problema za enega samega ponudnika, na primer shranjevanja vseh skrivnosti izključno pri Amazonu, Azure ali Googlu.

Ne želimo ad hoc pristopov, kot so »zapomni si« ali »zapiši na listek« ali »poišči si svoj način shranjevanja«.

Naš varnostni model za ta namen je v redu z uporabo uglednih ponudnikov COTS, kot so orodja za upravljanje gesel SaaS.


### Omejitve

Zdaj želimo nekaj, kar je preprosto, tj. brez potrebe po pisanju kode, brez potrebe po namestitvi strežnikov, brez potrebe po veliki zavezi, brez potrebe po standardizaciji vseh.


### Stališča

Preučili smo:

1. Končnim uporabnikom namenjene že pripravljene upravljalnike gesel: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG itd.

2. Sistemsko usmerjene upravljalnike gesel COTS: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Pristope, usmerjene v deljenje: uporaba skupnega dokumenta Google, skupnega kanala Slack ali skupne omrežne mape itd.

4. Ad hoc pristope z nizko tehnologijo, kot so pomnjenje, pisanje listka ali zanašanje na to, da vsak uporabnik poišče svoj pristop.


### Argument

Bitwarden, LastPass, 1Password in Dashlane so vsi komercialni izdelki, ki so na voljo v prosti prodaji (COTS).

  * Podobne vrste funkcij za uporabnike, ekipe, organizacije itd.

  * Namizna zmožnost za Windows in Mac ter mobilna zmožnost za Android in iOS.

  * Razširitve brskalnika za Chrome in Firefox za samodejno izpolnjevanje obrazcev itd.

Bitwarden ima dve prednosti pred drugimi:

  * Bitwarden je odprtokoden, kar pomeni, da je varnost mogoče pregledati s strani sodelavcev, podjetje pa je tudi široko cenjeno med razvijalci, usmerjenimi v varnost.

  * Anekdote razvijalcev programske opreme opisujejo občutno prednost Bitwardena pred drugimi.

Tipičen dober primer zapisa: https://jcs.org/2017/11/17/bitwarden

Tipična spletna stran za primerjavo in glasovanje: https://stackshare.io/stackups/bitwarden-vs-dashlane

KeyPass, pass, GPG itd. odlagamo, ker imajo dodatno kompleksnost. Vsi so videti kot dobre rešitve za tehnične uporabnike. GPG je videti še posebej dober za tehnične uporabnike, ki želijo zmožnosti, usmerjene v ukaze in prečne med sistemi.

KMS odlagamo, ker pomeni zaklenitev pri enem samem ponudniku.

Za sistemske potrebe izbiramo Vault, ker so ocene neverjetno pozitivne in ker ima HashiCorp odlično zgodovino vrhunske programske opreme in podpore.

Pristope z deljenjem, kot so skupni dokumenti, skupni kanali, skupne omrežne mape itd., zavračamo. Ti ne zagotavljajo varnostnih lastnosti, ki jih želimo.

Ad hoc pristope z nizko tehnologijo zavračamo, ker se vsi strinjamo, da to ni dolgoročna pot naprej.


### Posledice

Razvijalci bodo morda morali slediti skrivnostim na dveh mestih: v Bitwardenu za dostop, usmerjen v uporabnike, in v Vaultu za dostop, usmerjen v sisteme.


## Povezano


### Povezane odločitve

Odločitev o tem, kateri strežnik CI/CD, mora vključevati dokaz zmožnosti za dostop do skrivnosti.

Odločiti se bomo morali, kako upravljati skrivnosti glede politik, rotacij, organizacij itd.


### Povezane zahteve

Skrivnosti bodo imele sorodne zahteve glede skladnosti, revizije ter uvajanja/odjave kadrov.


### Povezani artefakti

Pričakujemo, da bomo nekatere skrivnosti morda izvozili v okoljske spremenljivke.


### Povezana načela

Lahko povratljivo.

Lahko vzporedno, tj. preprosto je uporabljati različne upravljalnike gesel.

Poceni za preizkus, tj. obstaja brezplačen preizkus in brez zaveze.


## Opombe

Tu so opombe vrednotenja. Opombe so vsi javni komentarji na različnih razpravnih forumih o DevOps.


### Vault by HashiCorp

Vault je natanko to, kar tukaj želite. 

Vaulta pa ne vrzite kar v produkcijo, najprej ga postavite v testnem okolju, ker je lahko dokumentacija HashiCorp precej pomanjkljiva, čeprav so njihovi izdelki neverjetni.

Zelo strma krivulja učenja in postavitev ni trivialna. 

Začetna postavitev je nekoliko mučna. Vendar se v celoti splača, skupnost pa jo podpira dovolj dobro, da se boste znašli.

Grozna dokumentacija, vendar je na spletu veliko vodnikov ljudi, ki so ga postavili, in če jih združite nekaj, boste imeli delujočo postavitev.

Začetna postavitev je zahtevala igranje z njihovimi grafikoni helm (vault in consul). Čeprav lahko tehnično uporabite veliko drugih zalednih sistemov, tega zares zares ne priporočam. Zaledje/consul je lahko majhen, če nimate veliko podatkov za shranjevanje.

Vsekakor se udomačite z uporabo CLI, ker je GUI bolj dokaz koncepta/oglasni portal za njihovo podjetniško izdajo.

Dejstvo, da ga ne morete preprosto »napolniti«, je mučno. Na primer, če imate 5 polj, morate ročno dodati vsako polje za vsak element. Torej ni tako, da vnaprej določite polja za posamezno kategorijo in nato izpolnite ta polja za vse elemente v tej kategoriji, ampak je bolj »vse generirate vsakič«, kar je (po mojem mnenju) mučenje.

Morda si oglejte tudi goldfish kot uporabniški vmesnik povrh vaulta. Precej olajša pridobitev vaše ekipe. Imajo tudi predstavitev. 1. Postavite consul. 2. Postavite vault, ki kaže na consul. 3. Postavite goldfish, ki kaže na vault. 3. Nastavite nek cron job za izvajanje consul snapshot za varnostne kopije.



### LastPass

LastPass Teams. Uporabljamo ga, ima predloge po meri, ACL, po mojem ničesar ne manjka.

LastPass sem uvedel v svoji organizaciji in mu dajem C+/B-. Največja težava v zadnjem času je pomanjkanje zanesljivosti. V zadnjih 90 dneh je bilo večkrat več ur, ko so bili trezorji prisiljeni v način brez povezave. To za mojo organizacijo ni idealno, ker imamo dobesedno več kot 4.000 gesel, shranjenih v več kot 20 skupnih mapah. Kot si lahko predstavljate, se pri toliko geslih vsaj nekaj posodobi ali doda vsak dan. Imamo načrt za obnovitev po nesreči, če težave trajajo več kot eno ali dve uri: skript vsako noč podpiše in šifrira izvoz trezorja v CSV, ki ga je mogoče uvoziti v keepass.

LastPass je imel neprijavljene zastoje poslabšane storitve: prijava »deluje«, a ne potegne spletnih mest, naključne funkcije v skrbniški plošči ne delujejo in ključi se ne delijo pravilno za nove skupne mape najvišje ravni. Imam posebnega uporabnika za »potiskanje ključev«/varnostno kopiranje, ki je v vsaki skupini. Prijava kot ta uporabnik običajno odpravi težave z deljenjem ključev, vendar ne takrat, ko je storitev poslabšana, ne glede na to, kaj piše na strani s stanjem ...

Za integracijo je lahko preprosta, če imate ustrezne ACL z modelom najmanjših privilegijev, npr. če ima uporabnik na vnosu ali mapi branje in pisanje ter samo branje, dobi samo dovoljenja za branje. Žal ACL moje organizacije niso najboljši, zato sem na koncu uporabil API za zagotavljanje v JSON in ~500 vrstic Pythona, ker se odvisna narava naših stotin ACL ni dobro preslikala v model najmanjših privilegijev. Na koncu sem pridobil vse ACL, v katerih je bil uporabnik, in izvedel nekakšen sprehod po odvisnostih.

Če sta vaša struktura ACL ali skupin že zgrajena z mislijo na strukturo najmanjših privilegijev, bo orodje za sinhronizacijo AD/LDAP za Windows delovalo dobro.

Obrnite se na njihovo prodajno ekipo in lahko vam uredijo daljši podjetniški preizkus. Pred odločitvijo se prepričajte, da popolnoma razumete njegove omejitve. Imeli smo kar nekaj rastnih bolečin, a razen izpadov ali poslabšav na strani strežnika je bilo neverjetno gladko.


### Bitwarden

Bitwarden ima lepa orodja okoli sebe (spletni UI, CLI, mobilna, namizna). Samostojno gostovanje in dokaj enostavna postavitev. Dokaj dobra dokumentacija in orodje, ki ga priporoča PrivacyTools.


### EnvKey

https://www.envkey.com/ je SaaS. Zelo preprost za uvedbo, integracijo in upravljanje.

Funkcije:

  * Zaščita ključev API in poverilnic.

  * Ohranjanje konfiguracije usklajene povsod.

  * Pametno, od konca do konca šifrirano upravljanje konfiguracije in skrivnosti. 

  * Preprečevanje nezavarovanega deljenja in razraščanja konfiguracije. 

  * Integracija v nekaj minutah.

Zmožnosti:

  * Upravljajte konfiguracijo in ravni dostopa za vse svoje aplikacije, okolja in ekipe na enem mestu.

  * Nastavite katero koli razvojno ali strežniško okolje z eno samo okoljsko spremenljivko.

Prednosti:

  * Dobra domača stran.

  * Jasna vrednostna ponudba.

  * Vizualno odlična spletna aplikacija.

  * Vrhunski vzorčni podatki, npr. Algolia, AWS, Datadog, GitHub, Stripe itd.

  * 30 minut sem se pogovarjal z ustanoviteljem o podjetju, UI itd. Dane se zdi dobro obveščen, iskren glede prednosti/slabosti in sposoben partner.

  * Podjetje je v bistvu tipično podjetje Y Combinator z 1 ustanoviteljem. Januarja 2018 je zbralo 120.000 USD.

  * Poudarek je na doseganju podjetniških funkcij, zlasti na prehodu z gostovanja EnvKey v oblaku na lokalno gostovanje ali BYOC.

  * Možna pot naprej: začeti z EnvKey zaradi enostavnosti uporabe, nato pozneje (ali vzporedno) dodati Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant je odprtokodna storitev za upravljanje skrivnosti, ki zagotavlja uporabniku prijazno shranjevanje skrivnosti in dostop do njih na varen način, razvijalcev pri Lyftu.

Preverjanje pristnosti KMS: Confidant rešuje problem preverjanja pristnosti »kura ali jajce« z uporabo AWS KMS in IAM, da vlogam IAM omogoči generiranje varnih žetonov za preverjanje pristnosti, ki jih lahko Confidant preveri. Confidant upravlja tudi dovoljenja KMS za vaše vloge IAM, kar vlogam IAM omogoča generiranje žetonov, ki jih je mogoče uporabiti za preverjanje pristnosti med storitvami ali za posredovanje šifriranih sporočil med storitvami.

Šifriranje različiciranih skrivnosti v mirovanju: Confidant shranjuje skrivnosti samo z dodajanjem v DynamoDB in za vsako revizijo vsake skrivnosti generira edinstven podatkovni ključ KMS z uporabo simetrične overjene kriptografije Fernet.

Uporabniku prijazen spletni vmesnik za upravljanje skrivnosti: Confidant zagotavlja spletni vmesnik AngularJS, ki končnim uporabnikom omogoča preprosto upravljanje skrivnosti, preslikav skrivnosti na storitve in zgodovine sprememb.


### Devolutions Password Server

https://server.devolutions.net/

Zavarujte, upravljajte in nadzirajte dostop do privilegiranih računov in sej.

Celovit, zelo zavarovan trezor gesel, ki vam omogoča nadzor dostopa do privilegiranih računov, hkrati pa izboljšuje splošno vidnost omrežja za sistemske skrbnike in zagotavlja brezhibno izkušnjo za končne uporabnike.

Funkcije: osrednji trezor gesel organizacije, zasebni trezor za posameznega uporabnika, upravljalnik gesel, vstavljanje poverilnic,
integracija z Active Directory, nadzor dostopa na podlagi vlog, dvofaktorsko preverjanje pristnosti, pripravljenost za podjetja, omejitve IP, zmožnosti upravljanja, samodejni generator gesel, dostop prek mobilne aplikacije, zgodovina gesel, poročila o dostopu, opozorila po e-pošti.

  * podpira šifriranje podatkov

  * podpira več shem preverjanja pristnosti, vključno z LDAP, O365 in lokalnimi uporabniki Z OPORO za MFA iz več virov

  * več repozitorijev/trezorjev z natančnim nadzorom dostopa za več ekip

  * sodoben spletni UI

  * zasebni trezorji poverilnic in povezav za osebne poverilnice/povezave

  * mobilne aplikacije za iOS/Android

  * revizijski dnevniki za vsak vnos, kdo/kaj/kdaj z izbirnim pozivom, zakaj dostopajo

  * predloge po meri (čeprav izvorno podpirajo stotine vrst povezav)

  * še veliko več funkcij in debeli odjemalec za Windows/Mac (Remote Desktop Manager), s katerim se lahko sinhronizirate in ki močno razširi možnosti ... povezave z enim klikom

  * cena ni tako slaba – do 15 uporabnikov stane 500 USD na leto za strežnik gesel


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Funkcije lokalne različice: 

  * Popoln nadzor nad vašimi varnostnimi sistemi in infrastrukturo od konca do konca

  * Namestitev programske opreme v vašem lokalnem podatkovnem centru ali v lastni instanci navideznega zasebnega oblaka

  * Izpolnjevanje pravnih in regulativnih obveznosti, ki zahtevajo, da vsi podatki in sistemi ostanejo lokalno

Funkcije oblačne različice:

  * Model programske opreme kot storitve (SaaS) vam omogoča, da se prijavite in takoj začnete

  * Elastična razširljivost z vašo rastjo

  * Nadzor in redundanco zagotavlja Azure s SLA razpoložljivosti 99,9 %

Povratne informacije uporabnikov:

  * Ta izdelek smo včasih uporabljali. Tako zlahka se ga je dalo zaobiti in pravila delujejo samo za pametne ljudi. Leni ali neumni uporabniki ga lahko v ekipnem območju preprosto pokvarijo. Cene so pogajalske, ko se pogovarjate z njimi.

  * Lahko ga poganjate z SQL Express in strežnikom Win 7. 

  * Poceni.
