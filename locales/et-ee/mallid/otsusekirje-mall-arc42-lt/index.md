# arc42-lt pärit otsusekirje mall

<https://arc42.org/overview>

## 1. Sissejuhatus ja eesmärgid

Nõuded, liikumapanevate jõudude lühikirjeldus, nõuete väljavõte (või kokkuvõte). Arhitektuuri kolm (kuni viis) peamist kvaliteedieesmärki, millel on kõige olulisematele huvirühmadele kõrgeim prioriteet. Oluliste huvirühmade ülevaade nende ootustega arhitektuurile.

## 1.1 Nõuete ülevaade

### Sisu

Funktsionaalsete nõuete lühikirjeldus, liikumapanevad jõud, nõuete väljavõte (või
kokkuvõte). Lingid (loodetavasti olemasolevatele) nõuete dokumentidele
koos teabega, kust neid leida. 

### Motivatsioon

Lõppkasutajate vaatenurgast ehitatakse või muudetakse süsteemi, et
parandada ärilise tegevuse toetamist või tõsta kvaliteeti. 

### Vorming

Lühike tekstikirjeldus, võib-olla tabelina kasutusjuhtudest. Kui
nõuete dokumendid on olemas, peaks see ülevaade viitama neile dokumentidele.

Hoia see väljavõte nii lühike kui võimalik. Kaalu selle dokumendi loetavust
nõuete dokumentidega võimaliku dubleerimise vastu. 

## 1.2 Kvaliteedieesmärgid

### Sisu

Arhitektuuri kolm (kuni viis) peamist kvaliteedieesmärki, mille
täitmine on kõige olulisematele huvirühmadele kõige tähtsam. Me mõtleme tõesti arhitektuuri kvaliteedieesmärke. Ära aja
neid segi projekti eesmärkidega. Need ei ole tingimata identsed. ISO 25010 standard
annab hea ülevaate potentsiaalselt huvipakkuvatest teemadest.

### Motivatsioon

Sa peaksid teadma kõige olulisemate huvirühmade kvaliteedieesmärke, sest need
mõjutavad põhimõttelisi arhitektuuriotsuseid. Ole nende kvaliteetide osas väga
konkreetne ja väldi moesõnu. Kui sa arhitektina ei tea, kuidas sinu töö kvaliteeti
hinnatakse …

### Vorming

Tabel peamiste kvaliteedieesmärkide ja konkreetsete stsenaariumidega prioriteedi järjekorras.

## 1.3 Huvirühmad

### Sisu

Süsteemi huvirühmade selgesõnaline ülevaade, st kõik isikud, rollid või organisatsioonid, kes

- peavad arhitektuuri tundma

- tuleb arhitektuuris veenda

- peavad arhitektuuriga või koodiga töötama

- vajavad arhitektuuridokumentatsiooni oma töö jaoks

- peavad tegema otsuseid süsteemi või selle arenduse kohta

### Motivatsioon

Sa peaksid teadma kõiki osapooli, kes on süsteemi arendusega seotud või seda mõjutavad.
Vastasel juhul võid arendusprotsessi hilisemas etapis kogeda ebameeldivaid üllatusi. Need huvirühmad
määravad sinu töö ulatuse ja detailsustaseme ning selle tulemused.

### Vorming

Tabel rollinimedega, isikunimedega ning nende ootustega arhitektuurile ja
selle dokumentatsioonile.

## 2. Piirangud

Kõik, mis piirab meeskonda disaini- ja teostusotsustes või seotud protsessi otsustes.
Mõnikord kehtivad need terviklikele organisatsioonidele ja ettevõtetele väljaspool üksikuid süsteeme.

### Sisu

Kõik nõuded, mis piiravad tarkvaraarhitekte nende vabaduses disaini-,
teostus- või arendusprotsessi otsustes. Need piirangud kehtivad mõnikord
terviklikele organisatsioonidele ja ettevõtetele väljaspool üksikuid süsteeme.

### Motivatsioon

