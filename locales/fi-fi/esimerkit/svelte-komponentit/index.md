# Arkkitehtuuripäätöstietue (ADR) Svelte-komponenteille

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Konteksti

Valitsemme Svelte-käyttöliittymäkomponenttikirjastoa, joka tarjoaa täydet ominaisuudet:
- **Taulukoille**
- **Kaavioille**
- **Luetteloille**
- **Ruudukoille**
- **Gantt-kaavioille**

Tavoitteena on valita kirjasto, joka tasapainottaa integroinnin helppouden, täyden ominaisuustuen, suorituskyvyn ja pitkän aikavälin ylläpidettävyyden. Harkittavat vaihtoehdot ovat:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Vaihtoehtojen analyysi

### 1. **SVAR**
- **Yleiskuva**: SVAR on moderni, ominaisuuksiltaan rikas komponenttikirjasto Sveltelle, jonka painopiste on suunnittelujärjestelmissä ja yrityskäyttöön valmiissa komponenteissa.
- **Hyvät puolet**:
  - Täysin varustellut komponentit, mukaan lukien taulukot, lomakkeet ja kaaviot.
  - Korkeat mukautusvaihtoehdot sisäänrakennetulla teematuella.
  - Sisäänrakennettu tuki saavutettavuudelle ja responsiivisuudelle.
  - Hyvin dokumentoitu ja yhteisön panoksia sisältävä.
- **Huonot puolet**:
  - Voi olla raskaampi verrattuna muihin yksinkertaisempiin kirjastoihin.
  - Rajallinen tuki tietyille komponenteille, kuten Gantt-kaavioille ja edistyneille ruudukoille.
- **Sopii parhaiten**: Yritystason sovelluksiin, joissa tarvitaan täysi suunnittelujärjestelmä.
- **Taulukko-/kaaviotuki**: Kohtalainen–hyvä.
- **Ruudukko-/Gantt-tuki**: Vähäinen.

### 2. **Carbon**
- **Yleiskuva**: Carbon Design System on IBM:n avoimen lähdekoodin suunnittelujärjestelmä, joka tarjoaa vankan joukon käyttöliittymäkomponentteja.
- **Hyvät puolet**:
  - Korkealaatuinen, viimeistelty suunnittelu ja laaja dokumentaatio.
  - Erittäin saavutettava ja responsiivinen.
  - Suuri komponenttikirjasto, mukaan lukien ruudukot, taulukot ja lomakeohjaimet.
- **Huonot puolet**:
  - Ei keskity Svelteen, joten integrointi voi olla hankalaa.
  - Voi vaatia lisämukautusta täyden Svelte-yhteensopivuuden saavuttamiseksi.
  - Ei valmista tukea edistyneille komponenteille, kuten Gantt-kaavioille tai monimutkaisille kaavioille.
- **Sopii parhaiten**: Suuriin projekteihin, jotka vaativat yhdenmukaisen, viimeistellyn käyttöliittymän.
- **Taulukko-/kaaviotuki**: Hyvä (kaaviokirjastointegraatioilla).
- **Ruudukko-/Gantt-tuki**: Hyvä (ruudukkotuki saatavilla, mutta ei Gantt-kaavioita).

### 3. **Flowbite**
- **Yleiskuva**: Flowbite on Tailwind CSS:llä rakennettu komponenttikirjasto, joka tarjoaa erilaisia komponentteja ja käyttöliittymäelementtejä.
- **Hyvät puolet**:
  - Tailwind CSS -pohjainen, mikä tekee mukauttamisesta helppoa.
  - Helppo integroida ja käyttää Sveltellä.
  - Tarjoaa rikkaita komponentteja, kuten taulukoita, kaavioita ja käyttöliittymäohjaimia.
- **Huonot puolet**:
  - Puuttuvat edistyneet ominaisuudet (esim. Gantt-kaaviot tai monimutkaiset ruudukot).
  - Ei natiiveja kaaviokomponentteja; luottaa ulkoisiin kirjastoihin.
- **Sopii parhaiten**: Projekteihin, jotka vaativat nopeaa kehitystä ja keskittyvät Tailwind CSS -integraatioon.
- **Taulukko-/kaaviotuki**: Hyvä (vaatii integroinnin kolmannen osapuolen kaaviokirjastoihin).
- **Ruudukko-/Gantt-tuki**: Vähäinen.

### 4. **SkeletonUI**
- **Yleiskuva**: SkeletonUI on kevyt komponenttikirjasto Sveltelle, joka keskittyy yksinkertaisuuteen ja minimalismiin.
- **Hyvät puolet**:
  - Erittäin kevyt ja nopea.
  - Yksinkertainen ja intuitiivinen API.
  - Hyvä pienille projekteille tai silloin, kun suorituskyky on kriittistä.
- **Huonot puolet**:
  - Mukana on hyvin vähän komponentteja, joten se ei ole ominaisuuksiltaan rikas.
  - Puuttuvat edistyneet taulukko-/ruudukko-/kaavio-/Gantt-komponentit.
  - Rajallinen yhteisön tuki ja vähemmän kattava dokumentaatio.
- **Sopii parhaiten**: Projekteihin, jotka tarvitsevat kevyitä komponentteja minimaalisella kuormituksella.
- **Taulukko-/kaaviotuki**: Vähäinen.
- **Ruudukko-/Gantt-tuki**: Vähäinen.

### 5. **MeltUI**
- **Yleiskuva**: MeltUI on kokoelma saavutettavia käyttöliittymäkomponentteja Sveltelle, joka keskittyy yksinkertaisuuteen ja yhdisteltävyyteen.
- **Hyvät puolet**:
  - Kevyt ja täysin mukautettavissa.
  - Hyvät saavutettavuusominaisuudet heti käyttöön otettaessa.
  - Moderni ja minimalistinen ulkoasu.
