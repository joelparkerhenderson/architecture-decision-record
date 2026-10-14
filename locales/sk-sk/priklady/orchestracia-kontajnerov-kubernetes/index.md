# Záznam architektonického rozhodnutia: orchestrácia kontajnerov Kubernetes

## Opis problému 

Musíme vybrať platformu na orchestráciu kontajnerov pre naše rastúce portfólio cloud-native aplikácií. Naše súčasné nasadenie starej platformy je príliš pomalé a nedostatočne agilné, aby držalo krok s našimi rastúcimi potrebami. Hľadáme systém, ktorý nám umožní škálovať naše služby čo najefektívnejším spôsobom bez kompromisov v agilite alebo jednoduchosti používania.

## Zvažované alternatívy

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Prijaté rozhodnutie

Po dôkladnej analýze každej platformy na orchestráciu kontajnerov sme sa rozhodli prijať Kubernetes ako najlepšiu možnosť pre potreby nášho podniku. Naše dôvody na výber Kubernetes sú nasledovné:

1. **Škálovateľnosť:**  Jedinečný dizajn Kubernetes je ideálny na škálovanie aplikácií a keďže sa naše požiadavky na škálovateľnosť v čase vyvíjajú, Kubernetes má vstavanú schopnosť tieto zmeny zvládnuť bez problémov.

2. **Decentralizovaná architektúra:**  Topológia master-worker v Kubernetes zaisťuje decentralizovanú architektúru, ktorá zaručuje, že neexistuje jediný bod zlyhania.

3. **Podpora komunity:**  Kubernetes má najväčšiu a najaktívnejšiu open source komunitu, čo znamená, že má veľký počet prispievateľov, vývojárov a dodávateľov, vďaka čomu je pre nás jednoduchšie získať pomoc a nájsť zdroje.

4. **Podpora ekosystému:**  Kubernetes má rastúci ekosystém s rôznymi nástrojmi tretích strán, integráciami s registrami kontajnerov, CI/CD pipeline, ukladaním dát a ďalšími.

Preto sme sa rozhodli prijať Kubernetes ako našu platformu na orchestráciu kontajnerov pre súčasnosť a najbližšiu budúcnosť.

<h6>Zdroj: túto stránku vygeneroval ChatGPT a potom bola upravená kvôli prehľadnosti a formátu.</h6>