# Arkitekturbeslutningspost: kodeeditorer til programmering

## Kontekst

Kodeeditorer til programmering er et essentielt værktøj for udviklere til at skrive og redigere kode. Der findes talrige kodeeditorer, hver med sit eget sæt funktioner, fordele og ulemper. Formålet med denne ADR er at dokumentere de arkitekturbeslutninger, der er truffet for kodeeditorer til programmering.

## Prioriteter

Arkitekturen for kodeeditorer til programmering bør prioritere følgende:

* **Modularitet**: kodeeditoren bør designes modulært, så udviklere kan tilpasse og udvide den efter behov. Det giver en fleksibel arkitektur, der kan tilpasse sig forskellige udvikleres og teams behov.

* **Ydeevne**: kodeeditoren bør have god ydeevne og være responsiv, så udviklere kan arbejde effektivt uden at blive forsinket af det værktøj, de bruger.

* **Brugergrænseflade**: brugergrænsefladen bør være intuitiv og nem at bruge, så udviklere kan fokusere på deres kode frem for at kæmpe med editoren.

* **Udvidelsesmuligheder**: kodeeditoren bør designes, så den let kan udvides med tredjepartsplugins og integrationer.

* **Kompatibilitet**: kodeeditoren bør være kompatibel med et bredt udvalg af programmeringssprog og teknologier, så den er et nyttigt værktøj for en bred vifte af udviklere.

## Beslutning

På baggrund af disse prioriteter bør arkitekturen for kodeeditorer til programmering designes med følgende komponenter:

* **Kerne**: denne komponent leverer kodeeditorens grundlæggende funktionalitet, såsom syntaksfremhævning, tekstredigering og filhåndtering.

* **UI**: denne komponent leverer kodeeditorens brugergrænseflade, herunder menuer, værktøjslinjer og tastaturgenveje.

* **Plugins**: denne komponent giver udviklere mulighed for at udvide kodeeditorens funktionalitet ved at installere tredjepartsplugins. Plugins kan levere yderligere funktioner, såsom kodefuldførelse, linting eller fejlfinding.

* **Integrationer**: denne komponent giver kodeeditoren mulighed for at integrere med andre værktøjer og teknologier, såsom versionsstyringssystemer, byggesystemer eller fejlfindingsværktøjer.

## Begrundelse

Kodeeditorens modularitet giver udviklere mulighed for at tilpasse og udvide den efter behov. Det er vigtigt, fordi forskellige udviklere og teams har forskellige behov og arbejdsgange, og en fleksibel arkitektur kan imødekomme disse forskelle.

* **Ydeevne**: afgørende, fordi udviklere skal kunne arbejde effektivt uden at blive forsinket af deres værktøjer. En editor med god ydeevne er essentiel for produktivitet og kan hjælpe udviklere med at bevare deres fokus og koncentration.

* **UI**: vigtig, fordi den giver udviklere mulighed for at fokusere på deres kode frem for at kæmpe med editoren. Det kan føre til bedre produktivitet og mindre frustration for udviklere.

* **Udvidelsesmuligheder**: kraftfulde, fordi de gør det muligt at tilpasse kodeeditoren til forskellige behov og arbejdsgange. Tredjepartsplugins og -integrationer kan levere yderligere funktioner og muligheder, som ikke er inkluderet i kerneeditoren.

* **Kompatibilitet**: værdifuld, fordi den gør det muligt at bruge kodeeditoren med et bredt udvalg af programmeringssprog og teknologier. Det gør editoren til et mere nyttigt værktøj for en bred vifte af udviklere.

Kerne-, plugin-, integrations- og UI-komponenterne giver en klar adskillelse af ansvarsområder og muliggør en modulær arkitektur, der let kan udvides og tilpasses. Denne arkitektur er fleksibel, har god ydeevne og er kompatibel med et bredt udvalg af programmeringssprog og teknologier, hvilket gør den til et nyttigt værktøj for udviklere.