- **Huonot puolet**:
  - Vähemmän ominaisuuksia verrattuna muihin kirjastoihin.
  - Puuttuvat edistyneet ruudukko- ja taulukkokomponentit.
  - Ei Gantt-kaavioita eikä monimutkaisia kaaviovaihtoehtoja.
- **Sopii parhaiten**: Minimalistisiin suunnitelmiin, jotka priorisoivat saavutettavuutta ja suorituskykyä.
- **Taulukko-/kaaviotuki**: Vähäinen.
- **Ruudukko-/Gantt-tuki**: Vähäinen.

### 6. **SvelteUI**
- **Yleiskuva**: SvelteUI on kattava ja mukautettava käyttöliittymäkomponenttikirjasto Sveltelle, joka on suunniteltu nykyaikaisten verkkosovellusten rakentamiseen tyylikkäällä käyttöliittymällä.
- **Hyvät puolet**:
  - Kattava komponenttijoukko, mukaan lukien taulukot, ruudukot, kaaviot ja lomakkeet.
  - Tarjoaa sekä vaalean että tumman tilan tuen.
  - Erittäin mukautettavissa ja helppo laajentaa.
  - Sisäänrakennetut integraatiot kaaviokirjastoihin, kuten `chart.js` tai `d3.js`.
- **Huonot puolet**:
  - Voi olla raskaampi kuin yksinkertaisemmat komponenttikirjastot.
  - Vaatii jonkin verran käyttöönottoa ulkoisten kirjastojen integroimiseksi monimutkaisempia ominaisuuksia, kuten Gantt-kaavioita, varten.
- **Sopii parhaiten**: Projekteihin, jotka tarvitsevat kattavan, mukautettavan komponenttijoukon.
- **Taulukko-/kaaviotuki**: Erinomainen (kaaviokirjastot tuettu).
- **Ruudukko-/Gantt-tuki**: Hyvä (ruudukkokomponentit saatavilla; Gantt vaatii ulkoisen integroinnin).

### 7. **shadcn-svelte**
- **Yleiskuva**: ShadCN:n Svelte-versio, joka keskittyy apuluokkapainotteiseen (utility-first) suunnitteluun ja tarjoaa nykyaikaisia, tyyliteltyjä komponentteja.
- **Hyvät puolet**:
  - Apuluokkapainotteinen suunnittelu, rakennettu Tailwind CSS:n päälle, mikä tekee mukauttamisesta helppoa.
  - Rikas komponenttijoukko ja täysin tyylitelty heti käyttöön otettaessa.
  - Helppo integroida muihin kirjastoihin.
- **Huonot puolet**:
  - Ei yhtä täydellinen ominaisuuksiltaan kuin jotkin muut edistyneiden käyttöliittymäelementtien osalta.
  - Puuttuu sisäänrakennettu tuki taulukoille, kaavioille tai ruudukoille.
  - Ei valmista tukea Gantt-kaavioille.
- **Sopii parhaiten**: Pieniin tai keskisuuriin projekteihin, jotka vaativat apuluokkapainotteisen, mukautettavan lähestymistavan.
- **Taulukko-/kaaviotuki**: Vähäinen.
- **Ruudukko-/Gantt-tuki**: Vähäinen.

## Päätös

### Suositeltu vaihtoehto: **SvelteUI**

- **Perustelut**: SvelteUI tarjoaa tasapainoisen, kattavan komponenttisarjan, joka vastaa taulukoiden, kaavioiden, ruudukoiden ja lomakkeiden tarpeeseen. Se on erittäin mukautettavissa, integroituu hyvin muihin kaaviokirjastoihin (kuten `chart.js` ja `d3.js`) ja sillä on hyvä tasapaino kevyen suorituskyvyn ja ominaisuuksien rikkauden välillä. Vaikka se ei välttämättä tarjoa valmista Gantt-kaaviotukea, sitä voidaan helposti laajentaa kolmansien osapuolten integraatioilla, mikä tekee siitä ihanteellisen täysiominaisuuksiseen, skaalautuvaan ratkaisuun.
  
  - **Hyvät puolet**:
    - Erinomainen taulukko- ja kaaviotuki.
    - Täydet ruudukko- ja asettelukomponentit.
    - Mukautettavissa ja integroituu hyvin ulkoisiin kaaviokirjastoihin.
    - Hyvä yhteisö ja dokumentaatio.
  
  - **Huonot puolet**:
    - Raskaampi kuin jotkin muut minimalistiset kirjastot.
    - Tarvitsee ulkoisen integroinnin monimutkaisille kaavioille, kuten Gantt-kaavioille.
  
### Vaihtoehto: **Flowbite** tai **Carbon** (suurempiin yritysprojekteihin)
- Jos tarvitaan viimeisteltyä, Tailwind-pohjaista tai yhdenmukaisempaa suunnittelujärjestelmää, **Flowbite** (Tailwind CSS:llä) tai **Carbon** (yritystason ratkaisuihin) voivat olla sopivia vaihtoehtoja. Ne voivat kuitenkin vaatia lisävaivaa integraatioihin monimutkaisempien kaavioiden ja komponenttien kanssa.

## Johtopäätös

Vaatimuksiisi (täydet ominaisuudet taulukoille, kaavioille, luetteloille, ruudukoille, Gantt-kaavioille) parhaiten sopiva on **SvelteUI**, jota seuraavat **Flowbite** ja **Carbon** projektin tarpeista ja suunnitteluasetuksista riippuen.
