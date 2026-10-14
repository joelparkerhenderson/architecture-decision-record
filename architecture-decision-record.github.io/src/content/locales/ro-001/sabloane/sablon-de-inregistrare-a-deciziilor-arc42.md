# Șablon de înregistrare a deciziilor de la arc42

<https://arc42.org/overview>

## 1. Introducere și obiective

Scurtă descriere a cerințelor, a forțelor motrice, extras (sau rezumat) al
cerințelor. Primele trei (maximum cinci) obiective de calitate ale arhitecturii,
care au cea mai mare prioritate pentru părțile interesate principale. Un tabel cu
părțile interesate importante și așteptările lor privind arhitectura.

## 1.1 Prezentare generală a cerințelor

### Conținut

Scurtă descriere a cerințelor funcționale, a forțelor motrice, extras (sau
rezumat) al cerințelor. Linkuri către documentele de cerințe (sperăm că
existente), cu informații despre unde pot fi găsite. 

### Motivație

Din punctul de vedere al utilizatorilor finali, un sistem este creat sau
modificat pentru a sprijini mai bine o activitate de business și/sau pentru a
îmbunătăți calitatea. 

### Formă

Scurtă descriere textuală, probabil în format tabelar de cazuri de utilizare.
Dacă există documente de cerințe, această prezentare ar trebui să facă trimitere
la ele.

Păstrează aceste extrase cât mai scurte posibil. Echilibrează lizibilitatea
acestui document cu redundanța potențială față de documentele de cerințe. 

## 1.2 Obiective de calitate

### Conținut

Primele trei (maximum cinci) obiective de calitate ale arhitecturii a căror
îndeplinire este cea mai importantă pentru părțile interesate principale. Ne
referim într-adevăr la obiectivele de calitate ale arhitecturii. Nu le confunda
cu obiectivele proiectului. Ele nu sunt neapărat identice. Standardul ISO 25010
oferă o prezentare bună a subiectelor potențial de interes.

### Motivație

Ar trebui să cunoști obiectivele de calitate ale celor mai importante părți
interesate ale tale, deoarece acestea vor influența deciziile arhitecturale
fundamentale. Fii foarte concret în privința acestor calități, evită cuvintele la
modă. Dacă tu, ca arhitect, nu știi cum va fi judecată calitatea muncii tale …

### Formă

Un tabel cu cele mai importante obiective de calitate și scenarii concrete,
ordonate după priorități.

## 1.3 Părți interesate

### Conținut

Prezentare explicită a părților interesate ale sistemului, adică toate
persoanele, rolurile sau organizațiile care

- ar trebui să cunoască arhitectura

- trebuie convinse de arhitectură

- trebuie să lucreze cu arhitectura sau cu codul

- au nevoie de documentația arhitecturii pentru munca lor

- trebuie să ia decizii despre sistem sau despre dezvoltarea lui

### Motivație

Ar trebui să cunoști toate părțile implicate în dezvoltarea sistemului sau
afectate de sistem. Altfel, poți avea surprize neplăcute mai târziu în procesul
de dezvoltare. Aceste părți interesate determină amploarea și nivelul de detaliu
al muncii tale și al rezultatelor ei.

### Formă

Tabel cu numele rolurilor, numele persoanelor și așteptările lor în ceea ce
privește arhitectura și documentația ei.

## 2. Constrângeri

Orice constrânge echipele în deciziile de proiectare și implementare sau în
deciziile despre procesele conexe. Uneori pot depăși sistemele individuale și
sunt valabile pentru organizații și companii întregi.

### Conținut

Orice cerință care constrânge arhitecții software în libertatea lor de proiectare
și în deciziile de implementare sau în decizia privind procesul de dezvoltare.
Aceste constrângeri depășesc uneori sistemele individuale și sunt valabile pentru
organizații și companii întregi.

### Motivație

Arhitecții ar trebui să știe exact unde sunt liberi în deciziile lor de
proiectare și unde trebuie să respecte constrângerile. Constrângerile trebuie
întotdeauna tratate; totuși, pot fi negociabile.

### Formă

Tabele simple de constrângeri, cu explicații. Dacă este necesar, le poți
subdivide în constrângeri tehnice, constrângeri organizaționale și politice și
convenții (de exemplu ghiduri de programare sau de versionare, convenții de
documentare sau de denumire)

