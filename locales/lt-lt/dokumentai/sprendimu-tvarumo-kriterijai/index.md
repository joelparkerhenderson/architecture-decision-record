# Sprendimų tvarumo kriterijai

<https://www.infoq.com/articles/sustainable-architectural-design-decisions/>

Norėdami išsamiai apibrėžti sprendimų tvarumą, išvedėme penkis pagrindinius kriterijus.

## Strateginis

Priimant sprendimą, kas nagrinėja strategines pasekmes, turėtų atsižvelgti į tokius dalykus kaip ilgalaikis sprendimų poveikis, pavyzdžiui, būsimos eksploatacijos ir priežiūros pastangos.

## Išmatuojamas ir valdomas

Sprendimo rezultatą galite matuoti ir vertinti laikui bėgant pagal objektyvius, geriausia skaitinius, kriterijus (kaip, pavyzdžiui, propaguoja kokybės atributų scenarijai ir dirbtuvės4). Užfiksuoti visus smulkius sprendimus neįmanoma, todėl architektai turi apriboti sprendimų detalumą iki tam tikro lygio (pavyzdžiui, kurti projektavimo klasę). Tai lems tvaresnį sprendimų rinkinį ir mažiau atsekamumo saitų. Be to, ribojant sprendimų tarpusavio priklausomybių skaičių, sumažėja pokyčių bangos efektas.

## Pasiekiamas ir realistiškas

Sprendimo pritaikymo problemai pagrindimas turėtų būti parinktas pragmatiškai ir padarytas aiškus. Pavyzdžiui, architektai gali nurodyti, kad stengėsi išvengti per didelio ar per mažo projektavimo (t. y. turėtų taikyti požiūrį „pakankamai gerai“).

## Pagrįstas reikalavimais

Sprendimų priėmimas turėtų būti grindžiamas konkrečios srities architektūros patirtimi ir kontekstu. Jame reikėtų atsižvelgti į įmonės aplinką, taip pat į projekto reikalavimus ir apribojimus, įskaitant dabartinius kūrimo komandos įgūdžius, mokymų biudžetą ir procesą.

## Nesenstantis

Sprendimai turėtų būti grindžiami patirtimi ir žiniomis, kurios greičiausiai netrukus nepasens. Pavyzdžiui, architektai gali rinktis nuo platformos nepriklausomus architektūros šablonus ar taktikas.
