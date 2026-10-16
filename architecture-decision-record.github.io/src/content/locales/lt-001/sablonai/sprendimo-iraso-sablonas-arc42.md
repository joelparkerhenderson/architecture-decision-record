# Sprendimo įrašo šablonas pagal arc42

<https://arc42.org/overview>

## 1. Įvadas ir tikslai

Trumpas reikalavimų ir varomųjų jėgų aprašas, reikalavimų ištrauka (arba santrauka). Trys (daugiausia penki) svarbiausi architektūros kokybės tikslai, turintys didžiausią prioritetą pagrindiniams suinteresuotiesiems asmenims. Svarbiausių suinteresuotųjų asmenų lentelė su jų lūkesčiais architektūros atžvilgiu.

## 1.1 Reikalavimų apžvalga

### Turinys

Trumpas funkcinių reikalavimų ir varomųjų jėgų aprašas, reikalavimų ištrauka (arba santrauka). Nuorodos į (tikimės, esamus) reikalavimų dokumentus, nurodant, kur juos rasti. 

### Motyvacija

Galutinių naudotojų požiūriu sistema kuriama arba keičiama siekiant geriau palaikyti verslo veiklą ir (arba) pagerinti kokybę. 

### Forma

Trumpas tekstinis aprašas, tikriausiai lentelės pavidalo naudojimo atvejų formatu. Jei reikalavimų dokumentai egzistuoja, ši apžvalga turėtų nurodyti šiuos dokumentus.

Šias ištraukas darykite kuo trumpesnes. Subalansuokite šio dokumento skaitomumą su galimu pasikartojimu reikalavimų dokumentų atžvilgiu. 

## 1.2 Kokybės tikslai

### Turinys

Trys (daugiausia penki) svarbiausi architektūros kokybės tikslai, kurių įgyvendinimas
yra pats svarbiausias pagrindiniams suinteresuotiesiems asmenims. Mes tikrai turime omenyje architektūros kokybės tikslus. Nepainiokite jų su projekto tikslais. Jie nebūtinai sutampa. ISO 25010 standartas pateikia gerą galimų dominančių temų apžvalgą.

### Motyvacija

Turėtumėte žinoti svarbiausių suinteresuotųjų asmenų kokybės tikslus, nes
jie darys įtaką esminiams architektūriniams sprendimams. Būtinai būkite labai
konkretūs dėl šių savybių, venkite madingų žodžių. Jei jūs, kaip architektas, nežinote,
kaip bus vertinama jūsų darbo kokybė …

### Forma

Lentelė su svarbiausiais kokybės tikslais ir konkrečiais scenarijais, išdėstyta pagal prioritetus.

## 1.3 Suinteresuotieji asmenys

### Turinys

Aiški sistemos suinteresuotųjų asmenų apžvalga, t. y. visi asmenys, vaidmenys ar organizacijos, kurie

- turėtų žinoti architektūrą

- turi būti įtikinti architektūra

- turi dirbti su architektūra ar kodu

- savo darbui reikalauja architektūros dokumentacijos

- turi priimti sprendimus dėl sistemos ar jos kūrimo

### Motyvacija

Turėtumėte žinoti visas šalis, dalyvaujančias kuriant sistemą arba paveiktas sistemos. Priešingu atveju vėliau kūrimo procese galite sulaukti nemalonių staigmenų. Šie suinteresuotieji asmenys nulemia jūsų darbo ir jo rezultatų apimtį bei detalumo lygį.

### Forma

Lentelė su vaidmenų pavadinimais, asmenų vardais ir jų lūkesčiais architektūros ir jos dokumentacijos atžvilgiu.

## 2. Apribojimai

Viskas, kas riboja komandas priimant projektavimo ir įgyvendinimo sprendimus ar sprendimus dėl susijusių procesų. Kartais gali išeiti už atskirų sistemų ribų ir galioti ištisoms organizacijoms ir įmonėms.

### Turinys

Bet koks reikalavimas, ribojantis programinės įrangos architektų laisvę priimant projektavimo ir įgyvendinimo sprendimus ar sprendimus dėl kūrimo proceso. Šie apribojimai kartais išeina už atskirų sistemų ribų ir galioja ištisoms organizacijoms ir įmonėms.

