## Zapis arhitekturne odluke: okvir za automatizaciju preglednika za E2E testiranje (Playwright ili Selenium)

### 1. **Kontekst**

U procesu smo odabira okvira za automatizaciju preglednika za naš cjevovod cjelovitog (end-to-end, E2E) testiranja. Taj će okvir biti sastavni dio naših CI/CD procesa i pokretat će testove koji simuliraju stvarne interakcije korisnika s našom platformom. Konkretno, testovi će pokrivati scenarije poput registracije/prijave korisnika, učitavanja datoteka, interakcija s nadzornom pločom i preuzimanja izvješća.

Kao **startup**, naš je fokus na **agilnom razvoju**, uz potrebu za brzom iteracijom i razvojem. Naš tim pretežno radi s **TypeScriptom** i **Pythonom**, a mogućnost pisanja testova na tim jezicima je ključna. Osim toga, platforma sadrži **interaktivne grafikone i nadzorne ploče**, zbog čega je kritično da alat za automatizaciju dobro podržava bogata, dinamična korisnička sučelja.

Dva kandidata za ovaj zadatak su **Playwright** i **Selenium**, svaki sa svojim prednostima i kompromisima. Moramo vrednovati ove okvire na temelju značajki i zahtjeva navedenih u nastavku.

### 2. **Razmatrane opcije**

- **Playwright** (Microsoft)
- **Selenium** (projekt Selenium)

### 3. **Pokretači odluke**

Čimbenici koji utječu na našu odluku su sljedeći:

1. **Agilni razvoj**: Odabrani alat mora omogućiti brze, fleksibilne razvojne cikluse.
2. **Podrška za jezike**: Naš tim zahtijeva podršku i za **TypeScript** i za **Python**.
3. **Testiranje interaktivnog korisničkog sučelja**: Mogućnost pouzdanog testiranja interaktivnih grafikona, nadzornih ploča i dinamičnih elemenata je ključna.
4. **Brzina izvođenja**: Iako nije primarna briga, performanse u CI/CD cjevovodima su razmatranje.
5. **Skalabilnost**: Ne planiramo masivno skaliranje u neposrednoj budućnosti, ali želimo osigurati da rješenje može podnijeti budući rast.
6. **Povratna kompatibilnost**: Naslijeđeni sustavi i kompatibilnost sa starijim preglednicima trenutačno nisu kritični za naš projekt.
7. **Testiranje na mobilnim uređajima**: Iako nije neposredan fokus, okvir bi trebao moći testirati mobilno prilagodljive značajke ili biti proširiv za takve slučajeve uporabe.
8. **Testiranje s više monitora**: Podrška za konfiguracije s više monitora sekundarni je zahtjev, osobito ako ikada budemo skalirali na testiranje složenijih korisničkih tijekova rada.
9. **Testiranje učitavanja datoteka**: Okvir mora učinkovito obrađivati učitavanje datoteka, što je temeljni zahtjev naših potreba za testiranjem.

### 4. **Kriteriji vrednovanja**

- **Jednostavnost uporabe**: Koliko je lako pisati i održavati testove?
- **Podrška za jezike**: Podržava li okvir TypeScript i Python, dva jezika koja naš tim najčešće koristi?
- **Testiranje interaktivnog korisničkog sučelja**: Koliko dobro okvir obrađuje složena, interaktivna korisnička sučelja poput grafikona, učitavanja datoteka i dinamičnih podataka?
- **Integracija s CI/CD-om**: Koliko se dobro okvir integrira u uobičajene CI/CD alate i usluge?
- **Podrška za više preglednika**: Koji su preglednici podržani i koliko dobro rade?
- **Performanse i brzina**: Koliko brzo se testovi izvode, osobito u CI/CD cjevovodu?
- **Skalabilnost**: Koliko dobro okvir može skalirati ako se dodaju brojniji testovi ili složeniji scenariji?
- **Zajednica i ekosustav**: Koliko je aktivna zajednica okvira? Postoji li mnogo dostupnih integracija i proširenja?

