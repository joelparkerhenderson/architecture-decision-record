# Stocarea secretelor

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Rezumat


### Problemă

Trebuie să stocăm secrete, precum parole, chei private, token-uri de autentificare etc.

Unele secrete sunt orientate spre utilizator. De exemplu, dezvoltatorul nostru vrea să poată folosi telefonul mobil pentru a căuta parola unui serviciu.

Unele secrete sunt orientate spre sistem. De exemplu, fluxul nostru de livrare continuă trebuie să poată căuta datele de autentificare pentru găzduirea noastră în cloud.


### Decizie

Bitwarden pentru secretele orientate spre utilizator

Vault by HashiCorp pentru secretele orientate spre sistem.


### Stare

Decis. Suntem deschiși la alternative noi pe măsură ce apar.


## Detalii


### Ipoteze

Pentru acest scop, și în starea noastră actuală, prețuim comoditatea orientată spre utilizator, precum aplicațiile mobile utilizabile.

  * Vrem să asigurăm acces rapid și ușor din mers, de exemplu pentru un dezvoltator care face inginerie de fiabilitate a sistemelor în regim de permanență.

  * Vrem să putem partaja unele secrete între persoane selectate, precum o echipă.

Nu încercăm să rezolvăm pentru un singur furnizor, precum stocarea tuturor secretelor exclusiv la Amazon, Azure sau Google.

Nu vrem abordări ad-hoc precum „ține-le minte” sau „scrie-le pe o hârtiuță” sau „găsește-ți propriul mod de a le stoca”.

Modelul nostru de securitate pentru acest scop este în regulă cu folosirea unor furnizori COTS bine respectați, precum instrumentele SaaS de gestionare a parolelor.


### Constrângeri

Acum vrem ceva ușor, adică fără a fi nevoie să scriem cod, fără a instala servere, fără a ne angaja major, fără a standardiza pe toată lumea.


### Poziții

Am luat în considerare:

1. Manageri de parole gata făcuți, orientați spre utilizator: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG etc.

2. Manageri de parole COTS orientați spre sistem: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Abordări orientate spre partajare: folosirea unui document Google partajat, a unui canal Slack partajat, a unui folder de rețea partajat etc.

4. Abordări ad-hoc cu tehnologie redusă, precum memorarea, scrierea unei note sau lăsarea fiecărui utilizator să-și găsească propria abordare.


### Argument

Bitwarden, LastPass, 1Password și Dashlane sunt toate produse comerciale gata făcute.

  * Tipuri similare de funcții pentru utilizatori, echipe, organizații etc.

  * Capabilitate desktop pentru Windows și Mac și capabilitate mobilă pentru Android și iOS.

  * Extensii de browser pentru Chrome și Firefox, pentru completarea automată a formularelor etc.

Bitwarden are două avantaje față de celelalte:

  * Bitwarden este open source, ceea ce înseamnă că securitatea poate fi analizată de colegi, iar compania este apreciată pe scară largă de dezvoltatorii orientați spre securitate.

  * Anecdotele lucrătorilor din software descriu o preferință semnificativă pentru Bitwarden față de celelalte.

Un exemplu tipic bun de articol: https://jcs.org/2017/11/17/bitwarden

Un site tipic de vot comparativ: https://stackshare.io/stackups/bitwarden-vs-dashlane

Amânăm KeyPass, pass, GPG etc. pentru că implică complexitate suplimentară. Toate arată ca soluții bune pentru utilizatori tehnici. GPG arată deosebit de bine pentru utilizatorii tehnici care vor capabilități între sisteme, orientate pe comenzi.

Amânăm KMS pentru că implică dependență de un singur furnizor.

Alegem Vault pentru nevoile orientate spre sistem, pentru că recenziile sunt uimitor de pozitive și pentru că HashiCorp are un istoric excelent de software și suport de cea mai înaltă calitate.

Respingem prin veto abordările de partajare, precum prin documente partajate, canale partajate, foldere de rețea partajate etc. Acestea nu oferă calitățile de securitate pe care le dorim.

Respingem prin veto abordările ad-hoc cu tehnologie redusă, pentru că toți suntem de acord că nu este o cale viabilă pe termen lung.


### Implicații

Dezvoltatorii ar putea fi nevoiți să urmărească secretele în două locuri: Bitwarden pentru accesul orientat spre utilizator și Vault pentru accesul orientat spre sistem.


## Conexe


### Decizii conexe

Decizia privind serverul CI/CD trebuie să includă dovada capacității de acces la secrete.

Va trebui să decidem cum gestionăm secretele, în termeni de politici, rotații, organizații etc.


### Cerințe conexe

Secretele vor avea cerințe conexe privind conformitatea, auditul și integrarea/ieșirea angajaților în HR.


### Artefacte conexe

Ne așteptăm să putem exporta unele secrete în variabile de mediu.


### Principii conexe

Ușor reversibil.

Ușor paralel, adică este ușor să folosești o varietate de manageri de parole.

Ieftin de încercat, adică există o perioadă de probă gratuită și niciun angajament.


