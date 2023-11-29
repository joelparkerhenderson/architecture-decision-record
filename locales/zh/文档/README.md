# Architecture decision record (ADR)

An architecture decision record (ADR) is a document that captures an important architecture decision made along with its context and consequences.

Contents:

- [What is an architecture decision record?](#what-is-an-architecture-decision-record)
- [How to start using ADRs](#how-to-start-using-adrs)
- [How to start using ADRs with tools](#how-to-start-using-adrs-with-tools)
- [How to start using ADRs with git](#how-to-start-using-adrs-with-git)
- [File name conventions for ADRs](#file-name-conventions-for-adrs)
- [Suggestions for writing good ADRs](#suggestions-for-writing-good-adrs)
- [ADR example templates](#adr-example-templates)
- [Teamwork advice for ADRs](#teamwork-advice-for-adrs)
- [For more information](#for-more-information)

Templates:

* [Decision record template by Jeff Tyree and Art Akerman](locales/en/templates/decision-record-template-by-jeff-tyree-and-art-akerman/)
* [Decision record template by Michael Nygard](locales/en/templates/decision-record-template-by-michael-nygard/)
* [Decision record template by EdgeX](locales/en/templates/decision-record-template-by-edgex/)
* [Decision record template for Alexandrian pattern](locales/en/templates/decision-record-template-for-alexandrian-pattern/)
* [Decision record template for business case](locales/en/templates/decision-record-template-for-business-case/)
* [Decision record template of the MADR project](locales/en/templates/decision-record-template-of-the-madr-project/)
* [Decision record template using Planguage](locales/en/templates/decision-record-template-using-planguage/)
* [Decision record template by Paulo Merson](https://github.com/pmerson/ADR-template)
* [Decision record template by Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
* [Translations into more languages](locales/)

Examples:

* [CSS framework](locales/en/examples/css-framework/)
* [Environment variable configuration](locales/en/examples/environment-variable-configuration/)
* [Metrics, monitors, alerts](locales/en/examples/metrics-monitors-alerts/)
* [Microsoft Azure DevOps](locales/en/examples/microsoft-azure-devops/)
* [Monorepo vs multirepo](locales/en/examples/monorepo-vs-multirepo/)
* [Programming languages](locales/en/examples/programming-languages/)
* [Secrets storage](locales/en/examples/secrets-storage/)
* [Timestamp format](locales/en/examples/timestamp-format/)
* [Many more...](locales/en/examples/)

[Translations into more languages](locales/)


<div class="include" data-path="locales/en/what-is-an-architecture-decision-record">

## What is an architecture decision record?

An **architecture decision record** (ADR) is a document that captures an important architectural decision made along with its context and consequences.

An **architecture decision** (AD) is a software design choice that addresses a significant requirement.

An **architecture decision log** (ADL) is the collection of all ADRs created and maintained for a particular project (or organization).

An **architecturally-significant requirement** (ASR) is a requirement that has a measurable effect on a software system’s architecture.

All these are within the topic of **architecture knowledge management** (AKM).

The goal of this document is to provide a fast overview of ADRs, how to create them, and where to look for more information.

Abbreviations:

  * **AD**: architecture decision

  * **ADL**: architecture decision log

  * **ADR**: architecture decision record

  * **AKM**: architecture knowledge management

  * **ASR**: architecturally-significant requirement

</div>

<div class="include" data-path="locales/en/how-to-start-using-adrs">