Arhitektid peaksid täpselt teadma, kus nad on oma disainiotsustes vabad ja
kus peavad nad piiranguid austama. Piiranguid tuleb alati käsitleda,
kuid need võivad olla läbiräägitavad.

### Vorming

Lihtsad tabelid piirangute ja selgitustega. Vajaduse korral võid need
jagada tehnilisteks piiranguteks, organisatsioonilisteks ja poliitilisteks piiranguteks ning
konventsioonideks (nt programmeerimis- või versioonihalduse juhised, dokumenteerimis- või nimetamiskonventsioonid)

## 3. Kontekst ja ulatus

Eraldab sinu süsteemi (välistest) suhtluspartneritest (naabersüsteemid ja kasutajad). Määrab välised
liidesed. Näita seda äri-/valdkonnaperspektiivist (alati) või tehnilisest perspektiivist (valikuline)

### Sisu

Süsteemi ulatus ja kontekst eraldavad, nagu nimi ütleb, sinu süsteemi (st ulatuse) kõigist
suhtluspartneritest (naabersüsteemid ja kasutajad, st süsteemi kontekst). Seeläbi
määravad nad välised liidesed.

Vajaduse korral erista ärikonteksti (valdkonnaspetsiifiline sisend ja väljund) tehnilisest kontekstist (kanalid, protokollid, riistvara).

### Motivatsioon

Valdkonnaliidesed ja tehnilised liidesed suhtluspartneritega kuuluvad
sinu süsteemi kõige kriitilisemate aspektide hulka. Veendu, et mõistad neid täielikult.

### Vorming

Mitu võimalust:

- Erinevad kontekstidiagrammid

- Suhtluspartnerite ja nende liideste loetelud.

## 3.1 Ärikontekst

### Sisu

Kõigi suhtluspartnerite (kasutajad, IT-süsteemid, …) spetsifikatsioon valdkonnaspetsiifilise
sisendi ja väljundi või liideste selgitustega. Soovi korral võid lisada valdkonnaspetsiifilisi vorminguid või suhtlusprotokolle.

### Motivatsioon

Kõik huvirühmad peaksid mõistma süsteemi keskkonda ja seda, milliseid andmeid
vahetatakse.

### Vorming

Igasugused diagrammid, mis näitavad süsteemi mustas kastis ja määravad valdkonnaliidesed
suhtluspartneritega.

Või (lisaks) tabel. Tabeli pealkiri on sinu süsteemi nimi, kolm veergu sisaldavad suhtluspartneri nime,
sisendit ja väljundit.

## 3.2 Tehniline kontekst

### Sisu

Tehnilised liidesed (kanalid ja edastusmeediumid), mis ühendavad süsteemi selle keskkonnaga. Lisaks
valdkonnaspetsiifilise sisendi/väljundi kaardistus kanalitele, st selgitus, milline sisend ja väljund kasutab millist kanalit.

### Motivatsioon

Paljud huvirühmad teevad arhitektuuriotsuseid süsteemi ja
selle konteksti vaheliste tehniliste liideste põhjal. Eriti taristu- või riistvaradisainerid otsustavad need tehnilised liidesed.

### Vorming

Näiteks UML-i kasutuselevõtudiagramm, mis kirjeldab kanaleid naabersüsteemidesse,
koos kaardistustabeliga, mis näitab seoseid kanalite ja sisendite/väljundite vahel.

## 4. Lahendusstrateegia

Arhitektuuri kujundavate põhimõtteliste otsuste ja lahendusstrateegiate kokkuvõte. Võib sisaldada tehnoloogiat, kõrgeima taseme dekompositsiooni,
lähenemisi peamiste kvaliteedieesmärkide saavutamiseks ja asjakohaseid organisatsioonilisi otsuseid.

### Sisu

Lühike kokkuvõte ja selgitus põhimõtetest otsustest ja lahendusstrateegiatest, mis
kujundavad süsteemiarhitektuuri. See hõlmab

- tehnoloogiaotsuseid