### Motyvacija

Architektai turėtų tiksliai žinoti, kur jie laisvi priimdami projektavimo sprendimus ir
kur privalo laikytis apribojimų. Su apribojimais visada reikia susitvarkyti;
vis dėlto dėl jų gali būti galima derėtis.

### Forma

Paprastos apribojimų lentelės su paaiškinimais. Prireikus galite jas suskirstyti
į techninius apribojimus, organizacinius ir politinius apribojimus bei konvencijas (pvz., programavimo ar versijavimo gaires, dokumentavimo ar pavadinimų
konvencijas)

## 3. Kontekstas ir apimtis

Atriboja jūsų sistemą nuo jos (išorinių) komunikacijos partnerių (gretimų
sistemų ir naudotojų). Nurodo išorines sąsajas. Rodoma iš verslo /
srities perspektyvos (visada) arba iš techninės perspektyvos (neprivaloma)

### Turinys

Sistemos apimtis ir kontekstas – kaip rodo pavadinimas – atriboja jūsų sistemą (t. y.
jūsų apimtį) nuo visų jos komunikacijos partnerių (gretimų sistemų ir naudotojų,
t. y. jūsų sistemos konteksto). Taip nurodomos išorinės sąsajos.

Jei reikia, atskirkite verslo kontekstą (srities įvestis ir
išvestis) nuo techninio konteksto (kanalai, protokolai, aparatinė įranga).

### Motyvacija

Srities sąsajos ir techninės sąsajos su komunikacijos partneriais yra
vieni svarbiausių jūsų sistemos aspektų. Įsitikinkite, kad juos visiškai
suprantate.

### Forma

- Įvairios konteksto diagramos

- Komunikacijos partnerių ir jų sąsajų sąrašai.

## 3.1 Verslo kontekstas

### Turinys

Visų komunikacijos partnerių (naudotojų, IT sistemų, …) specifikacija su
srities įvesčių ir išvesčių ar sąsajų paaiškinimais. Neprivalomai galite
pridėti srities formatus ar komunikacijos protokolus.

### Motyvacija

Visi suinteresuotieji asmenys turėtų suprasti, kokie duomenys keičiamiesi su sistemos
aplinka.

### Forma

Visų rūšių diagramos, rodančios sistemą kaip juodąją dėžę ir nurodančios srities
sąsajas su komunikacijos partneriais.

Alternatyviai (arba papildomai) galite naudoti lentelę. Lentelės pavadinimas yra
jūsų sistemos pavadinimas, trijuose stulpeliuose pateikiami komunikacijos
partnerio pavadinimas, įvestys ir išvestys.

## 3.2 Techninis kontekstas

### Turinys

Techninės sąsajos (kanalai ir perdavimo terpės), siejančios jūsų sistemą su
jos aplinka. Be to, srities įvesties / išvesties susiejimas su
kanalais, t. y. paaiškinimas, kuri I/O naudoja kurį kanalą.

### Motyvacija

Daugelis suinteresuotųjų asmenų priima architektūrinius sprendimus remdamiesi techninėmis sąsajomis
tarp sistemos ir jos konteksto. Ypač infrastruktūros ar aparatinės įrangos
projektuotojai sprendžia dėl šių techninių sąsajų.

### Forma

Pvz., UML diegimo diagrama, aprašanti kanalus į gretimas sistemas, kartu
su susiejimo lentele, rodančia ryšius tarp kanalų ir
įvesties / išvesties.

## 4. Sprendimo strategija

Pagrindinių sprendimų ir sprendimo strategijų, formuojančių
architektūrą, santrauka. Gali apimti technologiją, aukščiausio lygio dekompoziciją, būdus
svarbiausiems kokybės tikslams pasiekti ir svarbius organizacinius sprendimus.

### Turinys

Trumpa pagrindinių sprendimų ir sprendimo strategijų, formuojančių sistemos architektūrą, santrauka ir paaiškinimas. Tai apima

- technologijų sprendimus

