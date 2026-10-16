# {Jūsų pavadinimas čia}

!!! info

    **Būsena**: { Pasiūlytas | Peržiūrimas | Priimtas |  Atmestas | Pakeistas | Nebenaudotinas }
    
    **Atnaujinta**: {YYYY-MM-DD}

## Santrauka

{Tai jūsų ADR „vadovų santrauka“ arba „liftų kalba“. Keliais glaustais sakiniais
(paprastai 2–4) aiškiai nurodykite pagrindinę problemą, klausimą ar galimybę,
kurią šis ADR nagrinėja. Trumpai užsiminkite apie priimtą sprendimą arba
dėmesio sritį. Tikslas – padėti skaitytojams greitai suprasti, apie ką šis
ADR, ir nuspręsti, ar jis jiems aktualus, neskaitant viso dokumento.
Įsivaizduokite tai kaip techninio straipsnio anotaciją arba labai trumpą
pagrindinės temos įvadą.}

## Veiksniai

{Šiame skyriuje paaiškinama, **kodėl** šis sprendimas priimamas **dabar**. Aiškiai
suformuluokite pagrindines motyvacijas, poreikius ar problemas, dėl kurių šis
architektūrinis sprendimas yra būtinas. Pagalvokite apie pagrindines priežastis
ir spaudimą.}

* {pvz., kuriame naują funkciją / galimybę, kuriai reikia...}

* {pvz., turime pagerinti našumą, prieinamumą, pašalinti skolą...}

* {pvz., naudotojų atsiliepimai rodo, kad...}

* {pvz., dabartinis požiūris kelia šiuos apribojimus...}

## Variantai

{Čia išvardykite skirtingus variantus, kuriuos svarstote. Laikykitės faktų ir
venkite nuomonių, kitas skyrius skirtas analizei. Pateikite glaustą aprašą,
nuorodas į svarbią dokumentaciją ar pavyzdžius.

Įtraukite visas reikšmingas alternatyvas, kurias nagrinėjote, net jei galiausiai
jos nebuvo pasirinktos. Tikslas – suteikti skaitytojams aiškų, nešališką
kiekvienos alternatyvos supratimą, prieš pradedant vertinimą.}

### {1 varianto pavadinimas}

{Aprašykite variantą, pateikite santrauką, išvardykite faktus, pateikite nuorodas ir pan.}

### {n varianto pavadinimas}

...

## Variantų analizė

{Čia kritiškai įvertinate kiekvieną skyriuje *Variantai* pateiktą variantą.
Kiekvienam variantui pateikite subalansuotą jo privalumų, trūkumų ir kitų
svarbių svarstymų ar kompromisų vaizdą. Būkite konkretūs ir, kai įmanoma,
susiekite savo teiginius su *Veiksniais*.

Apsvarstykite tokius aspektus kaip:

* Kaina (kūrimo, eksploatacijos, licencijavimo)

* Sudėtingumas (įgyvendinimo, priežiūros, mokymosi kreivė)

* Rizikos (techninės, eksploatacinės, saugumo)

* Atitiktis architektūros principams ar esamiems standartams

* Poveikis našumui, mastelio keitimui, naudojamumui, prižiūrimumui,
    saugumui ir pan.

Įtraukite tiek teiginių „Privalumas / Trūkumas / Kita“, kiek reikia.
}

### {1 varianto vertinimas}

* Privalumas: {Konkretus šio varianto pranašumas ar nauda.}

* Trūkumas: {Konkretus su šiuo variantu susijęs trūkumas, rizika ar kaina.}

* Kita: {Svarbus punktas, kuris nėra griežtai privalumas ar trūkumas.}

### {n varianto vertinimas}

...

## Rekomendacija

{Čia aiškiai nurodykite galutinį sprendimą ir aiškiai įvardykite pasirinktą
variantą. Išsamiai paaiškinkite, **kodėl** pasirinktas būtent šis variantas.
Aiškiai išdėstykite, kaip pasirinktas variantas geriausiai atliepia *Veiksnius*
ir atitinka pagrindinius reikalavimus ar išsprendžia nurodytą problemą.}

### Pasekmės

{Šis skyrius yra **neprivalomas**.}

{Dabar, kai sprendimas priimtas, kokių rezultatų ir poveikio tikimasi, tiek
teigiamo, tiek neigiamo? Kokie žinomi apribojimai, sąnaudos ar rizikos
priimami darant šį sprendimą? Kaip šis sprendimas paveiks skirtingus
suinteresuotuosius asmenis, kitas sistemas, kūrimo praktikas, eksploatacijos
procedūras ar naudotojo patirtį?}

* Privalumas: {Konkretus teigiamas rezultatas ar nauda, tikimasi iš šio sprendimo.}

* Trūkumas: {Konkretus priimtas trūkumas, kaina ar rizika, atsirandanti dėl šio
    sprendimo. }

* Kita: {Pasekmė, kuri nėra griežtai privalumas ar trūkumas.}

### Patvirtinimas

{Šis skyrius yra **neprivalomas**.}

{Apibūdinkite, kaip bus tikrinamas šio sprendimo įgyvendinimas ir kaip bus
užtikrinama nuolatinė atitiktis. Tai padeda parodyti, kad sprendimas nėra vien
teorinis, o bus aktyviai taikomas praktikoje ir stebimas.

Kaip patikrinsite, ar sprendimas įgyvendintas teisingai? (pvz., kodo
peržiūros, konkretūs testai, demonstracijos, kolegų peržiūra).

Kaip laikui bėgant bus išlaikomas šio sprendimo laikymasis? (pvz.,
automatizuoti patikrinimai, periodiniai auditai, komandos gairių
atnaujinimai, mokymai).

Ar yra konkrečių metrikų ar rodiklių, kurie parodys, kad sprendimas
pasiekia numatytus teigiamus rezultatus? (pvz., našumo palyginamieji
testai, naudojimo rodikliai, konkrečių klaidų sumažėjimas, naudotojų
atsiliepimų įvertinimai).

Kas atsakingas už tai prižiūrėti ir kas nutinka, jei sprendimo nesilaikoma?}

## Daugiau informacijos

{Šis skyrius yra **neprivalomas**.}

{Šiame skyriuje pateikite bet kokią papildomą informaciją, kuri palaiko
sprendimą, suteikia konteksto ar nukreipia būsimus veiksmus. Čia taip pat gali
būti nuorodos į kitus sprendimus ir išteklius.

Galite trumpai nurodyti, kas dalyvavo sprendimo priėmimo procese ir
ar bei kaip buvo pasiektas sutarimas. Taip pat galbūt norėsite pasiūlyti
laikotarpį ar konkrečius įvykius, kurie ateityje galėtų paskatinti
šio sprendimo pakartotinį vertinimą.}
