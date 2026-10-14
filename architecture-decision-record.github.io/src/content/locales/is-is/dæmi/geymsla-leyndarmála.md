# Geymsla leyndarmála

Efnisyfirlit:

* [Samantekt](#samantekt)
  * [Vandamál](#vandamál)
  * [Ákvörðun](#ákvörðun)
  * [Staða](#staða)
* [Nánar](#nánar)
  * [Forsendur](#forsendur)
  * [Takmarkanir](#takmarkanir)
  * [Afstöður](#afstöður)
  * [Röksemd](#röksemd)
  * [Afleiðingar](#afleiðingar)
* [Tengt](#tengt)
  * [Tengdar ákvarðanir](#tengdar-ákvarðanir)
  * [Tengdar kröfur](#tengdar-kröfur)
  * [Tengdar afurðir](#tengdar-afurðir)
  * [Tengdar meginreglur](#tengdar-meginreglur)
* [Athugasemdir](#athugasemdir)
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Samantekt


### Vandamál

Við þurfum að geyma leyndarmál, svo sem lykilorð, einkalykla, auðkenningartákn o.s.frv.

Sum leyndarmálanna eru notendamiðuð. Til dæmis vill þróunaraðili okkar geta notað farsímann sinn til að fletta upp lykilorði að þjónustu.

Sum leyndarmálanna eru kerfismiðuð. Til dæmis þarf samfelld afhendingarleiðsla okkar að geta fundið skilríki fyrir skýjahýsinguna okkar.


### Ákvörðun

Bitwarden fyrir notendamiðuð leyndarmál

Vault by HashiCorp fyrir kerfismiðuð leyndarmál.


### Staða

Ákveðið. Við erum opin fyrir nýjum valkostum þegar þeir koma fram.


## Nánar


### Forsendur

Í þessum tilgangi, og miðað við núverandi stöðu okkar, metum við notendamiðaða þægindi, svo sem nothæf farsímaforrit.

  * Við viljum tryggja skjótan og auðveldan aðgang á ferðinni, til dæmis fyrir þróunaraðila í bakvakt við áreiðanleikaverkfræði kerfa.

  * Við viljum geta deilt sumum leyndarmálum milli valinna einstaklinga, svo sem teymis.

Við reynum ekki að leysa fyrir einn þjónustuveitanda, svo sem að geyma öll leyndarmál eingöngu hjá Amazon, Azure eða Google.

Við viljum ekki ad hoc nálganir eins og „muna það“ eða „skrifa það á miða“ eða „finna sína eigin leið til að geyma það“.

Öryggislíkan okkar í þessum tilgangi sættir sig við að nota virta tilbúna söluaðila (COTS), svo sem SaaS-lykilorðastjórnunartól.


### Takmarkanir

Núna viljum við eitthvað sem er einfalt, þ.e. enga þörf á að skrifa kóða, enga þörf á að setja upp þjóna, enga þörf á að skuldbinda sig mikið, enga þörf á að staðla alla.


### Afstöður

Við skoðuðum:

1. Notendamiðaða tilbúna lykilorðastjóra: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG o.s.frv.

2. Kerfismiðaða tilbúna (COTS) lykilorðastjóra: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Nálganir miðaðar við miðlun: að nota sameiginlegt Google-skjal, sameiginlega Slack-rás, sameiginlega netmöppu o.s.frv.

4. Ad hoc nálganir með lágri tækni, svo sem að muna, skrifa á miða eða treysta því að hver notandi finni sína eigin leið.


### Röksemd

Bitwarden, LastPass, 1Password og Dashlane eru allt tilbúnar viðskiptavörur.

  * Svipaðir eiginleikar fyrir notendur, teymi, stofnanir o.s.frv.

  * Borðtölvugeta fyrir Windows og Mac og farsímagetu fyrir Android og iOS.

  * Vafraviðbætur fyrir Chrome og Firefox, fyrir sjálfvirka útfyllingu eyðublaða o.s.frv.

Bitwarden hefur tvo kosti umfram hin:

  * Bitwarden er opinn hugbúnaður, sem þýðir að öryggið getur verið jafningjarýnt og fyrirtækið nýtur víðtækrar virðingar meðal öryggismiðaðra þróunaraðila.

  * Sögur hugbúnaðarfólks lýsa umtalsverðu vali á Bitwarden umfram hin.

Dæmigerð góð umfjöllun: https://jcs.org/2017/11/17/bitwarden

Dæmigerð atkvæðagreiðslusíða hlið við hlið: https://stackshare.io/stackups/bitwarden-vs-dashlane

Við frestum KeyPass, pass, GPG o.s.frv. því að viðbótarflækjustig fylgir. Allt þetta lítur út eins og fínar lausnir fyrir tæknilega notendur. GPG lítur sérstaklega vel út fyrir tæknilega notendur sem vilja skipanamiðaða getu þvert á kerfi.

Við frestum KMS því að það bindur við einn þjónustuveitanda.

Við veljum Vault fyrir kerfismiðaðar þarfir, því umsagnirnar eru ótrúlega jákvæðar og því HashiCorp hefur framúrskarandi afrekaskrá í hugbúnaði og stuðningi í hæsta gæðaflokki.

Við beitum neitunarvaldi gegn nálgunum sem byggja á miðlun, svo sem í gegnum sameiginleg skjöl, sameiginlegar rásir, sameiginlegar netmöppur o.s.frv. Þær veita ekki þau öryggisgæði sem við viljum.

Við beitum neitunarvaldi gegn ad hoc nálgunum með lágri tækni, því við erum öll sammála um að það sé ekki vegur fram á við til lengri tíma.


### Afleiðingar

Þróunaraðilar gætu þurft að halda utan um leyndarmál á tveimur stöðum: Bitwarden fyrir notendamiðaðan aðgang og Vault fyrir kerfismiðaðan aðgang.


## Tengt


### Tengdar ákvarðanir

Ákvörðunin um hvaða CI/CD-þjón skuli nota verður að fela í sér sönnun á getu til að nálgast leyndarmál.

Við þurfum að ákveða hvernig á að stýra leyndarmálunum, hvað varðar stefnur, snúning, stofnanir o.s.frv.


### Tengdar kröfur

Leyndarmálin munu hafa tengdar kröfur um fylgni, endurskoðun og móttöku/brottför starfsfólks hjá mannauðsdeild.


### Tengdar afurðir

Við væntum þess að við gætum flutt út einhver leyndarmál í umhverfisbreytur.


### Tengdar meginreglur

Auðafturkræft.

Auðsamhliða, þ.e. auðvelt er að nota fjölbreytta lykilorðastjóra.

Ódýrt að prófa, þ.e. ókeypis prufa er í boði og engin skuldbinding.


## Athugasemdir

Matsathugasemdir hér. Athugasemdirnar eru allar opinberar athugasemdir á ýmsum devops-umræðuvettvöngum.


### Vault by HashiCorp

Vault er nákvæmlega það sem þú vilt hér. 

Hentu þó ekki bara Vault í framleiðslu, settu það fyrst upp í prófunarumhverfi, því skjölun HashiCorp getur verið ansi ábótavant þótt vörur þeirra séu stórkostlegar.

Mjög brattur námsferill og ekki léttvægt að setja upp. 

Upphafsuppsetningin er dálítil plága. Það er vel þess virði, og samfélagið mun styðja það nógu vel til að þú komist af.

Hræðileg skjölun en það eru fullt af leiðbeiningum á netinu frá fólki sem hefur sett það upp og ef þú setur nokkrar þeirra saman færðu virka uppsetningu.

Upphafsuppsetning krafðist þess að fikta í helm-chartum þeirra (vault og consul). Þótt tæknilega sé hægt að nota marga aðra bakenda mæli ég alls ekki með því. Bakendinn/consul getur verið agnarsmár ef þú hefur ekki mikið af gögnum til að geyma.

Vendu þig endilega á að nota CLI, því GUI er meira eins og hugmyndaprófun/auglýsingagátt fyrir fyrirtækjaútgáfu þeirra.

Sú staðreynd að þú getur ekki bara „fyllt það upp“ er plága. Til dæmis, ef þú hefur 5 reiti þarftu að bæta handvirkt við hverjum reit fyrir hvern hlut. Svo þetta er ekki þannig að þú skilgreinir fyrirfram reiti fyrir tiltekinn flokk og fyllir þá reiti fyrir alla hluti í þeim flokki, heldur meira eins og „þú býrð til allt í hvert skipti“, sem (að mínu mati) er plága.

Þú gætir líka viljað skoða goldfish sem UI ofan á vault. Gerir það frekar notalegt að fá teymið þitt með. Þeir hafa líka kynningu. 1. Settu upp consul. 2. Settu upp vault sem bendir á consul. 3. Settu upp goldfish sem bendir á vault. 3. Settu upp cron-verk sem keyrir consul snapshot fyrir afrit.



### LastPass

LastPass Teams. Við notum það, hefur sérsniðin sniðmát, ACL, ekkert vantar að mínu mati.

Ég innleiddi LastPass hjá stofnun minni og gef því C+/B-. Stærsta vandamálið undanfarið er skortur á áreiðanleika. Síðustu 90 daga hafa verið margar klukkustundir þar sem hvelfingar voru þvingaðar í ótengda stillingu. Þetta er ekki tilvalið fyrir stofnun mína þar sem við höfum bókstaflega 4.000+ lykilorð geymd í 20+ sameiginlegum möppum. Eins og þú getur ímyndað þér með svo mörg lykilorð eru að minnsta kosti nokkur uppfærð eða bætt við daglega. Við höfum DR-áætlun ef vandamál vara lengur en klukkustund eða tvær: skrifta undirritar og dulkóðar CSV-afrit af hvelfingunni á hverri nóttu sem hægt er að flytja inn í keepass.

LastPass hefur orðið fyrir ótilkynntum truflunum á þjónustu: innskráning „virkar“ en sækir ekki vefsvæði, tilviljanakenndir eiginleikar bilaðir í stjórnborðinu og lyklar ekki rétt sameiginlegir fyrir nýjar sameiginlegar möppur á efsta stigi. Ég er með sérstakan „lyklaýtingar“/afritunarnotanda sem er í hverjum hópi. Venjulega lagar innskráning sem sá notandi öll vandamál með lyklamiðlun en ekki þegar þjónustan er skert þrátt fyrir það sem stöðusíðan segir...

Fyrir samþættingu getur það verið auðvelt ef þú ert með réttar ACL með líkani minnsta forréttinda, t.d. ef notandi hefur lestrar- og skrifheimild og eingöngu lestrarheimild á færslu eða möppu fær hann aðeins eingöngu lestrarheimildir. Því miður eru ACL stofnunar minnar ekki þær bestu, svo ég endaði á að nota JSON-úthlutunar-API og ~500 línur af python vegna þess að háð eðli hundruða ACL okkar passaði ekki vel við líkan minnsta forréttinda. Ég endaði á að sækja allar ACL sem notandi var í og gera eins konar ávirknigöngu.

Ef ACL- eða hópaskipan þín er þegar byggð með líkan minnsta forréttinda í huga mun AD/LDAP-samstillingartólið fyrir Windows virka vel.

Hafðu samband við sölufólk þeirra og það getur útvegað þér lengri Enterprise-prufu. Gakktu úr skugga um að þú skiljir takmarkanir þess til fulls áður en þú tekur af skarið. Við fengum töluvert af vaxtarverkjum en fyrir utan bilanir eða skerðingar á þjónahliðinni hefur þetta gengið ótrúlega snurðulaust.


### Bitwarden

Bitwarden hefur gott tólaúrval í kringum sig (vefviðmót, CLI, farsími, borðtölva). Hægt að hýsa sjálfur og tiltölulega auðvelt í uppsetningu. Nokkuð góð skjölun og tól sem PrivacyTools mælir með.


### EnvKey

https://www.envkey.com/ er SaaS. Mjög auðvelt að útfæra, samþætta og stýra.

Eiginleikar:

  * Verndar API-lykla og skilríki.

  * Heldur uppsetningu samstilltri alls staðar.

  * Snjöll, enda-til-enda dulkóðuð stýring uppsetningar og leyndarmála. 

  * Kemur í veg fyrir óörugga miðlun og dreifingu uppsetningar. 

  * Samþættist á mínútum.

Geta:

  * Stýrðu uppsetningu og aðgangsstigum fyrir öll forrit, umhverfi og teymi á einum stað.

  * Settu upp hvaða þróunar- eða þjónaumhverfi sem er með einni umhverfisbreytu.

Kostir:

  * Góð heimasíða.

  * Skýr verðmætatillaga.

  * Sjónrænt framúrskarandi vefforrit.

  * Frábær sýnigögn, t.d. Algolia, AWS, Datadog, GitHub, Stripe o.s.frv.

  * Ræddi við stofnandann í 30 mínútur um fyrirtækið, viðmótið o.s.frv. Dane hljómar vel upplýstur, heiðarlegur um kosti/galla og raunhæfur samstarfsaðili.

  * Fyrirtækið er í meginatriðum dæmigert Y Combinator fyrirtæki með 1 stofnanda. Safnaði 120.000 dölum í janúar 2018.

  * Áherslan er á að ná fyrirtækjaeiginleikum, einkum að færa sig frá skýjahýsingu EnvKey yfir í annaðhvort á staðnum eða BYOC.

  * Hugsanleg leið fram á við sem byrjar á EnvKey fyrir einfaldleika, og bætir síðar (eða samhliða) við Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant er opin leyndarmálastýringarþjónusta sem veitir notendavæna geymslu og aðgang að leyndarmálum á öruggan hátt, frá þróunaraðilum hjá Lyft.

KMS-auðkenning: Confidant leysir „hænan eða eggið“ vandamál auðkenningar með því að nota AWS KMS og IAM til að leyfa IAM-hlutverkum að búa til örugg auðkenningartákn sem Confidant getur sannreynt. Confidant stýrir einnig KMS-veitingum fyrir IAM-hlutverk þín, sem leyfir IAM-hlutverkum að búa til tákn sem hægt er að nota til auðkenningar milli þjónusta eða til að senda dulkóðuð skilaboð milli þjónusta.

Dulkóðun útgáfustýrðra leyndarmála í hvíld: Confidant geymir leyndarmál á viðbótarhátt (append-only) í DynamoDB og býr til einstakan KMS-gagnalykil fyrir hverja endurskoðun hvers leyndarmáls með Fernet samhverfri auðkenndri dulritun.

Notendavænt vefviðmót til að stýra leyndarmálum: Confidant býður upp á AngularJS-vefviðmót sem gerir notendum kleift að stýra leyndarmálum, vörpun leyndarmála á þjónustur og sögu breytinga á einfaldan hátt.


### Devolutions Password Server

https://server.devolutions.net/

Tryggðu, stýrðu og vaktaðu aðgang að forréttindareikningum og lotum.

Alhliða, mjög örugg lykilorðahvelfing sem leyfir þér að stjórna aðgangi að forréttindareikningum þínum, um leið og hún bætir heildarsýnileika netsins fyrir kerfisstjóra og veitir snurðulausa upplifun fyrir endanotendur.

Eiginleikar: miðlæg lykilorðahvelfing stofnunar, einkahvelfing fyrir einstaka notendur, lykilorðastjóri, innsprautun skilríkja, Active Directory-samþætting, hlutverkamiðuð aðgangsstýring, tveggja þátta auðkenning, tilbúið fyrir fyrirtæki, IP-takmarkanir, stýringargeta, sjálfvirkur lykilorðagjafi, aðgangur í farsímaforriti, lykilorðasaga, aðgangsskýrslur, tölvupóstviðvaranir.

  * styður gagnadulkóðun

  * styður margar auðkenningarleiðir, þar á meðal LDAP, O365 og staðbundna notendur MEÐ stuðningi við MFA frá mörgum uppsprettum

  * margar geymslur/hvelfingar með nákvæmri aðgangsstýringu fyrir mörg teymi

  * nútímalegt vefviðmót

  * einkahvelfingar fyrir skilríki og tengingar fyrir persónuleg skilríki/tengingar

  * farsímaforrit fyrir IOS/Android

  * endurskoðunarskrár fyrir hverja færslu, hver/hvað/hvenær með valfrjálsri spurningu um hvers vegna þeir fá aðgang

  * sérsníðanleg sniðmát (þótt þeir styðji hundruð tengingartegunda innbyggt)

  * fullt af fleiri eiginleikum og Windows/Mac þykkur biðlari (Remote Desktop Manager) sem þú getur samstillt við og eykur möguleikana til muna...tengingar með einum smelli

  * verðlagning er ekki svo slæm - allt að 15 notendur kosta $500 á ári fyrir lykilorðaþjóninn


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Eiginleikar útgáfu á staðnum: 

  * Full stjórn á enda-til-enda öryggiskerfum og innviðum þínum

  * Settu hugbúnaðinn upp í þínu eigin gagnaveri á staðnum eða í eigin einkaskýjatilviki

  * Uppfylltu laga- og reglugerðarskyldur sem krefjast þess að öll gögn og kerfi séu á staðnum

Eiginleikar skýjaútgáfu:

  * Hugbúnaður sem þjónusta (SaaS) leyfir þér að skrá þig og byrja strax

  * Teygjanleg stigstærð eftir því sem þú vex

  * Stýringar og offramboð veitt af Azure með 99,9% SLA um uppitíma

Endurgjöf notenda:

  * Við notuðum þessa vöru áður. Það var svo auðvelt að komast framhjá henni og reglurnar virka aðeins fyrir snjallt fólk. Löt eða heimsk notendur geta auðveldlega klúðrað því á teymissvæði. Verð eru samningsatriði þegar þú talar við þá.

  * Þú getur keyrt það með SQL express og Win 7 vél. 

  * Ódýrt.
