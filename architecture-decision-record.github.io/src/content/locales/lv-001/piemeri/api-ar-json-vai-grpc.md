# Arhitektūras lēmuma ieraksts: API ar JSON vai gRPC

## Statuss

Pieņemts

## Konteksts

Mēs projektējam API jaunam pakalpojumam, ko izmantos vairāki klienti. Esam apsvēruši divas API īstenošanas iespējas: JSON pa HTTP vai gRPC.

JSON pa HTTP ir plaši izmantota pieeja API veidošanai, un to atbalsta daudzas programmēšanas valodas un ietvari. Šī pieeja ir vienkārša, viegla un viegli saprotama, tāpēc tā ir laba izvēle daudziem projektiem. Tomēr tā var būt mazāk efektīva nekā citas iespējas, īpaši, apstrādājot lielus datu apjomus.

gRPC savukārt ir jaunāka tehnoloģija, kas piedāvā efektīvāku veidu, kā veidot API. Datu pārsūtīšanai tas izmanto bināro serializāciju, kas var būt ātrāka un kompaktāka nekā JSON. gRPC atbalsta arī divvirzienu straumēšanu (bidirectional streaming), padarot to par labu izvēli reāllaika lietojumprogrammām.

## Lēmums

Apsvēruši abu iespēju priekšrocības un trūkumus, mēs nolēmām savam API izmantot gRPC. Lai gan JSON pa HTTP ir vienkāršāka iespēja, mēs uzskatām, ka gRPC nodrošinās efektīvāku un mērogojamāku risinājumu mūsu pakalpojumam. Mēs arī paredzam, ka mūsu API apstrādās lielu datu apjomu, un gRPC bināra serializācija būs efektīvāka šādam lietojuma gadījumam.

Turklāt mēs uzskatām, ka gRPC atbalsts divvirzienu straumēšanai būs noderīgs reāllaika lietojumprogrammām, ko mēs varētu izstrādāt nākotnē.

## Sekas

Izvēloties gRPC, mums būs jāizmanto cits rīku un bibliotēku kopums sava API veidošanai, salīdzinot ar JSON pa HTTP. Tas var prasīt papildu laiku un pūles, lai apgūtu un īstenotu šīs tehnoloģijas. Turklāt klientiem, kuri vēlas izmantot mūsu API, būs jāizmanto ar gRPC saderīgas bibliotēkas, kuras var nebūt tik plaši atbalstītas kā JSON pa HTTP bibliotēkas.

Tomēr mēs uzskatām, ka gRPC izmantošanas ieguvumi atsver šos iespējamos trūkumus, un esam pārliecināti, ka šis lēmums rezultēsies efektīvākā un mērogojamākā API.
