## Arkitektúrákvörðunarskrá: vafrasjálfvirknirammi fyrir E2E-prófanir (Playwright eða Selenium)

### 1. **Samhengi**

Við erum að velja vafrasjálfvirknirammi fyrir E2E-prófunarleiðslu okkar (end-to-end). Þessi rammi mun vera ómissandi hluti af CI/CD-ferlum okkar og keyra próf sem herma eftir raunverulegum samskiptum notenda á vettvangi okkar. Einkum munu prófin ná yfir sviðsmyndir eins og nýskráningu/innskráningu notenda, skráaupphleðslur, samskipti við mælaborð og niðurhal skýrslna.

Sem **sprotafyrirtæki** beinist áhersla okkar að **liprri þróun**, með þörf fyrir að þróa hratt í áföngum. Teymið okkar vinnur aðallega með **TypeScript** og **Python**, og hæfileikinn til að skrifa próf á þessum málum er nauðsynlegur. Auk þess inniheldur vettvangurinn **gagnvirk myndrit og mælaborð**, sem gerir það mikilvægt að sjálfvirknitólið styðji ríkulegt, kvikt viðmót vel.

Keppinautarnir tveir um þetta verkefni eru **Playwright** og **Selenium**, hvor með sína styrkleika og málamiðlanir. Við þurfum að meta þessa ramma út frá eiginleikum og kröfum sem lýst er hér að neðan.

### 2. **Valkostir sem voru skoðaðir**

- **Playwright** (frá Microsoft)
- **Selenium** (frá Selenium Project)

### 3. **Drifkraftar ákvörðunar**

Þættirnir sem hafa áhrif á ákvörðun okkar eru eftirfarandi:

1. **Lipur þróun**: Tólið sem valið er verður að gera hraðar og sveigjanlegar þróunarlotur mögulegar.
2. **Stuðningur við forritunarmál**: Teymið okkar krefst stuðnings við bæði **TypeScript** og **Python**.
3. **Prófun gagnvirks viðmóts**: Hæfileikinn til að prófa gagnvirk myndrit, mælaborð og kvika þætti á áreiðanlegan hátt er nauðsynlegur.
4. **Keyrsluhraði**: Þótt það sé ekki aðalatriði eru afköst í CI/CD-leiðslum sjónarmið.
5. **Stigstærð**: Við áformum ekki mikla stækkun í nánustu framtíð, en við viljum tryggja að lausnin ráði við framtíðarvöxt.
6. **Afturábak samhæfni**: Eldri kerfi og samhæfni við eldri vafra eru ekki mikilvæg fyrir verkefni okkar að svo stöddu.
7. **Prófun á farsímum**: Þótt það sé ekki bein áhersla ætti ramminn að geta prófað svörunarfúsa eiginleika fyrir farsíma eða verið útvíkkanlegur fyrir slík notkunartilvik.
8. **Prófun með mörgum skjám**: Stuðningur við uppsetningar með mörgum skjám er aukakrafa, einkum ef við stækkum einhvern tímann í prófanir á flóknari vinnuflæði notenda.
9. **Prófun á skráaupphleðslu**: Ramminn verður að meðhöndla skráaupphleðslur á skilvirkan hátt, sem er kjarnakrafa í prófunarþörfum okkar.

### 4. **Matsviðmið**

- **Auðveld notkun**: Hversu auðvelt er að skrifa og viðhalda prófum?
- **Stuðningur við forritunarmál**: Styður ramminn TypeScript og Python, málin tvö sem teymið okkar notar oftast?
- **Prófun gagnvirks viðmóts**: Hversu vel meðhöndlar ramminn flókin, gagnvirk notendaviðmót eins og myndrit, skráaupphleðslur og kvik gögn?
- **CI/CD-samþætting**: Hversu vel samþættist ramminn algengum CI/CD-verkfærum og þjónustum?
- **Stuðningur við marga vafra**: Hvaða vafrar eru studdir og hversu vel standa þeir sig?
- **Afköst og hraði**: Hversu hratt keyra próf, einkum í CI/CD-leiðslu?
- **Stigstærð**: Hversu vel getur ramminn stækkað ef fleiri próf eða flóknari sviðsmyndum er bætt við?
- **Samfélag og vistkerfi**: Hversu virkt er samfélag rammans? Eru til nægar samþættingar og viðbætur?

