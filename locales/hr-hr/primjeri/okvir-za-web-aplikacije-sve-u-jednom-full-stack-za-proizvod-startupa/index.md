# Zapis arhitekturne odluke: okvir za web aplikacije, sve u jednom, full stack, za proizvod startupa

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
Izgraditi web aplikaciju u kojoj se plaćajući klijenti mogu prijaviti, učitavati datoteke, obrađivati podatke i pregledavati izvješća, s fokusom na agilni razvoj, full-stack funkcionalnost i snažnu kompatibilnost s alatima umjetne inteligencije/strojnog učenja, osobito s bilježnicama Project Jupyter.

### Kontekst i zahtjevi:

1. **Agilni razvoj (visoki prioritet)**: Kao startup trebamo brzu iteraciju i fleksibilnost. Agilne prakse, poput brzog prototipiranja, iterativnog razvoja i prilagodljivosti promjenama, ključne su za naš razvojni ciklus.

2. **Full-stack okvir (visoki prioritet)**: Nastojimo minimizirati režijske troškove odabirom okvira koji može učinkovito obrađivati i back-end i front-end, smanjujući potrebu za zasebnim front-end okvirima.

3. **Kompatibilnost s alatima umjetne inteligencije/strojnog učenja (visoki prioritet)**: Mogućnost jednostavne integracije s alatima za analizu podataka poput bilježnica Jupyter i Pythonova ekosustava znanosti o podacima (NumPy, Pandas, TensorFlow itd.) je ključna. To bi olakšalo učinkovitu obradu podataka i izvještavanje.

4. **Kriteriji niske važnosti**:
   - **Brzina izvođenja**: Iako su performanse relevantne, na početku nisu najkritičniji čimbenik jer nam je više stalo do brzine razvoja i cjelovitosti značajki.
   - **Skalabilnost**: Očekujemo rast, ali pitanja skalabilnosti mogu se riješiti kasnije i to trenutačno nije primarni zahtjev.
   - **Povratna kompatibilnost**: Usredotočeni smo na trenutačne tehnologije i ne brine nas previše povratna kompatibilnost s naslijeđenim sustavima.

### Vrednovani okviri:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Pregled**:  
Django je web okvir visoke razine za Python koji potiče brz razvoj i čist, pragmatičan dizajn. Poznat je po filozofiji „sve u jednom“ (batteries included), što znači da odmah uključuje mnoge značajke poput autentifikacije, usmjeravanja, ORM-a i obrade obrazaca.

**Snage**:  
- **Full-stack**: Django je sveobuhvatan full-stack okvir koji može obrađivati potrebe i back-enda i front-enda s integriranim značajkama (npr. mehanizam predložaka, administratorsko sučelje).
- **Agilni razvoj**: Djangova dobro definirana struktura i konvencije omogućuju brz razvoj i prilagodljivost, što je ključno za startup okruženje. Okvir dolazi s izvrsnom dokumentacijom i bogatim ekosustavom paketa trećih strana, što ubrzava razvoj.
- **Integracija umjetne inteligencije/strojnog učenja**: Pythonov ekosustav nenadmašan je kada je riječ o znanosti o podacima i strojnom učenju. Django, budući da se temelji na Pythonu, besprijekorno se integrira s alatima poput bilježnica Jupyter, Pandasa, NumPyja, TensorFlowa i scikit-learna.
- **Zajednica i ekosustav**: Django ima opsežnu zajednicu, robusnu dokumentaciju i širok raspon dodataka i proširenja, što znatno ubrzava razvoj i rješavanje problema.
  
**Slabosti**:  
- **Brzina izvođenja**: Python je obično sporiji u usporedbi s jezicima poput Rusta ili Elixira. Međutim, za ovaj slučaj uporabe, gdje performanse nisu primarna briga, to možda nije presudno.
- **Skalabilnost**: Iako je Django vrlo skalabilan, pri vrlo velikom opsegu bez pažljive optimizacije mogu postojati izazovi (npr. pri obradi velikog broja istodobnih zahtjeva). Međutim, Django se i dalje može učinkovito skalirati tehnikama uravnoteživanja opterećenja i keširanja.

