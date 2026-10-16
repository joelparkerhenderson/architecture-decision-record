# Predloga zapisa odločitve arc42

<https://arc42.org/overview>

## 1. Uvod in cilji

Kratek opis zahtev, gonilnih sil in izvleček (ali povzetek) zahtev. Trije (največ pet) kakovostni cilji arhitekture z najvišjo prednostjo za glavne deležnike. Tabela pomembnih deležnikov z njihovimi pričakovanji glede arhitekture.

## 1.1 Pregled zahtev

### Vsebina

Kratek opis funkcionalnih zahtev, gonilnih sil in izvleček (ali povzetek) zahtev. Povezave na (upajmo obstoječe) dokumente zahtev z informacijo, kje jih najti. 

### Motivacija

Z vidika končnih uporabnikov se sistem ustvari ali spremeni, da bi izboljšal podporo poslovni dejavnosti in/ali izboljšal kakovost. 

### Oblika

Kratek besedilni opis, verjetno v tabelarični obliki primerov uporabe. Če dokumenti zahtev obstajajo, naj ta pregled napotuje nanje.

Ti izvlečki naj bodo čim krajši. Uravnotežite berljivost tega dokumenta in morebitno odvečnost glede na dokumente zahtev. 

## 1.2 Kakovostni cilji

### Vsebina

Trije (največ pet) kakovostni cilji arhitekture, katerih izpolnitev je najpomembnejša za glavne deležnike. Res mislimo kakovostne cilje za arhitekturo. Ne zamenjujte jih s projektnimi cilji. Niso nujno enaki. Standard ISO 25010 ponuja lep pregled morebitnih zanimivih tem.

### Motivacija

Poznati morate kakovostne cilje svojih najpomembnejših deležnikov, saj bodo vplivali na temeljne arhitekturne odločitve. Bodite zelo konkretni glede teh kakovosti, izogibajte se modnim izrazom. Če kot arhitekt ne veste, kako bo kakovost vašega dela ocenjena ...

### Oblika

Tabela z najpomembnejšimi kakovostnimi cilji in konkretnimi scenariji, razvrščena po prednostih.

## 1.3 Deležniki

### Vsebina

Izrecen pregled deležnikov sistema, to je vseh oseb, vlog ali organizacij, ki

- morajo poznati arhitekturo

- jih je treba prepričati o arhitekturi

- morajo delati z arhitekturo ali s kodo

- potrebujejo dokumentacijo arhitekture za svoje delo

- morajo sprejemati odločitve o sistemu ali njegovem razvoju

### Motivacija

Poznati morate vse strani, vključene v razvoj sistema ali ki jih sistem zadeva. Sicer vas lahko pozneje v razvojnem procesu čakajo neprijetna presenečenja. Ti deležniki določajo obseg in raven podrobnosti vašega dela in njegovih rezultatov.

### Oblika

Tabela z imeni vlog, imeni oseb in njihovimi pričakovanji glede arhitekture in njene dokumentacije.

## 2. Omejitve

Vse, kar omejuje ekipe pri odločitvah o oblikovanju in izvedbi ali odločitvah o sorodnih procesih. Včasih presegajo posamezne sisteme in veljajo za cele organizacije in podjetja.

### Vsebina

Vsaka zahteva, ki programske arhitekte omejuje v svobodi odločanja o oblikovanju in izvedbi ali o razvojnem procesu. Te omejitve včasih presegajo posamezne sisteme in veljajo za cele organizacije in podjetja.

### Motivacija

Arhitekti morajo natančno vedeti, kje so pri svojih oblikovalskih odločitvah svobodni in kje morajo upoštevati omejitve. Z omejitvami se je treba vedno ukvarjati; lahko pa so predmet pogajanj.

### Oblika

Preproste tabele omejitev s pojasnili. Po potrebi jih lahko razdelite na tehnične omejitve, organizacijske in politične omejitve ter konvencije (npr. smernice za programiranje ali upravljanje različic, konvencije za dokumentacijo ali poimenovanje)

## 3. Kontekst in obseg

Razmejuje vaš sistem od njegovih (zunanjih) komunikacijskih partnerjev (sosednjih sistemov in uporabnikov). Določa zunanje vmesnike. Prikazano z vidika poslovanja/domene (vedno) ali tehničnega vidika (neobvezno)

