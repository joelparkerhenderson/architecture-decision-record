# Rejestr decyzji architektonicznych: snake_case czy camelCase w API REST?

Decyzja: Dla punktów końcowych API REST zostanie użyta konwencja nazewnictwa snake_case

Status: Zaakceptowany

## Kontekst

W konwencjach nazewnictwa API REST są dwa popularne formaty: snake_case i camelCase. W formacie snake_case każde słowo w nazwie jest oddzielone podkreślnikami, a w camelCase pierwsze słowo nazwy jest pisane małymi literami, a kolejne słowa zaczynają się wielką literą. Ta decyzja określi, której konwencji nazewnictwa należy używać w API REST.

## Czynniki decyzji

- Spójność z istniejącymi konwencjami nazewnictwa w projekcie

- Czytelność i jasność dla każdego, kto może pracować nad API

- Zgodność z najlepszymi praktykami branżowymi dla nazewnictwa API REST

- Łatwość wdrożenia i utrzymania

## Decyzja

Dla punktów końcowych API REST zostanie użyta konwencja nazewnictwa snake_case. Ten wybór wynika z następujących czynników:

1. **Spójność**: Projekt już używa konwencji nazewnictwa snake_case dla wszystkich punktów końcowych i warto utrzymać tę konwencję, aby zapewnić spójność w całym projekcie.

2. **Czytelność i jasność**: Konwencja snake_case jest bardziej czytelna i łatwiejsza do zrozumienia. Podkreślniki zapewniają wyraźne oddzielenie słów, co ułatwia analizę i zrozumienie znaczenia nazwy.

3. **Zgodność z najlepszymi praktykami branżowymi**: Konwencja snake_case jest szeroko stosowana w branży i uważana za najlepszą praktykę dla API REST, co czyni ją dobrym wyborem dla projektu.

4. **Łatwość wdrożenia i utrzymania**: Pozostanie przy istniejącej konwencji nazewnictwa jest łatwiejsze we wdrożeniu i utrzymaniu, ponieważ w razie wyboru nowej konwencji trzeba by zaktualizować cały istniejący kod i dokumentację.

## Konsekwencje

Ta decyzja niesie potencjalne konsekwencje. 

* Jeśli nowi członkowie zespołu dołączający do projektu nie znają konwencji nazewnictwa snake_case, może to prowadzić do nieporozumień i błędów w rozwoju. Ponieważ jednak snake_case jest szeroko stosowaną konwencją, takie ryzyko jest minimalne. 
  
* Jeśli w projekcie używane są inne narzędzia lub frameworki silnie oparte na konwencji camelCase, konwersja między konwencjami nazewnictwa może wymagać dodatkowego wysiłku. Nie jest to jednak istotna kwestia, ponieważ projekt ustandaryzował się na konwencji snake_case. 
 
Ogólnie decyzja o użyciu konwencji nazewnictwa snake_case dla punktów końcowych API REST skutkuje spójnym, czytelnym i zgodnym ze standardem branżowym podejściem, a jednocześnie jest łatwa we wdrożeniu i utrzymaniu.

<h6>Źródło: ta strona została wygenerowana przez ChatGPT, a następnie zredagowana pod kątem jasności i formatu.</h6>