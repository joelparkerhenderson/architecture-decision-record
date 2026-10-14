# Architekturális döntési feljegyzés: adatbázis-technológia kiválasztása

## Állapot

Elfogadott

## Háttér

Új alkalmazást tervezünk, amely az adatok skálázható és teljesítőképes tárolását és lekérdezését igényli. Három, gyakran használt adatbázis-technológia-típust azonosítottunk: relációs adatbázisok, dokumentumadatbázisok és eseményadatbázisok.

A relációs adatbázisok az adatokat rögzített sémájú táblákban tárolják, és szigorú adatintegritási megszorításokat érvényesítenek. Alkalmasak olyan alkalmazásokhoz, amelyek összetett adatkapcsolatokat és tranzakciókat igényelnek. Példák: MySQL, PostgreSQL és Oracle.

A dokumentumadatbázisok az adatokat JSON-szerű dokumentumokban tárolják, és séma nélküliek. Jól illeszkednek olyan alkalmazásokhoz, amelyek rugalmas adatmodelleket és vízszintes skálázást igényelnek. Példák: MongoDB, Couchbase és Amazon DynamoDB.

Az eseményadatbázisok az adatokat események sorozataként tárolják, rögzítve az adatok minden változását. Alkalmasak olyan alkalmazásokhoz, amelyek auditálást, eseményforrást (event sourcing) és összetett adatfeldolgozást igényelnek. Példák: Apache Kafka, Apache Pulsar és AWS Kinesis.

## Döntés

Alkalmazásunk követelményeinek és megszorításainak gondos értékelése után úgy döntöttünk, hogy dokumentumadatbázist használunk.

## Indoklás

Azért választottunk dokumentumadatbázist, mert:

1. Alkalmazásunknak rugalmas adatmodellre van szüksége, amely idővel fejlődhet. A dokumentumadatbázisok lehetővé teszik, hogy az adatokat séma nélküli formátumban tároljuk, ami azt jelenti, hogy új mezőket adhatunk hozzá vagy módosíthatjuk a meglévő dokumentumok szerkezetét az adatbázissémájának módosítása nélkül.

2. Alkalmazásunknak vízszintesen kell skálázódnia a nagy adat- és forgalommennyiség kezeléséhez. A dokumentumadatbázisok beépített támogatást nyújtanak a shardinghoz és a replikációhoz, ami lehetővé teszi, hogy az adatokat több kiszolgálón osszuk el, és magas olvasási és írási átviteli sebességet kezeljünk.

3. Alkalmazásunknak gyors és hatékony adatlekérdezésre van szüksége. A dokumentumadatbázisok erőteljes indexelési és lekérdezési képességeket nyújtanak, amelyek lehetővé teszik, hogy gyorsan és hatékonyan kérjük le az adatokat.

4. Alkalmazásunknak nincs szüksége összetett tranzakciókra vagy adatkapcsolatokra. Bár a relációs adatbázisok kiválóan érvényesítik az adatintegritási megszorításokat és kezelik az összetett tranzakciókat, alkalmazásunknak nincsenek ilyen követelményei. A dokumentumadatbázisok elegendő konzisztencia- és tartóssági garanciát nyújthatnak az esetünkben.

## Következmények

A dokumentumadatbázis választásával be kell fektetnünk a konkrétan választott technológia megismerésébe és megértésébe. Ezenkívül gondoskodnunk kell arról, hogy alkalmazásunk adatmodellje jól illeszkedjen a dokumentumadatbázis adatmodelljéhez a teljesítmény és a skálázhatóság maximalizálása érdekében.

Úgy véljük azonban, hogy a dokumentumadatbázis használatának előnyei meghaladják a költségeket, és hogy ez a legjobb illeszkedés alkalmazásunk követelményeihez és megszorításaihoz.
