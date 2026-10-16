# Zapis arhitekturne odločitve: spletno ogrodje »vse v enem«, full stack, za zagonski izdelek

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Primarni cilj:**  
Zgraditi spletno aplikacijo, v kateri se plačujoče stranke prijavijo, naložijo datoteke, obdelajo podatke in si ogledajo poročila, s poudarkom na agilnem razvoju, funkcionalnosti full stack in močni združljivosti z orodji UI/ML, zlasti z zvezki Project Jupyter.

### Kontekst in zahteve:

1. **Agilen razvoj (visoka prednost)**: Kot zagonsko podjetje potrebujemo hitro iteracijo in prilagodljivost. Agilne prakse, kot so hitra izdelava prototipov, iterativni razvoj in prilagodljivost spremembam, so ključne za naš razvojni cikel.

2. **Ogrodje full stack (visoka prednost)**: Cilj nam je zmanjšati režijske stroške z izbiro ogrodja, ki lahko učinkovito obravnava zaledje in uporabniški del, s čimer se zmanjša potreba po ločenih ogrodjih za uporabniški del.

3. **Združljivost z orodji UI/ML (visoka prednost)**: Bistvena je zmožnost enostavne integracije z orodji za analizo podatkov, kot so zvezki Jupyter, in ekosistemom podatkovne znanosti Pythona (NumPy, Pandas, TensorFlow itd.). To bi olajšalo učinkovito obdelavo podatkov in poročanje.

4. **Merila nizke pomembnosti**:
   - **Hitrost izvajanja**: Čeprav je zmogljivost pomembna, na začetku ni najkritičnejši dejavnik, saj nas bolj skrbita hitrost razvoja in popolnost funkcij.
   - **Razširljivost**: Pričakujemo rast, vendar je skrbi glede razširljivosti mogoče obravnavati pozneje in zdaj ni primarna zahteva.
   - **Združljivost za nazaj**: Osredotočamo se na trenutne tehnologije in nas združljivost za nazaj s podedovanimi sistemi ne skrbi močno.

### Ovrednotena ogrodja:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Pregled**:  
Django je visokonivojsko spletno ogrodje za Python, ki spodbuja hiter razvoj ter čisto, pragmatično zasnovo. Znano je po filozofiji »vse v enem« (»batteries included«), kar pomeni, da že takoj vključuje številne funkcije, kot so preverjanje pristnosti, usmerjanje, ORM in obravnava obrazcev.

**Prednosti**:  
- **Full stack**: Django je celovito ogrodje full stack, ki lahko z integriranimi funkcijami (npr. mehanizem predlog, skrbniški vmesnik) obravnava potrebe zaledja in uporabniškega dela.
- **Agilen razvoj**: Dobro opredeljena struktura in konvencije ogrodja Django omogočajo hiter razvoj in prilagodljivost, kar je ključno za zagonsko okolje. Ogrodje ima odlično dokumentacijo in bogat ekosistem paketov tretjih oseb, kar pospešuje razvoj.
- **Integracija UI/ML**: Ekosistem Pythona je neprekosljiv, ko gre za podatkovno znanost in strojno učenje. Django, ki temelji na Pythonu, se brezhibno integrira z orodji, kot so zvezki Jupyter, Pandas, NumPy, TensorFlow in scikit-learn.
- **Skupnost in ekosistem**: Django ima obsežno skupnost, robustno dokumentacijo in široko paleto vtičnikov in razširitev, kar bistveno pospeši razvoj in odpravljanje težav.
  
**Slabosti**:  
- **Hitrost izvajanja**: Python je počasnejši v primerjavi z jeziki, kot sta Rust ali Elixir. Vendar za ta primer uporabe, kjer zmogljivost ni primarna skrb, to morda ni odločilno.
- **Razširljivost**: Čeprav je Django zelo razširljiv, lahko pri zelo visokem obsegu brez skrbne optimizacije pride do izzivov (npr. pri obravnavi velikega števila sočasnih zahtev). Vendar je Django še vedno mogoče učinkovito skalirati z uporabo uravnoteženja obremenitve in tehnik predpomnjenja.

