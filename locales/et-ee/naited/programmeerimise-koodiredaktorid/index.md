# Arhitektuuriotsuse kirje: programmeerimise koodiredaktorid

## Kontekst

Programmeerimise koodiredaktorid on arendajatele koodi kirjutamiseks ja redigeerimiseks hädavajalik tööriist. Saadaval on arvukalt koodiredaktoreid, igaühel oma funktsioonide, eeliste ja puuduste komplekt. Selle ADR-i eesmärk on dokumenteerida programmeerimise koodiredaktorite jaoks tehtud arhitektuuriotsused.

## Prioriteedid

Programmeerimise koodiredaktorite arhitektuur peaks seadma esikohale järgmise:

* **Modulaarsus**: koodiredaktor tuleks disainida modulaarselt, võimaldades arendajatel seda vajaduse korral kohandada ja laiendada. See võimaldab paindlikku arhitektuuri, mis suudab kohaneda erinevate arendajate ja meeskondade vajadustega.

* **Jõudlus**: koodiredaktor peaks olema jõudlusel ja reageeriv, võimaldades arendajatel tõhusalt töötada, ilma et neid kasutatav tööriist aeglustaks.

* **Kasutajaliides**: kasutajaliides peaks olema intuitiivne ja hõlpsasti kasutatav, võimaldades arendajatel keskenduda oma koodile, mitte redaktoriga maadelda.

* **Laiendatavus**: koodiredaktor tuleks disainida nii, et seda saaks hõlpsasti laiendada kolmandate osapoolte pluginate ja integratsioonidega.

* **Ühilduvus**: koodiredaktor peaks ühilduma laia valiku programmeerimiskeelte ja tehnoloogiatega, muutes selle kasulikuks tööriistaks laiale arendajate ringile.

## Otsus

Nende prioriteetide põhjal tuleks programmeerimise koodiredaktorite arhitektuur disainida järgmiste komponentidega:

* **Tuum**: see komponent pakub koodiredaktori põhifunktsionaalsust, nagu süntaksi esiletõstmine, tekstiredigeerimine ja failihaldus.

* **UI**: see komponent pakub koodiredaktori kasutajaliidest, sealhulgas menüüsid, tööriistaribasid ja kiirklahve.

* **Pluginad**: see komponent võimaldab arendajatel koodiredaktori funktsionaalsust laiendada, paigaldades kolmandate osapoolte pluginaid. Pluginad võivad pakkuda lisafunktsioone, nagu koodi täiendamine, linting või silumine.

* **Integratsioonid**: see komponent võimaldab koodiredaktoril integreeruda teiste tööriistade ja tehnoloogiatega, nagu versioonihaldussüsteemid, ehitussüsteemid või silumistööriistad.

## Põhjendus

Koodiredaktori modulaarsus võimaldab arendajatel seda vajaduse korral kohandada ja laiendada. See on oluline, sest erinevatel arendajatel ja meeskondadel on erinevad vajadused ja töövood ning paindlik arhitektuur suudab neid erinevusi arvestada.

* **Jõudlus**: ülioluline, sest arendajad peavad suutma tõhusalt töötada, ilma et nende tööriistad neid aeglustaksid. Jõudlusel koodiredaktor on tootlikkuse jaoks hädavajalik ja võib aidata arendajatel säilitada keskendumist ja kontsentratsiooni.

* **UI**: oluline, sest see võimaldab arendajatel keskenduda oma koodile, mitte redaktoriga maadelda. See võib viia parema tootlikkuse ja vähema frustratsioonini arendajate jaoks.

* **Laiendatavus**: võimas, sest see võimaldab koodiredaktorit erinevatele vajadustele ja töövoogudele kohandada. Kolmandate osapoolte pluginad ja integratsioonid võivad pakkuda lisafunktsioone ja võimalusi, mida tuumredaktor ei sisalda.

* **Ühilduvus**: väärtuslik, sest see võimaldab koodiredaktorit kasutada laia valiku programmeerimiskeelte ja tehnoloogiatega. See teeb redaktorist kasulikuma tööriista laiale arendajate ringile.

Tuuma-, plugina-, integratsiooni- ja UI-komponendid pakuvad selget vastutusalade eraldamist ning võimaldavad modulaarset arhitektuuri, mida saab hõlpsasti laiendada ja kohandada. See arhitektuur on paindlik, jõudlusel ja ühildub laia valiku programmeerimiskeelte ja tehnoloogiatega, muutes selle arendajatele kasulikuks tööriistaks.
