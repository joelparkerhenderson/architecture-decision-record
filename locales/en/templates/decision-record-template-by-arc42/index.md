# Decision record template by arc42

<https://arc42.org/overview>

## 1. Introduction and Goals

Short description of the requirements, driving forces, extract (or abstract) of
requirements. Top three (max five) quality goals for the architecture which have
highest priority for the major stakeholders. A table of important stakeholders
with their expectation regarding architecture.

## 1.1 Requirements Overview

### Contents

Short description of the functional requirements, driving forces, extract (or
abstract) of requirements. Links to the (hopefully existing) requirements
documents, with information where to find it. 

### Motivation

From the point of view of the end users a system is created or modified to
improve support of a business activity and/or improve the quality. 

### Form

Short textual description, probably in tabular use-case format. If requirements
documents exist this overview should refer to these documents.

Keep these excerpts as short as possible. Balance readability of this document
with potential redundancy w.r.t. requirements documents. 

## 1.2 Quality goals

### Content

The top three (max five) quality goals for the architecture whose fulfillment is
of highest importance to the major stakeholders. We really mean quality goals
for the architecture. Don’t confuse them with project goals. They are not
necessarily identical. The ISO 25010 standard provides a nice overview of
potential topics of interest.

### Motivation

You should know the quality goals of your most important stakeholders, since
they will influence fundamental architectural decisions. Make sure to be very
concrete about these qualities, avoid buzzwords. If you as an architect do not
know how the quality of your work will be judged …

### Form

A table with the most important quality goals and concrete scenarios, ordered by priorities.

## 1.3 Stakeholder

### Content

Explicit overview of stakeholders of the system, i.e. all person, roles or
organizations that

- should know the architecture

- have to be convinced of the architecture

- have to work with the architecture or with code

- need the documentation of the architecture for their work

- have to come up with decisions about the system or its development

### Motivation

You should know all parties involved in development of the system or affected by
the system. Otherwise, you may get nasty surprises later in the development
process. These stakeholders determine the extent and the level of detail of your
work and its results.

### Form

Table with role names, person names, and their expectations with respect to the
architecture and its documentation.

## 2. Constraints

Anything that constrains teams in design and implementation decisions or
decision about related processes. Can sometimes go beyond individual systems and
are valid for whole organizations and companies.

### Content

Any requirement that constrains software architects in their freedom of design
and implementation decisions or decision about the development process. These
constraints sometimes go beyond individual systems and are valid for whole
organizations and companies.

### Motivation

Architects should know exactly where they are free in their design decisions and
where they must adhere to constraints. Constraints must always be dealt with;
they may be negotiable, though.

### Form

Simple tables of constraints with explanations. If needed you can subdivide them
into technical constraints, organizational and political constraints and
conventions (e.g. programming or versioning guidelines, documentation or naming
conventions)

## 3. Context and Scope

Delimits your system from its (external) communication partners (neighboring
systems and users). Specifies the external interfaces. Shown from a
business/domain perspective (always) or a technical perspective (optional)

### Content

System scope and context - as the name suggests - delimits your system (i.e.
your scope) from all its communication partners (neighboring systems and users,
i.e. the context of your system). It thereby specifies the external interfaces.

If necessary, differentiate the business context (domain specific inputs and
outputs) from the technical context (channels, protocols, hardware).

### Motivation

The domain interfaces and technical interfaces to communication partners are
among your system’s most critical aspects. Make sure that you completely
understand them.

### Form

- Various context diagrams

- Lists of communication partners and their interfaces.

## 3.1 Business context

### Content

Specification of all communication partners (users, IT-systems, …) with
explanations of domain specific inputs and outputs or interfaces. Optionally you
can add domain specific formats or communication protocols.

### Motivation

All stakeholders should understand which data are exchanged with the environment
of the system.

### Form

All kinds of diagrams that show the system as a black box and specify the domain
interfaces to communiations partners.

Alternatively (or additionally) you can use a table. The title of the table is
the name of your system, the three columns contain the name of the communication
partner, the inputs, and the outputs.

## 3.2 Technical context

### Contents

Technical interfaces (channels and transmission media) linking your system to
its environment. In addition a mapping of domain specific input/output to the
channels, i.e. an explanation with I/O uses which channel.

### Motivation