## Note

Note de evaluare aici. Notele sunt toate comentarii publice de pe diverse forumuri de discuții devops.


### Vault by HashiCorp

Vault este exact ce îți trebuie aici. 

Totuși, nu pune Vault direct în producție, mai întâi pune-l în picioare într-un mediu de testare, pentru că documentația HashiCorp poate fi destul de deficitară, chiar dacă produsele lor sunt uimitoare.

Curbă de învățare foarte abruptă și nu este trivial de pus în funcțiune. 

Configurarea inițială este oarecum chinuitoare. Merită totuși din plin, iar comunitatea îl va susține suficient de bine cât să te descurci.

Documentație oribilă, dar există multe ghiduri online ale unor oameni care l-au configurat și, dacă pui câteva dintre ele cap la cap, vei avea o configurație funcțională.

Configurarea inițială a presupus să mă joc cu graficele lor helm (vault și consul). Deși tehnic poți folosi multe alte back-end-uri, chiar nu recomand. Back-end-ul/consul poate fi minuscul dacă nu ai multe date de stocat.

Cu siguranță familiarizează-te cu CLI-ul, pentru că GUI-ul este mai degrabă un proof-of-concept/portal publicitar pentru ediția lor enterprise.

Faptul că nu poți pur și simplu să-l „umpli” este o bătaie de cap. De exemplu, dacă ai 5 câmpuri, trebuie să adaugi manual fiecare câmp pentru fiecare element. Deci nu este ca și cum ai predefini câmpuri pentru o anumită categorie și le-ai completa pentru toate elementele din acea categorie, ci mai degrabă „generezi tot de fiecare dată”, ceea ce (după mine) este o corvoadă.

Poate vrei să te uiți și la goldfish ca UI peste vault. Face destul de plăcut convingerea echipei. Au și o demonstrație. 1. Configurează consul. 2. Configurează vault care indică spre consul. 3. Configurează goldfish care indică spre vault. 3. Configurează un job cron care rulează consul snapshot pentru copii de siguranță.



### LastPass

LastPass Teams. Îl folosim, are șabloane personalizate, ACL, nu lipsește nimic după mine.

Am implementat LastPass în organizația mea și îi dau C+/B-. Cea mai mare problemă în ultima vreme este lipsa fiabilității. În ultimele 90 de zile au fost mai multe ore în care seifurile au fost forțate în modul offline. Aceasta nu este ideal pentru organizația mea, deoarece avem, la propriu, peste 4.000 de parole stocate în peste 20 de foldere partajate. După cum îți poți imagina, cu atâtea parole, cel puțin câteva sunt actualizate sau adăugate zilnic. Avem un plan DR pentru cazul în care problemele durează mai mult de o oră sau două: un script semnează și criptează în fiecare noapte un export CSV al seifului, care poate fi importat în keepass.

LastPass a avut mici sincope neraportate ale serviciului degradat: autentificarea „funcționează”, dar nu aduce site-urile, funcții aleatorii din panoul de administrare sunt defecte și cheile nu sunt partajate corect pentru noile foldere partajate de nivel superior. Am un utilizator special „key push”/backup care este în fiecare grup. De obicei, autentificarea cu acel utilizator rezolvă orice probleme de partajare a cheilor, dar nu și când serviciul este degradat, indiferent ce spune pagina de stare...

Pentru integrare poate fi ușor dacă ai ACL-uri corecte, cu un model al privilegiului minim, de exemplu dacă un utilizator are citire și scriere și doar citire pe o intrare sau un folder, primește doar permisiuni de citire. Din păcate, ACL-urile organizației mele nu sunt cele mai bune, așa că am ajuns să folosesc API-ul de provizionare JSON și ~500 de linii de Python, din cauza naturii dependente a sutelor noastre de ACL-uri, care nu se mapează bine pe modelul privilegiului minim. Am ajuns să iau toate ACL-urile în care se află un utilizator și să fac un fel de parcurgere a dependențelor.

Dacă ACL-ul sau structura grupurilor tale este deja construită având în vedere privilegiul minim, instrumentul de sincronizare AD/LDAP pentru Windows va funcționa bine.

Contactează echipa lor de vânzări și îți pot face rost de o probă Enterprise mai lungă. Asigură-te că le înțelegi pe deplin limitările înainte de a te decide. Am avut destule dureri de creștere, dar, cu excepția întreruperilor sau a degradărilor din partea serverului, a mers incredibil de fluent.


### Bitwarden

Bitwarden are instrumente frumoase în jurul lui (WebUI, CLI, mobil, desktop). Găzduit propriu și destul de ușor de configurat. Documentație destul de bună și instrument recomandat de PrivacyTools.


### EnvKey

https://www.envkey.com/ Este un SaaS. Foarte ușor de implementat, integrat și gestionat.

Funcții:

  * Protejează cheile API și datele de autentificare.

  * Menține configurația sincronizată peste tot.

  * Gestionare inteligentă, criptată end-to-end, a configurației și a secretelor. 

  * Previne partajarea nesigură și proliferarea configurațiilor. 

  * Integrare în câteva minute.

