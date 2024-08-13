<!--
  browser: architecture-decision-record
  tracker: 2bd6622ec3beeeddd8ff55cf0ccf2efc
  version: 3.0.0
  updated: 2023-11-07T20:42:12Z
  contact: Joel Parker Henderson (http://joelparkerhenderson.com)
  options: commentable
-->

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

## How to start using ADRs

To start using ADRs, talk with your teammates about these areas.

Decision identification:

  * How urgent and how important is the AD?

  * Does it have to be made now, or can it wait until more is known?

  * Both personal and collective experience, as well as recognized design methods and practices, can assist with decision identification.

  * Ideally maintain a decision todo list that complements the product todo list.

Decision making:

  * A number of decision making techniques exists, both general ones and software architecture specific ones, for instance, dialogue mapping.

  * Group decision making is an active research topic.

Decision enactment and enforcement:

  * ADs are used in software design; hence they have to be communicated to, and accepted by, the stakeholders of the system that fund, develop, and operate it.

  * Architecturally evident coding styles and code reviews that focus on architectural concerns and decisions are two related practices.

  * ADs also have to be (re-)considered when modernizing a software system in software evolution.

Decision sharing (optional):

  * Many ADs recur across projects.

  * Hence, experiences with past decisions, both good and bad, can be valuable reusable assets when employing an explicit knowledge management strategy.

Decision documentation:

  * Many templates and tools for decision capturing exist.

  * See agile communities, e.g. M. Nygard's ADRs.

  * See traditional software engineering and architecture design processes, e.g. table layouts suggested by IBM UMF and by Tyree and Akerman from CapitalOne.

For more:

  * The steps above are adopted from the Wikipedia entry on [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

</div>

<div class="include" data-path="locales/en/how-to-start-using-adrs-with-tools">

## How to start using ADRs with tools

You can start using ADRs with tools any way you want.

For example:

  * If you like using Google Drive and online editing, then you can create a Google Doc, or Google Sheet.

  * If you like use source code version control, such as git, then you can create a file for each ADR.

  * If you like using project planning tools, such as Atlassian Jira, then you can use the tool's planning tracker.

  * If you like using wikis, such as MediaWiki, then you can create an ADR wiki.

</div>

<div class="include" data-path="locales/en/how-to-start-using-ADRs-with-git">

## How to start using ADRs with git

If you like using git version control, then here is how we like to start using ADRs with git for a typical software project with source code.

Create a directory for ADR files:

```sh
$ mkdir adr
```

For each ADR, create a text file, such as `database.txt`:

```sh
$ vi database.txt
```

Write anything you want in the ADR. See the templates in this repository for ideas.

Commit the ADR to your git repo.

</div>

<div class="include" data-path="locales/en/file-name-conventions-for-adrs">

## File name conventions for ADRs

If you choose to create your ADRs using typical text files, then you may want to come up with your own ADR file name convention.

We prefer to use a file name convention that has a specific format.

Examples:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Our file name convention:

  * The name has a present tense imperative verb phrase. This helps readability and matches our commit message format.

  * The name uses lowercase and dashes (same as this repo). This is a balance of readability and system usability.

  * The extension is markdown. This can be useful for easy formatting.

</div>

<div class="import" data-path="locales/en/suggestions-for-writing-good-adrs">

## Suggestions for writing good ADRs

Characteristics of a good ADR:

  * Rationale: Explain the reasons for doing the particular AD. This can include the context (see below), pros and cons of various potential choices, feature comparisons, cost/benefit discussions, and more.

  * Specific: Each ADR should be about one AD, not multiple ADs.

  * Timestamps: Identify when each item in the ADR is written. This is especially important for aspects that may change over time, such as costs, schedules, scaling, and the like.

  * Immutable: Don't alter existing information in an ADR. Instead, amend the ADR by adding new information, or supersede the ADR by creating a new ADR.

Characteristics of a good "Context" section in an ADR:

  * Explain your organization's situation and business priorities.

  * Include rationale and considerations based on social and skills makeups of your teams.

  * Include pros and cons that are relevant, and describe them in terms that align with your needs and goals.

Characteristics of good "Consequences" section in an ADR:

  * Explain what follows from making the decision. This can include the effects, outcomes, outputs, follow ups, and more.

  * Include information about any subsequent ADRs. It's relatively common for one ADR to trigger the need for more ADRs, such as when one ADR makes a big overarching choice, which in turn creates needs for more smaller decisions.

  * Include any after-action review processes. It's typical for teams to review each ADR one month later, to compare the ADR information with what's happened in actual practice, in order to learn and grow.

A new ADR may take the place of a previous ADR:

  * When an AD is made that replaces or invalidates a previous ADR, then a new ADR should be created

</div>

## ADR example templates

ADR example templates that we have collected on the net:

  * [ADR template by Michael Nygard](locales/en/templates/decision-record-template-by-michael-nygard/) (simple and popular)

  * [ADR template by Jeff Tyree and Art Akerman](locales/en/templates/decision-record-template-by-jeff-tyree-and-art-akerman/) (more sophisticated)

  * [ADR template for Alexandrian pattern](locales/en/templates/decision-record-template-for-alexandrian-pattern/) (simple with context specifics)

  * [ADR template for business case](locales/en/templates/decision-record-template-for-business-case/) (more MBA-oriented, with costs, SWOT, and more opinions)

  * [ADR template of the Markdown Any Decision Records (MADR) project](locales/en/templates/decision-record-template-of-the-madr-project/) (both simple and elaborate version; the latter emphasizes options and their pros and cons)

  * [ADR template using Planguage](locales/en/templates/decision-record-template-using-planguage/) (more quality assurance oriented)

<div class="import" data-path="locales/en/teamwork-advice-for-adrs">

## Teamwork advice for ADRs

If you're considering using decision records with your team, then here's some advice that we've learned by working with many teams.

You have an opportunity to lead your teammates, by talking together about the "why", rather than mandating the "what". For example, decision records are a way for teams to think smarter and communicate better; decision records are not valuable if they're just an after-the-fact forced paperwork requirement.

Some teams much prefer the name "decisions" over the abbreviation "ADRs". When some teams use the directory name "decisions", then it's as if a light bulb turns on, and the team starts putting more information into the directory, such as vendor decisions, planning decisions, scheduling decisions, etc. All of these kinds of information can use the same template. We hypothesize that people learn faster with words ("decisions") over abbreviations ("ADRs"), and people are more motivated to write work-in-progress docs when the word "record" is removed, and also some developers and some managers dislike the word "architecture".

In theory, immutability is ideal. In practice, mutability has worked better for our teams. We insert the new info the existing ADR, with a date stamp, and a note that the info arrived after the decision. This kind of approach leads to a "living document" that we all can update. Typical updates are when we get information thanks to new teammates, or new offerings, or real-world results of our usages, or after-the-fact third-party changes such as vendor capabilities, pricing plans, license agreements, etc.

</div>

## For more information

Introduction:

  * [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

  * [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Templates:

  * [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

  * [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

  * [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

In-depth:

  * [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

  * [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

  * [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

  * [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

  * [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

  * [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

  * [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

 * [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

* [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

Tools:

  * [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

  * [Command line tools with python by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

  * [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

Company-Specific Guidance:

  * [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

 * [GitHub: ADR GitHub organization](https://adr.github.io/)

 * [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Examples:

  * [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

See also:

  * REMAP (Representation and Maintenance of Process Knowledge)

  * DRL (Decision Representation Language)

  * IBIS (Issue-Based Information System)

  * QOC (Questions, Options, and Criteria)

  * IBM’s e-Business Reference Architecture Framework
