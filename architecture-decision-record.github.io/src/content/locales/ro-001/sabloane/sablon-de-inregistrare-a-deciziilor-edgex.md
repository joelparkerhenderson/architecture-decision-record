# Șablon de înregistrare a deciziilor de arhitectură (ADR) <!-- Replace with ADR title -->

Acesta este un șablon pentru ADR-urile EdgeX Foundry.

Sursă: https://docs.edgexfoundry.org/2.3/design/adr/template/


### Inițiatori

Enumeră inițiatorii ADR-ului.

Format:

- Nume (Organizație)


## Jurnal de modificări

Enumeră modificările aduse documentului, inclusiv starea, data și URL-ul PR.

Starea este una dintre: pending (în așteptare), approved (aprobat), amended (modificat), deprecated (depășit).

Data este un șir ISO 8601 (AAAA-LL-ZZ).

PR este pull request-ul care a trimis modificarea, incluzând informații precum diferențele, contribuitorii și recenzenții.

Format:

- \[Starea ADR, de exemplu approved, amended etc.\]\(URL-ul pull request-ului\) AAAA-LL-ZZ


## Cazuri de utilizare menționate

Enumeră toate documentele relevante de cazuri de utilizare / cerințe.

ADR-ul necesită cel puțin un caz de utilizare relevant și aprobat.

Format:

- \[Numele cazului de utilizare\]\(URL\)

Adaugă explicații dacă ADR-ul nu abordează toate cerințele unui caz de utilizare.


## Context

Descrie:

- în ce fel proiectarea este semnificativă din punct de vedere arhitectural, justificând un ADR (spre deosebire de o simplă problemă raportată și un PR care rezolvă o problemă)

- abordarea de proiectare la nivel înalt (detaliile sunt descrise în proiectarea propusă de mai jos)


## Proiectare propusă

Detalii ale proiectării (fără a intra în implementare, unde este posibil).

Schiță:

- servicii/module afectate (modificate)

- servicii/module noi de adăugat

- impactul asupra modelului și DTO (modificări/adăugiri/eliminări)

- impactul asupra API (modificări/adăugiri/eliminări)

- impactul asupra configurației generale (crearea de secțiuni noi, modificări/adăugiri/eliminări)

- impactul asupra devops


## Considerații

Documentează alternativele, preocupările, problemele auxiliare sau conexe și întrebările apărute în dezbaterea ADR-ului. 

Indică dacă și cum au fost rezolvate sau atenuate.


## Decizie

Documentează orice detaliu de implementare important agreat, avertismentele, considerațiile viitoare și problemele de proiectare rămase sau amânate.

Documentează orice parte a cerințelor care nu este satisfăcută de proiectarea propusă.


## Alte ADR-uri conexe

Enumeră orice ADR-uri relevante — de exemplu o decizie de proiectare pentru o subcomponentă a unei funcționalități, o proiectare depășită ca urmare a acestei proiectări etc. 

Format:

- \[Titlul ADR\]\(URL\) - Relevanță


## Referințe

Enumeră referințe suplimentare.

Format:

- \[Titlu\]\(URL\)

