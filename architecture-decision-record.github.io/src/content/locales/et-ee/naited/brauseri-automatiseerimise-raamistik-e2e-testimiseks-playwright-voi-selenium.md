## Arhitektuuriotsuse kirje: brauseri automatiseerimise raamistik E2E-testimiseks (Playwright või Selenium)

### 1. **Kontekst**

Valime brauseri automatiseerimise raamistikku oma otsast-otsani (E2E) testimise torujuhtme jaoks. See raamistik on meie CI/CD protsesside lahutamatu osa, käitades teste, mis simuleerivad päris kasutaja interaktsioone meie platvormil. Täpsemalt katavad testid stsenaariume nagu kasutaja registreerumine/sisselogimine, failide üleslaadimine, armatuurlaua interaktsioonid ja aruannete allalaadimine.

**Idufirmana** keskendume **agiilsele arendusele**, vajadusega kiiresti iteratsioone teha ja areneda. Meie meeskond töötab peamiselt **TypeScripti** ja **Pythoniga** ning nendes keeltes testide kirjutamise võime on hädavajalik. Lisaks sisaldab platvorm **interaktiivseid diagramme ja armatuurlaudu**, mis teeb kriitiliseks, et automatiseerimistööriist toetaks rikkalikke, dünaamilisi UI-sid hästi.

Kaks kandidaati selle ülesande jaoks on **Playwright** ja **Selenium**, kummalgi oma tugevused ja kompromissid. Peame neid raamistikke hindama allpool kirjeldatud funktsioonide ja nõuete põhjal.

### 2. **Kaalutud valikud**

- **Playwright** (Microsoftilt)
- **Selenium** (Selenium Projectilt)

### 3. **Otsuse liikumapanevad jõud**

Meie otsust mõjutavad järgmised tegurid:

1. **Agiilne arendus**: valitud tööriist peab võimaldama kiireid, paindlikke arendustsükleid.
2. **Keeletugi**: meie meeskond nõuab tuge nii **TypeScriptile** kui ka **Pythonile**.
3. **Interaktiivsete UI-de testimine**: võime usaldusväärselt testida interaktiivseid diagramme, armatuurlaudu ja dünaamilisi elemente on hädavajalik.
4. **Käitusaja kiirus**: kuigi see pole peamine mure, on jõudlus CI/CD torujuhtmetes kaalutlus.
5. **Skaleeritavus**: ei plaani lähitulevikus massilist skaleerimist, kuid tahame tagada, et lahendus suudab tulevast kasvu käsitleda.
6. **Tagasiulatuv ühilduvus**: pärandsüsteemid ja ühilduvus vanemate brauseritega ei ole meie projekti jaoks praegu kriitilised.
7. **Mobiilitestimine**: kuigi see pole vahetu fookus, peaks raamistik suutma testida mobiiliga ühilduvaid funktsioone või olema selliste kasutusjuhtude jaoks laiendatav.
8. **Mitme ekraaniga testimine**: mitme ekraaniga seadistuste tugi on teisene nõue, eriti kui skaleerime hiljem keerukamate kasutajatöövoogude testimiseni.
9. **Failide üleslaadimise testimine**: raamistik peab tõhusalt käsitlema failide üleslaadimist, mis on meie testimisvajaduste põhinõue.

### 4. **Hindamiskriteeriumid**

- **Kasutuslihtsus**: kui lihtne on teste kirjutada ja hooldada?
- **Keeletugi**: kas raamistik toetab TypeScripti ja Pythonit, kahte keelt, mida meie meeskond kõige rohkem kasutab?
- **Interaktiivsete UI-de testimine**: kui hästi käsitleb raamistik keerukaid, interaktiivseid kasutajaliideseid nagu diagrammid, failide üleslaadimised ja dünaamilised andmed?
- **CI/CD integratsioon**: kui hästi integreerub raamistik tavaliste CI/CD tööriistade ja teenustega?
- **Mitme brauseri tugi**: milliseid brausereid toetatakse ja kui hästi need toimivad?
- **Jõudlus ja kiirus**: kui kiiresti testid jooksevad, eriti CI/CD torujuhtmes?
- **Skaleeritavus**: kui hästi saab raamistik skaleeruda, kui lisatakse rohkem teste või keerukamaid stsenaariume?
- **Kogukond ja ökosüsteem**: kui aktiivne on raamistiku kogukond? Kas integratsioone ja pluginaid on rohkelt?

