# Arkkitehtuuripäätöstietue (ADR)

Arkkitehtuuripäätöstietue (ADR) on dokumentti, joka kirjaa tärkeän arkkitehtuuripäätöksen yhdessä sen taustan ja seurausten kanssa.

> [!IMPORTANT]
> Tee omat tarvittavat selvityksesi näistä resursseista ennen kuin käytät niitä kriittisissä järjestelmissä.

Sisällys:

- [Mikä on arkkitehtuuripäätöstietue?](#mikä-on-arkkitehtuuripäätöstietue)
- [Kuinka aloittaa ADR-tietueiden käyttö](#kuinka-aloittaa-adr-tietueiden-käyttö)
- [Kuinka aloittaa ADR-tietueiden käyttö työkaluilla](#kuinka-aloittaa-adr-tietueiden-käyttö-työkaluilla)
- [Kuinka aloittaa ADR-tietueiden käyttö gitillä](#kuinka-aloittaa-adr-tietueiden-käyttö-gitillä)
- [Claude Code -taidot ADR-tietueille](#claude-code--taidot-adr-tietueille)
- [Tiedostojen nimeämiskäytännöt](#tiedostojen-nimeämiskäytännöt)
- [Ehdotuksia hyvien ADR-tietueiden kirjoittamiseen](#ehdotuksia-hyvien-adr-tietueiden-kirjoittamiseen)
- [ADR-esimerkkimallipohjat](#adr-esimerkkimallipohjat)
- [Tiimityön neuvoja ADR-tietueille](#tiimityön-neuvoja-adr-tietueille)
- [Tiimityökysymykset ADR-tietueille](#tiimityökysymykset-adr-tietueille)
- [ADR-tietueiden seuraavan askeleen käsitteet](#adr-tietueiden-seuraavan-askeleen-käsitteet)
- [Arkkitehtuurikaaviot, näkymät ja näkökulmat](#arkkitehtuurikaaviot-näkymät-ja-näkökulmat)
- [Sopivuusfunktiot koodina ilmaistuille päätöksille](#sopivuusfunktiot-koodina-ilmaistuille-päätöksille)
- [Päätösten suojakaiteet vetopyynnöille](#päätösten-suojakaiteet-vetopyynnöille)
- [Lisätietoja](#lisätietoja)

Mallipohjat:

- [Päätöstietueen mallipohja: Jeff Tyree ja Art Akerman](mallipohjat/päätöstietueen-mallipohja-jeff-tyree-ja-art-akerman/)
- [Päätöstietueen mallipohja: Michael Nygard](mallipohjat/päätöstietueen-mallipohja-michael-nygard/)
- [Päätöstietueen mallipohja: EdgeX](mallipohjat/päätöstietueen-mallipohja-edgex/)
- [Päätöstietueen mallipohja: arc42](mallipohjat/päätöstietueen-mallipohja-arc42/)
- [Päätöstietueen mallipohja: alexanderilainen malli](mallipohjat/päätöstietueen-mallipohja-alexanderilainen-malli/)
- [Päätöstietueen mallipohja: liiketoimintaperustelu](mallipohjat/päätöstietueen-mallipohja-liiketoimintaperustelu/)
- [Päätöstietueen mallipohja: MADR-projekti](mallipohjat/päätöstietueen-mallipohja-madr-projekti/)
- [Päätöstietueen mallipohja: Planguage](mallipohjat/päätöstietueen-mallipohja-planguage/)
- [Paulo Mersonin päätöstietueen mallipohja](https://github.com/pmerson/ADR-template)
- [Olaf Zimmermannin päätöstietueen mallipohja](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Päätöstietueen mallipohja: Gareth Morgan](mallipohjat/päätöstietueen-mallipohja-gareth-morgan/)
- [Päätöstietueen mallipohja: GIG Cymru NHS Wales](mallipohjat/päätöstietueen-mallipohja-gig-cymru/)
- [Päätöstietueen mallipohja: tärkeät tekniset päätökset (ITD), Ignacio Larrañaga](mallipohjat/päätöstietueen-mallipohja-tärkeät-tekniset-päätökset/)

Esimerkit:

- [CSS-kehys](esimerkit/css-kehys/)
- [Ympäristömuuttujien konfigurointi](esimerkit/ympäristömuuttujien-konfigurointi/)
- [Mittarit, seuranta, hälytykset](esimerkit/mittarit-seuranta-hälytykset/)
- [Microsoft Azure DevOps](esimerkit/microsoft-azure-devops/)
- [Monorepo vai multirepo](esimerkit/monorepo-vai-multirepo/)
- [Ohjelmointikielet](esimerkit/ohjelmointikielet/)
- [Salaisuuksien tallennus](esimerkit/salaisuuksien-tallennus/)
- [Aikaleiman muoto](esimerkit/aikaleiman-muoto/)
- [Paljon lisää...](esimerkit/)

## Mikä on arkkitehtuuripäätöstietue?

**Arkkitehtuuripäätöstietue** (ADR) on dokumentti, joka kirjaa tärkeän arkkitehtuuripäätöksen yhdessä sen kontekstin ja seurausten kanssa.

**Arkkitehtuuripäätös** (AD) on ohjelmistosuunnittelun valinta, joka vastaa merkittävään vaatimukseen.

**Arkkitehtuuripäätösloki** (ADL) on kokoelma kaikista tietyssä projektissa (tai organisaatiossa) luoduista ja ylläpidetyistä ADR-tietueista.

**Arkkitehtuurin kannalta merkittävä vaatimus** (ASR) on vaatimus, jolla on mitattavissa oleva vaikutus ohjelmistojärjestelmän arkkitehtuuriin.

Kaikki nämä kuuluvat **arkkitehtuuritiedon hallinnan** (AKM) aihepiiriin.

Tämän dokumentin tavoitteena on antaa nopea yleiskuva ADR-tietueista, niiden luomisesta ja siitä, mistä löytää lisätietoa.

Lyhenteet:

  * **AD**: arkkitehtuuripäätös

  * **ADL**: arkkitehtuuripäätösloki

  * **ADR**: arkkitehtuuripäätöstietue

  * **AKM**: arkkitehtuuritiedon hallinta

  * **ASR**: arkkitehtuurin kannalta merkittävä vaatimus

## Kuinka aloittaa ADR-tietueiden käyttö

ADR-tietueiden käytön aloittamiseksi keskustele tiimikavereidesi kanssa näistä alueista.

Päätösten tunnistaminen:

  * Kuinka kiireellinen ja kuinka tärkeä AD on?

  * Pitääkö se tehdä nyt, vai voiko se odottaa, kunnes tiedetään enemmän?

  * Sekä henkilökohtainen ja yhteinen kokemus että tunnustetut suunnittelumenetelmät ja -käytännöt voivat auttaa päätösten tunnistamisessa.

  * Ihannetapauksessa ylläpidetään päätöslistaa, joka täydentää tuotteen tehtävälistaa.

Päätöksenteko:

  * Päätöksentekoon on olemassa useita tekniikoita, sekä yleisiä että ohjelmistoarkkitehtuurille ominaisia, esimerkiksi dialogikartoitus.

  * Ryhmäpäätöksenteko on aktiivinen tutkimusaihe.

Päätösten toimeenpano ja valvonta:

  * AD-päätöksiä käytetään ohjelmistosuunnittelussa; siksi ne on viestittävä järjestelmän sidosryhmille, jotka rahoittavat, kehittävät ja käyttävät sitä, ja näiden on hyväksyttävä ne.

  * Arkkitehtuurin selvästi näkyvään tekevät koodaustyylit sekä arkkitehtuurikysymyksiin ja -päätöksiin keskittyvät koodikatselmoinnit ovat kaksi toisiinsa liittyvää käytäntöä.

  * AD-päätökset on myös otettava (uudelleen) harkittavaksi, kun ohjelmistojärjestelmää modernisoidaan ohjelmiston kehittyessä.

Päätösten jakaminen (valinnainen):

  * Monet AD-päätökset toistuvat projektista toiseen.

  * Siksi aiempien päätösten kokemukset, sekä hyvät että huonot, voivat olla arvokkaita uudelleenkäytettäviä voimavaroja, kun käytetään nimenomaista tiedonhallintastrategiaa.

Päätösten dokumentointi:

  * Päätösten kirjaamiseen on olemassa monia mallipohjia ja työkaluja.

  * Katso ketterät yhteisöt, esim. M. Nygardin ADR-tietueet.

  * Katso perinteiset ohjelmistotuotannon ja arkkitehtuurisuunnittelun prosessit, esim. IBM UMF:n sekä CapitalOnen Tyreen ja Akermanin ehdottamat taulukkoasettelut.

Lisätietoa:

  * Yllä olevat vaiheet on otettu Wikipedian artikkelista [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Kuinka aloittaa ADR-tietueiden käyttö työkaluilla

- [MySpec](https://myspec.dev) — Automatisoitu määrittely- ja arkkitehtuuripäätösalusta, joka jäsentää projektin perustan, tekniset arkkitehtuurit ja ADR-tietueet selkeäksi Markdowniksi, jota tarjotaan MCP:n kautta.

Voit aloittaa ADR-tietueiden käytön työkaluilla millä tavalla haluat.

Esimerkiksi:

  * Jos pidät Google Drivesta ja verkossa muokkaamisesta, voit luoda Google Docs -dokumentin tai Google Sheets -taulukon.

  * Jos pidät lähdekoodin versionhallinnasta, kuten gitistä, voit luoda tiedoston jokaista ADR-tietuetta varten.

  * Jos pidät projektinhallintatyökaluista, kuten Atlassian Jirasta, voit käyttää työkalun suunnittelun seurantaa.

  * Jos pidät wikeistä, kuten MediaWikistä, voit luoda ADR-wikin.

## Kuinka aloittaa ADR-tietueiden käyttö gitillä

Jos pidät git-versionhallinnasta, tässä on tapa, jolla aloitamme mielellämme ADR-tietueiden käytön gitillä tyypillisessä ohjelmistoprojektissa, jossa on lähdekoodia.

Luo hakemisto ADR-tiedostoille:

```sh
$ mkdir adr
```

Luo jokaista ADR-tietuetta varten tekstitiedosto, esimerkiksi `database.txt`:

```sh
$ vi database.txt
```

Kirjoita ADR-tietueeseen mitä haluat. Katso tämän tietovaraston mallipohjista ideoita.

Tallenna (commit) ADR-tietue git-tietovarastoosi.

## Claude Code -taidot ADR-tietueille

Tämä tietovarasto sisältää kaksi [Claude Code](https://claude.com/claude-code) -taitoa (skill) kansiossa [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), jotta tekoälyohjelmointiagentti voi kirjoittaa ja ylläpitää ADR-tietueita tämän projektin suosittelemalla tavalla:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — yleiskäyttöinen, kenelle tahansa, joka kirjoittaa ADR-tietueen missä tahansa projektissa. Auttaa päättämään, tarvitseeko päätös ADR-tietueen, luo `adr/`- tai `decisions/`-hakemiston, nimeää tiedoston, valitsee mallipohjan yhdestätoista mukana tulevasta rungosta ja kirjoittaa vankat tausta-, päätös- ja seuraukset-osiot.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — erityisesti tämän tietovaraston ylläpitäjille. Dokumentoi tietovaraston rakenteen, README- ja locales-peilauksen käytännön sekä tarkat vaiheet uuden mallipohjan, esimerkin tai työkalulinkin lisäämiseen.

Käyttääksesi taitoa kopioi sen kansio työskentelemäsi tietovaraston juuressa olevaan `.claude/skills/`-kansioon (tai kansioon `~/.claude/skills/`, jotta se on käytettävissä jokaisessa projektissa) ja pyydä sitten Claude Codea kirjoittamaan tai tarkistamaan ADR-tietue.

## Tiedostojen nimeämiskäytännöt

Jos luot ADR-tietueesi tavallisina tekstitiedostoina, saatat haluta keksiä oman ADR-tiedostojen nimeämiskäytäntösi.

Suosimme nimeämiskäytäntöä, jolla on tietty muoto.

Esimerkkejä:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Meidän nimeämiskäytäntömme:

  * Nimi sisältää preesensissä olevan käskymuotoisen verbilausekkeen. Tämä parantaa luettavuutta ja vastaa commit-viestiemme muotoa.

  * Nimessä käytetään pieniä kirjaimia ja tavuviivoja (kuten tässä tietovarastossa). Tämä on tasapaino luettavuuden ja järjestelmän käytettävyyden välillä.

  * Tiedostopääte on markdown. Tämä voi olla hyödyllistä helpon muotoilun vuoksi.

## Ehdotuksia hyvien ADR-tietueiden kirjoittamiseen

Hyvän ADR-tietueen ominaisuudet:

* Perustelut: Selitä syyt kyseisen AD-päätöksen tekemiselle. Tähän voi kuulua konteksti (katso alla), eri vaihtoehtojen hyvät ja huonot puolet, ominaisuusvertailut, kustannus–hyöty-keskustelut ja paljon muuta.

* Täsmällinen: Jokaisen ADR-tietueen tulisi koskea yhtä AD-päätöstä, ei useita.

* Aikaleimat: Merkitse, milloin kukin ADR-tietueen kohta on kirjoitettu. Tämä on erityisen tärkeää seikoille, jotka voivat muuttua ajan myötä, kuten kustannukset, aikataulut, skaalautuminen ja vastaavat.

* Muuttumaton: Älä muuta ADR-tietueessa jo olevaa tietoa. Sen sijaan täydennä ADR-tietuetta lisäämällä uutta tietoa tai korvaa ADR-tietue luomalla uusi ADR-tietue.

Hyvän "Konteksti"-osion ominaisuudet ADR-tietueessa:

* Selitä organisaatiosi tilanne ja liiketoiminnan prioriteetit.

* Sisällytä perustelut ja huomiot, jotka perustuvat tiimiesi sosiaaliseen koostumukseen ja osaamiseen.

* Sisällytä olennaiset hyvät ja huonot puolet ja kuvaile ne tavalla, joka vastaa tarpeitasi ja tavoitteitasi.

Hyvän "Seuraukset"-osion ominaisuudet ADR-tietueessa:

* Selitä, mitä päätöksen tekemisestä seuraa. Tähän voi kuulua vaikutukset, tulokset, tuotokset, jatkotoimet ja paljon muuta.

* Sisällytä tietoa mahdollisista myöhemmistä ADR-tietueista. On suhteellisen tavallista, että yksi ADR-tietue synnyttää tarpeen useammille ADR-tietueille, esimerkiksi kun yksi ADR-tietue tekee ison kattavan valinnan, joka puolestaan synnyttää tarpeen useille pienemmille päätöksille.

* Sisällytä mahdolliset jälkikäteisarviointiprosessit. On tavallista, että tiimit arvioivat jokaisen ADR-tietueen kuukauden kuluttua verratakseen ADR-tietueen tietoja siihen, mitä käytännössä on tapahtunut, oppiakseen ja kehittyäkseen.

Uusi ADR-tietue voi korvata aiemman ADR-tietueen:

* Kun tehdään AD, joka korvaa tai mitätöi aiemman ADR-tietueen, tulisi luoda uusi ADR-tietue

## ADR-esimerkkimallipohjat

Verkosta keräämiämme ADR-esimerkkimallipohjia:

- [Michael Nygardin ADR-mallipohja](mallipohjat/päätöstietueen-mallipohja-michael-nygard/) (yksinkertainen ja suosittu)

- [Jeff Tyreen ja Art Akermanin ADR-mallipohja](mallipohjat/päätöstietueen-mallipohja-jeff-tyree-ja-art-akerman/) (hienostuneempi)

- [ADR-mallipohja Alexandrian-mallille](mallipohjat/päätöstietueen-mallipohja-alexanderilainen-malli/) (yksinkertainen, taustan yksityiskohdilla)

- [ADR-mallipohja liiketoimintatapaukselle](mallipohjat/päätöstietueen-mallipohja-liiketoimintaperustelu/) (enemmän MBA-painotteinen, kustannuksilla, SWOT-analyysilla ja useammilla mielipiteillä)

- [Markdown Any Decision Records (MADR) -projektin ADR-mallipohja](mallipohjat/päätöstietueen-mallipohja-madr-projekti/) (sekä yksinkertainen että laaja versio; jälkimmäinen korostaa vaihtoehtoja ja niiden hyviä ja huonoja puolia)

- [Planguagea käyttävä ADR-mallipohja](mallipohjat/päätöstietueen-mallipohja-planguage/) (enemmän laadunvarmistukseen suuntautunut)

- [Ignacio Larrañagan mallipohja tärkeille teknisille päätöksille (ITD)](mallipohjat/päätöstietueen-mallipohja-tärkeät-tekniset-päätökset/) (kevyt ja päätös edellä, optimoitu nopeaan johdon arviointiin)

## Tiimityön neuvoja ADR-tietueille

Jos harkitset päätöstietueiden käyttöä tiimisi kanssa, tässä on neuvoja, jotka olemme oppineet työskennellessämme monien tiimien kanssa.

Sinulla on mahdollisuus johtaa tiimikaverejasi keskustelemalla yhdessä "miksi"-kysymyksestä sen sijaan, että määräisit "mitä". Esimerkiksi päätöstietueet ovat tapa, jolla tiimit voivat ajatella älykkäämmin ja viestiä paremmin; päätöstietueet eivät ole arvokkaita, jos ne ovat vain jälkikäteen pakotettu paperityövaatimus.

Jotkut tiimit pitävät nimestä "päätökset" paljon enemmän kuin lyhenteestä "ADR". Kun jotkin tiimit käyttävät hakemiston nimenä "decisions", on kuin valo syttyisi, ja tiimi alkaa laittaa hakemistoon enemmän tietoa, kuten toimittajapäätöksiä, suunnittelupäätöksiä, aikataulupäätöksiä jne. Kaikki nämä tietotyypit voivat käyttää samaa mallipohjaa. Oletamme, että ihmiset oppivat nopeammin sanoista ("päätökset") kuin lyhenteistä ("ADR"), että ihmiset ovat motivoituneempia kirjoittamaan keskeneräisiä dokumentteja, kun sana "tietue" poistetaan, ja että jotkut kehittäjät ja johtajat eivät myöskään pidä sanasta "arkkitehtuuri".

Teoriassa muuttumattomuus on ihanteellista. Käytännössä muutettavuus on toiminut tiimeillämme paremmin. Lisäämme uuden tiedon olemassa olevaan ADR-tietueeseen päivämääräleimalla ja huomautuksella siitä, että tieto saapui päätöksen jälkeen. Tällainen lähestymistapa johtaa "elävään dokumenttiin", jota me kaikki voimme päivittää. Tyypillisiä päivityksiä tehdään, kun saamme tietoa uusien tiimikavereiden ansiosta, tai uusien tarjousten vuoksi, tai käyttömme todellisista tuloksista, tai jälkikäteisistä kolmansien osapuolten muutoksista, kuten toimittajien ominaisuuksista, hinnoittelusuunnitelmista, lisenssisopimuksista jne.

## Tiimityökysymykset ADR-tietueille

### Kuka voi luoda ADR-tietueen?

Harkitse alueita kuten tietyt henkilöt, tietyt roolit, tietyt tiimit tai tietyt osastot; harkitse myös, onko henkilöitä, rooleja, tiimejä tai osastoja, jotka voivat tilata ADR-tietueen, eli pyytää sellaista jonkun muun kirjoitettavaksi. 

Esimerkkivastaus: Kuka tahansa organisaatiomme jäsen, joka on lukenut arkkitehtuuripäätöstietueen README-sivun, voi ehdottaa ADR-tietuetta, eli henkilö voi aloittaa sen kirjoittamisen ja jakaa sen tiimin kanssa.

### Mikä oikeuttaa ADR-tietueen laatimiseen?

Harkitse alueita kuten organisaatiosi tiimien työskentelytavat, ohjelmistojärjestelmäsi rakenne, tiimien välinen koordinointi, pitkän aikavälin ylläpidettävyys, ulkoiset rajapinnat, kenen haluat hyötyvän ja vastaavat. 

Esimerkkivastaus: Haluamme laatia ADR-tietueen, kun haluamme tulevien kehittäjien ymmärtävän tekemisemme "miksi".

### Mikä oikeuttaa ADR-tietueen laatimatta jättämiseen?

Harkitse alueita kuten päätökset, jotka eivät liity arkkitehtuuriin tai jotka ovat pieniä, kuten vähäriskisiä, itsenäisiä tai yhden kehittäjän päätöksiä, tai jotka on jo katettu täysin muualla, kuten standardeissa, politiikoissa tai dokumentaatiossa, tai jotka ovat tilapäisiä, kuten kiertoratkaisut, konseptitodistukset tai kokeilut. 

Esimerkkivastaus: Haluamme ohittaa ADR-tietueen, kun päätös on rajattu laajuudeltaan, ajaltaan, riskiltään ja kustannukseltaan tai se on jo katettu muualla.

### Mikä on ADR-tietueen elinkaari?

Harkitse alueita kuten luontiprosessi, tutkimusprosessi, päätösprosessi, toteutusprosessi ja käytöstä poistamisen prosessi. Harkitse, kuinka ADR-tietueen elinkaarta seurataan ajan myötä, esimerkiksi kuinka ADR-tietue siirretään tilasta toiseen ja kuinka tästä viestitään sidosryhmille. 

Esimerkkivastaus: Haluamme ADR-tietueella olevan viisi elinkaaren vaihetta: Aloittaminen → Tutkiminen → Arviointi → Toteuttaminen → Ylläpito → Käytöstä poistaminen.

### Mitkä ovat ADR-tietueen elinkaaren vaiheiden kriteerit?

Harkitse alueita kuten ADR-tietueen hyväksymiskriteerit, eli mistä tiedät, että se on riittävän hyvä siirtyäkseen elinkaaren vaiheesta seuraavaan? Onko ongelma ilmaistu selkeästi? Onko vaihtoehtoja harkittu? Onko kompromissit ymmärretty ja dokumentoitu riittävän hyvin?
Onko kaikki olennainen konteksti paikallaan? Ovatko kaikki olennaiset sidosryhmät mukana? Onko kaikki palaute otettu huomioon? 

Esimerkkivastaus: Haluamme sidosryhmien äänestävän ADR-tietueesta, kun aktiivinen tiimi on 1) saanut tutkimuksensa valmiiksi, 2) saanut arviointinsa valmiiksi, 3) julkaissut ADR-ehdotuksen sidosryhmille kommenttipyynnön ja yhden viikon aikarajan kera, 4) kaikki sidosryhmien kommentit on otettu huomioon ja käsitelty.

### Mitkä roolit ja vastuut ovat vuorovaikutuksessa ADR-tietueen kanssa?

Harkitse rooleja kuten ehdottaja, tutkija, arvioija, katselmoija, hyväksyjä, ylläpitäjä ja vastaavat. Harkitse vastuita kuten viestintä sidosryhmille, odotusten täyttymisen varmistaminen, jakaminen verkkosivustolla tai intranetissä sekä työn säännöllinen katselmointi ja erityisesti silloin, kun olennaisia muutoksia tapahtuu.

Esimerkkivastaus: Haluamme jokaiselle ADR-tietueelle aina ensisijaisen yhteyshenkilön, toissijaisen yhteyshenkilön ja vastuullisen tiimin; nämä vastaavat viestinnästä, julkaisemisesta, ylläpidosta, määräaikaiskatselmoinnista vähintään kerran vuodessa ja tarvittaessa lopulta käytöstä poistamisesta.

### Miten hallinto on vuorovaikutuksessa ADR-tietueen kanssa?

Harkitse alueita kuten organisaatiosi työskentelytavat, erityiset vaatimustenmukaisuustarpeet esimerkiksi lakiasioissa tai henkilöstöasioissa sekä se, miten haluat käsitellä konsensusta, ristiriitoja ja eskalointia. Onko alueita, henkilöitä tai tiimejä, joilla voi olla enemmän vaikutusvaltaa kuin muilla ADR-tietueen suhteen, esimerkiksi oikeus hyväksyä se, äänestää siitä tai kieltää se?

Esimerkkivastaus: ADR-tietueen hallinto on tässä tärkeysjärjestyksessä: toimitusjohtaja, tekninen johtaja, lakiasiainjohtaja, ADR-tietueen toteuttava tiimi, tiimin asiantuntijat, jotka tuntevat AD-päätöksen parhaiten. Kenelläkään muulla ei ole hallintaoikeutta, ellei se ole kuvattu ADR-tietueessa. 

### Mitkä periaatteet ovat vuorovaikutuksessa ADR-tietueen kanssa?

Harkitse alueita kuten organisaatiosi työskentelytavat, jotka sisältävät nopean tai hitaan etenemisen, päätöksistä konsensuksen tai ristiriidan, riskien tai turvallisuuden suosimisen, julkisen tai yksityisen keskustelun ja vastaavat.

Esimerkkivastaus: Käytämme johtamisperiaatteita toimintaan kallistuminen, eri mieltä oleminen ja sitoutuminen, 70 %:n arviot ovat riittävän hyviä helposti peruttaville ja helposti eristettäville päätöksille sekä julkinen työskentelytapa lukuun ottamatta luottamuksellista tietoa, kuten organisaatiomme salassapitosopimuksessa kuvataan.

## ADR-tietueiden seuraavan askeleen käsitteet

[Arc42](https://arc42.org/) vastaa kahteen kysymykseen pragmaattisesti, ja sitä voi mukauttaa tarpeisiisi. Mitä arkkitehtuuristasi kannattaa dokumentoida/viestiä? Miten kannattaa dokumentoida/viestiä? Arc42 sisältää arkkitehtuuripäätöstietueet sekä ohjeita tavoitteista, rajoitteista, konteksteista, laadusta, riskeistä ja muusta.

[C4-malli](https://c4model.com/) on helposti opittava, kehittäjäystävällinen tapa laatia ohjelmistoarkkitehtuurin kaavioita. C4 on joukko hierarkkisia kaavioita kontekstille, konteille, komponenteille ja koodille sekä tukikaaviot järjestelmämaisemalle, dynamiikalle ja käyttöönotolle.

## Arkkitehtuurikaaviot, näkymät ja näkökulmat

Arkkitehtuurikaaviota kutsutaan "arkkitehtuurinäkymäksi".

"Arkkitehtuurinäkymä" on "arkkitehtuurinäkökulman" ilmentymä.

"Arkkitehtuurinäkökulmalla" on tietty kohdeyleisö, jolla on tiettyjä huolenaiheita.

Esimerkkejä arkkitehtuurinäkökulmista, näkymistä ja kaavioista:

- Liiketoimintakyvykkyydet

- Korkean tason liiketoimintaprosessit

- [Arvovirrat](https://en.wikipedia.org/wiki/Value_stream)

- Sovelluskomponentteihin yhdistetyt ohjelmistotoiminnot

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Kontekstikaavio (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Konttikaavio (TO-BE / AS-IS)

- [Entiteetti-suhdekaavio](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) tietoentiteettien yhdistämiseksi sovelluskomponentteihin

- [Sekvenssikaaviot](https://en.wikipedia.org/wiki/Sequence_diagram) toiminnallisten kulkujen kuvaamiseksi järjestelmien sisällä ja integraatioissa

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) kaaviot tietovirtojen kuvaamiseksi sovelluskomponenttien välillä

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) kaaviot liiketoimintaprosessien / käyttäjäskenaarioiden kuvaamiseksi

- [Identiteetin- ja käyttöoikeuksien hallinta](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) kaaviot

- [Roolipohjainen käyttöoikeuksien hallinta](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) kaaviot rooleineen sovelluskomponenttia kohden

- [Attribuuttipohjainen käyttöoikeuksien hallinta](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) kaaviot attribuutteineen sovelluskomponenttia kohden

- Tietosuojakaaviot

Liittyvät kaaviot:

- Käyttötapauskaavio näyttää käyttötapaukset johdolle/asiakkaille, mikä edeltää vaatimuksia, jotka edeltävät ohjelmistoarkkitehtuuria.

- Käyttöönottokaavio näyttää fyysisen laitteiston/tietokoneet, joihin ohjelmistokomponentit otetaan käyttöön.
- Tietovirtakaavio näyttää, miten data liikkuu järjestelmässä ja muuntuu.
- Sekvenssikaaviolla näytetään, miten protokollat kuten HTTP toimivat aika-akselilla.

- Toimintakaavio kuvaa ohjelmistojärjestelmän suorittamien toimintojen työnkulun, kuten NPC-tekoälyn.

## Sopivuusfunktiot koodina ilmaistuille päätöksille

Sopivuusfunktiot (fitness functions) ovat objektiivisia automaattisia tarkistuksia, jotka on kirjoitettu ohjelmointikoodilla ja jotka varmistavat, että päätöksiä noudatetaan.

- Sopivuusfunktiot tekevät päätöksistä testattavia ja varmistettavia.

- Päätösten sopivuusfunktiot voivat auttaa suuresti laadunvarmistuksessa, sääntelyprosesseissa ja hallintotavoitteissa.

### Miten sopivuusfunktiot liittyvät päätöksiin

Päätöstietue dokumentoi päätöksen, kun taas sopivuusfunktio varmistaa päätöksen.

- Esimerkkipäätös: Käytämme tapahtumalähteistystä (event sourcing) auditointivaatimusten vuoksi.

- Esimerkkisopivuusfunktio: Käytämme jatkuvan integroinnin palvelinta testaamaan, että kaikkien tilamuutosten on tuotettava tapahtumia.

### Miksi sopivuusfunktiot auttavat päätöksiä

Objektiiviset mittaukset: Sopivuusfunktiot joko läpäisevät tai epäonnistuvat, joten työ on näkyvää ja selkeää.

Jatkuva käyttö: Sopivuusfunktiot ovat elävät sääntösi, jotka ajetaan jokaisella commitilla ja koonnilla.

Varmuus refaktorointiin: Sopivuusfunktiot havaitsevat päätössääntöjen virheet automaattisesti.

Skaalautuva hallinto: Sopivuusfunktiot varmistavat standardit luomatta pullonkauloja.

### Voivatko sopivuusfunktiot käyttää tekoälyä?

Sopivuusfunktiot voivat hyödyntää tekoälyn suuria kielimalleja (LLM) päätösten arvioinnissa esittämällä kysymyksiä työstäsi,
kuten suunnitelmistasi, koodistasi, skeemoistasi, rajapinnoistasi ja muusta:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Arkkitehtuurin yksikkötestaus

[ArchUnit](https://www.archunit.org/): tarkista Java-koodin arkkitehtuurisäännöt käyttämällä mitä tahansa tavallista Javan yksikkötestauskehystä.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): tarkista TypeScript-koodin ja JavaScript-koodin arkkitehtuurisäännöt käyttämällä Jestiä, Vitestiä, Jasminea jne.

## Päätösten suojakaiteet vetopyynnöille

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
nostaa oikeat päätöstietueet esiin oikealla hetkellä, eli kun
kehittäjä muokkaa aktiivisesti koodia, jota nämä päätökset koskevat. Sen sijaan, että toivottaisiin kehittäjien
lukevan dokumenttikansion ennen yhdistämistä, olennainen tausta ilmestyy suoraan vetopyyntöön.

Tämä toimii kaikenlaisille päätöstietueille: arkkitehtuuripäätöksille, tietopäätöksille, vaatimustenmukaisuuspäätöksille, kliinisille ja lääketieteellisille päätöksille, tietoturvapäätöksille ja muille.

Toimii minkä tahansa CI-järjestelmän (GitLab, Jenkins, CircleCI) kanssa ja pre-commit-koukkuna.
Avoin lähdekoodi. MIT-lisenssi.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) on GitHub
Action, joka hylkää vetopyynnön, kun valvotut koodipolut muuttuvat ilman, että arkkitehtuuripäätöstietuetta
lisätään tai päivitetään. Poikkeukset ovat selkeitä: perusteltu
`ADR-Exempt:`-rivi päästää portin läpi ja kirjoitetaan työn yhteenvetoon. Mallipohjasta riippumaton, ei riippuvuuksia. Avoin lähdekoodi. MIT-lisenssi.

## Lisätietoja

Johdanto:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Mallipohjat:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Syvällisesti:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - ilmainen kuukausittainen ohjelmistoarkkitehtuurin oppitunti

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Työkalut:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Yrityskohtaisia ohjeita:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Esimerkit:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Videot:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcastit:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Kirjat:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

Katso myös:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Toimittajariippumaton, koneluettava YAML/JSON-muoto päätösten esittämiseen selkeine perusteluineen, oletuksineen, kognitiivisine tiloineen ja kompromisseineen. Täydentää ADR-tietueita lisäämällä päätösdokumentaatioon jäsenneltyä, validoitavaa päättelyä.
