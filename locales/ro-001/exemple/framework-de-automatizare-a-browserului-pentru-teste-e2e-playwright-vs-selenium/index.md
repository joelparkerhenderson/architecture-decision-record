## Înregistrare a deciziei de arhitectură: framework de automatizare a browserului pentru teste E2E (Playwright vs Selenium)

### 1. **Context**

Suntem în procesul de selectare a unui framework de automatizare a browserului pentru fluxul nostru de testare end-to-end (E2E). Acest framework va fi parte integrantă din procesele noastre CI/CD, rulând teste care simulează interacțiuni reale ale utilizatorilor cu platforma noastră. Mai exact, testele vor acoperi scenarii precum înregistrarea/autentificarea utilizatorului, încărcarea de fișiere, interacțiunile cu tablouri de bord și descărcarea rapoartelor.

Ca **startup**, ne concentrăm pe **dezvoltarea agilă**, cu nevoia de a itera și a evolua rapid. Echipa noastră lucrează predominant cu **TypeScript** și **Python**, iar posibilitatea de a scrie teste în aceste limbaje este esențială. În plus, platforma conține **grafice interactive și tablouri de bord**, ceea ce face critic ca instrumentul de automatizare să suporte bine interfețe bogate și dinamice.

Cei doi candidați pentru această sarcină sunt **Playwright** și **Selenium**, fiecare cu punctele sale forte și compromisuri. Trebuie să evaluăm aceste framework-uri pe baza funcționalităților și cerințelor prezentate mai jos.

### 2. **Opțiuni luate în considerare**

- **Playwright** (de la Microsoft)
- **Selenium** (de la proiectul Selenium)

### 3. **Factori de decizie**

Factorii care ne influențează decizia sunt următorii:

1. **Dezvoltare agilă**: Instrumentul ales trebuie să permită cicluri de dezvoltare rapide și flexibile.
2. **Suport pentru limbaje**: Echipa noastră are nevoie de suport atât pentru **TypeScript**, cât și pentru **Python**.
3. **Testarea interfețelor interactive**: Capacitatea de a testa fiabil grafice interactive, tablouri de bord și elemente dinamice este esențială.
4. **Viteza de execuție**: Deși nu este o preocupare principală, performanța în fluxurile CI/CD este un aspect de luat în seamă.
5. **Scalabilitate**: Nu planificăm o scalare masivă în viitorul imediat, dar vrem să ne asigurăm că soluția poate face față creșterii viitoare.
6. **Compatibilitate retroactivă**: Sistemele vechi și compatibilitatea cu browsere mai vechi nu sunt critice pentru proiectul nostru în acest moment.
7. **Testare mobilă**: Deși nu este un obiectiv imediat, framework-ul ar trebui să poată testa funcționalități adaptate pentru mobil sau să fie extensibil pentru astfel de cazuri de utilizare.
8. **Testare multi-monitor**: Suportul pentru configurații cu mai multe monitoare este o cerință secundară, mai ales dacă vom ajunge să testăm fluxuri de lucru mai complexe ale utilizatorilor.
9. **Testarea încărcării de fișiere**: Framework-ul trebuie să gestioneze eficient încărcările de fișiere, o cerință de bază a testelor noastre.

### 4. **Criterii de evaluare**

- **Ușurința în utilizare**: Cât de ușor este să scrii și să întreții teste?
- **Suport pentru limbaje**: Suportă framework-ul TypeScript și Python, cele două limbaje pe care echipa noastră le folosește cel mai des?
- **Testarea interfețelor interactive**: Cât de bine gestionează framework-ul interfețe complexe și interactive precum graficele, încărcările de fișiere și datele dinamice?
- **Integrare CI/CD**: Cât de bine se integrează framework-ul în instrumentele și serviciile CI/CD obișnuite?
- **Suport pentru mai multe browsere**: Ce browsere sunt suportate și cât de bine funcționează?
- **Performanță și viteză**: Cât de repede rulează testele, mai ales într-un flux CI/CD?
- **Scalabilitate**: Cât de bine poate scala framework-ul dacă se adaugă mai multe teste sau scenarii mai complexe?
- **Comunitate și ecosistem**: Cât de activă este comunitatea framework-ului? Există multe integrări și extensii disponibile?

