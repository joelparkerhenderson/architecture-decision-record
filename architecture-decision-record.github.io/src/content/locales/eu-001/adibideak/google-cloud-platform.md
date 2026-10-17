# Google Cloud Platform-erako arkitektura-erabakien erregistroa

## Testuingurua

Google Cloud Platform (GCP) hodei-konputazioko plataforma garrantzitsua da, hodei-zerbitzu desberdinak eskaintzen dituena, konputazio-, biltegiratze- eta sare-soluzioak barne. ADR honen helburua gure erakundearentzat GCP oinarritutako azpiegitura garatzeko eta ezartzeko hartutako arkitektura-erabakiak dokumentatzea da.

## Erabakia

Gure erakundeak Google Cloud Platform gure aplikaziorako hodei-azpiegitura gisa erabiltzea erabaki du. Erabaki honen kontuan hartzeko nagusiak hauek dira:

   - Kostu-eraginkortasuna

   - Eskalagarritasuna

   - Fidagarritasuna

   - Malgutasuna

## Hautaketak

GCP-ren zerbitzu hauek aukeratu dira gure eskakizunak betetzeko:

   - Compute Engine makina birtual eta konputazio-baliabideetarako

   - Cloud Storage objektuen biltegiratzerako eta fitxategien ostatatzerako

   - Cloud SQL kudeatutako datu-base zerbitzurako

   - Firebase aplikazioen garapenerako eta ostatatzerako

## Arrazoibidea

   - Kostu-eraginkortasuna: Google Cloud Platform oso kostu-eraginkorra da beste hodei-plataformekin alderatuta, aurrekontu-murrizketak dituzten erakundeentzat aukera erakargarria bihurtuz.

   - Eskalagarritasuna: GCP-ren azpiegitura erraz eskalagarriak edozein trafiko-kopuru denbora errealean kudeatzea ahalbidetzen du.

   - Fidagarritasuna: GCP-ren kudeatutako zerbitzuek fidagarritasun handia eskaintzen dute, babeskopia automatikoekin eta hondamendi-berreskuratzeko gaitasunekin, baliabideen eta datuen erabilgarritasun handia bermatzen dutenak.

   - Malgutasuna: Plataformak domeinu desberdinetan, hala nola AA, datu-analitika eta IoT, tresna eta zerbitzu ugari eskaintzen ditu, oso erabilgarria bihurtuz.

## Ondorioak

Google Cloud Platform-era migratzeak gure taldeak GCP zerbitzuetan prestatzea, aplikazioa hautatutako zerbitzuekin bateragarria izateko berriro arkitekturatzea eta azpiegitura-kodea GCP zerbitzuak onartzeko eguneratzea eskatuko du. Hala ere, migrazioa amaitutakoan, gure aplikazioa ostatatzeko azpiegitura oso eskalagarria, fidagarria eta kostu-eraginkorra izango dugula espero da. Gainera, GCP-n baliabideak hornitzearen etengabeko kostuak kudeatu beharko ditugu.

## Ondorioa

Google Cloud Platform aukera bikaina da gure hodei-azpiegiturarako bere kostu-eraginkortasunagatik, eskalagarritasunagatik, fidagarritasunagatik eta malgutasunagatik. Hautatutako zerbitzuak erabiliz, gure aplikaziorako azpiegitura oso erabilgarri eta sendoa eman dezakegu.
