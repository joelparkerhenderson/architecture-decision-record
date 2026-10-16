# Architektūros sprendimo įrašas: interneto programų karkasas „viskas viename“, full stack, startuolio produktui

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Pagrindinis tikslas:**  
Sukurti interneto programą, kurioje mokantys klientai galėtų prisijungti, įkelti failus, apdoroti duomenis ir peržiūrėti ataskaitas, sutelkiant dėmesį į lanksčiąjį kūrimą, full stack funkcionalumą ir stiprų suderinamumą su DI / mašininio mokymosi įrankiais, ypač Project Jupyter užrašų knygelėmis.

### Kontekstas ir reikalavimai:

1. **Lankstusis kūrimas (aukštas prioritetas)**: kaip startuoliui, mums reikia sparčios iteracijos ir lankstumo. Lanksčiosios praktikos, tokios kaip greitas prototipų kūrimas, iteracinis kūrimas ir prisitaikymas prie pokyčių, yra mūsų kūrimo ciklo pagrindas.

2. **Full-stack karkasas (aukštas prioritetas)**: siekiame sumažinti pridėtines sąnaudas pasirinkdami karkasą, galintį efektyviai tvarkyti ir galinę, ir priekinę dalį, taip sumažindami poreikį atskiriems priekinės dalies karkasams.

3. **Suderinamumas su DI / ML įrankiais (aukštas prioritetas)**: būtina galėti lengvai integruotis su duomenų analizės įrankiais, tokiais kaip Jupyter užrašų knygelės, ir Python duomenų mokslo ekosistema (NumPy, Pandas, TensorFlow ir kt.). Tai palengvintų efektyvų duomenų apdorojimą ir ataskaitų rengimą.

4. **Mažos svarbos kriterijai**:
   - **Vykdymo greitis**: nors našumas yra svarbus, pradžioje jis nėra svarbiausias veiksnys, nes labiau rūpi kūrimo greitis ir funkcijų išbaigtumas.
   - **Mastelio keitimas**: tikimės augimo, bet mastelio keitimo klausimus galima spręsti vėliau, ir dabar tai nėra pagrindinis reikalavimas.
   - **Atgalinis suderinamumas**: sutelkiame dėmesį į dabartines technologijas ir ypač nesirūpiname atgaliniu suderinamumu su paveldėtomis sistemomis.

### Įvertinti karkasai:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Apžvalga**:  
Django yra aukšto lygio Python interneto karkasas, skatinantis spartų kūrimą ir švarų, pragmatišką dizainą. Jis žinomas dėl „viskas viename“ (angl. batteries included) filosofijos, o tai reiškia, kad iškart apima daug funkcijų, tokių kaip autentifikavimas, maršrutizavimas, ORM ir formų tvarkymas.

**Stiprybės**:  
- **Full-stack**: Django yra išsamus full-stack karkasas, galintis patenkinti ir galinės, ir priekinės dalies poreikius su integruotomis funkcijomis (pvz., šablonų variklis, administravimo sąsaja).
- **Lankstusis kūrimas**: gerai apibrėžta Django struktūra ir konvencijos leidžia sparčiai kurti ir prisitaikyti, o tai labai svarbu startuolio aplinkoje. Karkasas turi puikią dokumentaciją ir turtingą trečiųjų šalių paketų ekosistemą, kuri pagreitina kūrimą.
- **DI / ML integracija**: Python ekosistema neprilygstama duomenų mokslo ir mašininio mokymosi srityje. Django, būdamas Python pagrindu, sklandžiai integruojasi su tokiais įrankiais kaip Jupyter užrašų knygelės, Pandas, NumPy, TensorFlow ir scikit-learn.
- **Bendruomenė ir ekosistema**: Django turi plačią bendruomenę, tvirtą dokumentaciją ir platų papildinių bei plėtinių spektrą, o tai žymiai pagreitina kūrimą ir problemų sprendimą.
  
**Silpnybės**:  
- **Vykdymo greitis**: Python paprastai lėtesnė nei tokios kalbos kaip Rust ar Elixir. Tačiau šiuo naudojimo atveju, kai našumas nėra pagrindinis rūpestis, tai gali nebūti lemiama kliūtis.
- **Mastelio keitimas**: nors Django labai gerai keičia mastelį, labai dideliu mastu gali kilti sunkumų be kruopštaus optimizavimo (pvz., tvarkant daug lygiagrečių užklausų). Tačiau Django vis tiek galima veiksmingai plėsti naudojant apkrovos balansavimo ir spartinančiosios atminties (angl. caching) metodus.