Many stakeholders make architectural decision based on the technical interfaces
between the system and its context. Especially infrastructure or hardware
designers decide these technical interfaces.

### Form

E.g. UML deployment diagram describing channels to neighboring systems, together
with a mapping table showing the relationships between channels and
input/output.

## 4. Solution Strategy

Summary of the fundamental decisions and solution strategies that shape the
architecture. Can include technology, top-level decomposition, approaches to
achieve top quality goals and relevant organizational decisions.

### Contents

A short summary and explanation of the fundamental decisions and solution strategies, that shape the system’s architecture. These include

- technology decisions

- decisions about the top-level decomposition of the system, e.g. usage of an architectural pattern or design pattern

- decisions on how to achieve key quality goals

- relevant organizational decisions, e.g. selecting a development process or delegating certain tasks to third parties.

### Motivation

These decisions form the cornerstones for your architecture. They are the basis
for many other detailed decisions or implementation rules.

### Form

Keep the explanation of these key decisions short.

Motivate what you have decided and why you decided that way, based upon your
problem statement, the quality goals and key constraints. Refer to details in
the following sections (section 5 for structural details, section 8 for
crosscutting concepts).

You might use a list of solution-approaches or a table.

## 5. Building Block View

Static decomposition of the system, abstractions of source-code, shown as
hierarchy of white boxes (containing black boxes), up to the appropriate level
of detail.

### Content

The building block view shows the static decomposition of the system into
building blocks (modules, components, subsystems, classes, interfaces, packages,
libraries, frameworks, layers, partitions, tiers, functions, macros, operations,
data structures, …) as well as their dependencies (relationships, associations,
…)

This view is mandatory for every architecture documentation. In analogy to a
house this is the floor plan.

### Motivation

Maintain an overview of your source code by making its structure understandable
through abstraction.

This allows you to communicate with your stakeholder on an abstract level
without disclosing implementation details.

### Form

The building block view is a hierarchial collection of black boxes and white
boxes (see figure below) and their descriptions.

## 5.1 Whitebox Overall System

Here you describe the decomposition of the overall system using the following white box template. It contains

- an overview diagram

- a motivation for the decomposition

- black box descriptions of the contained building blocks. For these we offer you alternatives:

  - use one table for a short and pragmatic overview of all contained building blocks and their interfaces

  - use a list of black box descriptions of the building blocks according to the black box template (see below). Depending on your choice of tool this list could be sub-chapters (in text files), sub-pages (in a Wiki) or nested elements (in a modelling tool).

  - (optional:) important interfaces, that are not explained in the black box templates of a building block, but are very important for understanding the white box.

Since there are so many ways to specify interfaces why do not provide a specific template for them.

In the best case you will get away with examples or simple signatures.

## 5.2 Level 2

Here you can specify the inner structure of (some) building blocks from level 1
as white boxes.

You have to decide which building blocks of your system are important enough to
justify such a detailed description. Please prefer relevance over completeness.
Specify important, surprising, risky, complex or volatile building blocks. Leave
out normal, simple, boring or standardized parts of your system

### 5.2.1 White Box for building block 1

Specifies the internal structure of building block 1.

Use the white box template (see above).

## 6. Runtime View

Behavior of building blocks as scenarios, covering important use cases or
features, interactions at critical external interfaces, operation and
administration plus error and exception behavior.

### Content

The runtime view describes concrete behavior and interactions of the system’s building blocks in form of scenarios from the following areas:

- important use cases or features: how do building blocks execute them?

- interactions at critical external interfaces: how do building blocks cooperate with users and neighbouring systems?

- operation and administration: launch, start-up, stop

- error and exception scenarios

Remark: The main criterion for the choice of possible scenarios (sequences, workflows) is their architectural relevancy. It is not important to describe a large number of scenarios. You should rather document a representative selection.

### Motivation

You should understand how (instances of) building blocks of your system perform their job and communicate at runtime. You will mainly capture scenarios in your documentation to communicate your architecture to stakeholders that are less willing or able to read and understand the static models (building block view, deployment view).

### Form

There are many notations for describing scenarios, e.g.


- numbered list of steps (in natural language)

- activity diagrams or flow charts

- sequence diagrams

- BPMN or EPCs (event process chains)

- state machines

- etc.

## 6.n Runtime Scenario n (1, 2, 3, etc.)

Insert runtime diagram or textual description of the scenario.

