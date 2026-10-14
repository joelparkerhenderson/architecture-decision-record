# Arkitektúrákvörðunarskrá (ADR) fyrir Svelte-íhluti

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Samhengi

Við erum að velja safn viðmótsíhluta fyrir Svelte sem veitir alla eiginleika fyrir:
- **Töflur**
- **Myndrit**
- **Lista**
- **Ristar**
- **Gantt-rit**

Markmiðið er að velja safn sem jafnar auðvelda samþættingu, fullan eiginleikastuðning, afköst og langtímaviðhaldshæfni. Valkostirnir sem eru til skoðunar eru:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Greining valkosta

### 1. **SVAR**
- **Yfirlit**: SVAR er nútímalegt, eiginleikaríkt íhlutasafn fyrir Svelte, með áherslu á hönnunarkerfi og íhluti tilbúna fyrir fyrirtæki.
- **Kostir**:
  - Fullbúnir íhlutir, þar á meðal töflur, eyðublöð og myndrit.
  - Mikil sérsníðun með innbyggðum stuðningi við þemu.
  - Innbyggður stuðningur við aðgengi og svörunarfúsa framsetningu.
  - Vel skjalfest með framlögum frá samfélaginu.
- **Gallar**:
  - Gæti verið þyngra en önnur einfaldari söfn.
  - Takmarkaður stuðningur við tiltekna íhluti eins og Gantt-rit og háþróaðar ristar.
- **Best fyrir**: Forrit á fyrirtækjastigi þar sem fullbúið hönnunarkerfi er nauðsynlegt.
- **Stuðningur við töflur/myndrit**: Miðlungs til góður.
- **Stuðningur við ristar/Gantt**: Lágmarks.

### 2. **Carbon**
- **Yfirlit**: Carbon Design System er opið hönnunarkerfi frá IBM sem býður upp á öflugt safn viðmótsíhluta.
- **Kostir**:
  - Hágæða, fáguð hönnun með ítarlegri skjölun.
  - Mjög aðgengilegt og svörunarfúst.
  - Stórt íhlutasafn, þar á meðal ristar, töflur og eyðublaðastýringar.
- **Gallar**:
  - Beinist ekki að Svelte, svo samþætting getur verið óþjál.
  - Gæti krafist frekari sérsníðunar fyrir fulla samhæfni við Svelte.
  - Enginn innbyggður stuðningur við háþróaða íhluti eins og Gantt-rit eða flókin myndrit.
- **Best fyrir**: Stór verkefni sem krefjast samræmds, fágaðs viðmóts.
- **Stuðningur við töflur/myndrit**: Góður (með samþættingu myndritasafna).
- **Stuðningur við ristar/Gantt**: Góður (stuðningur við ristar er til staðar, en engin Gantt-rit).

### 3. **Flowbite**
- **Yfirlit**: Flowbite er íhlutasafn smíðað með Tailwind CSS sem býður upp á ýmsa íhluti og viðmótsþætti.
- **Kostir**:
  - Byggt á Tailwind CSS, sem gerir auðvelt að sérsníða.
  - Auðvelt að samþætta og nota með Svelte.
  - Býður upp á ríka íhluti eins og töflur, myndrit og viðmótsstýringar.
- **Gallar**:
  - Skortir háþróaða eiginleika (t.d. Gantt-rit eða flóknar ristar).
  - Hefur ekki innbyggða myndritaíhluti; reiðir sig á ytri söfn.
- **Best fyrir**: Verkefni sem krefjast hraðrar þróunar með áherslu á samþættingu við Tailwind CSS.
- **Stuðningur við töflur/myndrit**: Góður (krefst samþættingar við myndritasöfn þriðju aðila).
- **Stuðningur við ristar/Gantt**: Lágmarks.

### 4. **SkeletonUI**
- **Yfirlit**: SkeletonUI er létt íhlutasafn fyrir Svelte sem leggur áherslu á einfaldleika og naumhyggju.
- **Kostir**:
  - Afar létt og hratt.
  - Einfalt og innsæislegt API.
  - Gott fyrir lítil verkefni eða þar sem afköst skipta sköpum.
- **Gallar**:
  - Mjög fáir íhlutir eru innifaldir, svo það er ekki eiginleikaríkt.
  - Skortir háþróaða töflu-/ristar-/myndrita-/Gantt-íhluti.
  - Takmarkaður stuðningur samfélagsins og minna ítarleg skjölun.
- **Best fyrir**: Verkefni sem krefjast léttra íhluta með lágmarks yfirbyggingu.
- **Stuðningur við töflur/myndrit**: Lágmarks.
- **Stuðningur við ristar/Gantt**: Lágmarks.

### 5. **MeltUI**
- **Yfirlit**: MeltUI er safn aðgengilegra viðmótsíhluta fyrir Svelte sem leggur áherslu á einfaldleika og samsetningarhæfni.
- **Kostir**:
  - Létt og fullkomlega sérsníðanlegt.
  - Góðir aðgengiseiginleikar frá upphafi.
  - Nútímaleg og naumhyggjuleg hönnun.
