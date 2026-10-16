# Arhitektūras lēmuma ieraksts: tīmekļa lietotņu ietvars „viss vienā”, full stack, jaunuzņēmuma produktam

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Galvenais mērķis:**  
Izveidot tīmekļa lietojumprogrammu maksājošiem klientiem, kur tie var pieteikties, augšupielādēt failus, apstrādāt datus un skatīt pārskatus, koncentrējoties uz aģilu izstrādi, full stack funkcionalitāti un spēcīgu saderību ar MI/ML rīkiem, īpaši Project Jupyter piezīmjdatoriem.

### Konteksts un prasības:

1. **Aģila izstrāde (augsta prioritāte)**: kā jaunuzņēmumam mums nepieciešama ātra iterācija un elastība. Aģilās prakses, piemēram, ātra prototipēšana, iteratīva izstrāde un pielāgojamība pārmaiņām, ir mūsu izstrādes cikla pamatā.

2. **Full stack ietvars (augsta prioritāte)**: mēs mērķējam samazināt izmaksas, izvēloties ietvaru, kas efektīvi spēj apstrādāt gan aizmuguri, gan priekšpusi, samazinot nepieciešamību pēc atsevišķiem priekšpuses ietvariem.

3. **Saderība ar MI/ML rīkiem (augsta prioritāte)**: būtiska ir spēja viegli integrēties ar datu analīzes rīkiem, piemēram, Jupyter piezīmjdatoriem, un Python datu zinātnes ekosistēmu (NumPy, Pandas, TensorFlow utt.). Tas atvieglotu efektīvu datu apstrādi un pārskatu veidošanu.

4. **Zemas svarīguma kritēriji**:
   - **Izpildlaika ātrums**: lai gan veiktspēja ir būtiska, sākumā tā nav kritiskākais faktors, jo mūs vairāk uztrauc izstrādes ātrums un funkciju pilnība.
   - **Mērogojamība**: mēs paredzam izaugsmi, taču mērogojamības jautājumus var risināt vēlāk, un tā šobrīd nav galvenā prasība.
   - **Atpakaļsaderība**: mēs koncentrējamies uz pašreizējām tehnoloģijām un īpaši neuztraucamies par atpakaļsaderību ar mantotajām sistēmām.

### Izvērtētie ietvari:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Pārskats**:  
Django ir augsta līmeņa tīmekļa ietvars Python, kas veicina ātru izstrādi un tīru, pragmatisku dizainu. Tas ir pazīstams ar savu filozofiju „viss vienā” („batteries included”), kas nozīmē, ka tas uzreiz ietver daudzas funkcijas, piemēram, autentifikāciju, maršrutēšanu, ORM un veidlapu apstrādi.

**Stiprās puses**:  
- **Full stack**: Django ir visaptverošs full stack ietvars, kas ar integrētām funkcijām (piem., veidņu dzinējs, administratora saskarne) var apstrādāt gan aizmugures, gan priekšpuses vajadzības.
- **Aģila izstrāde**: Django labi definētā struktūra un konvencijas ļauj ātri izstrādāt un pielāgoties, kas ir būtiski jaunuzņēmuma vidē. Ietvaram ir teicama dokumentācija un bagāta trešo pušu pakotņu ekosistēma, kas paātrina izstrādi.
- **MI/ML integrācija**: Python ekosistēma ir nepārspējama datu zinātnē un mašīnmācīšanās jomā. Django, būdams uz Python balstīts, nevainojami integrējas ar tādiem rīkiem kā Jupyter piezīmjdatori, Pandas, NumPy, TensorFlow un scikit-learn.
- **Kopiena un ekosistēma**: Django ir plaša kopiena, robusta dokumentācija un plašs spraudņu un paplašinājumu klāsts, kas ievērojami paātrina izstrādi un problēmu novēršanu.
  
**Vājās puses**:  
- **Izpildlaika ātrums**: Python mēdz būt lēnāks salīdzinājumā ar tādām valodām kā Rust vai Elixir. Tomēr šajā lietošanas gadījumā, kur veiktspēja nav galvenā bažas, tas var nebūt izšķirošs.
- **Mērogojamība**: lai gan Django ir ļoti mērogojams, ļoti lielā mērogā bez rūpīgas optimizācijas var būt izaicinājumi (piem., apstrādājot smagus vienlaicīgus pieprasījumus). Tomēr Django joprojām var efektīvi mērogot, izmantojot slodzes līdzsvarošanas un kešatmiņas paņēmienus.

