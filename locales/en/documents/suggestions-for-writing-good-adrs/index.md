## Suggestions for writing good ADRs

Characteristics of a good ADR:

  * Rationale: Explain the reasons for doing the particular AD. This can include the context (see below), pros and cons of various potential choices, feature comparions, cost/benefit discussions, and more.

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