- sprendimus dėl aukščiausio lygio sistemos dekompozicijos, pvz., architektūrinio šablono ar projektavimo šablono naudojimas

- sprendimus, kaip pasiekti pagrindinius kokybės tikslus

- svarbius organizacinius sprendimus, pvz., kūrimo proceso pasirinkimas ar tam tikrų užduočių perdavimas trečiosioms šalims.

### Motyvacija

Šie sprendimai sudaro jūsų architektūros kertinius akmenis. Jie yra pagrindas
daugeliui kitų išsamių sprendimų ar įgyvendinimo taisyklių.

### Forma

Šių pagrindinių sprendimų paaiškinimą darykite trumpą.

Pagrįskite, ką nusprendėte ir kodėl taip nusprendėte, remdamiesi savo
problemos formulavimu, kokybės tikslais ir pagrindiniais apribojimais. Nurodykite išsamesnę informaciją
tolesniuose skyriuose (5 skyrius – struktūrinės detalės, 8 skyrius –
skersiniai konceptai).

Galite naudoti sprendimo būdų sąrašą arba lentelę.

## 5. Statybinių blokų vaizdas

Statinė sistemos dekompozicija, šaltinio kodo abstrakcijos, rodomos kaip
baltųjų dėžių (kuriose yra juodosios dėžės) hierarchija iki tinkamo
detalumo lygio.

### Turinys

Statybinių blokų vaizdas rodo statinę sistemos dekompoziciją į
statybinius blokus (modulius, komponentus, posistemes, klases, sąsajas, paketus,
bibliotekas, karkasus, sluoksnius, skaidinius, pakopas, funkcijas, makrokomandas, operacijas,
duomenų struktūras, …) ir jų priklausomybes (ryšius, asociacijas,
…)

Šis vaizdas yra privalomas kiekvienai architektūros dokumentacijai. Pagal analogiją su
namu tai yra grindų planas.

### Motyvacija

Išlaikykite šaltinio kodo apžvalgą padarydami jo struktūrą suprantamą
per abstrakciją.

Tai leidžia bendrauti su suinteresuotaisiais asmenimis abstrakčiu lygiu
neatskleidžiant įgyvendinimo detalių.

### Forma

Statybinių blokų vaizdas yra hierarchinis juodųjų ir baltųjų
dėžių rinkinys (žr. paveikslą žemiau) ir jų aprašai.

## 5.1 Visos sistemos baltoji dėžė

Čia aprašote visos sistemos dekompoziciją naudodami šį baltosios dėžės šabloną. Jame yra

- apžvalginė diagrama

- dekompozicijos motyvacija

- juodosios dėžės aprašai iš jos sudarančių statybinių blokų. Jiems siūlome alternatyvas:

  - naudokite vieną lentelę trumpai ir pragmatiškai visų sudedamųjų statybinių blokų ir jų sąsajų apžvalgai

  - naudokite statybinių blokų juodosios dėžės aprašų sąrašą pagal juodosios dėžės šabloną (žr. toliau). Priklausomai nuo jūsų pasirinkto įrankio, šis sąrašas gali būti poskyriai (tekstiniuose failuose), polapiai (viki) arba įdėtieji elementai (modeliavimo įrankyje).

  - (neprivaloma:) svarbios sąsajos, kurios nėra paaiškintos statybinio bloko juodosios dėžės šablonuose, bet yra labai svarbios baltajai dėžei suprasti.

Kadangi sąsajoms nurodyti yra tiek daug būdų, joms nepateikiame konkretaus šablono.

Geriausiu atveju pakaks pavyzdžių ar paprastų parašų.

## 5.2 2 lygis

Čia galite nurodyti (kai kurių) 1 lygio statybinių blokų vidinę struktūrą
kaip baltąsias dėžes.

Turite nuspręsti, kurie jūsų sistemos statybiniai blokai yra pakankamai svarbūs, kad
pateisintų tokį išsamų aprašą. Teikite pirmenybę svarbai, o ne išsamumui.
Nurodykite svarbius, netikėtus, rizikingus, sudėtingus ar nepastovius statybinius blokus. Praleiskite
įprastas, paprastas, nuobodžias ar standartizuotas sistemos dalis

