# Laika zīmoga formāts

Saturs:

* [Kopsavilkums](#kopsavilkums)
  * [Jautājums](#jautājums)
  * [Lēmums](#lēmums)
  * [Statuss](#statuss)
* [Detaļas](#detaļas)
  * [Pieņēmumi](#pieņēmumi)
  * [Ierobežojumi](#ierobežojumi)
  * [Pozīcijas](#pozīcijas)
  * [Arguments](#arguments)
  * [Sekas](#sekas)
* [Saistītais](#saistītais)
  * [Saistītie lēmumi](#saistītie-lēmumi)
  * [Saistītās prasības](#saistītās-prasības)
  * [Saistītie artefakti](#saistītie-artefakti)
  * [Saistītie principi](#saistītie-principi)
* [Piezīmes](#piezīmes)


## Kopsavilkums


### Jautājums

Mēs vēlamies varēt izsekot, kad notiek lietas, izmantojot laika zīmogus un konsekventu laika zīmoga formātu, kas labi darbojas visās mūsu sistēmās un trešo pušu sistēmās.

Mēs mijiedarbojamies ar sistēmām, kurām ir dažādi laika zīmogu formāti:

* JSON ziņojumiem nav dabiska laika zīmoga formāta, tāpēc mums jāizvēlas, kā pārveidot laika zīmogu par virkni un virkni par laika zīmogu, t. i., kā serializēt/deserializēt.

* Dažas lietojumprogrammas ir iestatītas izmantot vietējo laiku, nevis UTC laiku. Tas var būt ērti projektiem, kuriem jāpielāgojas vietējam laikam, piemēram, projektiem, kas ierosina notikumus, kuru pamatā ir vietējais laiks.

* Dažām sistēmām ir dažādas laika precizitātes vajadzības un iespējas, piemēram, izmantojot sekunžu, milisekunžu vai nanosekunžu laika izšķirtspēju. Piemēram, Linux operētājsistēmas komanda `date` izmanto noklusējuma laika precizitāti sekundēs, savukārt Nasdaq biržai vajadzīga noklusējuma laika precizitāte nanosekundēs.


### Lēmums

Mēs izvēlamies laika zīmoga standarta formātu ISO 8601 ar nanosekunžu precizitāti, konkrēti „YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ”.

Formāts parāda gadu, mēnesi, dienu, stundu, minūti, sekundi, nanosekundes un Zulu laika joslu, saukto arī par UTC, GMT.


### Statuss

Izlemts.


## Detaļas


### Pieņēmumi

Mums jāapstrādā šīs laika zīmogu teksta virknes, jāpārveido no laika zīmoga uz virkni (saukts arī par serializēšanu) un jāpārveido no virknes uz laika zīmogu (saukts arī par deserializēšanu).

Mēs vēlamies formātu, kuru kopumā ir viegli lietot, viegli pārveidot un cilvēkam viegli lasīt.

Mēs vēlamies saderību ar plašu ārējo sistēmu klāstu, ko mēs nevaram kontrolēt, piemēram, analītikas sistēmām, datubāzu sistēmām, finanšu sistēmām.


### Ierobežojumi

Dažām sistēmām ir laika precizitātes ierobežojumi. Piemēram, macOS operētājsistēmas komanda `date` var izdrukāt laika precizitāti sekundēs, bet ne nanosekundēs.


### Pozīcijas

Mēs apsvērām vairākas iespējas:

* Unix laikmets (epoch), t. i., viens pieaugošs skaitlis.

* Kodolīgs teksta formāts „YYYYMMDDTHHMMSSNNNNNNNNN”.

* Vietējās laika joslas izmantošana pret UTC laika joslu.


### Arguments

Tipiskai lietošanai mēs vērtējam cilvēkiem vieglu lasīšanu/rakstīšanu vairāk nekā neapstrādātu ātrumu/izmēru.

Tipiskai lietošanai mēs vēlamies formātu, kas labi darbojas mašīnu sistēmās un arī labi darbojas manuāli, piemēram, rakstot paraugu datus, lasot JSON izvadi, meklējot ar grep žurnāla failā utt.

Netipiskai lietošanai, piemēram, augstas veiktspējas skaitļošanai, mēs sagaidām, ka vēlēsimies optimizēt jebkuru izvēlēto teksta formātu, pārveidojot tekstu ātrākā formātā, piemēram, programmēšanas valodas iebūvētā datuma objekta tipā. Tāpēc teksta formāts HPC nav nozīmīgs.


### Sekas

Mūsu dažādās teksta sistēmas un laika sistēmas konverģēs uz šo formātu.


## Saistītais


### Saistītie lēmumi

Mēs varētu vēlēties ātru/vieglu veidu, kā izsekot arī laika starpībām, sauktām par ilgumiem. Tās ir vienkāršas ar Unix laikmeta laika zīmogiem.


### Saistītās prasības

Mēs varētu vēlēties pielāgot savu lēmumu, piem., ja mums ir saistīta prasība konkrēta veida žurnāla ziņojuma zīmogam, piemēram, Splunk, Sumo, ELK utt.


### Saistītie artefakti

Valodu formatētāji un parsētāji:

  * [date-fns: moderna JavaScript datuma utilītu bibliotēka](https://date-fns.org/)
  * [Crono: datuma un laika bibliotēka Rust](https://github.com/chronotope/chron)
  
Rosetta Code piemēri:

  * [Sistēmas laiks](https://www.rosettacode.org/wiki/System_time)
  * [Datuma formāts](https://www.rosettacode.org/wiki/Date_format)
  * [Laikmeta (epoch) parādīšana](https://www.rosettacode.org/wiki/Show_the_epoch)

SixArm piemēri:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Saistītie principi

Viegli atgriezenisks. Mēs varam diezgan viegli pāriet uz citu formātu, piemēram, Unix laikmetu.

Atlikt priekšlaicīgu optimizāciju. Tipiskai lietošanai mums daudz nerūp pāris papildu rakstzīmes, piemēram, formāts, kas izmanto domuzīmes un kolus.


## Piezīmes

Šeit pievienojiet piezīmes.
