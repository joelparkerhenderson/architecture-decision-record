# Architektur-Decisiounsopzeechnung: snake_case vs camelCase fir eng REST-API?

Decisioun: D'snake_case-Nummkonventioun gëtt fir REST-API-Endpunkte benotzt

Zoustand: Akzeptéiert

## Kontext

Bei Nummkonventioune fir REST-APIen gëtt et zwee populär Formater: snake_case a camelCase. Beim snake_case-Format ass all Wuert am Numm duerch Ënnerstécher getrennt, während beim camelCase dat éischt Wuert vum Numm klengbuschtabéiert ass, an déi folgend Wierder hiren éischte Buschtaf grousschreiwe. Dës Decisioun bestëmmt, wéi eng Nummkonventioun fir eng REST-API benotzt soll ginn.

## Decisiounstreiwer

- Konsistenz mat bestoende Nummkonventiounen am Projet

- Liesbarkeet a Kloerheet fir jiddereen, deen un der API schaffe kann

- Ausriichtung u Branchen-Beschte-Praktike fir Nummkonventioune vu REST-APIen

- Einfachheet vun der Ëmsetzung an Ënnerhalt

## Decisioun

D'snake_case-Nummkonventioun gëtt fir REST-API-Endpunkte benotzt. Dës Wiel gëtt vun de folgende Faktore gedriwwen:

1. **Konsistenz**: De Projet benotzt scho d'snake_case-Nummkonventioun fir all Endpunkten, an et wier vun Notzen, dës Konventioun ze behalen, fir Konsistenz am ganze Projet ze garantéieren.

2. **Liesbarkeet a Kloerheet**: D'snake_case-Konventioun ass méi liesbar a méi einfach ze verstoen. D'Ënnerstécher bidden eng kloer Trennung tëscht de Wierder, wat et méi einfach mécht, d'Bedeitung vum Numm ze erfaassen a ze verstoen.

3. **Ausriichtung u Branchen-Beschte-Praktiken**: D'snake_case-Konventioun gëtt an der Branche wäit benotzt a gëllt als Beschte Praxis fir REST-APIen, wouduerch se eng gutt Wiel fir de Projet ass.

4. **Einfachheet vun der Ëmsetzung an Ënnerhalt**: Bei der bestoender Nummkonventioun ze bleiwen ass méi einfach ëmzesetzen an z'erhalen, well all bestoende Code an Dokumentatioun misste aktualiséiert ginn, wann eng nei Konventioun gewielt géif ginn.

## Konsequenzen

Et gëtt potenziell Konsequenzen vun dëser Decisioun. 

* Wann nei Teammemberen, déi dem Projet bäitrieden, mat der snake_case-Nummkonventioun net vertraut sinn, kéint dat zu Verwirrung a Feeler an der Entwécklung féieren. Well snake_case awer eng wäit benotzt Konventioun ass, ass esou e Risiko minimal. 
  
* Wann am Projet aner Tools oder Frameworks benotzt ginn, déi staark op der camelCase-Konventioun baséieren, kann et zousätzlechen Effort erfuerderen, tëscht Nummkonventiounen ze konvertéieren. Et ass awer kee bedeitende Bedenken, well de Projet sech op d'snake_case-Konventioun standardiséiert huet. 
 
Insgesamt féiert d'Decisioun, d'snake_case-Nummkonventioun fir REST-API-Endpunkte ze benotzen, zu engem konsistenten, liesbaren Usaz mat Branchenstandard, deen einfach z'implementéieren an z'erhalen ass.

<h6>Credit: dës Säit gouf vun ChatGPT generéiert, duerno fir Kloerheet a Format editéiert.</h6>
