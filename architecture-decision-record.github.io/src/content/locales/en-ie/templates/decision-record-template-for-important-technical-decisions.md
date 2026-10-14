# Decision record template for Important Technical Decisions (ITDs)

This is the Important Technical Decisions (ITD) template described in
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

ITDs are a focused evolution of ADRs, optimised for speed, clarity, and
executive validation. Where an ADR documents what was decided, an ITD is a
lean, decision-first artifact that makes the decision itself reviewable, so
stakeholders can scan it quickly and challenge it easily. ITDs are well suited
to technical decisions that are not strictly architectural, such as choosing a
model, a library, or a CI/CD strategy.

In each ITD file, write these sections:

# Title

State the decision itself, not a description of the topic.
For example, "Use Qwen2.5 1.5B Instruct for on-device translation".

## The Problem

One sentence stating what we are trying to solve.

## Options Considered

The alternatives that were on the table, with the selected option in **bold**.

## Rationale

Only the decisive factors that led to the choice, not an exhaustive list of
every pro and con.

## Notes

Optional. Any additional context worth recording, such as constraints,
assumptions, or links.
