# Rejestr decyzji architektonicznych: orkiestracja kontenerów Kubernetes

## Opis problemu 

Musimy wybrać platformę orkiestracji kontenerów dla naszego rosnącego portfolio aplikacji cloud-native. Nasze obecne wdrożenie na starszej platformie jest zbyt wolne i niewystarczająco zwinne, by nadążać za rosnącymi potrzebami. Szukamy systemu, który pozwoli skalować nasze usługi w możliwie najefektywniejszy sposób bez uszczerbku dla zwinności i łatwości użycia.

## Rozważane alternatywy

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Podjęta decyzja

Po dokładnej analizie każdej platformy orkiestracji kontenerów postanowiliśmy przyjąć Kubernetes jako najlepszą opcję dla potrzeb naszego przedsiębiorstwa. Powody wyboru Kubernetes są następujące:

1. **Skalowalność:**  Unikalna konstrukcja Kubernetes idealnie nadaje się do skalowania aplikacji, a wraz z ewolucją naszych wymagań dotyczących skalowalności Kubernetes ma wbudowaną zdolność sprostania tym zmianom bez problemów.

2. **Zdecentralizowana architektura:**  Topologia master-worker w Kubernetes zapewnia zdecentralizowaną architekturę, w której nie ma pojedynczego punktu awarii.

3. **Wsparcie społeczności:**  Kubernetes ma największą i najaktywniejszą społeczność open source, co oznacza wielu współtwórców, programistów i dostawców, dzięki czemu łatwiej uzyskać pomoc i znaleźć zasoby.

4. **Wsparcie ekosystemu:**  Kubernetes ma rosnący ekosystem z różnymi narzędziami firm trzecich, integracjami z rejestrami kontenerów, potokami CI/CD, magazynami danych i innymi.

Dlatego postanowiliśmy przyjąć Kubernetes jako naszą platformę orkiestracji kontenerów na teraz i najbliższą przyszłość.

<h6>Źródło: ta strona została wygenerowana przez ChatGPT, a następnie zredagowana pod kątem jasności i formatu.</h6>