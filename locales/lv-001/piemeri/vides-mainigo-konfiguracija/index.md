# Vides mainīgo konfigurācija

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
  * [Sekas ](#sekas)
* [Saistītais](#saistītais)
  * [Saistītie lēmumi](#saistītie-lēmumi)
  * [Saistītās prasības](#saistītās-prasības)
  * [Saistītie artefakti](#saistītie-artefakti)
  * [Saistītie principi](#saistītie-principi)
* [Piezīmes](#piezīmes)


## Kopsavilkums


### Jautājums

Mēs vēlamies, lai mūsu lietojumprogrammas būtu konfigurējamas ārpus artefaktiem/bināriem failiem/pirmkoda, lai viena būvēšana varētu uzvesties atšķirīgi atkarībā no tās izvietošanas vides.

  * Lai to panāktu, mēs vēlamies izmantot vides mainīgo konfigurāciju.

  * Mēs vēlamies pārvaldīt konfigurāciju, izmantojot failus, kurus varam iekļaut versiju kontrolē.

  * Mēs vēlamies nodrošināt dažas izstrādātāja pieredzes ērtības, piemēram, zināt, ko var konfigurēt, un jebkuras attiecīgās noklusējuma vērtības.


### Lēmums

Izvēlējāmies .env failus ar saistīto noklusējuma failu un shēmas failu.


### Statuss

Izlemts. Atvērti jaunu iespēju apsvēršanai, kad tās parādās.


## Detaļas


### Pieņēmumi

Mēs dodam priekšroku lietojumprogrammas koda un vides koda nošķiršanai. Mēs pieņemam, ka lietotnei jādarbojas atšķirīgi dažādās vidēs, piemēram, izstrādes vidē, testa vidē, demonstrācijas vidē, ražošanas vidē utt.

Mēs dodam priekšroku nozares praksei „12 factor app” un vēl vairāk saistītajai praksei „15 factor app”.

Daudzi mūsu iepriekšējie projekti ir izmantojuši `.env` faila vai līdzīgas `.env` direktorijas konvenciju. Tipiska prakse ir turēt tos ārpus versiju kontroles un tā vietā izmantot citu veidu to izvietošanai, versionēšanai un pārvaldībai.


### Ierobežojumi

Mēs vēlamies turēt noslēpumus ārpus mūsu pirmkoda pārvaldības (SCM) versiju kontroles sistēmas (VCS).

Mēs vēlamies censties nodrošināt saderību ar populārām programmatūras ietvarām un bibliotēkām. Piemēram, Node ir modulis „dotenv” vides mainīgo konfigurācijas lasīšanai.


### Pozīcijas

Mēs apsvērām dažas pieejas:

  * Glabāt konfigurāciju lietotnē, piemēram, failā `config.js`.

  * Glabāt konfigurāciju vidē, piemēram, failā `.env`.

  * Iegūt konfigurāciju no zināmas vietas, piemēram, licenču servera.


### Arguments

Mēs izvēlējāmies pieeju ar failu .env, jo:

  * Tā ir populāra, tostarp ekspertu vidū.

  * Tā seko `.env` failu modelim, ko mūsu komandas ir veiksmīgi izmantojušas daudzas reizes daudzos projektos.

  * Tā ir vienkārša. Jo īpaši mēs pagaidām esam pieņēmuši ievērojamos kompromisus, ko redzam, piemēram, revīzijas iespēju trūkumu salīdzinājumā ar licenču servera pieeju.


### Sekas 

Mums jāizdomā veids, kā nošķirt vides mainīgo konfigurāciju, kas ir publiska, no jebkādas noslēpumu pārvaldības.


## Saistītais


### Saistītie lēmumi

Mēs sagaidām, ka visas mūsu lietojumprogrammas izmantos šo pieeju.

Mēs plānosim jaunināt jebkuras mūsu lietojumprogrammas, kas izmanto mazāk spējīgu pieeju, piemēram, cieto kodēšanu binārajā failā vai pirmkodā.

Mēs atstāsim nemainītas jebkuras mūsu lietojumprogrammas, kas izmanto spējīgāku pieeju, piemēram, licencēšanas serveri.


### Saistītās prasības

Mēs pievienosim failiem DevOps iespējas, tostarp kāšus, testus un nepārtraukto integrāciju.

Mums jāapmāca visi izstrādātāju komandas biedri par šo lēmumu.



### Saistītie artefakti

Katrai izvietošanas vietai būs nepieciešams savs .env fails un saistītie faili.


### Saistītie principi

Viegli atgriezenisks.


## Piezīmes


Faila `.env` piemērs:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Faila `.env.defaults` piemērs:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Faila `.env.schema` piemērs tikai ar atslēgām:

```env
NAME
EMAIL
```
