# Skabelon til beslutningspost fra arc42

<https://arc42.org/overview>

## 1. Introduktion og mål

Krav, kort beskrivelse af drivkræfterne, uddrag (eller resumé) af kravene. De tre (højst fem) vigtigste kvalitetsmål for arkitekturen, som har højeste prioritet for de vigtigste interessenter. En oversigt over vigtige interessenter med deres forventninger til arkitekturen.

## 1.1 Kravoversigt

### Indhold

Kort beskrivelse af de funktionelle krav, drivkræfter, uddrag (eller
resumé) af kravene. Links til (forhåbentlig eksisterende) kravdokumenter
med oplysninger om, hvor de kan findes. 

### Motivation

Fra slutbrugernes perspektiv bygges eller ændres et system for at
forbedre understøttelsen af forretningsaktiviteter eller for at forbedre kvaliteten. 

### Format

Kort tekstbeskrivelse, eventuelt i tabelform af anvendelsestilfælde. Hvis
der findes kravdokumenter, bør denne oversigt referere til disse dokumenter.

Hold dette uddrag så kort som muligt. Afvej dette dokuments læsbarhed mod
mulig redundans med kravdokumenter. 

## 1.2 Kvalitetsmål

### Indhold

De tre (højst fem) vigtigste kvalitetsmål for arkitekturen, hvis
opfyldelse er mest afgørende for de vigtigste interessenter. Vi mener virkelig kvalitetsmål for arkitekturen. Forveksl dem
ikke med projektmål. De er ikke nødvendigvis identiske. ISO 25010-standarden
giver et godt overblik over potentielle emner af interesse.

### Motivation

Du bør kende de vigtigste interessenters kvalitetsmål, fordi de
påvirker grundlæggende arkitekturbeslutninger. Vær meget
konkret omkring disse kvaliteter og undgå buzzwords. Hvis du som arkitekt ikke ved, hvordan kvaliteten af dit arbejde
vil blive vurderet …

### Format

En tabel med de vigtigste kvalitetsmål og konkrete scenarier, i prioriteret rækkefølge.

## 1.3 Interessenter

### Indhold

Eksplicit oversigt over systemets interessenter, dvs. alle personer, roller eller organisationer, der

- skal kende arkitekturen

- skal overbevises om arkitekturen

- skal arbejde med arkitekturen eller koden

- har brug for arkitekturdokumentationen til deres arbejde

- skal træffe beslutninger om systemet eller dets udvikling

### Motivation

Du bør kende alle parter, der er involveret i systemets udvikling eller påvirkes af det.
Ellers kan du få ubehagelige overraskelser senere i udviklingsprocessen. Disse interessenter
bestemmer omfanget og detaljeniveauet af dit arbejde og dets resultater.

### Format

Tabel med rollenavne, personnavne og deres forventninger til arkitekturen og
dokumentationen af den.

## 2. Begrænsninger

Alt, der begrænser teamet i design- og implementeringsbeslutninger eller beslutninger om den relaterede proces.
Nogle gælder undertiden for hele organisationer og virksomheder ud over de enkelte systemer.

### Indhold

Alle krav, der begrænser softwarearkitekter i deres frihed med hensyn til
design-, implementerings- eller udviklingsprocesbeslutninger. Disse begrænsninger gælder undertiden
for hele organisationer og virksomheder ud over de enkelte systemer.

### Motivation

Arkitekter bør vide præcis, hvor de er frie i deres designbeslutninger, og
hvor de skal respektere begrænsninger. Begrænsninger skal altid behandles,
men kan være til forhandling.

### Format

Enkle tabeller med begrænsninger og forklaringer. Hvis det er nødvendigt, kan du
underinddele dem i tekniske begrænsninger, organisatoriske og politiske begrænsninger og
konventioner (f.eks. programmerings- eller versionsstyringsretningslinjer, dokumentations- eller navngivningskonventioner)

## 3. Kontekst og afgrænsning

Afgrænser dit system fra (eksterne) kommunikationspartnere (nabosystemer og brugere). Specificerer de eksterne
grænseflader. Vis det fra et forretnings-/domæneperspektiv (altid) eller et teknisk perspektiv (valgfrit)