### 5.2.1 1 statybinio bloko baltoji dėžė

Nurodo 1 statybinio bloko vidinę struktūrą.

Naudokite baltosios dėžės šabloną (žr. aukščiau).

## 6. Vykdymo vaizdas

Statybinių blokų elgsena kaip scenarijai, apimantys svarbius naudojimo atvejus
ar funkcijas, sąveikas kritinėse išorinėse sąsajose, eksploatavimą ir
administravimą, taip pat klaidų ir išimčių elgseną.

### Turinys

Vykdymo vaizdas aprašo konkrečią sistemos statybinių blokų elgseną ir sąveikas scenarijų pavidalu iš šių sričių:

- svarbūs naudojimo atvejai ar funkcijos: kaip statybiniai blokai juos vykdo?

- sąveikos kritinėse išorinėse sąsajose: kaip statybiniai blokai bendradarbiauja su naudotojais ir gretimomis sistemomis?

- eksploatavimas ir administravimas: paleidimas, startas, sustabdymas

- klaidų ir išimčių scenarijai

Pastaba: pagrindinis galimų scenarijų (sekų, darbo eigų) pasirinkimo kriterijus yra jų architektūrinė svarba. Nesvarbu aprašyti daug scenarijų. Verčiau dokumentuokite reprezentatyvią atranką.

### Motyvacija

Turėtumėte suprasti, kaip jūsų sistemos statybinių blokų (egzemplioriai) atlieka savo darbą ir bendrauja vykdymo metu. Scenarijus daugiausia fiksuosite dokumentacijoje, kad perteiktumėte savo architektūrą suinteresuotiesiems asmenims, kurie mažiau nori ar gali skaityti ir suprasti statinius modelius (statybinių blokų vaizdą, diegimo vaizdą).

### Forma

Yra daug scenarijų aprašymo žymėjimų, pvz.


- sunumeruotas žingsnių sąrašas (natūralia kalba)

- veiklos diagramos arba blokinės schemos

- sekų diagramos

- BPMN arba EPC (įvykių proceso grandinės)

- būsenų mašinos

- ir kt.

## 6.n Vykdymo scenarijus n (1, 2, 3 ir t. t.)

Įterpkite vykdymo diagramą arba tekstinį scenarijaus aprašą.

Įterpkite šioje diagramoje pavaizduotų statybinių blokų egzempliorių sąveikų pastebimų aspektų aprašą.

## 7. Diegimo vaizdas

Techninė infrastruktūra su aplinkomis, kompiuteriais, procesoriais, topologijomis.
(Programinės įrangos) statybinių blokų susiejimas su infrastruktūros elementais.

### Turinys

Diegimo vaizdas aprašo:

- techninę infrastruktūrą, naudojamą jūsų sistemai vykdyti, su infrastruktūros
  elementais, tokiais kaip geografinės vietos, aplinkos, kompiuteriai, procesoriai,
  kanalai ir tinklo topologijos, taip pat kitais infrastruktūros elementais, ir

- (programinės įrangos) statybinių blokų susiejimą su tais infrastruktūros elementais.

Sistemos dažnai vykdomos skirtingose aplinkose, pvz., kūrimo
aplinkoje, testavimo aplinkoje, gamybinėje aplinkoje. Tokiais atvejais turėtumėte
dokumentuoti visas svarbias aplinkas.

Diegimo vaizdą ypač dokumentuokite, kai jūsų programinė įranga vykdoma kaip
paskirstyta sistema su daugiau nei vienu kompiuteriu, procesoriumi, serveriu ar konteineriu
arba kai projektuojate ir konstruojate savo aparatinės įrangos procesorius ir lustus.

Programinės įrangos požiūriu pakanka užfiksuoti tuos
infrastruktūros elementus, kurių reikia statybinių blokų diegimui parodyti.
Aparatinės įrangos architektai gali eiti toliau ir aprašyti infrastruktūrą bet kokiu
jiems reikalingu detalumo lygiu. 

### Motyvacija

