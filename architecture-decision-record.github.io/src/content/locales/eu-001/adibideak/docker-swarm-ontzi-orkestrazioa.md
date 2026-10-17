# Arkitektura-erabakien erregistroa: Docker Swarm ontzi-orkestrazioa

Erabaki zenbakia: 001

Erabakitzailea: [Zure izena edo kargua]

Data: [Erabakiaren data]

## Testuingurua

Ontzi-orkestrazioko tresna desberdinak aztertzen ari gara gure mikrozerbitzuetan oinarritutako arkitektura kudeatzeko. Kubernetes, Docker Swarm eta Mesosphere DC/OS bezalako soluzio desberdinak ebaluatu ditugu. Hala ere, Docker Swarm-en jartzea erabaki dugu bere sinpletasunagatik, Docker-ekiko integrazioagatik eta barne-karga-orekatzeagatik.

## Erabakia

Docker Swarm gure ontzi-orkestrazioko tresna gisa erabiltzea erabaki dugu. Docker Swarm-ek modu sinple eta intuitiboa eskaintzen du nodo-kluster batean ontzidun aplikazioak kudeatzeko. Gainera, Docker-en oinarritutako gure lehendik dauden lan-fluxuak eta azpiegitura aprobetxatzeko aukera ematen digu. Docker Swarm-ekin, gure aplikazioak erraz hedatu, eskalatu eta kudeatu ditzakegu, eta, aldi berean, barne-karga-orekatzearen abantaila hartu.

## Onurak

- **Sinpletasuna:**  Docker Swarm-ek Docker-en printzipio berberak jarraitzen ditu, beraz ez dago teknologia berri bat ikasi beharrik. Ikaskuntza-kurba nahiko lauak da Docker ezagutzen duten garatzaileentzat.

- **Integrazioa:**  Docker Swarm Docker tresnekin sorbalda-sorbalda integratzen da, hala nola Docker Compose-rekin, eta horrek errazten du gure ontzi eta zerbitzu guztiak leku bakar batetik kudeatzea.

- **Karga-oreka:**  Docker Swarm-ek barne-karga-orekatzea eskaintzen du, gure aplikazioak beti eskuragarri eta klusterrean modu uniformean banatuta daudela ziurtatuz.

- **Eskalagarritasuna:**  Docker Swarm-ek erraz egiten du gure aplikazioak horizontalki eskalatzea klusterretik nodoak gehituz edo kenduz.

- **Erabilgarritasun handia:**  Docker Swarm-ek automatikoki banatzen ditu gure zerbitzuak nodoen artean, nodo-hutsegitea gertatuz gero erabilgarritasun handia ematen duena.

## Arriskuak

- **Funtzionalitate mugatua:**  Docker Swarm-ek Kubernetes edo Mesosphere DC/OS-n aurkitzen diren ezaugarri aurreratu batzuk falta izan ditzake, hala nola eskalatze automatikoa edo auto-sendatzea.

- **Docker-en zentratua:**  Docker Swarm Docker-ekin estu lotuta dago, eta horrek gure malgutasuna mugatu dezake Docker-en oinarritutako soluzioetatik urruntzeko beharra badugu.

- **Heldugabetasuna:**  Docker Swarm teknologia nahiko berria da oraindik, eta egonkortasun-arazoak edo dokumentazioan hutsuneak egon daitezke.

## Alternatibak

- **Kubernetes:**  Kubernetes da gehien erabiltzen den ontzi-orkestrazio plataforma eta ezaugarri aurreratuak eta ekosistema helduagoa eskaintzen ditu. Hala ere, ikaskuntza-kurba aldapatsuagoa du eta gure beharretarako gehiegizkoa izan daiteke.

- **Mesosphere DC/OS:**  Mesosphere DC/OS tresna ahaltsua da, hodei anitzeko euskarria eta datu handien eta AA plataformaren gaitasun natiboak bezalako ezaugarri aurreratuak eskaintzen dituena. Hala ere, adituen ezagutza handia behar du ezartzeko eta gure eskakizunetarako konplexuegia izan daiteke.

## Ondorioa

Arretaz pentsatu ondoren, Docker Swarm gure ontzi-orkestrazioko tresna gisa erabiltzea erabaki dugu. Docker Swarm-ek gure ontzidun aplikazioak kudeatzeko behar dugun sinpletasuna, integrazioa eta barne-karga-orekatzea eskaintzen ditu. Ezaugarri aurreratu batzuk falta izan ditzakeen arren, uste dugu Docker Swarm-en onurak bere arriskuak baino handiagoak direla gure oraingo eskakizunetarako.

<h6>Kreditua: orri hau ChatGPT-k sortu du, eta gero argitasunerako eta formaturako editatu da.</h6>