### Vsebina

Obseg in kontekst sistema – kot ime pove – razmejuje vaš sistem (tj. vaš obseg) od vseh njegovih komunikacijskih partnerjev (sosednjih sistemov in uporabnikov, tj. konteksta vašega sistema). S tem določa zunanje vmesnike.

Če je potrebno, ločite poslovni kontekst (vhodi in izhodi, specifični za domeno) od tehničnega konteksta (kanali, protokoli, strojna oprema).

### Motivacija

Domenski in tehnični vmesniki do komunikacijskih partnerjev spadajo med najbolj kritične vidike vašega sistema. Poskrbite, da jih popolnoma razumete.

### Oblika

- Različni kontekstni diagrami

- Seznami komunikacijskih partnerjev in njihovih vmesnikov.

## 3.1 Poslovni kontekst

### Vsebina

Specifikacija vseh komunikacijskih partnerjev (uporabnikov, IT-sistemov, ...) s pojasnili domensko specifičnih vhodov in izhodov ali vmesnikov. Po želji lahko dodate domensko specifične formate ali komunikacijske protokole.

### Motivacija

Vsi deležniki bi morali razumeti, kateri podatki se izmenjujejo z okoljem sistema.

### Oblika

Vse vrste diagramov, ki prikazujejo sistem kot črno skrinjico in določajo domenske vmesnike do komunikacijskih partnerjev.

Lahko (ali dodatno) uporabite tabelo. Naslov tabele je ime vašega sistema, trije stolpci vsebujejo ime komunikacijskega partnerja, vhode in izhode.

## 3.2 Tehnični kontekst

### Vsebina

Tehnični vmesniki (kanali in prenosni mediji), ki povezujejo vaš sistem z njegovim okoljem. Poleg tega preslikava domensko specifičnih vhodov/izhodov na kanale, tj. pojasnilo, kateri V/I uporablja kateri kanal.

### Motivacija

Mnogi deležniki sprejemajo arhitekturne odločitve na podlagi tehničnih vmesnikov med sistemom in njegovim kontekstom. Te tehnične vmesnike določajo predvsem oblikovalci infrastrukture ali strojne opreme.

### Oblika

Npr. diagram uvajanja UML, ki opisuje kanale do sosednjih sistemov, skupaj s preslikovalno tabelo, ki prikazuje razmerja med kanali in vhodi/izhodi.

## 4. Strategija rešitve

Povzetek temeljnih odločitev in strategij rešitve, ki oblikujejo arhitekturo. Lahko vključuje tehnologijo, razgradnjo najvišje ravni, pristope k doseganju najpomembnejših kakovostnih ciljev in ustrezne organizacijske odločitve.

### Vsebina

Kratek povzetek in pojasnilo temeljnih odločitev in strategij rešitve, ki oblikujejo arhitekturo sistema. Sem spadajo

- tehnološke odločitve

- odločitve o razgradnji sistema na najvišji ravni, npr. uporaba arhitekturnega vzorca ali oblikovalskega vzorca

- odločitve o doseganju ključnih kakovostnih ciljev

- ustrezne organizacijske odločitve, npr. izbira razvojnega procesa ali prenos določenih nalog na tretje strani.

### Motivacija

Te odločitve tvorijo temeljne kamne vaše arhitekture. So osnova za številne druge podrobne odločitve ali pravila izvedbe.

### Oblika

Pojasnilo teh ključnih odločitev naj bo kratko.

Utemeljite, kaj ste odločili in zakaj ste se tako odločili, na podlagi svoje izjave o problemu, kakovostnih ciljev in ključnih omejitev. Za podrobnosti se sklicujte na naslednje razdelke (razdelek 5 za strukturne podrobnosti, razdelek 8 za prečne koncepte).

Uporabite lahko seznam pristopov k rešitvi ali tabelo.

## 5. Pogled gradnikov

Statična razgradnja sistema, abstrakcije izvorne kode, prikazane kot hierarhija belih skrinjic (ki vsebujejo črne skrinjice), do ustrezne ravni podrobnosti.

### Vsebina

Pogled gradnikov prikazuje statično razgradnjo sistema na gradnike (module, komponente, podsisteme, razrede, vmesnike, pakete, knjižnice, ogrodja, plasti, particije, nivoje, funkcije, makre, operacije, podatkovne strukture, ...) ter njihove odvisnosti (razmerja, povezave, ...)