### Indhold

Systemafgrænsning og kontekst adskiller, som navnet siger, dit system (dvs. afgrænsningen) fra alle
kommunikationspartnere (nabosystemer og brugere, dvs. systemets kontekst). Dermed
specificerer de de eksterne grænseflader.

Hvis det er nødvendigt, skal du skelne forretningskonteksten (domænespecifikt input og output) fra den tekniske kontekst (kanaler, protokoller, hardware).

### Motivation

Domænegrænsefladerne og de tekniske grænseflader til kommunikationspartnere er blandt
de mest kritiske aspekter af dit system. Sørg for, at du forstår dem fuldt ud.

### Format

Forskellige muligheder:

- Diverse kontekstdiagrammer

- Lister over kommunikationspartnere og deres grænseflader.

## 3.1 Forretningskontekst

### Indhold

Specifikation af alle kommunikationspartnere (brugere, IT-systemer, …) med forklaringer af domænespecifikt
input og output eller grænseflader. Du kan eventuelt tilføje domænespecifikke formater eller kommunikationsprotokoller.

### Motivation

Alle interessenter bør forstå systemets omgivelser, og hvilke data der
udveksles.

### Format

Alle slags diagrammer, der viser systemet som en blackbox og specificerer domænegrænsefladerne
til kommunikationspartnere.

Eller (som supplement) en tabel. Tabellens titel er navnet på dit system, de tre kolonner indeholder kommunikationspartnerens navn,
input og output.

## 3.2 Teknisk kontekst

### Indhold

Tekniske grænseflader (kanaler og transmissionsmedier), der forbinder systemet med dets omgivelser. Derudover
en kortlægning af domænespecifikt input/output til kanalerne, dvs. en forklaring på, hvilket input og output der bruger hvilken kanal.

### Motivation

Mange interessenter træffer arkitekturbeslutninger baseret på de tekniske grænseflader mellem systemet og
dets kontekst. Især infrastruktur- eller hardwaredesignere beslutter disse tekniske grænseflader.

### Format

F.eks. et UML-deploymentdiagram, der beskriver kanalerne til nabosystemer,
sammen med en kortlægningstabel, der viser forholdet mellem kanaler og input/output.

## 4. Løsningsstrategi

Oversigt over de grundlæggende beslutninger og løsningsstrategier, der former arkitekturen. Kan omfatte teknologi, nedbrydning på øverste niveau,
tilgange til at nå de vigtigste kvalitetsmål og relevante organisatoriske beslutninger.

### Indhold

Et kort resumé og en forklaring af de grundlæggende beslutninger og løsningsstrategier, der
former systemarkitekturen. Det omfatter

- teknologibeslutninger

- beslutninger om nedbrydning af systemet på øverste niveau, f.eks. brug af arkitekturmønstre eller designmønstre

- beslutninger om, hvordan de vigtigste kvalitetsmål nås

- relevante organisatoriske beslutninger, f.eks. valg af udviklingsproces eller delegering af bestemte opgaver til tredjeparter.

### Motivation

Disse beslutninger er hjørnestenene i din arkitektur. De er grundlaget for mange andre detaljerede
beslutninger eller implementeringsregler.

### Format

Hold forklaringen af disse nøglebeslutninger kort.

Motivér, hvad du besluttede, og hvorfor du besluttede det, baseret på problembeskrivelsen, kvalitetsmålene og de vigtigste
begrænsninger. Se de følgende afsnit for detaljer (afsnit 5 for strukturelle detaljer, afsnit 8 for
tværgående forhold).

Du kan bruge en liste eller tabel over løsningstilgange.

## 5. Byggeblokvisning

Statisk nedbrydning af systemet, abstraktioner af kildekode, vist som et hierarki af
whiteboxe (med blackboxe indeni), op til et passende detaljeniveau.

### Indhold

