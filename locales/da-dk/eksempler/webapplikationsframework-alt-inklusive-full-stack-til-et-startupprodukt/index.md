# Arkitekturbeslutningspost: webapplikationsframework, alt inklusive (batteries included), full stack, til et startupprodukt

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Primært mål:**  
At bygge en webapplikation, hvor betalende kunder kan logge ind, uploade filer, behandle data og se rapporter, med fokus på agil udvikling, full stack-funktionalitet og stærk kompatibilitet med AI/ML-værktøjer, især Project Jupyter-notebooks.

### Kontekst og krav:

1. **Agil udvikling (høj prioritet)**: som startup har vi brug for hurtig iteration og fleksibilitet. Agile metoder, såsom hurtig prototyping, iterativ udvikling og tilpasningsevne over for forandring, er nøglen til vores udviklingscyklus.

2. **Full stack-framework (høj prioritet)**: vi stræber efter at minimere overhead ved at vælge et framework, der effektivt kan håndtere både backend og frontend, hvilket reducerer behovet for separate frontend-frameworks.

3. **Kompatibilitet med AI/ML-værktøjer (høj prioritet)**: evnen til nemt at integrere med dataanalyseværktøjer som Jupyter-notebooks og Pythons økosystem for datavidenskab (NumPy, Pandas, TensorFlow osv.) er afgørende. Det vil lette effektiv databehandling og rapportering.

4. **Kriterier med lav prioritet**:
   - **Kørselshastighed**: selv om ydeevne er relevant, er det ikke den mest kritiske faktor i starten, da vi er mere optaget af udviklingshastighed og færdiggørelse af funktioner.
   - **Skalerbarhed**: vi forudser vækst, men skalerbarhedsproblemer kan håndteres senere og er ikke et primært krav lige nu.
   - **Bagudkompatibilitet**: vi fokuserer på nuværende teknologier og er ikke særlig bekymrede over bagudkompatibilitet med ældre systemer.

### Evaluerede frameworks:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Oversigt**:  
Django er et webframework på højt niveau til Python, der fremmer hurtig udvikling og et rent, pragmatisk design. Det er kendt for sin "batteries included"-filosofi, hvilket betyder, at det som standard indeholder mange funktioner såsom autentificering, routing, ORM og formularhåndtering.

**Styrker**:  
- **Full stack**: Django er et omfattende full stack-framework, der kan håndtere både backend- og frontendbehov med integrerede funktioner (f.eks. skabelonmotor, administrationsgrænseflade).
- **Agil udvikling**: Djangos veldefinerede struktur og konventioner muliggør hurtig udvikling og tilpasningsevne, afgørende for et startupmiljø. Frameworket leveres med fremragende dokumentation og et rigt økosystem af tredjepartspakker, hvilket fremskynder udviklingen.
- **AI/ML-integration**: Pythons økosystem er uovertrufnet inden for datavidenskab og maskinlæring. Django, der er Python-baseret, integrerer problemfrit med værktøjer som Jupyter-notebooks, Pandas, NumPy, TensorFlow og scikit-learn.
- **Fællesskab og økosystem**: Django har et omfattende fællesskab, robust dokumentation og et bredt udvalg af plugins og udvidelser, hvilket i høj grad fremskynder udvikling og fejlfinding.
  
**Svagheder**:  
- **Kørselshastighed**: Python har en tendens til at være langsommere sammenlignet med sprog som Rust eller Elixir. Til dette anvendelsestilfælde, hvor ydeevne ikke er den primære bekymring, behøver det dog ikke at være afgørende.
- **Skalerbarhed**: selv om Django er meget skalerbart, kan der være udfordringer ved meget høj skala uden omhyggelig optimering (f.eks. ved håndtering af tunge samtidige forespørgsler). Django kan dog stadig skalere effektivt med load balancing og cachingteknikker.