Ta pogled je obvezen za vsako dokumentacijo arhitekture. Po analogiji s hišo je to tloris.

### Motivacija

Ohranjajte pregled nad svojo izvorno kodo tako, da njeno strukturo z abstrakcijo naredite razumljivo.

To vam omogoča komunikacijo z deležniki na abstraktni ravni brez razkrivanja podrobnosti izvedbe.

### Oblika

Pogled gradnikov je hierarhična zbirka črnih in belih skrinjic (glejte sliko spodaj) ter njihovih opisov.

## 5.1 Bela skrinjica: celoten sistem

Tu opišete razgradnjo celotnega sistema z naslednjo predlogo bele skrinjice. Vsebuje

- pregledni diagram

- motivacijo za razgradnjo

- opise črnih skrinjic vsebovanih gradnikov. Za te vam ponujamo alternative:

  - uporabite eno tabelo za kratek in pragmatičen pregled vseh vsebovanih gradnikov in njihovih vmesnikov

  - uporabite seznam opisov črnih skrinjic gradnikov po predlogi črne skrinjice (glejte spodaj). Odvisno od izbranega orodja so lahko to podpoglavja (v besedilnih datotekah), podstrani (v wikiju) ali ugnezdeni elementi (v orodju za modeliranje).

  - (neobvezno:) pomembni vmesniki, ki niso pojasnjeni v predlogah črnih skrinjic gradnika, so pa zelo pomembni za razumevanje bele skrinjice.

Ker obstaja toliko načinov za določanje vmesnikov, zanje ne zagotavljamo posebne predloge.

V najboljšem primeru se boste izognili s primeri ali preprostimi podpisi.

## 5.2 Raven 2

Tu lahko notranjo strukturo (nekaterih) gradnikov z ravni 1 določite kot bele skrinjice.

Odločiti se morate, kateri gradniki vašega sistema so dovolj pomembni, da upravičujejo tako podroben opis. Prednost dajte ustreznosti pred popolnostjo. Določite pomembne, presenetljive, tvegane, kompleksne ali spremenljive gradnike. Izpustite običajne, preproste, dolgočasne ali standardizirane dele sistema

### 5.2.1 Bela skrinjica za gradnik 1

Določa notranjo strukturo gradnika 1.

Uporabite predlogo bele skrinjice (glejte zgoraj).

## 6. Pogled izvajanja

Vedenje gradnikov kot scenariji, ki zajemajo pomembne primere uporabe ali funkcije, interakcije na kritičnih zunanjih vmesnikih, delovanje in upravljanje ter vedenje ob napakah in izjemah.

### Vsebina

Pogled izvajanja opisuje konkretno vedenje in interakcije gradnikov sistema v obliki scenarijev z naslednjih področij:

- pomembni primeri uporabe ali funkcije: kako jih gradniki izvedejo?

- interakcije na kritičnih zunanjih vmesnikih: kako gradniki sodelujejo z uporabniki in sosednjimi sistemi?

- delovanje in upravljanje: zagon, zagon sistema, ustavitev

- scenariji napak in izjem

Opomba: Glavno merilo za izbiro možnih scenarijev (zaporedij, potekov dela) je njihova arhitekturna ustreznost. Ni pomembno opisati veliko število scenarijev. Raje dokumentirajte reprezentativen izbor.

### Motivacija

Razumeti morate, kako (primerki) gradnikov vašega sistema opravljajo svoje delo in komunicirajo med izvajanjem. Scenarije boste v dokumentaciji zajemali predvsem zato, da arhitekturo sporočite deležnikom, ki so manj pripravljeni ali sposobni brati in razumeti statične modele (pogled gradnikov, pogled uvajanja).

### Oblika

Za opisovanje scenarijev obstaja veliko notacij, npr.


- oštevilčen seznam korakov (v naravnem jeziku)

- diagrami dejavnosti ali diagrami poteka

- sekvenčni diagrami

- BPMN ali EPC (event process chains, verige dogodkovnih procesov)

- avtomati stanj

- itd.

## 6.n Scenarij izvajanja n (1, 2, 3 itd.)

