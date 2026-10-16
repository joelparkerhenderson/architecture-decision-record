## Arhitektūras lēmuma ieraksts: pārlūkprogrammas automatizācijas ietvars E2E testēšanai (Playwright vai Selenium)

### 1. **Konteksts**

Mēs izvēlamies pārlūkprogrammas automatizācijas ietvaru savam pilna cikla (end-to-end, E2E) testēšanas cauruļvadam. Šis ietvars būs neatņemama mūsu CI/CD procesu daļa, izpildot testus, kas simulē reālu lietotāju mijiedarbību mūsu platformā. Testi īpaši aptvers tādus scenārijus kā lietotāja reģistrēšanās/pieteikšanās, failu augšupielāde, mijiedarbība ar informācijas paneli un pārskatu lejupielāde.

Kā **jaunuzņēmums** mēs koncentrējamies uz **aģilu izstrādi**, ar nepieciešamību ātri iterēt un attīstīties. Mūsu komanda pārsvarā strādā ar **TypeScript** un **Python**, un spēja rakstīt testus šajās valodās ir būtiska. Turklāt platformā ir **interaktīvas diagrammas un informācijas paneļi**, tāpēc ir kritiski svarīgi, lai automatizācijas rīks labi atbalstītu bagātas, dinamiskas lietotāja saskarnes.

Divi pretendenti šim uzdevumam ir **Playwright** un **Selenium**, katram ar savām stiprajām pusēm un kompromisiem. Mums šie ietvari jāizvērtē, pamatojoties uz tālāk izklāstītajām funkcijām un prasībām.

### 2. **Apsvērtās iespējas**

- **Playwright** (Microsoft)
- **Selenium** (projekts Selenium)

### 3. **Lēmuma virzītājspēki**

Faktori, kas ietekmē mūsu lēmumu, ir šādi:

1. **Aģila izstrāde**: izvēlētajam rīkam jānodrošina ātri, elastīgi izstrādes cikli.
2. **Valodu atbalsts**: mūsu komandai nepieciešams atbalsts gan **TypeScript**, gan **Python**.
3. **Interaktīvas UI testēšana**: būtiska ir spēja uzticami testēt interaktīvas diagrammas, informācijas paneļus un dinamiskus elementus.
4. **Izpildlaika ātrums**: lai gan tas nav galvenā bažas, veiktspēja CI/CD cauruļvados ir apsvērums.
5. **Mērogojamība**: tuvākajā nākotnē mēs neplānojam masveida mērogošanu, taču vēlamies nodrošināt, ka risinājums var apstrādāt turpmāko izaugsmi.
6. **Atpakaļsaderība**: mantotās sistēmas un saderība ar vecākām pārlūkprogrammām mūsu projektam šobrīd nav kritiskas.
7. **Mobilo ierīču testēšana**: lai gan šobrīd tā nav tūlītēja prioritāte, ietvaram jāspēj testēt mobilajām ierīcēm atsaucīgas funkcijas vai jābūt paplašināmam šādiem lietošanas gadījumiem.
8. **Vairāku monitoru testēšana**: atbalsts vairāku monitoru konfigurācijām ir sekundāra prasība, īpaši, ja mēs kādreiz mērogosim uz sarežģītāku lietotāju darbplūsmu testēšanu.
9. **Failu augšupielādes testēšana**: ietvaram efektīvi jāapstrādā failu augšupielādes, kas ir mūsu testēšanas vajadzību pamatprasība.

### 4. **Izvērtēšanas kritēriji**

- **Lietošanas vienkāršība**: cik viegli ir rakstīt un uzturēt testus?
- **Valodu atbalsts**: vai ietvars atbalsta TypeScript un Python, divas valodas, ko mūsu komanda izmanto visbiežāk?
- **Interaktīvas UI testēšana**: cik labi ietvars apstrādā sarežģītas, interaktīvas lietotāja saskarnes, piemēram, diagrammas, failu augšupielādes un dinamiskus datus?
- **CI/CD integrācija**: cik labi ietvars integrējas parastajos CI/CD rīkos un pakalpojumos?
- **Daudzu pārlūkprogrammu atbalsts**: kuras pārlūkprogrammas tiek atbalstītas un cik labi tās darbojas?
- **Veiktspēja un ātrums**: cik ātri tiek izpildīti testi, īpaši CI/CD cauruļvadā?
- **Mērogojamība**: cik labi ietvars var mērogoties, ja tiek pievienoti vairāk testu vai sarežģītāki scenāriji?
- **Kopiena un ekosistēma**: cik aktīva ir ietvara kopiena? Vai ir pieejams daudz integrāciju un paplašinājumu?

