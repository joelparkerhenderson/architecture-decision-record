# AWS-i arhitektuuriotsuse kirjete protsess

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Arhitektuuriotsuse kirje (architectural decision record, ADR) on dokument, mis kirjeldab valikuid, mida meeskond teeb tarkvaraarhitektuuri olulise aspekti kohta, mida ta kavatseb ehitada. Iga ADR kirjeldab arhitektuuriotsust, selle konteksti ja tagajärgi. ADR-idel on olek ja seetõttu järgivad need elutsüklit. ADR-ide näiteid vaata lisast.

ADR-protsess annab tulemuseks arhitektuuriotsuse kirjete kogumi. See kogum moodustab otsuste logi. Otsuste logi pakub projekti konteksti kõrval üksikasjalikku teavet teostuse ja disaini kohta. Projekti liikmed vaatavad iga ADR-i pealkirja läbi, et saada ülevaade projekti kontekstist. Seejärel loevad nad ADR-e, et saada põhjalik arusaam projekti teostus- ja disainivalikutest.

Kui meeskond ADR-i aktsepteerib, muutub see muutumatuks. Kui uued arusaamad nõuavad teistsugust otsust, teeb meeskond ettepaneku uue ADR-i kohta. Kui meeskond uue ADR-i aktsepteerib, asendab see eelmise ADR-i.

## ADR-protsessi ulatus

Projekti liikmed peaksid kirjutama ADR-i iga arhitektuuriliselt olulise otsuse kohta, mis mõjutab tarkvaraprojekti või toodet, sealhulgas (Richards ja Ford 2020):

* Struktuur (näiteks mustrid nagu mikroteenused)

* Mittefunktsionaalsed nõuded (turvalisus, kõrge käideldavus, veataluvus)

* Sõltuvused (komponentide sidumine)

* Liidesed (API-d ja avaldatud lepingud)

* Ehitusmeetodid (teegid, raamistikud, tööriistad, protsessid)

* Funktsionaalsed ja mittefunktsionaalsed nõuded on ADR-protsessi kõige levinumad sisendid.


## ADR-i sisu

Kui meeskond tuvastab ADR-i vajaduse, hakkavad meeskonnaliikmed ADR-i kirjutama kogu projekti hõlmava malli alusel. (Mallide näiteid vaata GitHubi ADR-i organisatsioonist.) Mall lihtsustab ADR-i kirjutamist ja tagab, et ADR sisaldab kogu asjakohast teavet. Vähemalt peaks iga ADR määratlema otsuse konteksti, otsuse enda ning otsuse tagajärjed projektile ja selle tulemitele. (Nende jaotiste näiteid vaata lisast.) Üks ADR-i struktuuri võimsamaid külgi on keskendumine otsuse põhjusele, mitte sellele, kuidas meeskond selle teostas. Kui mõistad, miks meeskond otsuse tegi, on teistel meeskonnaliikmetel seda lihtsam aktsepteerida ja sa hoiad ära, et teised arhitektid, kes otsustusprotsessis ei osalenud, otsuse hiljem tühistaksid.


## ADR-ide kasutuselevõtu protsess

Kuigi iga meeskonnaliige võib ADR-i kirjutada, peaks meeskond kehtestama ADR-ide omandi määratluse. Iga autor, kes on ADR-i omanik, peaks ADR-i sisu aktiivselt hooldama ja sellest teavitama. Selle omandi selgitamiseks nimetab see juhend ADR-i autoreid hilisemates jaotistes ADR-i omanikeks. Teised meeskonnaliikmed võivad ADR-ile igal ajal kaasa aidata. Kui ADR-i sisu muutub enne, kui meeskond ADR-i aktsepteerib, peab omanik need muudatused kinnitama.

Kui meeskond on arhitektuuriotsuse ja selle omaniku tuvastanud, esitab ADR-i omanik protsessi alguses ADR-i olekuga **Proposed** (ettepanek). Olekus Proposed olev ADR on ülevaatuseks valmis.

Seejärel alustab ADR-i omanik selle ADR-i ülevaatusprotsessi. ADR-i ülevaatusprotsessi eesmärk on, et meeskond otsustaks, kas ADR-i aktsepteerida, leida, et see vajab ümbertöötamist, või ADR tagasi lükata. Projektimeeskond, sealhulgas omanik, vaatab ADR-i üle. Ülevaatuskoosolek peaks algama ADR-i lugemiseks eraldatud ajaga. Keskmiselt piisab 10–15 minutist. Selle aja jooksul lisab iga meeskonnaliige kommentaare ja küsimusi, et märkida ebaselged teemad. Ülevaatusetapi lõpus loeb ADR-i omanik iga kommentaari läbi ja arutab neid meeskonnaga.

Kui meeskond leiab ADR-i parandamiseks tegevuspunkte, jääb ADR-i olek **Proposed**. ADR-i omanik koondab tegevused ja teeb meeskonnaga koostööd, et määrata igale tegevusele vastutaja. Iga meeskonnaliige võib tegevuspunktidele kaasa aidata ja need lahendada. ADR-i omaniku vastutus on ülevaatusprotsess uuesti ajastada.

Meeskond võib ka otsustada ADR-i tagasi lükata. Sel juhul lisab ADR-i omanik tagasilükkamise põhjuse, et vältida tulevasi arutelusid samal teemal. Omanik muudab ADR-i oleku väärtuseks **Rejected** (tagasi lükatud).

Kui meeskond ADR-i kinnitab, lisab omanik ajatempli, versiooni ja huvirühmade loendi. Seejärel värskendab omanik oleku väärtuseks **Accepted** (aktsepteeritud).

ADR ja sellest tekkiv otsuste logi esindavad meeskonna otsuseid ning pakuvad kõigi otsuste ajalugu. Võimalusel kasutab meeskond ADR-e viitena kooditöö ja arhitektuuri ülevaatustel. Lisaks koodiülevaatuste, disainitöö ja teostustöö tegemisele peaksid meeskonnaliikmed toote strateegiliste otsuste puhul ADR-e nõu pidama.

Heade tavade kohaselt peaks kõik tarkvaramuudatused läbima kolleegide ülevaatuse ja nõudma vähemalt ühte kinnitust. Koodiülevaatuse käigus võib ülevaataja leida muudatuse, mis rikub ühte või mitut ADR-i. Sel juhul palub ülevaataja koodimuudatuse autoril koodi parandada ja jagab ADR-i(de) linki. Kui autor koodi parandab, saab ta kolleegist ülevaatajalt kinnituse ja kood liidetakse põhikoodibaasi.


## ADR-i ülevaatusprotsess

Kui meeskond on ADR-i aktsepteerinud või tagasi lükanud, peaks ta seda käsitlema muutumatu dokumendina. Olemasoleva ADR-i muutmiseks peab meeskond kirjutama uue ADR-i, kehtestama uue ADR-i ülevaatusprotsessi ja ADR-i kinnitama. Kui meeskond uue ADR-i kinnitab, peab omanik muutma vana ADR-i oleku väärtuseks **Superseded** (asendatud). 
