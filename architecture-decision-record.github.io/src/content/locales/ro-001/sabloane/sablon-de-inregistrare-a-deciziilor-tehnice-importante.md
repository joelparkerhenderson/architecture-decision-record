# Șablon de înregistrare a deciziilor pentru Deciziile Tehnice Importante (ITD)

Acesta este șablonul pentru Deciziile Tehnice Importante (engl. Important Technical Decisions, ITD) descris în
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

ITD-urile sunt o evoluție țintită a ADR-urilor, optimizată pentru viteză, claritate
și validare de către conducere. Dacă un ADR documentează ce s-a decis, un ITD este un
artefact suplu, în care decizia vine prima și care face decizia însăși analizabilă, astfel încât
părțile interesate să o poată parcurge rapid și să o conteste ușor. ITD-urile se potrivesc bine
deciziilor tehnice care nu sunt strict arhitecturale, cum ar fi alegerea unui
model, a unei biblioteci sau a unei strategii CI/CD.

În fiecare fișier ITD, scrie aceste secțiuni:

# Titlu

Formulează decizia însăși, nu o descriere a subiectului.
De exemplu: „Folosim Qwen2.5 1.5B Instruct pentru traducerea pe dispozitiv”.

## Problema

O propoziție care spune ce încercăm să rezolvăm.

## Opțiuni luate în considerare

Alternativele care au fost pe masă, cu opțiunea aleasă în **aldine**.

## Justificare

Doar factorii decisivi care au dus la alegere, nu o listă exhaustivă a
tuturor avantajelor și dezavantajelor.

## Note

Opțional. Orice context suplimentar care merită consemnat, cum ar fi constrângeri,
ipoteze sau linkuri.