**Spriedums**:  
Django labi atbilst prasībām par aģilu izstrādi, full stack atbalstu un MI/ML saderību. Tā integrācija ar Python piedāvā nevainojamu piekļuvi datu zinātnes rīkiem un bibliotēkām, kas nepieciešamas lietojumprogrammai.

---

### 2. **Ruby on Rails (Ruby)**

**Pārskats**:  
Ruby on Rails (RoR) ir nobriedis full stack tīmekļa lietojumprogrammu ietvars, kas pazīstams ar pieeju „konvencija pār konfigurāciju”, kas atvieglo ātru izstrādi.

**Stiprās puses**:  
- **Full stack**: RoR ir iebūvēti rīki gan aizmugures, gan priekšpuses izstrādei (piem., skati, veidnes, sastatnes), un tā bagātā gem bibliotēka ļauj ātri īstenot dažādas funkcijas.
- **Aģila izstrāde**: Ruby on Rails ir īpaši pazīstams ar saviem ātrajiem iterācijas cikliem, kas ir izdevīgi jaunuzņēmumiem, kuri vēlas ātri iterēt funkcijas. RoR atbalsta testos balstītu izstrādi (TDD) un tam ir iedibināta ekosistēma aģilām darbplūsmām.
- **Kopiena un ekosistēma**: RoR ir labi iedibināta, spēcīga kopiena un plašs gem klāsts, kas var paātrināt izstrādi.
- **Lietošanas vienkāršība**: Rails ir ļoti izstrādātājam draudzīga sintakse, un tas ir pazīstams ar to, ka tādus uzdevumus kā datubāzes migrācijas, modeļa-skata-kontroliera (MVC) arhitektūra un maršrutu apstrāde padara ātrus un vienkāršus.

**Vājās puses**:  
- **Veiktspēja**: Ruby mēdz būt lēnāka izpildlaika veiktspēja salīdzinājumā ar Python vai Elixir. Lai gan RoR var mērogoties ar pareizo infrastruktūru, Ruby veiktspēja var kļūt par sašaurinājumu lietojumprogrammām, kurām nepieciešama smaga reāllaika apstrāde vai liela vienlaicīga datplūsma.
- **MI/ML integrācija**: lai gan Ruby ir dažas mašīnmācīšanās bibliotēkas, tas nav tik plaši pieņemts MI/ML kopienā kā Python. Integrācija ar tādiem rīkiem kā Jupyter piezīmjdatori nav tik nevainojama, padarot Python par spēcīgāku izvēli datu ietilpīgām lietojumprogrammām.
  
**Spriedums**:  
Lai gan Ruby on Rails izceļas aģilā izstrādē un ātrā prototipēšanā, tas atpaliek MI/ML saderības ziņā salīdzinājumā ar Python (Django). Tā ir dzīvotspējīga izvēle jaunuzņēmumiem, kas prioritizē ātru iterāciju pār dziļu datu analīzes integrāciju.

---

### 3. **Phoenix (Elixir)**

**Pārskats**:  
Phoenix ir tīmekļa ietvars, kas veidots ar Elixir, funkcionālo programmēšanas valodu, kas paredzēta mērogojamībai un vienlaicībai. Phoenix izmanto Erlang VM, kas pazīstama ar masveida vienlaicības un kļūmju izturīgu sistēmu apstrādi.

**Stiprās puses**:  
- **Mērogojamība un veiktspēja**: Phoenix izceļas mērogojamībā un augstas vienlaicības apstrādē. Tas ir veidots uz Erlang VM, kas var atbalstīt tūkstošiem (vai pat miljoniem) vienlaicīgu savienojumu, padarot to par spēcīgu kandidātu lietojumprogrammām, kurām nepieciešama reāllaika datu apstrāde vai liela apjoma datplūsma.
- **Full stack**: Phoenix ietver visu nepieciešamo gan lietojumprogrammas aizmugures, gan priekšpuses veidošanai. Tas atbalsta tiešos skatus (live views) interaktīviem UI atjauninājumiem un ietver veidņu dzinēju.
- **Aģila izstrāde**: Phoenix ir ļoti modulārs, ļaujot ātri iterēt funkcijas. Tas ir labi piemērots jaunuzņēmumiem, kuriem jāvirzās ātri.
- **MI/ML saderība**: lai gan Elixir ir topošas mašīnmācīšanās bibliotēkas, tas nav tik plaši atbalstīts MI/ML uzdevumiem kā Python. Integrācijai ar tādiem rīkiem kā Jupyter piezīmjdatori būtu nepieciešami apvedceļi, jo Elixir ekosistēma datu zinātnei nav tik nobriedusi kā Python.

