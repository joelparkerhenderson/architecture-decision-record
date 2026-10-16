# Predloga zapisa odločitve za pomembne tehnične odločitve (ITD)

To je predloga za pomembne tehnične odločitve (Important Technical Decisions, ITD), opisana v
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

ITD so osredotočen razvoj ADR, optimiziran za hitrost, jasnost in potrditev
vodstva. Medtem ko ADR dokumentira, kaj je bilo odločeno, je ITD vitek artefakt,
ki na prvo mesto postavlja odločitev in omogoča, da je sama odločitev
pregledljiva, tako da jo lahko deležniki hitro preletijo in preprosto
izpodbijajo. ITD so zelo primerni za tehnične odločitve, ki niso strogo
arhitekturne, na primer izbiro modela, knjižnice ali strategije CI/CD.

V vsaki datoteki ITD napišite te razdelke:

# Naslov

Navedite samo odločitev, ne opisa teme.
Na primer »Use Qwen2.5 1.5B Instruct for on-device translation«.

## Problem

En stavek, ki pove, kaj poskušamo rešiti.

## Preučene možnosti

Alternative, ki so bile na mizi, pri čemer je izbrana možnost **krepko**.

## Utemeljitev

Samo odločilni dejavniki, ki so vodili do izbire, ne izčrpen seznam
vseh prednosti in slabosti.

## Opombe

Neobvezno. Vsak dodaten kontekst, ki ga je vredno zabeležiti, na primer omejitve,
predpostavke ali povezave.