Programinė įranga neveikia be aparatinės įrangos. Ši pagrindinė infrastruktūra gali ir
darys įtaką jūsų sistemai ir (arba) kai kuriems skersiniams konceptams. Todėl
turite žinoti infrastruktūrą.

### Forma

Galbūt aukščiausio lygio diegimo diagrama jau yra 3.2 skyriuje kaip techninis kontekstas, kuriame jūsų pačių infrastruktūra yra VIENA juodoji dėžė. Šiame skyriuje šią juodąją dėžę priartinsite naudodami papildomas diegimo diagramas.

- UML siūlo diegimo diagramas šiam vaizdui išreikšti. Naudokite jas, tikriausiai su įdėtosiomis diagramomis, kai jūsų infrastruktūra sudėtingesnė.

- Kai jūsų (aparatinės įrangos) suinteresuotieji asmenys teikia pirmenybę kitokioms diagramoms, o ne
  UML diegimo diagramai, leiskite jiems naudoti bet kokią, galinčią parodyti infrastruktūros
  mazgus ir kanalus.

## 7.1 Infrastruktūra, 1 lygis

Aprašykite (paprastai diagramų, lentelių ir teksto deriniu):

- jūsų sistemos paskirstymą keliose vietose, aplinkose, kompiuteriuose, procesoriuose, .. taip pat fizinius ryšius tarp jų

- svarbų šios diegimo struktūros pagrindimą ar motyvaciją

- infrastruktūros kokybės ir (arba) našumo savybes

- programinės įrangos artefaktų (statybinių blokų) susiejimą su infrastruktūros elementais

Kelioms aplinkoms ar alternatyviems diegimams nukopijuokite šį arc42 skyrių visoms svarbioms aplinkoms. **

## 7.2 Infrastruktūra, 2 lygis

Čia galite pateikti (kai kurių) 1 lygio infrastruktūros elementų vidinę struktūrą.

Nukopijuokite 1 lygio struktūrą kiekvienam pasirinktam elementui.

## 8. Skersiniai konceptai

Bendrosios, pagrindinės taisyklės ir sprendimo būdai, svarbūs keliose
sistemos dalyse (→ skersiniai). Konceptai dažnai susiję su keliais
statybiniais blokais. Apima įvairias temas, tokias kaip srities modeliai, architektūros
šablonai ir stiliai, konkrečių technologijų naudojimo taisyklės ir įgyvendinimo
taisyklės.

### Turinys

Šiame skyriuje aprašomi skersiniai konceptai (praktikos, šablonai, taisyklės
ar sprendimo idėjos). Tokie konceptai dažnai susiję su keliais statybiniais blokais.
Jie gali apimti daug įvairių temų.

### Motyvacija

Konceptai sudaro architektūros konceptualaus vientisumo (nuoseklumo, vienalytiškumo)
pagrindą. Todėl jie yra svarbus indėlis siekiant vidinės jūsų sistemos
kokybės.

Tai šablono vieta, kurią skyrėme nuosekliai tokių konceptų specifikacijai.

Daugelis šių konceptų yra susiję su keliais jūsų statybiniais blokais arba daro jiems įtaką.

### Forma

Forma gali būti įvairi:

- konceptų dokumentai bet kokios struktūros

- pavyzdiniai įgyvendinimai, ypač techniniams konceptams

- skersinių modelių ištraukos arba scenarijai, naudojantys architektūros vaizdų žymėjimus

### Šio skyriaus struktūra

Pasirinkite tik labiausiai jūsų sistemai reikalingas temas ir kiekvienai priskirkite 2 lygio antraštę šiame skyriuje (pvz., 8.1, 8.2 ir t. t.).

- NEBANDYKITE aprėpti visų aukščiau minėtoje diagramoje pateiktų temų.

### Fonas

Kai kurios sistemų temos dažnai susijusios su keliais statybiniais blokais, aparatinės įrangos
elementais ar kūrimo procesais. Gali būti lengviau perteikti ar dokumentuoti
tokias skersines temas centrinėje vietoje, užuot kartojus jas
susijusių statybinių blokų, aparatinės įrangos elementų ar kūrimo procesų
aprašuose.

Tam tikri konceptai gali liesti visus sistemos elementus, kiti gali būti svarbūs tik
keliems.

