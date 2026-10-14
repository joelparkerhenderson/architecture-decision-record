# Predložak zapisa odluke – arc42

<https://arc42.org/overview>

## 1. Uvod i ciljevi

Kratak opis zahtjeva, pokretačkih snaga, izvadak (ili sažetak) zahtjeva.
Tri (najviše pet) ciljeva kvalitete za arhitekturu koji imaju najviši prioritet
za glavne dionike. Tablica važnih dionika s njihovim očekivanjima
u pogledu arhitekture.

## 1.1 Pregled zahtjeva

### Sadržaj

Kratak opis funkcionalnih zahtjeva, pokretačkih snaga, izvadak (ili
sažetak) zahtjeva. Poveznice na (nadamo se postojeće) dokumente
zahtjeva, s informacijama gdje ih pronaći. 

### Motivacija

Iz perspektive krajnjih korisnika sustav se stvara ili mijenja kako bi
poboljšao podršku poslovnoj aktivnosti i/ili poboljšao kvalitetu. 

### Oblik

Kratak tekstualni opis, vjerojatno u tabličnom formatu slučajeva uporabe. Ako dokumenti
zahtjeva postoje, ovaj pregled treba upućivati na te dokumente.

Neka ti izvaci budu što kraći. Uravnotežite čitljivost ovog dokumenta
s potencijalnom redundancijom u odnosu na dokumente zahtjeva. 

## 1.2 Ciljevi kvalitete

### Sadržaj

Tri (najviše pet) ciljeva kvalitete za arhitekturu čije je ispunjenje
od najveće važnosti za glavne dionike. Doista mislimo na ciljeve kvalitete
za arhitekturu. Nemojte ih miješati s ciljevima projekta. Oni nisu
nužno identični. Norma ISO 25010 pruža dobar pregled
potencijalnih tema od interesa.

### Motivacija

Trebali biste znati ciljeve kvalitete svojih najvažnijih dionika jer
oni utječu na temeljne arhitekturne odluke. Budite vrlo
konkretni u pogledu tih kvaliteta, izbjegavajte modne riječi. Ako vi kao arhitekt ne
znate kako će se kvaliteta vašeg rada ocjenjivati …

### Oblik

Tablica s najvažnijim ciljevima kvalitete i konkretnim scenarijima, poredana po prioritetima.

## 1.3 Dionici

### Sadržaj

Eksplicitan pregled dionika sustava, tj. svih osoba, uloga ili
organizacija koje

- trebaju znati arhitekturu

- trebaju biti uvjerene u arhitekturu

- moraju raditi s arhitekturom ili s kodom

- trebaju dokumentaciju arhitekture za svoj rad

- moraju donositi odluke o sustavu ili njegovu razvoju

### Motivacija

Trebali biste poznavati sve strane uključene u razvoj sustava ili na koje sustav utječe.
Inače možete doživjeti neugodna iznenađenja kasnije u procesu
razvoja. Ti dionici određuju opseg i razinu detalja vašeg
rada i njegovih rezultata.

### Oblik

Tablica s nazivima uloga, imenima osoba i njihovim očekivanjima u pogledu
arhitekture i njezine dokumentacije.

## 2. Ograničenja

Sve što ograničava timove u odlukama o dizajnu i implementaciji ili odlukama
o povezanim procesima. Ponekad mogu nadilaziti pojedinačne sustave i
vrijede za cijele organizacije i tvrtke.

### Sadržaj

Svaki zahtjev koji ograničava softverske arhitekte u njihovoj slobodi odluka o dizajnu
i implementaciji ili odluka o procesu razvoja. Ta
ograničenja ponekad nadilaze pojedinačne sustave i vrijede za cijele
organizacije i tvrtke.

### Motivacija

Arhitekti bi trebali točno znati gdje su slobodni u svojim odlukama o dizajnu i
gdje se moraju pridržavati ograničenja. Ograničenja se uvijek moraju uzeti u obzir;
no ona mogu biti podložna pregovorima.

### Oblik

Jednostavne tablice ograničenja s objašnjenjima. Po potrebi ih možete podijeliti
na tehnička ograničenja, organizacijska i politička ograničenja te
konvencije (npr. smjernice za programiranje ili verzioniranje, dokumentaciju ili konvencije imenovanja)

## 3. Kontekst i opseg

