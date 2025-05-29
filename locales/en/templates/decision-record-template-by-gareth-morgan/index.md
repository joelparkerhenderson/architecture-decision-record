# [000] Title
*Allocate each ADR a number for easy reference and cataloging* \
*NOTE: All italicised text provides hints and should be removed for production*

## Status - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## Context
*Briefly describe the problem(s) that this ADR intends to address, and why the problems exist.*

## Decided Approach
*Detail the architecturally significant decision that has been / will be made and describe how it addresses the problems outlined in the Context section.*

## Consequences
*What is the impact of this decision on the architecture characteristics and functional requirements of the system?*

## Governance
*How will the outcomes of this decision be monitored?* \
*How will compliance with this decision be ensured?*

## Options Analysis
*If applicable, include or link to any trade-off analysis which has been performed to arrive at the decision made in this document.*

### Key
*Optional: Provide visual aids to stakeholders which can help to quickly spot the positive and the negative trade-offs - for example simple traffic-light highlights with positive or negative prefixes.*

A <span style="background-color:#4bce97; color:black;">green</span> background indicates a good fit, worsening through <span style="background-color:#f1c232; color:black;">amber</span>, with <span style="background-color:#e06666; color:black;">red</span> being the worst fit. \
\+ indicates a positive impacting comment \
\- indicates a negative impacting comment

### High-Level Overview
*How well does each option fit the problem context at a glance?*

<table>
  <thead>
    <tr>
      <th>Summary</th>
      <th>Option 1</th>
      <th>Option 2</th>
      <th>Option 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Ease of Implementation</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Super easy
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Tricky
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Large implementation requiring expert knowledge
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Timescales</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Very quick
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Fairly slow
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Very slow
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Strategic Value</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - No strategic value, purely tactical
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Slightly improves the customer onboarding experience
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideal for the upcoming merger
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Functional Requirements
*How well does each potential option fit the desired functional requirements?*

<table>
  <thead>
    <tr>
      <th>Scenario</th>
      <th><i>Option 1</i></th>
      <th><i>Option 2</i></th>
      <th><i>Option 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Scenario 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenario 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenario 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Optional: Add rows / another table to cover known future scenarios.*

### Non-Functional Requirements
*How well does each potential option fit the desired architecture characteristics?
Note: ‘Architecture Characteristics’ would be a more appropriate title, but tailor this to familiar language for your business domain.*

<table>
  <thead>
    <tr>
      <th>Architecture </br> Characteristic</th>
      <th><i>Option 1</i></th>
      <th><i>Option 2</i></th>
      <th><i>Option 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Scalability</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Performance</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Availability</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Optional: Add in or link to definitions of the architecture characteristics as they pertain to your business / product.*