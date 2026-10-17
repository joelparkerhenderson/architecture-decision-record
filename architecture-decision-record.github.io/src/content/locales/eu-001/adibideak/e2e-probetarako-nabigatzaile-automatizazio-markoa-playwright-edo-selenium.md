## Arkitektura-erabakien erregistroa: E2E probetarako nabigatzaile-automatizazio markoa (Playwright vs Selenium)

### 1. **Testuingurua**

Gure muturretik muturrerako (E2E) proba-hodirako nabigatzaile-automatizazio marko bat aukeratzen ari gara. Marko hau gure CI/CD prozesuen osagai ezinbestekoa izango da, gure plataforman benetako erabiltzaileen interakzioak simulatzen dituzten probak exekutatuz. Zehazki, probek eszenatoki hauek estaliko dituzte: erabiltzaileen izen-ematea/saio-hasiera, fitxategi-kargatzeak, panelen interakzioak eta txosten-deskargak.

**Startup** gisa, gure ardatza **garapen arina** da, azkar iteratu eta eboluzionatzeko beharrarekin. Gure taldeak nagusiki **TypeScript** eta **Python** erabiltzen ditu, beraz funtsezkoa da lengoaia horietan probak idazteko gaitasuna. Gainera, plataformak **grafiko eta panel interaktiboak** ditu, eta, beraz, ezinbestekoa da automatizazio-tresnak UI aberats eta dinamikoak ondo onartzea.

Zeregin honetarako bi hautagaiak **Playwright** eta **Selenium** dira, bakoitzak bere indarrak eta konpentsazioak dituena. Marko hauek behean azaltzen diren ezaugarri eta eskakizunen arabera ebaluatu behar ditugu.

### 2. **Aztertutako aukerak**

- **Playwright** (Microsoft-ena)
- **Selenium** (Selenium Project-ena)

### 3. **Erabakiaren bultzatzaileak**

Gure erabakian eragiten duten faktoreak hauek dira:

1. **Garapen arina**: Aukeratutako tresnak garapen-ziklo azkar eta malguak ahalbidetu behar ditu.
2. **Lengoaia-euskarria**: Gure taldeak **TypeScript** zein **Python** onartzea behar du.
3. **UI interaktiboen probak**: Funtsezkoa da grafiko interaktiboak, panelak eta elementu dinamikoak modu fidagarrian probatzeko gaitasuna.
4. **Exekuzio-abiadura**: Lehentasun nagusia ez den arren, CI/CD hodietako errendimendua kontuan hartzeko faktorea da.
5. **Eskalagarritasuna**: Berehalako etorkizunean eskala handian planifikatzen ez dugun arren, soluzioak etorkizuneko hazkundea kudeatu dezakeela ziurtatu nahi dugu.
6. **Atzerako bateragarritasuna**: Sistema zaharrak eta nabigatzaile zaharrekiko bateragarritasuna ez dira kritikoak gure proiekturako une honetan.
7. **Mugikorren probak**: Berehalako ardatza ez den arren, markoak mugikorretarako moldatutako ezaugarriak probatzeko gai izan behar du edo horretarako zabalgarria izan behar du.
8. **Pantaila anitzeko probak**: Pantaila anitzeko konfigurazioen euskarria bigarren mailako eskakizuna da, bereziki erabiltzaile-lan-fluxu konplexuagoak probatzera eskalatzen badugu.
9. **Fitxategi-kargatzeen probak**: Markoak fitxategi-kargatzeak eraginkortasunez kudeatu behar ditu, gure proba-beharren oinarrizko eskakizuna.

### 4. **Ebaluazio-irizpideak**

- **Erabilera-erraztasuna**: Zein erraza da probak idaztea eta mantentzea?
- **Lengoaia-euskarria**: Markoak TypeScript eta Python onartzen ditu, gure taldeak gehien erabiltzen dituen bi lengoaiak?
- **UI interaktiboen probak**: Zein ondo kudeatzen ditu markoak erabiltzaile-interfaze interaktibo konplexuak, hala nola grafikoak, fitxategi-kargatzeak eta datu dinamikoak?
- **CI/CD integrazioa**: Zein ondo integratzen da markoa ohiko CI/CD tresna eta zerbitzuetan?
- **Nabigatzaile anitzeko euskarria**: Zein nabigatzaile onartzen dira eta zein ondo funtzionatzen dute?
- **Errendimendua eta abiadura**: Zein azkar exekutatzen dira probak, bereziki CI/CD hodi batean?
- **Eskalagarritasuna**: Zein ondo eskala dezake markoak proba gehiago edo eszenatoki konplexuagoak gehitzen badira?
- **Komunitatea eta ekosistema**: Zein aktiboa da markoaren komunitatea? Integrazio eta luzapen ugari eskuragarri al daude?