## 9. Architektūriniai sprendimai

Svarbūs, brangūs, kritiniai, plataus masto ar rizikingi architektūros sprendimai
su pagrindimais.

### Turinys

Svarbūs, brangūs, plataus masto ar rizikingi architektūros sprendimai, įskaitant
pagrindimus. „Sprendimais“ turime omenyje vienos alternatyvos pasirinkimą pagal duotus
kriterijus.

Pasitelkite savo sprendimą, ar architektūrinį sprendimą reikėtų
dokumentuoti čia, šiame centriniame skyriuje, ar geriau dokumentuoti jį
vietoje (pvz., vieno statybinio bloko baltosios dėžės šablone). Venkite
pasikartojančių tekstų. Nurodykite 4 skyrių, kuriame jau užfiksavote svarbiausius
savo architektūros sprendimus.

### Motyvacija

Jūsų sistemos suinteresuotieji asmenys turėtų galėti suprasti ir atsekti jūsų
sprendimus.

### Forma

- ADR (architektūros sprendimo įrašas) kiekvienam svarbiam sprendimui

- sąrašas arba lentelė, išdėstyta pagal svarbą ir pasekmes, arba

- išsamiau atskirais skyriais kiekvienam sprendimui

### Fonas (apie ADR)

Mažesnius dokumentacijos gabalus lengviau skaityti, kurti ir prižiūrėti. Kalbant
apie architektūros sprendimus, kūrimo komandos dažnai:

- žino sprendimą, nes jis matomas, pvz., šaltinio kode, bet

- nežino šio sprendimo motyvacijos (žr. Nygard 2011)

Todėl turėtumėte dokumentuoti keletą svarbių sprendimų kartu su jų motyvacija, argumentacija

### Mūsų pasiūlymas dėl sprendimų

Laikykite architektūriškai reikšmingų sprendimų rinkinį – tų sprendimų,
kurie veikia struktūrą, kokybės charakteristikas, svarbias (ypač išorines)
priklausomybes ir sąsajas arba kūrimo būdus (dėkojame Michael
Nygard už šį pasiūlymą).

## 10. Kokybės reikalavimai

Kokybės reikalavimai kaip scenarijai, su kokybės medžiu aukšto lygio
apžvalgai pateikti. Svarbiausi kokybės tikslai turėjo būti aprašyti
1.2 skyriuje (kokybės tikslai).

### Turinys

Šiame skyriuje pateikti visi svarbūs kokybės reikalavimai.

Svarbiausi iš šių reikalavimų jau aprašyti 1.2 skyriuje
(kokybės tikslai), todėl čia jie turėtų būti tik nurodomi. Šiame
10 skyriuje taip pat turėtumėte užfiksuoti mažiau svarbius kokybės reikalavimus,
kurių visiškai nepasiekus nekils didelės rizikos (bet kurie gali būti
pageidautini).

### Motyvacija

Kadangi kokybės reikalavimai labai paveiks architektūrinius
sprendimus, turėtumėte žinoti, kokios savybės iš tiesų svarbios jūsų
suinteresuotiesiems asmenims, konkrečiai ir išmatuojamai.

### Papildoma informacija

Žr. išsamų Q42 kokybės modelį adresu https://quality.arc42.org.

## 10.1 Kokybės reikalavimų apžvalga

### Turinys

Kokybės reikalavimų apžvalga arba santrauka.

### Motyvacija