## 3. Context și domeniu de aplicare

Delimitează sistemul tău de partenerii săi (externi) de comunicare (sisteme
vecine și utilizatori). Specifică interfețele externe. Prezentat dintr-o
perspectivă de business/domeniu (întotdeauna) sau dintr-o perspectivă tehnică
(opțional)

### Conținut

Domeniul și contextul sistemului — după cum sugerează și numele — delimitează
sistemul tău (adică domeniul tău de aplicare) de toți partenerii săi de
comunicare (sisteme vecine și utilizatori, adică contextul sistemului tău). Astfel,
specifică interfețele externe.

Dacă este necesar, diferențiază contextul de business (intrări și ieșiri
specifice domeniului) de contextul tehnic (canale, protocoale, hardware).

### Motivație

Interfețele de domeniu și interfețele tehnice către partenerii de comunicare
sunt printre cele mai critice aspecte ale sistemului tău. Asigură-te că le
înțelegi complet.

### Formă

- Diverse diagrame de context

- Liste de parteneri de comunicare și interfețele lor.

## 3.1 Contextul de business

### Conținut

Specificarea tuturor partenerilor de comunicare (utilizatori, sisteme IT, …) cu
explicații ale intrărilor și ieșirilor sau ale interfețelor specifice
domeniului. Opțional, poți adăuga formate specifice domeniului sau protocoale de
comunicare.

### Motivație

Toate părțile interesate ar trebui să înțeleagă ce date sunt schimbate cu mediul
sistemului.

### Formă

Orice fel de diagrame care arată sistemul ca pe o cutie neagră și specifică
interfețele de domeniu către partenerii de comunicare.

Alternativ (sau suplimentar) poți folosi un tabel. Titlul tabelului este numele
sistemului tău, iar cele trei coloane conțin numele partenerului de comunicare,
intrările și ieșirile.

## 3.2 Contextul tehnic

### Conținut

Interfețele tehnice (canale și medii de transmisie) care leagă sistemul tău de
mediul său. În plus, o mapare a intrărilor/ieșirilor specifice domeniului pe
canale, adică o explicație a canalului pe care îl folosește fiecare intrare/ieșire.

### Motivație

Multe părți interesate iau decizii arhitecturale pe baza interfețelor tehnice
dintre sistem și contextul său. În special proiectanții de infrastructură sau de
hardware decid aceste interfețe tehnice.

### Formă

De exemplu, o diagramă de implementare UML care descrie canalele către sistemele
vecine, împreună cu un tabel de mapare care arată relațiile dintre canale și
intrări/ieșiri.

## 4. Strategia soluției

Rezumat al deciziilor fundamentale și al strategiilor de soluție care modelează
arhitectura. Poate include tehnologie, descompunerea la nivel înalt, abordări
pentru atingerea obiectivelor de calitate de top și decizii organizaționale
relevante.

### Conținut

Un scurt rezumat și o explicație a deciziilor fundamentale și a strategiilor de
soluție care modelează arhitectura sistemului. Acestea includ

- decizii tehnologice

- decizii privind descompunerea sistemului la nivel înalt, de exemplu utilizarea unui tipar arhitectural sau a unui tipar de proiectare

- decizii privind modul de atingere a obiectivelor cheie de calitate

- decizii organizaționale relevante, de exemplu alegerea unui proces de dezvoltare sau delegarea anumitor sarcini către terți.

### Motivație

Aceste decizii formează pietrele de temelie ale arhitecturii tale. Ele stau la
baza multor alte decizii de detaliu sau reguli de implementare.

### Formă

Păstrează explicația acestor decizii cheie scurtă.

Motivează ce ai decis și de ce ai decis astfel, pe baza enunțului problemei,
a obiectivelor de calitate și a constrângerilor cheie. Fă trimitere la detalii
în secțiunile următoare (secțiunea 5 pentru detalii structurale, secțiunea 8
pentru concepte transversale).

Poți folosi o listă de abordări ale soluției sau un tabel.

## 5. Vederea blocurilor de construcție

Descompunerea statică a sistemului, abstracții ale codului sursă, prezentate ca
ierarhie de cutii albe (care conțin cutii negre), până la nivelul de detaliu
adecvat.

### Conținut

