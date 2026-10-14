# Înregistrarea deciziilor de arhitectură (ADR)

O înregistrare a deciziilor de arhitectură (ADR) este un document care consemnează o decizie arhitecturală importantă luată, împreună cu contextul și consecințele ei.

> [!IMPORTANT]
> Efectuează propria verificare riguroasă a acestor resurse înainte de a le folosi în orice sisteme critice.

Cuprins:

- [Ce este o înregistrare a deciziilor de arhitectură?](#ce-este-o-înregistrare-a-deciziilor-de-arhitectură)
- [Cum să începi să folosești ADR-uri](#cum-să-începi-să-folosești-adr-uri)
- [Cum să începi să folosești ADR-uri cu instrumente](#cum-să-începi-să-folosești-adr-uri-cu-instrumente)
- [Cum să începi să folosești ADR-uri cu git](#cum-să-începi-să-folosești-adr-uri-cu-git)
- [Abilități Claude Code pentru ADR](#abilități-claude-code-pentru-adr)
- [Convenții de denumire a fișierelor ADR](#convenții-de-denumire-a-fișierelor-adr)
- [Sugestii pentru scrierea unor ADR bune](#sugestii-pentru-scrierea-unor-adr-bune)
- [Șabloane exemplu de ADR](#șabloane-exemplu-de-adr)
- [Sfaturi de lucru în echipă pentru ADR](#sfaturi-de-lucru-în-echipă-pentru-adr)
- [Întrebări despre munca în echipă pentru ADR](#întrebări-despre-munca-în-echipă-pentru-adr)
- [Concepte pentru pasul următor pentru ADR](#concepte-pentru-pasul-următor-pentru-adr)
- [Diagrame, vederi și puncte de vedere de arhitectură](#diagrame-vederi-și-puncte-de-vedere-de-arhitectură)
- [Funcții de adecvare pentru decizii ca cod](#funcții-de-adecvare-pentru-decizii-ca-cod)
- [Bariere de decizie pentru pull request-uri](#bariere-de-decizie-pentru-pull-request-uri)
- [Mai multe informații](#mai-multe-informații)

Șabloane:

- [Șablon de înregistrare a deciziilor de Jeff Tyree și Art Akerman](sabloane/sablon-de-inregistrare-a-deciziilor-jeff-tyree-si-art-akerman/)
- [Șablon de înregistrare a deciziilor de Michael Nygard](sabloane/sablon-de-inregistrare-a-deciziilor-michael-nygard/)
- [Șablon de înregistrare a deciziilor de la EdgeX](sabloane/sablon-de-inregistrare-a-deciziilor-edgex/)
- [Șablon de înregistrare a deciziilor de la arc42](sabloane/sablon-de-inregistrare-a-deciziilor-arc42/)
- [Șablon de înregistrare a deciziilor pentru tiparul alexandrin](sabloane/sablon-de-inregistrare-a-deciziilor-tipar-alexandrin/)
- [Șablon de înregistrare a deciziilor pentru studiul de caz de afaceri](sabloane/sablon-de-inregistrare-a-deciziilor-studiu-de-caz-de-afaceri/)
- [Șablon de înregistrare a deciziilor al proiectului MADR](sabloane/sablon-de-inregistrare-a-deciziilor-proiectul-madr/)
- [Șablon de înregistrare a deciziilor cu Planguage](sabloane/sablon-de-inregistrare-a-deciziilor-cu-planguage/)
- [Șablon de înregistrare a deciziilor de Paulo Merson](https://github.com/pmerson/ADR-template)
- [Șablon de înregistrare a deciziilor de Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Șablon de înregistrare a deciziilor de Gareth Morgan](sabloane/sablon-de-inregistrare-a-deciziilor-gareth-morgan/)
- [Șablon de înregistrare a deciziilor de la GIG Cymru NHS Wales](sabloane/sablon-de-inregistrare-a-deciziilor-gig-cymru-nhs-wales/)
- [Șablon de înregistrare a deciziilor pentru Deciziile Tehnice Importante (ITD) de Ignacio Larrañaga](sabloane/sablon-de-inregistrare-a-deciziilor-tehnice-importante/)

Exemple:

- [Framework CSS](exemple/framework-css/)
- [Configurarea variabilelor de mediu](exemple/configurarea-variabilelor-de-mediu/)
- [Metrici, monitoare, alerte](exemple/metrici-monitoare-alerte/)
- [Microsoft Azure DevOps](exemple/microsoft-azure-devops/)
- [Monorepo sau multirepo](exemple/monorepo-sau-multirepo/)
- [Limbaje de programare](exemple/limbaje-de-programare/)
- [Stocarea secretelor](exemple/stocarea-secretelor/)
- [Formatul marcajului de timp](exemple/formatul-marcajului-de-timp/)
- [Multe altele...](exemple/)

## Ce este o înregistrare a deciziilor de arhitectură?

O **înregistrare a deciziilor de arhitectură** (engl. architecture decision record, ADR) este un document care consemnează o decizie arhitecturală importantă luată, împreună cu contextul și consecințele ei.

O **decizie de arhitectură** (engl. architecture decision, AD) este o alegere de proiectare software care răspunde unei cerințe semnificative.

Un **jurnal al deciziilor de arhitectură** (engl. architecture decision log, ADL) este colecția tuturor ADR-urilor create și întreținute pentru un anumit proiect (sau o anumită organizație).

O **cerință semnificativă pentru arhitectură** (engl. architecturally-significant requirement, ASR) este o cerință care are un efect măsurabil asupra arhitecturii unui sistem software.

Toate acestea țin de domeniul **managementului cunoștințelor de arhitectură** (engl. architecture knowledge management, AKM).

Scopul acestui document este să ofere o prezentare rapidă a ADR-urilor, a modului de creare a lor și a locurilor în care se pot găsi mai multe informații.

Abrevieri:

  * **AD**: decizie de arhitectură

  * **ADL**: jurnal al deciziilor de arhitectură

  * **ADR**: înregistrare a deciziilor de arhitectură

  * **AKM**: managementul cunoștințelor de arhitectură

  * **ASR**: cerință semnificativă pentru arhitectură

## Cum să începi să folosești ADR-uri

Pentru a începe să folosești ADR-uri, discută cu colegii tăi despre următoarele domenii.

Identificarea deciziilor:

  * Cât de urgentă și cât de importantă este decizia de arhitectură?

  * Trebuie luată acum sau poate aștepta până când se știe mai mult?

  * Atât experiența personală și colectivă, cât și metodele și practicile de proiectare recunoscute pot ajuta la identificarea deciziilor.

  * În mod ideal, ține o listă de decizii de luat, care o completează pe cea a sarcinilor produsului.

Luarea deciziilor:

  * Există numeroase tehnici de luare a deciziilor, atât generale, cât și specifice arhitecturii software, de exemplu maparea dialogului (engl. dialogue mapping).

  * Luarea deciziilor în grup este un subiect activ de cercetare.

Punerea în aplicare și impunerea deciziilor:

  * Deciziile de arhitectură sunt folosite în proiectarea software; de aceea trebuie comunicate părților interesate ale sistemului care îl finanțează, îl dezvoltă și îl operează, și acceptate de acestea.

  * Stilurile de codare în care arhitectura este evidentă și analizele de cod axate pe aspecte și decizii arhitecturale sunt două practici conexe.

  * Deciziile de arhitectură trebuie, de asemenea, (re)luate în considerare la modernizarea unui sistem software în cadrul evoluției software.

Partajarea deciziilor (opțional):

  * Multe decizii de arhitectură se repetă de la un proiect la altul.

  * De aceea, experiențele cu deciziile anterioare, bune sau rele, pot fi active reutilizabile valoroase atunci când se aplică o strategie explicită de management al cunoștințelor.

Documentarea deciziilor:

  * Există multe șabloane și instrumente pentru consemnarea deciziilor.

  * Vezi comunitățile agile, de exemplu ADR-urile lui M. Nygard.

  * Vezi procesele tradiționale de inginerie software și de proiectare a arhitecturii, de exemplu structurile de tabele propuse de IBM UMF și de Tyree și Akerman de la CapitalOne.

Pentru mai multe informații:

  * Pașii de mai sus sunt preluați din articolul Wikipedia [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Cum să începi să folosești ADR-uri cu instrumente

- [MySpec](https://myspec.dev) — Platformă automatizată de specificații și decizii de arhitectură, care structurează constituția proiectului, arhitectura tehnică și ADR-urile în Markdown curat, servit prin MCP.

Poți începe să folosești ADR-uri cu instrumente în orice mod dorești.

De exemplu:

  * Dacă îți place Google Drive și editarea online, poți crea un document Google sau o foaie de calcul Google.

  * Dacă îți place controlul versiunilor codului sursă, cum ar fi git, poți crea un fișier pentru fiecare ADR.

  * Dacă îți plac instrumentele de planificare a proiectelor, cum ar fi Atlassian Jira, poți folosi modulul de planificare al instrumentului.

  * Dacă îți plac wiki-urile, cum ar fi MediaWiki, poți crea un wiki cu ADR-uri.

## Cum să începi să folosești ADR-uri cu git

Dacă îți place controlul versiunilor cu git, iată cum ne place nouă să începem să folosim ADR-uri cu git într-un proiect software obișnuit, cu cod sursă.

Creează un director pentru fișierele ADR:

```sh
$ mkdir adr
```

Pentru fiecare ADR, creează un fișier text, de exemplu `choose-database.md`:

```sh
$ vi choose-database.md
```

Scrie în ADR orice dorești. Vezi șabloanele din acest depozit pentru idei.

Fă commit ADR-ului în depozitul tău git.

## Abilități Claude Code pentru ADR

Acest depozit livrează două abilități (skills) pentru [Claude Code](https://claude.com/claude-code) în [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), astfel încât un agent de programare AI să poată scrie și întreține ADR-uri așa cum recomandă acest proiect:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — de uz general, pentru oricine scrie un ADR în orice proiect. Ajută să decizi dacă o decizie necesită un ADR, creează un director `adr/` sau `decisions/`, denumește fișierul, alege un șablon dintre cele unsprezece schelete incluse și scrie secțiuni solide Context/Decizie/Consecințe.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — special pentru responsabilii de întreținere ai acestui depozit. Documentează structura depozitului, convenția de oglindire README/locales și pașii exacți pentru adăugarea unui șablon, a unui exemplu sau a unui link către un instrument nou.

Pentru a folosi o abilitate, copiază-i folderul în `.claude/skills/` din rădăcina depozitului în care lucrezi (sau în `~/.claude/skills/` pentru a o face disponibilă în fiecare proiect), apoi cere-i lui Claude Code să scrie sau să analizeze un ADR.

## Convenții de denumire a fișierelor ADR

Dacă alegi să creezi ADR-urile în fișiere text obișnuite, poate vrei să stabilești propria convenție de denumire a fișierelor ADR.

Noi preferăm o convenție de denumire cu un format anume.

Exemple:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Convenția noastră de denumire a fișierelor:

  * Numele conține o expresie verbală la imperativ (în engleză, timpul prezent). Aceasta îmbunătățește lizibilitatea și se potrivește cu formatul mesajelor noastre de commit.

  * Numele folosește litere mici și cratime (la fel ca acest depozit). Este un echilibru între lizibilitate și ușurința de utilizare în sistem.

  * Extensia este markdown. Aceasta poate fi utilă pentru formatare ușoară.

## Sugestii pentru scrierea unor ADR bune

Caracteristicile unui ADR bun:

* Justificare: Explică motivele pentru care se ia decizia de arhitectură respectivă. Aceasta poate include contextul (vezi mai jos), avantajele și dezavantajele diferitelor alegeri posibile, comparații de funcționalități, discuții cost/beneficiu și altele.

* Specific: Fiecare ADR ar trebui să se refere la o singură decizie de arhitectură, nu la mai multe.

* Marcaje de timp: Indică momentul în care a fost scris fiecare element din ADR. Acest lucru este deosebit de important pentru aspectele care se pot schimba în timp, cum ar fi costurile, calendarele, scalarea și altele asemenea.

* Imuabil: Nu modifica informațiile existente dintr-un ADR. În schimb, completează ADR-ul adăugând informații noi sau înlocuiește-l creând un ADR nou.

Caracteristicile unei secțiuni „Context” bune într-un ADR:

* Explică situația organizației tale și prioritățile de business.

* Include justificări și considerații bazate pe componența socială și competențele echipelor tale.

* Include avantajele și dezavantajele relevante și descrie-le în termeni care se aliniază nevoilor și obiectivelor tale.

Caracteristicile unei secțiuni „Consecințe” bune într-un ADR:

* Explică ce rezultă din luarea deciziei. Aceasta poate include efecte, rezultate, produse, acțiuni ulterioare și altele.

* Include informații despre orice ADR-uri ulterioare. Este relativ obișnuit ca un ADR să genereze nevoia de alte ADR-uri, de exemplu atunci când un ADR face o alegere mare, generală, care la rândul ei creează nevoia unor decizii mai mici.

* Include orice procese de analiză ulterioară. Este tipic ca echipele să analizeze fiecare ADR după o lună, pentru a compara informațiile din ADR cu ceea ce s-a întâmplat în practică, pentru a învăța și a evolua.

Un ADR nou poate lua locul unui ADR anterior:

* Când se ia o decizie de arhitectură care înlocuiește sau invalidează un ADR anterior, trebuie creat un ADR nou

## Șabloane exemplu de ADR

Șabloane exemplu de ADR pe care le-am adunat de pe net:

- [Șablon ADR de Michael Nygard](sabloane/sablon-de-inregistrare-a-deciziilor-michael-nygard/) (simplu și popular)

- [Șablon ADR de Jeff Tyree și Art Akerman](sabloane/sablon-de-inregistrare-a-deciziilor-jeff-tyree-si-art-akerman/) (mai sofisticat)

- [Șablon ADR pentru tiparul alexandrin](sabloane/sablon-de-inregistrare-a-deciziilor-tipar-alexandrin/) (simplu, cu specificități de context)

- [Șablon ADR pentru studiul de caz de afaceri](sabloane/sablon-de-inregistrare-a-deciziilor-studiu-de-caz-de-afaceri/) (mai orientat spre MBA, cu costuri, SWOT și mai multe opinii)

- [Șablon ADR al proiectului Markdown Any Decision Records (MADR)](sabloane/sablon-de-inregistrare-a-deciziilor-proiectul-madr/) (versiune simplă și elaborată; cea din urmă pune accent pe opțiuni și avantajele și dezavantajele lor)

- [Șablon ADR cu Planguage](sabloane/sablon-de-inregistrare-a-deciziilor-cu-planguage/) (mai orientat spre asigurarea calității)

- [Șablon pentru Deciziile Tehnice Importante (ITD) de Ignacio Larrañaga](sabloane/sablon-de-inregistrare-a-deciziilor-tehnice-importante/) (suplu, cu decizia pe primul loc, optimizat pentru analiză rapidă de către conducere)

## Sfaturi de lucru în echipă pentru ADR

Dacă te gândești să folosești înregistrări de decizii în echipa ta, iată câteva sfaturi pe care le-am învățat lucrând cu multe echipe.

Ai ocazia să-ți conduci colegii discutând împreună despre „de ce”, în loc să impui „ce”. De exemplu, înregistrările de decizii sunt o modalitate prin care echipele pot gândi mai inteligent și comunica mai bine; ele nu au valoare dacă sunt doar o cerință birocratică impusă după fapt.

Unele echipe preferă mult denumirea „decizii” în locul abrevierii „ADR”. Când unele echipe folosesc numele de director „decisions”, e ca și cum s-ar aprinde un bec, iar echipa începe să pună mai multe informații în director, cum ar fi deciziile privind furnizorii, planificarea, calendarele etc. Toate aceste tipuri de informații pot folosi același șablon. Presupunem că oamenii învață mai repede cu cuvinte („decizii”) decât cu abrevieri („ADR”), că sunt mai motivați să scrie documente în lucru când este eliminat cuvântul „înregistrare” și că unor dezvoltatori și manageri nu le place cuvântul „arhitectură”.

În teorie, imuabilitatea este ideală. În practică, mutabilitatea a funcționat mai bine pentru echipele noastre. Inserăm informația nouă în ADR-ul existent, cu o dată și o notă că informația a apărut după decizie. Această abordare duce la un „document viu” pe care îl putem actualiza cu toții. Actualizările tipice apar când obținem informații datorită unor colegi noi, unor oferte noi, rezultatelor reale ale utilizării noastre sau unor schimbări ulterioare din partea terților, cum ar fi capabilitățile furnizorilor, planurile de preț, acordurile de licență etc.

## Întrebări despre munca în echipă pentru ADR

### Cine poate crea un ADR?

Ia în considerare aspecte precum anumite persoane, anumite roluri, anumite echipe sau anumite departamente; ia în considerare și dacă există persoane, roluri, echipe sau departamente care pot comanda un ADR, adică pot cere unul pe care îl va scrie altcineva. 

Exemplu de răspuns: Orice persoană din organizația noastră care a citit pagina README despre înregistrarea deciziilor de arhitectură poate propune un ADR, adică poate începe să îl scrie și să îl partajeze cu echipa.

### Ce justifică inițierea unui ADR?

Ia în considerare aspecte precum modul de lucru al echipelor organizației tale, structura sistemului tău software, coordonarea între echipe, mentenabilitatea pe termen lung, interfețele externe, cui vrei să îi aducă beneficii și altele asemenea. 

Exemplu de răspuns: Vrem să creăm un ADR când dorim ca dezvoltatorii viitori să înțeleagă „de ce” facem ceea ce facem.

### Ce justifică neinițierea unui ADR?

Ia în considerare aspecte precum deciziile care nu țin de arhitectură sau sunt minuscule (de exemplu cu risc minim, autonome sau luate de un singur dezvoltator) ori sunt deja acoperite integral în altă parte (de exemplu prin standarde, politici sau documentație) ori sunt temporare (de exemplu soluții de ocolire, demonstrații de concept sau experimente). 

Exemplu de răspuns: Renunțăm la un ADR când o decizie este limitată ca domeniu, timp, risc și cost sau este deja acoperită în altă parte.

### Care este ciclul de viață al unui ADR?

Ia în considerare aspecte precum procesul de creare, procesul de cercetare, procesul decizional, procesul de implementare și procesul de retragere. Gândește-te cum urmărești ciclul de viață al ADR-ului în timp, de exemplu cum muți ADR-ul dintr-o stare în următoarea și cum comunici acest lucru părților interesate. 

Exemplu de răspuns: Vrem ca un ADR să aibă cinci etape ale ciclului de viață: Inițiere → Cercetare → Evaluare → Implementare → Întreținere → Retragere.

### Care sunt criteriile pentru etapele ciclului de viață ale unui ADR?

Ia în considerare aspecte precum criteriile de acceptare a unui ADR, adică cum știi că este suficient de bun pentru a trece de la o etapă a ciclului de viață la următoarea? Este problema formulată clar? Au fost luate în considerare alternativele? Sunt compromisurile suficient de bine înțelese și documentate?
Este prezent tot contextul relevant? Sunt implicate toate părțile interesate relevante? Au fost încorporate toate observațiile? 

Exemplu de răspuns: Vrem ca un ADR să fie votat de părțile interesate când echipa activă 1) și-a încheiat cercetarea, 2) și-a încheiat evaluarea, 3) a publicat propunerea de ADR către părțile interesate cu o cerere de comentarii și un termen de o săptămână, 4) toate comentariile părților interesate au fost încorporate și tratate.

### Ce roluri și responsabilități interacționează cu un ADR?

Ia în considerare roluri precum inițiator, cercetător, evaluator, recenzent, aprobator, responsabil de întreținere și altele asemenea. Ia în considerare responsabilități precum comunicarea cu părțile interesate, asigurarea îndeplinirii așteptărilor, partajarea pe site-ul web sau în intranet și revizuirea periodică a muncii, mai ales când apar schimbări relevante.

Exemplu de răspuns: Vrem ca fiecare ADR să aibă întotdeauna o persoană de contact principală, o persoană de contact secundară și o echipă responsabilă; acestea sunt responsabile de comunicări, publicații, întreținere, revizuire periodică cel puțin o dată pe an și eventuala retragere, după caz.

### Cum interacționează guvernanța cu un ADR?

Ia în considerare aspecte precum modul de lucru al organizației tale, eventuale nevoi speciale de conformitate, de exemplu aspecte juridice sau de resurse umane, și cum vrei să gestionezi consensul față de conflict și față de escaladare. Există domenii, persoane sau echipe care pot avea mai multă influență decât altele asupra unui ADR, de exemplu pot să îl aprobe, să voteze asupra lui sau să îl respingă prin veto?

Exemplu de răspuns: Guvernanța unui ADR se face în această ordine de prioritate: directorul general (CEO), directorul tehnic (CTO), directorul juridic (CLO), echipa care implementează un ADR, experții din echipă cei mai bine informați despre decizia de arhitectură. Nimeni altcineva nu are guvernanță, cu excepția cazului în care este descris în ADR. 

### Ce principii interacționează cu un ADR?

Ia în considerare aspecte precum modul de lucru al organizației tale, care include mișcarea rapidă față de mișcarea lentă, consensul decizional față de conflictul decizional, preferințele de risc față de preferințele de siguranță, discuția publică față de discuția privată și altele asemenea.

Exemplu de răspuns: Folosim principiile de conducere: înclinație spre acțiune, dezacord și angajament (disagree-and-commit), estimările de 70% sunt suficient de bune pentru decizii ușor reversibile și ușor de izolat și moduri de lucru publice, cu excepția informațiilor confidențiale, așa cum sunt descrise în acordul de confidențialitate al organizației noastre.

## Concepte pentru pasul următor pentru ADR

[Arc42](https://arc42.org/) răspunde pragmatic la două întrebări și poate fi adaptat nevoilor tale specifice. Ce ar trebui să documentezi/comunici despre arhitectura ta? Cum ar trebui să documentezi/comunici? Arc42 include înregistrări ale deciziilor de arhitectură, plus îndrumări despre obiective, constrângeri, contexte, calitate, riscuri și altele.

[Modelul C4](https://c4model.com/) este o abordare ușor de învățat, prietenoasă cu dezvoltatorii, a diagramării arhitecturii software. C4 este un set de diagrame ierarhice pentru context, containere, componente, cod, plus diagrame de sprijin pentru peisajul sistemelor, dinamică și implementare.

## Diagrame, vederi și puncte de vedere de arhitectură

O diagramă de arhitectură se numește „vedere de arhitectură”.

O „vedere de arhitectură” este o instanță a unui „punct de vedere de arhitectură”.

Un „punct de vedere de arhitectură” are un public specific, cu preocupări specifice în minte.

Exemple de puncte de vedere de arhitectură, exemple de vederi și exemple de diagrame:

- Capabilități de business

- Procese de business la nivel înalt

- [Fluxuri de valoare](https://en.wikipedia.org/wiki/Value_stream)

- Funcții software mapate pe componente ale aplicației

- Diagrama de context [C4 Model](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- Diagrama de containere [C4 Model](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- [Diagrama entitate-relație](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) pentru a mapa entitățile de date pe componentele aplicației

- [Diagrame de secvență](https://en.wikipedia.org/wiki/Sequence_diagram) pentru a descrie fluxurile funcționale din interiorul sistemelor și pentru integrări

- Diagrame [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) pentru a descrie fluxurile de date între componentele aplicației

- Diagrame [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) pentru a descrie procesele de business / scenariile utilizatorilor

- Diagrame [Identity and Access Management](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM)

- Diagrame [Role-Based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) cu roluri pentru fiecare componentă a aplicației

- Diagrame [Attribute-Based Access Control](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) cu atribute pentru fiecare componentă a aplicației

- Diagrame de confidențialitate

Diagrame conexe:

- O diagramă de cazuri de utilizare arată cazurile de utilizare conducerii/clienților, ceea ce precede cerințele, care preced arhitectura software.

- O diagramă de implementare arată hardware-ul fizic/calculatoarele pe care sunt implementate componentele software.
- O diagramă de flux de date arată cum se mișcă datele prin sistem și cum sunt transformate.
- O diagramă de secvență este folosită pentru a arăta cum funcționează protocoalele precum HTTP pe o axă a timpului.

- O diagramă de activitate descrie fluxul de lucru al activităților pe care le întreprinde un sistem software, cum ar fi o IA de tip NPC.

## Funcții de adecvare pentru decizii ca cod

Funcțiile de adecvare (engl. fitness functions) sunt verificări automate obiective, scrise în cod de programare, care confirmă că deciziile sunt respectate.

- Funcțiile de adecvare fac deciziile testabile și asigurabile.

- Funcțiile de adecvare pentru decizii pot ajuta foarte mult la asigurarea calității, la procesele de reglementare și la obiectivele de guvernanță.

### Cum se leagă funcțiile de adecvare de decizii

O înregistrare a deciziei documentează decizia, în timp ce o funcție de adecvare o asigură.

- Exemplu de decizie: Folosim event sourcing pentru cerințele de audit.

- Exemplu de funcție de adecvare: Folosim serverul de integrare continuă pentru a testa că orice schimbare de stare trebuie să producă evenimente.

### De ce ajută funcțiile de adecvare deciziile

Măsurători obiective: Funcțiile de adecvare trec sau eșuează, deci munca este vizibilă și clară.

Utilizare continuă: Funcțiile de adecvare sunt regulile tale vii, rulate la fiecare commit și build.

Încredere în refactorizare: Funcțiile de adecvare prind automat erorile din regulile deciziilor.

Guvernanță scalabilă: Funcțiile de adecvare asigură standardele fără a crea blocaje.

### Pot funcțiile de adecvare să folosească AI?

Funcțiile de adecvare pot folosi modele lingvistice mari (LLM) AI pentru decizii, adresând întrebări despre munca ta,
cum ar fi planurile, codul, schemele, API-urile și altele:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Testarea unitară a arhitecturii

[ArchUnit](https://www.archunit.org/): verifică regulile de arhitectură ale codului Java folosind orice framework simplu de teste unitare Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): verifică regulile de arhitectură ale codului TypeScript și JavaScript folosind Jest, Vitest, Jasmine etc.

## Bariere de decizie pentru pull request-uri

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
scoate automat la suprafață înregistrările de decizii potrivite la momentul
potrivit — atunci când un dezvoltator modifică activ codul pe care aceste
decizii îl acoperă. În loc să sperăm că dezvoltatorii citesc un folder de
documentație înainte de integrare, contextul relevant apare direct în pull
request.

Funcționează pentru orice fel de înregistrare de decizii: decizii de arhitectură,
decizii privind datele, decizii de conformitate, decizii clinice și medicale,
decizii de securitate și altele.

Funcționează cu orice sistem CI (GitLab, Jenkins, CircleCI) și ca hook
pre-commit. Open source. Licență MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) este un GitHub
Action care face să eșueze un pull request atunci când căile de cod urmărite se
schimbă fără ca o înregistrare a deciziilor de arhitectură să fie adăugată sau
actualizată. Derogările sunt explicite: o linie `ADR-Exempt:` cu un motiv
trece bariera și este scrisă în rezumatul jobului. Independent de șablon, fără
dependențe. Open source. Licență MIT.

## Mai multe informații

Introducere:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Șabloane:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Aprofundare:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - lecție lunară gratuită de arhitectură software

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Instrumente:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Îndrumări specifice companiilor:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Exemple:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Videoclipuri:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcasturi:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Cărți:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

Vezi și:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Un format YAML/JSON neutru față de furnizor, lizibil de mașină, pentru reprezentarea deciziilor cu raționament explicit, ipoteze, stare cognitivă și compromisuri. Completează ADR-urile adăugând raționament structurat și validabil în documentația deciziilor.