- otsuseid süsteemi kõrgeima taseme dekompositsiooni kohta, nt arhitektuurimustrite või disainimustrite kasutamine

- otsuseid selle kohta, kuidas peamised kvaliteedieesmärgid saavutatakse

- asjakohaseid organisatsioonilisi otsuseid, nt arendusprotsessi valimine või teatud ülesannete delegeerimine kolmandatele osapooltele.

### Motivatsioon

Need otsused on sinu arhitektuuri nurgakivid. Need on aluseks paljudele teistele üksikasjalikele
otsustele või teostusreeglitele.

### Vorming

Hoia nende võtmeotsuste selgitus lühike.

Motiveeri, mida otsustasid ja miks nii otsustasid, tuginedes probleemi püstitusele, kvaliteedieesmärkidele ja peamistele
piirangutele. Üksikasjade jaoks vaata järgmisi jaotisi (5. jaotis struktuuriliste üksikasjade, 8. jaotis
funktsioonideüleste küsimuste jaoks).

Võid kasutada lahendusviiside loetelu või tabelit.

## 5. Ehituskivide vaade

Süsteemi staatiline dekompositsioon, lähtekoodi abstraktsioonid, näidatud
valgete kastide (mustade kastidega sees) hierarhiana sobiva detailsustasemeni.

### Sisu

Ehituskivide vaade näitab süsteemi staatilist dekompositsiooni ehituskivideks (moodulid, komponendid, alamsüsteemid, klassid,
liidesed, paketid, teegid, raamistikud, kihid, partitsioonid, tasandid, funktsioonid, makrod, operatsioonid,
andmestruktuurid, …) ja nende sõltuvusteks (seosed, assotsiatsioonid, …)

See vaade on iga arhitektuuridokumentatsiooni jaoks kohustuslik. Maja analoogia põhjal
on see põrandaplaan.

### Motivatsioon

Hoia ülevaadet oma lähtekoodist, muutes struktuuri mõistetavaks
abstraktsiooni abil.

See võimaldab sul huvirühmadega abstraktsel tasandil suhelda, avaldamata
teostuse üksikasju.

### Vorming

Ehituskivide vaade on mustade ja valgete kastide hierarhiline kogum
(vt allolevat joonist) ja nende kirjeldused.

## 5.1 Kogu süsteemi valge kast

Siin kirjeldad kogu süsteemi dekompositsiooni järgmise valge kasti malli abil. See sisaldab

- ülevaatediagrammi

- dekompositsiooni motivatsiooni

- sisalduvate ehituskivide musta kasti kirjeldusi. Selleks on pakutud järgmised alternatiivid:

  - kasuta ühte tabelit kõigi sisalduvate ehituskivide ja nende liideste lühikese ja pragmaatilise ülevaate jaoks

  - kasuta ehituskivide musta kasti kirjelduste loetelu musta kasti malli järgi (vt allpool). Sõltuvalt sinu tööriistast võib see loetelu koosneda alapeatükkidest (tekstifailid), alamlehtedest (wiki) või pesastatud elementidest (modelleerimistööriistad).

  - (valikuline:) olulised liidesed, mida ehituskivi musta kasti mallis ei kirjeldata, kuid mis on valge kasti mõistmiseks väga olulised.

Kuna liideste määramiseks on nii palju viise, ei paku me selleks konkreetset malli.

Parimal juhul piisab näidetest või lihtsatest signatuuridest.

## 5.2 Tase 2

Siin võid määrata 1. taseme (mõne) ehituskivi sisestruktuuri valge kastina.

Sa pead otsustama, millised sinu süsteemi ehituskivid on piisavalt olulised, et õigustada nii üksikasjalikku
kirjeldust. Eelista asjakohasust täielikkusele.
Määra ehituskivid, mis on olulised, üllatavad, riskantsed, keerukad või muutlikud.
Jäta välja oma süsteemi tavalised, lihtsad, igavad või standardiseeritud osad

### 5.2.1 Ehituskivi 1 valge kast