Capabilități:

  * Gestionează configurația și nivelurile de acces pentru toate aplicațiile, mediile și echipele tale într-un singur loc.

  * Configurează orice mediu de dezvoltare sau de server cu o singură variabilă de mediu.

Avantaje:

  * Pagină principală bună.

  * Propunere de valoare clară.

  * Aplicație web excelentă vizual.

  * Date de exemplu superioare, de exemplu Algolia, AWS, Datadog, GitHub, Stripe etc.

  * Am vorbit cu fondatorul 30 de minute despre companie, UI etc. Dane pare bine informat, sincer despre avantaje/dezavantaje și un partener viabil.

  * Compania este în esență o companie Y Combinator tipică, cu 1 fondator. A strâns 120.000 USD în 2018-01.

  * Accentul este pe atingerea funcțiilor enterprise, în special trecerea de la găzduirea EnvKey în cloud la on-prem sau BYOC.

  * Cale potențială: începerea cu EnvKey pentru ușurința în utilizare, apoi mai târziu (sau în paralel) adăugarea Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant este un serviciu open source de gestionare a secretelor, care oferă stocare prietenoasă pentru utilizator și acces la secrete într-un mod sigur, de la dezvoltatorii de la Lyft.

Autentificare KMS: Confidant rezolvă problema oului și a găinii în autentificare folosind AWS KMS și IAM pentru a permite rolurilor IAM să genereze token-uri de autentificare sigure care pot fi verificate de Confidant. Confidant gestionează și permisiunile KMS pentru rolurile tale IAM, ceea ce permite rolurilor IAM să genereze token-uri care pot fi folosite pentru autentificare între servicii sau pentru transmiterea de mesaje criptate între servicii.

Criptare în repaus a secretelor versionate: Confidant stochează secretele în mod doar-adăugare în DynamoDB, generând o cheie de date KMS unică pentru fiecare revizie a fiecărui secret, folosind criptografie simetrică autentificată Fernet.

O interfață web prietenoasă pentru gestionarea secretelor: Confidant oferă o interfață web AngularJS care le permite utilizatorilor finali să gestioneze ușor secretele, mapările secretelor la servicii și istoricul modificărilor.


### Devolutions Password Server

https://server.devolutions.net/

Securizează, gestionează și monitorizează accesul la conturile și sesiunile privilegiate.

Un seif de parole cuprinzător și foarte securizat, care îți permite să controlezi accesul la conturile tale privilegiate, îmbunătățind în același timp vizibilitatea generală a rețelei pentru administratorii de sistem și oferind o experiență fluidă utilizatorilor finali.

Funcții: seif centralizat de parole al organizației, seif privat specific utilizatorului, manager de parole, injectare de credențiale,
integrare Active Directory, control al accesului bazat pe roluri, autentificare în doi factori, pregătit pentru enterprise, restricții IP, capabilități de gestionare, generator automat de parole, acces din aplicația mobilă, istoric al parolelor, rapoarte de acces, alerte prin e-mail.

  * suportă criptarea datelor

  * suportă mai multe scheme de autentificare, inclusiv LDAP, O365 și utilizatori locali CU suport MFA din mai multe surse

  * mai multe depozite/seifuri cu controale de acces fine pentru mai multe echipe

  * interfață web modernă

  * seifuri private de credențiale și conexiuni pentru credențiale/conexiuni personale

  * aplicații mobile pentru iOS/Android

  * jurnale de audit pentru fiecare intrare, cine/ce/când, cu o întrebare opțională despre motivul accesării

  * șabloane personalizabile (deși suportă nativ sute de tipuri de conexiuni)

  * multe alte funcții și un client greu pentru Windows/Mac (Remote Desktop Manager) cu care te poți sincroniza și care extinde mult opțiunile... conexiuni cu un singur clic

  * prețul nu este chiar rău - până la 15 utilizatori costă 500 USD pe an pentru serverul de parole


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Funcții ale versiunii locale (on-premise): 

  * Control total asupra sistemelor și infrastructurii tale de securitate end-to-end

  * Implementarea software-ului în centrul tău de date local sau în propria instanță de cloud privat virtual

  * Îndeplinirea obligațiilor legale și de reglementare care cer ca toate datele și sistemele să se afle local

Funcții ale versiunii cloud:

  * Modelul software ca serviciu îți permite să te înscrii și să începi imediat

  * Scalabilitate elastică pe măsură ce crești

  * Controale și redundanță furnizate de Azure cu SLA de disponibilitate de 99,9%

Feedback de la utilizatori:

  * Obișnuiam să folosim acest produs. A fost atât de ușor de ocolit, iar regulile funcționează doar pentru oameni deștepți. Utilizatorii leneși sau proști îl pot strica ușor într-o zonă de echipă. Prețurile sunt negociabile când vorbești cu ei.

  * Îl poți rula folosind SQL Express și o mașină cu Win 7. 

  * Ieftin.