Vstavite diagram izvajanja ali besedilni opis scenarija.

Vstavite opis pomembnih vidikov interakcij med primerki gradnikov, prikazanimi v tem diagramu.

## 7. Pogled uvajanja

Tehnična infrastruktura z okolji, računalniki, procesorji, topologijami. Preslikava (programskih) gradnikov na elemente infrastrukture.

### Vsebina

Pogled uvajanja opisuje:

- tehnično infrastrukturo, uporabljeno za izvajanje vašega sistema, z infrastrukturnimi
  elementi, kot so geografske lokacije, okolja, računalniki, procesorji,
  kanali in omrežne topologije, ter drugimi infrastrukturnimi elementi, in

- preslikavo (programskih) gradnikov na te infrastrukturne elemente.

Sistemi se pogosto izvajajo v različnih okoljih, npr. razvojno okolje, testno okolje, produkcijsko okolje. V takih primerih morate dokumentirati vsa ustrezna okolja.

Pogled uvajanja še posebej dokumentirajte, kadar se vaša programska oprema izvaja kot porazdeljen sistem z več kot enim računalnikom, procesorjem, strežnikom ali vsebnikom ali kadar sami oblikujete in izdelujete lastne strojne procesorje in čipe.

S programskega vidika zadošča zajeti tiste elemente infrastrukture, ki so potrebni za prikaz uvajanja vaših gradnikov. Arhitekti strojne opreme lahko gredo dlje in opišejo infrastrukturo do katere koli ravni podrobnosti, ki jo morajo zajeti. 

### Motivacija

Programska oprema ne deluje brez strojne opreme. Ta osnovna infrastruktura lahko in bo vplivala na vaš sistem in/ali nekatere prečne koncepte. Zato morate poznati infrastrukturo.

### Oblika

Morda je diagram uvajanja najvišje ravni že vsebovan v razdelku 3.2. kot tehnični kontekst z vašo lastno infrastrukturo kot ENO črno skrinjico. V tem razdelku to črno skrinjico povečate z dodatnimi diagrami uvajanja.

- UML ponuja diagrame uvajanja za izražanje tega pogleda. Uporabite jih, verjetno z ugnezdenimi diagrami, kadar je vaša infrastruktura kompleksnejša.

- Kadar vaši (strojni) deležniki raje uporabljajo druge vrste diagramov kot
  diagram uvajanja UML, jim dovolite uporabo katere koli vrste, ki lahko prikaže vozlišča
  in kanale infrastrukture.

## 7.1 Infrastruktura, raven 1

Opišite (običajno s kombinacijo diagramov, tabel in besedila):

- razporeditev vašega sistema na več lokacij, okolij, računalnikov, procesorjev, ... ter fizične povezave med njimi

- pomembno utemeljitev ali motivacijo za to strukturo uvajanja

- značilnosti kakovosti in/ali zmogljivosti infrastrukture

- preslikavo programskih artefaktov (gradnikov) na elemente infrastrukture

Za več okolij ali alternativna uvajanja prosimo kopirajte ta razdelek arc42 za vsa ustrezna okolja. **

## 7.2 Infrastruktura, raven 2

Tu lahko vključite notranjo strukturo (nekaterih) elementov infrastrukture z ravni 1 infrastrukture.

Prosimo, kopirajte strukturo z ravni 1 za vsak izbrani element.

## 8. Prečni koncepti

Splošna, temeljna pravila in pristopi k rešitvam, pomembni v več delih (→ prečno) sistema. Koncepti so pogosto povezani z več gradniki. Vključite različne teme, kot so domenski modeli, arhitekturni vzorci in slogi, pravila za uporabo določene tehnologije in pravila izvedbe.

### Vsebina

Ta razdelek opisuje prečne koncepte (prakse, vzorce, pravila ali zamisli za rešitve). Taki koncepti so pogosto povezani z več gradniki. Lahko vključujejo veliko različnih tem.

### Motivacija

Koncepti so osnova konceptualne celovitosti (doslednosti, homogenosti) arhitekture. Zato so pomemben prispevek k doseganju notranjih kakovosti vašega sistema.

To je mesto v predlogi, ki smo ga zagotovili za zaokroženo specifikacijo takih konceptov.

Mnogi od teh konceptov so povezani z več vašimi gradniki ali nanje vplivajo.