### 5. **Kaalutlused**

#### 5.1 **Playwright**

##### **Plussid**:
1. **Nutikam API kohalike failide üleslaadimiseks**: Playwrighti API kohalike failidega suhtlemiseks ja failide üleslaadimiseks on lihtsam ja intuitiivsem. See teeks failide üleslaadimise testide teostamise ja hooldamise lihtsamaks.
2. **Süntaks ja koodi genereerimine**: Playwrightil on lühem, kokkuvõtlikum süntaks. See annab vähem standardkoodi, mis parandab hooldatavust ja arendajate tõhusust. Lisaks parandab lühem süntaks OpenAI koodi genereerimise kvaliteeti, muutes testiskriptide automaatse genereerimise lihtsamaks.
3. **Interaktiivsete UI-de testimine**: Playwright paistab silma dünaamiliste, interaktiivsete veebirakenduste testimisel, näiteks neil, millel on rikkalikud diagrammid, keerukad kasutaja interaktsioonid ja reaalajauuendused. See käsitleb WebSocketeid, WebRTC-d, shadow DOM-i ja muid kaasaegseid veebitehnoloogiaid väga tõhusalt.
4. **Mitme brauseri tugi**: Playwright toetab **Chromiumi**, **WebKiti** ja **Firefoxi**. Sellel on nende brauserite lõikes ühtlane jõudlus, mis peaks katma enamiku meie testimisvajadustest.
5. **CI/CD integratsioon**: Playwright integreerub sujuvalt kaasaegsete CI/CD platvormidega (GitHub Actions, Jenkins jne). See saab teste paralleelselt erinevates brauserites käitada, mis optimeerib testide käitusaegu ja teeb selle sobivaks kiireks arenduseks.
6. **Kiire ja töökindel**: Playwright on üldiselt Seleniumist kiirem, eriti headless-režiimis, ja vastupidavam asünkroonsete veebielementide suhtes.

##### **Miinused**:
1. **Piiratud mobiilitestimine**: kuigi Playwright toetab brauserite mobiilieeskuju, puuduvad sellel sisseehitatud mobiilitestimise võimalused nagu Seleniumi integratsioon Appiumiga tõelise mobiilitestimise jaoks.
2. **Väiksem ökosüsteem**: Playwright on endiselt uuem ja vähem väljakujunenud kui Selenium. Kuigi sellel on kiiresti kasvav kogukond ja hea dokumentatsioon, ei pruugi sellel veel olla Seleniumi pakutavat suurt pluginate ja integratsioonide ökosüsteemi.
3. **Piiratud brauseritugi**: kuigi Playwright katab suured kaasaegsed brauserid (Chrome, Safari, Firefox), ei ole selle tugi vanematele brauseritele (nt Internet Explorer) nii töökindel kui Seleniumil.

#### 5.2 **Selenium**

##### **Plussid**:
1. **Pikem ajalugu ja küpsus**: Selenium on olnud olemas pikka aega ja sellel on tõestatud ajalugu. Seda kasutavad laialdaselt paljud meeskonnad ja valdkonnad, mis on viinud pluginate, integratsioonide ja ressursside suure ökosüsteemini.
2. **Mitme brauseri ja platvormi tugi**: Selenium toetab **laia valikut brausereid** ja versioone, sealhulgas **Internet Explorerit**, ning seda saab integreerida ka erinevate tööriistadega nagu **Docker**, **Selenium Grid** ja **pilveteenused** hajutatud testimiseks.
3. **Mobiilitestimine**: Selenium on oma integratsiooni **Appiumiga** kaudu mobiilitestimiseks palju töökindlam, sealhulgas nii Androidi kui ka iOS-i rakenduste jaoks. See teeb sellest parema valiku projektidele, mis on mobile-first või tugeva mobiilse fookusega.
4. **Mitme ekraaniga testimine**: Selenium pakub paremat tuge **mitme ekraani** stsenaariumidele või keerukatele mitme akna interaktsioonidele.

