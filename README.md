# Architecture Decision Record (ADR)

* [Introduction](#introduction)
* [Contributing](#contributing)
* [Simple start](#simple)
* [Lifecycle](#lifecycle)
* [Sources](#sources)

ADR templates:

* [ADR template by Michael Nygard](adr_template_by_michael_nygard.md) (simple and popular)
* [ADR template by Jeff Tyree and Art Akerman](adr_template_by_jeff_tyree_and_art_akerman.md) (more sophisticated)
* [ADR template for Alexandrian pattern[(adr_template_for_alexandrian_pattern.md) (simple with context specifics)
* [ADR template for business case](adr_template_for_business_case.md) (more MBA-oriented, with costs, SWOT, and more opinions)


<a name="introduction"><h2>Introduction</h2></a>

An architectural decision (AD) is a software design choice that addresses a significant requirement.

An architectural decision record (ADR) is a way to track an AD, such as by writing notes, or logging information.

An architecturally significant requirement (ASR) is a requirement that has a measurable effect on a software system’s architecture.

All these are within the topic of architectural knowledge management (AKM).

The goal of this document is to provide a fast overview of ADRs, how to create them, and where to look for more information.


<a name="contributing"><h2>Contributing</h2></a>

Your comments and suggestions are welcome.

You can open a GitHub issue, or create a pull request, or email joel@joelparkerhenderson.com.


<a name="implementation"><h2>Simple start</h2></a>

This simple start is for a typical software project. More sophisticated information comes later in this page.

1. Create a directory for the documentation, then the architecture, then the ADR files.

  Example directory names to choose from:

      ./doc/arch/adr/
      ./docs/architectures/decisions/
      ./documentation/architecture-decision-records/

2. For each ADR, create a text file. We like to use a title that has a date and a present tense imperative verb phrase, lowercase with underscore separators, and using markdown.

  Example file names:

      handle_more_users.md
      strengthen_security.md
      improve_energy_efficiency.md

3. Write anything you want in the ADR. We like ours to cover these areas at least.


  * Title: short and action-oriented, such as "Choose a database".

  * Context: what is the issue that we're seeing that is motivating this decision or change.

  * Action: what are we proposing, or evaluating, or doing, etc.


<a name="template-alternatives"><h2>Template ideas</h2></a>

ADR template by Michael Nygard, which is the simplest and most popular:

* Title
* Status
* Context
* Decision
* Consequences
* [more detail](adr_template_by_michael_nygard.md)

ADR template using Alexandrian pattern, which is simple and has context specifics:

* Prologue (Summary)
* Discussion (Context)
* Solution (Decision)
* Consequences (Results)
* [more detail](adr_template_for_alexandrian_pattern.md) 

ADR template for business case, which is MBA-oriented, with costs, SWOT, and  opinions:

* Title
* Status
* Evaluation criteria
* Candidates to consider
* Research and analysis of each candidate
  * Does/doesn't meet criteria and why
  * Cost analysis
  * SWOT analysis
  * Opinions and feedback
* Recommendation
* [more detail](adr_template_for_business_case.md) 

ADR template by Jeff Tyree and Art Akerman, which is more sophisticated:

* Issue
* Decision
* Status
* Group
* Assumptions
* Constraints
* Positions
* Argument
* Implications
* Related decisions
* Related requirements
* Related artifacts
* Related principles
* Note
* [more detail](adr_template_by_jeff_tyree_and_art_akerman.md)

Additional ideas that you may want to consider overall and/or for each option:

* Problem Definition
* Solution Context
* Evaluation Criteria
* Constraints
* High-Level Comparison Table
* Option Description
* Pros and Cons
* Constraints
* Points of Note
* RAID log
  * Risks
  * Assumptions
  * Issues
  * Dependencies
* SWOT analysis
  * Strengths
  * Weaknesses
  * Opportunites
  * Threats
* Porter's 5 Forces
  * Supplier power
  * Buyer power
  * Competitive rivalry
  * Threat of substitution
  * Threat of new entry


<a name="lifecycle"><h2>Lifecycle</h2></a>

1. Decision identification

  * How urgent and how important is the AD?
  * Does it have to be made now, or can it wait until more is known?
  * Both personal and collective experience, as well as recognized design methods and practices, can assist with decision identification.
  * Ideally maintain a decision todo list that complements the product todo list.

2. Decision making

  * A number of decision making technqiues exists, both general ones and software and software architecture specific ones, for instance, dialogue mapping.[15] Group decision making is an active research topic.

3. Decision documentation

  * Many templates and tools for decisison capturing exist, both in agile communities (e.g., M. Nygard's ADRs) and in traditional software engineering and architecture design processes (e.g., see table layouts suggested by IBM UMF and by Tyree and Akerman from CapitalOne.

4. Decision enactment and enforcement

  * ADs are used in software design; hence they have to be communicated to, and accepted by, the stakeholders of the system that fund, deveop, and operate it. Architecturally evident coding styles [19] and code reviews that focus on architectural concerns and decisions are two related practices. ADs also have to be (re-)considered when modernizing a software sytem in software evolution.

5. Decision sharing (optional)

  * Many ADs recur across projects; hence, experiences with past decisions, both good and bad, can be valuable reusable assets when employing an explicit knowledge management strategy.


<a name="sources"><h2>Sources</h2></a>

Introduction:

* [Architectural Decision - Wikipedia](https://en.wikipedia.org/wiki/Architectural_decision)
* [Architecturally significant requirements](https://en.wikipedia.org/wiki/Architecturally_significant_requirements)

Templates:

* [Documenting architecture decisions - Michael Nygard](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)
* [Template for documenting architecture alternatives and decisions - Stack Overflow](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

In-depth:

* [ADMentor XML project - GitHub](https://github.com/IFS-HSR/ADMentor)
* [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)
* [The Decision View's Role in Software Architecture Practice](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)
* [Documenting Software Architectures: Views and Beyond])(http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)
* [Architecture Decisions: Demystifying Architecture](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

See also:

* REMAP (Representation and Maintenance of Process Knowledge)
* DRL (Decision Representation Language) 
* IBIS (Issue-Based Information System)
* QOC (Questions, Options, and Criteria)
* DRL (Decision Representation Language), 
* IBM’s e-Business Reference Architecture Framework
