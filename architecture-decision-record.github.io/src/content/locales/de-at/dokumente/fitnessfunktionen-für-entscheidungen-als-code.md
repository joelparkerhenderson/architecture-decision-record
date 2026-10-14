# Fitnessfunktionen für Entscheidungen als Code

Fitnessfunktionen sind objektive, automatisierte Prüfungen, die mit Programmcode geschrieben werden und verifizieren, dass Entscheidungen eingehalten werden.

- Fitnessfunktionen machen Entscheidungen testbar und absicherbar.

- Fitnessfunktionen für Entscheidungen können Qualitätssicherung, regulatorische Prozesse und Governance-Ziele erheblich unterstützen.

## Wie Fitnessfunktionen mit Entscheidungen zusammenhängen

Ein Entscheidungsprotokoll dokumentiert die Entscheidung, während eine Fitnessfunktion die Entscheidung absichert.

- Beispielentscheidung: Wir verwenden Event Sourcing für Auditanforderungen.

- Beispiel-Fitnessfunktion: Wir nutzen den Continuous-Integration-Server, um zu testen, dass alle Zustandsänderungen Ereignisse erzeugen müssen.

## Warum Fitnessfunktionen Entscheidungen helfen

Objektive Messungen: Fitnessfunktionen bestehen oder fallen durch, daher ist die Arbeit sichtbar und klar.

Kontinuierliche Nutzung: Fitnessfunktionen sind Ihre lebendigen Regeln und laufen bei jedem Commit und jedem Build.

Vertrauen beim Refactoring: Fitnessfunktionen fangen Fehler bei Entscheidungsregeln automatisch ab.

Skalierbare Governance: Fitnessfunktionen sichern Standards ab, ohne Engpässe zu schaffen.

## Können Fitnessfunktionen KI nutzen?

Fitnessfunktionen können KI-LLMs für Entscheidungen nutzen, indem sie Fragen zu Ihrer Arbeit stellen,
etwa zu Ihren Plänen, Code, Schemata, APIs und mehr:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Architektur-Unit-Tests

[ArchUnit](https://www.archunit.org/): Architekturregeln von Java-Code mit einem beliebigen einfachen Java-Unit-Test-Framework prüfen.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): Architekturregeln von TypeScript-Code und JavaScript-Code mit Jest, Vitest, Jasmine usw. prüfen.