Byggeblokvisningen viser den statiske nedbrydning af systemet i byggeblokke (moduler, komponenter, delsystemer, klasser,
grænseflader, pakker, biblioteker, frameworks, lag, partitioner, tiers, funktioner, makroer, operationer,
datastrukturer, …) samt deres afhængigheder (relationer, associationer, …)

Denne visning er obligatorisk for enhver arkitekturdokumentation. I analogi med et hus
er det grundplanen.

### Motivation

Bevar overblikket over din kildekode ved at gøre strukturen forståelig gennem
abstraktion.

Det giver dig mulighed for at kommunikere med dine interessenter på et abstrakt niveau uden at
afsløre implementeringsdetaljer.

### Format

Byggeblokvisningen er en hierarkisk samling af blackboxe og whiteboxe
(se figuren nedenfor) og deres beskrivelser.

## 5.1 Whitebox for hele systemet

Her beskriver du nedbrydningen af det samlede system ved hjælp af følgende whiteboxskabelon. Den indeholder

- et oversigtsdiagram

- en motivation for nedbrydningen

- blackboxbeskrivelser af de indeholdte byggeblokke. Hertil tilbydes følgende alternativer:

  - brug én tabel til en kort og pragmatisk oversigt over alle indeholdte byggeblokke og deres grænseflader

  - brug en liste af blackboxbeskrivelser af byggeblokkene efter blackboxskabelonen (se nedenfor). Afhængigt af dit værktøj kan denne liste bestå af underkapitler (tekstfiler), undersider (wiki) eller indlejrede elementer (modelleringsværktøjer).

  - (valgfrit:) vigtige grænseflader, der ikke er beskrevet i byggeblokkens blackboxskabelon, men som er meget vigtige for at forstå whiteboxen.

Da der er så mange måder at specificere grænseflader på, giver vi ikke en specifik skabelon for dem.

I bedste fald er eksempler eller enkle signaturer tilstrækkelige.

## 5.2 Niveau 2

Her kan du specificere den indre struktur af (nogle af) byggeblokkene fra niveau 1 som whiteboxe.

Du skal beslutte, hvilke byggeblokke i dit system der er vigtige nok til at retfærdiggøre en så detaljeret
beskrivelse. Foretræk relevans frem for fuldstændighed.
Specificér byggeblokke, der er vigtige, overraskende, risikable, komplekse eller flygtige.
Udelad de almindelige, enkle, kedelige eller standardiserede dele af dit system

### 5.2.1 Whitebox for byggeblok 1

...beskriver den indre struktur af byggeblok 1.

Brug whiteboxskabelonen (se ovenfor).

## 6. Kørselstidsvisning

Byggeblokkes adfærd som scenarier, der dækker vigtige anvendelsestilfælde eller funktioner, interaktioner
ved kritiske eksterne grænseflader, drift og administration samt fejl- og undtagelsesadfærd.

### Indhold

Kørselstidsvisningen beskriver konkret adfærd og interaktioner mellem systemets byggeblokke i form af scenarier fra følgende områder:

- vigtige anvendelsestilfælde eller funktioner: hvordan udfører byggeblokkene dem?

- interaktioner ved kritiske eksterne grænseflader: hvordan samarbejder byggeblokkene med brugere og nabosystemer?

- drift og administration: opstart, start, stop

- fejl- og undtagelsesscenarier

Bemærkning: det vigtigste kriterium for valg af mulige scenarier (sekvenser, arbejdsgange) er deres arkitektoniske relevans. Det er ikke vigtigt at beskrive et stort antal scenarier. Du bør snarere dokumentere et repræsentativt udvalg.

### Motivation

Du bør forstå, hvordan (instanser af) byggeblokke i dit system udfører deres arbejde og kommunikerer ved kørsel. Du vil inkludere scenarier i dokumentationen primært for at kommunikere din arkitektur til interessenter, der er mindre aktive eller mindre dygtige til at læse og forstå de statiske modeller (byggeblokvisning, deploymentvisning).

### Format

Der er mange notationer til at beskrive scenarier, f.eks.


- nummereret trinliste (i naturligt sprog)

- aktivitetsdiagrammer eller rutediagrammer

- sekvensdiagrammer