Razgraničava vaš sustav od njegovih (vanjskih) komunikacijskih partnera (susjedni
sustavi i korisnici). Određuje vanjska sučelja. Prikazuje se iz
poslovne/domenske perspektive (uvijek) ili tehničke perspektive (neobavezno)

### Sadržaj

Opseg i kontekst sustava – kako i ime kaže – razgraničava vaš sustav (tj.
vaš opseg) od svih njegovih komunikacijskih partnera (susjedni sustavi i korisnici,
tj. kontekst vašeg sustava). Time određuje vanjska sučelja.

Ako je potrebno, razlikujte poslovni kontekst (domenski specifični ulazi i
izlazi) od tehničkog konteksta (kanali, protokoli, hardver).

### Motivacija

Domenska i tehnička sučelja prema komunikacijskim partnerima
među najkritičnijim su aspektima vašeg sustava. Pobrinite se da ih u potpunosti
razumijete.

### Oblik

- Razni kontekstni dijagrami

- Popisi komunikacijskih partnera i njihovih sučelja.

## 3.1 Poslovni kontekst

### Sadržaj

Specifikacija svih komunikacijskih partnera (korisnici, IT sustavi, …) s
objašnjenjima domenski specifičnih ulaza i izlaza ili sučelja. Po želji možete
dodati domenski specifične formate ili komunikacijske protokole.

### Motivacija

Svi dionici trebali bi razumjeti koji se podaci razmjenjuju s okolinom
sustava.

### Oblik

Sve vrste dijagrama koji prikazuju sustav kao crnu kutiju i određuju domenska
sučelja prema komunikacijskim partnerima.

Alternativno (ili dodatno) možete koristiti tablicu. Naslov tablice je
naziv vašeg sustava, tri stupca sadrže naziv komunikacijskog
partnera, ulaze i izlaze.

## 3.2 Tehnički kontekst

### Sadržaj

Tehnička sučelja (kanali i prijenosni mediji) koja povezuju vaš sustav s
njegovom okolinom. Uz to preslikavanje domenski specifičnih ulaza/izlaza na
kanale, tj. objašnjenje koji ulaz/izlaz koristi koji kanal.

### Motivacija

Mnogi dionici donose arhitekturne odluke na temelju tehničkih sučelja
između sustava i njegova konteksta. Osobito projektanti infrastrukture ili hardvera odlučuju o tim tehničkim sučeljima.

### Oblik

Npr. UML dijagram razmještaja koji opisuje kanale prema susjednim sustavima, zajedno
s tablicom preslikavanja koja prikazuje odnose između kanala i
ulaza/izlaza.

## 4. Strategija rješenja

Sažetak temeljnih odluka i strategija rješenja koje oblikuju
arhitekturu. Može uključivati tehnologiju, dekompoziciju najviše razine, pristupe
postizanju ključnih ciljeva kvalitete i relevantne organizacijske odluke.

### Sadržaj

Kratak sažetak i objašnjenje temeljnih odluka i strategija rješenja koje oblikuju arhitekturu sustava. To uključuje

- tehnološke odluke

- odluke o dekompoziciji sustava najviše razine, npr. upotreba arhitekturnog obrasca ili obrasca dizajna

- odluke o tome kako postići ključne ciljeve kvalitete

- relevantne organizacijske odluke, npr. odabir razvojnog procesa ili delegiranje određenih zadataka trećim stranama.

### Motivacija

Te odluke čine kamen temeljac vaše arhitekture. One su temelj
za mnoge druge detaljne odluke ili pravila implementacije.

### Oblik

Neka objašnjenje tih ključnih odluka bude kratko.

Obrazložite što ste odlučili i zašto ste tako odlučili, na temelju
opisa problema, ciljeva kvalitete i ključnih ograničenja. Uputite na pojedinosti u
sljedećim odjeljcima (odjeljak 5 za strukturne pojedinosti, odjeljak 8 za
međusektorske koncepte).

Možete koristiti popis pristupa rješenju ili tablicu.

## 5. Pogled građevnih blokova

Statička dekompozicija sustava, apstrakcije izvornog koda, prikazane kao
hijerarhija bijelih kutija (koje sadrže crne kutije), do odgovarajuće razine
detalja.

### Sadržaj