### 5. **Razmatranja**

#### 5.1 **Playwright**

##### **Prednosti**:
1. **Pametniji API za učitavanje lokalnih datoteka**: Playwrightov API za interakciju s lokalnim datotekama i učitavanje datoteka je jednostavniji i intuitivniji. To bi olakšalo implementaciju i održavanje testiranja učitavanja datoteka.
2. **Sintaksa i generiranje koda**: Playwright ima kraću, sažetiju sintaksu. To rezultira manje predloškog koda, što poboljšava održivost i učinkovitost programera. Osim toga, ta kraća sintaksa poboljšava kvalitetu generiranja koda pomoću OpenAI-ja, što olakšava automatsko generiranje testnih skripti.
3. **Testiranje interaktivnog korisničkog sučelja**: Playwright se ističe u testiranju dinamičnih, interaktivnih web aplikacija, poput onih s bogatim grafikonima, složenim korisničkim interakcijama i ažuriranjima u stvarnom vremenu. Vrlo učinkovito obrađuje WebSockete, WebRTC, shadow DOM i druge moderne web tehnologije.
4. **Podrška za više preglednika**: Playwright podržava **Chromium**, **WebKit** i **Firefox**. Ima dosljedne performanse u tim preglednicima, što bi trebalo pokriti većinu naših potreba za testiranjem.
5. **Integracija s CI/CD-om**: Playwright se besprijekorno integrira s modernim CI/CD platformama (GitHub Actions, Jenkins itd.). Može paralelno izvoditi testove u različitim preglednicima, optimizirajući vrijeme izvođenja testova i čineći ga prikladnim za brz razvoj.
6. **Brz i pouzdan**: Playwright je općenito brži od Seleniuma, osobito u headless načinu rada, i otporniji pri radu s asinkronim web elementima.

##### **Nedostaci**:
1. **Ograničeno testiranje na mobilnim uređajima**: Iako Playwright podržava mobilnu emulaciju za preglednike, nedostaju mu izvorne mogućnosti mobilnog testiranja poput Seleniumove integracije s Appiumom za pravo mobilno testiranje.
2. **Manji ekosustav**: Playwright je još uvijek noviji i manje etabliran od Seleniuma. Iako ima brzo rastuću zajednicu i dobru dokumentaciju, možda još nema golem ekosustav dodataka i integracija koje nudi Selenium.
3. **Ograničena podrška za preglednike**: Iako Playwright pokriva glavne moderne preglednike (Chrome, Safari, Firefox), njegova podrška za naslijeđene preglednike (npr. Internet Explorer) nije tako robusna kao Seleniumova.

#### 5.2 **Selenium**

##### **Prednosti**:
1. **Dulja povijest i zrelost**: Selenium postoji dugo i ima dokazan rezultat. Široko ga koriste mnogi timovi i industrije, što je dovelo do golemog ekosustava dodataka, integracija i resursa.
2. **Podrška za više preglednika i platformi**: Selenium podržava **široku paletu preglednika** i verzija, uključujući **Internet Explorer**, a može se integrirati i s raznim alatima poput **Dockera**, **Selenium Grida** i **cloud usluga** za distribuirano testiranje.
3. **Testiranje na mobilnim uređajima**: Selenium je, putem integracije s **Appiumom**, mnogo robusniji za mobilno testiranje, uključujući Android i iOS aplikacije. To ga čini boljim izborom za projekte s mobilnim prioritetom ili izraženim mobilnim fokusom.
4. **Testiranje s više monitora**: Selenium pruža bolju podršku za scenarije koji uključuju **više monitora** ili složene interakcije s više prozora.

