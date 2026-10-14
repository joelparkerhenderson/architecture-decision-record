# Arkitekturbeslutningspost: programmeringssproget Rust

Beslutningsnummer: AR-001

Beslutningstitel: Indførelse af programmeringssproget Rust

Dato: 1. december 2021

Status: Accepteret

### Problembeskrivelse

Efterhånden som vi fortsætter med at udvikle softwareapplikationer, har vi observeret, at det bliver stadig mere udfordrende at afbøde potentielle sikkerhedssårbarheder og forhindre kørselsfejl. Med de eksisterende programmeringssprog, såsom C og C++, oplever vi fortsat problemer som bufferoverløb, hukommelseslækager og udefineret adfærd, der fører til nedbrud i applikationer. Vi har brug for et programmeringssprog, der giver garantier for hukommelsessikkerhed og er effektivt nok til at understøtte ydeevnekritiske applikationer.

### Overvejelser

Flere programmeringssprog er designet til at løse de eksisterende problemer. Blandt dem har programmeringssproget Rust fået betydelig opmærksomhed i udviklerfællesskabet på grund af dets unikke designegenskaber. Overvejelser omfatter;

1. Hukommelsessikkerhed og sikkerhed

2. Ydeevne og effektivitet

3. Fællesskabsstøtte og udbredelse

4. Indlæringskurve

5. Værktøjer og økosystem

6. Kompatibilitet med eksisterende softwaresystemer.

### Begrænsninger

Indførelse af et nyt programmeringssprog kræver omskoling af udviklere, hvilket kræver tid og ressourcer. Integration af sproget i den eksisterende udviklingsarbejdsgang kan være en udfordring. Vi skal sikre kompatibilitet med de eksisterende systemer og undgå brydende ændringer for at bevare kontinuiteten.

### Implementering

1. Vores udviklingsteam gennemgår uddannelse for at lære og blive fortrolige med programmeringssproget Rust.

2. Vi opretter et nyt projekt med Rust på prøvebasis for at evaluere dets kompatibilitet og egnethed til vores udviklingsformål.

3. Vi migrerer gradvist eksisterende systemer skrevet i C og C++ til Rust.

4. Vi samarbejder med Rust-fællesskabet for at udforske de tilgængelige værktøjer og biblioteker, der kan forbedre vores udviklingsarbejdsgang.

5. Vi overvåger Rusts ydeevne og sammenligner den regelmæssigt med de eksisterende programmeringssprogs ydeevne.

6. Vi vælger en langsigtet tilgang, der afvejer omkostningerne ved uddannelse og integration mod de potentielle fordele ved at bruge Rust.

### Begrundelse

Vi har indført Rust på grund af dets unikke funktioner, der er designet til at give garantier for hukommelsessikkerhed og sikkerhed, samtidig med at ydeevne og effektivitet opretholdes. Rusts robuste typesystem, borrow checker og koncepter for hukommelsessikkerhed gør det meget egnet til udvikling af ydeevnekritiske og sikkerhedskritiske applikationer. Desuden har Rust et betydeligt fællesskab af udviklere, hvilket giver os adgang til et bredt udvalg af værktøjer, biblioteker og økosystem, der understøtter vores udviklingsarbejdsgang. Selv om Rust kommer med en indlæringskurve, tror vi, at fordelene ved at indføre Rust opvejer omkostningerne og giver en fremragende mulighed for fortsat vækst og innovation.

### Konsekvenser

1. Indførelsen af Rust kræver en betydelig investering i tid og ressourcer til at uddanne udviklere og integrere sproget i den eksisterende udviklingsarbejdsgang.

2. Indførelse af Rust kan forårsage en vis grad af kompatibilitetsproblemer med eksisterende systemer, hvilket kræver refaktorering og ændringer.

3. Indførelsen af Rust kan øge antallet af udviklere, der kan bidrage til vores projekt, ved at tiltrække Rust-udviklere, der vil arbejde på spændende projekter.

4. Indførelsen kan føre til forbedret ydeevne, effektivitet og sikkerhed sammenlignet med de eksisterende sprog.

5. Endelig kommer indførelsen af Rust med den potentielle fordel at reducere sikkerhedssårbarheder i vores applikationer.
   
<h6>Kildehenvisning: Denne side er genereret af ChatGPT og derefter redigeret for klarhed og format.</h6>