### 5. **Kontuan hartzekoak**

#### 5.1 **Playwright**

##### **Alde onak**:
1. **API adimentsuagoa tokiko fitxategi-kargatzeetarako**: Playwright-en tokiko fitxategiekin elkarreragiteko eta fitxategi-kargatzeak egiteko API-a sinpleagoa eta intuitiboagoa da. Horrek fitxategi-kargatzeen probak ezartzea eta mantentzea errazagoa egingo luke.
2. **Sintaxia eta kode-sorkuntza**: Playwright-ek sintaxi laburragoa eta zehatzagoa du. Horrek boilerplate kode gutxiago dakar, eta horrek mantentzeko gaitasuna eta garatzaileen eraginkortasuna hobetzen ditu. Gainera, sintaxi laburrago honek OpenAI kode-sorkuntzaren kalitatea hobetzen du, proba-scriptak automatikoki sortzea errazagoa eginez.
3. **UI interaktiboen probak**: Playwright bikaina da web aplikazio dinamiko eta interaktiboak probatzeko, hala nola grafiko aberatsak, erabiltzaile-interakzio konplexuak eta denbora errealeko eguneraketak dituztenak. WebSockets, WebRTC, shadow DOM-ak eta beste web teknologia moderno batzuk oso eraginkortasunez kudeatzen ditu.
4. **Nabigatzaile anitzeko euskarria**: Playwright-ek **Chromium**, **WebKit** eta **Firefox** onartzen ditu. Errendimendu koherentea du nabigatzaile hauetan, eta horrek gure proba-behar gehienak estali beharko lituzke.
5. **CI/CD integrazioa**: Playwright oztoporik gabe integratzen da CI/CD plataforma modernoekin (GitHub Actions, Jenkins, eta abar). Probak paraleloan exekuta ditzake nabigatzaile desberdinetan, proba-exekuzioen denborak optimizatuz eta garapen azkarrerako egokia izanik.
6. **Azkarra eta fidagarria**: Playwright orokorrean Selenium baino azkarragoa da, bereziki headless moduan, eta erresistenteagoa da web elementu asinkronoak kudeatzean.

##### **Alde txarrak**:
1. **Mugikorren proba mugatuak**: Playwright-ek nabigatzaileetarako mugikor-emulazioa onartzen duen arren, ez du Selenium-ek Appium-ekin duen integrazioa bezalako mugikor-proba natiborik benetako mugikor-proba egiteko.
2. **Ekosistema txikiagoa**: Playwright berriagoa eta Selenium baino finkatuagoa ez da oraindik. Komunitate azkar hazkorra eta dokumentazio ona duen arren, baliteke Selenium-ek eskaintzen duen plugin eta integrazioen ekosistema zabala oraindik ez izatea.
3. **Nabigatzaile-euskarri mugatua**: Playwright-ek nabigatzaile moderno nagusiak (Chrome, Safari, Firefox) estaltzen dituen arren, nabigatzaile zaharretarako (adib. Internet Explorer) euskarria ez da Selenium-ena bezain sendoa.

#### 5.2 **Selenium**

##### **Alde onak**:
1. **Historia luzeagoa eta helduaroa**: Selenium aspaldi dago eta emaitza frogatua du. Talde eta industria askotan oso erabilia da, eta horrek plugin, integrazio eta baliabideen ekosistema zabala ekarri du.
2. **Nabigatzaile anitzeko eta plataforma anitzeko euskarria**: Selenium-ek **nabigatzaile eta bertsio sorta zabala** onartzen du, **Internet Explorer** barne, eta **Docker**, **Selenium Grid** eta **hodei-zerbitzuak** bezalako tresnekin ere integra daiteke proba banatuetarako.
3. **Mugikorren probak**: Selenium, **Appium**-ekin duen integrazioaren bidez, askoz sendoagoa da mugikorren probetarako, Android eta iOS aplikazioak barne. Horrek mugikorra-lehenengo edo mugikorrean-astuna den proiektuetarako aukera hobea egiten du.
4. **Pantaila anitzeko probak**: Selenium-ek euskarri hobea eskaintzen du **hainbat pantaila** edo leiho anitzeko interakzio konplexuak dituzten eszenatokietarako.

