# Zapis arhitekturne odluke (ADR) za komponente Sveltea

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Kontekst

Biramo biblioteku UI komponenti za Svelte koja će pružiti pune značajke za:
- **Tablice**
- **Grafikone**
- **Popise**
- **Mreže**
- **Ganttove dijagrame**

Cilj je odabrati biblioteku koja uravnotežuje jednostavnost integracije, punu podršku značajki, performanse i dugoročnu održivost. Opcije koje se razmatraju su:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Analiza opcija

### 1. **SVAR**
- **Pregled**: SVAR je moderna biblioteka komponenti bogata značajkama za Svelte, s fokusom na dizajnerske sustave i komponente spremne za enterprise.
- **Prednosti**:
  - Komponente s punim značajkama, uključujući tablice, obrasce i grafikone.
  - Visoke mogućnosti prilagodbe s ugrađenom podrškom za teme.
  - Ugrađena podrška za pristupačnost i responzivnost.
  - Dobro dokumentirano uz doprinose zajednice.
- **Nedostaci**:
  - Mogao bi biti teži u usporedbi s drugim jednostavnijim bibliotekama.
  - Ograničena podrška za specifične komponente poput Ganttovih dijagrama i naprednih mreža.
- **Najbolje za**: Aplikacije na razini enterprisea gdje je potreban dizajnerski sustav s punim značajkama.
- **Podrška za tablice/grafikone**: Umjerena do dobra.
- **Podrška za mreže/Gantt**: Minimalna.

### 2. **Carbon**
- **Pregled**: Carbon Design System je dizajnerski sustav otvorenog koda tvrtke IBM koji nudi robustan skup UI komponenti.
- **Prednosti**:
  - Visokokvalitetan, dotjeran dizajn s opsežnom dokumentacijom.
  - Vrlo pristupačan i responzivan.
  - Velika biblioteka komponenti, uključujući mreže, tablice i kontrole obrazaca.
- **Nedostaci**:
  - Nije usmjeren na Svelte, pa integracija može biti glomazna.
  - Moglo bi biti potrebno dodatno prilagođavanje za punu kompatibilnost sa Svelteom.
  - Nema izvorne podrške za napredne komponente poput Ganttovih dijagrama ili složenih grafikona.
- **Najbolje za**: Velike projekte koji zahtijevaju dosljedno, dotjerano UI.
- **Podrška za tablice/grafikone**: Dobra (uz integracije biblioteka grafikona).
- **Podrška za mreže/Gantt**: Dobra (podrška za mreže dostupna, ali nema Ganttovih dijagrama).

### 3. **Flowbite**
- **Pregled**: Flowbite je biblioteka komponenti izgrađena s Tailwind CSS-om koja nudi razne komponente i UI elemente.
- **Prednosti**:
  - Temelji se na Tailwind CSS-u, što olakšava prilagodbu.
  - Lako se integrira i koristi sa Svelteom.
  - Pruža bogate komponente poput tablica, grafikona i UI kontrola.
- **Nedostaci**:
  - Nedostaju napredne značajke (npr. Ganttovi dijagrami ili složene mreže).
  - Nema izvorne komponente za grafikone; oslanja se na vanjske biblioteke.
- **Najbolje za**: Projekte koji zahtijevaju brz razvoj s fokusom na integraciju Tailwind CSS-a.
- **Podrška za tablice/grafikone**: Dobra (zahtijeva integraciju s bibliotekama grafikona trećih strana).
- **Podrška za mreže/Gantt**: Minimalna.

### 4. **SkeletonUI**
- **Pregled**: SkeletonUI je lagana biblioteka komponenti za Svelte, usmjerena na jednostavnost i minimalizam.
- **Prednosti**:
  - Izuzetno lagan i brz.
  - Jednostavan i intuitivan API.
  - Dobar za male projekte ili gdje su performanse kritične.
- **Nedostaci**:
  - Uključeno je vrlo malo komponenti, pa nije bogat značajkama.
  - Nedostaju napredne komponente za tablice/mreže/grafikone/Gantt.
  - Ograničena podrška zajednice i manje opsežna dokumentacija.
- **Najbolje za**: Projekte koji zahtijevaju lagane komponente uz minimalno opterećenje.
- **Podrška za tablice/grafikone**: Minimalna.
- **Podrška za mreže/Gantt**: Minimalna.

### 5. **MeltUI**
- **Pregled**: MeltUI je zbirka pristupačnih UI komponenti za Svelte, usmjerenih na jednostavnost i kompozabilnost.
- **Prednosti**:
  - Lagan i potpuno prilagodljiv.
  - Dobre značajke pristupačnosti odmah po instalaciji.
  - Moderan i minimalistički dizajn.
