# AWS architektūros sprendimų įrašų procesas

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Architektūros sprendimo įrašas (ADR) yra dokumentas, aprašantis pasirinkimą, kurį komanda padaro dėl reikšmingo programinės įrangos architektūros, kurią planuoja sukurti, aspekto. Kiekvienas ADR aprašo architektūrinį sprendimą, jo kontekstą ir pasekmes. ADR turi būsenas, todėl jiems būdingas gyvavimo ciklas. ADR pavyzdį rasite priede.

ADR proceso rezultatas yra architektūros sprendimų įrašų rinkinys. Šis rinkinys sudaro sprendimų žurnalą. Sprendimų žurnalas pateikia projekto kontekstą ir išsamią įgyvendinimo bei projektavimo informaciją. Projekto nariai peržvelgia kiekvieno ADR antraštes, kad susidarytų projekto konteksto vaizdą. Jie skaito ADR, kad giliai suprastų projekto įgyvendinimą ir projektavimo pasirinkimus.

Kai komanda priima ADR, jis tampa nekeičiamas. Jei dėl naujų įžvalgų reikia kitokio sprendimo, komanda pasiūlo naują ADR. Kai komanda priima naują ADR, jis pakeičia ankstesnįjį ADR.

## ADR proceso apimtis

Projekto nariai turėtų sukurti ADR kiekvienam architektūriškai reikšmingam sprendimui, darančiam poveikį programinės įrangos projektui ar produktui, įskaitant šiuos (Richards ir Ford 2020):

* Struktūra (pavyzdžiui, šablonai, tokie kaip mikropaslaugos)

* Nefunkciniai reikalavimai (saugumas, aukštas prieinamumas ir atsparumas gedimams)

* Priklausomybės (komponentų tarpusavio susiejimas)

* Sąsajos (API ir paskelbtos sutartys)

* Kūrimo būdai (bibliotekos, karkasai, įrankiai ir procesai)

* Funkciniai ir nefunkciniai reikalavimai yra dažniausi ADR proceso įvesties duomenys.


## ADR turinys

Kai komanda nustato, kad reikia ADR, komandos narys pradeda rašyti ADR pagal viso projekto šabloną. (Pavyzdinių šablonų ieškokite ADR GitHub organizacijoje.) Šablonas supaprastina ADR kūrimą ir užtikrina, kad ADR užfiksuotų visą reikiamą informaciją. Bent jau kiekvienas ADR turėtų apibrėžti sprendimo kontekstą, patį sprendimą ir sprendimo pasekmes projektui ir jo rezultatams. (Šių skyrių pavyzdžių žr. priede.) Vienas galingiausių ADR struktūros aspektų yra tai, kad ji sutelkia dėmesį į sprendimo priežastį, o ne į tai, kaip komanda jį įgyvendino. Supratimas, kodėl komanda priėmė sprendimą, kitiems komandos nariams palengvina jį perimti ir neleidžia kitiems architektams, nedalyvavusiems sprendimų priėmimo procese, ateityje to sprendimo atmesti.


## ADR priėmimo procesas

Kiekvienas komandos narys gali sukurti ADR, tačiau komanda turėtų nustatyti ADR nuosavybės apibrėžtį. Kiekvienas autorius, kuris yra ADR savininkas, turėtų aktyviai prižiūrėti ir skelbti ADR turinį. Siekiant paaiškinti šią nuosavybę, šiame vadove tolesniuose skyriuose ADR autoriai vadinami ADR savininkais. Kiti komandos nariai visada gali prisidėti prie ADR. Jei ADR turinys pasikeičia, kol komanda dar nėra jo priėmusi, savininkas turėtų patvirtinti šiuos pakeitimus.

Kai komanda nustato architektūrinį sprendimą ir jo savininką, ADR savininkas proceso pradžioje pateikia ADR **Pasiūlytas** (angl. Proposed) būsenoje. Pasiūlytos būsenos ADR yra paruošti peržiūrai.

Tada ADR savininkas pradeda ADR peržiūros procesą. ADR peržiūros proceso tikslas – nuspręsti, ar komanda priima ADR, ar nustato, kad jį reikia perdirbti, ar jį atmeta. ADR peržiūri projekto komanda, įskaitant savininką. Peržiūros susitikimas turėtų prasidėti nustatytu laiku ADR perskaityti. Vidutiniškai pakanka 10–15 minučių. Per šį laiką kiekvienas komandos narys perskaito dokumentą ir prideda komentarų bei klausimų neaiškioms temoms pažymėti. Po peržiūros fazės ADR savininkas perskaito ir aptaria kiekvieną komentarą su komanda.

Jei komanda randa veiksmų punktų ADR pagerinti, ADR būsena lieka **Pasiūlytas**. ADR savininkas suformuluoja veiksmus ir kartu su komanda prie kiekvieno veiksmo priskiria vykdytoją. Kiekvienas komandos narys gali prisidėti prie veiksmų punktų ir juos išspręsti. ADR savininko atsakomybė – iš naujo suplanuoti peržiūros procesą.

Komanda taip pat gali nuspręsti ADR atmesti. Tokiu atveju ADR savininkas prideda atmetimo priežastį, kad ateityje būtų išvengta diskusijų ta pačia tema. Savininkas pakeičia ADR būseną į **Atmestas** (angl. Rejected).

Jei komanda ADR patvirtina, savininkas prideda laiko žymą, versiją ir suinteresuotųjų asmenų sąrašą. Tada savininkas atnaujina būseną į **Priimtas** (angl. Accepted).

ADR ir jų sukurtas sprendimų žurnalas atspindi komandos priimtus sprendimus ir pateikia visų sprendimų istoriją. Komanda ADR kaip nuorodą naudoja kodo ir architektūros peržiūrų metu, kai tik įmanoma. Be kodo peržiūrų, projektavimo ir įgyvendinimo užduočių vykdymo, komandos nariai turėtų peržiūrėti ADR dėl strateginių produkto sprendimų.

Gera praktika yra tai, kad kiekvienas programinės įrangos pakeitimas turėtų būti peržiūrimas kolegų ir reikalauti bent vieno patvirtinimo. Per kodo peržiūrą kodo peržiūrėtojas gali rasti pakeitimų, pažeidžiančių vieną ar kelis ADR. Tokiu atveju peržiūrėtojas paprašo kodo pakeitimo autoriaus atnaujinti kodą ir pateikia nuorodą į ADR. Kai autorius atnaujina kodą, jį patvirtina kolegos peržiūrėtojai ir jis sujungiamas į pagrindinę kodo bazę.


## ADR peržiūros procesas

Komanda ADR turėtų traktuoti kaip nekeičiamus dokumentus po to, kai juos priima arba atmeta. Norint pakeisti esamą ADR, reikia sukurti naują ADR, nustatyti naujo ADR peržiūros procesą ir patvirtinti ADR. Jei komanda patvirtina naują ADR, savininkas turėtų pakeisti seno ADR būseną į **Pakeistas** (angl. Superseded).
