# Paslapčių saugojimas

Turinys:

* [Santrauka](#santrauka)
  * [Problema](#problema)
  * [Sprendimas](#sprendimas)
  * [Būsena](#būsena)
* [Detalės](#detalės)
  * [Prielaidos](#prielaidos)
  * [Apribojimai](#apribojimai)
  * [Pozicijos](#pozicijos)
  * [Argumentas](#argumentas)
  * [Implikacijos](#implikacijos)
* [Susiję](#susiję)
  * [Susiję sprendimai](#susiję-sprendimai)
  * [Susiję reikalavimai](#susiję-reikalavimai)
  * [Susiję artefaktai](#susiję-artefaktai)
  * [Susiję principai](#susiję-principai)
* [Pastabos](#pastabos)
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Santrauka


### Problema

Turime saugoti paslaptis, tokias kaip slaptažodžiai, privatieji raktai, autentifikavimo žetonai ir pan.

Kai kurios paslaptys yra orientuotos į naudotoją. Pavyzdžiui, mūsų programuotojas nori galėti naudodamas mobilųjį telefoną susirasti paslaugos slaptažodį.

Kai kurios paslaptys yra orientuotos į sistemą. Pavyzdžiui, mūsų nuolatinio pristatymo konvejeris turi galėti susirasti mūsų debesijos talpinimo prisijungimo duomenis.


### Sprendimas

Bitwarden naudotojams skirtoms paslaptims

Vault by HashiCorp sistemoms skirtoms paslaptims.


### Būsena

Nuspręsta. Atviri naujoms alternatyvoms, kai jos atsiras.


## Detalės


### Prielaidos

Šiam tikslui ir mūsų dabartinei būsenai vertiname patogumą naudotojui, pavyzdžiui, tinkamas naudoti mobiliąsias programas.

  * Norime užtikrinti greitą ir lengvą prieigą keliaujant, pavyzdžiui, programuotojui, atliekančiam budinčią sistemų patikimumo inžineriją.

  * Norime galėti dalytis kai kuriomis paslaptimis su pasirinktais žmonėmis, pavyzdžiui, komanda.

Nesistengiame spręsti vieno teikėjo atvejo, pavyzdžiui, visų paslapčių saugojimo išimtinai Amazon, Azure ar Google.

Nenorime ad hoc požiūrių, tokių kaip „prisimink“, „užsirašyk ant lapelio“ ar „sugalvok savo būdą saugoti“.

Mūsų saugumo modelis šiam tikslui tinka naudoti gerbiamus COTS tiekėjus, tokius kaip SaaS slaptažodžių valdymo įrankiai.


### Apribojimai

Šiuo metu norime kažko paprasto, t. y. nereikia rašyti kodo, nereikia diegti serverių, nereikia imtis didelio įsipareigojimo, nereikia visų standartizuoti.


### Pozicijos

Svarstėme:

1. Naudotojams skirtus paruoštus slaptažodžių tvarkykles: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG ir kt.

2. Sistemoms skirtus COTS slaptažodžių tvarkykles: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Dalijimuisi skirtus požiūrius: bendrai naudojamo Google dokumento, bendro Slack kanalo ar bendro tinklo aplanko ir pan. naudojimą.

4. Žemųjų technologijų ad hoc požiūrius, tokius kaip prisiminimas, užrašo rašymas ar pasikliovimas tuo, kad kiekvienas naudotojas pats sugalvos savo būdą.


### Argumentas

Bitwarden, LastPass, 1Password ir Dashlane visi yra komerciniai paruošti produktai.

  * Panašios funkcijos naudotojams, komandoms, organizacijoms ir pan.

  * Darbalaukio galimybės „Windows“ ir „Mac“ sistemoms, mobiliosios galimybės „Android“ ir „iOS“ sistemoms.

  * Naršyklių plėtiniai „Chrome“ ir „Firefox“, skirti automatiniam formų užpildymui ir pan.

Bitwarden turi du pranašumus prieš kitus:

  * Bitwarden yra atvirojo kodo, o tai reiškia, kad saugumą gali peržiūrėti kolegos, ir įmonę plačiai vertina į saugumą orientuoti programuotojai.

  * Programinės įrangos darbuotojų anekdotai apibūdina didelę pirmenybę Bitwarden, palyginti su kitais.

Tipinis geras aprašymo pavyzdys: https://jcs.org/2017/11/17/bitwarden

Tipinė šalia vienas kito balsavimo svetainė: https://stackshare.io/stackups/bitwarden-vs-dashlane

KeyPass, pass, GPG ir kt. atidedame, nes yra papildomo sudėtingumo. Visi jie atrodo kaip geri sprendimai techniniams naudotojams. GPG atrodo ypač gerai techniniams naudotojams, norintiems tarpsisteminių komandomis grįstų galimybių.

KMS atidedame, nes jis susieja su vienu teikėju.

Sistemoms skirtiems poreikiams renkamės Vault, nes atsiliepimai nuostabiai teigiami, ir nes HashiCorp turi puikią aukščiausios kokybės programinės įrangos ir palaikymo istoriją.

Atmetame dalijimosi požiūrius, pavyzdžiui, per bendrus dokumentus, bendrus kanalus, bendrus tinklo aplankus ir pan. Jie nesuteikia saugumo savybių, kurių norime.

Atmetame ad hoc žemųjų technologijų požiūrius, nes visi sutinkame, kad tai nėra ilgalaikis kelias į priekį.


### Implikacijos

Programuotojams gali tekti sekti paslaptis dviejose vietose: Bitwarden naudotojams skirtai prieigai ir Vault sistemoms skirtai prieigai.


## Susiję


### Susiję sprendimai

Sprendime, kurį CI/CD serverį naudoti, turi būti įtrauktas gebėjimo pasiekti paslaptis įrodymas.

Turėsime nuspręsti, kaip valdyti paslaptis politikų, rotacijų, organizacijų ir pan. požiūriu.


### Susiję reikalavimai

Paslaptys turės susijusių atitikties, audito ir HR įdarbinimo / atleidimo reikalavimų.


### Susiję artefaktai

Tikimės, kad kai kurias paslaptis galime eksportuoti į aplinkos kintamuosius.


### Susiję principai

Lengvai atšaukiama.

Lengvai lygiagretu, t. y. lengva naudoti įvairias slaptažodžių tvarkykles.

Pigu išbandyti, t. y. yra nemokamas bandomasis laikotarpis ir jokio įsipareigojimo.


## Pastabos

Čia vertinimo pastabos. Pastabos yra viešieji komentarai įvairiose devops diskusijų lentose.


### Vault by HashiCorp

Vault yra būtent tai, ko čia reikia. 

Tačiau nemeskite Vault tiesiai į gamybą, pirmiausia paleiskite jį testavimo aplinkoje, nes HashiCorp dokumentacija gali būti gana skurdi, net jei jų produktai nuostabūs.

Labai stati mokymosi kreivė, ir paleisti nėra paprasta. 

Pradinė sąranka šiek tiek vargina. Tačiau tai tikrai verta, ir bendruomenė pakankamai gerai jį palaiko, kad išsiverstumėte.

Siaubinga dokumentacija, bet internete yra daug vadovų, kuriuose žmonės jį nustato, ir jei sudėsite kelis iš jų, turėsite veikiančią sąranką.

Pradinė sąranka reikalavo patrafaretuoti su jų helm diagramomis (vault ir consul). Nors techniškai galite naudoti daugybę kitų galinių dalių (back-end), labai labai nerekomenduoju. Galinė dalis / consul gali būti visiškai maža, jei neturite daug duomenų saugoti.

Būtinai priprasti / susipažinkite su CLI naudojimu, nes GUI labiau panaši į koncepcijos įrodymą / reklaminį portalą jų įmonių leidimui.

Tai, kad negalima tiesiog „užpildyti“, yra vargas. Pavyzdžiui, jei turite 5 laukus, turite rankiniu būdu pridėti kiekvieną lauką kiekvienam elementui. Taigi tai ne taip, kad iš anksto apibrėžiate tam tikros kategorijos laukus ir užpildote tuos laukus visiems tos kategorijos elementams, o labiau „kiekvieną kartą viską generuojate“, o tai (mano nuomone) yra vargas.

Taip pat galbūt norėsite pažiūrėti į goldfish kaip UI virš vault. Padeda gana gražiai įtraukti komandą. Jie taip pat turi demonstraciją. 1. Nustatykite consul. 2. Nustatykite vault, nukreiptą į consul. 3. Nustatykite goldfish, nukreiptą į vault. 3. Nustatykite kokią nors cron užduotį, kuri vykdytų consul snapshot atsarginėms kopijoms.



### LastPass

LastPass Teams. Naudojame, turi pasirinktinius šablonus, ACL, mano nuomone, nieko netrūksta.

Įdiegiau LastPass savo organizacijoje ir vertinu C+/B-. Didžiausia pastarojo meto problema – patikimumo trūkumas. Per pastarąsias 90 dienų buvo kelios valandos, kai saugyklos (vaults) buvo priverstos pereiti į neprisijungimo režimą. Mano organizacijai tai nėra idealu, nes joje saugoma, tiesiogine prasme, 4 000+ slaptažodžių 20+ bendrų aplankų. Kaip galite įsivaizduoti, turint tiek slaptažodžių, bent keletas atnaujinami ar pridedami kasdien. Turime avarinio atkūrimo planą, jei problemos trunka ilgiau nei valandą ar dvi: scenarijus kiekvieną naktį pasirašo ir užšifruoja saugyklos CSV iškrovą, kurią galima importuoti į keepass.

LastPass turėjo nepraneštų trumpalaikių paslaugos pablogėjimų: prisijungimas „veikia“, bet nepatraukia svetainių, kai kurios funkcijos administravimo skydelyje neveikia, ir netinkamai dalijamasi raktais naujiems aukščiausio lygio bendriems aplankams. Turiu specialų „raktų stūmimo“ / atsarginių kopijų naudotoją, esantį kiekvienoje grupėje. Paprastai prisijungus kaip tas naudotojas išsprendžiamos bet kokios raktų dalijimosi problemos, bet ne tada, kai paslauga pablogėjusi, nepaisant to, ką sako būsenos puslapis...

Integracija gali būti lengva, jei turite tinkamus ACL su mažiausių privilegijų modeliu, pvz., jei naudotojas turi ir skaitymo bei rašymo, ir tik skaitymo teises į įrašą ar aplanką, jis gauna tik skaitymo teises. Deja, mano organizacijos ACL nėra geriausi, todėl galiausiai naudojau JSON aprūpinimo API ir ~500 python eilučių, nes mūsų šimtų ACL priklausomas pobūdis netinkamai atitinka mažiausių privilegijų modelį. Galiausiai gaudavau visus ACL, kuriuose yra naudotojas, ir atlikdavau tam tikrą priklausomybių perėjimą.

Jei jūsų ACL ar grupių struktūra jau sukurta atsižvelgiant į mažiausių privilegijų struktūrą, „Windows“ AD/LDAP sinchronizavimo įrankis veiks gerai.

Susisiekite su jų pardavimų komanda, ir jie gali suteikti ilgesnį Enterprise bandomąjį laikotarpį. Būtinai visiškai supraskite jo apribojimus prieš apsispręsdami. Turėjome nemažai augimo skausmų, bet, išskyrus serverio pusės sutrikimus ar pablogėjimus, viskas buvo neįtikėtinai sklandu.


### Bitwarden

Bitwarden turi gerus įrankius aplink save (WebUI, CLI, mobilusis, darbalaukio). Savarankiškai talpinamas ir gana lengvai nustatomas. Gana gera dokumentacija ir PrivacyTools rekomenduojamas įrankis.


### EnvKey

https://www.envkey.com/ yra saas. Tikrai lengva įdiegti, integruoti ir valdyti.

Funkcijos:

  * Apsaugo API raktus ir prisijungimo duomenis.

  * Visur sinchronizuoja konfigūraciją.

  * Išmanus, visapusiškai užšifruotas konfigūracijos ir paslapčių valdymas. 

  * Neleidžia nesaugiai dalytis ir konfigūracijos plitimo. 

  * Integruojama per kelias minutes.

Galimybės:

  * Valdykite visų savo programų, aplinkų ir komandų konfigūraciją ir prieigos lygius vienoje vietoje.

  * Sukonfigūruokite bet kurią kūrimo ar serverio aplinką tik vienu aplinkos kintamuoju.

Privalumai:

  * Gera pagrindinė svetainė.

  * Aiškus vertės pasiūlymas.

  * Vizualiai puiki interneto programa.

  * Puikūs pavyzdiniai duomenys, pvz., Algolia, AWS, Datadog, GitHub, Stripe ir kt.

  * Kalbėjausi su įkūrėju 30 min. apie įmonę, UI ir pan. Dane atrodo gerai informuotas, sąžiningas dėl privalumų / trūkumų ir gyvybingas partneris.

  * Įmonė iš esmės yra tipinė Y Combinator įmonė su 1 įkūrėju. 2018 m. sausį pritraukė 120 tūkst. USD.

  * Dėmesys skiriamas pasiekti įmonių funkcijas, ypač pereinant nuo EnvKey debesijos talpinimo prie vietinio (on-prem) arba BYOC.

  * Galimas kelias į priekį: pradėti nuo EnvKey dėl paprastumo, vėliau (ar lygiagrečiai) pridėti Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant yra atvirojo kodo paslapčių valdymo paslauga, suteikianti patogų naudotojui paslapčių saugojimą ir prieigą prie jų saugiu būdu, nuo Lyft programuotojų.

KMS autentifikavimas: Confidant išsprendžia autentifikavimo vištos ir kiaušinio problemą naudodamas AWS KMS ir IAM, kad IAM vaidmenys galėtų generuoti saugius autentifikavimo žetonus, kuriuos Confidant gali patikrinti. Confidant taip pat valdo jūsų IAM vaidmenų KMS suteikimus (angl. grants), leidžiančius IAM vaidmenims generuoti žetonus, kuriuos galima naudoti paslaugų tarpusavio autentifikavimui arba užšifruotiems pranešimams perduoti tarp paslaugų.

Versijuotų paslapčių šifravimas ramybės būsenoje: Confidant saugo paslaptis DynamoDB tik pridedamu būdu, generuodamas unikalų KMS duomenų raktą kiekvienai kiekvienos paslapties versijai, naudodamas Fernet simetrinę autentifikuotą kriptografiją.

Naudotojui patogi interneto sąsaja paslaptims valdyti: Confidant suteikia AngularJS interneto sąsają, leidžiančią galutiniams naudotojams lengvai valdyti paslaptis, paslapčių susiejimą su paslaugomis ir pakeitimų istoriją.


### Devolutions Password Server

https://server.devolutions.net/

Apsaugokite, valdykite ir stebėkite prieigą prie privilegijuotų paskyrų ir seansų.

Išsami, labai apsaugota slaptažodžių saugykla, leidžianti kontroliuoti prieigą prie jūsų privilegijuotų paskyrų, kartu gerinant bendrą tinklo matomumą sistemų administratoriams ir suteikiant sklandžią patirtį galutiniams naudotojams.

Funkcijos: centralizuota organizacijos slaptažodžių saugykla, naudotojui specifinė privati saugykla, slaptažodžių tvarkyklė, prisijungimo duomenų įterpimas,
Active Directory integracija, vaidmenimis grindžiama prieigos kontrolė, dviejų veiksnių autentifikavimas, paruošta įmonėms, IP apribojimai, valdymo galimybės, automatinis slaptažodžių generatorius, prieiga per mobiliąją programą, slaptažodžių istorija, prieigos ataskaitos, el. pašto įspėjimai.

  * palaiko duomenų šifravimą

  * palaiko kelias autentifikavimo schemas, įskaitant LDAP, O365 ir vietinius naudotojus SU MFA palaikymu iš kelių šaltinių

  * kelios saugyklos su smulkiai sureguliuota prieigos kontrole keliomis komandoms

  * modernioji interneto sąsaja

  * privačios prisijungimo duomenų ir ryšių saugyklos asmeniniams prisijungimo duomenims / ryšiams

  * mobiliosios programos „iOS“ / „Android“

  * audito žurnalai kiekvienam įrašui, kas / ką / kada, su pasirenkamu klausimu, kodėl prieinama

  * pritaikomi šablonai (nors jie savaime palaiko šimtus ryšių tipų)

  * daugybė kitų funkcijų ir „Windows“ / „Mac“ storasis klientas (Remote Desktop Manager), su kuriuo galite sinchronizuoti, ir kuris labai išplečia galimybes... vieno paspaudimo ryšiai

  * kaina nėra tokia bloga – iki 15 naudotojų slaptažodžių serveris kainuoja 500 USD per metus


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Vietinės (on-premise) versijos funkcijos: 

  * Visiška kontrolė jūsų visapusiškoms saugumo sistemoms ir infrastruktūrai

  * Diegkite programinę įrangą savo vietiniame duomenų centre arba savo virtualiojo privačiojo debesies egzemplioriuje

  * Atitikite teisinius ir reguliacinius įsipareigojimus, reikalaujančius, kad visi duomenys ir sistemos būtų vietoje

Debesijos versijos funkcijos:

  * Programinės įrangos kaip paslaugos modelis leidžia užsiregistruoti ir pradėti iš karto

  * Elastingas mastelio keitimas augant

  * Kontrolė ir pertekliškumas, užtikrinami Azure su 99,9 % veikimo SLA

Naudotojų atsiliepimai:

  * Anksčiau naudojome tą produktą. Jį taip lengvai buvo galima apeiti, o taisyklės veikia tik protingiems žmonėms. Tingūs ar kvaili naudotojai gali lengvai viską sugadinti komandos srityje. Kainos yra derybinės, kai su jais kalbate.

  * Galite jį paleisti naudodami SQL express ir Win 7 kompiuterį. 

  * Pigu.
