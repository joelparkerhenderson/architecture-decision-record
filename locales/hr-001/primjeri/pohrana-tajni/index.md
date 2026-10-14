# Pohrana tajni

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Sažetak


### Problem

Moramo pohranjivati tajne, poput lozinki, privatnih ključeva, tokena za autentifikaciju itd.

Neke su tajne usmjerene na korisnika. Na primjer, naš programer želi moći koristiti svoj mobilni telefon za pronalaženje lozinke za uslugu.

Neke su tajne usmjerene na sustav. Na primjer, naš cjevovod kontinuirane isporuke mora moći pronaći vjerodajnice za naš cloud hosting.


### Odluka

Bitwarden za tajne usmjerene na korisnika

Vault by HashiCorp za tajne usmjerene na sustav.


### Status

Odlučeno. Otvoreni smo za nove alternative kako se pojave.


## Pojedinosti


### Pretpostavke

Za ovu svrhu i naše trenutačno stanje cijenimo praktičnost usmjerenu na korisnika, poput upotrebljivih mobilnih aplikacija.

  * Želimo osigurati brz i jednostavan pristup u pokretu, primjerice za programera koji obavlja dežurno inženjerstvo pouzdanosti sustava.

  * Želimo moći dijeliti neke tajne među odabranim osobama, primjerice timom.

Ne pokušavamo rješavati za jednog pružatelja, poput pohrane svih tajni isključivo na Amazonu, Azureu ili Googleu.

Ne želimo ad hoc pristupe poput „zapamti“ ili „zapiši na bilješku“ ili „smisli vlastiti način pohrane“.

Naš sigurnosni model za ovu svrhu u redu je s korištenjem cijenjenih COTS dobavljača, poput SaaS alata za upravljanje lozinkama.


### Ograničenja

Sada želimo nešto jednostavno, tj. bez potrebe za pisanjem koda, bez potrebe za instaliranjem poslužitelja, bez potrebe za velikom obvezom, bez potrebe za standardizacijom svih.


### Pozicije

Razmatrali smo:

1. Gotove upravitelje lozinki usmjerene na korisnika: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG itd.

2. COTS upravitelje lozinki usmjerene na sustav: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Pristupe usmjerene na dijeljenje: korištenje zajedničkog Google dokumenta, zajedničkog Slack kanala, zajedničke mrežne mape itd.

4. Niskotehnološke ad hoc pristupe, poput pamćenja, pisanja bilješke ili oslanjanja na to da svaki korisnik smisli vlastiti pristup.


### Argument

Bitwarden, LastPass, 1Password i Dashlane svi su komercijalni gotovi proizvodi.

  * Slične vrste značajki za korisnike, timove, organizacije itd.

  * Desktop mogućnosti za Windows i Mac te mobilne mogućnosti za Android i iOS.

  * Proširenja za preglednike Chrome i Firefox za automatsko popunjavanje obrazaca itd.

Bitwarden ima dvije prednosti pred ostalima:

  * Bitwarden je otvorenog koda, što znači da se sigurnost može pregledavati od strane kolega, a tvrtku također široko cijene programeri usmjereni na sigurnost.

  * Anegdote softverskih radnika opisuju značajnu preferenciju Bitwardena pred ostalima.

Tipičan dobar članak: https://jcs.org/2017/11/17/bitwarden

Tipična stranica za glasanje usporedbe jedan pored drugog: https://stackshare.io/stackups/bitwarden-vs-dashlane

Odgađamo KeyPass, pass, GPG itd. jer postoji dodatna složenost. Sva ta rješenja izgledaju kao dobra rješenja za tehničke korisnike. GPG izgleda osobito dobro za tehničke korisnike koji žele mogućnosti usmjerene na naredbe među sustavima.

Odgađamo KMS jer ima zaključavanje kod jednog pružatelja.

Za potrebe usmjerene na sustav biramo Vault jer su recenzije nevjerojatno pozitivne i jer HashiCorp ima izvrsnu povijest vrhunskog softvera i podrške.

