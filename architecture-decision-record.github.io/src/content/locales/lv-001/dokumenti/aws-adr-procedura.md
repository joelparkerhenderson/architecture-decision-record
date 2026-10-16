# AWS arhitektūras lēmumu ierakstu procedūra

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Arhitektūras lēmuma ieraksts (ADR) ir dokuments, kas apraksta izvēli, ko komanda izdara par būtisku programmatūras arhitektūras aspektu, kuru tā plāno būvēt. Katrs ADR apraksta arhitektūras lēmumu, tā kontekstu un tā sekas. ADR ir stāvokļi, un tāpēc tiem ir dzīves cikls. ADR piemēru skatiet pielikumā.

ADR procedūras rezultāts ir arhitektūras lēmumu ierakstu kopums. Šis kopums veido lēmumu žurnālu. Lēmumu žurnāls nodrošina projekta kontekstu, kā arī detalizētu informāciju par īstenošanu un projektēšanu. Projekta dalībnieki pārskata katra ADR virsrakstus, lai iegūtu pārskatu par projekta kontekstu. Viņi lasa ADR, lai iedziļinātos projekta īstenojumos un projektēšanas izvēlēs.

Kad komanda pieņem ADR, tas kļūst nemainīgs. Ja jaunas atziņas prasa citu lēmumu, komanda ierosina jaunu ADR. Kad komanda pieņem jauno ADR, tas aizstāj iepriekšējo ADR.

## ADR procedūras tvērums

Projekta dalībniekiem jāizveido ADR katram arhitektūriski nozīmīgam lēmumam, kas ietekmē programmatūras projektu vai produktu, tostarp šādiem (Richards un Ford 2020):

* Struktūra (piemēram, modeļi, kā mikropakalpojumi)

* Nefunkcionālās prasības (drošība, augsta pieejamība un noturība pret kļūmēm)

* Atkarības (komponentu saistība)

* Saskarnes (API un publicētie līgumi)

* Būvēšanas paņēmieni (bibliotēkas, ietvari, rīki un procesi)

* Funkcionālās un nefunkcionālās prasības ir visizplatītākā ADR procedūras ievade.


## ADR saturs

Kad komanda konstatē vajadzību pēc ADR, komandas dalībnieks sāk rakstīt ADR, pamatojoties uz visa projekta veidni. (Veidņu piemērus skatiet ADR GitHub organizācijā.) Veidne vienkāršo ADR izveidi un nodrošina, ka ADR fiksē visu būtisko informāciju. Vismaz katram ADR jādefinē lēmuma konteksts, pats lēmums un lēmuma sekas projektam un tā rezultātiem. (Šo sadaļu piemērus skatiet pielikumā.) Viens no ADR struktūras spēcīgākajiem aspektiem ir tas, ka tā koncentrējas uz lēmuma iemeslu, nevis uz to, kā komanda to īstenoja. Izpratne par to, kāpēc komanda pieņēma lēmumu, atvieglo citiem komandas dalībniekiem lēmuma pieņemšanu un neļauj citiem arhitektiem, kuri nebija iesaistīti lēmumu pieņemšanas procesā, nākotnē šo lēmumu atcelt.


## ADR pieņemšanas process

Katrs komandas dalībnieks var izveidot ADR, taču komandai jāizveido ADR īpašumtiesību definīcija. Katram autoram, kas ir ADR īpašnieks, aktīvi jāuztur un jāpaziņo ADR saturs. Lai precizētu šo īpašumtiesību, šajā rokasgrāmatā turpmākajās sadaļās ADR autori tiek saukti par ADR īpašniekiem. Citi komandas dalībnieki vienmēr var sniegt ieguldījumu ADR. Ja ADR saturs mainās, pirms komanda pieņem ADR, īpašniekam šīs izmaiņas jāapstiprina.

Pēc tam, kad komanda ir noteikusi arhitektūras lēmumu un tā īpašnieku, ADR īpašnieks procesa sākumā iesniedz ADR stāvoklī **Ierosināts** (Proposed). ADR stāvoklī Ierosināts ir gatavi pārskatīšanai.

Pēc tam ADR īpašnieks uzsāk ADR pārskatīšanas procesu. ADR pārskatīšanas procesa mērķis ir izlemt, vai komanda pieņem ADR, nolemj, ka tas jāpārstrādā, vai noraida ADR. ADR pārskata projekta komanda, tostarp īpašnieks. Pārskatīšanas sanāksmei jāsākas ar īpašu laika logu ADR lasīšanai. Vidēji vajadzētu pietikt ar 10 līdz 15 minūtēm. Šajā laikā katrs komandas dalībnieks izlasa dokumentu un pievieno komentārus un jautājumus, lai atzīmētu neskaidras tēmas. Pēc pārskatīšanas fāzes ADR īpašnieks nolasa un apspriež katru komentāru kopā ar komandu.

Ja komanda atrod rīcības punktus ADR uzlabošanai, ADR stāvoklis paliek **Ierosināts**. ADR īpašnieks formulē darbības un sadarbībā ar komandu katrai darbībai pievieno izpildītāju. Katrs komandas dalībnieks var sniegt ieguldījumu rīcības punktos un tos atrisināt. ADR īpašnieka pienākums ir pārplānot pārskatīšanas procesu.

Komanda var arī nolemt noraidīt ADR. Šādā gadījumā ADR īpašnieks pievieno noraidīšanas iemeslu, lai novērstu turpmākas diskusijas par to pašu tēmu. Īpašnieks maina ADR stāvokli uz **Noraidīts** (Rejected).

Ja komanda ADR apstiprina, īpašnieks pievieno laika zīmogu, versiju un ieinteresēto pušu sarakstu. Pēc tam īpašnieks atjaunina stāvokli uz **Pieņemts** (Accepted).

ADR un lēmumu žurnāls, ko tie veido, atspoguļo komandas pieņemtos lēmumus un nodrošina visu lēmumu vēsturi. Komanda ADR izmanto kā atsauci koda un arhitektūras pārskatos, kur vien iespējams. Papildus koda pārskatu, projektēšanas uzdevumu un īstenošanas uzdevumu veikšanai komandas dalībniekiem jākonsultējas ar ADR par produkta stratēģiskajiem lēmumiem.

Kā laba prakse, katrai programmatūras izmaiņai jāiziet savstarpējie pārskati, un tai nepieciešams vismaz viens apstiprinājums. Koda pārskata laikā koda pārskatītājs var atrast izmaiņas, kas pārkāpj vienu vai vairākus ADR. Šādā gadījumā pārskatītājs lūdz koda izmaiņu autoru atjaunināt kodu un kopīgo saiti uz ADR. Kad autors atjaunina kodu, savstarpējie pārskatītāji to apstiprina un tas tiek sapludināts galvenajā koda bāzē.


## ADR pārskatīšanas process

Komandai pēc ADR pieņemšanas vai noraidīšanas jāuzskata ADR par nemainīgiem dokumentiem. Esoša ADR izmaiņām jāizveido jauns ADR, jāizveido jaunā ADR pārskatīšanas process un jāapstiprina ADR. Ja komanda jauno ADR apstiprina, īpašniekam jāmaina vecā ADR stāvoklis uz **Aizstāts** (Superseded).
