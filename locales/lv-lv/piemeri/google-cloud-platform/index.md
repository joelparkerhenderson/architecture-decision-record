# Arhitektūras lēmuma ieraksts par Google Cloud Platform

## Konteksts

Google Cloud Platform (GCP) ir ievērojama mākoņskaitļošanas platforma, kas piedāvā dažādus mākoņpakalpojumus, tostarp skaitļošanas, glabāšanas un tīklošanas risinājumus. Šī ADR mērķis ir dokumentēt arhitektūras lēmumus, kas pieņemti, lai izstrādātu un īstenotu uz GCP balstītu infrastruktūru mūsu organizācijai.

## Lēmums

Mūsu organizācija ir nolēmusi izmantot Google Cloud Platform kā mākoņinfrastruktūru savai lietojumprogrammai. Galvenie apsvērumi šim lēmumam ir:

   - Rentabilitāte

   - Mērogojamība

   - Uzticamība

   - Elastība

## Izvēles

Mūsu prasību apmierināšanai ir izvēlēti šādi GCP pakalpojumi:

   - Compute Engine virtuālajām mašīnām un skaitļošanas resursiem

   - Cloud Storage objektu glabāšanai un failu mitināšanai

   - Cloud SQL pārvaldītam datubāzes pakalpojumam

   - Firebase lietotņu izstrādei un mitināšanai

## Pamatojums

   - Rentabilitāte: Google Cloud Platform ir ļoti rentabla salīdzinājumā ar citām mākoņplatformām, padarot to par pievilcīgu iespēju organizācijām ar budžeta ierobežojumiem.

   - Mērogojamība: GCP viegli mērogojamā infrastruktūra ļauj reāllaikā apstrādāt jebkādu datplūsmas apjomu.

   - Uzticamība: GCP pārvaldītie pakalpojumi piedāvā augstu uzticamību ar automatizētām rezerves kopijām un atkopšanas pēc katastrofas iespējām, kas nodrošina resursu un datu augstu pieejamību.

   - Elastība: platforma nodrošina dažādus rīkus un pakalpojumus dažādās jomās, piemēram, MI, datu analītikā un IoT, padarot to ļoti daudzpusīgu.

## Sekas

Pārcelšanās uz Google Cloud Platform prasīs apmācīt mūsu komandas par GCP pakalpojumiem, pārveidot lietojumprogrammu arhitektūru, lai tā būtu saderīga ar izvēlētajiem pakalpojumiem, un atjaunināt infrastruktūras kodu, lai atbalstītu GCP pakalpojumus. Tomēr paredzams, ka pēc migrācijas pabeigšanas mums būs ļoti mērogojama, uzticama un rentabla infrastruktūra mūsu lietojumprogrammas mitināšanai. Mums būs jāpārvalda arī pastāvīgās resursu nodrošināšanas izmaksas GCP.

## Secinājums

Google Cloud Platform ir lieliska izvēle mūsu mākoņinfrastruktūrai tās rentabilitātes, mērogojamības, uzticamības un elastības dēļ. Izmantojot izvēlētos pakalpojumus, mēs varam nodrošināt ļoti pieejamu un robustu infrastruktūru savai lietojumprogrammai.
