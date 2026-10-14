# Înregistrare a deciziei de arhitectură: limbajul de programare Rust

Numărul deciziei: AR-001

Titlul deciziei: Adoptarea limbajului de programare Rust

Data: 1 decembrie 2021

Stare: Acceptată

### Enunțul problemei

Pe măsură ce continuăm să dezvoltăm aplicații software, am observat că este din ce în ce mai dificil să atenuăm potențialele vulnerabilități de securitate și să prevenim erorile la execuție. Cu limbajele de programare existente, precum C și C++, continuăm să întâmpinăm probleme precum depășirile de buffer, scurgerile de memorie și comportamentul nedefinit care duce la blocarea aplicațiilor. Avem nevoie de un limbaj de programare care oferă garanții de siguranță a memoriei și este suficient de eficient pentru a suporta aplicații critice din punct de vedere al performanței.

### Considerații

Mai multe limbaje de programare sunt concepute pentru a aborda problemele existente. Printre ele, limbajul de programare Rust a atras o atenție semnificativă din partea comunității de dezvoltatori datorită caracteristicilor sale unice de proiectare. Considerațiile includ;

1. Siguranța memoriei și securitatea

2. Performanța și eficiența

3. Suportul comunității și adoptarea

4. Curba de învățare

5. Instrumentele și ecosistemul

6. Compatibilitatea cu sistemele software existente.

### Constrângeri

Adoptarea unui limbaj de programare nou necesită reinstruirea dezvoltatorilor, ceea ce consumă timp și resurse. Integrarea limbajului în fluxul de dezvoltare existent poate fi o provocare. Trebuie să asigurăm compatibilitatea cu sistemele existente și să evităm modificările cu impact negativ pentru a menține continuitatea.

### Implementare

1. Echipa noastră de dezvoltare va urma instruire pentru a învăța și a se familiariza cu limbajul de programare Rust.

2. Vom crea un proiect nou în Rust, pe bază de probă, pentru a evalua compatibilitatea și adecvarea lui pentru scopurile noastre de dezvoltare.

3. Vom migra treptat sistemele existente scrise în C și C++ la Rust.

4. Vom colabora cu comunitatea Rust pentru a explora instrumentele și bibliotecile disponibile care pot îmbunătăți fluxul nostru de dezvoltare.

5. Vom monitoriza regulat performanța Rust și o vom compara cu performanța limbajelor de programare existente.

6. Vom adopta o abordare pe termen lung care echilibrează costurile instruirii, integrării și beneficiile potențiale ale utilizării Rust.

### Justificare

Am adoptat Rust datorită caracteristicilor sale unice, concepute pentru a oferi garanții de siguranță a memoriei și de securitate, menținând în același timp performanța și eficiența. Sistemul robust de tipuri al Rust, borrow checker-ul și conceptele de siguranță a memoriei îl fac foarte potrivit pentru dezvoltarea de aplicații critice din punct de vedere al performanței și al siguranței. Mai mult, Rust are o comunitate semnificativă de dezvoltatori, ceea ce ne permite accesul la o gamă largă de instrumente, biblioteci și ecosistem care susțin fluxul nostru de dezvoltare. Deși Rust are o curbă de învățare, credem că beneficiile adoptării Rust depășesc costurile și oferă o oportunitate excelentă pentru creștere și inovare continue.

### Consecințe

1. Adoptarea Rust va necesita o investiție semnificativă de timp și resurse pentru instruirea dezvoltatorilor și integrarea limbajului în fluxul de dezvoltare existent.

2. Adoptarea Rust poate provoca un anumit grad de probleme de compatibilitate cu sistemele existente, necesitând refactorizare și modificări.

3. Adoptarea Rust poate crește numărul de dezvoltatori care pot contribui la proiectul nostru, atrăgând dezvoltatori Rust care vor să lucreze la proiecte interesante.

4. Adoptarea ar putea duce la performanță, eficiență și siguranță îmbunătățite în comparație cu limbajele existente.

5. În sfârșit, adoptarea Rust vine cu beneficiul potențial al reducerii vulnerabilităților de securitate din aplicațiile noastre.
   
<h6>Credit: această pagină a fost generată de ChatGPT, apoi editată pentru claritate și format.</h6>