**Vurdering**:  
Django passer godt til kravene om agil udvikling, full stack-understøttelse og AI/ML-kompatibilitet. Dets Python-integration giver problemfri adgang til de datavidenskabsværktøjer og -biblioteker, der er nødvendige for applikationen.

---

### 2. **Ruby on Rails (Ruby)**

**Oversigt**:  
Ruby on Rails (RoR) er et modent full stack-framework til webapplikationer, kendt for sin tilgang med "konvention frem for konfiguration", som letter hurtig udvikling.

**Styrker**:  
- **Full stack**: RoR leveres med indbyggede værktøjer til både backend- og frontendudvikling (f.eks. views, skabeloner, scaffolding), og dets rige bibliotek af gems gør det muligt hurtigt at implementere forskellige funktioner.
- **Agil udvikling**: Ruby on Rails er især kendt for sine hurtige iterationscyklusser, hvilket er en fordel for startups, der vil iterere hurtigt på funktioner. RoR understøtter testdrevet udvikling (TDD) og har et etableret økosystem til agile arbejdsgange.
- **Fællesskab og økosystem**: RoR har et veletableret, stærkt fællesskab og et bredt udvalg af gems, der kan fremskynde udviklingen.
- **Brugervenlighed**: Rails har en meget udviklervenlig syntaks og er kendt for at gøre opgaver som databasemigreringer, Model-View-Controller (MVC)-arkitekturen og rutehåndtering hurtige og nemme.

**Svagheder**:  
- **Ydeevne**: Ruby har en tendens til at have langsommere kørselsydeevne sammenlignet med Python eller Elixir. Selv om RoR kan skalere med den rette infrastruktur, kan Rubys ydeevne blive en flaskehals for applikationer, der kræver tung realtidsbehandling eller høj samtidig trafik.
- **AI/ML-integration**: selv om Ruby har nogle biblioteker til maskinlæring, er det ikke lige så bredt anvendt i AI/ML-fællesskabet som Python. Integration med værktøjer som Jupyter-notebooks er ikke lige så problemfri, hvilket gør Python til et stærkere valg til datatunge applikationer.
  
**Vurdering**:  
Selv om Ruby on Rails udmærker sig ved agil udvikling og hurtig prototyping, kommer det til kort med hensyn til AI/ML-kompatibilitet sammenlignet med Python (Django). Det er et brugbart valg til startups, der prioriterer hurtig iteration frem for dyb integration af dataanalyse.

---

### 3. **Phoenix (Elixir)**

**Oversigt**:  
Phoenix er et webframework bygget med Elixir, et funktionelt programmeringssprog designet til skalerbarhed og samtidighed. Phoenix udnytter Erlang VM, som er kendt for at håndtere massiv samtidighed og fejltolerante systemer.

**Styrker**:  
- **Skalerbarhed og ydeevne**: Phoenix skinner i skalerbarhed og håndtering af høj samtidighed. Det er bygget på Erlang VM, der kan understøtte tusindvis (eller endda millioner) af samtidige forbindelser, hvilket gør det til en stærk kandidat til applikationer, der kræver realtidsdatabehandling eller trafik med høj volumen.
- **Full stack**: Phoenix indeholder alt, hvad der er nødvendigt for at bygge både backend og frontend i en applikation. Det understøtter live views til interaktive UI-opdateringer og indeholder en skabelonmotor.
- **Agil udvikling**: Phoenix er meget modulært, hvilket muliggør hurtig iteration på funktioner. Det passer godt til startups, der skal bevæge sig hurtigt.
- **AI/ML-kompatibilitet**: selv om Elixir har fremspirende biblioteker til maskinlæring, er det ikke lige så bredt understøttet til AI/ML-opgaver som Python. Integration med værktøjer som Jupyter-notebooks ville kræve omveje, da Elixirs økosystem for datavidenskab ikke er lige så modent som Pythons.

