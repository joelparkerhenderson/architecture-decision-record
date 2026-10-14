# Arkitekturbeslutningspost for Python Django-frameworket

Beslutningsdato: 2021-07-15

Status: Accepteret

## Kontekst

Vores organisation planlægger at udvikle en webapplikation, der administrerer kundedata. Vi har valgt Python som programmeringssprog og overvejer Django som webframework til udviklingen af applikationen.

## Beslutning

Vi har besluttet at bruge Django-webframeworket til udviklingen af webapplikationen. Django leverer et robust sæt værktøjer og funktioner til at bygge webapplikationer hurtigt og effektivt. 

## Faktorer

Nogle af de faktorer, der påvirkede vores beslutning, omfatter:

1. Objekt-relationel mapping (ORM): Django har en indbygget ORM, der gør det muligt for os at interagere med databasen uden at skrive SQL-forespørgsler. Det gør det lettere at udvikle applikationen og vedligeholde den på lang sigt.

2. MVC-framework: Django følger en Model-View-Controller (MVC)-arkitektur, hvilket gør det lettere at adskille applikationens forretningslogik og præsentationslag.

3. Skalerbarhed: Django er kendt for sin skalerbarhed, hvilket gør det til et fremragende valg til udvikling af store applikationer.

4. Sikkerhed: Django har indbyggede sikkerhedsfunktioner, såsom beskyttelse mod almindelige webangreb som cross-site scripting (XSS) og SQL-injektion.

5. Fællesskabsstøtte: Django har et stort og aktivt fællesskab, der yder support og bidrager til udviklingen af frameworket.

## Overvejede alternativer

Vi overvejede andre webframeworks såsom Flask og Pyramid. Vi fandt dog, at Django er et mere modent og veletableret framework med et robust sæt funktioner.

Vi drøftede også at udvikle applikationen uden et webframework og med biblioteker som SQLAlchemy og Flask-RESTful. Vi fandt dog, at Django tilbyder bredere funktionalitet, hvilket gør det til et bedre valg til en komplet webapplikation.

## Konsekvenser

Indførelsen af Django vil føre til følgende konsekvenser:

1. Lettere at udvikle og vedligeholde applikationen på grund af Djangos indbyggede værktøjer og funktioner.

2. Adskillelse af forretningslogik og præsentationslag, hvilket fører til mere organiseret og lettere vedligeholdelig kode.

3. Skalerbarhed og robusthed af applikationen.

4. Indbyggede sikkerhedsfunktioner, der hjælper med at beskytte applikationen mod almindelige webangreb.

5. Adgang til et stort og aktivt fællesskab til support.

Vi forstår, at Django har en stejlere indlæringskurve end andre frameworks, men vi finder, at det er investeringen værd på grund af de langsigtede fordele, det giver.

## Konklusion

På baggrund af de overvejede faktorer har vi besluttet at bruge Django-webframeworket til udviklingen af webapplikationen. Vi tror, at Djangos funktioner, fællesskabsstøtte og skalerbarhed gør det til det bedste valg til at bygge en komplet webapplikation. Vi vil uddanne vores udviklere i at bruge Django for at sikre, at frameworket bruges effektivt og virkningsfuldt.