Vederea blocurilor de construcție arată descompunerea statică a sistemului în
blocuri de construcție (module, componente, subsisteme, clase, interfețe,
pachete, biblioteci, framework-uri, straturi, partiții, niveluri, funcții,
macrocomenzi, operații, structuri de date, …) precum și dependențele lor
(relații, asocieri, …)

Această vedere este obligatorie pentru orice documentație de arhitectură. Prin
analogie cu o casă, este planul etajului.

### Motivație

Păstrează o privire de ansamblu asupra codului tău sursă făcând structura lui
ușor de înțeles prin abstractizare.

Aceasta îți permite să comunici cu părțile interesate la un nivel abstract, fără
a dezvălui detalii de implementare.

### Formă

Vederea blocurilor de construcție este o colecție ierarhică de cutii negre și
cutii albe (vezi figura de mai jos) și descrierile lor.

## 5.1 Cutie albă — sistemul în ansamblu

Aici descrii descompunerea sistemului în ansamblu folosind următorul șablon de
cutie albă. Acesta conține

- o diagramă de ansamblu

- o motivație pentru descompunere

- descrieri de cutie neagră ale blocurilor de construcție conținute. Pentru
  acestea îți oferim alternative:

  - folosește un tabel pentru o prezentare scurtă și pragmatică a tuturor blocurilor de construcție conținute și a interfețelor lor

  - folosește o listă de descrieri de cutie neagră ale blocurilor de construcție, conform șablonului de cutie neagră (vezi mai jos). În funcție de instrumentul ales, această listă poate fi alcătuită din subcapitole (în fișiere text), subpagini (într-un Wiki) sau elemente imbricate (într-un instrument de modelare).

  - (opțional:) interfețe importante, care nu sunt explicate în șabloanele de cutie neagră ale unui bloc de construcție, dar sunt foarte importante pentru înțelegerea cutiei albe.

Deoarece există atât de multe moduri de a specifica interfețele, nu oferim un
șablon specific pentru ele.

În cel mai bun caz, te vei descurca cu exemple sau semnături simple.

## 5.2 Nivelul 2

Aici poți specifica structura internă a (unor) blocuri de construcție din
nivelul 1 sub formă de cutii albe.

Trebuie să decizi care blocuri de construcție ale sistemului tău sunt suficient
de importante pentru a justifica o descriere atât de detaliată. Preferă
relevanța în locul completitudinii. Specifică blocurile de construcție
importante, surprinzătoare, riscante, complexe sau volatile. Omite părțile
normale, simple, plictisitoare sau standardizate ale sistemului tău

### 5.2.1 Cutie albă pentru blocul de construcție 1

Specifică structura internă a blocului de construcție 1.

Folosește șablonul de cutie albă (vezi mai sus).

## 6. Vederea de execuție

Comportamentul blocurilor de construcție sub formă de scenarii, acoperind cazuri
de utilizare sau funcționalități importante, interacțiuni la interfețele externe
critice, operare și administrare, plus comportamentul în caz de erori și
excepții.

### Conținut

Vederea de execuție descrie comportamentul concret și interacțiunile blocurilor
de construcție ale sistemului sub formă de scenarii din următoarele domenii:

- cazuri de utilizare sau funcționalități importante: cum le execută blocurile de construcție?

- interacțiuni la interfețele externe critice: cum cooperează blocurile de construcție cu utilizatorii și cu sistemele vecine?

- operare și administrare: lansare, pornire, oprire

- scenarii de eroare și de excepție

Observație: Principalul criteriu pentru alegerea scenariilor posibile (secvențe, fluxuri de lucru) este relevanța lor arhitecturală. Nu este important să descrii un număr mare de scenarii. Mai bine documentează o selecție reprezentativă.

### Motivație

Ar trebui să înțelegi cum își îndeplinesc (instanțele) blocurile de construcție ale sistemului tău sarcina și cum comunică în timpul execuției. În documentație vei consemna în principal scenarii pentru a comunica arhitectura ta părților interesate care sunt mai puțin dispuse sau capabile să citească și să înțeleagă modelele statice (vederea blocurilor de construcție, vederea de implementare).

### Formă

Există multe notații pentru descrierea scenariilor, de exemplu


- listă numerotată de pași (în limbaj natural)

- diagrame de activitate sau organigrame