...kirjeldab ehituskivi 1 sisestruktuuri.

Kasuta valge kasti malli (vt eespool).

## 6. Käitusaja vaade

Ehituskivide käitumine stsenaariumidena, mis hõlmavad olulisi kasutusjuhte või funktsioone, vastasmõjusid
kriitilistes välistes liidestes, käitust ja haldust ning vea- ja erandikäitumist.

### Sisu

Käitusaja vaade kirjeldab süsteemi ehituskivide konkreetset käitumist ja vastasmõjusid stsenaariumide kujul järgmistest valdkondadest:

- olulised kasutusjuhud või funktsioonid: kuidas ehituskivid neid täidavad?

- vastasmõjud kriitilistes välistes liidestes: kuidas ehituskivid kasutajate ja naabersüsteemidega koostööd teevad?

- käitus ja haldus: käivitamine, alustamine, peatamine

- vea- ja erandistsenaariumid

Märkus: peamine kriteerium võimalike stsenaariumide (järjestused, töövood) valimisel on nende arhitektuuriline asjakohasus. Suure hulga stsenaariumide kirjeldamine ei ole oluline. Pigem tuleks dokumenteerida esinduslik valik.

### Motivatsioon

Sa peaksid mõistma, kuidas sinu süsteemi ehituskivide (eksemplarid) oma tööd teevad ja käitusajal suhtlevad. Lisad stsenaariumid dokumentatsiooni peamiselt selleks, et edastada oma arhitektuuri huvirühmadele, kes on staatiliste mudelite (ehituskivide vaade, kasutuselevõtuvaade) lugemisel ja mõistmisel vähem aktiivsed või vähem osavad.

### Vorming

Stsenaariumide kirjeldamiseks on palju notatsioone, näiteks


- nummerdatud sammude loend (loomulikus keeles)

- tegevusdiagrammid või vooskeemid

- jadadiagrammid

- BPMN või EPC-d (sündmusprotsessi ahelad)

- olekumasinad

- jne.

## 6.n Käitusaja stsenaarium n (1, 2, 3 jne)

Sisesta käitusaja diagramm või stsenaariumi tekstikirjeldus.

Sisesta selgitus selles diagrammil kujutatud ehituskivide eksemplaride vastasmõjude tähelepanuväärsete aspektide kohta.

## 7. Kasutuselevõtuvaade

Tehniline taristu koos keskkondade, arvutite, protsessorite ja topoloogiatega.
(Tarkvara) ehituskivide kaardistus taristuelementidele.

### Sisu

Kasutuselevõtuvaade kirjeldab:

- tehnilist taristut, mida kasutatakse sinu süsteemi käitamiseks, koos taristuelementidega nagu geograafilised asukohad, keskkonnad, arvutid, protsessorid,
  kanalid ja võrgutopoloogiad ning muud taristuelemendid, ja

- (tarkvara) ehituskivide kaardistust neile taristuelementidele.

Sageli töötavad süsteemid erinevates keskkondades, näiteks arenduskeskkond, testimiskeskkond, tootmiskeskkond. Sellistel juhtudel peaksid
dokumenteerima kõik asjakohased keskkonnad.

Dokumenteeri kasutuselevõtuvaade eriti siis, kui sinu tarkvara töötab hajussüsteemina, mis hõlmab rohkem kui ühte arvutit, protsessorit, serverit või konteinerit, või kui sa disainid ja ehitad oma riistvaraprotsessoreid ja kiipe.

Tarkvara perspektiivist piisab ehituskivide kasutuselevõtu näitamiseks vajalike
taristuelementide jäädvustamisest.
Riistvaraarhitektid võivad minna kaugemale ja kirjeldada taristut mis tahes
detailsustasemel, mida nad vajavad jäädvustada. 

### Motivatsioon

Tarkvara ei tööta ilma riistvarata. See aluseks olev taristu võib ja hakkab mõjutama sinu süsteemi ja/või mõnda
funktsioonideülest kontseptsiooni. Seetõttu pead taristut tundma.