### Oblika

Oblika je lahko različna:

- konceptualni dokumenti s kakršno koli strukturo

- primeri izvedb, zlasti za tehnične koncepte

- prečni izseki modelov ali scenariji z notacijami arhitekturnih pogledov

### Struktura tega razdelka

Izberite samo najpotrebnejše teme za svoj sistem in vsaki dodelite naslov druge ravni v tem razdelku (npr. 8.1, 8.2 itd).

- NE POSKUŠAJTE zajeti vseh tem iz zgoraj omenjenega diagrama.

### Ozadje

Nekatere teme znotraj sistemov pogosto zadevajo več gradnikov, elementov strojne opreme ali razvojnih procesov. Take prečne teme je morda lažje sporočati ali dokumentirati na osrednji lokaciji, namesto da bi jih ponavljali v opisu zadevnih gradnikov, elementov strojne opreme ali razvojnih procesov.

Nekateri koncepti lahko zadevajo vse elemente sistema, drugi so morda pomembni le za nekaj.

## 9. Arhitekturne odločitve

Pomembne, drage, kritične, obsežne ali tvegane arhitekturne odločitve z utemeljitvami.

### Vsebina

Pomembne, drage, obsežne ali tvegane arhitekturne odločitve z utemeljitvami. »Odločitve« pomenijo izbiro ene alternative na podlagi danih meril.

Presodite, ali naj se arhitekturna odločitev dokumentira tukaj v tem osrednjem razdelku ali pa jo je bolje dokumentirati lokalno (npr. znotraj predloge bele skrinjice enega gradnika). Izogibajte se odvečnim besedilom. Sklicujte se na razdelek 4, kjer ste najpomembnejše odločitve svoje arhitekture že zajeli.

### Motivacija

Deležniki vašega sistema bi morali biti sposobni razumeti in izslediti vaše odločitve.

### Oblika

- ADR (zapis arhitekturne odločitve) za vsako pomembno odločitev

- seznam ali tabela, razvrščena po pomembnosti in posledicah ali

- podrobneje v obliki ločenih razdelkov za vsako odločitev

### Ozadje (o ADR)

Manjše kose dokumentacije je lažje brati, ustvarjati in vzdrževati. Ko gre za arhitekturne odločitve, razvojne ekipe pogosto:

- vedo za odločitev, saj je vidna npr. v izvorni kodi, vendar

- ne poznajo motivacije za to odločitev (glejte Nygard 2011)

Zato bi morali dokumentirati nekaj pomembnih odločitev skupaj z njihovo motivacijo in utemeljitvijo

### Naš predlog glede odločitev

Vodite zbirko arhitekturno pomembnih odločitev, to je odločitev, ki vplivajo na strukturo, kakovostne značilnosti, pomembne (zlasti zunanje) odvisnosti in vmesnike ali tehnike gradnje (zahvala Michaelu Nygardu za ta predlog).

## 10. Zahteve glede kakovosti

Zahteve glede kakovosti kot scenariji, z drevesom kakovosti za pregled na visoki ravni. Najpomembnejši kakovostni cilji bi morali biti opisani v razdelku 1.2. (kakovostni cilji).

### Vsebina

Ta razdelek vsebuje vse ustrezne zahteve glede kakovosti.

Najpomembnejše med njimi so že opisane v razdelku 1.2. (kakovostni cilji), zato naj se tukaj le navedejo. V tem razdelku 10 zajemite tudi zahteve glede kakovosti manjše pomembnosti, ki ne bodo ustvarile velikih tveganj, če niso popolnoma doseženi (a so lahko zaželene).

### Motivacija

Ker bodo zahteve glede kakovosti močno vplivale na arhitekturne odločitve, bi morali vedeti, katere kakovosti so za vaše deležnike resnično pomembne, na konkreten in merljiv način.

### Dodatne informacije

Oglejte si obsežni model kakovosti Q42 na https://quality.arc42.org.

## 10.1 Pregled zahtev glede kakovosti

### Vsebina

Pregled ali povzetek zahtev glede kakovosti.

### Motivacija