- BPMN eller EPK'er (hændelsesprocesskæder)

- tilstandsmaskiner

- osv.

## 6.n Kørselstidsscenarie n (1, 2, 3 osv.)

Indsæt et kørselstidsdiagram eller en tekstbeskrivelse af scenariet.

Indsæt en forklaring af bemærkelsesværdige aspekter ved interaktionerne mellem de byggeblokinstanser, der er afbildet i dette diagram.

## 7. Deploymentvisning

Teknisk infrastruktur med miljøer, computere, processorer og topologier.
Kortlægning af (software-)byggeblokke til infrastrukturelementer.

### Indhold

Deploymentvisningen beskriver:

- den tekniske infrastruktur, der bruges til at køre dit system, med infrastrukturelementer som geografiske lokationer, miljøer, computere, processorer,
  kanaler og netværkstopologier samt andre infrastrukturelementer, og

- kortlægningen af (software-)byggeblokke til disse infrastrukturelementer.

Systemer kører ofte i forskellige miljøer, f.eks. udviklingsmiljø, testmiljø, produktionsmiljø. I sådanne tilfælde bør du
dokumentere alle relevante miljøer.

Dokumentér især deploymentvisningen, når din software køres som et distribueret system med mere end én computer, processor, server eller container, eller når du designer og bygger dine egne hardwareprocessorer og chips.

Fra et softwareperspektiv er det tilstrækkeligt at registrere de infrastrukturelementer, der er nødvendige for at vise
deployment af byggeblokke.
Hardwarearkitekter kan gå videre og beskrive infrastrukturen på et hvilket som helst
detaljeniveau, de har brug for at registrere. 

### Motivation

Software kører ikke uden hardware. Denne underliggende infrastruktur kan og vil påvirke dit system og/eller nogle
tværgående koncepter. Derfor skal du kende infrastrukturen.

### Format

Det øverste niveau af deploymentdiagrammer er allerede inkluderet i afsnit 3.2 som teknisk kontekst med din egen
infrastruktur som én enkelt blackbox. I dette afsnit zoomer du ind på den blackbox med yderligere deploymentdiagrammer.

- UML tilbyder deploymentdiagrammer til at udtrykke den visning. Brug dem, eventuelt med indlejrede diagrammer,
  når din infrastruktur er mere kompleks.

- Når dine (hardware-)interessenter foretrækker en anden slags diagram frem for UML-deploymentdiagrammet,
  så lad dem bruge enhver slags, der kan vise noder og kanaler i infrastrukturen.

## 7.1 Infrastruktur niveau 1

Beskriv (normalt i en kombination af diagrammer, tabeller og tekst):

- fordelingen af et system på flere lokationer, miljøer, computere, processorer osv. samt de fysiske forbindelser imellem dem

- vigtig begrundelse eller motivation for denne deploymentstruktur

- kvalitets- og/eller ydeevnekarakteristika for infrastrukturen

- kortlægning af softwareartefakter (byggeblokke) til elementer i infrastrukturen

Ved flere miljøer eller alternative deployments skal du kopiere dette afsnit af arc42 for alle relevante miljøer. **

## 7.2 Infrastruktur niveau 2

Det kan omfatte den indre struktur af (nogle af) infrastrukturelementerne fra niveau 1.

Kopiér strukturen fra niveau 1 for hvert valgt element.

## 8. Tværgående koncepter

Overordnede, principielle regler og løsningstilgange, der er relevante for flere
dele (→ tværgående) af dit system. Koncepter relaterer sig ofte til flere
byggeblokke. Medtag forskellige emner som domænemodeller, arkitekturmønstre
og -stile, regler for brug af specifik teknologi og implementeringsregler.

### Indhold

Dette afsnit beskriver tværgående koncepter (praksisser, mønstre, regler
eller løsningsidéer). Sådanne koncepter relaterer sig ofte til flere byggeblokke.
De kan omfatte mange forskellige emner.

### Motivation

Koncepter er grundlaget for arkitekturens konceptuelle integritet (konsistens, homogenitet). Derfor er
de et vigtigt bidrag til systemets indre kvalitet.

