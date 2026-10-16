# Architektūros sprendimo įrašas: API su JSON ar gRPC

## Būsena

Priimtas

## Kontekstas

Projektuojame API naujai paslaugai, kurią naudos keli klientai. Svarstėme du API įgyvendinimo variantus: JSON per HTTP arba gRPC.

JSON per HTTP yra plačiai naudojamas API kūrimo būdas, kurį palaiko daugelis programavimo kalbų ir karkasų. Šis požiūris paprastas, lengvas ir lengvai suprantamas, todėl yra geras pasirinkimas daugeliui projektų. Tačiau jis gali būti mažiau efektyvus nei kiti variantai, ypač apdorojant didelius duomenų kiekius.

gRPC, kita vertus, yra naujesnė technologija, siūlanti efektyvesnį API kūrimo būdą. Duomenims perduoti ji naudoja dvejetainę serializaciją, kuri gali būti greitesnė ir kompaktiškesnė nei JSON. gRPC taip pat palaiko dvikryptį srautinį perdavimą, todėl yra geras pasirinkimas realaus laiko programoms.

## Sprendimas

Apsvarstę abiejų variantų privalumus ir trūkumus, nusprendėme savo API naudoti gRPC. Nors JSON per HTTP yra paprastesnis variantas, manome, kad gRPC pasiūlys efektyvesnį ir lengviau keičiamo mastelio sprendimą mūsų paslaugai. Taip pat numatome, kad mūsų API apdoros didelį duomenų kiekį, o gRPC dvejetainė serializacija šiuo atveju bus efektyvesnė.

Be to, manome, kad gRPC palaikomas dvikryptis srautinis perdavimas bus naudingas realaus laiko programoms, kurias galime sukurti ateityje.

## Pasekmės

Pasirinkę gRPC, API kurti turėsime naudoti kitokį įrankių ir bibliotekų rinkinį nei naudojant JSON per HTTP. Gali prireikti papildomo laiko ir pastangų šioms technologijoms išmokti ir įgyvendinti. Be to, klientai, norintys naudoti mūsų API, turės naudoti su gRPC suderinamas bibliotekas, kurios gali būti ne taip plačiai palaikomos kaip JSON per HTTP bibliotekos.

Tačiau manome, kad gRPC naudojimo privalumai nusveria šiuos galimus trūkumus, ir esame tikri, kad šis sprendimas lems efektyvesnį ir lengviau keičiamo mastelio API.