Stavljamo veto na pristupe dijeljenja, poput putem zajedničkih dokumenata, zajedničkih kanala, zajedničkih mrežnih mapa itd. Oni ne pružaju sigurnosne kvalitete koje želimo.

Stavljamo veto na ad hoc niskotehnološke pristupe jer se svi slažemo da to nije dugoročan put naprijed.


### Implikacije

Programeri će možda morati pratiti tajne na dva mjesta: Bitwarden za pristup usmjeren na korisnika i Vault za pristup usmjeren na sustav.


## Povezano


### Povezane odluke

Odluka o tome koji CI/CD poslužitelj koristiti mora uključivati dokaz sposobnosti pristupa tajnama.

Morat ćemo odlučiti kako upravljati tajnama, u smislu politika, rotacija, organizacija itd.


### Povezani zahtjevi

Tajne će imati povezane zahtjeve za usklađenost, reviziju te uvođenje/izlazak zaposlenika u HR-u.


### Povezani artefakti

Očekujemo da bismo mogli izvesti neke tajne u varijable okruženja.


### Povezana načela

Lako reverzibilno.

Lako paralelno, tj. lako je koristiti razne upravitelje lozinki.

Jeftino za isprobati, tj. postoji besplatno probno razdoblje i nema obveze.


## Bilješke

Bilješke o vrednovanju ovdje. Sve su bilješke javni komentari na raznim devops forumima.


### Vault by HashiCorp

Vault je upravo ono što ovdje želite. 

Ipak, nemojte Vault samo baciti u produkciju, prvo ga podignite u testnom okruženju, jer HashiCorpova dokumentacija može biti prilično manjkava iako su njihovi proizvodi nevjerojatni.

Vrlo strma krivulja učenja i nije trivijalno podići ga. 

Početno postavljanje je pomalo mučno. Ipak, itekako se isplati, a zajednica ga podržava dovoljno da se snađete.

Užasna dokumentacija, ali na internetu ima mnogo vodiča ljudi koji su ga postavljali i ako ih nekoliko spojite imat ćete radnu postavu.

Početno postavljanje zahtijevalo je petljanje s njihovim helm chartovima (vault i consul). Iako tehnički možete koristiti mnoge druge pozadine, stvarno, stvarno to ne preporučujem. Pozadina/consul može biti sićušan ako nemate puno podataka za pohranu.

Definitivno se naviknite na korištenje CLI-ja, jer je GUI više proof-of-concept/reklamni portal za njihovo enterprise izdanje.

Činjenica da ga ne možete jednostavno „napuniti“ je muka. Na primjer, ako imate 5 polja, morate ručno dodati svako polje za svaku stavku. Dakle, nije kao da unaprijed definirate polja za određenu kategoriju i popunite ta polja za sve stavke u toj kategoriji, više je kao „sve generirate svaki put“, što je (po mom mišljenju) velika gnjavaža.

Možda biste trebali pogledati i goldfish kao UI povrh vaulta. Prilično olakšava pridobivanje vašeg tima. Imaju i demo. 1. Postavite consul. 2. Postavite vault koji pokazuje na consul. 3. Postavite goldfish koji pokazuje na vault. 3. Postavite neki cron posao za pokretanje consul snapshota za sigurnosne kopije.



### LastPass

LastPass Teams. Koristimo ga, ima prilagođene predloške, ACL, ništa ne nedostaje po mom mišljenju.

Implementirao sam LastPass u svojoj organizaciji i dajem mu C+/B-. Najveći problem u posljednje vrijeme je nedostatak pouzdanosti. U posljednjih 90 dana bilo je više sati kada su trezori bili prisilno prebačeni u offline način rada. To nije idealno za moju organizaciju jer imamo doslovno 4 000+ lozinki pohranjenih u 20+ zajedničkih mapa. Kao što možete zamisliti, s toliko lozinki barem se nekoliko dnevno ažurira ili dodaje. Imamo plan oporavka od katastrofe (DR) ako problemi traju dulje od sat-dva: skripta svake noći potpisuje i šifrira CSV ispis trezora koji se može uvesti u keepass.