Dette er stedet, vi har skabt i skabelonen til en sammenhængende specifikation af sådanne koncepter.

Mange af disse koncepter relaterer sig til eller påvirker flere byggeblokke.

### Format

Formatet kan variere:

- konceptpapirer med en hvilken som helst struktur

- eksempelimplementeringer, især til tekniske koncepter

- tværgående modeludsnit eller scenarier ved hjælp af arkitekturvisningernes notationer

### Struktur for dette afsnit

Vælg kun de emner, der er mest nødvendige for dit system, og giv hver en overskrift på niveau 2 i dette afsnit (f.eks. 8.1, 8.2 osv.).

- Forsøg ikke at dække alle emnerne i ovennævnte diagram.

### Baggrund

Nogle emner i et system relaterer sig ofte til flere byggeblokke, hardware-
elementer eller udviklingsprocesser. Det kan være lettere at kommunikere eller dokumentere sådanne tværgående emner ét centralt
sted frem for at gentage dem i beskrivelsen af de relaterede byggeblokke, hardwareelementer eller
udviklingsprocesser.

Visse koncepter kan være relevante for alle elementer i systemet, andre kun for nogle få.

## 9. Arkitekturbeslutninger

Vigtige, dyre, kritiske, store eller risikable arkitekturbeslutninger inklusive begrundelser.

### Indhold

Vigtige, dyre, store eller risikable arkitekturbeslutninger inklusive begrundelser.
Med "beslutninger" mener vi valget af ét alternativ baseret på givne kriterier.

Beslut efter eget skøn, om du vil dokumentere arkitekturbeslutninger i dette centrale afsnit, eller om du hellere vil
dokumentere dem lokalt (f.eks. inden for en byggebloks whiteboxskabelon). Undgå redundant tekst. Se afsnit 4, som allerede
indeholder de vigtigste beslutninger i din arkitektur.

### Motivation

Interessenter i dit system bør kunne forstå og spore
dine beslutninger.

### Format

- ADR'er (arkitekturbeslutningsposter) for hver vigtig beslutning

- liste eller tabel, ordnet efter vigtighed og konsekvenser, eller

- mere detaljeret i separate afsnit for hver beslutning

### Baggrund (om ADR'er)

Mindre stykker dokumentation er nemmere at læse, skrive og vedligeholde. Om arkitekturbeslutninger
kender udviklingsteams ofte:

- beslutningen, fordi den f.eks. er synlig i kildekoden, men

- savner motivationen bag den beslutning (se Nygard 2011)

Derfor bør du dokumentere nogle få vigtige beslutninger med deres motivation og ræsonnement

### Vores forslag til beslutninger

Før en samling af arkitektonisk væsentlige beslutninger, dvs. beslutninger, der påvirker struktur, kvalitetsegenskaber, vigtige
(især eksterne) afhængigheder og grænseflader eller konstruktionsteknikker (tak til Michael
Nygard for dette forslag).

## 10. Kvalitetskrav

Kvalitetskrav som scenarier, med et kvalitetstræ til et overordnet overblik.
De vigtigste kvalitetsmål bør allerede være beskrevet i afsnit
1.2 (kvalitetsmål).

### Indhold

Dette afsnit indeholder alle relevante kvalitetskrav.

De vigtigste af dem er allerede beskrevet i afsnit
1.2 (kvalitetsmål), så du bør kun referere til dem her. I dette
afsnit 10 bør du også medtage mindre vigtige kvalitetskrav, som ikke skaber høj risiko, hvis de
ikke opnås fuldt ud (men som er rare at have).

### Motivation

Da kvalitetskrav påvirker arkitekturbeslutninger meget, bør du vide, hvilken kvalitet
der virkelig er vigtig for interessenterne, på en konkret og målbar måde.

### Yderligere oplysninger

Se den omfattende Q42-kvalitetsmodel på https://quality.arc42.org.

## 10.1 Oversigt over kvalitetskrav

### Indhold

En oversigt eller et resumé af kvalitetskravene.

### Motivation

