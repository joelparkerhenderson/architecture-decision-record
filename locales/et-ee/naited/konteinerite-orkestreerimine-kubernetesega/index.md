# Arhitektuuriotsuse kirje: konteinerite orkestreerimine Kubernetesega

## Probleemi püstitus 

Peame valima konteinerite orkestreerimise platvormi oma kasvavale pilvepõhiste rakenduste portfellile. Meie praegune pärandplatvormi kasutuselevõtt on liiga aeglane ja ei ole piisavalt agiilne, et meie kasvavate vajadustega sammu pidada. Otsime süsteemi, mis võimaldaks meie teenuseid skaleerida kõige tõhusamal viisil, agiilsust või kasutuslihtsust kahjustamata.

## Kaalutud alternatiivid

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Tehtud otsus

Pärast iga konteinerite orkestreerimise platvormi põhjalikku analüüsi otsustasime võtta Kubernetese kasutusele meie ettevõtte vajaduste parima valikuna. Meie põhjused Kubernetese valimiseks on järgmised:

1. **Skaleeritavus:**  Kubernetese ainulaadne disain sobib suurepäraselt rakenduste skaleerimiseks ja kui meie skaleeritavuse nõuded aja jooksul muutuvad, on Kubernetesel sisseehitatud võime nende muutustega probleemideta toime tulla.

2. **Detsentraliseeritud arhitektuur:**  Kubernetese master-worker topoloogia tagab detsentraliseeritud arhitektuuri, kus puudub üksik tõrkepunkt.

3. **Kogukonna toetus:**  Kubernetesel on suurim ja aktiivseim avatud lähtekoodiga kogukond, mis tähendab, et sellel on suur hulk kaasautoreid, arendajaid ja tarnijaid, mis muudab meil abi saamise ja ressursside leidmise lihtsamaks.

4. **Ökosüsteemi toetus:**  Kubernetesel on kasvav ökosüsteem mitmesuguste kolmandate osapoolte tööriistade, integratsioonidega konteineriregistritega, CI/CD torujuhtmetega, andmesalvestusega ja muuga.

Seetõttu otsustasime võtta Kubernetese kasutusele oma konteinerite orkestreerimise platvormina praeguseks ja lähitulevikuks.

<h6>Allikaviide: see leht on loodud ChatGPT-ga ja seejärel selguse ja vormingu huvides toimetatud.</h6>
