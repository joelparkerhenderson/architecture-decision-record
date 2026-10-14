# Architekturális döntési feljegyzés: Kubernetes konténer-orkesztráció

## Problémafelvetés 

Konténer-orkesztrációs platformot kell választanunk növekvő felhőnatív alkalmazásportfóliónkhoz. A jelenlegi, régebbi platformon futó telepítésünk túl lassú és nem elég agilis ahhoz, hogy lépést tartson növekvő igényeinkkel. Olyan rendszert keresünk, amely lehetővé teszi, hogy szolgáltatásainkat a lehető leghatékonyabb módon skálázzuk az agilitás vagy a használhatóság feladása nélkül.

## Megfontolt alternatívák

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Meghozott döntés

Az egyes konténer-orkesztrációs platformok alapos elemzése után úgy döntöttünk, hogy a Kubernetest vezetjük be vállalati igényeink legjobb lehetőségeként. A Kubernetes választásának okai a következők:

1. **Skálázhatóság:**  A Kubernetes egyedi felépítése tökéletes az alkalmazások skálázásához, és ahogy skálázhatósági követelményeink idővel fejlődnek, a Kubernetes beépített képességgel rendelkezik e változások problémamentes kezelésére.

2. **Decentralizált architektúra:**  A Kubernetes master-worker topológiája decentralizált architektúrát biztosít, amely garantálja, hogy nincs egyetlen hibapont.

3. **Közösségi támogatás:**  A Kubernetesnek van a legnagyobb és legaktívabb nyílt forráskódú közössége, ami azt jelenti, hogy sok közreműködője, fejlesztője és szállítója van, megkönnyítve a segítség és források megtalálását.

4. **Ökoszisztéma-támogatás:**  A Kubernetesnek növekvő ökoszisztémája van harmadik féltől származó eszközök sokaságával, integrációkkal konténer-regiszterekkel, CI/CD-folyamatokkal, adattárolással és mással.

Ezért úgy döntöttünk, hogy a Kubernetest vezetjük be konténer-orkesztrációs platformként a jelenre és a közvetlen jövőre.

<h6>Forrás: ezt az oldalt a ChatGPT generálta, majd az érthetőség és a formázás érdekében szerkesztették.</h6>