Dažnai susiduriame su dešimtimis (ar net šimtais) išsamių kokybės reikalavimų.
Šiame apžvalgos skyriuje turėtumėte stengtis juos apibendrinti, pvz., aprašydami
kategorijas ar temas (kaip siūlo ISO 25010:2023 arba Q42

Jei šie apibendrinantys aprašai jau yra tikslūs, pakankamai konkretūs ir
išmatuojami, 10.2 skyrių galite praleisti.

### Forma

Naudokite paprastą lentelę, kurios kiekvienoje eilutėje pateikiama kategorija ar tema ir trumpas
kokybės reikalavimo aprašas. Alternatyviai galite naudoti minčių žemėlapį
šiems kokybės reikalavimams struktūrizuoti.

Literatūroje taip pat aprašyta kokybės atributų medžio idėja,
kurioje bendras terminas „kokybė“ yra šaknis, o terminas „kokybė“ išskleidžiamas
medžio pavidalu. [Bass+21] šiam tikslui įvedė terminą „Quality
Attribute Utility Tree“.

## 10.2 Kokybės scenarijai

### Turinys

Kokybės scenarijai padaro kokybės reikalavimus konkrečius ir leidžia nuspręsti, ar
jie įvykdyti (priėmimo kriterijų prasme). Užtikrinkite, kad jūsų
scenarijai būtų konkretūs ir išmatuojami.

Ypač naudingi du scenarijų tipai:

- Naudojimo scenarijai (dar vadinami taikomųjų programų scenarijais arba naudojimo atvejų scenarijais)
  aprašo sistemos reakciją vykdymo metu į tam tikrą dirgiklį. Tai apima
  ir scenarijus, aprašančius sistemos efektyvumą ar našumą.
  Pavyzdys: sistema reaguoja į naudotojo užklausą per vieną sekundę.

- Pokyčių scenarijai aprašo pageidaujamą sistemos ar jos artimiausios aplinkos modifikacijos ar išplėtimo
  poveikį. Pavyzdys: įgyvendinama papildoma funkcija arba keičiasi kokybės atributo reikalavimai,
  ir matuojamos pokyčio pastangos ar trukmė.

### Forma

Tipinė išsamių scenarijų informacija apima:

Trumpa forma (teikiama pirmenybė Q42 modelyje):

- Kontekstas / fonas: kokia tai sistema ar komponentas, kokia aplinka ar situacija?

- Šaltinis / dirgiklis: kas arba kas inicijuoja ar sukelia elgseną, reakciją ar veiksmą.

- Metrika / priėmimo kriterijai: atsakas su matu ar metrika

Ilga scenarijų forma (teikiama pirmenybė SEI ir [Bass+21]) yra išsamesnė ir apima šią informaciją:

- Scenarijaus ID: unikalus scenarijaus identifikatorius.

- Scenarijaus pavadinimas: trumpas, aprašomasis scenarijaus pavadinimas.

- Šaltinis: esybė (naudotojas, sistema ar įvykis), inicijuojanti scenarijų.

- Dirgiklis: sukeliantis įvykis ar sąlyga, kurią sistema turi apdoroti.

- Aplinka: veiklos kontekstas ar sąlyga, kuriomis sistema patiria dirgiklį.

- Artefaktas: dirgiklio paveikti statybiniai blokai ar kiti sistemos elementai.

- Atsakas: rezultatas ar elgsena, kurią sistema rodo reaguodama į dirgiklį.

- Atsako matas: kriterijai ar metrika, pagal kuriuos vertinamas sistemos atsakas.

### Taip pat žr.

Nuo 2023 m. sausio arc42 pateikia pragmatišką kokybės modelį, siūlantį
žymėti kokybės reikalavimus grotažymėmis ar žymomis, pvz., #flexible, #efficient,
#usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Rizikos ir techninė skola

Žinomos techninės rizikos arba techninė skola. Kokios galimos problemos egzistuoja sistemoje ar
aplink ją? Dėl ko kūrimo komanda jaučiasi blogai?

### Turinys

Nustatytų techninių rizikų ar techninės skolos sąrašas, išdėstytas pagal prioritetą

### Motyvacija

„Rizikos valdymas yra suaugusiųjų projektų valdymas“ (Tim Lister, Atlantic
Systems Guild.)

Tai turėtų būti jūsų šūkis sistemingai aptinkant ir vertinant architektūros rizikas ir
techninę skolą, kurios prireiks vadovybės suinteresuotiesiems asmenims (pvz., projektų vadovams, produkto savininkams) kaip bendros
rizikos analizės ir priemonių planavimo dalies.

### Forma

Rizikų ir (arba) techninės skolos sąrašas, tikriausiai su siūlomomis priemonėmis
rizikoms sumažinti, sušvelninti ar išvengti arba techninei skolai mažinti.