LastPass je imao neprijavljene oscilacije degradirane usluge: prijava „radi“, ali ne povlači stranice, nasumične značajke u administratorskom panelu su pokvarene i ne dijele ispravno ključeve za nove zajedničke mape najviše razine. Imam posebnog korisnika za „key push“/sigurnosnu kopiju koji je u svakoj grupi. Prijava kao taj korisnik obično će riješiti sve probleme s dijeljenjem ključeva, ali ne kada je usluga degradirana bez obzira na to što kaže stranica statusa...

Za integraciju može biti jednostavno ako imate ispravne ACL-ove s modelom najmanjih privilegija, npr. ako korisnik ima čitanje i pisanje te samo čitanje na stavci ili mapi, dobiva samo dopuštenja samo za čitanje. Nažalost, ACL-ovi moje organizacije nisu najbolji pa sam na kraju koristio JSON provisioning API i ~500 redaka Pythona jer se ovisna priroda naših stotina ACL-ova ne preslikava dobro na model najmanjih privilegija. Na kraju sam dohvatio sve ACL-ove u kojima je korisnik bio i napravio nešto poput obilaska ovisnosti.

Ako je vaša struktura ACL-ova ili grupa već izgrađena s modelom najmanjih privilegija na umu, alat za sinkronizaciju AD/LDAP za Windows dobro će raditi.

Obratite se njihovom prodajnom timu i mogu vam osigurati dulje Enterprise probno razdoblje. Pobrinite se da u potpunosti razumijete njegova ograničenja prije nego što se odlučite. Imali smo priličan broj boli rasta, ali osim ispada ili oštećenja na strani poslužitelja bilo je nevjerojatno glatko.


### Bitwarden

Bitwarden ima dobre alate oko sebe (WebUI, CLI, mobilni, desktop). Može se samostalno hostirati i prilično ga je lako postaviti. Prilično dobra dokumentacija i alat koji preporučuje PrivacyTools.


### EnvKey

https://www.envkey.com/ je SaaS. Zaista jednostavan za implementaciju, integraciju i upravljanje.

Značajke:

  * Zaštita API ključeva i vjerodajnica.

  * Održavanje konfiguracije sinkroniziranom svugdje.

  * Pametno, end-to-end šifrirano upravljanje konfiguracijom i tajnama. 

  * Sprječavanje nesigurnog dijeljenja i raširenosti konfiguracije. 

  * Integracija u nekoliko minuta.

Mogućnosti:

  * Upravljanje konfiguracijom i razinama pristupa za sve vaše aplikacije, okruženja i timove na jednom mjestu.

  * Konfiguriranje bilo kojeg razvojnog ili poslužiteljskog okruženja samo jednom varijablom okruženja.

Prednosti:

  * Dobra početna stranica.

  * Jasna vrijednosna ponuda.

  * Vizualno izvrsna web aplikacija.

  * Vrhunski primjeri podataka, npr. Algolia, AWS, Datadog, GitHub, Stripe itd.

  * Razgovarao sam s osnivačem 30 minuta o tvrtki, UI-ju itd. Dane zvuči dobro informirano, iskreno o prednostima/nedostacima i kao održiv partner.

  * Tvrtka je u biti tipična tvrtka iz Y Combinatora s 1 osnivačem. Prikupila je 120 tisuća USD u 2018-01.

  * Fokus je na dosezanju enterprise značajki, osobito prelasku s EnvKey cloud hostinga na on-prem ili BYOC.

  * Potencijalni put naprijed: početi s EnvKeyem radi jednostavnosti uporabe, a zatim (ili paralelno) dodati Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant je usluga upravljanja tajnama otvorenog koda koja pruža korisniku prijateljsku pohranu i pristup tajnama na siguran način, od programera u Lyftu.

