# Skabelon til arkitekturbeslutningspost (ADR) <!-- Replace with ADR title -->

Dette er en skabelon til EdgeX Foundry ADR'er.

Kilde: https://docs.edgexfoundry.org/2.3/design/adr/template/


### Indsendere

Angiv ADR'ens indsendere.

Format:

- Navn (organisation)


## Ændringslog

Angiv ændringer i dokumentet, herunder status, dato og pull request-URL.

Status er en af: pending, approved, amended, deprecated.

Datoen er en ISO 8601-streng (YYYY-MM-DD).

PR er det pull request, der indsendte ændringen, og indeholder oplysninger som diffs, bidragydere og gennemgåere.

Format:

- \[ADR'ens status, f.eks. approved, amended osv.\]\(pull request-URL\) YYYY-MM-DD


## Refererede anvendelsestilfælde

Angiv alle relevante dokumenter med anvendelsestilfælde / krav.

En ADR skal have mindst ét relevant og godkendt anvendelsestilfælde.

Format:

- \[Anvendelsestilfældets navn\]\(URL\)

Tilføj en forklaring, hvis ADR'en ikke dækker alle anvendelsestilfældets krav.


## Kontekst

Beskriv:

- Hvorfor designet er arkitektonisk væsentligt - hvorfor der er brug for en ADR (frem for blot en issue og PR til at løse problemet)

- Den overordnede designtilgang (detaljer kommer i det foreslåede design nedenfor)


## Foreslået design

Detaljerne i designet (om muligt uden at gå ind i implementeringen).

Oversigt over:

- De services/moduler, der påvirkes (ændres)

- De nye services/moduler, der tilføjes

- Indvirkning på modeller og DTO'er (ændre/tilføje/fjerne)

- Indvirkning på API'er (ændre/tilføje/fjerne)

- Indvirkning på fælles konfiguration (nyt afsnit, ændre/tilføje/fjerne)

- Indvirkning på devops


## Overvejelser

Dokumentér alternativer, bekymringer, sideløbende eller relaterede problemer og spørgsmål, der blev rejst under ADR-diskussionen. 

Angiv, om og hvordan de er løst eller afbødet.


## Beslutning

Dokumentér vigtige implementeringsdetaljer, der er opnået enighed om, forbehold, fremtidige overvejelser og resterende eller udskudte designspørgsmål.

Dokumentér de dele af kravene, der ikke opfyldes af det foreslåede design.


## Andre relaterede ADR'er

Angiv relaterede ADR'er, for eksempel designbeslutninger for delkomponenter af funktionen, designs der er blevet forældet som følge af dette design osv.. 

Format:

- \[ADR-titel\]\(URL\) - relevans


## Referencer

Angiv eventuelle yderligere referencer.

Format:

- \[Titel\]\(URL\)