- **Gallar**:
  - Minna eiginleikaríkt miðað við önnur söfn.
  - Skortir háþróaða ristar- og töfluíhluti.
  - Engin Gantt-rit eða flóknir myndritamöguleikar.
- **Best fyrir**: Naumhyggjulega hönnun sem setur aðgengi og afköst í forgang.
- **Stuðningur við töflur/myndrit**: Lágmarks.
- **Stuðningur við ristar/Gantt**: Lágmarks.

### 6. **SvelteUI**
- **Yfirlit**: SvelteUI er alhliða og sérsníðanlegt viðmótsíhlutasafn fyrir Svelte, hannað til að smíða nútímaleg vefforrit með fáguðu viðmóti.
- **Kostir**:
  - Alhliða safn íhluta, þar á meðal töflur, ristar, myndrit og eyðublöð.
  - Býður upp á stuðning við bæði ljósa og dökka stillingu.
  - Mjög sérsníðanlegt og auðvelt að víkka út.
  - Innbyggðar samþættingar við myndritasöfn eins og `chart.js` eða `d3.js`.
- **Gallar**:
  - Getur verið þyngra en einfaldari íhlutasöfn.
  - Krefst nokkurrar uppsetningar til að samþætta ytri söfn fyrir flóknari eiginleika eins og Gantt-rit.
- **Best fyrir**: Verkefni sem þurfa alhliða, sérsníðanlegt safn íhluta.
- **Stuðningur við töflur/myndrit**: Framúrskarandi (myndritasöfn studd).
- **Stuðningur við ristar/Gantt**: Góður (ristaríhlutir í boði; Gantt krefst ytri samþættingar).

### 7. **shadcn-svelte**
- **Yfirlit**: Svelte-útgáfa af ShadCN, sem leggur áherslu á hönnun þar sem nytjaflokkar koma fyrst og býður upp á nútímalega, stílaða íhluti.
- **Kostir**:
  - Hönnun þar sem nytjaflokkar koma fyrst, byggð ofan á Tailwind CSS, sem gerir auðvelt að sérsníða.
  - Ríkt safn íhluta og fullkomlega stílað frá upphafi.
  - Auðvelt að samþætta við önnur söfn.
- **Gallar**:
  - Ekki jafn fullbúið og sum önnur hvað varðar háþróaða viðmótsþætti.
  - Skortir innbyggðan stuðning við töflur, myndrit eða ristar.
  - Enginn innbyggður stuðningur við Gantt-rit.
- **Best fyrir**: Lítil til meðalstór verkefni sem krefjast sérsníðanlegrar nálgunar þar sem nytjaflokkar koma fyrst.
- **Stuðningur við töflur/myndrit**: Lágmarks.
- **Stuðningur við ristar/Gantt**: Lágmarks.

## Ákvörðun

### Ráðlagður valkostur: **SvelteUI**

- **Rökstuðningur**: SvelteUI býður upp á vel ávalið, alhliða safn íhluta sem mætir þörfinni fyrir töflur, myndrit, ristar og eyðublöð. Það er mjög sérsníðanlegt, samþættist vel við önnur myndritasöfn (eins og `chart.js` og `d3.js`) og hefur gott jafnvægi léttra afkasta og eiginleikaauðgi. Þótt það veiti ekki innbyggðan stuðning við Gantt-rit er auðvelt að víkka það út með samþættingum þriðju aðila, sem gerir það tilvalið fyrir fullbúna, stigstæða lausn.
  
  - **Kostir**:
    - Framúrskarandi stuðningur við töflur og myndrit.
    - Fullir ristar- og útlitsíhlutir.
    - Sérsníðanlegt og samþættist vel við ytri myndritasöfn.
    - Gott samfélag og skjölun.
  
  - **Gallar**:
    - Þyngra en sum önnur naumhyggjusöfn.
    - Þarf ytri samþættingu fyrir flókin myndrit eins og Gantt-rit.
  
### Valkostur: **Flowbite** eða **Carbon** (fyrir stærri fyrirtækjaverkefni)
- Ef þörf er á fáguðu, Tailwind-byggðu eða samræmdara hönnunarkerfi geta **Flowbite** (með Tailwind CSS) eða **Carbon** (fyrir lausnir á fyrirtækjastigi) verið hentugir valkostir. Þeir gætu hins vegar krafist aukinnar fyrirhafnar við samþættingu við flóknari myndrit og íhluti.

## Niðurstaða

Besta passunin fyrir kröfur þínar (fullir eiginleikar fyrir töflur, myndrit, lista, ristar, Gantt) er **SvelteUI**, og síðan **Flowbite** og **Carbon** eftir þörfum verkefnisins og hönnunarvali.