Ofte står du over for snesevis (endda hundredvis) af detaljerede kvalitetskrav.
I dette oversigtsafsnit bør du forsøge at opsummere dem, for eksempel ved at beskrive kategorier eller emner (som foreslået af ISO 25010:2023 eller Q42)

Hvis disse opsummerende beskrivelser allerede er præcise, tilstrækkeligt specifikke
og målbare, kan du springe afsnit 10.2 over.

### Format

Brug en enkel tabel med kategorien eller emnet og en kort beskrivelse af kvalitetskravet på hver linje.
Eller brug et mindmap til at strukturere disse kvalitetskrav.

I litteraturen beskrives også idéen om kvalitetsattributtræer, som har den generelle term "kvalitet" som rod og
forfiner termen "kvalitet" i en træstruktur.
[Bass+21] introducerede termen "Quality
Attribute Utility Tree" til dette formål.

## 10.2 Kvalitetsscenarier

### Indhold

Kvalitetsscenarier konkretiserer kvalitetskrav og gør det muligt at afgøre, om de
(i betydningen acceptkriterier) er opfyldt. Sørg for, at scenarier er
specifikke og målbare.

To slags scenarier er særligt nyttige:

- Brugsscenarier (også kaldet applikationsscenarier eller anvendelsesscenarier) beskriver systemets kørselstidsreaktion på en
  bestemt stimulus. Det omfatter også scenarier, der beskriver systemets effektivitet eller
  ydeevne.
  Eksempel: systemet reagerer på en brugers anmodning inden for ét sekund.

- Ændringsscenarier beskriver den ønskede effekt af en ændring eller udvidelse af systemet eller
  dets umiddelbare omgivelser. Eksempel: en yderligere funktion implementeres, eller kravene
  til en kvalitetsattribut ændres, og ændringens indsats eller varighed måles.

### Format

Typiske oplysninger i detaljerede scenarier omfatter:

Kort form (foretrukket i Q42-modellen):

- Kontekst/baggrund: hvilken slags system eller komponent, og hvad er miljøet eller situationen?

- Kilde/stimulus: hvem eller hvad starter eller udløser handlingen, reaktionen eller adfærden.

- Metrik/acceptkriterium: responsen, inklusive skala eller metrik

Den lange form af scenarier (foretrukket af SEI og [Bass+21]) er mere detaljeret og omfatter følgende oplysninger:

- Scenarie-ID: en unik identifikator for scenariet.

- Scenarienavn: et kort, beskrivende navn for scenariet.

- Kilde: den enhed (bruger, system eller hændelse), der igangsætter scenariet.

- Stimulus: den udløsende hændelse eller betingelse, systemet skal reagere på.

- Miljø: den operationelle kontekst eller de betingelser, hvorunder systemet oplever stimulussen.

- Artefakt: den byggeblok eller andet element i systemet, der påvirkes af stimulussen.

- Respons: det resultat eller den adfærd, systemet udviser som reaktion på stimulussen.

- Responsmål: det kriterium eller den metrik, hvormed systemets respons vurderes.

### Se også

Siden januar 2023 tilbyder arc42 en pragmatisk kvalitetsmodel, der foreslår at tagge kvalitetskrav
med hashtags eller labels som
#flexible, #efficient, #usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Risici og teknisk gæld

Kendte tekniske risici eller teknisk gæld. Hvilke potentielle problemer er der i eller omkring systemet?
Hvad har udviklingsteamet problemer med?

### Indhold

En prioriteret liste over identificerede tekniske risici eller teknisk gæld

### Motivation

"Risikostyring er projektledelse for voksne" (Tim Lister, Atlantic
Systems Guild.)

Dette bør være dit motto for en systematisk afdækning og vurdering af risici og teknisk gæld i arkitekturen,
som ledelsesinteressenter (f.eks. projektledere, product owners) vil have brug for som en del af den overordnede risikoanalyse og planlægning af foranstaltninger.

### Format

Liste over risici og/eller teknisk gæld, eventuelt med foreslåede foranstaltninger til
at minimere, afbøde eller undgå risiciene eller reducere den tekniske gæld.