##### **Miinused**:
1. **Keerukus**: Seleniumi API on sõnarohkem ja selgesõnalisem. Kuigi see võib mõnel juhul olla eelis, tähendab see rohkem koodi kirjutamiseks ja hooldamiseks, mis võib vähendada arendajate nobedust – eriti oluline idufirma keskkonnas.
2. **Jõudlus**: Selenium jookseb üldiselt Playwrightist aeglasemalt, eriti headless-režiimis. See võib mõjutada CI/CD torujuhtmeid, eriti kui testide arv kasvab.
3. **Interaktiivsete UI-de testimine**: Selenium ei ole nii sujuv kui Playwright kaasaegsete, interaktiivsete veebi-UI-de testimisel, eriti diagrammide ja reaalajas andmeuuendustega. See nõuab rohkem seadistust ja käsitlemist, et dünaamilise sisuga usaldusväärselt suhelda.

### 6. **Võrdluse kokkuvõte**

| Funktsioon                        | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Kasutuslihtsus**                | Lühem süntaks, intuitiivsem kaasaegsetele UI-dele | Selgesõnalisem, vajab rohkem standardkoodi |
| **Keeletugi**                     | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Interaktiivsete UI-de testimine** | Suurepärane dünaamilistele reaalaja-UI-dele | Käsitleb põhi-UI-sid, kuid sõnarohkem ja keerukam rikkalike interaktsioonide jaoks |
| **Failide üleslaadimise testimine** | Nutikam API failide üleslaadimiseks         | Sõnarohkem, vähem intuitiivne API         |
| **CI/CD integratsioon**           | Lihtne integratsioon GitHub Actionsi, Jenkinsiga | Tugev integratsioon paljude CI-tööriistadega |
| **Mobiilitestimine**              | Piiratud, ainult eeskuju                      | Täielik tugi Appiumi kaudu                |
| **Mitme brauseri tugi**           | Chromium, WebKit, Firefox                     | Täielik tugi suurtele ja vanematele brauseritele |
| **Jõudlus**                       | Kiire, optimeeritud headless-testimiseks      | Aeglasem, eriti headless-režiimis         |
| **Mitme ekraaniga testimine**     | Piiratud                                      | Hea tugi mitme ekraaniga seadistustele    |
| **Kogukond ja ökosüsteem**        | Kasvav, hea dokumentatsioon                   | Suur, küps, ulatuslik ökosüsteem          |

### 7. **Otsus**

Pärast nõuete ja kompromisside kaalumist on **Playwright** meie praeguste vajaduste jaoks parem valik. Selle nutikam API kohalike failide üleslaadimise testimiseks, kokkuvõtlik süntaks ja tugev tugi interaktiivsete UI-de testimiseks teevad sellest ideaalse sobivuse meie agiilse arendustsükliga. Asjaolu, et see toetab nii **TypeScripti** kui ka **Pythonit**, on meie meeskonna jaoks ülioluline ning raamistiku kaasaegne lähenemine testimisele võimaldab meil kirjutada puhast, hooldatavat koodi.

Kuigi **Selenium** jääb suurepäraseks tööriistaks, eriti mobiilitestimise, vanemate brauserite toe ja mitme ekraaniga seadistuste jaoks, sobib see meie praeguste vajaduste jaoks vähem. Selle sõnarohkus, aeglasem jõudlus ja keerukam dünaamiliste UI-de nagu diagrammide käsitlemine teevad selle meie kasutusjuhu jaoks vähem optimaalseks.

### 8. **Tagajärjed**

- **Vahetu tegevus**: võtame oma E2E-testimiseks kasutusele **Playwrighti**, keskendudes registreerumist, sisselogimist, failide üleslaadimist, armatuurlaudu ja aruannete allalaadimist hõlmavate kasutajavoogude testimisele.
- **Pikaajalised kaalutlused**: jälgime Playwrighti arenevat ökosüsteemi. Kui meie vajadused muutuvad, eriti mobiilitestimise või vanemate brauserite toe osas, võime Seleniumi uuesti kaaluda.
- **Koolitus ja dokumentatsioon**: arendusmeeskonnad peavad Playwrighti API-ga tuttavaks saama, eriti dünaamiliste UI-de ja failide üleslaadimise käsitlemiseks.
- **Migratsioon**: olemasolevad Seleniumi testid (kui neid on) migreeritakse järk-järgult Playwrightile.

### 9. **Tulevased kaalutlused**
