# Šablona záznamu rozhodnutí pro Důležitá technická rozhodnutí (ITD)

Toto je šablona Důležitých technických rozhodnutí (anglicky Important Technical Decisions, ITD) popsaná v
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

ITD jsou cílenou evolucí ADR, optimalizovanou na rychlost, srozumitelnost
a schválení vedením. Zatímco ADR dokumentuje, co bylo rozhodnuto, ITD je
štíhlý artefakt s rozhodnutím na prvním místě, který činí samotné rozhodnutí přezkoumatelným, aby
ho zainteresované strany mohly rychle prolétnout a snadno zpochybnit. ITD se hodí
pro technická rozhodnutí, která nejsou striktně architektonická, například volbu
modelu, knihovny nebo strategie CI/CD.

V každém souboru ITD napište tyto sekce:

# Název

Uveďte samotné rozhodnutí, ne popis tématu.
Například „Použít Qwen2.5 1.5B Instruct pro překlad na zařízení“.

## Problém

Jedna věta uvádějící, co se snažíme vyřešit.

## Zvažované možnosti

Alternativy, které byly na stole, s vybranou možností **tučně**.

## Odůvodnění

Pouze rozhodující faktory, které vedly k volbě, nikoli vyčerpávající seznam
všech výhod a nevýhod.

## Poznámky

Volitelné. Jakýkoli další kontext, který stojí za zaznamenání, například omezení,
předpoklady nebo odkazy.