### 5. **Sjónarmið**

#### 5.1 **Playwright**

##### **Kostir**:
1. **Snjallara API fyrir staðbundnar skráaupphleðslur**: API Playwright til að eiga við staðbundnar skrár og framkvæma skráaupphleðslur er einfaldara og innsæislegra. Þetta myndi gera auðveldara að útfæra og viðhalda prófum á skráaupphleðslu.
2. **Setningafræði og kóðamyndun**: Playwright hefur styttri og hnitmiðaðri setningafræði. Þetta leiðir til minni staðlaðs kóða, sem bætir viðhaldshæfni og skilvirkni þróunaraðila. Auk þess bætir þessi styttri setningafræði gæði kóðamyndunar OpenAI, sem gerir auðveldara að mynda prófunarskriftur sjálfvirkt.
3. **Prófun gagnvirks viðmóts**: Playwright skarar fram úr í prófun kvikra, gagnvirkra vefforrita, svo sem þeirra með ríkum myndritum, flóknum samskiptum notenda og rauntímauppfærslum. Það meðhöndlar WebSockets, WebRTC, skuggaDOM og aðra nútíma vefttækni mjög vel.
4. **Stuðningur við marga vafra**: Playwright styður **Chromium**, **WebKit** og **Firefox**. Það hefur samræmd afköst í þessum vöfrum, sem ætti að ná yfir flestar prófunarþarfir okkar.
5. **CI/CD-samþætting**: Playwright samþættist snurðulaust við nútíma CI/CD-vettvanga (GitHub Actions, Jenkins o.s.frv.). Það getur keyrt próf samhliða í ólíkum vöfrum, sem fínstillir keyrslutíma prófa og gerir það hentugt fyrir hraða þróun.
6. **Hratt og áreiðanlegt**: Playwright er almennt hraðara en Selenium, einkum í hauslausri stillingu, og seigara þegar tekist er á við ósamstillta vefþætti.

##### **Gallar**:
1. **Takmörkuð prófun á farsímum**: Þótt Playwright styðji hermun farsíma fyrir vafra skortir það innbyggða getu til prófunar á farsímum eins og samþætting Selenium við Appium fyrir raunverulegar farsímaprófanir.
2. **Minna vistkerfi**: Playwright er enn nýrra og minna rótgróið en Selenium. Þótt það eigi ört vaxandi samfélag og góða skjölun hefur það hugsanlega ekki enn hið mikla vistkerfi viðbóta og samþættinga sem Selenium býður upp á.
3. **Takmarkaður stuðningur við vafra**: Þótt Playwright nái yfir helstu nútímavafra (Chrome, Safari, Firefox) er stuðningur þess við eldri vafra (t.d. Internet Explorer) ekki jafn öflugur og hjá Selenium.

#### 5.2 **Selenium**

##### **Kostir**:
1. **Lengri saga og þroski**: Selenium hefur verið til lengi og hefur sannað sig. Það er víða notað hjá mörgum teymum og í mörgum greinum, sem hefur leitt til mikils vistkerfis viðbóta, samþættinga og úrræða.
2. **Stuðningur við marga vafra og vettvanga**: Selenium styður **fjölbreytt úrval vafra** og útgáfa, þar á meðal **Internet Explorer**, og er einnig hægt að samþætta ýmsum verkfærum eins og **Docker**, **Selenium Grid** og **skýjaþjónustum** fyrir dreifðar prófanir.
3. **Prófun á farsímum**: Selenium, með samþættingu sinni við **Appium**, er mun öflugra fyrir prófanir á farsímum, bæði Android- og iOS-forritum. Þetta gerir það að betri kosti fyrir verkefni með áherslu á farsíma eða mikla notkun farsíma.
4. **Prófun með mörgum skjám**: Selenium veitir betri stuðning fyrir sviðsmyndir sem fela í sér **marga skjái** eða flókin samskipti í mörgum gluggum.