**Išvada**:  
Django gerai atitinka lanksčiojo kūrimo, full-stack palaikymo ir DI / ML suderinamumo reikalavimus. Jo Python integracija suteikia sklandžią prieigą prie programai būtinų duomenų mokslo įrankių ir bibliotekų.

---

### 2. **Ruby on Rails (Ruby)**

**Apžvalga**:  
Ruby on Rails (RoR) yra brandus, full-stack interneto programų karkasas, žinomas dėl požiūrio „konvencija vietoj konfigūracijos“, kuris palengvina spartų kūrimą.

**Stiprybės**:  
- **Full-stack**: RoR turi integruotus įrankius tiek galinės, tiek priekinės dalies kūrimui (pvz., vaizdai, šablonai, karkasų generavimas), o turtinga jo gem bibliotekų kolekcija leidžia greitai įgyvendinti įvairias funkcijas.
- **Lankstusis kūrimas**: Ruby on Rails ypač žinomas dėl greitų iteracijos ciklų, o tai naudinga startuoliams, norintiems greitai iteruoti funkcijas. RoR palaiko testais grįstą kūrimą (TDD) ir turi susiformavusią lanksčiųjų darbo eigų ekosistemą.
- **Bendruomenė ir ekosistema**: RoR turi gerai įsitvirtinusią, stiprią bendruomenę ir platų gem asortimentą, galintį pagreitinti kūrimą.
- **Naudojimo paprastumas**: Rails turi labai programuotojams draugišką sintaksę ir žinomas tuo, kad tokias užduotis kaip duomenų bazės migracijos, Model-View-Controller (MVC) architektūra ir maršrutų tvarkymas daro greitas ir paprastas.

**Silpnybės**:  
- **Našumas**: Ruby paprastai turi lėtesnį vykdymo našumą nei Python ar Elixir. Nors RoR gali keisti mastelį su tinkama infrastruktūra, Ruby našumas gali tapti kliūtimi programoms, kurioms reikia intensyvaus realaus laiko apdorojimo ar didelio lygiagretaus srauto.
- **DI / ML integracija**: nors Ruby turi kai kurių mašininio mokymosi bibliotekų, jis nėra taip plačiai priimtas DI / ML bendruomenėje kaip Python. Integracija su tokiais įrankiais kaip Jupyter užrašų knygelės nėra tokia sklandi, todėl Python yra stipresnis pasirinkimas daug duomenų naudojančioms programoms.
  
**Išvada**:  
Nors Ruby on Rails puikiai tinka lanksčiajam kūrimui ir sparčiam prototipų kūrimui, jis nusileidžia DI / ML suderinamumo požiūriu, palyginti su Python (Django). Tai tinkamas pasirinkimas startuoliams, kurie teikia pirmenybę greitai iteracijai, o ne gilesnei duomenų analizės integracijai.

---

### 3. **Phoenix (Elixir)**

**Apžvalga**:  
Phoenix yra interneto karkasas, sukurtas su Elixir – funkcine programavimo kalba, skirta mastelio keitimui ir lygiagretumui. Phoenix naudoja Erlang VM, žinomą dėl didžiulio lygiagretumo ir atsparių gedimams sistemų tvarkymo.

**Stiprybės**:  
- **Mastelio keitimas ir našumas**: Phoenix blizga mastelio keitimo ir didelio lygiagretumo tvarkymo srityse. Jis sukurtas ant Erlang VM, kuri gali palaikyti tūkstančius (ar net milijonus) lygiagrečių ryšių, todėl yra stiprus kandidatas programoms, kurioms reikia realaus laiko duomenų apdorojimo ar didelės apimties srauto.
- **Full-stack**: Phoenix apima viską, ko reikia programos galinei ir priekinei daliai sukurti. Jis palaiko gyvuosius vaizdus (live views) interaktyviems UI atnaujinimams ir turi šablonų variklį.
- **Lankstusis kūrimas**: Phoenix yra labai modulinis, leidžiantis sparčiai iteruoti funkcijas. Jis gerai tinka startuoliams, kuriems reikia judėti greitai.
- **DI / ML suderinamumas**: nors Elixir turi atsirandančių mašininio mokymosi bibliotekų, jis nėra taip plačiai palaikomas DI / ML užduotims kaip Python. Integracijai su tokiais įrankiais kaip Jupyter užrašų knygelės reiktų apėjimo būdų, nes Elixir duomenų mokslo ekosistema nėra tokia brandi kaip Python.