### 5. **Considerații**

#### 5.1 **Playwright**

##### **Avantaje**:
1. **API mai inteligent pentru încărcarea fișierelor locale**: API-ul Playwright pentru lucrul cu fișiere locale și pentru încărcarea fișierelor este mai simplu și mai intuitiv. Aceasta ar face testarea încărcării de fișiere mai ușor de implementat și de întreținut.
2. **Sintaxă și generare de cod**: Playwright are o sintaxă mai scurtă și mai concisă. Rezultă mai puțin cod repetitiv, ceea ce îmbunătățește mentenabilitatea și eficiența dezvoltatorilor. În plus, această sintaxă mai scurtă îmbunătățește calitatea codului generat de OpenAI, ușurând generarea automată a scripturilor de test.
3. **Testarea interfețelor interactive**: Playwright excelează la testarea aplicațiilor web dinamice și interactive, precum cele cu grafice bogate, interacțiuni complexe ale utilizatorilor și actualizări în timp real. Gestionează foarte eficient WebSockets, WebRTC, shadow DOM și alte tehnologii web moderne.
4. **Suport pentru mai multe browsere**: Playwright suportă **Chromium**, **WebKit** și **Firefox**. Are performanță consecventă pe aceste browsere, ceea ce ar trebui să acopere majoritatea nevoilor noastre de testare.
5. **Integrare CI/CD**: Playwright se integrează fără probleme cu platformele CI/CD moderne (GitHub Actions, Jenkins etc.). Poate rula teste în paralel pe browsere diferite, optimizând timpii de rulare a testelor și făcându-l potrivit pentru dezvoltarea rapidă.
6. **Rapid și fiabil**: Playwright este în general mai rapid decât Selenium, în special în modul headless, și mai rezistent la elementele web asincrone.

##### **Dezavantaje**:
1. **Testare mobilă limitată**: Deși Playwright suportă emularea mobilă pentru browsere, îi lipsesc capabilitățile native de testare mobilă, precum integrarea Selenium cu Appium pentru testare mobilă reală.
2. **Ecosistem mai mic**: Playwright este încă mai nou și mai puțin consacrat decât Selenium. Deși are o comunitate în creștere rapidă și documentație bună, poate nu are încă vastul ecosistem de pluginuri și integrări pe care îl oferă Selenium.
3. **Suport limitat pentru browsere**: Deși Playwright acoperă principalele browsere moderne (Chrome, Safari, Firefox), suportul său pentru browsere vechi (de exemplu, Internet Explorer) nu este la fel de solid ca cel al Selenium.

#### 5.2 **Selenium**

##### **Avantaje**:
1. **Istorie mai lungă și maturitate**: Selenium există de mult timp și are un istoric dovedit. Este larg folosit în multe echipe și industrii, ceea ce a dus la un vast ecosistem de pluginuri, integrări și resurse.
2. **Suport pentru mai multe browsere și platforme**: Selenium suportă o **mare varietate de browsere** și versiuni, inclusiv **Internet Explorer**, și poate fi integrat și cu diverse instrumente precum **Docker**, **Selenium Grid** și **servicii cloud** pentru testare distribuită.
3. **Testare mobilă**: Selenium, prin integrarea cu **Appium**, este mult mai robust pentru testarea mobilă, inclusiv aplicații Android și iOS. Aceasta îl face alegerea mai bună pentru proiecte cu accent pe mobil sau cu componentă mobilă puternică.
4. **Testare multi-monitor**: Selenium oferă un suport mai bun pentru scenarii care implică **mai multe monitoare** sau interacțiuni complexe cu mai multe ferestre.