- diagrame de secvență

- BPMN sau EPC (lanțuri de procese conduse de evenimente)

- mașini de stări

- etc.

## 6.n Scenariu de execuție n (1, 2, 3 etc.)

Inserează diagrama de execuție sau o descriere textuală a scenariului.

Inserează o descriere a aspectelor notabile ale interacțiunilor dintre instanțele blocurilor de construcție reprezentate în această diagramă.

## 7. Vederea de implementare

Infrastructura tehnică cu medii, calculatoare, procesoare, topologii.
Maparea blocurilor de construcție (software) pe elementele infrastructurii.

### Conținut

Vederea de implementare descrie:

- infrastructura tehnică folosită pentru a executa sistemul tău, cu elemente de
  infrastructură precum locații geografice, medii, calculatoare, procesoare,
  canale și topologii de rețea, precum și alte elemente de infrastructură și

- maparea blocurilor de construcție (software) pe aceste elemente de infrastructură.

Adesea sistemele sunt executate în medii diferite, de exemplu mediul de
dezvoltare, mediul de testare, mediul de producție. În astfel de cazuri ar
trebui să documentezi toate mediile relevante.

Documentează în special vederea de implementare atunci când software-ul tău este
executat ca sistem distribuit cu mai mult de un calculator, procesor, server sau
container sau atunci când îți proiectezi și construiești propriile procesoare și
cipuri hardware.

Din perspectiva software, este suficient să consemnezi acele elemente ale
infrastructurii care sunt necesare pentru a arăta implementarea blocurilor tale
de construcție. Arhitecții hardware pot merge mai departe și pot descrie
infrastructura la orice nivel de detaliu au nevoie. 

### Motivație

Software-ul nu rulează fără hardware. Această infrastructură de bază poate și va
influența sistemul tău și/sau unele concepte transversale. Prin urmare, trebuie
să cunoști infrastructura.

### Formă

Poate că diagrama de implementare de cel mai înalt nivel este deja inclusă în secțiunea 3.2 ca context tehnic, cu infrastructura ta ca O SINGURĂ cutie neagră. În această secțiune vei face zoom pe această cutie neagră folosind diagrame de implementare suplimentare.

- UML oferă diagrame de implementare pentru a exprima această vedere. Folosește-le, probabil cu diagrame imbricate, când infrastructura ta este mai complexă.

- Când părțile tale interesate (de hardware) preferă alte tipuri de diagrame în
  locul diagramei de implementare UML, lasă-le să folosească orice tip care poate
  arăta nodurile și canalele infrastructurii.

## 7.1 Infrastructura nivelul 1

Descrie (de obicei printr-o combinație de diagrame, tabele și text):

- distribuția sistemului tău în mai multe locații, medii, calculatoare, procesoare, .. precum și conexiunile fizice dintre ele

- justificarea sau motivația importantă pentru această structură de implementare

- caracteristici de calitate și/sau de performanță ale infrastructurii

- maparea artefactelor software (blocuri de construcție) pe elementele infrastructurii

Pentru mai multe medii sau implementări alternative, copiază această secțiune din arc42 pentru toate mediile relevante. **

## 7.2 Infrastructura nivelul 2

Aici poți include structura internă a (unor) elemente de infrastructură din nivelul 1 al infrastructurii.

Copiază structura din nivelul 1 pentru fiecare element selectat.

## 8. Concepte transversale

Reglementări generale, de principiu, și abordări de soluție relevante în mai
multe părți (→ transversal) ale sistemului. Conceptele sunt adesea legate de mai
multe blocuri de construcție. Includ teme diferite, precum modele de domeniu,
tipare și stiluri arhitecturale, reguli de utilizare a unei anumite tehnologii și
reguli de implementare.

### Conținut

Această secțiune descrie concepte transversale (practici, tipare, reglementări
sau idei de soluție). Astfel de concepte sunt adesea legate de mai multe blocuri
de construcție. Pot include multe teme diferite.

### Motivație

Conceptele formează baza integrității conceptuale (consecvență, omogenitate) a
arhitecturii. Prin urmare, sunt o contribuție importantă la atingerea calităților
interne ale sistemului tău.

Acesta este locul din șablon pe care l-am prevăzut pentru o specificare coerentă
a unor astfel de concepte.

