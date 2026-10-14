# Záznam architektonického rozhodnutí: orchestrace kontejnerů Kubernetes

## Popis problému 

Potřebujeme vybrat platformu pro orchestraci kontejnerů pro naše rostoucí portfolio cloud-native aplikací. Naše současné nasazení na staré platformě je příliš pomalé a není dostatečně agilní, aby drželo krok s našimi rostoucími potřebami. Hledáme systém, který nám umožní škálovat naše služby co nejefektivnějším způsobem bez kompromisů v agilitě nebo snadnosti použití.

## Zvažované alternativy

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Učiněné rozhodnutí

Po důkladné analýze každé platformy pro orchestraci kontejnerů jsme se rozhodli přijmout Kubernetes jako nejlepší možnost pro potřeby našeho podniku. Důvody pro volbu Kubernetes jsou následující:

1. **Škálovatelnost:**  Jedinečný design Kubernetes je dokonalý pro škálování aplikací a s tím, jak se naše požadavky na škálovatelnost v čase vyvíjejí, má Kubernetes vestavěnou schopnost těmto změnám bez problémů vyhovět.

2. **Decentralizovaná architektura:**  Topologie master-worker v Kubernetes zajišťuje decentralizovanou architekturu, která zaručuje, že neexistuje jediný bod selhání.

3. **Podpora komunity:**  Kubernetes má největší a nejaktivnější open source komunitu, což znamená velký počet přispěvatelů, vývojářů a dodavatelů, takže je pro nás snazší získat pomoc a najít zdroje.

4. **Podpora ekosystému:**  Kubernetes má rostoucí ekosystém s řadou nástrojů třetích stran, integrací s registry kontejnerů, pipeline CI/CD, úložišti dat a dalšími.

Proto jsme se rozhodli přijmout Kubernetes jako naši platformu pro orchestraci kontejnerů pro současnost a nejbližší budoucnost.

<h6>Zdroj: tuto stránku vygeneroval ChatGPT a poté byla upravena pro přehlednost a formát.</h6>