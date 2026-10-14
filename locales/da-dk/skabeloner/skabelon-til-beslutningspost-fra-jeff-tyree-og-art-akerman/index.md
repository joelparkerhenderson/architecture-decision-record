# Skabelon til beslutningspost fra Jeff Tyree og Art Akerman

Dette er skabelonen til beskrivelse af arkitekturbeslutninger fra ["Architecture Decisions: Demystifying Architecture", Jeff Tyree og Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Problemstilling (Issue)**: Beskriv det arkitekturdesignproblem, der behandles, så der ikke er tvivl om, hvorfor du adresserer det nu. Efter en minimalistisk tilgang behandler og dokumenterer du kun de problemstillinger, der kræver opmærksomhed på bestemte tidspunkter i livscyklussen.

* **Beslutning (Decision)**: Angiv tydeligt arkitekturretningen, dvs. det valgte standpunkt.

* **Status**: Beslutningens status, for eksempel pending, decided, approved.

* **Gruppe (Group)**: Du kan bruge enkle grupperinger, såsom integration, præsentation, data osv., til at organisere et sæt beslutninger. Du kan også bruge en mere raffineret arkitekturontologi, såsom den fra John Kyaruzi og Jan van Katwijk, med mere abstrakte kategorier som hændelser, kalendere og lokationer. Med denne ontologi ville du for eksempel gruppere beslutninger, der adresserer situationer, hvor systemet har brug for oplysninger, under hændelser.

* **Antagelser (Assumptions)**: Beskriv tydeligt de underliggende antagelser i det miljø, hvor beslutningen træffes: omkostninger, tidsplan, teknologi og så videre. Bemærk, at begrænsninger i miljøet (såsom accepterede teknologistandarder, virksomhedsarkitektur, almindeligt anvendte mønstre) kan begrænse de overvejede alternativer.

* **Begrænsninger (Constraints)**: Registrér eventuelle yderligere begrænsninger, som det valgte alternativ (beslutningen) kan pålægge miljøet.

* **Standpunkter (Positions)**: Angiv de overvejede standpunkter (mulige valg eller alternativer). Det kræver ofte en lang forklaring og nogle gange endda modeller og diagrammer. Dette er ikke nødvendigvis en udtømmende liste. Du vil dog ikke høre spørgsmålet "Har du tænkt på ...?" ved den afsluttende gennemgang. Det fører til tab af tillid og tvivl om andre arkitekturbeslutninger. Dette afsnit hjælper også med at bekræfte, at du har lyttet til andres meninger. At gøre andre meninger eksplicitte hjælper med at få deres fortalere med på din beslutning.

* **Argument**: Skitsér, hvorfor du valgte et standpunkt, med emner som implementeringsomkostninger, samlede ejeromkostninger, tid til marked og tilgængeligheden af nødvendige udviklingsressourcer. Det er sandsynligvis lige så vigtigt som selve beslutningen.

* **Implikationer (Implications)**: En beslutning har mange implikationer, som REMAP-metamodellen viser. For eksempel kan en beslutning skabe behov for at træffe andre beslutninger, skabe nye krav eller ændre eksisterende, pålægge miljøet yderligere begrænsninger, kræve genforhandling af omfang eller tidsplan med kunden eller kræve yderligere oplæring af personale. Klar forståelse og angivelse af en beslutnings implikationer kan være meget effektivt til at opnå tilslutning og skabe en køreplan for udførelsen af arkitekturen.

* **Relaterede beslutninger**: Det er tydeligt, at mange beslutninger hænger sammen; du kan angive dem her. I praksis finder vi dog, at en sporbarhedsmatrix, et beslutningstræ eller en metamodel er mere nyttig. Metamodeller er nyttige til at vise komplekse relationer i diagrammer (f.eks. Rose-modeller).

* **Relaterede krav**: Beslutninger bør være forretningsdrevne. For at vise ansvarlighed skal du eksplicit koble beslutninger til mål eller krav. Du kan opregne disse relaterede krav her, men vi finder det mere bekvemt at referere til en sporbarhedsmatrix. Du vurderer i hvilket omfang hver arkitekturbeslutning bidrager til at opfylde hvert krav, og derefter hvor godt kravene er opfyldt på tværs af alle beslutninger. Hvis en beslutning ikke bidrager til at opfylde et krav, så træf ikke den beslutning.

* **Relaterede artefakter**: Angiv de relevante arkitektur-, design- eller omfangsdokumenter, som denne beslutning påvirker.

* **Relaterede principper**: Hvis virksomheden har et aftalt sæt principper, så sørg for, at beslutningen er i overensstemmelse med et eller flere af dem. Det hjælper med at sikre afstemning på tværs af domæner eller systemer.

* **Noter**: Fordi beslutningsprocesser kan tage uger, finder vi det nyttigt at registrere de noter og problemstillinger, som teamet drøfter under den indledende deling.