### 5. **Apsvērumi**

#### 5.1 **Playwright**

##### **Priekšrocības**:
1. **Gudrāks API lokālo failu augšupielādei**: Playwright API mijiedarbībai ar lokāliem failiem un failu augšupielādes veikšanai ir vienkāršāks un intuitīvāks. Tas atvieglotu failu augšupielādes testēšanas īstenošanu un uzturēšanu.
2. **Sintakse un koda ģenerēšana**: Playwright ir īsāka, kodolīgāka sintakse. Tas rada mazāk šablonkoda, kas uzlabo uzturamību un izstrādātāju efektivitāti. Turklāt šī īsākā sintakse uzlabo OpenAI koda ģenerēšanas kvalitāti, atvieglojot testu skriptu automātisku ģenerēšanu.
3. **Interaktīvas UI testēšana**: Playwright izceļas dinamisku, interaktīvu tīmekļa lietojumprogrammu testēšanā, piemēram, ar bagātām diagrammām, sarežģītu lietotāju mijiedarbību un reāllaika atjauninājumiem. Tas ļoti efektīvi apstrādā WebSockets, WebRTC, ēnu DOM (shadow DOM) un citas modernas tīmekļa tehnoloģijas.
4. **Daudzu pārlūkprogrammu atbalsts**: Playwright atbalsta **Chromium**, **WebKit** un **Firefox**. Tam ir konsekventa veiktspēja šajās pārlūkprogrammās, kam vajadzētu aptvert lielāko daļu mūsu testēšanas vajadzību.
5. **CI/CD integrācija**: Playwright nevainojami integrējas ar modernām CI/CD platformām (GitHub Actions, Jenkins utt.). Tas var izpildīt testus paralēli dažādās pārlūkprogrammās, optimizējot testu izpildes laikus un padarot to piemērotu ātrai izstrādei.
6. **Ātrs un uzticams**: Playwright kopumā ir ātrāks par Selenium, īpaši bezgalvas (headless) režīmā, un noturīgāks, strādājot ar asinhroniem tīmekļa elementiem.

##### **Trūkumi**:
1. **Ierobežota mobilo ierīču testēšana**: lai gan Playwright atbalsta mobilo ierīču emulāciju pārlūkprogrammām, tam trūkst dabisku mobilo ierīču testēšanas iespēju, piemēram, Selenium integrācija ar Appium īstai mobilo ierīču testēšanai.
2. **Mazāka ekosistēma**: Playwright joprojām ir jaunāks un mazāk iedibināts nekā Selenium. Lai gan tam ir strauji augoša kopiena un laba dokumentācija, tam vēl var nebūt tik plašas spraudņu un integrāciju ekosistēmas, ko piedāvā Selenium.
3. **Ierobežots pārlūkprogrammu atbalsts**: lai gan Playwright aptver galvenās modernās pārlūkprogrammas (Chrome, Safari, Firefox), tā atbalsts mantotajām pārlūkprogrammām (piem., Internet Explorer) nav tik robusts kā Selenium.

#### 5.2 **Selenium**

##### **Priekšrocības**:
1. **Ilgāka vēsture un nobriedums**: Selenium pastāv jau ilgu laiku, un tam ir pierādīta pieredze. To plaši izmanto daudzās komandās un nozarēs, kas ir novedis pie plašas spraudņu, integrāciju un resursu ekosistēmas.
2. **Daudzu pārlūkprogrammu un platformu atbalsts**: Selenium atbalsta **plašu pārlūkprogrammu klāstu** un versijas, tostarp **Internet Explorer**, un to var integrēt arī ar dažādiem rīkiem, piemēram, **Docker**, **Selenium Grid** un **mākoņpakalpojumiem** sadalītai testēšanai.
3. **Mobilo ierīču testēšana**: Selenium, izmantojot integrāciju ar **Appium**, ir daudz robustāks mobilo ierīču testēšanai, ieskaitot gan Android, gan iOS lietojumprogrammas. Tas padara to par labāku izvēli projektiem ar mobilo ierīču prioritāti vai lielu mobilo ierīču īpatsvaru.
4. **Vairāku monitoru testēšana**: Selenium nodrošina labāku atbalstu scenārijiem, kas ietver **vairākus monitorus** vai sarežģītu mijiedarbību ar vairākiem logiem.

