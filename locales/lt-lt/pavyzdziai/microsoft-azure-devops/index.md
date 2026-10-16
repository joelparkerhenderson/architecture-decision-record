# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: An Unsatisfying Adventure](#microsoft-devops-ci-an-unsatisfying-adventure)
  * [Hacker News diskusijos akcentai](#hacker-news-diskusijos-akcentai)
  * [Windows Development MVP](#windows-development-mvp)
  * [Edward Thomson (Azure PM) santrauka](#edward-thomson-azure-pm-santrauka)


## Santrauka


### Problema

Norime naudoti devops savo projektams kurti, integruoti, diegti ir talpinti. Svarstome Microsoft Azure DevOps.

  * Norime, kad programuotojo patirtis būtų greita ir patikima, tiek devops sąrankos (pvz., konfigūravimo), tiek nuolatinio naudojimo metu (pvz., greiti kūrimo laikai).
  
  * Norime apsvarstyti galimybę naudoti Microsoft Azure kaip visumą projekto programoms, duomenų bazėms ir pan. talpinti.


### Sprendimas

Nuspręsta nenaudoti Microsoft Azure DevOps.


### Būsena

Nuspręsta. Atviri pakartotiniam svarstymui, jei / kai atsiras nauja reikšminga informacija.


## Detalės


### Prielaidos

Visos įprastos devops prielaidos, pavyzdžiui, knygoje Accelerate.

  * Greiti kūrimo laikai labai padeda. Tai pagreitina grįžtamojo ryšio ciklus.

  * Galime keisti dalis alternatyvių tiekėjų, t. y. galime norėti naudoti savo greitesnius kūrimo serverius arba pasirinkti savo versijų valdymo sistemą, arba derinti su savarankiškai talpinamu nuolatinės integracijos serveriu.
  
  * Supaprastintas naudojamumas labai padeda programuotojo patirčiai, o kartu ir subtiliems aspektams, tokiems kaip nuoseklumas, aiškumas, saugumas ir mokymosi kreivės paprastumas.

  * Kai kas nors sugenda ar kelia problemų, norime veiksmingo būdo pranešti apie problemą. Tai ypač svarbu bet kokioms su saugumu susijusioms problemoms.


### Apribojimai

Žinomų nėra. Azure yra paskelbusi įsipareigojimą gerai sugyventi su išoriniais įrankiais.


### Pozicijos

Svarstėme Microsoft Azure Devops ir AWS, kuris yra esamas sprendimas.

Eksperimentavome su Azure DevOps, Azure Pipelines, Azure Repo ir naujo serverio paleidimu Azure per Terraform.

Eksperimentavome gaudami palaikymą iš Microsoft atstovų.

Rinkome informaciją iš kolegų tinklaraščiuose ir Hacker News.


### Argumentas

Azure DevOps reklamuoja puikų pasiūlymų rinkinį, tačiau jie neatitinka lūkesčių, prastai veikia kartu, o palaikymas prastas.

Mūsų tiesioginė patirtis:

  * Azure sąranka yra sąsajų netvarka, kai kurios iš jų persidengia su Microsoft paskyromis, kai kurios – ne. Pvz., yra Azure prisijungimas, Microsoft.com prisijungimas, Live.com prisijungimas ir pan., ir visi vienu metu veikia.

  * Sąrankos metu susidūrėme su nedidele saugumo problema ir nerado sprendimo. Bandėme apie ją pranešti daugeliu būdų, daugeliui Microsoft atstovų, be sėkmės. Sėkmingai pranešėme Microsoft saugumo komandai, kuri atsakė, kad netaisys.

  * Dokumentacija dažnai arba neteisinga, arba pasenusi. Bent dalis to atsiranda dėl prastos Microsoft paieškos sistemos, o dalis – dėl prastos SEO.
  
  * Terraform sąranka gerai dokumentuota ir veikia. Tačiau Terraform palaikymas yra silpnas, palyginti su AWS, nes Microsoft kuria verslo santykius su tiekėjais, kad šie pateiktų nuoseklius Terraform sąrankos pavyzdžius.

Mūsų kolegų patirtis:

  * Atlikę savo aklą vertinimą, ieškojome kolegų patirties. Tai, ką radome, patvirtino mūsų patirtį.

  * Kolegos pranešė apie papildomas problemas dėl kūrimo laikų ir problemas su savo kūrimo serverio atsinešimu (angl. bring-your-own-build server). Šios problemos yra žymiai rimtesnės nei sąsajos problemos, nes kūrimas yra pagrindinis kūrimo konvejerio tikslas, o mes tikimės kasdien atlikti daug kūrimų.

  * Radome puikų Azure komandos narių dalyvavimą diskusijų vietose. Už tai Microsoft nusipelno pagyrimo. Mus ypač sužavėjo Edward Thomson, Azure PM ir programuotojas, dėl jo dalyvavimo, tiesumo ir techninių paaiškinimų.


### Implikacijos

Microsoft Azure DevOps pasirinkimas, atrodo, bus brangesnis (~3 kartus) laiko ir kainos požiūriu nei Azure nepasirinkimas.


## Susiję


### Susiję sprendimai

Jei pasirinksime Azure DevOps, yra daug susijusių pasiūlymų, įskaitant Azure Repo, Azure Pipeline ir kt. Manome, kad jei pasirinksime Azure Devops, tai gali palengvinti daugiau Azure galimybių naudojimą arba apsunkinti kitų tiekėjų galimybių naudojimą.

Manome, kad Microsoft daro didelę pažangą programuotojo patirties srityje, ir matome, kaip Microsoft perka didelius programuotojų įrankius (pvz., GitHub) ir priklausomybes (pvz., Citus).

Jei pasirinksime Azure DevOps, galime norėti pabrėžti Microsoft įsigytų pasiūlymų pasirinkimą, o taip pat galime norėti prie įsigytų pasiūlymų žiūrėti atidžiau / juos kruopščiau vertinti dėl galimo audinių atmetimo, pvz., darbuotojų kaitos rizikos.


### Susiję reikalavimai

Norime, kad kūrimo laikai būtų labai greiti. Sutinkame už tai mokėti didelę priemoką. Taip yra todėl, kad norime labai greitai iteruoti.

Norime labai didelio patikimumo. Sutinkame už tai mokėti didelę priemoką. Taip yra todėl, kad testuojame didelės vertės naudojimo atvejus, įskaitant finansines transakcijas, konfidencialias transakcijas ir pan.

Mūsų 4 pagrindiniai devops KPI apima vidutinį atkūrimo laiką, o tam reikia greitų kūrimų ir didelio patikimumo.


### Susiję artefaktai

Norime, kad kūrimo sistema išvestų artefaktus, tinkamus naudoti kitose sistemose, pavyzdžiui, Artifactory.


### Susiję principai

Lengvai atšaukiama. Galime vertinti Azure DevOps lygiagrečiai su esamu AWS.


## Pastabos


### Microsoft Devops CI: An Unsatisfying Adventure

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Tinklaraščio įrašas.

„Kaip programinės įrangos kūrėjas iš pirmų lūpų žinau, kaip sunku greitai ir pigiai kurti kokybiškus produktus. Tai meno forma, kurią kartais atliekame gerai, o kartais ji virsta kažkuo panašiu į Obamos eros vyriausybės sveikatos apsaugos svetainę. Mūsų kontrolės lygis gaunamam produktui yra įvairus, o kaltė už nesėkmę dažnai krenta ne ant tų žmonių sprendimų priėmimo hierarchijoje. Microsoft Azure DevOps (anksčiau žinomas kaip Visual Studio Team Services), nepaisant aiškiai gerų ketinimų, yra tobula blogų sprendimų ir prasto vykdymo audra.“


### Hacker News diskusijos akcentai

https://news.ycombinator.com/item?id=18983586

„Savo darbe plačiai naudojame Azure DevOps ir, išbandęs GitHub, Gitlab, savarankiškai talpinamus sprendimus, Jenkins, TeamCity... Azure DevOps užima paskutinę vietą.“

„Sąsaja visur siaubingai nerangi. Blogiausia man – pull requests. Neįtikėtinai sunku su žmonėmis dirbti prie pull request. Negaliu net nurodyti „vienos“ konkrečios problemos – mums sugedę viskas.“

„Azure Devops yra kažkas, ką noriu pamilti. Sąsaja nuolat keičiasi, bet netaiso pagrindinių klaidų, kurios egzistuoja amžius.“

„Įrankiai nėra gerai integruoti, sąsaja tikrai lėta, nėra skydelio vaizdo su aktyviais pull requests, kūrimais, išleidimais ir pan. mano mėgstamoms saugykloms. Kūrimo / diegimo laikai pamišėliškai lėti.“

„Bandėme naudoti ir Azure Boards (darbo elementai, lentos, atsilikimai ir pan.). Oi. Tai visiška sąsajos netvarka iš nesusijusių idėjų. Užuot gerai įgyvendinę vieną dalyką, jie siaubingai įgyvendino du tuzinus dalykų.“


### Windows Development MVP

Windows Development MVP čia. Jaučiu, kad turiu prisiimti dalį atsakomybės už tai, kad apie šias problemas nekalbėjau garsiau. Bet turiu pasakyti, kad nusivyliau išgirdęs, jog jūs „nustebote“ dėl UX problemų. Aš jūsų žmonėms sakiau, kad UX siaubingas (pvz., dar prieš paleidimą) ir vis girdėjau atsakymą „žinome, taisome“. Pradėsiu formalizuoti atsiliepimus ir pastumsiu juos per vamzdžius, laukite naujienų. Aš taip pat vietinis (Bellevue), mielai ateičiau ir pabandyčiau sukurti konvejerį savo gana paprastai oss .net/wpf/uwp programai. Įtariu, kad tai atvers akis mums abiem.

Keli pavyzdžiai:

* Negalima sukurti konvejerio su git saugykla, kurioje yra submodulių

* Neįmanoma redaguoti PATH kai kuriems pasirinktiniams įrankiams

* Naujo konvejerio patirtis tiesiog neturi daug prasmės, nauji naudotojai, spaudinėdami aplink, galiausiai atsidurs ne toje dokumentacijoje.


### Edward Thomson (Azure PM) santrauka

Aš parašiau kodą, kuris sujungia jūsų pull requests. Microsoft Azure DevOps programų vadovas (Program Manager); anksčiau programinės įrangos inžinierius, dirbęs su versijų valdymo įrankiais GitHub, Microsoft ir SourceGear.

https://www.edwardthomson.com/

libgit2 bendraautoris. https://libgit2.github.io

All Things Git, tinklalaidės apie Git, vedėjas kartu su kitu. https://www.allthingsgit.com/

Developer Tools Weekly, naujienlaiškio apie kūrimo įrankius, sudarytojas. https://developertoolsweekly.com/