**Presuda**:  
Django se dobro uklapa u zahtjeve za agilnim razvojem, full-stack podrškom i kompatibilnošću s umjetnom inteligencijom/strojnim učenjem. Njegova integracija s Pythonom nudi besprijekoran pristup alatima i bibliotekama znanosti o podacima potrebnima za aplikaciju.

---

### 2. **Ruby on Rails (Ruby)**

**Pregled**:  
Ruby on Rails (RoR) je zreo full-stack okvir za web aplikacije poznat po pristupu konvencija umjesto konfiguracije, koji olakšava brz razvoj.

**Snage**:  
- **Full-stack**: RoR dolazi s ugrađenim alatima za razvoj back-enda i front-enda (npr. prikazi, predlošci, scaffolding), a njegova bogata biblioteka gemova omogućuje brzu implementaciju raznih značajki.
- **Agilni razvoj**: Ruby on Rails osobito je poznat po brzim ciklusima iteracije, što je prednost za startupe koji žele brzo iterirati značajke. RoR podržava razvoj vođen testovima (TDD) i ima uspostavljen ekosustav za agilne tijekove rada.
- **Zajednica i ekosustav**: RoR ima dobro uspostavljenu, snažnu zajednicu i široku paletu gemova koji mogu ubrzati razvoj.
- **Jednostavnost uporabe**: Rails ima sintaksu vrlo prijateljsku prema programerima i poznat je po tome što zadaće poput migracija baze podataka, arhitekture model-view-controller (MVC) i obrade ruta čini brzima i jednostavnima.

**Slabosti**:  
- **Performanse**: Ruby obično ima sporije performanse izvođenja u usporedbi s Pythonom ili Elixirom. Iako se RoR može skalirati uz odgovarajuću infrastrukturu, Rubyjeve performanse mogle bi postati usko grlo za aplikacije koje zahtijevaju intenzivnu obradu u stvarnom vremenu ili visok istodobni promet.
- **Integracija umjetne inteligencije/strojnog učenja**: Iako Ruby ima neke biblioteke za strojno učenje, nije tako široko usvojen u zajednici umjetne inteligencije/strojnog učenja kao Python. Integracija s alatima poput bilježnica Jupyter nije tako besprijekorna, zbog čega je Python snažniji izbor za aplikacije s mnogo podataka.
  
**Presuda**:  
Iako Ruby on Rails briljira u agilnom razvoju i brzom prototipiranju, zaostaje u kompatibilnosti s umjetnom inteligencijom/strojnim učenjem u usporedbi s Pythonom (Django). To je održiv izbor za startupe koji daju prednost brzoj iteraciji pred dubokom integracijom analize podataka.

---

### 3. **Phoenix (Elixir)**

**Pregled**:  
Phoenix je web okvir izgrađen u Elixiru, funkcijskom programskom jeziku dizajniranom za skalabilnost i istodobnost. Phoenix koristi Erlang VM, poznat po obradi masivne istodobnosti i sustava otpornih na kvarove.

**Snage**:  
- **Skalabilnost i performanse**: Phoenix blista u skalabilnosti i obradi visoke istodobnosti. Izgrađen je na Erlang VM-u, koji može podržati tisuće (pa i milijune) istodobnih veza, što ga čini snažnim kandidatom za aplikacije koje zahtijevaju obradu podataka u stvarnom vremenu ili velik obujam prometa.
- **Full-stack**: Phoenix uključuje sve potrebno za izgradnju i back-enda i front-enda aplikacije. Podržava live views za interaktivna ažuriranja UI-ja i uključuje mehanizam predložaka.
- **Agilni razvoj**: Phoenix je vrlo modularan, što omogućuje brzu iteraciju značajki. Dobro je prikladan za startupe koji se moraju brzo kretati.
- **Kompatibilnost s umjetnom inteligencijom/strojnim učenjem**: Iako Elixir ima nove biblioteke za strojno učenje, nije tako široko podržan za zadaće umjetne inteligencije/strojnog učenja kao Python. Integracija s alatima poput bilježnica Jupyter zahtijevala bi zaobilazna rješenja jer Elixirov ekosustav za znanost o podacima nije tako zreo kao Pythonov.

