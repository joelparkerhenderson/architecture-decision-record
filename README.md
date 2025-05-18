<!--
  browser: architecture-decision-record
  tracker: 2bd6622ec3beeeddd8ff55cf0ccf2efc
  version: 3.1.0
  updated: 2025-05-18T11:55:54Z
  contact: Joel Parker Henderson (http://joelparkerhenderson.com)
  options: commentable
  summary: Architecture Decision Record (ADR) for software planning, CTO/CIO leadership teamwork, and project management documentation. Examples, templates, and tutorials. 
  tags: architecturedecisionrecord adr decisionrecord projectmanagement plan cto cio leadership teamwork documentation template tutorial architecture decision record
-->

# Architecture decision record (ADR)

An architecture decision record (ADR) is a document that captures an important architecture decision made along with its context and consequences.

Contents:

* [What is an architecture decision record?](#what-is-an-architecture-decision-record)
* [How to start using ADRs](#how-to-start-using-adrs)
* [How to start using ADRs with tools](#how-to-start-using-adrs-with-tools)
* [How to start using ADRs with git](#how-to-start-using-adrs-with-git)
* [File name conventions for ADRs](#file-name-conventions-for-adrs)
* [Suggestions for writing good ADRs](#suggestions-for-writing-good-adrs)
* [ADR example templates](#adr-example-templates)
* [Teamwork advice for ADRs](#teamwork-advice-for-adrs)
* [Teamwork questions for ADRs](#teamwork-questions-for-adrs)
  * [Who can create an ADR?](#who-can-create-an-adr)
  * [What justifies raising an ADR?](#what-justifies-raising-an-adr)
  * [What justifies not rasing an ADR?](#what-justifies-not-rasing-an-adr)
  * [What is the lifecycle of an ADR?](#what-is-the-lifecycle-of-an-adr)
  * [What are criteria for lifecycle steps of an ADR?](#what-are-criteria-for-lifecycle-steps-of-an-adr)
  * [What roles and responsibilities interact with an ADR?](#what-roles-and-responsibilities-interact-with-an-adr)
  * [How does governance interact with an ADR?](#how-does-governance-interact-with-an-adr)
  * [What principles interact with an ADR?](#what-principles-interact-with-an-adr)
* [For more information](#for-more-information)

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

<div class="include" data-path="locales/en/documents/what-is-an-architecture-decision-record">

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

<div class="include" data-path="locales/en/documents/how-to-start-using-adrs">

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

<div class="include" data-path="locales/en/documents/how-to-start-using-adrs-with-tools">

## How to start using ADRs with tools

You can start using ADRs with tools any way you want.

For example:

* If you like using Google Drive and online editing, then you can create a Google Doc, or Google Sheet.

* If you like use source code version control, such as git, then you can create a file for each ADR.

* If you like using project planning tools, such as Atlassian Jira, then you can use the tool's planning tracker.

* If you like using wikis, such as MediaWiki, then you can create an ADR wiki.

</div>

<div class="include" data-path="locales/en/documents/how-to-start-using-ADRs-with-git">

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

<div class="include" data-path="locales/en/documents/file-name-conventions-for-adrs">

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

<div class="import" data-path="locales/en/documents/suggestions-for-writing-good-adrs">

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

<div class="import" data-path="locales/en/documents/teamwork-advice-for-adrs">

## Teamwork advice for ADRs

If you're considering using decision records with your team, then here's some advice that we've learned by working with many teams.

You have an opportunity to lead your teammates, by talking together about the "why", rather than mandating the "what". For example, decision records are a way for teams to think smarter and communicate better; decision records are not valuable if they're just an after-the-fact forced paperwork requirement.

Some teams much prefer the name "decisions" over the abbreviation "ADRs". When some teams use the directory name "decisions", then it's as if a light bulb turns on, and the team starts putting more information into the directory, such as vendor decisions, planning decisions, scheduling decisions, etc. All of these kinds of information can use the same template. We hypothesize that people learn faster with words ("decisions") over abbreviations ("ADRs"), and people are more motivated to write work-in-progress docs when the word "record" is removed, and also some developers and some managers dislike the word "architecture".

In theory, immutability is ideal. In practice, mutability has worked better for our teams. We insert the new info the existing ADR, with a date stamp, and a note that the info arrived after the decision. This kind of approach leads to a "living document" that we all can update. Typical updates are when we get information thanks to new teammates, or new offerings, or real-world results of our usages, or after-the-fact third-party changes such as vendor capabilities, pricing plans, license agreements, etc.

</div>

<div class="import" data-path="locales/en/documents/teamwork-questions-for-adrs">

## Teamwork questions for ADRs

### Who can create an ADR?

Consider areas such as specific people, or specific roles, or specific teams, or specific departments; also consider if there are people, or roles, or teams, or department that can commission an ADR, meaning they request one that someone else will author. 

Example answer: Any person in our organization who has read the architecture decision record README page can propose an ADR, meaning the person can start writing it, and share it with the team.

### What justifies raising an ADR?

Consider areas such as your organization's team ways of working, your software system structure, cross-team coordination, long-term maintainability, external interfaces, who you want to benefit, and the like. 

Example answer: We want to create an ADR when we want future developers to understand the “why” of what we're doing.

### What justifies not rasing an ADR?

Consider areas such as decisions that are not about architecture, or are tiny such as minimal-risk or self-contained or single-developer, or are already fully covered elsewhere such as by standards or policies or documentation, or are temporary such as workarounds or proofs of concepts or orexperiments. 

Example answer: We want to skip an ADR when a decision is limited in scope and time and risk and cost, or is already covered elsewhere.

### What is the lifecycle of an ADR?

Consider areas such as the creation process, research process, decisioning process, implementation process, and sunsetting process. Consider how to track the ADR lifecycle over time, such as how to move the ADR from one state to the next state, and also how to communicate this to stakeholders. 

Example answer: We want an ADR to have five lifecycle stages: Initiating → Researching → Evaluating → Implementing → Maintaining → Sunsetting.

### What are criteria for lifecycle steps of an ADR?

Consider areas such as acceptance criteria for an ADR, meaning how do you know it's good enough to progress from one lifecycle step to the next? Is the problem clearly articulated? Have the alternatives been considered? Are trade-offs well-enough understood and documented?
Is all relevant context in place? Are all revelant stakeholders involved? Has all feedback been incorporated? 

Example answer: We want an ADR to be voted on by stakeholders when the active team has 1) completed their research, 2) completed their evaluation, 3) published the ADR proposal to the stakeholders with a request for comments and a timebox of one week, 4) all stakeholder comments have been incorporated and addressed.

### What roles and responsibilities interact with an ADR?

Consider roles such as proposer, researcher, evaluator, reviewer, approver, maintainer, and the like. Consider responsbilities such as communication with stakeholders, ensuring expectations are met, sharing on the website or intranet, and reviewing the work periodically and especially when relevant changes happen.

Example answer: We want each ADR to always have a primary contact person, secondary contact person, and accountable team; these are responsble for communications, publications, maintenance, periodic review at least once per year, and eventual sunsetting as needed.

### How does governance interact with an ADR?

Consider areas such as your organization's ways of working, any special compliance needs such as for legal aspects or human resource aspects, how you want to handle consensus versus conflict versus escalation. Are there areas or people or teams that can have more influence than others regarding an ADR, such as being able to approve it, or vote on it, or veto it?

Example answer: The governance of an ADR is in this priority order: the CEO, the CTO, the CLO, the team that implements an ADR, the experts on the team that are most-knowledgeable about the ADD. No one else has governance unless described in the ADR. 

### What principles interact with an ADR?

Consider areas such as your organization's ways of working that include  moving quickly versus moving slowly, for decision consensus versus decision conflict, and for risk preferences versus safety preferences, public discussion versus private discussion, and the like.

Example answer: We use the leadership priciples of bias for action, disagree-and-commit, 70% estimates are good enough for easily-reversable easily-isolatable decisions, and public ways of working with the exception of confidential information as described in our organization's confidentiality agreement.

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

* [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - free monthly software architecture lesson

Tools:

* [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

* [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

* [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

Company-Specific Guidance:

* [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

* [GitHub: ADR GitHub organization](https://adr.github.io/)

* [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Examples:

* [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Videos:

* [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcasts:

* [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Books:

* [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

* [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

* [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

* [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

* [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

* [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

* [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

* [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

* [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2))

* [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

See also:

* REMAP (Representation and Maintenance of Process Knowledge)

* DRL (Decision Representation Language)

* IBIS (Issue-Based Information System)

* QOC (Questions, Options, and Criteria)

* IBM’s e-Business Reference Architecture Framework