**Vājās puses**:  
- **MI/ML ekosistēma**: Elixir nav primārā valoda, ko izmanto datu zinātnē vai mašīnmācīšanās jomā, un ekosistēma nav tik nobriedusi kā Python. Tādējādi integrācija ar tādiem rīkiem kā Jupyter piezīmjdatori vai populārām MI bibliotēkām (TensorFlow, PyTorch) būs apgrūtinoša.
- **Mācīšanās līkne**: ja komanda nepārzina funkcionālo programmēšanu un Elixir, mācīšanās līkne var būt stāvāka.

**Spriedums**:  
Phoenix ir lieliska izvēle, ja mērogojamība un vienlaicība ir galvenās bažas. Tomēr, ņemot vērā prioritāti MI/ML saderībai, Phoenix var nebūt labākā izvēle Elixir ierobežotās ekosistēmas dēļ šajā jomā.

---

### 4. **Loco (Rust)**

**Pārskats**:  
Loco ir tīmekļa ietvars, kas veidots ar Rust, sistēmu programmēšanas valodu, kas pazīstama ar veiktspēju, atmiņas drošību un vienlaicību. Rust kļūst arvien populārāka augstas veiktspējas lietojumprogrammu veidošanai.

**Stiprās puses**:  
- **Veiktspēja**: Rust galvenā stiprā puse ir augsta veiktspēja un atmiņas drošība, padarot to par teicamu izvēli lietojumprogrammām, kurām nepieciešama zema līmeņa kontrole vai ārkārtīgi augsta veiktspēja.
- **Vienlaicība**: Rust īpašumtiesību sistēma nodrošina atmiņas drošību, vienlaikus ļaujot drošu vienlaicīgu programmēšanu, padarot to ideālu sistēmām, kurām jāmērogojas efektīvi un jāapstrādā paralēlisms.

**Vājās puses**:  
- **Full stack izstrāde**: Loco, lai gan daudzsološs, nav tik nobriedis kā citi ietvari attiecībā uz pilna full stack risinājuma nodrošināšanu. Tas ir piemērotāks aizmugures izstrādei, un priekšpuses ekosistēma ap Rust vēl veidojas.
- **Aģila izstrāde**: izstrāde ar Rust var būt lēnāka salīdzinājumā ar augstākā līmeņa valodām, piemēram, Python vai Ruby, tās zemāka līmeņa rakstura un stāvākas mācīšanās līknes dēļ.
- **MI/ML ekosistēma**: Rust nav tik plašas MI/ML ekosistēmas kā Python. Lai gan Rust ir augošas bibliotēkas skaitliskai skaitļošanai, tās ir daudz mazāk nobriedušas nekā Python piedāvājums, piemēram, Jupyter piezīmjdatori vai mašīnmācīšanās ietvari.
  
**Spriedums**:  
Lai gan Rust un tā ietvars Loco piedāvā izcilu veiktspēju, full stack atbalsta, aģilās izstrādes ieguvumu un MI/ML ekosistēmas trūkums padara to mazāk ideālu šim konkrētajam lietošanas gadījumam. Tas ir piemērotāks veiktspējai kritiskām lietojumprogrammām nekā ātrai tīmekļa izstrādei ar integrētiem datu zinātnes rīkiem.

---

### Secinājums

Pēc iespēju izvērtēšanas, pamatojoties uz projekta prasībām, **Django (Python)** ir vispiemērotākā izvēle. Tas piedāvā šādas priekšrocības:

- **Full stack iespējas**: Django ir full stack ietvars, kas integrē gan aizmugures, gan priekšpuses izstrādi.
- **Aģila izstrāde**: ietvars ir labi piemērots ātrai prototipēšanai un iterācijai, kas ir būtiski jaunuzņēmuma vidē.
- **MI/ML saderība**: Python ir vadošā valoda MI/ML jomā, un Django saderība ar bibliotēkām, piemēram, Jupyter piezīmjdatoriem, nodrošina gludu integrāciju datu analīzei un apstrādei.
- **Kopiena un ekosistēma**: Django spēcīgais kopienas atbalsts un plašā bibliotēku ekosistēma nodrošina daudzus rīkus izstrādes paātrināšanai.

Lai gan **Ruby on Rails** ir arī spēcīgs kandidāts aģilai izstrādei, tā ierobežotais MI/ML atbalsts padara to mazāk ideālu šim konkrētajam lietošanas gadījumam. **Phoenix (Elixir)** un **Loco (Rust)**, lai gan teicami mērogojamības un veiktspējas ziņā, atpaliek MI/ML integrācijas un full stack izstrādes ziņā. Tāpēc Django ir ieteicamais ietvars šim projektam.