Pogled građevnih blokova prikazuje statičku dekompoziciju sustava na
građevne blokove (module, komponente, podsustave, klase, sučelja, pakete,
biblioteke, okvire, slojeve, particije, razine, funkcije, makroe, operacije,
strukture podataka, …) kao i njihove ovisnosti (odnose, asocijacije,
…)

Ovaj je pogled obvezan za svaku arhitekturnu dokumentaciju. Po analogiji s
kućom, ovo je tlocrt.

### Motivacija

Zadržite pregled svog izvornog koda tako da njegovu strukturu učinite razumljivom
putem apstrakcije.

To vam omogućuje komunikaciju s dionicima na apstraktnoj razini
bez otkrivanja pojedinosti implementacije.

### Oblik

Pogled građevnih blokova je hijerarhijska zbirka crnih kutija i bijelih
kutija (vidi sliku u nastavku) i njihovih opisa.

## 5.1 Bijela kutija cijelog sustava

Ovdje opisujete dekompoziciju cijelog sustava pomoću sljedećeg predloška bijele kutije. Sadrži

- dijagram pregleda

- motivaciju za dekompoziciju

- opise sadržanih građevnih blokova kao crnih kutija. Za njih nudimo alternative:

  - koristite jednu tablicu za kratak i pragmatičan pregled svih sadržanih građevnih blokova i njihovih sučelja

  - koristite popis opisa građevnih blokova kao crnih kutija prema predlošku crne kutije (vidi dolje). Ovisno o vašem odabiru alata, taj popis mogu biti potpoglavlja (u tekstualnim datotekama), podstranice (u wikiju) ili ugniježđeni elementi (u alatu za modeliranje).

  - (neobavezno:) važna sučelja koja nisu objašnjena u predlošcima crne kutije građevnog bloka, ali su vrlo važna za razumijevanje bijele kutije.

Budući da postoji toliko načina za određivanje sučelja, ne nudimo poseban predložak za njih.

U najboljem slučaju proći ćete s primjerima ili jednostavnim potpisima.

## 5.2 Razina 2

Ovdje možete odrediti unutarnju strukturu (nekih) građevnih blokova s razine 1
kao bijelih kutija.

Morate odlučiti koji su građevni blokovi vašeg sustava dovoljno važni da
opravdaju tako detaljan opis. Molimo, preferirajte relevantnost umjesto cjelovitosti.
Odredite važne, iznenađujuće, rizične, složene ili promjenjive građevne blokove. Izostavite
normalne, jednostavne, dosadne ili standardizirane dijelove vašeg sustava

### 5.2.1 Bijela kutija za građevni blok 1

Određuje unutarnju strukturu građevnog bloka 1.

Koristite predložak bijele kutije (vidi gore).

## 6. Pogled izvođenja

Ponašanje građevnih blokova kao scenariji, koji pokrivaju važne slučajeve uporabe ili
značajke, interakcije na kritičnim vanjskim sučeljima, rad i
administraciju te ponašanje u slučaju pogrešaka i iznimaka.

### Sadržaj

Pogled izvođenja opisuje konkretno ponašanje i interakcije građevnih blokova sustava u obliku scenarija iz sljedećih područja:

- važni slučajevi uporabe ili značajke: kako ih građevni blokovi izvršavaju?

- interakcije na kritičnim vanjskim sučeljima: kako građevni blokovi surađuju s korisnicima i susjednim sustavima?

- rad i administracija: pokretanje, podizanje, zaustavljanje

- scenariji pogrešaka i iznimaka

Napomena: Glavni kriterij za odabir mogućih scenarija (nizovi, tijekovi rada) je njihova arhitekturna relevantnost. Nije važno opisati velik broj scenarija. Radije dokumentirajte reprezentativan odabir.

### Motivacija

Trebali biste razumjeti kako (instance) građevnih blokova vašeg sustava obavljaju svoj posao i komuniciraju tijekom izvođenja. Scenarije ćete uglavnom bilježiti u svojoj dokumentaciji kako biste arhitekturu priopćili dionicima koji su manje voljni ili sposobni čitati i razumjeti statičke modele (pogled građevnih blokova, pogled razmještaja).

### Oblik

Postoje mnoge notacije za opisivanje scenarija, npr.


- numerirani popis koraka (na prirodnom jeziku)

- dijagrami aktivnosti ili dijagrami toka

- sekvencijski dijagrami

- BPMN ili EPC-ovi (lanci događajnih procesa)

- konačni automati

- itd.

