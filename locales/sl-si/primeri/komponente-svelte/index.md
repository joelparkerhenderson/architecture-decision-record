# Zapis arhitekturne odločitve (ADR) za komponente Svelte

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Kontekst

Izbiramo knjižnico komponent uporabniškega vmesnika Svelte, ki bi zagotavljala polne funkcije za:
- **Tabele**
- **Grafikone**
- **Sezname**
- **Mreže**
- **Ganttove diagrame**

Cilj je izbrati knjižnico, ki uravnoteži enostavnost integracije, polno podporo funkcijam, zmogljivost in dolgoročno vzdržljivost. Preučevane možnosti so:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Analiza možnosti

### 1. **SVAR**
- **Pregled**: SVAR je sodobna knjižnica komponent za Svelte, bogata s funkcijami, osredotočena na oblikovalske sisteme in komponente, pripravljene za podjetja.
- **Prednosti**:
  - Komponente s polnimi funkcijami, vključno s tabelami, obrazci in grafikoni.
  - Velike možnosti prilagajanja z vgrajeno podporo za teme.
  - Vgrajena podpora za dostopnost in odzivnost.
  - Dobro dokumentirana s prispevki skupnosti.
- **Slabosti**:
  - Morda je težja v primerjavi z drugimi preprostejšimi knjižnicami.
  - Omejena podpora za določene komponente, kot so Ganttovi diagrami in napredne mreže.
- **Najboljša za**: Aplikacije na ravni podjetij, kjer je potreben oblikovalski sistem s polnimi funkcijami.
- **Podpora za tabele/grafikone**: Zmerna do dobra.
- **Podpora za mreže/Gantta**: Minimalna.

### 2. **Carbon**
- **Pregled**: Carbon Design System je odprtokodni oblikovalski sistem podjetja IBM, ki ponuja robusten nabor komponent uporabniškega vmesnika.
- **Prednosti**:
  - Visokokakovostna, izpopolnjena zasnova z obsežno dokumentacijo.
  - Zelo dostopna in odzivna.
  - Velika knjižnica komponent, vključno z mrežami, tabelami in kontrolniki obrazcev.
- **Slabosti**:
  - Ni osredotočena na Svelte, zato je integracija lahko okorna.
  - Za polno združljivost s Svelte bo morda potrebna dodatna prilagoditev.
  - Brez takojšnje podpore za napredne komponente, kot so Ganttovi diagrami ali zapleteni grafikoni.
- **Najboljša za**: Obsežne projekte, ki zahtevajo dosleden, izpopolnjen uporabniški vmesnik.
- **Podpora za tabele/grafikone**: Dobra (z integracijami knjižnic za grafikone).
- **Podpora za mreže/Gantta**: Dobra (podpora za mreže je na voljo, Ganttovih diagramov pa ni).

### 3. **Flowbite**
- **Pregled**: Flowbite je knjižnica komponent, zgrajena s Tailwind CSS, ki ponuja različne komponente in elemente uporabniškega vmesnika.
- **Prednosti**:
  - Temelji na Tailwind CSS, zato jo je enostavno prilagoditi.
  - Enostavna za integracijo in uporabo s Svelte.
  - Zagotavlja bogate komponente, kot so tabele, grafikoni in kontrolniki uporabniškega vmesnika.
- **Slabosti**:
  - Nima naprednih funkcij (npr. Ganttovih diagramov ali zapletenih mrež).
  - Nima izvornih komponent za grafikone; zanaša se na zunanje knjižnice.
- **Najboljša za**: Projekte, ki zahtevajo hiter razvoj s poudarkom na integraciji s Tailwind CSS.
- **Podpora za tabele/grafikone**: Dobra (zahteva integracijo s knjižnicami za grafikone tretjih oseb).
- **Podpora za mreže/Gantta**: Minimalna.

### 4. **SkeletonUI**
- **Pregled**: SkeletonUI je lahka knjižnica komponent za Svelte, osredotočena na preprostost in minimalizem.
- **Prednosti**:
  - Izjemno lahka in hitra.
  - Preprost in intuitiven API.
  - Dobra za majhne projekte ali kjer je zmogljivost kritična.
- **Slabosti**:
  - Vključenih je zelo malo komponent, zato ni bogata s funkcijami.
  - Nima naprednih komponent za tabele/mreže/grafikone/Gantta.
  - Omejena podpora skupnosti in manj obsežna dokumentacija.
- **Najboljša za**: Projekte, ki zahtevajo lahke komponente z minimalnimi režijskimi stroški.
- **Podpora za tabele/grafikone**: Minimalna.
- **Podpora za mreže/Gantta**: Minimalna.

### 5. **MeltUI**
- **Pregled**: MeltUI je zbirka dostopnih komponent uporabniškega vmesnika za Svelte, osredotočena na preprostost in sestavljivost.
- **Prednosti**:
  - Lahka in popolnoma prilagodljiva.
  - Dobre funkcije dostopnosti takoj ob namestitvi.
  - Sodobna in minimalistična zasnova.