**Ocena**:  
Django se dobro ujema z zahtevami za agilen razvoj, podporo full stack in združljivost z UI/ML. Njegova integracija s Pythonom ponuja brezhiben dostop do orodij in knjižnic podatkovne znanosti, potrebnih za aplikacijo.

---

### 2. **Ruby on Rails (Ruby)**

**Pregled**:  
Ruby on Rails (RoR) je zrelo spletno ogrodje full stack, znano po pristopu »konvencija pred konfiguracijo«, ki olajša hiter razvoj.

**Prednosti**:  
- **Full stack**: RoR ima vgrajena orodja za razvoj zaledja in uporabniškega dela (npr. pogledi, predloge, scaffolding), bogata knjižnica paketov gem pa omogoča hitro izvedbo različnih funkcij.
- **Agilen razvoj**: Ruby on Rails je še posebej znan po hitrih iteracijskih ciklih, kar je koristno za zagonska podjetja, ki želijo hitro iterirati funkcije. RoR podpira razvoj, voden s testi (TDD), in ima uveljavljen ekosistem za agilne poteke dela.
- **Skupnost in ekosistem**: RoR ima uveljavljeno, močno skupnost in široko paleto paketov gem, ki lahko pospešijo razvoj.
- **Enostavnost uporabe**: Rails ima zelo razvijalcem prijazno sintakso in je znan po tem, da naloge, kot so selitve podatkovne baze, arhitektura model-pogled-krmilnik (MVC) in obravnava poti, naredi hitre in preproste.

**Slabosti**:  
- **Zmogljivost**: Ruby ima počasnejšo zmogljivost izvajanja v primerjavi s Pythonom ali Elixirjem. Čeprav se lahko RoR z ustrezno infrastrukturo skalira, lahko zmogljivost jezika Ruby postane ozko grlo za aplikacije, ki zahtevajo težko obdelavo v realnem času ali velik sočasni promet.
- **Integracija UI/ML**: Čeprav ima Ruby nekaj knjižnic za strojno učenje, ni tako široko sprejet v skupnosti UI/ML kot Python. Integracija z orodji, kot so zvezki Jupyter, ni tako brezhibna, zato je Python močnejša izbira za aplikacije, ki temeljijo na podatkih.
  
**Ocena**:  
Čeprav Ruby on Rails blesti pri agilnem razvoju in hitri izdelavi prototipov, zaostaja pri združljivosti z UI/ML v primerjavi s Pythonom (Django). Je izvedljiva izbira za zagonska podjetja, ki dajejo prednost hitri iteraciji pred globoko integracijo analize podatkov.

---

### 3. **Phoenix (Elixir)**

**Pregled**:  
Phoenix je spletno ogrodje, zgrajeno z jezikom Elixir, funkcijskim programskim jezikom, zasnovanim za razširljivost in sočasnost. Phoenix izkorišča virtualni stroj Erlang, ki je znan po obvladovanju množične sočasnosti in sistemov, odpornih proti napakam.

**Prednosti**:  
- **Razširljivost in zmogljivost**: Phoenix blesti pri razširljivosti in obvladovanju visoke sočasnosti. Zgrajen je na virtualnem stroju Erlang, ki lahko podpira tisoče (ali celo milijone) sočasnih povezav, zaradi česar je močan kandidat za aplikacije, ki zahtevajo obdelavo podatkov v realnem času ali promet velikega obsega.
- **Full stack**: Phoenix vključuje vse, kar je potrebno za gradnjo zaledja in uporabniškega dela aplikacije. Podpira žive poglede (live views) za interaktivne posodobitve uporabniškega vmesnika in vključuje mehanizem predlog.
- **Agilen razvoj**: Phoenix je zelo modularen in omogoča hitro iteracijo funkcij. Dobro je primeren za zagonska podjetja, ki se morajo gibati hitro.
- **Združljivost z UI/ML**: Čeprav ima Elixir nastajajoče knjižnice za strojno učenje, ni tako široko podprt za naloge UI/ML kot Python. Integracija z orodji, kot so zvezki Jupyter, bi zahtevala zasilne rešitve, saj ekosistem jezika Elixir za podatkovno znanost ni tako zrel kot Pythonov.