## 6.n Scenarij izvođenja n (1, 2, 3 itd.)

Umetnite dijagram izvođenja ili tekstualni opis scenarija.

Umetnite opis značajnih aspekata interakcija između instanci građevnih blokova prikazanih na ovom dijagramu.

## 7. Pogled razmještaja

Tehnička infrastruktura s okruženjima, računalima, procesorima, topologijama.
Preslikavanje (softverskih) građevnih blokova na elemente infrastrukture.

### Sadržaj

Pogled razmještaja opisuje:

- tehničku infrastrukturu korištenu za izvršavanje vašeg sustava, s elementima infrastrukture
  poput zemljopisnih lokacija, okruženja, računala, procesora,
  kanala i mrežnih topologija te drugih elemenata infrastrukture i

- preslikavanje (softverskih) građevnih blokova na te elemente infrastrukture.

Sustavi se često izvršavaju u različitim okruženjima, npr. razvojno
okruženje, testno okruženje, produkcijsko okruženje. U takvim slučajevima trebali
biste dokumentirati sva relevantna okruženja.

Pogled razmještaja osobito dokumentirajte kada se vaš softver izvršava kao
distribuirani sustav s više od jednog računala, procesora, poslužitelja ili kontejnera
ili kada dizajnirate i gradite vlastite hardverske procesore i čipove.

Iz softverske perspektive dovoljno je zabilježiti one elemente
infrastrukture koji su potrebni za prikaz razmještaja vaših građevnih blokova.
Hardverski arhitekti mogu ići dalje i opisati infrastrukturu do bilo koje razine
detalja koju trebaju zabilježiti. 

### Motivacija

Softver ne radi bez hardvera. Ta temeljna infrastruktura može i
hoće utjecati na vaš sustav i/ili neke međusektorske koncepte. Stoga
trebate poznavati infrastrukturu.

### Oblik

Možda je dijagram razmještaja najviše razine već sadržan u odjeljku 3.2. kao tehnički kontekst s vašom vlastitom infrastrukturom kao JEDNOM crnom kutijom. U ovom odjeljku zumirat ćete tu crnu kutiju pomoću dodatnih dijagrama razmještaja.

- UML nudi dijagrame razmještaja za izražavanje tog pogleda. Koristite ih, vjerojatno s ugniježđenim dijagramima, kada je vaša infrastruktura složenija.

- Kada vaši (hardverski) dionici preferiraju druge vrste dijagrama umjesto
  UML dijagrama razmještaja, dopustite im da koriste bilo koju vrstu koja može prikazati čvorove i
  kanale infrastrukture.

## 7.1 Infrastruktura razina 1

Opišite (obično kombinacijom dijagrama, tablica i teksta):

- raspodjelu vašeg sustava na više lokacija, okruženja, računala, procesora, .. kao i fizičke veze među njima

- važno opravdanje ili motivaciju za ovu strukturu razmještaja

- značajke kvalitete i/ili performansi infrastrukture

- preslikavanje softverskih artefakata (građevnih blokova) na elemente infrastrukture

Za više okruženja ili alternativnih razmještaja kopirajte taj odjeljak arc42 za sva relevantna okruženja. **

## 7.2 Infrastruktura razina 2

Ovdje možete uključiti unutarnju strukturu (nekih) elemenata infrastrukture s infrastrukture razine 1.

Molimo kopirajte strukturu s razine 1 za svaki odabrani element.

## 8. Međusektorski koncepti

Opći, glavni propisi i pristupi rješenju relevantni u više
dijelova (→ međusektorski) sustava. Koncepti su često povezani s više
građevnih blokova. Uključuju različite teme poput domenskih modela, arhitekturnih
obrazaca i stilova, pravila za upotrebu određene tehnologije i pravila implementacije.

### Sadržaj

Ovaj odjeljak opisuje međusektorske koncepte (prakse, obrasce, propise
ili ideje rješenja). Takvi su koncepti često povezani s više građevnih blokova.
Mogu uključivati mnoge različite teme.

### Motivacija

Koncepti čine temelj konceptualnog integriteta (dosljednosti, homogenosti)
arhitekture. Stoga su važan doprinos postizanju unutarnjih
kvaliteta vašeg sustava.

Ovo je mjesto u predlošku koje smo osigurali za koherentnu specifikaciju
takvih koncepata.

