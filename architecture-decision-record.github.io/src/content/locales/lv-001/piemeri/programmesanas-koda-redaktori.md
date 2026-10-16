# Arhitektūras lēmuma ieraksts: programmēšanas koda redaktori

## Konteksts

Programmēšanas koda redaktori ir būtisks rīks izstrādātājiem koda rakstīšanai un rediģēšanai. Ir pieejami daudzi koda redaktori, katram no kuriem ir savs funkciju kopums, priekšrocības un trūkumi. Šī ADR mērķis ir dokumentēt arhitektūras lēmumus, kas pieņemti programmēšanas koda redaktoriem.

## Prioritātes

Programmēšanas koda redaktoru arhitektūrai jādod priekšroka šiem aspektiem:

* **Modularitāte**: koda redaktoram jābūt projektētam modulāri, ļaujot izstrādātājiem to pielāgot un paplašināt pēc vajadzības. Tas ļauj izveidot elastīgu arhitektūru, kas var pielāgoties dažādu izstrādātāju un komandu vajadzībām.

* **Veiktspēja**: koda redaktoram jābūt veiktspējīgam un atsaucīgam, ļaujot izstrādātājiem strādāt efektīvi, neaizkavējoties no izmantotā rīka.

* **Lietotāja saskarne**: lietotāja saskarnei jābūt intuitīvai un viegli lietojamai, ļaujot izstrādātājiem koncentrēties uz savu kodu, nevis cīnīties ar redaktoru.

* **Paplašināmība**: koda redaktoram jābūt projektētam tā, lai ļautu viegli paplašināt ar trešo pušu spraudņiem un integrācijām.

* **Saderība**: koda redaktoram jābūt saderīgam ar plašu programmēšanas valodu un tehnoloģiju klāstu, padarot to par noderīgu rīku plašam izstrādātāju lokam.

## Lēmums

Pamatojoties uz šīm prioritātēm, programmēšanas koda redaktoru arhitektūra jāprojektē ar šādām komponentēm:

* **Kodols**: šī komponente nodrošina koda redaktora pamatfunkcionalitāti, piemēram, sintakses izcelšanu, teksta rediģēšanu un failu pārvaldību.

* **UI**: šī komponente nodrošina koda redaktora lietotāja saskarni, tostarp izvēlnes, rīkjoslas un tastatūras īsinājumtaustiņus.

* **Spraudņi**: šī komponente ļauj izstrādātājiem paplašināt koda redaktora funkcionalitāti, instalējot trešo pušu spraudņus. Spraudņi var nodrošināt papildu funkcijas, piemēram, koda pabeigšanu, linting vai atkļūdošanu.

* **Integrācijas**: šī komponente ļauj koda redaktoram integrēties ar citiem rīkiem un tehnoloģijām, piemēram, versiju kontroles sistēmām, būvēšanas sistēmām vai atkļūdošanas rīkiem.

## Pamatojums

Koda redaktora modularitāte ļauj izstrādātājiem to pielāgot un paplašināt pēc vajadzības. Tas ir svarīgi, jo dažādiem izstrādātājiem un komandām ir atšķirīgas vajadzības un darbplūsmas, un elastīga arhitektūra var šīs atšķirības ņemt vērā.

* **Veiktspēja**: izšķiroša, jo izstrādātājiem jāspēj strādāt efektīvi, neaizkavējoties no saviem rīkiem. Veiktspējīgs koda redaktors ir būtisks produktivitātei un var palīdzēt izstrādātājiem saglabāt savu uzmanību un koncentrēšanos.

* **UI**: svarīgs, jo tas ļauj izstrādātājiem koncentrēties uz savu kodu, nevis cīnīties ar redaktoru. Tas var nodrošināt labāku produktivitāti un mazāku izstrādātāju vilšanos.

* **Paplašināmība**: jaudīga, jo tā ļauj koda redaktoru pielāgot dažādām vajadzībām un darbplūsmām. Trešo pušu spraudņi un integrācijas var nodrošināt papildu funkcijas un iespējas, kas nav iekļautas pamata redaktorā.

* **Saderība**: vērtīga, jo tā ļauj koda redaktoru izmantot ar plašu programmēšanas valodu un tehnoloģiju klāstu. Tas padara redaktoru par noderīgāku rīku plašam izstrādātāju lokam.

Kodola, spraudņu, integrāciju un UI komponentes nodrošina skaidru atbildību nošķiršanu un ļauj izveidot modulāru arhitektūru, ko var viegli paplašināt un pielāgot. Šī arhitektūra ir elastīga, veiktspējīga un saderīga ar plašu programmēšanas valodu un tehnoloģiju klāstu, padarot to par noderīgu rīku izstrādātājiem.
