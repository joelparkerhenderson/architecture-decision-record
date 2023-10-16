# AWS Architectural Decision Records Process

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

An architectural decision record (ADR) is a document that describes a choice the team makes about a significant aspect of the software architecture they’re planning to build. Each ADR describes the architectural decision, its context, and its consequences. ADRs have states and therefore follow a lifecycle. For an example of an ADR, see the appendix.

The ADR process outputs a collection of architectural decision records. This collection creates the decision log. The decision log provides the project context as well as detailed implementation and design information. Project members skim the headlines of each ADR to get an overview of the project context. They read the ADRs to dive deep into project implementations and design choices.

When the team accepts an ADR, it becomes immutable. If new insights require a different decision, the team proposes a new ADR. When the team accepts the new ADR, it supersedes the previous ADR.

## Scope of the ADR process

Project members should create an ADR for every architecturally significant decision that affects the software project or product, including the following (Richards and Ford 2020):

* Structure (for example, patterns such as microservices)

* Non-functional requirements (security, high availability, and fault tolerance)

* Dependencies (coupling of components)

* Interfaces (APIs and published contracts)

* Construction techniques (libraries, frameworks, tools, and processes)

* Functional and non-functional requirements are the most common inputs to the ADR process.


## ADR contents

When the team identifies a need for an ADR, a team member starts to write the ADR based on a projectwide template. (See the ADR GitHub organization for example templates.) The template simplifies ADR creation and ensures that the ADR captures all the relevant information. At a minimum, each ADR should define the context of the decision, the decision itself, and the consequences of the decision for the project and its deliverables. (For examples of these sections, see the appendix.) One of the most powerful aspects of the ADR structure is that it focuses on the reason for the decision rather than how the team implemented it. Understanding why the team made the decision makes it easier for other team members to adopt the decision, and prevents other architects who weren’t involved in the decision-making process to overrule that decision in the future.


## ADR adoption process

Every team member can create an ADR, but the team should establish a definition of ownership for an ADR. Each author who is the owner of an ADR should actively maintain and communicate the ADR content. To clarify this ownership, this guide refers to ADR authors as ADR owners in the following sections. Other team members can always contribute to an ADR. If the content of an ADR changes before the team accepts the ADR, the owner should approve these changes.

After the team identifies an architectural decision and its owner, the ADR owner provides the ADR in the **Proposed** state at the beginning of the process. ADRs in the Proposed state are ready for review.

The ADR owner then initiates the review process for the ADR. The goal of the ADR review process is to decide whether the team accepts the ADR, determines that it needs rework, or rejects the ADR. The project team, including the owner, reviews the ADR. The review meeting should start with a dedicated time slot to read the ADR. On average, 10 to 15 minutes should be enough. During this time, each team member reads the document and adds comments and questions to flag unclear topics. After the review phase, the ADR owner reads out and discusses each comment with the team.

If the team finds action points to improve the ADR, the state of the ADR stays **Proposed**. The ADR owner formulates the actions, and, in collaboration with the team, adds an assignee to each action. Each team member can contribute and resolve the action points. It is the responsibility of the ADR owner to reschedule the review process.

The team can also decide to reject the ADR. In this case, the ADR owner adds a reason for the rejection to prevent future discussions on the same topic. The owner changes the ADR state to **Rejected**.

If the team approves the ADR, the owner adds a timestamp, version, and list of stakeholders. The owner then updates the state to **Accepted**.

ADRs and the decision log they create represent decisions made by the team and provide a history of all decisions. The team uses the ADRs as a reference during code and architectural reviews where possible. In addition to performing code reviews, design tasks, and implementation tasks, team members should consult ADRs for strategic decisions for the product.

As a good practice, each software change should go through peer reviews and require at least one approval. During the code review, a code reviewer might find changes that violate one or more ADRs. In this case, the reviewer asks the author of the code change to update the code, and shares a link to the ADR. When the author updates the code, it is approved by peer reviewers and merged into the main code base.


## ADR review process

The team should treat ADRs as immutable documents after the team accepts or rejects them. Changes to an existing ADR requires creating a new ADR, establishing a review process for the new ADR, and approving the ADR. If the team approves the new ADR, the owner should change the state of the old ADR to **Superseded**. 