### Vorming

Kõrgeim kasutuselevõtudiagrammide tase on juba lisatud jaotisesse 3.2 tehnilise kontekstina, kus sinu oma
taristu on üks must kast. Selles jaotises suumid sellesse musta kasti täiendavate kasutuselevõtudiagrammidega.

- UML pakub selle vaate väljendamiseks kasutuselevõtudiagramme. Kasuta neid, võib-olla pesastatud diagrammidega,
  kui sinu taristu on keerukam.

- Kui sinu (riistvara) huvirühmad eelistavad UML-i kasutuselevõtudiagrammile mingit muud diagrammi,
  lase neil kasutada mis tahes liiki, mis suudab näidata taristu sõlmi ja kanaleid.

## 7.1 Taristu tase 1

Kirjelda (tavaliselt diagrammide, tabelite ja teksti kombinatsioonis):

- süsteemi jaotust mitmele asukohale, keskkonnale, arvutile, protsessorile jne ning nendevahelisi füüsilisi ühendusi

- selle kasutuselevõtustruktuuri olulist põhjendust või motivatsiooni

- taristu kvaliteedi- ja/või jõudlusomadusi

- tarkvaraartefaktide (ehituskivide) kaardistust taristu elementidele

Mitme keskkonna või alternatiivse kasutuselevõtu korral kopeeri see arc42 jaotis kõigi asjakohaste keskkondade jaoks. **

## 7.2 Taristu tase 2

See võib sisaldada 1. taseme (mõne) taristuelemendi sisestruktuuri.

Kopeeri 1. taseme struktuur iga valitud elemendi jaoks.

## 8. Funktsioonideülesed kontseptsioonid

Üldised, põhimõttelised reeglid ja lahendusviisid, mis on asjakohased sinu süsteemi mitmele
osale (→ funktsioonideülene). Kontseptsioonid on sageli seotud mitme
ehituskiviga. Lisa mitmesuguseid teemasid, nagu valdkonnamudelid, arhitektuurimustrid
ja -stiilid, konkreetse tehnoloogia kasutamise reeglid ja teostusreeglid.

### Sisu

See jaotis kirjeldab funktsioonideüleseid kontseptsioone (tavasid, mustreid, reegleid
või lahendusideid). Sellised kontseptsioonid on sageli seotud mitme ehituskiviga.
Need võivad hõlmata paljusid erinevaid teemasid.

### Motivatsioon

Kontseptsioonid on arhitektuuri kontseptuaalse terviklikkuse (järjepidevus, ühtlus) alus. Seetõttu on
need oluline panus sinu süsteemi sisemisse kvaliteeti.

See on koht, mille oleme mallis loonud selliste kontseptsioonide ühtse spetsifikatsiooni jaoks.

Paljud neist kontseptsioonidest on seotud mitme ehituskiviga või mõjutavad neid.

### Vorming

Vorming võib varieeruda:

- kontseptsioonipaberid mis tahes struktuuriga

- näiteteostused, eriti tehniliste kontseptsioonide jaoks

- funktsioonideülesed mudelite väljavõtted või stsenaariumid arhitektuurivaadete notatsioonidega

### Selle jaotise struktuur

Vali ainult need teemad, mis on sinu süsteemi jaoks kõige vajalikumad, ja anna igaühele selles jaotises 2. taseme pealkiri (nt 8.1, 8.2 jne).

- Ära proovi katta kõiki ülaltoodud diagrammi teemasid.

### Taust

Mõned süsteemisisesed teemad on sageli seotud mitme ehituskivi, riistvara-
elemendi või arendusprotsessiga. Võib olla lihtsam selliseid funktsioonideüleseid teemasid edastada või dokumenteerida ühes keskses
kohas, mitte neid seotud ehituskivide, riistvaraelementide või
arendusprotsesside kirjelduses korrata.

Teatud kontseptsioonid võivad olla asjakohased kõigile süsteemi elementidele, teised vaid mõnele.

## 9. Arhitektuuriotsused

