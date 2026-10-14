# Arhitektuuriotsuse kirje: programmeerimiskeel Rust

Otsuse number: AR-001

Otsuse pealkiri: programmeerimiskeele Rust kasutuselevõtt

Kuupäev: 1. detsember 2021

Olek: Aktsepteeritud

### Probleemi püstitus

Tarkvararakenduste arendamist jätkates oleme täheldanud, et potentsiaalsete turvaaukude leevendamine ja käitusaja vigade ennetamine muutub üha keerulisemaks. Olemasolevate programmeerimiskeeltega, nagu C ja C++, puutume jätkuvalt kokku probleemidega nagu puhvri ületäitumine, mälulekked ja määratlemata käitumine, mis viib rakenduste kokkujooksmisteni. Vajame programmeerimiskeelt, mis pakub mäluohutuse garantiisid ja on piisavalt tõhus jõudluskriitiliste rakenduste toetamiseks.

### Kaalutlused

Olemasolevate probleemide lahendamiseks on loodud mitu programmeerimiskeelt. Nende hulgas on programmeerimiskeel Rust pälvinud arendajate kogukonnas märkimisväärset tähelepanu oma ainulaadsete disainiomaduste tõttu. Kaalutlused hõlmavad;

1. Mäluohutus ja turvalisus

2. Jõudlus ja tõhusus

3. Kogukonna toetus ja kasutuselevõtt

4. Õppimiskõver

5. Tööriistad ja ökosüsteem

6. Ühilduvus olemasolevate tarkvarasüsteemidega.

### Piirangud

Uue programmeerimiskeele kasutuselevõtt nõuab arendajate ümberõpet, mis võtab aega ja ressursse. Keele integreerimine olemasolevasse arendustöövoogu võib olla väljakutse. Peame tagama ühilduvuse olemasolevate süsteemidega ja vältima katkestavaid muudatusi järjepidevuse säilitamiseks.

### Teostus

1. Meie arendusmeeskond läbib koolituse, et programmeerimiskeelt Rust õppida ja sellega tutvuda.

2. Loome proovi korras Rustiga uue projekti, et hinnata selle ühilduvust ja sobivust meie arenduseesmärkidele.

3. Migreerime järk-järgult olemasolevad C-s ja C++-s kirjutatud süsteemid Rustile.

4. Teeme koostööd Rusti kogukonnaga, et uurida saadaolevaid tööriistu ja teeke, mis võivad meie arendustöövoogu täiustada.

5. Jälgime Rusti jõudlust ja võrdleme seda regulaarselt olemasolevate programmeerimiskeelte jõudlusega.

6. Võtame pikaajalise lähenemise, mis tasakaalustab koolituse, integratsiooni kulud ja Rusti kasutamise võimalikud eelised.

### Põhjendus

Võtsime Rusti kasutusele selle ainulaadsete funktsioonide tõttu, mis on loodud mäluohutuse ja turvalisuse garantiide pakkumiseks, säilitades samal ajal jõudluse ja tõhususe. Rusti töökindel tüübisüsteem, laenukontroll (borrow checker) ja mäluohutuse kontseptsioonid muudavad selle väga sobivaks jõudluskriitiliste ja ohutuskriitiliste rakenduste arendamiseks. Lisaks on Rustil märkimisväärne arendajate kogukond, mis annab meile juurdepääsu laiale valikule tööriistadele, teekidele ja ökosüsteemile, mis toetavad meie arendustöövoogu. Kuigi Rustiga kaasneb õppimiskõver, usume, et Rusti kasutuselevõtu eelised kaaluvad kulud üles ja pakuvad suurepärase võimaluse jätkuvaks kasvuks ja innovatsiooniks.

### Tagajärjed

1. Rusti kasutuselevõtt nõuab märkimisväärset ajalist ja ressursiinvesteeringut arendajate koolitamiseks ja keele integreerimiseks olemasolevasse arendustöövoogu.

2. Rusti kasutuselevõtt võib põhjustada teatud määral ühilduvusprobleeme olemasolevate süsteemidega, mis nõuab refaktoreerimist ja muudatusi.

3. Rusti kasutuselevõtt võib suurendada arendajate arvu, kes saavad meie projektile kaasa aidata, meelitades ligi Rusti arendajaid, kes tahavad töötada põnevate projektidega.

4. Kasutuselevõtt võib viia paranenud jõudluse, tõhususe ja ohutuseni võrreldes olemasolevate keeltega.

5. Lõpuks kaasneb Rusti kasutuselevõtuga potentsiaalne eelis vähendada meie rakenduste turvaauke.
   
<h6>Allikaviide: see leht on loodud ChatGPT-ga ja seejärel selguse ja vormingu huvides toimetatud.</h6>
