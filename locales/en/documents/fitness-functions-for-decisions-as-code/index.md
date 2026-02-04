# Fitness functions for decisions as code

Fitness functions are objective automated checks, written with programming code, that verify decisions are being maintained.

- Fitness functions make decisions testable and assurable.

- Fitness functions for decisions can greatly help quality assurance, regulatory processes, and governance goals.

## How fitness functions connect to decisions

A decision record documents the decision, while a fitness function assures the decision.

- Example decision: We use event sourcing for audit requirements.

- Example fitness function: We use the continuous integration server to test that all state changes must produce events.

## Why fitness functions help decisions

Objective measurements: Fitness functions pass or fail, so work is visible and clear.

Continuous use: Fitness functions are your living rules, run on every commit and build.

Confidence to refactor: Fitness functions automatically catch decision rule errors.

Scalable governance: Fitness functions assure standards without creating bottlenecks.

## Can fitness functions use AI?

Fitness functions can leverage AI LLMs for decisions by asking questions for your work,
such as your plans, code, schemas, APIs, and more:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our wor to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Architecture unit testing

[ArchUnit](https://www.archunit.org/): check architecture rules of Java code by using any plain Java unit test framework.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): check architecture rules of TypeScript code and JavaScript code by using Jest, Vitest, Jasmine, etc.