##### **Trūkumi**:
1. **Sarežģītība**: Selenium API ir daudzvārdīgāks un tiešāks. Lai gan dažos gadījumos tā var būt priekšrocība, tas nozīmē vairāk koda rakstīšanai un uzturēšanai, kas var mazināt izstrādātāju veiklību – īpaši svarīgi jaunuzņēmuma vidē.
2. **Veiktspēja**: Selenium parasti darbojas lēnāk nekā Playwright, īpaši bezgalvas režīmā. Tas varētu ietekmēt CI/CD cauruļvadus, īpaši, palielinoties testu skaitam.
3. **Interaktīvas UI testēšana**: Selenium nav tik gluds kā Playwright, testējot modernas, interaktīvas tīmekļa lietotāja saskarnes, īpaši ar diagrammām un reāllaika datu atjauninājumiem. Lai uzticami mijiedarbotos ar dinamisku saturu, nepieciešams vairāk iestatījumu un apstrādes.

### 6. **Salīdzinājuma kopsavilkums**

| Funkcija                          | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Lietošanas vienkāršība**        | Īsāka sintakse, intuitīvāks modernām UI       | Tiešāks, nepieciešams vairāk šablonkoda   |
| **Valodu atbalsts**               | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Interaktīvas UI testēšana**     | Teicams dinamiskām, reāllaika UI              | Apstrādā pamata UI, bet daudzvārdīgāk un sarežģītāk bagātai mijiedarbībai |
| **Failu augšupielādes testēšana** | Gudrāks API failu augšupielādei               | Daudzvārdīgāks, mazāk intuitīvs API       |
| **CI/CD integrācija**             | Viegla integrācija ar GitHub Actions, Jenkins | Spēcīga integrācija ar daudziem CI rīkiem |
| **Mobilo ierīču testēšana**       | Ierobežota, tikai emulācija                   | Pilns atbalsts ar Appium                  |
| **Daudzu pārlūkprogrammu atbalsts** | Chromium, WebKit, Firefox                   | Pilns atbalsts galvenajās un mantotajās pārlūkprogrammās |
| **Veiktspēja**                    | Ātrs, optimizēts bezgalvas testēšanai         | Lēnāks, īpaši bezgalvas režīmā            |
| **Vairāku monitoru testēšana**    | Ierobežota                                    | Labs atbalsts vairāku monitoru iestatījumiem |
| **Kopiena un ekosistēma**         | Augoša, laba dokumentācija                    | Liela, nobriedusi, plaša ekosistēma       |

### 7. **Lēmums**

Pēc prasību un kompromisu apsvēršanas **Playwright** ir labāka izvēle mūsu pašreizējām vajadzībām. Tā gudrākais API lokālo failu augšupielādes testēšanai, kodolīgā sintakse un spēcīgais atbalsts interaktīvas UI testēšanai padara to par ideāli piemērotu mūsu aģilajam izstrādes ciklam. Fakts, ka tas atbalsta gan **TypeScript**, gan **Python**, ir kritisks mūsu komandai, un ietvara moderna pieeja testēšanai ļaus mums rakstīt tīru, uzturamu kodu.

Lai gan **Selenium** joprojām ir lielisks rīks, īpaši mobilo ierīču testēšanai, mantoto pārlūkprogrammu atbalstam un vairāku monitoru iestatījumiem, tas ir mazāk piemērots mūsu pašreizējām vajadzībām. Tā daudzvārdība, lēnākā veiktspēja un sarežģītāka dinamisku UI, piemēram, diagrammu, apstrāde padara to mazāk optimālu mūsu lietošanas gadījumam.

### 8. **Sekas**

- **Tūlītēja darbība**: mēs pieņemsim **Playwright** savai E2E testēšanai, koncentrējoties uz lietotāju plūsmu testēšanu, kas ietver reģistrēšanos, pieteikšanos, failu augšupielādes, informācijas paneļus un pārskatu lejupielādes.
- **Ilgtermiņa apsvērumi**: mēs sekosim Playwright ekosistēmas attīstībai. Ja mūsu vajadzības mainīsies, īpaši attiecībā uz mobilo ierīču testēšanu vai mantoto pārlūkprogrammu atbalstu, mēs varētu atkal apsvērt Selenium.
- **Apmācība un dokumentācija**: izstrādes komandām būs jāiepazīstas ar Playwright API, īpaši dinamisku UI un failu augšupielāžu apstrādei.
- **Migrācija**: esošie Selenium testi (ja tādi ir) tiks pakāpeniski migrēti uz Playwright.

### 9. **Turpmākie apsvērumi**