##### **Gallar**:
1. **Flækjustig**: API Selenium er orðfleira og skýrara. Þótt það geti verið kostur í sumum tilvikum þýðir það meiri kóða til að skrifa og viðhalda, sem getur dregið úr lipurð þróunaraðila — sérstaklega mikilvægt í sprotaumhverfi.
2. **Afköst**: Selenium keyrir almennt hægar en Playwright, einkum í hauslausri stillingu. Þetta gæti haft áhrif á CI/CD-leiðslur, sérstaklega eftir því sem prófum fjölgar.
3. **Prófun gagnvirks viðmóts**: Selenium er ekki jafn liðugt og Playwright við prófun nútímalegra, gagnvirkra vefviðmóta, einkum með myndritum og rauntímauppfærslum gagna. Það krefst meiri uppsetningar og meðhöndlunar til að eiga áreiðanlega við kvikt efni.

### 6. **Samantekt á samanburði**

| Eiginleiki                          | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Auðveld notkun**                   | Styttri setningafræði, innsæislegra fyrir nútímaviðmót | Skýrara, krefst meiri staðlaðs kóða  |
| **Stuðningur við forritunarmál**              | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Prófun gagnvirks viðmóts**        | Framúrskarandi fyrir kvik rauntímaviðmót          | Meðhöndlar einföld viðmót, en orðfleira og flóknara fyrir ríkuleg samskipti |
| **Prófun á skráaupphleðslu**           | Snjallara API fyrir skráaupphleðslur                  | Orðfleira, minna innsæislegt API         |
| **CI/CD-samþætting**             | Auðveld samþætting við GitHub Actions, Jenkins | Sterk samþætting við mörg CI-verkfæri    |
| **Prófun á farsímum**                | Takmörkuð, aðeins hermun                       | Fullur stuðningur í gegnum Appium               |
| **Stuðningur við marga vafra**         | Chromium, WebKit, Firefox                     | Fullur stuðningur við helstu og eldri vafra |
| **Afköst**                   | Hratt, fínstillt fyrir hauslausar prófanir          | Hægara, einkum í hauslausri stillingu       |
| **Prófun með mörgum skjám**         | Takmörkuð                                       | Góður stuðningur við uppsetningar með mörgum skjám    |
| **Samfélag og vistkerfi**       | Vaxandi, góð skjölun                   | Stórt, þroskað, umfangsmikið vistkerfi       |

### 7. **Ákvörðun**

Eftir að hafa íhugað kröfur og málamiðlanir er **Playwright** betri kosturinn fyrir núverandi þarfir okkar. Snjallara API þess fyrir prófanir á staðbundnum skráaupphleðslum, hnitmiðuð setningafræði og sterkur stuðningur við prófun gagnvirks viðmóts gera það að kjörinni passun fyrir lipra þróunarlotu okkar. Sú staðreynd að það styður bæði **TypeScript** og **Python** er mikilvæg fyrir teymið okkar og nútímaleg nálgun rammans við prófanir gerir okkur kleift að skrifa hreinan, viðhaldshæfan kóða.

Þótt **Selenium** sé áfram frábært tól, einkum fyrir prófanir á farsímum, stuðning við eldri vafra og uppsetningar með mörgum skjám, hentar það síður núverandi þörfum okkar. Orðmergð þess, hægari afköst og flóknari meðhöndlun kvikra viðmóta eins og myndrita gera það minna ákjósanlegt fyrir okkar notkunartilvik.

### 8. **Afleiðingar**

- **Tafarlaus aðgerð**: Við munum taka upp **Playwright** fyrir E2E-prófanir okkar, með áherslu á að prófa notendaflæði sem fela í sér nýskráningu, innskráningu, skráaupphleðslur, mælaborð og niðurhal skýrslna.
- **Langtímasjónarmið**: Við munum fylgjast með þróun vistkerfis Playwright. Ef þarfir okkar breytast, einkum varðandi prófanir á farsímum eða stuðning við eldri vafra, gætum við endurskoðað Selenium.
- **Þjálfun og skjölun**: Þróunarteymi þurfa að kynnast API Playwright, einkum til að meðhöndla kvik viðmót og skráaupphleðslur.
- **Flutningur**: Fyrirliggjandi Selenium-próf (ef einhver eru) verða smám saman flutt yfir í Playwright.

### 9. **Framtíðarsjónarmið**

#####