Mnogi od tih koncepata odnose se na nekoliko vaših građevnih blokova ili na njih utječu.

### Oblik

Oblik može varirati:

- konceptualni dokumenti s bilo kakvom strukturom

- primjeri implementacije, osobito za tehničke koncepte

- međusektorski izvaci modela ili scenariji pomoću notacija arhitekturnih pogleda

### Struktura ovog odjeljka

Odaberite samo najpotrebnije teme za vaš sustav i svakoj dodijelite naslov razine 2 u ovom odjeljku (npr. 8.1, 8.2 itd.).

- NE POKUŠAVAJTE pokriti sve teme iz spomenutog dijagrama.

### Pozadina

Neke teme unutar sustava često se tiču više građevnih blokova, hardverskih
elemenata ili razvojnih procesa. Možda je lakše komunicirati ili dokumentirati
takve međusektorske teme na središnjem mjestu, umjesto da ih ponavljate u
opisu dotičnih građevnih blokova, hardverskih elemenata ili
razvojnih procesa.

Određeni koncepti mogu se tiče svih elemenata sustava, drugi mogu biti
relevantni samo za neke.

## 9. Arhitekturne odluke

Važne, skupe, kritične, velike ili rizične arhitekturne odluke
uključujući obrazloženja.

### Sadržaj

Važne, skupe, velike ili rizične arhitekturne odluke uključujući
obrazloženja. Pod „odlukama“ mislimo na odabir jedne alternative na temelju zadanih
kriterija.

Molimo, upotrijebite svoju prosudbu da odlučite treba li arhitekturnu odluku
dokumentirati ovdje u ovom središnjem odjeljku ili je bolje dokumentirati
lokalno (npr. unutar predloška bijele kutije jednog građevnog bloka). Izbjegavajte
redundantne tekstove. Uputite na odjeljak 4, gdje ste već zabilježili najvažnije
odluke svoje arhitekture.

### Motivacija

Dionici vašeg sustava trebali bi moći shvatiti i ponovno pratiti vaše
odluke.

### Oblik

- ADR (zapis arhitekturne odluke) za svaku važnu odluku

- popis ili tablica, poredani po važnosti i posljedicama ili

- detaljnije u obliku zasebnih odjeljaka po odluci

### Pozadina (o ADR-ovima)

Manje dijelove dokumentacije lakše je čitati, stvarati i održavati. Kada
je riječ o arhitekturnim odlukama, razvojni timovi često:

- znaju za odluku jer je vidljiva npr. u izvornom kodu, ali

- ne znaju motivaciju iza te odluke (vidi Nygard 2011)

Stoga biste trebali dokumentirati nekoliko važnih odluka zajedno s njihovom
motivacijom, razmišljanjem

### Naš prijedlog u vezi s odlukama

Vodite zbirku arhitekturno značajnih odluka, onih odluka koje
utječu na strukturu, značajke kvalitete, važne (osobito vanjske)
ovisnosti i sučelja ili tehnike izgradnje (zahvaljujući Michaelu
Nygardu na ovom prijedlogu).

## 10. Zahtjevi kvalitete

Zahtjevi kvalitete kao scenariji, sa stablom kvalitete koje daje pregled na visokoj razini.
Najvažniji ciljevi kvalitete trebali su biti opisani u odjeljku
1.2. (ciljevi kvalitete).

### Sadržaj

Ovaj odjeljak sadrži sve relevantne zahtjeve kvalitete.

Najvažniji od tih zahtjeva već su opisani u odjeljku
1.2. (ciljevi kvalitete), stoga ih ovdje treba samo referencirati. U ovom
odjeljku 10 trebali biste zabilježiti i zahtjeve kvalitete manje važnosti,
koji neće stvoriti visoke rizike ako nisu u potpunosti postignuti (ali mogu biti
poželjni).

### Motivacija

Budući da će zahtjevi kvalitete imati velik utjecaj na arhitekturne
odluke, trebali biste znati koje su kvalitete doista važne vašim
dionicima, na specifičan i mjerljiv način.

### Dodatne informacije

Pogledajte opsežan model kvalitete Q42 na https://quality.arc42.org.

## 10.1 Pregled zahtjeva kvalitete

### Sadržaj

Pregled ili sažetak zahtjeva kvalitete.

### Motivacija

