# Svelte komponentide arhitektuuriotsuse kirje (ADR)

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Kontekst

Valime Svelte UI komponentide teeki, mis pakub täielikke funktsioone järgmiste jaoks:
- **Tabelid**
- **Diagrammid**
- **Loendid**
- **Ruudustikud**
- **Gantti diagrammid**

Eesmärk on valida teek, mis tasakaalustab integreerimise lihtsuse, täieliku funktsioonitoe, jõudluse ja pikaajalise hooldatavuse. Kaalutavad valikud on:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Valikute analüüs

### 1. **SVAR**
- **Ülevaade**: SVAR on kaasaegne, funktsioonirikas Svelte komponentide teek, mis keskendub disainisüsteemidele ja ettevõtteks valmis komponentidele.
- **Plussid**:
  - Täisfunktsionaalsed komponendid, sealhulgas tabelid, vormid ja diagrammid.
  - Kõrged kohandamisvõimalused sisseehitatud teematoega.
  - Sisseehitatud tugi ligipääsetavusele ja reageerivusele.
  - Hästi dokumenteeritud kogukonna panustega.
- **Miinused**:
  - Võib olla teiste lihtsamate teekidega võrreldes raskem.
  - Piiratud tugi konkreetsetele komponentidele nagu Gantti diagrammid ja täiustatud ruudustikud.
- **Parim**: ettevõtte taseme rakendused, kus on vaja täisfunktsionaalset disainisüsteemi.
- **Tabeli/diagrammi tugi**: mõõdukas kuni hea.
- **Ruudustiku/Gantti tugi**: minimaalne.

### 2. **Carbon**
- **Ülevaade**: Carbon Design System on IBM-i avatud lähtekoodiga disainisüsteem, mis pakub töökindlat UI komponentide komplekti.
- **Plussid**:
  - Kõrgekvaliteediline, viimistletud disain põhjaliku dokumentatsiooniga.
  - Väga ligipääsetav ja reageeriv.
  - Suur komponentide teek, sealhulgas ruudustikud, tabelid ja vormikontrollid.
- **Miinused**:
  - Ei keskendu Sveltele, seega võib integreerimine olla tülikas.
  - Võib nõuda täiendavat kohandamist täieliku Svelte ühilduvuse jaoks.
  - Puudub valmis tugi täiustatud komponentidele nagu Gantti diagrammid või keerukad diagrammid.
- **Parim**: suuremahulised projektid, mis nõuavad järjepidevat, viimistletud UI-d.
- **Tabeli/diagrammi tugi**: hea (diagrammiteekide integratsioonidega).
- **Ruudustiku/Gantti tugi**: hea (ruudustiku tugi saadaval, kuid Gantti diagramme pole).

### 3. **Flowbite**
- **Ülevaade**: Flowbite on Tailwind CSS-iga ehitatud komponentide teek, mis pakub erinevaid komponente ja UI elemente.
- **Plussid**:
  - Põhineb Tailwind CSS-il, mis teeb kohandamise lihtsaks.
  - Lihtne integreerida ja kasutada Sveltega.
  - Pakub rikkalikke komponente nagu tabelid, diagrammid ja UI juhtelemendid.
- **Miinused**:
  - Puuduvad täiustatud funktsioonid (nt Gantti diagrammid või keerukad ruudustikud).
  - Pole natiivseid diagrammikomponente; tugineb välistele teekidele.
- **Parim**: projektid, mis nõuavad kiiret arendust keskendumisega Tailwind CSS-i integratsioonile.
- **Tabeli/diagrammi tugi**: hea (nõuab integreerimist kolmandate osapoolte diagrammiteekidega).
- **Ruudustiku/Gantti tugi**: minimaalne.

### 4. **SkeletonUI**
- **Ülevaade**: SkeletonUI on kerge Svelte komponentide teek, mis keskendub lihtsusele ja minimalismile.
- **Plussid**:
  - Äärmiselt kerge ja kiire.
  - Lihtne ja intuitiivne API.
  - Hea väikestele projektidele või kus jõudlus on kriitiline.
- **Miinused**:
  - Kaasatud on väga vähe komponente, seega pole see funktsioonirikas.
  - Puuduvad täiustatud tabeli-/ruudustiku-/diagrammi-/Gantti komponendid.
  - Piiratud kogukonna toetus ja vähem põhjalik dokumentatsioon.
- **Parim**: projektid, mis nõuavad kergeid komponente minimaalse lisakoormusega.
- **Tabeli/diagrammi tugi**: minimaalne.
- **Ruudustiku/Gantti tugi**: minimaalne.

### 5. **MeltUI**
- **Ülevaade**: MeltUI on ligipääsetavate UI komponentide kogum Svelte jaoks, mis keskendub lihtsusele ja komponeeritavusele.
- **Plussid**:
  - Kerge ja täielikult kohandatav.
  - Head ligipääsetavusfunktsioonid karbist välja.
  - Kaasaegne ja minimalistlik disain.
