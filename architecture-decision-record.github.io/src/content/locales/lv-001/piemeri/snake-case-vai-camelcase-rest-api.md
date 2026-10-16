# Arhitektūras lēmuma ieraksts: snake_case vai camelCase REST API?

Lēmums: REST API galapunktiem tiks izmantota snake_case nosaukumu piešķiršanas konvencija

Statuss: pieņemts

## Konteksts

REST API nosaukumu piešķiršanas konvencijās ir divi populāri formāti: snake_case un camelCase. Snake_case formātā katrs vārds nosaukumā tiek atdalīts ar pasvītrojumiem, savukārt camelCase formātā nosaukuma pirmais vārds ir ar mazajiem burtiem, bet turpmāko vārdu pirmais burts ir liels. Šis lēmums noteiks, kura nosaukumu piešķiršanas konvencija jāizmanto REST API.

## Lēmuma virzītājspēki

- Konsekvence ar esošajām nosaukumu piešķiršanas konvencijām projektā

- Lasāmība un skaidrība ikvienam, kas var strādāt pie API

- Atbilstība nozares labākajām praksēm REST API nosaukumu piešķiršanas konvencijām

- Īstenošanas un uzturēšanas vienkāršība

## Lēmums

REST API galapunktiem tiks izmantota snake_case nosaukumu piešķiršanas konvencija. Šo izvēli virza šādi faktori:

1. **Konsekvence**: projekts jau izmanto snake_case nosaukumu piešķiršanas konvenciju visiem galapunktiem, un būtu lietderīgi saglabāt šo konvenciju, lai nodrošinātu konsekvenci visā projektā.

2. **Lasāmība un skaidrība**: snake_case konvencija ir lasāmāka un vieglāk saprotama. Pasvītrojumi nodrošina skaidru atdalījumu starp vārdiem, atvieglojot nosaukuma parsēšanu un nozīmes izpratni.

3. **Atbilstība nozares labākajām praksēm**: snake_case konvenciju nozarē plaši izmanto, un tā tiek uzskatīta par labāko praksi REST API, padarot to par labu izvēli projektam.

4. **Īstenošanas un uzturēšanas vienkāršība**: esošās nosaukumu piešķiršanas konvencijas saglabāšana ir vieglāk īstenojama un uzturama, jo, izvēloties jaunu konvenciju, būtu jāatjaunina viss esošais kods un dokumentācija.

## Sekas

Šim lēmumam ir iespējamas sekas. 

* Ja jauni komandas locekļi, kas pievienojas projektam, nepārzina snake_case nosaukumu piešķiršanas konvenciju, tas varētu novest pie neskaidrībām un kļūdām izstrādē. Tomēr, tā kā snake_case ir plaši izmantota konvencija, šāds risks ir minimāls. 
  
* Ja projektā tiek izmantoti citi rīki vai ietvari, kas lielā mērā balstīti uz camelCase konvenciju, var būt nepieciešamas papildu pūles, lai pārveidotu starp nosaukumu piešķiršanas konvencijām. Tomēr tas nav būtisks jautājums, jo projekts ir standartizēts uz snake_case konvenciju. 
 
Kopumā lēmums izmantot snake_case nosaukumu piešķiršanas konvenciju REST API galapunktiem nodrošina konsekventu, lasāmu un nozares standartam atbilstošu pieeju, vienlaikus esot viegli īstenojamam un uzturamam.

<h6>Atzinība: šo lapu ģenerēja ChatGPT, pēc tam to rediģēja skaidrības un formāta uzlabošanai.</h6>
