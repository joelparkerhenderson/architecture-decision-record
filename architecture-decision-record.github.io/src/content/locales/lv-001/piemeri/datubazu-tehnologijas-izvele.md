# Arhitektūras lēmuma ieraksts: datubāzu tehnoloģijas izvēle

## Statuss

Pieņemts

## Konteksts

Mēs projektējam jaunu lietojumprogrammu, kurai nepieciešama datu glabāšana un izgūšana mērogojamā un veiktspējīgā veidā. Esam noteikuši trīs datubāzu tehnoloģiju veidus, ko parasti izmanto: relāciju datubāzes, dokumentu datubāzes un notikumu datubāzes.

Relāciju datubāzes glabā datus tabulās ar fiksētām shēmām un nodrošina stingrus datu integritātes ierobežojumus. Tās ir piemērotas lietojumprogrammām, kurām nepieciešamas sarežģītas datu attiecības un transakcijas. Piemēri ir MySQL, PostgreSQL un Oracle.

Dokumentu datubāzes glabā datus JSON līdzīgos dokumentos un ir bez shēmas. Tās ir labi piemērotas lietojumprogrammām, kurām nepieciešami elastīgi datu modeļi un horizontāla mērogošana. Piemēri ir MongoDB, Couchbase un Amazon DynamoDB.

Notikumu datubāzes glabā datus kā notikumu virkni, fiksējot katru datu izmaiņu. Tās ir piemērotas lietojumprogrammām, kurām nepieciešama revīzija, notikumu avotu izmantošana (event sourcing) un sarežģīta datu apstrāde. Piemēri ir Apache Kafka, Apache Pulsar un AWS Kinesis.
Lēmums

Rūpīgi izvērtējot mūsu lietojumprogrammas prasības un ierobežojumus, mēs nolēmām izmantot dokumentu datubāzi.

## Pamatojums

Mēs izvēlējāmies dokumentu datubāzi, jo:

1. Mūsu lietojumprogrammai nepieciešams elastīgs datu modelis, kas var attīstīties laika gaitā. Dokumentu datubāzes ļauj mums glabāt datus formātā bez shēmas, kas nozīmē, ka varam pievienot jaunus laukus vai mainīt esošo dokumentu struktūru, nemainot datubāzes shēmu.

2. Mūsu lietojumprogrammai jāmērogojas horizontāli, lai apstrādātu lielus datu un datplūsmas apjomus. Dokumentu datubāzēm ir iebūvēts atbalsts sadalīšanai (sharding) un replicēšanai, kas ļauj mums sadalīt datus pa vairākiem serveriem un apstrādāt augstu lasīšanas un rakstīšanas caurlaidspēju.

3. Mūsu lietojumprogrammai nepieciešama ātra un efektīva datu izgūšana. Dokumentu datubāzes nodrošina jaudīgas indeksēšanas un vaicāšanas iespējas, kas ļauj mums ātri un efektīvi izgūt datus.

4. Mūsu lietojumprogrammai nav nepieciešamas sarežģītas transakcijas vai datu attiecības. Lai gan relāciju datubāzes izceļas ar datu integritātes ierobežojumu nodrošināšanu un sarežģītu transakciju apstrādi, mūsu lietojumprogrammai tādu prasību nav. Dokumentu datubāzes mūsu lietojuma gadījumam var nodrošināt pietiekamas konsekvences un izturības garantijas.

## Sekas

Izvēloties dokumentu datubāzi, mums būs jāiegulda laiks, lai apgūtu un izprastu konkrēto tehnoloģiju, ko izvēlēsimies izmantot. Turklāt mums būs jānodrošina, ka mūsu lietojumprogrammas datu modelis labi atbilst dokumentu datubāzes datu modelim, lai maksimāli palielinātu veiktspēju un mērogojamību.

Tomēr mēs uzskatām, ka dokumentu datubāzes izmantošanas ieguvumi atsver izmaksas un ka tā vislabāk atbilst mūsu lietojumprogrammas prasībām un ierobežojumiem.