**Slabosti**:  
- **Ekosustav umjetne inteligencije/strojnog učenja**: Elixir nije primarni jezik koji se koristi u znanosti o podacima ili strojnom učenju, a ekosustav nije tako zreo kao Pythonov. Stoga će integracija s alatima poput bilježnica Jupyter ili popularnih UI biblioteka (TensorFlow, PyTorch) biti glomazna.
- **Krivulja učenja**: Ako tim nije upoznat s funkcijskim programiranjem i Elixirom, može postojati strmija krivulja učenja.

**Presuda**:  
Phoenix je izvrstan izbor ako su skalabilnost i istodobnost primarna briga. Međutim, s obzirom na prioritet kompatibilnosti s umjetnom inteligencijom/strojnim učenjem, Phoenix možda nije najbolji izbor zbog Elixirova ograničenog ekosustava u tom području.

---

### 4. **Loco (Rust)**

**Pregled**:  
Loco je web okvir izgrađen u Rustu, sistemskom programskom jeziku poznatom po performansama, sigurnosti memorije i istodobnosti. Rust je sve popularniji za izgradnju aplikacija visokih performansi.

**Snage**:  
- **Performanse**: Rustova primarna snaga leži u visokim performansama i sigurnosti memorije, što ga čini izvrsnim izborom za aplikacije koje zahtijevaju kontrolu niske razine ili iznimno visoke performanse.
- **Istodobnost**: Rustov sustav vlasništva osigurava sigurnost memorije, a istodobno omogućuje sigurno istodobno programiranje, što ga čini idealnim za sustave koji se moraju učinkovito skalirati i obrađivati paralelizam.

**Slabosti**:  
- **Full-stack razvoj**: Loco, iako obećava, nije tako zreo kao ostali okviri u pogledu pružanja cjelovitog full-stack rješenja. Prikladniji je za back-end razvoj, a front-end ekosustav oko Rusta tek se pojavljuje.
- **Agilni razvoj**: Razvoj u Rustu može biti sporiji u usporedbi s jezicima više razine poput Pythona ili Rubyja zbog njegove niže razine i strmije krivulje učenja.
- **Ekosustav umjetne inteligencije/strojnog učenja**: Rust nema isti opsežan ekosustav za UI/ML kao Python. Iako postoje rastuće biblioteke u Rustu za numeričko računanje, one su daleko manje zrele od Pythonovih ponuda, poput bilježnica Jupyter ili okvira za strojno učenje.
  
**Presuda**:  
Iako Rust i njegov okvir Loco nude iznimne performanse, nedostatak full-stack podrške, koristi agilnog razvoja i ekosustav umjetne inteligencije/strojnog učenja čine ga manje idealnim za ovaj konkretni slučaj uporabe. Prikladniji je za aplikacije kritične za performanse nego za brz web razvoj s integriranim alatima znanosti o podacima.

---

### Zaključak

Nakon vrednovanja opcija na temelju zahtjeva projekta **Django (Python)** je najprikladniji izbor. Nudi sljedeće prednosti:

- **Full-stack mogućnosti**: Django je full-stack okvir koji integrira razvoj back-enda i front-enda.
- **Agilni razvoj**: Okvir je dobro prikladan za brzo prototipiranje i iteraciju, što je ključno za startup okruženje.
- **Kompatibilnost s umjetnom inteligencijom/strojnim učenjem**: Python je vodeći jezik u UI-ju/ML-u, a Djangova kompatibilnost s bibliotekama poput bilježnica Jupyter osigurava glatku integraciju za analizu i obradu podataka.
- **Zajednica i ekosustav**: Snažna podrška zajednice za Django i opsežan ekosustav biblioteka pružaju brojne alate za ubrzanje razvoja.

Iako je **Ruby on Rails** također snažan kandidat za agilni razvoj, njegova ograničena podrška za UI/ML čini ga manje idealnim za ovaj konkretni slučaj uporabe. **Phoenix (Elixir)** i **Loco (Rust)**, iako izvrsni za skalabilnost i performanse, zaostaju u integraciji umjetne inteligencije/strojnog učenja i full-stack razvoju. Stoga je Django preporučeni okvir za ovaj projekt.