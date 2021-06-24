<!--
  * browser: architecture-decision-record
  * tracker: 2bd6622ec3beeeddd8ff55cf0ccf2efc
  * version: 2.0.0
  * updated: 2021-05-19T18:56:40Z
  * contact: Joel Parker Henderson (http://joelparkerhenderson.com)
  * options: commentable
-->

# Architecture decision record (ADR)

An architectural decision record (ADR) is a document that captures an important architectural decision made along with its context and consequences.

Contents:

* [What is an architecture decision record?](#what-is-an-architecture-decision-record)
* [How to start using ADRs](#how-to-start-using-adrs)
* [How to start using ADRs with tools](#how-to-start-using-adrs-with-tools)
* [How to start using ADRs with git](#how-to-start-using-adrs-with-git)
* [ADR file name conventions](#adr-file-name-conventions)
* [Suggestions for writing good ADRs](#suggestions-for-writing-good-adrs)
* [ADR example templates](#adr-example-templates)
* [Teamwork advice](#teamwork-advice)
* [For more information](#for-more-information)

Templates:

* [Decision record template by Jeff Tyree and Art Akerman](templates/decision-record-template-by-jeff-tyree-and-art-akerman/index.md)
* [Decision record template by Michael Nygard](templates/decision-record-template-by-michael-nygard/index.md)
* [Decision record template for Alexandrian pattern](templates/decision-record-template-for-alexandrian-pattern/index.md)
* [Decision record template for business case](templates/decision-record-template-for-business-case/index.md)
* [Decision record template for MADR](templates/decision-record-template-madr/index.md)
* [Decision record template using Planguage](templates/decision-record-template-using-planguage/index.md)

Examples:

* [CSS framework](examples/css-framework/index.md)
* [Environment variable configuration](examples/environment-variable-configuration/index.md)
* [Metrics, monitors, alerts](examples/metrics-monitors-alerts/index.md)
* [Microsoft Azure DevOps](examples/microsoft-azure-devops/index.md)
* [Monorepo vs multirepo](examples/monorepo-vs-multirepo/index.md)
* [Programming languages](examples/programming-languages/index.md)
* [Secrets storage](examples/secrets-storage/index.md)
* [Timestamp format](examples/timestamp-format/index.md)


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

  * Group decision making is an active research topic.

Decision documentation:

  * Many templates and tools for decision capturing exist.

  * See agile communities, e.g. M. Nygard's ADRs.

  * See traditional software engineering and architecture design processes, e.g. table layouts suggested by IBM UMF and by Tyree and Akerman from CapitalOne.

Decision guidance:

  * The steps above are adopted from the Wikipedia entry on [Architectural Decision](https://en.wikipedia.org/wiki/Architectural-decision)

  * A number of decision making techniques exists, both general ones and software and software architecture specific ones, for instance, dialogue mapping.


## How to start using ADRs with tools

You can start using ADRs with tools any way you want.

For example:

  * If you like using Google Drive and online editing, then you can create a Google Doc, or Google Sheet.

  * If you like use source code version control, such as git, then you can create a file for each ADR.

  * If you like using project planning tools, such as Atlassian Jira, then you can use the tool's planning tracker.

  * If you like using wikis, such as MediaWiki, then you can create an ADR wiki.


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


## ADR file name conventions

If you choose to create your ADRs using typical text files, then you may want to come up with your own ADR file name convention.

We prefer to use a file name convention that has a specific format.

Examples:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Our file name convention:

  * The name has a present tense imperative verb phrase. This helps readability and matches our commit message format.

  * The name uses lowercase and dashs (same as this repo). This is a balance of readability and system usability.

  * The extension is markdown. This can be useful for easy formatting.


## Suggestions for writing good ADRs

Characteristics of a good ADR:

  * Point in Time - Identify when the AD was made

  * Rationality - Explain the reason for making the particular AD

  * Immutable record - The decisions made in a previously published ADR should not be altered

  * Specificity - Each ADR should be about a single AD

Characteristics of a good "Context" section in an ADR:

  * Explain your organization's situation and business priorities

  * Include rationale and considerations based on social and skills makeups of your teams

Characteristics of good "Consequences" section in an ADR:

  * Right approach - "We need to start doing X instead of Y"

  * Wrong approach - Do not explain the AD in terms of "Pros" and "Cons" of having made the particular AD

A new ADR may take the place of a previous ADR:

  * When an AD is made that replaces or invalidates a previous ADR, a new ADR should be created


## ADR example templates

ADR example templates that we have collected on the net:

  * [ADR template by Michael Nygard](templates/decision-record-template-by-michael-nygard/index.md) (simple and popular)

  * [ADR template by Jeff Tyree and Art Akerman](templates/decision-record-template-by-jeff-tyree-and-art-akerman/index.md) (more sophisticated)

  * [ADR template for Alexandrian pattern](templates/decision-record-template-for-alexandrian-pattern/index.md) (simple with context specifics)

  * [ADR template for business case](templates/decision-record-template-for-business-case/index.md) (more MBA-oriented, with costs, SWOT, and more opinions)

  * [ADR template MADR](templates/decision-record-template-madr/index.md) (more Markdown)

  * [ADR template using Planguage](templates/decision-record-template-using-planguage/index.md) (more quality assurance oriented)


## Teamwork advice

If you're considering using decision records with your team, then here's some advice that we've learned by working with many teams.

You have an opportunity to lead your teammates, by talking together about the "why", rather than mandating the "what". For example, decision records are a way for teams to think smarter and communicate better; decision records are not valuable if they're just an after-the-fact forced paperwork requirement.

Some teams much prefer the name "decisions" over the abbreviation "ADRs". When some teams use the directory name "decisions", then it's as if a light bulb turns on, and the team starts putting more information into the directory, such as vendor decisions, planning decisions, scheduling decisions, etc. All of these kinds of information can use the same template. We hypothesize that people learn faster with words ("decisions") over abbreviations ("ADRs"), and people are more motivated to write work-in-progress docs when the word "record" is removed, and also some developers and some managers dislike the word "architecture".

In theory, immutability is ideal. In practice, mutability has worked better for our teams. We insert the new info the existing ADR, with a date stamp, and a note that the info arrived after the decision. This kind of approach leads to a "living document" that we all can update. Typical updates are when we get information thanks to new teammates, or new offerings, or real-world results of our usages, or after-the-fact third-party changes such as vendor capabilties, pricing plans, license agreements, etc.


## For more information

Introduction:

  * [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

  * [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Templates:

  * [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

  * [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/) - provided by the [adr GitHub organization](https://adr.github.io/)

  * [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

In-depth:

  * [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

  * [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

  * [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

  * [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

  * [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

  * [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

Tools:

  * [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

  * [Command line tools with python by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

Examples:

  * [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

See also:

  * REMAP (Representation and Maintenance of Process Knowledge)

  * DRL (Decision Representation Language)

  * IBIS (Issue-Based Information System)

  * QOC (Questions, Options, and Criteria)

  * IBM’s e-Business Reference Architecture Framework
