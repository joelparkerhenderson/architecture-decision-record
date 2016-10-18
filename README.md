# Architecture Decision Record (ADR)

* [Introduction](#introduction)
* [Simple start](#simple)
* [Template by Michael Nygard](#template-by-michael-nygard)
* [Template by Jeff Tyree and Art Akerman](#template-by-jeff-tyree-and-art-akerman)
* [Lifecycle](#lifecycle)
* [Sources](#sources)


<a name="introduction"><h2>Introduction</h2></a>

An architectural decision (AD) is a software design choice that addresses a significant requirement.

An architecturally significant requirement (ASR) is a requirement that has a measurable effect on a software system’s architecture.

These are within the topic of architectural knowledge management (AKM).


<a name="implementation"><h2>Simple start</h2></a>

This simple start is for a typical software project. More sophisticated information comes later in this page.

1. Create a directory for the documentation, then the architecture, then the ADR files.

  Example directory names to choose from:

      ./doc/arch/adr/
      ./doc/architecture/decisions/
      ./doc/architecture-decision-records/

2. For each ADR, create a text file. We like to use a title that has a date and a present tense imperative verb phrase, lowercase with dashes, and using markdown.

  Example file names:

      2016-02-14-handle-more-users.md
      2016-03-15-strengthen-security.md
      2016-04-22-improve-energy-efficiency.md


<a name="template-by-michael-nygard"><h2>Template by Michael Nygard</h2></a>

This is the template in [Documenting architecture decisions - Michael Nygard](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

In each ARD file, write these sections:

* **Title**: short present tense imperative phrase, less than 50 characters, like a git commit message.

* **Context**: what is the issue that we're seeing that is motivating this decision or change.

* **Decision**: what is the change that we're actually proposing or doing.

* **Status**: proposed, accepted, rejected, deprecated, superseded, etc.

* **Consequences**: what becomes easier or more difficult to do because of this change.


<a name="template-by-jeff-tyree-and-art-akerman"><h2>Template by Jeff Tyree and Art Akerman</h2></a>

This is the Architecture decision description template published in ["Architecture Decisions: Demystifying Architecture" by Jeff Tyree and Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Issue**: Describe the architectural design issue you’re addressing, leaving no questions about why you’re addressing this issue now. Following a minimalist approach, address and document only the issues that need addressing at various points in the life cycle.

* **Decision**: Clearly state the architecture’s direction—that is, the position you’ve selected.

* **Status**: The decision’s status, such as pending, decided, or approved.

* **Group**: You can use a simple grouping—such as integration, presentation, data, and so on—to help organize the set of decisions. You could also use a more sophisticated architecture ontology, such as John Kyaruzi and Jan van Katwijk’s, which includes more abstract categories such as event, calendar, and location.8 For example, using this ontology, you’d group decisions that deal with occurrences where the system requires information under event.

* **Assumptions**: Clearly describe the underlying assumptions in the environment in which you’re making the decision—cost, schedule, technology, and so on. Note that environmental constraints (such as accepted technology standards, enterprise architecture, commonly employed patterns, and so on) might limit the alternatives you consider.

* **Constraints**: Capture any additional constraints to the environment that the chosen alternative (the decision) might pose.

* **Positions**: List the positions (viable options or alternatives) you considered. These often require long explanations, sometimes even models and diagrams. This isn’t an exhaustive list. However, you don’t want to hear the question "Did you think about...?" during a final review; this leads to loss of credibility and questioning of other architectural decisions. This section also helps ensure that you heard others’ opinions; explicitly stating other opinions helps enroll their advocates in your decision.

* **Argument**: Outline why you selected a position, including items such as implementation cost, total ownership cost, time to market, and required development resources’ availability. This is probably as important as the decision itself.

* **Implications**: A decision comes with many implications, as the REMAP metamodel denotes. For example, a decision might introduce a need to make other decisions, create new requirements, or modify existing requirements; pose additional constraints to the environment; require renegotiating scope or schedule with customers; or require additional staff training. Clearly understanding and stating your decision’s implications can be very effective in gaining buy-in and creating a roadmap for architecture execution.

* **Related decisions**: It’s obvious that many decisions are related; you can list them here. However, we’ve found that in practice, a traceability matrix, decision trees, or metamodels are more useful. Metamodels are useful for showing complex relationships diagrammatically (such as Rose models).

* **Related requirements**: Decisions should be business driven. To show accountability, explicitly map your decisions to the objectives or requirements. You can enumerate these related requirements here, but we’ve found it more convenient to reference a traceability matrix. You can assess each architecture decision’s contribution to meeting each requirement, and then assess how well the requirement is met across all decisions. If a decision doesn’t contribute to meeting a requirement, don’t make that decision.

* **Related artifacts**: List the related architecture, design, or scope documents that this decision impacts.

* **Related principles**: If the enterprise has an agreed-upon set of principles, make sure the decision is consistent with one or more of them. This helps ensure alignment along domains or systems.

* **Notes**:  Because the decision-making process can take weeks, we’ve found it useful to capture notes and issues that the team discusses during the socialization process.


<a name="template-alternatives"><h2>Template alternatives</h2></a>

These alternatives are from [Template for documenting architecture alternatives and decisions - Stack Overflow](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Alternative 1 is simple:

* Option Description
* Pros and Cons
* Risks and Issues
* Assumptions and Constraints
* Points of Note

Alternative 2 is more detailed:

* Summary
  * Problem Definition
  * Solution Context
  * Assumptions
  * Constraints
* Evaluation Criteria
* Summary of Recommendations
  * Summary
  * High-Level Comparison Table (This is good for providing an "at a glance" comparison for people who don't want to read a long document; and having a side-by-side comparison is a good idea anyway).
* For each option:
  * Option Description
  * Pros and Cons
  * Risks and Issues
  * Assumptions and Constraints
  * Points of Note
  * Recommendation


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

