<!--
  * browser: architecture-decision-record
  * tracker: 2bd6622ec3beeeddd8ff55cf0ccf2efc
  * version: 1.0.0
  * updated: 2018-02-24T03:35:50Z
  * contact: Joel Parker Henderson (http://joelparkerhenderson.com)
  * options: commentable
-->

# Architecture Decision Record (ADR)

An architectural decision record (ADR) is a document that permanently records a specific software design choice made at a certain point in time, such as by writing notes, or logging information.

Contents:
* [What is an Architecture Decision Record?](#what-is-an-architecture-decision-record)
* [ADR example templates](#adr-example-templates)
* [How to start using ADRs](#how-to-start-using-adrs)
* [How to start using ADRs with tools](#how-to-start-using-adrs-with-tools)
* [How to start using ADRs with git](#how-to-start-using-adrs-with-git)
* [ADR file name conventions](#adr-file-name-conventions)
* [Rules of the ADR road](#rules-of-the-adr-road)
* [Organizations and Projects using ADRs](#organizations-and-projects-using-adrs)
* [Contributing](#contributing)
* [Sources](#sources)


## What is an Architecture Decision Record?

An **architectural decision record** (ADR) is a document that permanently records a specific software design choice made at a certain point in time, such as by writing notes, or logging information.

An **architectural decision** (AD) is a software design choice that addresses a significant requirement.

An **architecturally significant requirement** (ASR) is a requirement that has a measurable effect on a software system’s architecture.

All these are within the topic of **architectural knowledge management** (AKM).

The goal of this document is to provide a fast overview of ADRs, how to create them, and where to look for more information.


## ADR example templates

ADR example templates that we have collected on the net:

* [ADR template by Michael Nygard](adr_template_by_michael_nygard.md) (simple and popular)

* [ADR template by Jeff Tyree and Art Akerman](adr_template_by_jeff_tyree_and_art_akerman.md) (more sophisticated)

* [ADR template for Alexandrian pattern](adr_template_for_alexandrian_pattern.md) (simple with context specifics)

* [ADR template for business case](adr_template_for_business_case.md) (more MBA-oriented, with costs, SWOT, and more opinions)

* [ADR template MADR](adr_template_madr.md) (focuses on considered options)

* [ADR template using Planguage](adr_template_using_planguage.md) (more quality assurance oriented)

* [ADR template for microservices](adr_microservices_template_by_user.md) (more microservices oriented)


## How to start using ADRs

To start using ADRs, talk with your teammates about these areas.

1. Decision identification

  * How urgent and how important is the AD?

  * Does it have to be made now, or can it wait until more is known?

  * Both personal and collective experience, as well as recognized design methods and practices, can assist with decision identification.

  * Ideally maintain a decision todo list that complements the product todo list.

2. Decision making

    * A number of decision making techniques exists, both general ones and software and software architecture specific ones, for instance, dialogue mapping.

    * Group decision making is an active research topic.

3. Decision documentation

    * Many templates and tools for decisison capturing exist.

    * See agile communities, e.g. M. Nygard's ADRs.

    * See traditional software engineering and architecture design processes, e.g. table layouts suggested by IBM UMF and by Tyree and Akerman from CapitalOne.

4. Decision enactment and enforcement

    * ADs are used in software design; hence they have to be communicated to, and accepted by, the stakeholders of the system that fund, develop, and operate it.

    * Architecturally evident coding styles and code reviews that focus on architectural concerns and decisions are two related practices. 

    * ADs also have to be (re-)considered when modernizing a software sytem in software evolution.

5. Decision sharing (optional)
 
    * Many ADs recur across projects.

    * Hence, experiences with past decisions, both good and bad, can be valuable reusable assets when employing an explicit knowledge management strategy.

The steps above are adopted from the Wikipedia entry on [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)


## How to start using ADRs with tools

You can start using ADRs with tools any way you want.

For example:

  * If you like using Google Drive and online editing, then you can create a Google Doc, or Google Sheet.

  * If you like use source code version control, such as git, then you can create a file for each ADR.
  
  * If you like using project planning tools, such as Atlassian Jira, then you can use the tool's planning tracker.

  * If you like using wikis, such as MediaWiki, then you can create an ADR wiki.


## How to start using ADRs with git

If you like using git version control, then here's how we like to start using ADRs with git for a typical software project with source code.

1. Create a directory for ADR files.

      mkdir adr

2. For each ADR, create a text file, such as `database.txt`.

      vi database.txt

3. Write anything you want in the ADR. See the templates in this repository for ideas.

4. Commit the ADR to your git repo

## ADR file name conventions

If you choose to create your ADRs using typical text files, then you may want to come up with your own ADR file name convention.

We prefer to use a file name convention that has a specific format.

Examples:

  * 2017-01-01 Choose a database.md

  * 2017-01-02 Handle more users.md

  * 2017-01-03 Improve application security.md

Our file name convention:

  * The name has the date as YYYY-MM-DD. This is ISO standard and helps for sorting by date. 

  * The name has a present tense imperative verb phrase. This helps readability and matches our commit message format.

  * The name uses sentence capitalization and spaces. This is helpful for readability.

  * The extension is markdown. This can be useful for easy formatting.

## Rules of the ADR road

1. Characteristics of a good ADR:

* Point in Time - The ADR identifies when the AD was made

* Rationality - The ADR explains the rationale for making the particular AD

* Immutable record - The decisions made in previously published ADR should not be altered

* Specificity - Each ADR should be about a single AD

2. Characteristics of good Context in an ADR:

* Should explain your organization's situation and business priorities

* Should include considerations for the social, team and skills makeup of your teams

3. Characteristics of good Consequences in an ADR:

* Good approach - "We need to start doing X instead of Y"

* Bad appraoch - Don't explain the AD in terms of "Pros" and "Cons" of having made the particular AD

4. A new ADR may take the place the previous ADR

## Organizations and Projects using ADRs


## Contributing

Your comments and suggestions are welcome.

You can open a GitHub issue, or create a pull request, or email joel@joelparkerhenderson.com.


## Sources

Introduction:

* [Architectural Decision - Wikipedia](https://en.wikipedia.org/wiki/Architectural_decision)

* [Architecturally significant requirements](https://en.wikipedia.org/wiki/Architecturally_significant_requirements)

Templates:

* [Documenting architecture decisions - Michael Nygard](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

* [Markdown Architectural Decision Records](https://adr.github.io/madr/) - provided by the [adr GitHub organization](https://adr.github.io/)

* [Template for documenting architecture alternatives and decisions - Stack Overflow](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

In-depth:

* [ADMentor XML project - GitHub](https://github.com/IFS-HSR/ADMentor)

* [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

* [The Decision View's Role in Software Architecture Practice](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

* [Documenting Software Architectures: Views and Beyond](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

* [Architecture Decisions: Demystifying Architecture](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

* [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

Tools:

* [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

Examples:

* [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

See also:

* REMAP (Representation and Maintenance of Process Knowledge)

* DRL (Decision Representation Language)

* IBIS (Issue-Based Information System)

* QOC (Questions, Options, and Criteria)

* DRL (Decision Representation Language),

* IBM’s e-Business Reference Architecture Framework