##### **Nedostaci**:
1. **Složenost**: Seleniumov API je opširniji i eksplicitniji. Iako to u nekim slučajevima može biti prednost, znači više koda za pisanje i održavanje, što može smanjiti agilnost programera – osobito važnu u startup okruženju.
2. **Performanse**: Selenium se općenito izvodi sporije od Playwrighta, osobito u headless načinu rada. To bi moglo utjecati na CI/CD cjevovode, posebno kako broj testova raste.
3. **Testiranje interaktivnog korisničkog sučelja**: Selenium nije tako gladak kao Playwright kada je riječ o testiranju modernih, interaktivnih web korisničkih sučelja, osobito s grafikonima i ažuriranjima podataka u stvarnom vremenu. Zahtijeva više postavljanja i obrade za pouzdanu interakciju s dinamičnim sadržajem.

### 6. **Sažetak usporedbe**

| Značajka                          | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Jednostavnost uporabe**                   | Kraća sintaksa, intuitivnije za moderna korisnička sučelja | Eksplicitnije, zahtijeva više predloškog koda  |
| **Podrška za jezike**              | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Testiranje interaktivnog korisničkog sučelja**        | Izvrstan za dinamična korisnička sučelja u stvarnom vremenu          | Obrađuje osnovna korisnička sučelja, ali opširniji i složeniji za bogate interakcije |
| **Testiranje učitavanja datoteka**           | Pametniji API za učitavanje datoteka                  | Opširniji, manje intuitivan API         |
| **Integracija s CI/CD-om**             | Jednostavna integracija s GitHub Actions, Jenkins | Snažna integracija s mnogim CI alatima    |
| **Testiranje na mobilnim uređajima**                | Ograničeno, samo emulacija                       | Potpuna podrška putem Appiuma               |
| **Podrška za više preglednika**         | Chromium, WebKit, Firefox                     | Potpuna podrška za glavne i naslijeđene preglednike |
| **Performanse**                   | Brz, optimiziran za headless testiranje          | Sporiji, osobito u headless načinu rada       |
| **Testiranje s više monitora**         | Ograničeno                                       | Dobra podrška za postavke s više monitora    |
| **Zajednica i ekosustav**       | Raste, dobra dokumentacija                   | Velik, zreo, opsežan ekosustav       |

### 7. **Odluka**

Nakon razmatranja zahtjeva i kompromisa, **Playwright** je bolji izbor za naše trenutačne potrebe. Njegov pametniji API za testiranje učitavanja lokalnih datoteka, sažeta sintaksa i snažna podrška za testiranje interaktivnog korisničkog sučelja čine ga idealnim za naš ciklus agilnog razvoja. Činjenica da podržava i **TypeScript** i **Python** ključna je za naš tim, a moderni pristup okvira testiranju omogućit će nam pisanje čistog koda koji se lako održava.

Iako **Selenium** ostaje izvrstan alat, osobito za mobilno testiranje, podršku za naslijeđene preglednike i postavke s više monitora, slabije odgovara našim trenutačnim potrebama. Njegova opširnost, sporije performanse i složenije rukovanje dinamičnim korisničkim sučeljima poput grafikona čine ga manje optimalnim za naš slučaj uporabe.

### 8. **Posljedice**

- **Neposredna radnja**: Usvojit ćemo **Playwright** za naše E2E testiranje, usredotočujući se na testiranje korisničkih tokova koji uključuju registraciju, prijavu, učitavanje datoteka, nadzorne ploče i preuzimanje izvješća.
- **Dugoročna razmatranja**: Pratit ćemo razvoj ekosustava Playwrighta. Ako se naše potrebe promijene, osobito u pogledu mobilnog testiranja ili podrške za naslijeđene preglednike, možda ćemo ponovno razmotriti Selenium.
- **Obuka i dokumentacija**: Razvojni timovi morat će se upoznati s Playwrightovim API-jem, osobito za rukovanje dinamičnim korisničkim sučeljima i učitavanjem datoteka.
- **Migracija**: Postojeći Selenium testovi (ako ih ima) postupno će se migrirati na Playwright.

### 9. **Buduća razmatranja**