Pogosto naletimo na desetine (ali celo stotine) podrobnih zahtev glede kakovosti. V tem pregledovalnem razdelku poskusite povzeti, npr. z opisom kategorij ali tem (kot predlagata ISO 25010:2023 ali Q42

Če so ti povzetki že dovolj natančni, specifični in merljivi, lahko razdelek 10.2 preskočite.

### Oblika

Uporabite preprosto tabelo, v kateri vsaka vrstica vsebuje kategorijo ali temo in kratek opis zahteve glede kakovosti. Lahko pa uporabite miselni vzorec za strukturiranje teh zahtev glede kakovosti.

V literaturi je opisana tudi zamisel drevesa kakovostnih atributov, ki kot koren postavi splošni pojem »kakovost« in uporablja drevesno natančnejšo razdelitev pojma »kakovost«. [Bass+21] je v ta namen uvedel izraz »Quality Attribute Utility Tree«.

## 10.2 Scenariji kakovosti

### Vsebina

Scenariji kakovosti konkretizirajo zahteve glede kakovosti in omogočajo odločitev, ali so izpolnjene (v smislu meril sprejemljivosti). Poskrbite, da so vaši scenariji specifični in merljivi.

Zlasti uporabni sta dve vrsti scenarijev:

- Scenariji uporabe (imenovani tudi aplikacijski scenariji ali scenariji primerov uporabe)
  opisujejo odziv sistema med izvajanjem na določen dražljaj. Sem spadajo tudi
  scenariji, ki opisujejo učinkovitost ali zmogljivost sistema.
  Primer: Sistem se odzove na zahtevo uporabnika v eni sekundi.

- Scenariji sprememb opisujejo želeni učinek spremembe ali razširitve
  sistema ali njegovega neposrednega okolja. Primer: Izvede se dodatna funkcionalnost
  ali se spremenijo zahteve za kakovostni atribut, merita pa se napor ali trajanje spremembe.

### Oblika

Tipične informacije za podrobne scenarije vključujejo naslednje:

V kratki obliki (priljubljeni v modelu Q42):

- Kontekst/ozadje: Kakšen sistem ali komponenta, kakšno je okolje ali stanje?

- Vir/dražljaj: Kdo ali kaj sproži vedenje, odziv ali dejanje.

- Metrika/merila sprejemljivosti: Odziv, ki vključuje mero ali metriko

Dolga oblika scenarijev (priljubljena pri SEI in [Bass+21]) je podrobnejša in vključuje naslednje informacije:

- ID scenarija: Enolični identifikator scenarija.

- Ime scenarija: Kratko, opisno ime scenarija.

- Vir: Entiteta (uporabnik, sistem ali dogodek), ki sproži scenarij.

- Dražljaj: Sprožilni dogodek ali pogoj, ki ga mora sistem obravnavati.

- Okolje: Operativni kontekst ali pogoj, v katerem sistem doživi dražljaj.

- Artefakt: Gradniki ali drugi elementi sistema, na katere dražljaj vpliva.

- Odziv: Izid ali vedenje, ki ga sistem izkaže kot reakcijo na dražljaj.

- Mera odziva: Merila ali metrika, po kateri se odziv sistema ovrednoti.

### Glejte tudi

Od januarja 2023 arc42 ponuja pragmatičen model kakovosti, ki predlaga
označevanje zahtev glede kakovosti s ključniki ali oznakami, kot so #flexible, #efficient,
#usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Tveganja in tehnični dolg

Znana tehnična tveganja ali tehnični dolg. Kakšni potencialni problemi obstajajo znotraj sistema ali okoli njega? Kaj razvojni ekipi povzroča nelagodje?

### Vsebina

Seznam ugotovljenih tehničnih tveganj ali tehničnih dolgov, razvrščen po prednosti

### Motivacija

»Upravljanje tveganj je projektno vodenje za odrasle« (Tim Lister, Atlantic Systems Guild.)

To naj bo vaše vodilo za sistematično odkrivanje in vrednotenje tveganj in tehničnih dolgov v arhitekturi, ki ju bodo potrebovali deležniki iz vodstva (npr. projektni vodje, lastniki izdelkov) kot del celotne analize tveganj in načrtovanja ukrepov.

### Oblika

Seznam tveganj in/ali tehničnih dolgov, verjetno vključno s predlaganimi ukrepi za zmanjšanje, ublažitev ali izogibanje tveganjem ali zmanjšanje tehničnih dolgov.
