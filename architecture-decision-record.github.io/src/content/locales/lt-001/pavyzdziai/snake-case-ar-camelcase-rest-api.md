# Architektūros sprendimo įrašas: snake_case ar camelCase REST API?

Sprendimas: REST API galiniams taškams bus naudojama snake_case pavadinimų konvencija

Būsena: priimtas

## Kontekstas

REST API pavadinimų konvencijose yra du populiarūs formatai: snake_case ir camelCase. snake_case formate kiekvienas pavadinimo žodis atskiriamas pabraukimo brūkšniais, o camelCase formate pirmasis pavadinimo žodis rašomas mažosiomis raidėmis, o paskesnių žodžių pirmoji raidė rašoma didžiąja. Šiuo sprendimu bus nustatyta, kurią pavadinimų konvenciją reikėtų naudoti REST API.

## Sprendimo veiksniai

- Nuoseklumas su esamomis projekto pavadinimų konvencijomis

- Skaitomumas ir aiškumas bet kam, kas gali dirbti su API

- Atitiktis pramonės geriausioms REST API pavadinimų praktikoms

- Įgyvendinimo ir priežiūros paprastumas

## Sprendimas

REST API galiniams taškams bus naudojama snake_case pavadinimų konvencija. Šį pasirinkimą lemia šie veiksniai:

1. **Nuoseklumas**: projektas jau naudoja snake_case pavadinimų konvenciją visiems galiniams taškams, ir būtų naudinga išlaikyti šią konvenciją, kad būtų užtikrintas nuoseklumas visame projekte.

2. **Skaitomumas ir aiškumas**: snake_case konvencija yra labiau skaitoma ir lengviau suprantama. Pabraukimo brūkšniai aiškiai atskiria žodžius, todėl lengviau išskaidyti ir suprasti pavadinimo prasmę.

3. **Atitiktis pramonės geriausioms praktikoms**: snake_case konvencija plačiai naudojama pramonėje ir laikoma geriausia REST API praktika, todėl yra geras projekto pasirinkimas.

4. **Įgyvendinimo ir priežiūros paprastumas**: esamos pavadinimų konvencijos laikymasis yra lengvesnis įgyvendinti ir prižiūrėti, nes pasirinkus naują konvenciją reikėtų atnaujinti visą esamą kodą ir dokumentaciją.

## Pasekmės

Šis sprendimas turi galimų pasekmių. 

* Jei kuris nors naujas komandos narys, prisijungiantis prie projekto, nėra susipažinęs su snake_case pavadinimų konvencija, tai gali lemti painiavą ir klaidas kūrimo metu. Tačiau kadangi snake_case yra plačiai naudojama konvencija, tokia rizika yra minimali. 
  
* Jei projekte naudojami kiti įrankiai ar karkasai, kurie labai remiasi camelCase konvencija, gali prireikti papildomų pastangų konvertuojant tarp pavadinimų konvencijų. Tačiau tai nėra didelis rūpestis, nes projektas standartizuotas pagal snake_case konvenciją. 
 
Apskritai sprendimas REST API galiniams taškams naudoti snake_case pavadinimų konvenciją lemia nuoseklų, skaitomą ir pramonės standartą atitinkantį požiūrį, kartu esant lengvam įgyvendinti ir prižiūrėti.

<h6>Padėka: šį puslapį sugeneravo ChatGPT, vėliau jis buvo redaguotas aiškumui ir formatui pagerinti.</h6>