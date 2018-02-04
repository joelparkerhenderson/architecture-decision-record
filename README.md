# Architecture Decision Record (ADR)

* [Introduction](#introduction)
* [ADR example templates](#adr-example-templates)
* [How to start using ADRs](#how-to-start-using-adrs)
* [How to start using ADRs with tools](#how-to-start-using-adrs-with-tools)
* [How to start using ADRs with git](#how-to-start-using-adrs-with-git)
* [ADR file name conventions](#adr-file-name-conventions)
* [Contributing](#contributing)
* [Sources](#sources)


<h2><a name="introduction">Introduction</a></h2>

An architectural decision (AD) is a software design choice that addresses a significant requirement.

An architectural decision record (ADR) is a way to track an AD, such as by writing notes, or logging information.

An architecturally significant requirement (ASR) is a requirement that has a measurable effect on a software system’s architecture.

All these are within the topic of architectural knowledge management (AKM).

The goal of this document is to provide a fast overview of ADRs, how to create them, and where to look for more information.


<h2><a name="adr-example-templates">ADR example templates</a></h2>

ADR example templates that we have collected on the net:

* [ADR template by Michael Nygard](adr_template_by_michael_nygard.md) (simple and popular)
* [ADR template by Jeff Tyree and Art Akerman](adr_template_by_jeff_tyree_and_art_akerman.md) (more sophisticated)
* [ADR template for Alexandrian pattern](adr_template_for_alexandrian_pattern.md) (simple with context specifics)
* [ADR template for business case](adr_template_for_business_case.md) (more MBA-oriented, with costs, SWOT, and more opinions)
* [ADR template MADR](adr_template_madr.md) (focuses on considered options)
* [ADR template using Planguage](adr_template_using_planguage.md) (more quality assurance oriented)


<h2><a name="how-to-start-using-adrs">How to start using ADRs</a></h2>

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


<h2><a name="how-to-start-using-adrs-with-tools">How to start using ADRs with tools</a></h2>

You can start using ADRs with tools any way you want.

For example:

  * If you like using Google Drive and online editing, then you can create a Google Doc, or Google Sheet.

  * If you like use source code version control, such as git, then you can create a file for each ADR.
  
  * If you like using project planning tools, such as Atlassian Jira, then you can use the tool's planning tracker.

  * If you like using wikis, such as MediaWiki, then you can create an ADR wiki.


<h2><a name="how-to-start-using-adrs-with-git">How to start using ADRs with git</a></h2>

If you like using git version control, then here's how we like to start using ADRs with git for a typical software project with source code.

1. Create a directory for ADR files.

      mkdir adr

2. For each ADR, create a text file, such as `database.txt`.

      vi database.txt

3. Write anything you want in the ADR. See the templates in this repo for ideas.


<h2><a name="adr-file-name-conventions">ADR file name conventions</a></h2>

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

<h2><a name="contributing">Contributing</a></h2>

Your comments and suggestions are welcome.

You can open a GitHub issue, or create a pull request, or email joel@joelparkerhenderson.com.


<h2><a name="sources">Sources</a></h2>

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

See also:

* REMAP (Representation and Maintenance of Process Knowledge)
* DRL (Decision Representation Language)
* IBIS (Issue-Based Information System)
* QOC (Questions, Options, and Criteria)
* DRL (Decision Representation Language),
* IBM’s e-Business Reference Architecture Framework