##### **Dezavantaje**:
1. **Complexitate**: API-ul Selenium este mai verbos și mai explicit. Deși în unele cazuri poate fi un avantaj, înseamnă mai mult cod de scris și întreținut, ceea ce poate reduce agilitatea dezvoltatorilor — mai ales importantă într-un startup.
2. **Performanță**: Selenium rulează în general mai lent decât Playwright, în special în modul headless. Aceasta ar putea afecta fluxurile CI/CD, mai ales pe măsură ce crește numărul de teste.
3. **Testarea interfețelor interactive**: Selenium nu este la fel de fluid ca Playwright la testarea interfețelor web moderne și interactive, în special cu grafice și actualizări de date în timp real. Necesită mai multă configurare și gestionare pentru a interacționa fiabil cu conținutul dinamic.

### 6. **Rezumatul comparației**

| Caracteristică                   | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Ușurința în utilizare**         | Sintaxă mai scurtă, mai intuitiv pentru interfețe moderne | Mai explicit, necesită mai mult cod repetitiv  |
| **Suport pentru limbaje**         | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Testarea interfețelor interactive** | Excelent pentru interfețe dinamice, în timp real | Gestionează interfețe de bază, dar mai verbos și mai complex pentru interacțiuni bogate |
| **Testarea încărcării de fișiere**| API mai inteligent pentru încărcări de fișiere | API mai verbos, mai puțin intuitiv         |
| **Integrare CI/CD**               | Integrare ușoară cu GitHub Actions, Jenkins   | Integrare puternică cu multe instrumente CI    |
| **Testare mobilă**                | Limitată, doar emulare                        | Suport complet prin Appium               |
| **Suport pentru mai multe browsere** | Chromium, WebKit, Firefox                  | Suport complet pentru browsere principale și vechi |
| **Performanță**                   | Rapid, optimizat pentru testare headless      | Mai lent, în special în modul headless       |
| **Testare multi-monitor**         | Limitată                                      | Suport bun pentru configurații multi-monitor    |
| **Comunitate și ecosistem**       | În creștere, documentație bună                | Mare, matură, ecosistem extins       |

### 7. **Decizie**

După luarea în considerare a cerințelor și a compromisurilor, **Playwright** este alegerea mai bună pentru nevoile noastre actuale. API-ul său mai inteligent pentru testarea încărcării fișierelor locale, sintaxa concisă și suportul puternic pentru testarea interfețelor interactive îl fac o potrivire ideală pentru ciclul nostru de dezvoltare agilă. Faptul că suportă atât **TypeScript**, cât și **Python** este critic pentru echipa noastră, iar abordarea modernă a framework-ului față de testare ne va permite să scriem cod curat și ușor de întreținut.

Deși **Selenium** rămâne un instrument excelent, în special pentru testarea mobilă, suportul pentru browsere vechi și configurațiile multi-monitor, este mai puțin potrivit nevoilor noastre actuale. Verbozitatea, performanța mai lentă și gestionarea mai complexă a interfețelor dinamice, precum graficele, îl fac mai puțin optim pentru cazul nostru de utilizare.

### 8. **Consecințe**

- **Acțiune imediată**: Vom adopta **Playwright** pentru testele noastre E2E, concentrându-ne pe testarea fluxurilor utilizatorilor care implică înregistrare, autentificare, încărcări de fișiere, tablouri de bord și descărcări de rapoarte.
- **Considerații pe termen lung**: Vom urmări evoluția ecosistemului Playwright. Dacă nevoile noastre se schimbă, în special în privința testării mobile sau a suportului pentru browsere vechi, putem reveni la Selenium.
- **Instruire și documentație**: Echipele de dezvoltare vor trebui să se familiarizeze cu API-ul Playwright, în special pentru gestionarea interfețelor dinamice și a încărcărilor de fișiere.
- **Migrare**: Testele Selenium existente (dacă există) vor fi migrate treptat la Playwright.

### 9. **Considerații pentru viitor**