Multe dintre aceste concepte se leagă de mai multe dintre blocurile tale de
construcție sau le influențează.

### Formă

Forma poate fi variată:

- documente conceptuale cu orice fel de structură

- implementări exemplu, mai ales pentru conceptele tehnice

- extrase transversale de model sau scenarii care folosesc notațiile vederilor de arhitectură

### Structura acestei secțiuni

Alege doar temele cele mai necesare pentru sistemul tău și atribuie fiecăreia un titlu de nivel 2 în această secțiune (de exemplu 8.1, 8.2 etc.).

- NU ÎNCERCA să acoperi toate temele din diagrama menționată anterior.

### Context

Unele teme din sisteme privesc adesea mai multe blocuri de construcție, elemente
hardware sau procese de dezvoltare. Poate fi mai ușor să comunici sau să
documentezi astfel de teme transversale într-un loc central, în loc să le repeți
în descrierea blocurilor de construcție, a elementelor hardware sau a proceselor
de dezvoltare vizate.

Anumite concepte pot privi toate elementele unui sistem, altele pot fi relevante
doar pentru câteva.

## 9. Decizii arhitecturale

Decizii de arhitectură importante, costisitoare, critice, la scară largă sau
riscante, inclusiv justificările lor.

### Conținut

Decizii de arhitectură importante, costisitoare, la scară largă sau riscante,
inclusiv justificările lor. Prin „decizii” înțelegem alegerea unei alternative pe
baza unor criterii date.

Folosește-ți discernământul pentru a decide dacă o decizie arhitecturală ar
trebui documentată aici, în această secțiune centrală, sau dacă este mai bine să
o documentezi local (de exemplu în șablonul de cutie albă al unui bloc de
construcție). Evită textele redundante. Fă trimitere la secțiunea 4, unde ai
consemnat deja cele mai importante decizii ale arhitecturii tale.

### Motivație

Părțile interesate ale sistemului tău ar trebui să poată înțelege și urmări
deciziile tale.

### Formă

- ADR (înregistrare a deciziilor de arhitectură) pentru fiecare decizie importantă

- listă sau tabel, ordonat după importanță și consecințe, sau

- mai detaliat, sub formă de secțiuni separate pentru fiecare decizie

### Context (despre ADR)

Bucățile mai mici de documentație sunt mai ușor de citit, de creat și de
întreținut. În cazul deciziilor de arhitectură, echipele de dezvoltare adesea:

- cunosc decizia, deoarece este vizibilă, de exemplu, în codul sursă, dar

- nu cunosc motivația din spatele acelei decizii (vezi Nygard 2011)

Prin urmare, ar trebui să documentezi câteva decizii importante împreună cu
motivația și raționamentul lor

### Propunerea noastră privind deciziile

Ține o colecție de decizii semnificative pentru arhitectură, adică acele decizii
care afectează structura, caracteristicile de calitate, dependențele importante
(în special externe) și interfețele sau tehnicile de construcție (mulțumiri lui
Michael Nygard pentru această propunere).

## 10. Cerințe de calitate

Cerințele de calitate sub formă de scenarii, cu un arbore de calitate care oferă
o privire de ansamblu la nivel înalt. Cele mai importante obiective de calitate
ar fi trebuit descrise în secțiunea 1.2. (obiective de calitate).

### Conținut

Această secțiune conține toate cerințele de calitate relevante.

Cele mai importante dintre aceste cerințe au fost deja descrise în secțiunea
1.2. (obiective de calitate), deci aici ar trebui doar menționate. În această
secțiune 10 ar trebui să consemnezi și cerințele de calitate cu importanță mai
mică, care nu vor crea riscuri mari dacă nu sunt pe deplin atinse (dar ar putea
fi de dorit).

### Motivație

Deoarece cerințele de calitate vor avea o influență mare asupra deciziilor
arhitecturale, ar trebui să știi ce calități sunt cu adevărat importante pentru
părțile tale interesate, într-un mod specific și măsurabil.

### Informații suplimentare

Vezi modelul de calitate Q42, extins, la https://quality.arc42.org.

## 10.1 Prezentare generală a cerințelor de calitate

### Conținut

O prezentare generală sau un rezumat al cerințelor de calitate.

### Motivație