**Svagheder**:  
- **AI/ML-økosystem**: Elixir er ikke det primære sprog, der bruges til datavidenskab eller maskinlæring, og økosystemet er ikke lige så modent som Pythons. Derfor bliver integration med værktøjer som Jupyter-notebooks eller populære AI-biblioteker (TensorFlow, PyTorch) besværlig.
- **Indlæringskurve**: hvis teamet ikke er fortrolig med funktionel programmering og Elixir, kan der være en stejlere indlæringskurve.

**Vurdering**:  
Phoenix er et fremragende valg, hvis skalerbarhed og samtidighed er en primær bekymring. I betragtning af prioriteten for AI/ML-kompatibilitet er Phoenix dog måske ikke det bedste match på grund af Elixirs begrænsede økosystem på dette område.

---

### 4. **Loco (Rust)**

**Oversigt**:  
Loco er et webframework bygget med Rust, et systemprogrammeringssprog kendt for ydeevne, hukommelsessikkerhed og samtidighed. Rust bliver stadig mere populært til at bygge højtydende applikationer.

**Styrker**:  
- **Ydeevne**: Rusts primære styrke ligger i dets høje ydeevne og hukommelsessikkerhed, hvilket gør det til et fremragende valg til applikationer, der kræver lavniveaukontrol eller ekstremt høj ydeevne.
- **Samtidighed**: Rusts ejerskabssystem (ownership) sikrer hukommelsessikkerhed og tillader samtidig programmering på en sikker måde, hvilket gør det ideelt til systemer, der skal skalere effektivt og håndtere parallelisme.

**Svagheder**:  
- **Full stack-udvikling**: Loco er, selv om det er lovende, ikke lige så modent som de andre frameworks med hensyn til at levere en komplet full stack-løsning. Det er bedre egnet til backendudvikling, og frontend-økosystemet omkring Rust er stadig under udvikling.
- **Agil udvikling**: udvikling med Rust kan være langsommere sammenlignet med højniveausprog som Python eller Ruby på grund af dets lavere niveau og stejlere indlæringskurve.
- **AI/ML-økosystem**: Rust har ikke det samme omfattende økosystem til AI/ML som Python. Selv om der er voksende biblioteker i Rust til numerisk beregning, er de langt mindre modne end Pythons tilbud, såsom Jupyter-notebooks eller frameworks til maskinlæring.
  
**Vurdering**:  
Selv om Rust og dets framework Loco tilbyder exceptionel ydeevne, gør manglen på full stack-understøttelse, fordele ved agil udvikling og AI/ML-økosystem det mindre ideelt til dette specifikke anvendelsestilfælde. Det er bedre egnet til ydeevnekritiske applikationer end til hurtig webudvikling med integrerede datavidenskabsværktøjer.

---

### Konklusion

Efter at have evalueret mulighederne ud fra projektets krav er **Django (Python)** det mest egnede valg. Det tilbyder følgende fordele:

- **Full stack-funktioner**: Django er et full stack-framework, der integrerer backend- og frontendudvikling.
- **Agil udvikling**: frameworket egner sig godt til hurtig prototyping og iteration, hvilket er afgørende i et startupmiljø.
- **AI/ML-kompatibilitet**: Python er det førende sprog inden for AI/ML, og Djangos kompatibilitet med biblioteker som Jupyter-notebooks sikrer problemfri integration til dataanalyse og databehandling.
- **Fællesskab og økosystem**: Djangos stærke fællesskabsstøtte og omfattende biblioteksøkosystem leverer talrige værktøjer til at fremskynde udviklingen.

Selv om **Ruby on Rails** også er en stærk kandidat til agil udvikling, gør dets begrænsede AI/ML-understøttelse det mindre ideelt til dette specifikke anvendelsestilfælde. **Phoenix (Elixir)** og **Loco (Rust)**, der udmærker sig ved skalerbarhed og ydeevne, kommer til kort med hensyn til AI/ML-integration og full stack-udvikling. Derfor er Django det anbefalede framework til dette projekt.