KMS autentifikacija: Confidant rješava problem kokoši i jajeta pri autentifikaciji korištenjem AWS KMS-a i IAM-a kako bi omogućio IAM ulogama generiranje sigurnih autentifikacijskih tokena koje Confidant može provjeriti. Confidant također upravlja KMS grantovima za vaše IAM uloge, što IAM ulogama omogućuje generiranje tokena koji se mogu koristiti za autentifikaciju među uslugama ili za prosljeđivanje šifriranih poruka među uslugama.

Šifriranje verzioniranih tajni u mirovanju: Confidant pohranjuje tajne samo dodavanjem u DynamoDB, generirajući jedinstveni KMS ključ podataka za svaku reviziju svake tajne, koristeći simetričnu autentificiranu kriptografiju Fernet.

Korisniku prijateljsko web sučelje za upravljanje tajnama: Confidant pruža AngularJS web sučelje koje krajnjim korisnicima omogućuje jednostavno upravljanje tajnama, preslikavanjem tajni na usluge i poviješću promjena.


### Devolutions Password Server

https://server.devolutions.net/

Osigurajte, upravljajte i nadzirite pristup privilegiranim računima i sesijama.

Sveobuhvatan, visoko zaštićen trezor lozinki koji vam omogućuje kontrolu pristupa vašim privilegiranim računima, a istodobno poboljšava ukupnu vidljivost mreže za sistem administratore i pruža besprijekorno iskustvo za krajnje korisnike.

Značajke: centralizirani organizacijski trezor lozinki, privatni trezor specifičan za korisnika, upravitelj lozinki, ubrizgavanje vjerodajnica,
integracija s Active Directoryjem, kontrola pristupa temeljena na ulogama, dvofaktorska autentifikacija, spremnost za enterprise, IP ograničenja, mogućnosti upravljanja, automatski generator lozinki, pristup mobilnom aplikacijom, povijest lozinki, izvješća o pristupu, upozorenja e-poštom.

  * podržava šifriranje podataka

  * podržava više shema autentifikacije uključujući LDAP, O365 i lokalne korisnike UZ podršku za MFA iz više izvora

  * više repozitorija/trezora s finim kontrolama pristupa za više timova

  * moderno web UI

  * privatni trezori vjerodajnica i veza za osobne vjerodajnice/veze

  * mobilne aplikacije za iOS/Android

  * revizijski zapisnici za svaki unos, tko/što/kada s neobaveznim pitanjem zašto pristupaju

  * prilagodljivi predlošci (iako izvorno podržavaju stotine vrsta veza)

  * mnoštvo drugih značajki i tanki klijent za Windows/Mac (Remote Desktop Manager) s kojim možete sinkronizirati i koji uvelike proširuje mogućnosti... veze jednim klikom

  * cijena nije tako loša - do 15 korisnika košta 500 USD godišnje za password server


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Značajke on-premise verzije: 

  * Potpuna kontrola nad vašim end-to-end sigurnosnim sustavima i infrastrukturom

  * Implementacija softvera unutar vašeg on-premise podatkovnog centra ili vaše vlastite instance virtualnog privatnog clouda

  * Ispunjavanje zakonskih i regulatornih obveza koje zahtijevaju da svi podaci i sustavi borave on premise

Značajke cloud verzije:

  * Model softvera kao usluge omogućuje vam prijavu i početak odmah

  * Elastična skalabilnost kako rastete

  * Kontrole i redundanciju isporučuje Azure sa SLA-om dostupnosti od 99,9 %

Povratne informacije korisnika:

  * Nekad smo koristili taj proizvod. Bilo ga je vrlo lako zaobići, a pravila rade samo za pametne ljude. Lijeni ili glupi korisnici mogu ga lako pokvariti u timskom području. Cijene su pregovorive kad razgovarate s njima.

  * Možete ga pokrenuti pomoću SQL expressa i računala s Win 7. 

  * Jeftin.
