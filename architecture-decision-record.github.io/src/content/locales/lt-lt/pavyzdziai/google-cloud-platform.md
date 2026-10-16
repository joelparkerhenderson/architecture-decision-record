# Architektūros sprendimo įrašas dėl Google Cloud Platform

## Kontekstas

Google Cloud Platform (GCP) yra žymi debesijos skaičiavimo platforma, siūlanti įvairias debesijos paslaugas, įskaitant skaičiavimo, saugojimo ir tinklo sprendimus. Šiuo ADR siekiama dokumentuoti architektūrinius sprendimus, priimtus kuriant ir įgyvendinant GCP pagrįstą infrastruktūrą mūsų organizacijai.

## Sprendimas

Mūsų organizacija nusprendė kaip debesijos infrastruktūrą savo programai naudoti Google Cloud Platform. Pagrindiniai šio sprendimo svarstymai yra:

   - Ekonomiškumas

   - Mastelio keitimas

   - Patikimumas

   - Lankstumas

## Pasirinkimai

Mūsų reikalavimams tenkinti pasirinktos šios GCP paslaugos:

   - Compute Engine virtualioms mašinoms ir skaičiavimo ištekliams

   - Cloud Storage objektų saugojimui ir failų talpinimui

   - Cloud SQL valdomai duomenų bazės paslaugai

   - Firebase programų kūrimui ir talpinimui

## Pagrindimas

   - Ekonomiškumas: Google Cloud Platform yra labai ekonomiška, palyginti su kitomis debesijos platformomis, todėl yra patraukli galimybė organizacijoms, turinčioms biudžeto apribojimų.

   - Mastelio keitimas: lengvai keičiamo mastelio GCP infrastruktūra leidžia realiuoju laiku apdoroti bet kokį srauto kiekį.

   - Patikimumas: GCP valdomos paslaugos pasižymi dideliu patikimumu, su automatinėmis atsarginėmis kopijomis ir atkūrimo po avarijos galimybėmis, užtikrinančiomis aukštą išteklių ir duomenų prieinamumą.

   - Lankstumas: platforma suteikia įvairių įrankių ir paslaugų skirtingose srityse, tokiose kaip DI, duomenų analitika ir daiktų internetas (IoT), todėl ji yra labai universali.

## Pasekmės

Perkėlimas į Google Cloud Platform reikalaus apmokyti mūsų komandas GCP paslaugų, pertvarkyti programos architektūrą, kad ji būtų suderinama su pasirinktomis paslaugomis, ir atnaujinti infrastruktūros kodą, kad jis palaikytų GCP paslaugas. Tačiau tikimasi, kad baigus perkėlimą turėsime labai keičiamo mastelio, patikimą ir ekonomišką infrastruktūrą programai talpinti. Taip pat turėsime valdyti nuolatines išteklių teikimo GCP išlaidas.

## Išvada

Google Cloud Platform yra puikus pasirinkimas mūsų debesijos infrastruktūrai dėl savo ekonomiškumo, mastelio keitimo, patikimumo ir lankstumo. Naudodami pasirinktas paslaugas, galime užtikrinti labai prieinamą ir tvirtą infrastruktūrą savo programai.