Adesea întâlnim zeci (sau chiar sute) de cerințe de calitate detaliate.
În această secțiune de prezentare generală ar trebui să încerci să rezumi, de
exemplu descriind categorii sau teme (așa cum sugerează ISO 25010:2023 sau Q42

Dacă aceste descrieri-rezumat sunt deja precise, suficient de specifice și
măsurabile, poți omite secțiunea 10.2.

### Formă

Folosește un tabel simplu în care fiecare linie conține o categorie sau o temă și
o scurtă descriere a cerinței de calitate. Alternativ, poți folosi o hartă mentală
pentru a structura aceste cerințe de calitate.

În literatură a fost descrisă și ideea unui arbore al atributelor de calitate,
care pune termenul generic „calitate” ca rădăcină și folosește o rafinare în
formă de arbore a termenului „calitate”. [Bass+21] a introdus în acest scop
termenul „Quality Attribute Utility Tree”.

## 10.2 Scenarii de calitate

### Conținut

Scenariile de calitate concretizează cerințele de calitate și permit să se decidă
dacă sunt îndeplinite (în sensul criteriilor de acceptare). Asigură-te că
scenariile tale sunt specifice și măsurabile.

Două tipuri de scenarii sunt deosebit de utile:

- Scenariile de utilizare (numite și scenarii de aplicație sau scenarii de caz de
  utilizare) descriu reacția sistemului la execuție față de un anumit stimul.
  Aceasta include și scenariile care descriu eficiența sau performanța
  sistemului. Exemplu: Sistemul reacționează la cererea unui utilizator în
  decurs de o secundă.

- Scenariile de modificare descriu efectul dorit al unei modificări sau extinderi
  a sistemului sau a mediului său imediat. Exemplu: Se implementează funcționalități
  suplimentare sau se schimbă cerințele pentru un atribut de calitate, iar efortul
  sau durata modificării este măsurată.

### Formă

Informațiile tipice pentru scenariile detaliate includ următoarele:

În formă scurtă (preferată în modelul Q42):

- Context/Fundal: Ce fel de sistem sau componentă, care este mediul sau situația?

- Sursă/Stimul: Cine sau ce inițiază sau declanșează un comportament, o reacție sau o acțiune.

- Măsură/Criterii de acceptare: Un răspuns care include o măsură sau o metrică

Forma lungă a scenariilor (preferată de SEI și [Bass+21]) este mai detaliată și include următoarele informații:

- ID-ul scenariului: Un identificator unic al scenariului.

- Numele scenariului: Un nume scurt, descriptiv, al scenariului.

- Sursa: Entitatea (utilizator, sistem sau eveniment) care inițiază scenariul.

- Stimulul: Evenimentul sau condiția declanșatoare pe care sistemul trebuie să o abordeze.

- Mediul: Contextul operațional sau condiția în care sistemul întâmpină stimulul.

- Artefactul: Blocurile de construcție sau alte elemente ale sistemului afectate de stimul.

- Răspunsul: Rezultatul sau comportamentul pe care sistemul îl manifestă ca reacție la stimul.

- Măsura răspunsului: Criteriile sau metrica după care este evaluat răspunsul sistemului.

### Vezi și

Din ianuarie 2023, arc42 oferă un model de calitate pragmatic, care propune
etichetarea cerințelor de calitate cu hashtag-uri sau etichete precum #flexible,
#efficient, #usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Riscuri și datorie tehnică

Riscuri tehnice sau datorie tehnică cunoscute. Ce probleme potențiale există în
sistem sau în jurul lui? Ce îi face pe membrii echipei de dezvoltare să se simtă
rău?

### Conținut

O listă de riscuri tehnice sau datorii tehnice identificate, ordonată după
prioritate

### Motivație

„Managementul riscurilor este managementul de proiect pentru adulți” (Tim Lister,
Atlantic Systems Guild.)

Acesta ar trebui să fie motto-ul tău pentru detectarea și evaluarea sistematică
a riscurilor și a datoriilor tehnice din arhitectură, de care vor avea nevoie
părțile interesate din management (de exemplu manageri de proiect, proprietari de
produs) ca parte a analizei generale de risc și a planificării măsurilor.

### Formă

Listă de riscuri și/sau datorii tehnice, probabil incluzând măsuri sugerate
pentru a minimiza, atenua sau evita riscurile ori a reduce datoriile tehnice.