Olulised, kallid, kriitilised, ulatuslikud või riskantsed arhitektuuriotsused koos põhjendustega.

### Sisu

Olulised, kallid, ulatuslikud või riskantsed arhitektuuriotsused koos põhjendustega.
"Otsuste" all mõtleme ühe alternatiivi valimist etteantud kriteeriumide alusel.

Otsusta oma äranägemise järgi, kas dokumenteerida arhitektuuriotsused selles keskses jaotises või eelistad neid
dokumenteerida lokaalselt (nt ehituskivi valge kasti malli sees). Väldi liigset teksti. Vaata jaotist 4, mis juba
sisaldab sinu arhitektuuri kõige olulisemaid otsuseid.

### Motivatsioon

Sinu süsteemi huvirühmad peaksid suutma sinu otsuseid mõista ja
tagasi jälgida.

### Vorming

- ADR-id (arhitektuuriotsuse kirjed) iga olulise otsuse kohta

- loetelu või tabel, järjestatud tähtsuse ja tagajärgede järgi, või

- üksikasjalikum eraldi jaotistena iga otsuse kohta

### Taust (ADR-ide kohta)

Väiksemaid dokumentatsioonitükke on lihtsam lugeda, kirjutada ja hooldada. Arhitektuuriotsuste kohta
teavad arendusmeeskonnad sageli:

- otsust, sest see on näiteks lähtekoodis nähtav, kuid

- puudub selle otsuse taga olev motivatsioon (vt Nygard 2011)

Seetõttu peaksid dokumenteerima mõned olulised otsused koos nende motivatsiooni ja arutluskäiguga

### Meie ettepanek otsuste kohta

Hoia kogumit arhitektuuriliselt olulistest otsustest, st otsustest, mis mõjutavad struktuuri, kvaliteediomadusi, olulisi
(eriti väliseid) sõltuvusi ja liideseid või ehitusmeetodeid (tänu Michael
Nygardile selle ettepaneku eest).

## 10. Kvaliteedinõuded

Kvaliteedinõuded stsenaariumidena, koos kvaliteedipuuga kõrgetasemelise ülevaate andmiseks.
Kõige olulisemad kvaliteedieesmärgid peaksid olema juba kirjeldatud jaotises
1.2 (kvaliteedieesmärgid).

### Sisu

See jaotis sisaldab kõiki asjakohaseid kvaliteedinõudeid.

Kõige olulisemad neist on juba kirjeldatud jaotises
1.2 (kvaliteedieesmärgid), nii et siin peaksid neile ainult viitama. Selles
jaotises 10 peaksid lisama ka vähem olulised kvaliteedinõuded, mis ei tekita suurt riski, kui neid
ei saavutata täielikult (kuid on mõnusad omada).

### Motivatsioon

Kuna kvaliteedinõuded mõjutavad arhitektuuriotsuseid väga, peaksid teadma, milline kvaliteet
on huvirühmadele tõesti oluline, konkreetsel ja mõõdetaval viisil.

### Lisateave

Vaata põhjalikku Q42 kvaliteedimudelit aadressil https://quality.arc42.org.

## 10.1 Kvaliteedinõuete ülevaade

### Sisu

Kvaliteedinõuete ülevaade või kokkuvõte.

### Motivatsioon

Sageli seisad silmitsi kümnete (isegi sadade) üksikasjalike kvaliteedinõuetega.
Selles ülevaatejaotises peaksid proovima neid kokku võtta, näiteks kirjeldades kategooriaid või teemasid (nagu soovitavad ISO 25010:2023 või Q42)

Kui need kokkuvõtlikud kirjeldused on juba täpsed, piisavalt konkreetsed
ja mõõdetavad, võid jaotise 10.2 vahele jätta.

### Vorming

Kasuta lihtsat tabelit, kus igal real on kategooria või teema ja kvaliteedinõude lühikirjeldus.
Või kasuta mõttekaarti nende kvaliteedinõuete struktureerimiseks.

