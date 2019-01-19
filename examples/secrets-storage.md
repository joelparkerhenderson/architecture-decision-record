# Secrets storage

## Issue

We need to store secrets, such as passwords, private keys, authentication tokens, etc.

Some of the secrets are user-oriented. For example, our developer wants to be able to use their mobile phone to look up a password to a service.

Some of the secrets are system-oriented. For example, our continuous delivery pipeline needs to be able to look up the credentials for our cloud hosting.


## Decision

We are choosing Bitwarden for user-oriented secrets

We are choosing Vault by HashiCorp for system-oriented secrets.


## Status

Decided. We are open to new alternatives as they arise.


## Assumptions

For this purpose, and our current state, we value user-oriented convenience, such as usable mobile apps.

  * We want to ensure fast easy access on the go, such as for a developer doing on-call system reliability engineering.

  * We want to be able to share some secrets among selected people, such as a team.

We are not trying to solve for single-provider, such as storing all secrets exclusively on Amazon or Azure or Google.

We do not want ad-hoc approachs such as "remember it" or "write it on a note" or "figure out your own way to store it".

Our security model for this purpose is fine with using well-respected COTS vendors, such as SaaS password management tools.


## Constraints

Right now we want something that is easy i.e. no need to write code, no need to install servers, no need to make a major commitment, no need to standardize everyone.


## Positions

We considered:

1. User-oriented off-the-self password managers: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG, etc.

2. System-oriented COTS password managers: AWS KMS, Vault by HashiCorp.

3. Sharing-oriented approaches: using a shared Google document, or shared Slack channel, or shared network folder, etc.

4. Low-tech ad-hoc approaches, such as remembering, writing a note, or relying on each user to figure out their own approach.


## Argument

Bitwarden, LastPass, 1Password, and Dashlane all are commerical off-the-shelf products.

  * Similar kinds of features for users, teams, organizations, etc.

  * Desktop capability for Windows and Mac, and mobile capability for Android and iOS.

  * Browser extensions for Chrome and Firefox, for automatic form fill in, etc.

Bitwarden has two advantages over the others:

  * Bitwarden is open source, which means the security can be peer reviewed and also the company is widely-appreciated by security-oriented developers.

  * Anecdotes by software workers describe a significant preference for Bitwarden over the others.

A typical good example writeup: https://jcs.org/2017/11/17/bitwarden

A typical side-by-side voting site: https://stackshare.io/stackups/bitwarden-vs-dashlane

We defer KeyPass, pass, GPG, etc. because there's additional complexity. All of these look like fine solutions for technical users. GPG looks especially good for technical users who want cross-system command-oriented capabilities.

We defer KMS because it has single-provider lock-in.

We choose Vault for system-oriented needs, because the reviews are amazingly positive, and because HashiCorp has an excellent track record fup top-quality software and support.

We veto the approaches of sharing approaches such as via shared documents, shared channels, shared network folders, etc. These do not provide the security qualities that we want.

We veto the ad-hoc low-tech approaches, because we all agree it's not a long-term path forward.


## Implications

Developers may need to track secrets in two places: Bitwarden for user-oriented access, and Vault for system-oriented access.


## Related decisions

The decision of which CI/CD server must include proof of capability for accessing secrets.

We will need to decide how to managea the secrets, in terms of policies, rotations, organizations, etc.


## Related requirements

The secrets will have related requirements for compliance, auditing, and HR onboarding/offboarding.


## Related artifacts

We expect we may export some secrets to environment variables.


## Related principles

Easily reversible.

Easily parallel i.e. it's easy to use a variety of password managers.

Cheap to try i.e. there's a free trial and no commitment.


## Notes

Any notes here.