##### **Alde txarrak**:
1. **Konplexutasuna**: Selenium-en API-a hitz-jario handiagokoa eta esplizituagoa da. Kasu batzuetan abantaila izan daitekeen arren, kode gehiago idatzi eta mantendu behar dela esan nahi du, eta horrek garatzailearen arintasuna murriztu dezake —startup ingurunean bereziki garrantzitsua dena—.
2. **Errendimendua**: Selenium orokorrean Playwright baino motelago exekutatzen da, bereziki headless moduan. Horrek CI/CD hodietan eragina izan dezake, bereziki proba kopurua hazten den heinean.
3. **UI interaktiboen probak**: Selenium ez da Playwright bezain leuna UI moderno eta interaktiboak probatzean, bereziki grafikoekin eta denbora errealeko datu-eguneraketekin. Konfigurazio eta kudeaketa gehiago behar ditu eduki dinamikoarekin modu fidagarrian elkarreragiteko.

### 6. **Alderaketaren laburpena**

| Ezaugarria                          | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Erabilera-erraztasuna**                   | Sintaxi laburragoa, UI modernoetarako intuitiboagoa | Esplizituagoa, boilerplate gehiago behar du  |
| **Lengoaia-euskarria**              | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **UI interaktiboen probak**        | Bikaina UI dinamiko eta denbora errealekoetarako          | UI oinarrizkoak kudeatzen ditu, baina hitz-jario eta konplexutasun handiagoz interakzio aberatsetarako |
| **Fitxategi-kargatzeen probak**           | API adimentsuagoa fitxategi-kargatzeetarako                  | API hitz-jariotsuagoa eta intuitibo gutxiagokoa         |
| **CI/CD integrazioa**             | Integrazio erraza GitHub Actions, Jenkins-ekin | Integrazio sendoa CI tresna askorekin    |
| **Mugikorren probak**                | Mugatua, emulazioa soilik                       | Euskarri osoa Appium bidez               |
| **Nabigatzaile anitzeko euskarria**         | Chromium, WebKit, Firefox                     | Euskarri osoa nabigatzaile nagusietan eta zaharretan |
| **Errendimendua**                   | Azkarra, headless probetarako optimizatua          | Motelagoa, bereziki headless moduan       |
| **Pantaila anitzeko probak**         | Mugatua                                       | Euskarri ona pantaila anitzeko konfigurazioetarako    |
| **Komunitatea eta ekosistema**       | Hazten ari da, dokumentazio ona                   | Handia, heldua, ekosistema zabala       |

### 7. **Erabakia**

Eskakizunak eta konpentsazioak kontuan hartu ondoren, **Playwright** da gure oraingo beharretarako aukera hobea. Tokiko fitxategi-kargatzeen probetarako API adimentsuagoak, sintaxi zehatzak eta UI interaktiboen probetarako euskarri sendoak gure garapen-ziklo arinerako ezin hobeto egokitzen dute. **TypeScript** zein **Python** onartzen dituela funtsezkoa da gure taldearentzat, eta markoaren proba-ikuspegi modernoak kode garbia eta mantentzeko erraza idatzi ahalko digu.

**Selenium** tresna bikaina izaten jarraitzen duen arren, bereziki mugikorren probetarako, nabigatzaile zaharretarako euskarria eta pantaila anitzeko konfigurazioetarako, gure oraingo beharretarako ez da hain egokia. Bere hitz-jarioak, errendimendu motelagoak eta grafikoak bezalako UI dinamikoen kudeaketa konplexuagoak gure erabilera-kasurako ez da hain optimoa bihurtzen dute.

### 8. **Ondorioak**

- **Berehalako ekintza**: **Playwright** hartuko dugu gure E2E probetarako, izen-ematea, saio-hasiera, fitxategi-kargatzeak, panelak eta txosten-deskargak barne hartzen dituzten erabiltzaile-fluxuak probatzean zentratuz.
- **Epe luzerako kontuan hartzekoak**: Playwright ekosistemaren bilakaerari erreparatuko diogu. Gure beharrak aldatzen badira, bereziki mugikorren probei edo nabigatzaile zaharretarako euskarriari dagokienez, Selenium berriz aztertu dezakegu.
- **Prestakuntza eta dokumentazioa**: Garapen-taldeek Playwright-en API-arekin ohitu beharko dute, bereziki UI dinamikoak eta fitxategi-kargatzeak kudeatzeko.
- **Migrazioa**: Lehendik dauden Selenium probak (baleude) pixkanaka Playwright-era migratuko dira.

### 9. **Etorkizuneko kontuan hartzekoak**