- **Slabosti**:
  - Manj bogata s funkcijami v primerjavi z drugimi knjižnicami.
  - Nima naprednih komponent za mreže in tabele.
  - Brez Ganttovih diagramov ali zapletenih možnosti za grafikone.
- **Najboljša za**: Minimalistične zasnove, ki dajejo prednost dostopnosti in zmogljivosti.
- **Podpora za tabele/grafikone**: Minimalna.
- **Podpora za mreže/Gantta**: Minimalna.

### 6. **SvelteUI**
- **Pregled**: SvelteUI je obsežna in prilagodljiva knjižnica komponent uporabniškega vmesnika za Svelte, zasnovana za gradnjo sodobnih spletnih aplikacij z elegantnim uporabniškim vmesnikom.
- **Prednosti**:
  - Obsežen nabor komponent, vključno s tabelami, mrežami, grafikoni in obrazci.
  - Zagotavlja podporo za svetli in temni način.
  - Zelo prilagodljiva in enostavna za razširitev.
  - Vgrajene integracije za knjižnice za grafikone, kot sta `chart.js` ali `d3.js`.
- **Slabosti**:
  - Lahko je težja od preprostejših knjižnic komponent.
  - Zahteva nekaj nastavitev za integracijo zunanjih knjižnic za zahtevnejše funkcije, kot so Ganttovi diagrami.
- **Najboljša za**: Projekte, ki potrebujejo obsežen, prilagodljiv nabor komponent.
- **Podpora za tabele/grafikone**: Odlična (podprte so knjižnice za grafikone).
- **Podpora za mreže/Gantta**: Dobra (komponente za mreže so na voljo; Gantt potrebuje zunanjo integracijo).

### 7. **shadcn-svelte**
- **Pregled**: Različica ShadCN za Svelte, ki je osredotočena na zasnovo, usmerjeno v pripomočke (utility-first), in zagotavlja sodobne, oblikovane komponente.
- **Prednosti**:
  - Zasnova, usmerjena v pripomočke, zgrajena na Tailwind CSS, zato jo je enostavno prilagoditi.
  - Bogat nabor komponent, takoj ob namestitvi popolnoma oblikovanih.
  - Enostavna za integracijo z drugimi knjižnicami.
- **Slabosti**:
  - Ni tako popolna kot nekatere druge glede naprednih elementov uporabniškega vmesnika.
  - Nima vgrajene podpore za tabele, grafikone ali mreže.
  - Brez takojšnje podpore za Ganttove diagrame.
- **Najboljša za**: Majhne do srednje velike projekte, ki zahtevajo prilagodljiv pristop, usmerjen v pripomočke.
- **Podpora za tabele/grafikone**: Minimalna.
- **Podpora za mreže/Gantta**: Minimalna.

## Odločitev

### Priporočena možnost: **SvelteUI**

- **Utemeljitev**: SvelteUI ponuja uravnotežen, obsežen sklop komponent, ki zadovoljuje potrebo po tabelah, grafikonih, mrežah in obrazcih. Je zelo prilagodljiv, dobro se integrira z drugimi knjižnicami za grafikone (kot sta `chart.js` in `d3.js`) ter ima dobro ravnovesje med lahko zmogljivostjo in bogastvom funkcij. Čeprav morda ne zagotavlja takojšnje podpore za Ganttove diagrame, ga je mogoče enostavno razširiti z integracijami tretjih oseb, zaradi česar je idealen za razširljivo rešitev s polnimi funkcijami.
  
  - **Prednosti**:
    - Odlična podpora za tabele in grafikone.
    - Polne komponente za mreže in postavitev.
    - Prilagodljiv in se dobro integrira z zunanjimi knjižnicami za grafikone.
    - Dobra skupnost in dokumentacija.
  
  - **Slabosti**:
    - Težji od nekaterih drugih minimalističnih knjižnic.
    - Za zapletene grafikone, kot so Ganttovi diagrami, potrebuje zunanjo integracijo.
  
### Alternativa: **Flowbite** ali **Carbon** (za večje podjetniške projekte)
- Če je potreben izpopolnjen oblikovalski sistem, ki temelji na Tailwind, ali bolj dosleden oblikovalski sistem, sta primerni alternativi **Flowbite** (s Tailwind CSS) ali **Carbon** (za rešitve na podjetniški ravni). Vendar bosta morda zahtevala dodaten trud pri integracijah z zahtevnejšimi grafikoni in komponentami.

## Sklep

Najboljša izbira za vaše zahteve (polne funkcije za tabele, grafikone, sezname, mreže, Gantta) je **SvelteUI**, ji sledita **Flowbite** in **Carbon**, odvisno od potreb projekta in oblikovalskih preferenc.