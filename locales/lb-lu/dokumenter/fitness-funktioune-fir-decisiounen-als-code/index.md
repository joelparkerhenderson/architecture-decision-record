# Fitness-Funktioune fir Decisiounen als Code

Fitness-Funktioune si objektiv automatiséiert Kontrollen, mat Programméiercode geschriwwen, déi verifizéieren, datt Decisiounen agehale ginn.

- Fitness-Funktioune maachen Decisiounen testbar a sécherstellbar.

- Fitness-Funktioune fir Decisioune kënnen d'Qualitéitssécherung, regulatoresch Prozesser a Governance-Zieler staark ënnerstëtzen.

## Wéi Fitness-Funktioune mat Decisiounen zesummenhänken

Eng Decisiounsopzeechnung dokumentéiert d'Decisioun, während eng Fitness-Funktioun d'Decisioun sécherstellt.

- Beispilldecisioun: Mir benotzen Event Sourcing fir Audit-Ufuerderungen.

- Beispill fir eng Fitness-Funktioun: Mir benotzen de Continuous-Integration-Server, fir ze testen, datt all Zoustandsännerung Evenementer muss produzéieren.

## Firwat Fitness-Funktioune Decisioune hëllefen

Objektiv Miessungen: Fitness-Funktioune bestinn oder falen duerch, sou datt d'Aarbecht sichtbar a kloer ass.

Kontinuéierlech Notzung: Fitness-Funktioune sinn Är liewege Reegelen, déi bei all Commit a Build lafen.

Vertrauen fir Refactoring: Fitness-Funktioune fänken automatesch Feeler géint Decisiounsreegele op.

Skaléierbar Governance: Fitness-Funktioune sécheren Standarden of, ouni Flaschenhälser ze schafen.

## Kënnen Fitness-Funktioune AI benotzen?

Fitness-Funktioune kënnen AI-LLMs fir Decisiounen notzen, andeems si Froe fir Är Aarbecht stellen,
zum Beispill fir Är Pläng, Code, Schemaen, APIen a méi:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Unit-Testen vun der Architektur

[ArchUnit](https://www.archunit.org/): Architekturreegele vu Java-Code mat all ganz normalem Java-Unit-Test-Framework iwwerpréiwen.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): Architekturreegele vun TypeScript-Code a JavaScript-Code mat Jest, Vitest, Jasmine, asw. iwwerpréiwen.