Kirjanduses kirjeldatakse ka kvaliteediatribuudi puude ideed, mille juureks on üldine termin "kvaliteet" ja
mis täpsustavad terminit "kvaliteet" puustruktuuris.
[Bass+21] võttis selleks otstarbeks kasutusele termini "Quality
Attribute Utility Tree".

## 10.2 Kvaliteedistsenaariumid

### Sisu

Kvaliteedistsenaariumid muudavad kvaliteedinõuded konkreetseks ja võimaldavad otsustada, kas need
(vastuvõtukriteeriumide tähenduses) on täidetud. Veendu, et stsenaariumid on
konkreetsed ja mõõdetavad.

Eriti kasulikud on kaht liiki stsenaariumid:

- Kasutusstsenaariumid (nimetatakse ka rakendusstsenaariumideks või kasutusjuhu stsenaariumideks) kirjeldavad süsteemi käitusaja reaktsiooni
  teatud stiimulile. See hõlmab ka stsenaariume, mis kirjeldavad süsteemi tõhusust või
  jõudlust.
  Näide: süsteem reageerib kasutaja päringule ühe sekundi jooksul.

- Muutmisstsenaariumid kirjeldavad süsteemi või selle vahetu keskkonna muutmise või laiendamise soovitud mõju.
  Näide: teostatakse täiendav funktsioon või muutuvad nõuded
  kvaliteediatribuudile ning mõõdetakse muudatuse pingutust või kestust.

### Vorming

Tüüpiline teave üksikasjalikes stsenaariumides hõlmab:

Lühike vorm (eelistatud Q42 mudelis):

- Kontekst/taust: mis liiki süsteem või komponent ning milline on keskkond või olukord?

- Allikas/stiimul: kes või mis tegevuse, reaktsiooni või käitumise algatab või käivitab.

- Mõõdik/vastuvõtukriteerium: vastus, sealhulgas skaala või mõõdik

Stsenaariumide pikk vorm (eelistatud SEI ja [Bass+21] poolt) on üksikasjalikum ja sisaldab järgmist teavet:

- Stsenaariumi ID: stsenaariumi unikaalne identifikaator.

- Stsenaariumi nimi: stsenaariumi lühike, kirjeldav nimi.

- Allikas: olem (kasutaja, süsteem või sündmus), mis stsenaariumi algatab.

- Stiimul: käivitav sündmus või tingimus, millele süsteem peab reageerima.

- Keskkond: operatiivne kontekst või tingimused, milles süsteem stiimulit kogeb.

- Artefakt: süsteemi ehituskivi või muu element, mida stiimul mõjutab.

- Vastus: tulemus või käitumine, mida süsteem stiimulile reageerides üles näitab.

- Vastuse mõõt: kriteerium või mõõdik, mille alusel süsteemi vastust hinnatakse.

### Vaata ka

Alates 2023. aasta jaanuarist pakub arc42 pragmaatilist kvaliteedimudelit, mis soovitab kvaliteedinõudeid sildistada
räsimärkide või siltidega nagu
#flexible, #efficient, #usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Riskid ja tehniline võlg

Teadaolevad tehnilised riskid või tehniline võlg. Millised potentsiaalsed probleemid on süsteemis või selle ümber?
Millega arendusmeeskond maadleb?

### Sisu

Tuvastatud tehniliste riskide või tehnilise võla prioriseeritud loetelu

### Motivatsioon

"Riskijuhtimine on täiskasvanute projektijuhtimine" (Tim Lister, Atlantic
Systems Guild.)

See peaks olema sinu motoks arhitektuuri riskide ja tehnilise võla süstemaatilisel avastamisel ja hindamisel,
mida juhtimishuvirühmad (nt projektijuhid, tooteomanikud) vajavad üldise riskianalüüsi ja meetmete planeerimise osana.

### Vorming

Riskide ja/või tehnilise võla loetelu, võib-olla koos pakutud meetmetega
riskide minimeerimiseks, leevendamiseks või vältimiseks või tehnilise võla vähendamiseks.

