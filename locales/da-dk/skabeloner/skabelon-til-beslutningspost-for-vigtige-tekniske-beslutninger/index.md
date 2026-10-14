# Skabelon til beslutningspost for vigtige tekniske beslutninger (ITD)

Dette er skabelonen til vigtige tekniske beslutninger (Important Technical Decisions, ITD), som beskrevet i
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

En ITD er en fokuseret udvikling af ADR'en, optimeret til hastighed, klarhed og
ledelsesvalidering. Hvor en ADR dokumenterer, hvad der blev besluttet, er en ITD en lean
artefakt med beslutningen først, som gør selve beslutningen gennemgåelig, så interessenter hurtigt kan
skimme den og nemt udfordre den. ITD'er passer til tekniske beslutninger, der ikke strengt taget
handler om arkitektur, såsom valg af en model, et bibliotek eller en CI/CD-strategi.

I hver ITD-fil skriver du disse afsnit:

# Titel

Angiv selve beslutningen, ikke en beskrivelse af emnet.
For eksempel "Brug Qwen2.5 1.5B Instruct til oversættelse på enheden".

## Problem

Én sætning, der beskriver, hvad vi forsøger at løse.

## Overvejede muligheder

De alternativer, der blev vurderet, med den valgte mulighed i **fed**.

## Begrundelse

Kun de afgørende faktorer, der førte til valget, ikke en
udtømmende liste over alle fordele og ulemper.

## Bemærkninger

Valgfrit. Yderligere kontekst, der er værd at registrere, såsom begrænsninger, antagelser eller links.
