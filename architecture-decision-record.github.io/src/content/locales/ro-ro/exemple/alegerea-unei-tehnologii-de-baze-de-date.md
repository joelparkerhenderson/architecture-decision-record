# Înregistrare a deciziei de arhitectură: alegerea unei tehnologii de baze de date

## Stare

Acceptată

## Context

Proiectăm o aplicație nouă care necesită stocarea și regăsirea datelor într-un mod scalabil și performant. Am identificat trei tipuri de tehnologii de baze de date folosite frecvent: baze de date relaționale, baze de date de documente și baze de date de evenimente.

Bazele de date relaționale stochează datele în tabele cu scheme fixe și impun constrângeri stricte de integritate a datelor. Sunt potrivite pentru aplicațiile care necesită relații complexe între date și tranzacții. Exemple: MySQL, PostgreSQL și Oracle.

Bazele de date de documente stochează datele în documente de tip JSON și nu au schemă. Sunt potrivite pentru aplicațiile care necesită modele de date flexibile și scalare orizontală. Exemple: MongoDB, Couchbase și Amazon DynamoDB.

Bazele de date de evenimente stochează datele sub forma unei serii de evenimente, consemnând fiecare modificare a datelor. Sunt potrivite pentru aplicațiile care necesită audit, event sourcing și procesare complexă a datelor. Exemple: Apache Kafka, Apache Pulsar și AWS Kinesis.

## Decizie

După o evaluare atentă a cerințelor și constrângerilor aplicației noastre, am decis să folosim o bază de date de documente.

## Justificare

Am ales o bază de date de documente deoarece:

1. Aplicația noastră necesită un model de date flexibil, care poate evolua în timp. Bazele de date de documente ne permit să stocăm datele într-un format fără schemă, ceea ce înseamnă că putem adăuga câmpuri noi sau schimba structura documentelor existente fără a modifica schema bazei de date.

2. Aplicația noastră trebuie să scaleze orizontal pentru a gestiona volume mari de date și trafic. Bazele de date de documente oferă suport integrat pentru sharding și replicare, ceea ce ne permite să distribuim datele pe mai multe servere și să gestionăm un debit ridicat de citiri și scrieri.

3. Aplicația noastră necesită regăsirea rapidă și eficientă a datelor. Bazele de date de documente oferă capabilități puternice de indexare și interogare, care ne permit să regăsim datele rapid și eficient.

4. Aplicația noastră nu necesită tranzacții complexe sau relații între date. Deși bazele de date relaționale excelează la impunerea constrângerilor de integritate a datelor și la gestionarea tranzacțiilor complexe, aplicația noastră nu are astfel de cerințe. Bazele de date de documente pot oferi garanții suficiente de consecvență și durabilitate pentru cazul nostru de utilizare.

## Consecințe

Alegând o bază de date de documente, va trebui să investim în învățarea și înțelegerea tehnologiei specifice pe care o vom folosi. În plus, va trebui să ne asigurăm că modelul de date al aplicației noastre se potrivește bine cu modelul de date al bazei de date de documente, pentru a maximiza performanța și scalabilitatea.

Totuși, credem că beneficiile utilizării unei baze de date de documente depășesc costurile și că este cea mai bună potrivire pentru cerințele și constrângerile aplicației noastre.