**Silpnybės**:  
- **DI / ML ekosistema**: Elixir nėra pagrindinė kalba, naudojama duomenų moksle ar mašininiame mokyme, o ekosistema nėra tokia brandi kaip Python. Todėl integracija su tokiais įrankiais kaip Jupyter užrašų knygelės ar populiarios DI bibliotekos (TensorFlow, PyTorch) bus sudėtinga.
- **Mokymosi kreivė**: jei komanda nėra susipažinusi su funkciniu programavimu ir Elixir, mokymosi kreivė gali būti statesnė.

**Išvada**:  
Phoenix yra puikus pasirinkimas, jei mastelio keitimas ir lygiagretumas yra pagrindinis rūpestis. Tačiau atsižvelgiant į prioritetą DI / ML suderinamumui, Phoenix gali būti ne pats tinkamiausias dėl ribotos Elixir ekosistemos šioje srityje.

---

### 4. **Loco (Rust)**

**Apžvalga**:  
Loco yra interneto karkasas, sukurtas su Rust – sistemų programavimo kalba, žinoma dėl našumo, atminties saugumo ir lygiagretumo. Rust vis populiaresnė kuriant didelio našumo programas.

**Stiprybės**:  
- **Našumas**: pagrindinė Rust stiprybė yra didelis našumas ir atminties saugumas, todėl ji yra puikus pasirinkimas programoms, kurioms reikia žemo lygio kontrolės ar itin didelio našumo.
- **Lygiagretumas**: Rust nuosavybės sistema užtikrina atminties saugumą ir kartu leidžia saugų lygiagretų programavimą, todėl idealiai tinka sistemoms, kurios turi efektyviai keisti mastelį ir tvarkyti lygiagretumą.

**Silpnybės**:  
- **Full-stack kūrimas**: Loco, nors ir perspektyvus, nėra toks brandus kaip kiti karkasai teikiant išsamų full-stack sprendimą. Jis labiau tinka galinės dalies kūrimui, o priekinės dalies ekosistema aplink Rust dar tik formuojasi.
- **Lankstusis kūrimas**: kurti su Rust gali būti lėčiau nei su aukštesnio lygio kalbomis, tokiomis kaip Python ar Ruby, dėl jos žemesnio lygio pobūdžio ir statesnės mokymosi kreivės.
- **DI / ML ekosistema**: Rust neturi tokios plačios DI / ML ekosistemos kaip Python. Nors Rust auga skaitinių skaičiavimų bibliotekų, jos yra gerokai mažiau brandžios nei Python pasiūlymai, tokie kaip Jupyter užrašų knygelės ar mašininio mokymosi karkasai.
  
**Išvada**:  
Nors Rust ir jos karkasas Loco siūlo išskirtinį našumą, full-stack palaikymo, lanksčiojo kūrimo privalumų ir DI / ML ekosistemos trūkumas daro ją mažiau idealią šiam konkrečiam naudojimo atvejui. Ji labiau tinka našumui kritiškoms programoms, o ne spartiam interneto kūrimui su integruotais duomenų mokslo įrankiais.

---

### Išvada

Įvertinę variantus pagal projekto reikalavimus, nusprendėme, kad **Django (Python)** yra tinkamiausias pasirinkimas. Jis siūlo šiuos privalumus:

- **Full-stack galimybės**: Django yra full-stack karkasas, integruojantis ir galinės, ir priekinės dalies kūrimą.
- **Lankstusis kūrimas**: karkasas gerai tinka sparčiam prototipų kūrimui ir iteracijai, o tai būtina startuolio aplinkoje.
- **DI / ML suderinamumas**: Python yra pirmaujanti DI / ML kalba, o Django suderinamumas su tokiomis bibliotekomis kaip Jupyter užrašų knygelės užtikrina sklandžią integraciją duomenų analizei ir apdorojimui.
- **Bendruomenė ir ekosistema**: stipri Django bendruomenės parama ir plati bibliotekų ekosistema suteikia daug įrankių kūrimui pagreitinti.

Nors **Ruby on Rails** taip pat yra stiprus kandidatas lanksčiajam kūrimui, jo ribotas DI / ML palaikymas daro jį mažiau idealų šiam konkrečiam naudojimo atvejui. **Phoenix (Elixir)** ir **Loco (Rust)**, nors ir puikūs mastelio keitimo bei našumo požiūriu, nusileidžia DI / ML integracijos ir full-stack kūrimo požiūriu. Todėl šiam projektui rekomenduojamas karkasas yra Django.
