# Guidelines to Achieve Sustainable Decisions

<https://www.infoq.com/articles/sustainable-architectural-design-decisions/>

We learned the following lessons in our work that can serve as guidelines and assessment for achieving sustainable decisions:

1. Use a lean/minimalistic approach for the initial decision documentation.

2. Prioritize and capture all important decisions that are relevant enough for documenting and understanding the target architecture.

3. Detail the particularly important decisions with full-blown templates only after the initial work has been done (that is, when the decision makers are content with the architectural decisions made and confident that these decisions don’t have to be revised any time soon).

4. Use the lean/minimalistic versions from step 1 as a short version of documented decisions with the right granularity level to provide an overview of the detailed decisions, as well as for trivial or obvious decisions.

5. Wherever possible, use existing architectural knowledge, either from guidance models or from other sources. Review and extend such knowledge and fit it to the context of the specific decision.

6. Ensure that traceability links are established between decisions and both requirements and architectural designs/code. 

7. Provide automated consistency checking to make sure the traceability links are in sync after a change. Limit the number of dependencies between decisions and other software artifacts.

8 Apply the guidelines for the justifications consequently and forcefully—they’re the most important part of the decision documentation because they give the rationale.