**Slabosti**:  
- **Ekosistem UI/ML**: Elixir ni primarni jezik, ki se uporablja v podatkovni znanosti ali strojnem učenju, njegov ekosistem pa ni tako zrel kot Pythonov. Zato bo integracija z orodji, kot so zvezki Jupyter, ali priljubljenimi knjižnicami UI (TensorFlow, PyTorch) okorna.
- **Krivulja učenja**: Če ekipa ne pozna funkcijskega programiranja in jezika Elixir, je lahko krivulja učenja strmejša.

**Ocena**:  
Phoenix je odlična izbira, če sta razširljivost in sočasnost primarni skrbi. Vendar Phoenix glede na prednost združljivosti z UI/ML morda ni najboljša izbira zaradi omejenega ekosistema jezika Elixir na tem področju.

---

### 4. **Loco (Rust)**

**Pregled**:  
Loco je spletno ogrodje, zgrajeno z jezikom Rust, sistemskim programskim jezikom, znanim po zmogljivosti, varnosti pomnilnika in sočasnosti. Rust je vse bolj priljubljen za gradnjo visokozmogljivih aplikacij.

**Prednosti**:  
- **Zmogljivost**: Glavna prednost jezika Rust je visoka zmogljivost in varnost pomnilnika, zaradi česar je odlična izbira za aplikacije, ki zahtevajo nizkonivojski nadzor ali izjemno visoko zmogljivost.
- **Sočasnost**: Sistem lastništva jezika Rust zagotavlja varnost pomnilnika in hkrati omogoča varno sočasno programiranje, zaradi česar je idealen za sisteme, ki se morajo učinkovito skalirati in obvladovati vzporednost.

**Slabosti**:  
- **Razvoj full stack**: Loco, čeprav obetaven, ni tako zrel kot druga ogrodja glede zagotavljanja celovite rešitve full stack. Bolj je primeren za razvoj zaledja, ekosistem za uporabniški del okoli jezika Rust pa še nastaja.
- **Agilen razvoj**: Razvoj z jezikom Rust je lahko počasnejši v primerjavi z višjenivojskimi jeziki, kot sta Python ali Ruby, zaradi njegove nižjenivojske narave in strmejše krivulje učenja.
- **Ekosistem UI/ML**: Rust nima tako obsežnega ekosistema za UI/ML kot Python. Čeprav v jeziku Rust rastejo knjižnice za numerično računanje, so veliko manj zrele kot Pythonova ponudba, kot so zvezki Jupyter ali ogrodja za strojno učenje.
  
**Ocena**:  
Čeprav Rust in njegovo ogrodje Loco ponujata izjemno zmogljivost, pomanjkanje podpore full stack, prednosti agilnega razvoja in ekosistema UI/ML ga dela manj idealnega za ta konkretni primer uporabe. Bolj je primeren za aplikacije, kritične za zmogljivost, kot za hiter spletni razvoj z integriranimi orodji podatkovne znanosti.

---

### Sklep

Po vrednotenju možnosti glede na zahteve projekta je **Django (Python)** najprimernejša izbira. Ponuja naslednje prednosti:

- **Zmožnosti full stack**: Django je ogrodje full stack, ki združuje razvoj zaledja in uporabniškega dela.
- **Agilen razvoj**: Ogrodje je dobro primerno za hitro izdelavo prototipov in iteracijo, kar je bistveno za zagonsko okolje.
- **Združljivost z UI/ML**: Python je vodilni jezik na področju UI/ML, združljivost ogrodja Django s knjižnicami, kot so zvezki Jupyter, pa zagotavlja gladko integracijo za analizo in obdelavo podatkov.
- **Skupnost in ekosistem**: Močna podpora skupnosti in obsežen ekosistem knjižnic ogrodja Django zagotavljata številna orodja za pospešitev razvoja.

Čeprav je **Ruby on Rails** prav tako močan kandidat za agilen razvoj, ga omejena podpora UI/ML dela manj idealnega za ta konkretni primer uporabe. **Phoenix (Elixir)** in **Loco (Rust)**, čeprav odlična za razširljivost in zmogljivost, zaostajata pri integraciji UI/ML in razvoju full stack. Zato je Django priporočeno ogrodje za ta projekt.