- **Nedostaci**:
  - Manje bogat značajkama u usporedbi s drugim bibliotekama.
  - Nedostaju napredne komponente mreža i tablica.
  - Nema Ganttovih dijagrama ni složenih opcija grafikona.
- **Najbolje za**: Minimalističke dizajne koji daju prednost pristupačnosti i performansama.
- **Podrška za tablice/grafikone**: Minimalna.
- **Podrška za mreže/Gantt**: Minimalna.

### 6. **SvelteUI**
- **Pregled**: SvelteUI je sveobuhvatna i prilagodljiva biblioteka UI komponenti za Svelte, dizajnirana za izradu modernih web aplikacija s elegantnim UI-jem.
- **Prednosti**:
  - Sveobuhvatan skup komponenti, uključujući tablice, mreže, grafikone i obrasce.
  - Pruža podršku za svijetli i tamni način rada.
  - Vrlo prilagodljiv i lako proširiv.
  - Ugrađene integracije za biblioteke grafikona poput `chart.js` ili `d3.js`.
- **Nedostaci**:
  - Može biti teži od jednostavnijih biblioteka komponenti.
  - Zahtijeva određeno postavljanje za integraciju vanjskih biblioteka za složenije značajke poput Ganttovih dijagrama.
- **Najbolje za**: Projekte kojima je potreban sveobuhvatan, prilagodljiv skup komponenti.
- **Podrška za tablice/grafikone**: Izvrsna (podržane biblioteke grafikona).
- **Podrška za mreže/Gantt**: Dobra (komponente mreža dostupne; Gantt treba vanjsku integraciju).

### 7. **shadcn-svelte**
- **Pregled**: Svelte verzija ShadCN-a koja se usredotočuje na utility-first dizajn i pruža moderne, stilizirane komponente.
- **Prednosti**:
  - Utility-first dizajn, izgrađen na vrhu Tailwind CSS-a, što olakšava prilagodbu.
  - Bogat skup komponenti i potpuno stilizirane odmah po instalaciji.
  - Lako se integrira s drugim bibliotekama.
- **Nedostaci**:
  - Nije tako potpun u pogledu naprednih UI elemenata kao neki drugi.
  - Nedostaje ugrađena podrška za tablice, grafikone ili mreže.
  - Nema izvorne podrške za Ganttove dijagrame.
- **Najbolje za**: Male do srednje projekte koji zahtijevaju utility-first, prilagodljiv pristup.
- **Podrška za tablice/grafikone**: Minimalna.
- **Podrška za mreže/Gantt**: Minimalna.

## Odluka

### Preporučena opcija: **SvelteUI**

- **Obrazloženje**: SvelteUI nudi uravnotežen, sveobuhvatan paket komponenti koji zadovoljava potrebu za tablicama, grafikonima, mrežama i obrascima. Vrlo je prilagodljiv, dobro se integrira s drugim bibliotekama grafikona (poput `chart.js` i `d3.js`) i ima dobru ravnotežu lakih performansi i bogatstva značajki. Iako možda ne pruža izvornu podršku za Ganttove dijagrame, može se lako proširiti integracijama trećih strana, što ga čini idealnim za potpuno opremljeno, skalabilno rješenje.
  
  - **Prednosti**:
    - Izvrsna podrška za tablice i grafikone.
    - Pune komponente mreža i rasporeda.
    - Prilagodljiv i dobro se integrira s vanjskim bibliotekama grafikona.
    - Dobra zajednica i dokumentacija.
  
  - **Nedostaci**:
    - Teži od nekih drugih minimalističkih biblioteka.
    - Treba vanjsku integraciju za složene grafikone poput Ganttovih dijagrama.
  
### Alternativa: **Flowbite** ili **Carbon** (za veće enterprise projekte)
- Ako je potreban dotjeran dizajnerski sustav, temeljen na Tailwindu ili dosljedniji, **Flowbite** (s Tailwind CSS-om) ili **Carbon** (za rješenja razine enterprisea) mogu biti prikladne alternative. Međutim, mogu zahtijevati dodatni trud za integraciju sa složenijim grafikonima i komponentama.

## Zaključak

Najbolji izbor za vaše zahtjeve (pune značajke za tablice, grafikone, popise, mreže, Gantt) je **SvelteUI**, a slijede ga **Flowbite** i **Carbon** ovisno o potrebama projekta i dizajnerskim preferencijama.