- **Miinused**:
  - Vähem funktsioonirikas võrreldes teiste teekidega.
  - Puuduvad täiustatud ruudustiku- ja tabelikomponendid.
  - Pole Gantti diagramme ega keerukaid diagrammivalikuid.
- **Parim**: minimalistlikud disainid, mis seavad ligipääsetavuse ja jõudluse esikohale.
- **Tabeli/diagrammi tugi**: minimaalne.
- **Ruudustiku/Gantti tugi**: minimaalne.

### 6. **SvelteUI**
- **Ülevaade**: SvelteUI on põhjalik ja kohandatav UI komponentide teek Svelte jaoks, mis on loodud kaasaegsete veebirakenduste ehitamiseks elegantse UI-ga.
- **Plussid**:
  - Põhjalik komponentide komplekt, sealhulgas tabelid, ruudustikud, diagrammid ja vormid.
  - Pakub nii hele kui ka tume režiimi tuge.
  - Väga kohandatav ja hõlpsasti laiendatav.
  - Sisseehitatud integratsioonid diagrammiteekidega nagu `chart.js` või `d3.js`.
- **Miinused**:
  - Võib olla raskem kui lihtsamad komponentide teegid.
  - Nõuab mõningast seadistust väliste teekide integreerimiseks keerukamate funktsioonide jaoks nagu Gantti diagrammid.
- **Parim**: projektid, mis vajavad põhjalikku, kohandatavat komponentide komplekti.
- **Tabeli/diagrammi tugi**: suurepärane (diagrammiteegid toetatud).
- **Ruudustiku/Gantti tugi**: hea (ruudustiku komponendid saadaval; Gantt vajab välist integratsiooni).

### 7. **shadcn-svelte**
- **Ülevaade**: ShadCN-i Svelte versioon, mis keskendub utility-first disainile ja pakub kaasaegseid, stiilitud komponente.
- **Plussid**:
  - Utility-first disain, ehitatud Tailwind CSS-i peale, mis teeb kohandamise lihtsaks.
  - Rikkalik komponentide komplekt ja karbist välja täielikult stiilitud.
  - Lihtne integreerida teiste teekidega.
- **Miinused**:
  - Pole nii funktsioonitäielik kui mõned teised täiustatud UI elementide osas.
  - Puudub sisseehitatud tugi tabelitele, diagrammidele või ruudustikele.
  - Puudub valmis tugi Gantti diagrammidele.
- **Parim**: väikesed kuni keskmise suurusega projektid, mis nõuavad utility-first, kohandatavat lähenemist.
- **Tabeli/diagrammi tugi**: minimaalne.
- **Ruudustiku/Gantti tugi**: minimaalne.

## Otsus

### Soovitatud valik: **SvelteUI**

- **Põhjendus**: SvelteUI pakub tasakaalustatud, põhjalikku komponentide komplekti, mis vastab vajadusele tabelite, diagrammide, ruudustike ja vormide järele. See on väga kohandatav, integreerub hästi teiste diagrammiteekidega (nagu `chart.js` ja `d3.js`) ning sellel on hea tasakaal kerge jõudluse ja funktsioonirikkuse vahel. Kuigi see ei pruugi pakkuda valmis tuge Gantti diagrammidele, saab seda hõlpsasti kolmandate osapoolte integratsioonidega laiendada, muutes selle ideaalseks täisfunktsionaalse, skaleeritava lahenduse jaoks.
  
  - **Plussid**:
    - Suurepärane tabeli- ja diagrammitugi.
    - Täielikud ruudustiku- ja paigutuskomponendid.
    - Kohandatav ja integreerub hästi väliste diagrammiteekidega.
    - Hea kogukond ja dokumentatsioon.
  
  - **Miinused**:
    - Raskem kui mõned teised minimalistlikud teegid.
    - Vajab välist integratsiooni keerukate diagrammide jaoks nagu Gantti diagrammid.
  
### Alternatiiv: **Flowbite** või **Carbon** (suuremate ettevõtteprojektide jaoks)
- Kui on vaja viimistletud, Tailwindil põhinevat või järjepidevamat disainisüsteemi, võivad sobivad alternatiivid olla **Flowbite** (Tailwind CSS-iga) või **Carbon** (ettevõtte taseme lahenduste jaoks). Need võivad aga nõuda lisapingutust integratsioonideks keerukamate diagrammide ja komponentidega.

## Kokkuvõte

Parim sobivus sinu nõuetega (täielikud funktsioonid tabelite, diagrammide, loendite, ruudustike, Gantti jaoks) on **SvelteUI**, millele järgnevad **Flowbite** ja **Carbon**, sõltuvalt projekti vajadustest ja disaini eelistustest.
