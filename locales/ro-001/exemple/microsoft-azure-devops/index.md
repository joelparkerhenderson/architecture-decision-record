# Microsoft Azure DevOps

Cuprins:

* [Rezumat](#rezumat)
  * [Problemă](#problemă)
  * [Decizie](#decizie)
  * [Stare](#stare)
* [Detalii](#detalii)
  * [Ipoteze](#ipoteze)
  * [Constrângeri](#constrângeri)
  * [Poziții](#poziții)
  * [Argument](#argument)
  * [Implicații](#implicații)
* [Conexe](#conexe)
  * [Decizii conexe](#decizii-conexe)
  * [Cerințe conexe](#cerințe-conexe)
  * [Artefacte conexe](#artefacte-conexe)
  * [Principii conexe](#principii-conexe)
* [Note](#note)
  * [Microsoft Devops CI: An Unsatisfying Adventure](#microsoft-devops-ci-an-unsatisfying-adventure)
  * [Momente importante din discuția de pe Hacker News](#momente-importante-din-discuția-de-pe-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Rezumatul lui Edward Thomson (Azure PM)](#rezumatul-lui-edward-thomson-azure-pm)


## Rezumat


### Problemă

Vrem să folosim devops pentru a construi, integra, implementa și găzdui proiectele noastre. Luăm în considerare Microsoft Azure DevOps.

  * Vrem ca experiența dezvoltatorului să fie rapidă și fiabilă, atât pentru configurarea devops, de exemplu setarea, cât și pentru utilizarea continuă, de exemplu timpi rapizi de build.
  
  * Vrem să luăm în considerare folosirea Microsoft Azure ca ansamblu, pentru găzduirea aplicațiilor proiectelor, a bazelor de date etc.


### Decizie

S-a decis împotriva Microsoft Azure DevOps.


### Stare

Decis. Suntem deschiși să revenim dacă/atunci când apar informații noi semnificative.


## Detalii


### Ipoteze

Toate ipotezele obișnuite devops, precum cele din cartea Accelerate.

  * Buildurile rapide ajută semnificativ. Aceasta accelerează buclele de feedback.

  * Putem schimba piese cu piese de la alți furnizori, adică am putea dori să aducem propriile servere de build mai rapide sau să folosim propriul sistem de control al versiunilor sau să ne coordonăm cu un server de integrare continuă găzduit propriu.
  
  * Utilizabilitatea simplificată ajută semnificativ experiența dezvoltatorului și, la rândul ei, aspecte subtile precum consecvența, claritatea, securitatea și ușurința curbei de învățare.

  * Când ceva este defect sau problematic, vrem un mod eficient de a raporta problema. Aceasta este deosebit de importantă pentru orice probleme legate de securitate.


### Constrângeri

Niciuna cunoscută. Azure are un angajament publicat de a colabora bine cu instrumente externe.


### Poziții

Am luat în considerare Microsoft Azure Devops față de AWS, care este soluția actuală.

Am experimentat cu Azure DevOps, Azure Pipelines, Azure Repo și crearea unui server nou în Azure prin Terraform.

Am experimentat obținerea de suport de la reprezentanții Microsoft.

Am adunat informații de la colegi de breaslă de pe bloguri și de pe Hacker News.


### Argument

Azure DevOps promovează un set excelent de oferte, dar acestea nu rezistă, nu funcționează bine împreună, iar suportul este slab.

Experiența noastră directă:

  * Configurarea Azure este un talmeș-balmeș de interfețe, dintre care unele se suprapun cu conturile Microsoft, iar altele nu. De exemplu, există o autentificare Azure, o autentificare Microsoft.com, o autentificare Live.com etc. și toate sunt simultan în joc.

  * Am întâlnit o problemă minoră de securitate în timpul configurării și nu am găsit nicio rezolvare. Am încercat multe moduri de a o raporta, la mulți reprezentanți Microsoft, fără succes. Am raportat-o cu succes echipei de securitate Microsoft, care a răspuns că nu o va repara.

  * Documentația este adesea fie greșită, fie depășită. Cel puțin o parte din aceasta se datorează motorului de căutare slab al Microsoft, iar o parte se datorează unui SEO mediocru.
  
  * Configurarea Terraform este bine documentată și funcționează. Totuși, suportul Terraform este slab în comparație cu AWS, deoarece Microsoft construiește relații de afaceri cu furnizorii pentru a realiza exemple de configurare Terraform înlănțuite.

Experiențele colegilor de breaslă:

  * După ce am făcut propria evaluare pe nevăzute, am căutat experiențe ale colegilor. Ceea ce am găsit ne-a confirmat experiențele.

  * Colegii au raportat probleme suplimentare cu timpii de build și probleme cu serverul de build propriu. Aceste probleme sunt semnificativ mai grave decât problemele de interfață, deoarece realizarea de buildări este scopul de bază al unui flux de build, iar noi ne așteptăm să facem multe pe zi.

  * Am găsit o participare excelentă a colegilor de la Azure în zonele de discuții. Felicitări Microsoft pentru asta. Suntem impresionați în special de Edward Thomson, PM și programator Azure, pentru implicarea, directețea și explicațiile sale tehnice.


### Implicații

Alegerea Microsoft Azure DevOps pare probabil mai scumpă (~3x) ca timp și cost decât nealegerea Azure.


## Conexe


### Decizii conexe

Dacă alegem Azure DevOps, există multe oferte conexe, inclusiv Azure Repo, Azure Pipeline etc. Credem că, dacă alegem Azure Devops, aceasta ar putea ușura folosirea mai multor capabilități Azure sau ar putea îngreuna folosirea capabilităților altor furnizori.

Credem că Microsoft face pași mari în experiența dezvoltatorului și vedem că Microsoft face achiziții mari de instrumente pentru dezvoltatori (de exemplu GitHub) și dependențe (de exemplu Citus).

Dacă alegem Azure DevOps, am putea dori să punem accent pe alegerea ofertelor din achizițiile Microsoft și am putea dori și să abordăm ofertele achiziționate cu mai multă atenție/evaluare din cauza unui potențial respingeri a țesutului, de exemplu riscul de fluctuație a personalului.


### Cerințe conexe

Vrem timpi de build foarte rapizi. Acceptăm să plătim un preț suplimentar mare pentru aceasta. Aceasta pentru că vrem să iterăm foarte repede.

Vrem fiabilitate foarte ridicată. Acceptăm să plătim un preț suplimentar mare pentru aceasta. Aceasta pentru că testăm cazuri de utilizare de mare valoare, inclusiv tranzacții financiare, tranzacții confidențiale etc.

Primii noștri 4 KPI devops includ timpul mediu de recuperare, ceea ce necesită buildări rapide și fiabilitate ridicată.


### Artefacte conexe

Vrem ca sistemul de build să producă artefacte potrivite pentru utilizarea în alte sisteme, precum Artifactory.


### Principii conexe

Ușor reversibil. Putem evalua Azure DevOps în paralel cu AWS, soluția actuală.


## Note


### Microsoft Devops CI: An Unsatisfying Adventure

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Postare pe blog.

„Ca dezvoltator de software, știu din prima mână cât de greu este să construiești rapid și ieftin produse de calitate. Este o formă de artă pe care uneori o nimerim, iar alteori degenerează în ceva asemănător cu site-ul guvernamental de asistență medicală din epoca Obama. Nivelul nostru de control asupra produsului rezultat variază, iar vina eșecului cade adesea pe persoanele nepotrivite din ierarhia decizională. Azure DevOps de la Microsoft (cunoscut anterior ca Visual Studio Team Services), în ciuda intențiilor evident bune, este o furtună perfectă de decizii proaste și execuție slabă.”


### Momente importante din discuția de pe Hacker News

https://news.ycombinator.com/item?id=18983586

„Folosim intens Azure DevOps la locul meu de muncă și, după ce am folosit GitHub, Gitlab, soluții găzduite propriu, Jenkins, TeamCity... Azure DevOps se clasează pe ultimul loc.”

„Interfața este oribil de greoaie peste tot. Cel mai rău pentru mine sunt pull request-urile. Incredibil de greu să lucrezi cu oamenii pe un pull request. Nici măcar nu pot indica „o” problemă anume — la noi e stricat peste tot.”

„Azure Devops este ceva ce vreau să iubesc. Interfața se tot schimbă, dar nu rezolvă erorile de fond care există de ani de zile.”

„Instrumentele nu sunt bine integrate, interfața este foarte lentă, nu există o vedere de tablou de bord a pull request-urilor active, a build-urilor, a release-urilor etc. pentru depozitele mele preferate. Timpii de build/deploy sunt nebunește de lenți.”

„Am încercat să folosim și Azure Boards (Work Items, Boards, Backlogs etc.). Au. Este un talmeș-balmeș complet de interfață, făcut din idei disparate. În loc să implementeze un lucru bine, au implementat două duzini de lucruri prost.”


### Windows Development MVP

Aici, un MVP pentru dezvoltare Windows. Simt că trebuie să-mi asum o parte din responsabilitate pentru că nu am vorbit mai tare despre aceste probleme. Dar trebuie să spun că sunt dezamăgit să aud că sunteți „surprinși” de problemele de UX. Le-am spus oamenilor voștri că UX-ul este groaznic (de exemplu încă dinainte de lansare) și am tot auzit „știm, reparăm”. Voi începe să formalizez feedbackul și să-l împing prin țevi, rămâneți aproape. Sunt și local (Bellevue), mi-ar plăcea să vin și să încerc să pun în pipeline aplicația noastră oss .net/wpf/uwp relativ simplă. Bănuiesc că va fi o revelație pentru amândoi.

Câteva exemple:

* Nu poți construi un pipeline cu un depozit git care conține submodule

* Mi s-a părut imposibil să editez PATH pentru unele instrumente personalizate

* Experiența New Pipeline pur și simplu nu are prea mult sens, utilizatorii noi care dau clic prin jur vor ajunge în cele din urmă la documentația greșită.


### Rezumatul lui Edward Thomson (Azure PM)

Eu am scris codul care îmbină pull request-urile voastre. Program Manager la Microsoft pentru Azure DevOps; anterior inginer software pe instrumente de control al versiunilor la GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

Co-mentenor al libgit2. https://libgit2.github.io

Co-gazdă a All Things Git, podcastul despre Git. https://www.allthingsgit.com/

Curator al Developer Tools Weekly, un newsletter despre instrumente de dezvoltare. https://developertoolsweekly.com/
