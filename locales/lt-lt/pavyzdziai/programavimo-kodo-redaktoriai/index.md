# Architektūros sprendimo įrašas: programavimo kodo redaktoriai

## Kontekstas

Programavimo kodo redaktoriai yra esminis programuotojų įrankis kodui rašyti ir redaguoti. Yra daugybė kodo redaktorių, kurių kiekvienas turi savo funkcijų rinkinį, privalumus ir trūkumus. Šio ADR tikslas – dokumentuoti architektūrinius sprendimus, priimtus dėl programavimo kodo redaktorių.

## Prioritetai

Programavimo kodo redaktorių architektūroje turėtų būti teikiama pirmenybė šiems dalykams:

* **Moduliškumas**: kodo redaktorius turėtų būti suprojektuotas moduliškai, leidžiant programuotojams jį pritaikyti ir plėsti pagal poreikį. Tai leidžia sukurti lanksčią architektūrą, galinčią prisitaikyti prie skirtingų programuotojų ir komandų poreikių.

* **Našumas**: kodo redaktorius turėtų būti našus ir greitai reaguoti, leisdamas programuotojams dirbti efektyviai, kad naudojamas įrankis jų nestabdytų.

* **Naudotojo sąsaja**: naudotojo sąsaja turėtų būti intuityvi ir lengvai naudojama, leidžianti programuotojams sutelkti dėmesį į savo kodą, o ne kovoti su redaktoriumi.

* **Išplečiamumas**: kodo redaktorius turėtų būti suprojektuotas taip, kad būtų galima lengvai jį išplėsti trečiųjų šalių papildiniais ir integracijomis.

* **Suderinamumas**: kodo redaktorius turėtų būti suderinamas su plačiu programavimo kalbų ir technologijų spektru, kad būtų naudingas įrankis plačiam programuotojų ratui.

## Sprendimas

Remiantis šiais prioritetais, programavimo kodo redaktorių architektūra turėtų būti suprojektuota su šiais komponentais:

* **Branduolys**: šis komponentas suteikia pagrindines kodo redaktoriaus funkcijas, tokias kaip sintaksės paryškinimas, teksto redagavimas ir failų valdymas.

* **UI**: šis komponentas suteikia kodo redaktoriaus naudotojo sąsają, įskaitant meniu, įrankių juostas ir sparčiuosius klavišus.

* **Papildiniai**: šis komponentas leidžia programuotojams išplėsti kodo redaktoriaus funkcionalumą įdiegiant trečiųjų šalių papildinius. Papildiniai gali suteikti papildomų funkcijų, tokių kaip kodo užbaigimas, tikrinimas (linting) ar derinimas.

* **Integracijos**: šis komponentas leidžia kodo redaktoriui integruotis su kitais įrankiais ir technologijomis, tokiomis kaip versijų valdymo sistemos, kūrimo sistemos ar derinimo įrankiai.

## Pagrindimas

Kodo redaktoriaus moduliškumas leidžia programuotojams jį pritaikyti ir plėsti pagal poreikį. Tai svarbu, nes skirtingi programuotojai ir komandos turi skirtingus poreikius ir darbo eigas, o lanksti architektūra gali šiuos skirtumus patenkinti.

* **Našumas**: esminis, nes programuotojai turi galėti dirbti efektyviai, kad jų neslopintų jų įrankiai. Našus kodo redaktorius yra būtinas produktyvumui ir gali padėti programuotojams išlaikyti dėmesį ir susikaupimą.

* **UI**: svarbi, nes ji leidžia programuotojams sutelkti dėmesį į savo kodą, o ne kovoti su redaktoriumi. Tai gali lemti didesnį produktyvumą ir mažiau nusivylimo programuotojams.

* **Išplečiamumas**: galingas, nes leidžia kodo redaktorių pritaikyti skirtingiems poreikiams ir darbo eigoms. Trečiųjų šalių papildiniai ir integracijos gali suteikti papildomų funkcijų ir galimybių, kurių nėra pagrindiniame redaktoriuje.

* **Suderinamumas**: vertingas, nes leidžia kodo redaktorių naudoti su plačiu programavimo kalbų ir technologijų spektru. Tai daro redaktorių naudingesniu įrankiu plačiam programuotojų ratui.

Branduolio, papildinių, integracijų ir UI komponentai užtikrina aiškų rūpesčių atskyrimą ir leidžia sukurti modulinę architektūrą, kurią galima lengvai plėsti ir pritaikyti. Ši architektūra yra lanksti, našu ir suderinama su plačiu programavimo kalbų ir technologijų spektru, todėl yra naudingas įrankis programuotojams.