Insert description of the notable aspects of the interactions between the building block instances depicted in this diagram.

## 7. Deployment View

Technical infrastructure with environments, computers, processors, topologies.
Mapping of (software) building blocks to infrastructure elements.

### Content

The deployment view describes:

- the technical infrastructure used to execute your system, with infrastructure
  elements like geographical locations, environments, computers, processors,
  channels and net topologies as well as other infrastructure elements and

- the mapping of (software) building blocks to that infrastructure elements.

Often systems are executed in different environments, e.g. development
environment, test environment, production environment. In such cases you should
document all relevant environments.

Especially document the deployment view when your software is executed as
distributed system with more then one computer, processor, server or container
or when you design and construct your own hardware processors and chips.

From a software perspective it is sufficient to capture those elements of the
infrastructure that are needed to show the deployment of your building blocks.
Hardware architects can go beyond that and describe the infrastructure to any
level of detail they need to capture. 

### Motivation

Software does not run without hardware. This underlying infrastructure can and
will influence your system and/or some cross-cutting concepts. Therefore, you
need to know the infrastructure.

### Form

Maybe the highest level deployment diagram is already contained in section 3.2. as technical context with your own infrastructure as ONE black box. In this section you will zoom into this black box using additional deployment diagrams.

- UML offers deployment diagrams to express that view. Use it, probably with nested diagrams, when your infrastructure is more complex.

- When your (hardware) stakeholders prefer other kinds of diagrams rather than
  UML deployment diagram, let them use any kind that is able to show nodes and
  channels of the infrastructure.

## 7.1 Infrastructure Level 1

Describe (usually in a combination of diagrams, tables, and text):

- the distribution of your system to multiple locations, environments, computers, processors, .. as well as the physical connections between them

- important justification or motivation for this deployment structure

- quality and/or performance features of the infrastructure

- the mapping of software artifacts (building blocks) to elements of the infrastructure

For multiple environments or alternative deployments please copy that section of arc42 for all relevant environments. **

## 7.2 Infrastructure Level 2

Here you can include the internal structure of (some) infrastructure elements from infrastructure level 1.

Please copy the structure from level 1 for each selected element.

## 8. Crosscutting Concepts

Overall, principal regulations and solution approaches relevant in multiple
parts (→ cross-cutting) of the system. Concepts are often related to multiple
building blocks. Include different topics like domain models, architecture
patterns and -styles, rules for using specific technology and implementation
rules.

### Content

This section describes crosscutting concepts (practices, patterns, regulations
or solution ideas). Such concepts are often related to multiple building blocks.
They may include many different topics.

### Motivation

Concepts form the basis for conceptual integrity (consistency, homogeneity) of
the architecture. Thus, they are an important contribution to achieve inner
qualities of your system.

This is the place in the template that we provided for a cohesive specification
of such concepts.

Many of these concepts relate to or influence several of your building blocks.

### Form

The form can be varied:

- concept papers with any kind of structure

- example implementations, especially for technical concepts

- cross-cutting model excerpts or scenarios using notations of the architecture views

### Structure of this section

Pick only the most-needed topics for your system and assign each a level-2 heading in this section (e.g. 8.1, 8.2 etc).

- DO NOT ATTEMPT to cover all of the topics of the aforementioned diagram.

### Background

Some topics within systems often concern multiple building blocks, hardware
elements or development processes. It might be easier to communicate or document
such cross-cutting topics at a central location, instead of repeating them in
the description of the concerned building blocks, hardware elements or
development processes.

Certain concepts might concern all elements of a system, others might only be
relevant for a few.

## 9. Architectural Decisions

Important, expensive, critical, large scale or risky architecture decisions
including rationales.

### Content

Important, expensive, large scale or risky architecture decisions including
rationales. With “decisions” we mean selecting one alternative based on given
criteria.

Please use your judgement to decide whether an architectural decision should be
documented here in this central section or whether you better document it
locally (e.g. within the white box template of one building block). Avoid
redundant texts. Refer to section 4, where you captured the most important
decisions of your architecture already.

### Motivation

Stakeholders of your system should be able to comprehend and retrace your
decisions.

### Form

- ADR (architecture decision record) for every important decision

- list or table, ordered by importance and consequences or

- more detailed in form of separate sections per decision

### Background (on ADRs)