Često nailazimo na desetke (ili čak stotine) detaljnih zahtjeva kvalitete.
U ovom pregledu pokušajte sažeti, npr. opisivanjem
kategorija ili tema (kako predlažu ISO 25010:2023 ili Q42

Ako su ti sažeti opisi već precizni, dovoljno specifični i
mjerljivi, možete preskočiti odjeljak 10.2.

### Oblik

Koristite jednostavnu tablicu u kojoj svaki redak sadrži kategoriju ili temu i kratak
opis zahtjeva kvalitete. Alternativno, možete koristiti mentalnu mapu
za strukturiranje tih zahtjeva kvalitete.

U literaturi je opisana i ideja stabla atributa kvalitete,
koje stavlja generički pojam „kvaliteta“ kao korijen i koristi stablasto
doradivanje pojma „kvaliteta“. [Bass+21] je u tu svrhu uveo pojam „Quality
Attribute Utility Tree“.

## 10.2 Scenariji kvalitete

### Sadržaj

Scenariji kvalitete čine zahtjeve kvalitete konkretnima i omogućuju odlučivanje jesu li
ispunjeni (u smislu kriterija prihvaćanja). Pobrinite se da su vaši
scenariji specifični i mjerljivi.

Dvije vrste scenarija osobito su korisne:

- Scenariji uporabe (nazivaju se i aplikacijski scenariji ili scenariji slučajeva uporabe)
  opisuju reakciju sustava tijekom izvođenja na određeni poticaj. To također
  uključuje scenarije koji opisuju učinkovitost ili performanse sustava.
  Primjer: Sustav reagira na korisnikov zahtjev u roku od jedne sekunde.

- Scenariji promjene opisuju željeni učinak izmjene ili proširenja
  sustava ili njegova neposrednog okruženja. Primjer: Implementira se dodatna funkcionalnost
  ili se mijenjaju zahtjevi za atribut kvalitete, a mjeri se napor
  ili trajanje promjene.

### Oblik

Tipične informacije za detaljne scenarije uključuju sljedeće:

U kratkom obliku (poželjnom u modelu Q42):

- Kontekst/Pozadina: Kakva vrsta sustava ili komponente, kakvo je okruženje ili situacija?

- Izvor/Poticaj: Tko ili što pokreće ili aktivira ponašanje, reakciju ili radnju.

- Metrika/Kriterij prihvaćanja: Odgovor koji uključuje mjeru ili metriku

Dugi oblik scenarija (poželjan za SEI i [Bass+21]) je detaljniji i uključuje sljedeće informacije:

- ID scenarija: Jedinstveni identifikator scenarija.

- Naziv scenarija: Kratak, opisni naziv scenarija.

- Izvor: Entitet (korisnik, sustav ili događaj) koji pokreće scenarij.

- Poticaj: Događaj ili uvjet koji aktivira i koji sustav mora obraditi.

- Okruženje: Operativni kontekst ili uvjet pod kojim sustav doživljava poticaj.

- Artefakt: Građevni blokovi ili drugi elementi sustava na koje poticaj utječe.

- Odgovor: Ishod ili ponašanje koje sustav pokazuje kao reakciju na poticaj.

- Mjera odgovora: Kriterij ili metrika prema kojoj se vrednuje odgovor sustava.

### Vidi također

Od siječnja 2023. arc42 pruža pragmatičan model kvalitete koji predlaže
označavanje zahtjeva kvalitete hashtagovima ili oznakama poput #flexible, #efficient,
#usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Rizici i tehnički dug

Poznati tehnički rizici ili tehnički dug. Koji potencijalni problemi postoje unutar ili
oko sustava? Zbog čega se razvojni tim osjeća jadno?

### Sadržaj

Popis utvrđenih tehničkih rizika ili tehničkih dugova, poredan po prioritetu

### Motivacija

„Upravljanje rizikom je upravljanje projektima za odrasle“ (Tim Lister, Atlantic
Systems Guild.)

To bi trebao biti vaš moto za sustavno otkrivanje i vrednovanje rizika i
tehničkih dugova u arhitekturi, što će trebati dionicima iz uprave
(npr. voditeljima projekata, vlasnicima proizvoda) kao dio cjelokupne analize
rizika i planiranja mjera.

### Oblik

Popis rizika i/ili tehničkih dugova, vjerojatno uključujući predložene mjere za
minimiziranje, ublažavanje ili izbjegavanje rizika ili smanjenje tehničkih dugova.