Smaller pieces of documentation are easier to read, create and maintain. When it
comes to architecture decisions, development teams will often:

- know about the decision, as it visible e.g. in source code, but

- miss the motivation behind that decision (see Nygard 2011)

Therefore you should document a few important decisions together with their
motivation, reasoning

### Our proposal concerning decisions

Keep a collection of architecturally significant decisions, those decisions that
affect the structure, quality characteristics, important (especially external)
dependencies and interfaces, or construction techniques (thanks to Michael
Nygard for this proposal).

## 10. Quality Requirements

Quality requirements as scenarios, with quality tree to provide high-level
overview. The most important quality goals should have been described in section
1.2. (quality goals).

### Content

This section contains all relevant quality requirements.

The most important of these requirements have already been described in section
1.2. (quality goals), therefore they should only be referenced here. In this
section 10 you should also capture quality requirements with lesser importance,
which will not create high risks when they are not fully achieved (but might be
nice-to-have).

### Motivation

Since quality requirements will have a lot of influence on architectural
decisions you should know what qualities are really important for your
stakeholders, in a specific and measurable way.

### Further Information

See the extensive Q42 quality model on https://quality.arc42.org.

## 10.1 Quality Requirements Overview

### Content

An overview or summary of quality requirements.

### Motivation

Often we encounter dozens (or even hundreds) of detailed quality requirements.
In this overview section you should try to summarize, e.g. by describing
categories or topics (as suggested by ISO 25010:2023 or Q42

If these summary descriptions are already precise, specific enough and
measurable, you may skip section 10.2.

### Form

Use a simple table in which each line contains a category or topic and a short
description of the quality requirement. Alternatively, you may use a mindmap to
structure these quality requirements.

In literature, the idea of a quality attribute tree has also been described,
which puts the generic term “quality” as the root and uses a tree-like
refinement of the term “quality”. [Bass+21] introduced the term “Quality
Attribute Utility Tree” for this purpose.

## 10.2 Quality Scenarios

### Content

Quality scenarios make quality requirements concrete and allow to decide whether
they are fulfilled (in the sense of acceptance criteria). Ensure that your
scenarios are specific and measurable.

Two kinds of scenarios are especially useful:

- Usage scenarios (also called application scenarios or use case scenarios)
  describe the system’s runtime reaction to a certain stimulus. This also
  includes scenarios that describe the system’s efficiency or performance.
  Example: The system reacts to a user’s request within one second.

- Change scenarios describe the desired effect of a modification or extension of
  the system or of its immediate environment. Example: Additional functionality
  is implemented or requirements for a quality attribute change, and the effort
  or duration of the change is measured.

### Form

Typical information for detailed scenarios include the following:

In short form (favoured in the Q42 model):

- Context/Background: What kind of system or component, what is the envirionment or situation?

- Source/Stimulus: Who or what initiates or triggers a behaviour, reaction or action.

- Metric/Acceptance Criteria: A response including a measure or metric

The long form of scenarios (favoured by the SEI and [Bass+21]) is more detailed and includes the following information:

- Scenario ID: A unique identifier for the scenario.

- Scenario Name: A short, descriptive name for the scenario.

- Source: The entity (user, system, or event) that initiates the scenario.

- Stimulus: The triggering event or condition the system must address.

- Environment: The operational context or condition under which the system experiences the stimulus.

- Artifact: The building-blocks or other elements of the system affected by the stimulus.

- Response: The outcome or behavior the system exhibits in reaction to the stimulus.

- Response Measure: The criteria or metric by which the system’s response is evaluated.

### See also

Since January 2023, arc42 provides a pragmatic quality model, that proposes to
label quality requirements, with hashtags or labels like #flexible, #efficient,
#usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Risks and Technical Debt

Known technical risks or technical debt. What potential problems exist within or
around the system? What does the development team feel miserable about?

### Content

A list of identified technical risks or technical debts, ordered by priority

### Motivation

“Risk management is project management for grown-ups” (Tim Lister, Atlantic
Systems Guild.)

This should be your motto for systematic detection and evaluation of risks and
technical debts in the architecture, which will be needed by management
stakeholders (e.g. project managers, product owners) as part of the overall risk
analysis and measurement planning.

### Form

List of risks and/or technical debts, probably including suggested measures to
minimize, mitigate or avoid risks or reduce technical debts.
