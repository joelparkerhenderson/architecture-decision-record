# Arkitektúrákvörðunarskrá (ADR)

Arkitektúrákvörðunarskrá (ADR) er skjal sem fangar mikilvæga arkitektúrákvörðun ásamt samhengi hennar og afleiðingum.

> [!IMPORTANT]
> Gerðu þína eigin áreiðanleikakönnun á þessum úrræðum áður en þú notar þau í mikilvægum kerfum.

Efnisyfirlit:

- [Hvað er arkitektúrákvörðunarskrá?](#hvað-er-arkitektúrákvörðunarskrá)
- [Hvernig á að byrja að nota ADR](#hvernig-á-að-byrja-að-nota-adr)
- [Hvernig á að byrja að nota ADR með verkfærum](#hvernig-á-að-byrja-að-nota-adr-með-verkfærum)
- [Hvernig á að byrja að nota ADR með git](#hvernig-á-að-byrja-að-nota-adr-með-git)
- [Claude Code færni fyrir ADR](#claude-code-færni-fyrir-adr)
- [Venjur um skráarnöfn fyrir ADR](#venjur-um-skráarnöfn-fyrir-adr)
- [Tillögur að góðum ADR](#tillögur-að-góðum-adr)
- [Dæmi um ADR-sniðmát](#dæmi-um-adr-sniðmát)
- [Ráð um teymisvinnu fyrir ADR](#ráð-um-teymisvinnu-fyrir-adr)
- [Spurningar um teymisvinnu fyrir ADR](#spurningar-um-teymisvinnu-fyrir-adr)
- [Hugtök fyrir næsta skref ADR](#hugtök-fyrir-næsta-skref-adr)
- [Arkitektúrskýringarmyndir, sýnir og sjónarhorn](#arkitektúrskýringarmyndir-sýnir-og-sjónarhorn)
- [Hæfnisföll fyrir ákvarðanir sem kóða](#hæfnisföll-fyrir-ákvarðanir-sem-kóða)
- [Ákvörðunarvarnir fyrir pull request](#ákvörðunarvarnir-fyrir-pull-request)
- [Frekari upplýsingar](#frekari-upplýsingar)

Sniðmát:

- [Sniðmát ákvörðunarskrár frá Jeff Tyree og Art Akerman](sniðmát/sniðmát-ákvörðunarskrár-frá-jeff-tyree-og-art-akerman/)
- [Sniðmát ákvörðunarskrár frá Michael Nygard](sniðmát/sniðmát-ákvörðunarskrár-frá-michael-nygard/)
- [Sniðmát ákvörðunarskrár frá EdgeX](sniðmát/sniðmát-ákvörðunarskrár-frá-edgex/)
- [Sniðmát ákvörðunarskrár frá arc42](sniðmát/sniðmát-ákvörðunarskrár-frá-arc42/)
- [Sniðmát ákvörðunarskrár fyrir Alexander-mynstur](sniðmát/sniðmát-ákvörðunarskrár-fyrir-alexander-mynstur/)
- [Sniðmát ákvörðunarskrár fyrir viðskiptarök](sniðmát/sniðmát-ákvörðunarskrár-fyrir-viðskiptarök/)
- [Sniðmát ákvörðunarskrár MADR-verkefnisins](sniðmát/sniðmát-ákvörðunarskrár-madr-verkefnisins/)
- [Sniðmát ákvörðunarskrár með Planguage](sniðmát/sniðmát-ákvörðunarskrár-með-planguage/)
- [Sniðmát ákvörðunarskrár frá Paulo Merson](https://github.com/pmerson/ADR-template)
- [Sniðmát ákvörðunarskrár frá Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Sniðmát ákvörðunarskrár frá Gareth Morgan](sniðmát/sniðmát-ákvörðunarskrár-frá-gareth-morgan/)
- [Sniðmát ákvörðunarskrár frá GIG Cymru NHS Wales](sniðmát/sniðmát-ákvörðunarskrár-frá-gig-cymru-nhs-wales/)
- [Sniðmát ákvörðunarskrár fyrir mikilvægar tæknilegar ákvarðanir (ITD) eftir Ignacio Larrañaga](sniðmát/sniðmát-ákvörðunarskrár-fyrir-mikilvægar-tæknilegar-ákvarðanir/)

Dæmi:

- [CSS-rammi](dæmi/css-rammi/)
- [Uppsetning umhverfisbreyta](dæmi/uppsetning-umhverfisbreyta/)
- [Mælikvarðar, vöktun og viðvaranir](dæmi/mælikvarðar-vöktun-og-viðvaranir/)
- [Microsoft Azure DevOps](dæmi/microsoft-azure-devops/)
- [Monorepo eða multirepo](dæmi/monorepo-eða-multirepo/)
- [Forritunarmál](dæmi/forritunarmál/)
- [Geymsla leyndarmála](dæmi/geymsla-leyndarmála/)
- [Snið tímastimpla](dæmi/snið-tímastimpla/)
- [Margt fleira...](dæmi/)

## Hvað er arkitektúrákvörðunarskrá?

**Arkitektúrákvörðunarskrá** (ADR) er skjal sem fangar mikilvæga arkitektúrákvörðun ásamt samhengi hennar og afleiðingum.

**Arkitektúrákvörðun** (AD) er hönnunarval í hugbúnaði sem svarar mikilvægri kröfu.

**Arkitektúrákvörðunarannáll** (ADL) er safn allra ADR-skráa sem búnar eru til og viðhaldið fyrir tiltekið verkefni (eða stofnun).

**Arkitektúrlega mikilvæg krafa** (ASR) er krafa sem hefur mælanleg áhrif á arkitektúr hugbúnaðarkerfis.

Allt þetta heyrir undir viðfangsefnið **stjórnun arkitektúrþekkingar** (AKM).

Markmið þessa skjals er að veita hraða yfirsýn yfir ADR-skrár, hvernig á að búa þær til og hvar hægt er að finna frekari upplýsingar.

Skammstafanir:

  * **AD**: arkitektúrákvörðun

  * **ADL**: arkitektúrákvörðunarannáll

  * **ADR**: arkitektúrákvörðunarskrá

  * **AKM**: stjórnun arkitektúrþekkingar

  * **ASR**: arkitektúrlega mikilvæg krafa

## Hvernig á að byrja að nota ADR

Til að byrja að nota ADR-skrár skaltu ræða við samstarfsfólk þitt um eftirfarandi svið.

Greining ákvarðana:

  * Hversu brýn og hversu mikilvæg er AD-ákvörðunin?

  * Þarf að taka hana núna, eða getur hún beðið þar til meira er vitað?

  * Bæði persónuleg og sameiginleg reynsla, sem og viðurkenndar hönnunaraðferðir og starfsvenjur, geta hjálpað við greiningu ákvarðana.

  * Helst skaltu halda ákvörðunarverkefnalista sem bætir við verkefnalista vörunnar.

Ákvarðanataka:

  * Til eru ýmsar aðferðir við ákvarðanatöku, bæði almennar og sértækar fyrir hugbúnaðararkitektúr, til dæmis samræðukortlagning.

  * Hópákvarðanataka er virkt rannsóknarefni.

Framkvæmd og eftirfylgni ákvarðana:

  * AD-ákvarðanir eru notaðar í hugbúnaðarhönnun; því þarf að miðla þeim til hagsmunaaðila kerfisins sem fjármagna það, þróa og reka, og fá samþykki þeirra.

  * Kóðunarstíll þar sem arkitektúr er sýnilegur og kóðarýni sem beinist að arkitektúrsjónarmiðum og ákvörðunum eru tvær tengdar starfsvenjur.

  * Einnig þarf að (endur)skoða AD-ákvarðanir þegar hugbúnaðarkerfi er endurnýjað í þróunarferli þess.

Miðlun ákvarðana (valfrjálst):

  * Margar AD-ákvarðanir endurtaka sig milli verkefna.

  * Því getur reynsla af fyrri ákvörðunum, bæði góð og slæm, verið verðmæt endurnýtanleg eign þegar beitt er skýrri stefnu í þekkingarstjórnun.

Skjölun ákvarðana:

  * Til eru mörg sniðmát og verkfæri til að skrá ákvarðanir.

  * Sjá lipur samfélög, t.d. ADR-skrár M. Nygard.

  * Sjá hefðbundin ferli hugbúnaðarverkfræði og arkitektúrhönnunar, t.d. töfluuppsetningar sem IBM UMF og Tyree og Akerman hjá CapitalOne leggja til.

Frekari upplýsingar:

  * Skrefin hér að ofan eru sótt í grein Wikipedia um [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Hvernig á að byrja að nota ADR með verkfærum

- [MySpec](https://myspec.dev) — Sjálfvirkur vettvangur fyrir forskriftir og arkitektúrákvarðanir sem skipuleggur stjórnarskrá verkefnis, tæknilegan arkitektúr og ADR-skrár í hreint Markdown sem miðlað er í gegnum MCP.

Þú getur byrjað að nota ADR með verkfærum á hvaða hátt sem þú vilt.

Til dæmis:

  * Ef þú vilt nota Google Drive og netvinnslu, þá geturðu búið til Google Doc eða Google Sheet.

  * Ef þú vilt nota útgáfustýringu frumkóða, svo sem git, þá geturðu búið til skrá fyrir hverja ADR.

  * Ef þú vilt nota verkefnaáætlunartól, svo sem Atlassian Jira, þá geturðu notað verkefnarakningu tólsins.

  * Ef þú vilt nota wiki-kerfi, svo sem MediaWiki, þá geturðu búið til ADR-wiki.

## Hvernig á að byrja að nota ADR með git

Ef þú vilt nota git útgáfustýringu, þá er hér hvernig við byrjum helst að nota ADR með git fyrir dæmigert hugbúnaðarverkefni með frumkóða.

Búðu til möppu fyrir ADR-skrár:

```sh
$ mkdir adr
```

Búðu til textaskrá fyrir hverja ADR, til dæmis `choose-database.md`:

```sh
$ vi choose-database.md
```

Skrifaðu hvað sem þú vilt í ADR-skrána. Sjá sniðmátin í þessu safni til að fá hugmyndir.

Skráðu ADR-skrána í git-geymsluna þína (commit).

## Claude Code færni fyrir ADR

Þetta safn inniheldur tvær [Claude Code](https://claude.com/claude-code) færnieiningar (skills) undir [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), svo gervigreindar-forritunarfulltrúi geti skrifað og viðhaldið ADR-skrám á þann hátt sem þetta verkefni mælir með:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — almenn, fyrir alla sem skrifa ADR í hvaða verkefni sem er. Hjálpar til við að ákveða hvort ákvörðun þarfnast ADR, setur upp `adr/` eða `decisions/` möppu, gefur skránni nafn, velur sniðmát úr ellefu meðfylgjandi beinagrindum og skrifar traustar Samhengis-/Ákvörðunar-/Afleiðingakafla.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — sérstaklega fyrir umsjónarfólk þessa safns. Skjalfestir uppbyggingu safnsins, venjuna um speglun README/tungumála og nákvæm skref til að bæta við nýju sniðmáti, dæmi eða tengli á verkfæri.

Til að nota færnieiningu skaltu afrita möppu hennar í `.claude/skills/` í rót safnsins sem þú vinnur í (eða í `~/.claude/skills/` til að gera hana aðgengilega í hverju verkefni) og biðja síðan Claude Code að skrifa eða rýna ADR.

## Venjur um skráarnöfn fyrir ADR

Ef þú velur að búa til ADR-skrárnar þínar með venjulegum textaskrám gætirðu viljað koma þér upp eigin venju um skráarnöfn ADR.

Við kjósum að nota venju um skráarnöfn með tilteknu sniði.

Dæmi:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Venja okkar um skráarnöfn:

  * Nafnið hefur boðháttarsögn í nútíð. Þetta bætir læsileika og samræmist sniði okkar á skilaboðum í commit.

  * Nafnið notar lágstafi og bandstrik (eins og þetta safn). Þetta er jafnvægi milli læsileika og nothæfi kerfisins.

  * Skráarendingin er markdown. Þetta getur gagnast til að auðvelda snið.

## Tillögur að góðum ADR

Einkenni góðrar ADR:

* Rökstuðningur: Útskýrðu ástæður þess að gera tiltekna AD-ákvörðun. Þetta getur falið í sér samhengi (sjá hér að neðan), kosti og galla ýmissa mögulegra valkosta, samanburð á eiginleikum, umræður um kostnað og ávinning og fleira.

* Afmörkuð: Hver ADR ætti að fjalla um eina AD-ákvörðun, ekki margar.

* Tímastimplar: Tilgreindu hvenær hvert atriði í ADR er skrifað. Þetta er sérstaklega mikilvægt fyrir þætti sem geta breyst með tímanum, svo sem kostnað, tímaáætlanir, stækkun og þess háttar.

* Óbreytanleg: Breyttu ekki fyrirliggjandi upplýsingum í ADR. Bættu heldur við nýjum upplýsingum til að breyta ADR, eða láttu nýja ADR leysa hana af hólmi.

Einkenni góðs kafla um „samhengi“ í ADR:

* Útskýrðu stöðu stofnunarinnar og viðskiptaforgangsröðun.

* Taktu með rökstuðning og sjónarmið byggð á félagslegri samsetningu og færni teymanna þinna.

* Taktu með kosti og galla sem skipta máli og lýstu þeim á þann hátt sem samræmist þörfum þínum og markmiðum.

Einkenni góðs kafla um „afleiðingar“ í ADR:

* Útskýrðu hvað leiðir af því að taka ákvörðunina. Þetta getur falið í sér áhrif, niðurstöður, afurðir, eftirfylgni og fleira.

* Taktu með upplýsingar um allar síðari ADR-skrár. Það er tiltölulega algengt að ein ADR kalli á fleiri ADR-skrár, til dæmis þegar ein ADR tekur stórt yfirgripsmikið val sem aftur skapar þörf fyrir fleiri smærri ákvarðanir.

* Taktu með öll ferli til rýni eftir á. Algengt er að teymi rýni hverja ADR mánuði síðar, til að bera upplýsingar ADR saman við það sem gerðist í raun og læra og vaxa.

Ný ADR getur komið í stað fyrri ADR:

* Þegar tekin er AD-ákvörðun sem kemur í stað eða ógildir fyrri ADR, ætti að búa til nýja ADR

## Dæmi um ADR-sniðmát

Dæmi um ADR-sniðmát sem við höfum safnað á netinu:

- [ADR-sniðmát frá Michael Nygard](sniðmát/sniðmát-ákvörðunarskrár-frá-michael-nygard/) (einfalt og vinsælt)

- [ADR-sniðmát frá Jeff Tyree og Art Akerman](sniðmát/sniðmát-ákvörðunarskrár-frá-jeff-tyree-og-art-akerman/) (flóknara)

- [ADR-sniðmát fyrir Alexander-mynstur](sniðmát/sniðmát-ákvörðunarskrár-fyrir-alexander-mynstur/) (einfalt með sértækum upplýsingum um samhengi)

- [ADR-sniðmát fyrir viðskiptarök](sniðmát/sniðmát-ákvörðunarskrár-fyrir-viðskiptarök/) (meira MBA-miðað, með kostnaði, SWOT og fleiri skoðunum)

- [ADR-sniðmát Markdown Any Decision Records (MADR) verkefnisins](sniðmát/sniðmát-ákvörðunarskrár-madr-verkefnisins/) (bæði einföld og ítarleg útgáfa; sú síðarnefnda leggur áherslu á valkosti og kosti þeirra og galla)

- [ADR-sniðmát með Planguage](sniðmát/sniðmát-ákvörðunarskrár-með-planguage/) (meira miðað við gæðatryggingu)

- [Sniðmát fyrir mikilvægar tæknilegar ákvarðanir (ITD) eftir Ignacio Larrañaga](sniðmát/sniðmát-ákvörðunarskrár-fyrir-mikilvægar-tæknilegar-ákvarðanir/) (straumlínulagað og ákvörðun fyrst, fínstillt fyrir hraða rýni stjórnenda)

## Ráð um teymisvinnu fyrir ADR

Ef þú ert að íhuga að nota ákvörðunarskrár með teyminu þínu, þá eru hér nokkur ráð sem við höfum lært af því að vinna með mörgum teymum.

Þú hefur tækifæri til að leiða samstarfsfólk þitt með því að ræða saman um „hvers vegna“, frekar en að skylda „hvað“. Til dæmis eru ákvörðunarskrár leið fyrir teymi til að hugsa snjallar og miðla betur; ákvörðunarskrár eru ekki verðmætar ef þær eru bara þvinguð pappírsvinna eftir á.

Sum teymi kjósa mun frekar nafnið „ákvarðanir“ fram yfir skammstöfunina „ADR“. Þegar sum teymi nota möppuheitið „decisions“ er eins og kviknað hafi á ljósaperu og teymið byrjar að setja meiri upplýsingar í möppuna, svo sem ákvarðanir um söluaðila, skipulagsákvarðanir, tímasetningarákvarðanir o.s.frv. Allar þessar tegundir upplýsinga geta notað sama sniðmátið. Við setjum fram þá tilgátu að fólk læri hraðar með orðum („ákvarðanir“) en skammstöfunum („ADR“), að fólk sé áhugasamara um að skrifa skjöl í vinnslu þegar orðið „skrá“ er fjarlægt, og einnig að sumum þróunaraðilum og sumum stjórnendum mislíki orðið „arkitektúr“.

Í kenningu er óbreytanleiki æskilegur. Í reynd hefur breytanleiki reynst teymum okkar betur. Við setjum nýju upplýsingarnar inn í fyrirliggjandi ADR, með dagsetningarstimpli og athugasemd um að upplýsingarnar hafi borist eftir ákvörðunina. Þessi nálgun leiðir til „lifandi skjals“ sem við getum öll uppfært. Dæmigerðar uppfærslur eru þegar við fáum upplýsingar þökk sé nýju samstarfsfólki, nýju framboði, raunverulegum niðurstöðum af notkun okkar eða breytingum þriðju aðila eftir á, svo sem getu söluaðila, verðáætlunum, leyfissamningum o.s.frv.

## Spurningar um teymisvinnu fyrir ADR

### Hver getur búið til ADR?

Íhugaðu svið eins og tiltekið fólk, tiltekin hlutverk, tiltekin teymi eða tilteknar deildir; íhugaðu einnig hvort til séu einstaklingar, hlutverk, teymi eða deildir sem geta pantað ADR, það er óskað eftir einni sem einhver annar skrifar.

Dæmi um svar: Hver sá einstaklingur í stofnuninni okkar sem hefur lesið README-síðu arkitektúrákvörðunarskrárinnar getur lagt til ADR, það er byrjað að skrifa hana og deilt henni með teyminu.

### Hvað réttlætir að búa til ADR?

Íhugaðu svið eins og vinnulag teyma stofnunarinnar, uppbyggingu hugbúnaðarkerfisins, samhæfingu milli teyma, langtímaviðhaldshæfni, ytri viðmót, hverjum þú vilt koma til góða og þess háttar.

Dæmi um svar: Við viljum búa til ADR þegar við viljum að framtíðarþróunaraðilar skilji „hvers vegna“ við gerum það sem við gerum.

### Hvað réttlætir að búa ekki til ADR?

Íhugaðu svið eins og ákvarðanir sem snúast ekki um arkitektúr, eða eru smávægilegar, til dæmis með lágmarksáhættu, sjálfstæðar eða á könnu eins þróunaraðila, eða eru þegar að fullu fjallað um annars staðar, til dæmis í stöðlum, stefnum eða skjölun, eða eru tímabundnar, til dæmis lausnir til bráðabirgða, hugmyndaprófanir eða tilraunir.

Dæmi um svar: Við viljum sleppa ADR þegar ákvörðun er takmörkuð að umfangi, tíma, áhættu og kostnaði, eða er þegar fjallað um annars staðar.

### Hver er lífsferill ADR?

Íhugaðu svið eins og gerð, rannsóknarferli, ákvörðunarferli, útfærsluferli og lokaferli. Íhugaðu hvernig á að rekja lífsferil ADR yfir tíma, svo sem hvernig á að færa ADR úr einni stöðu í þá næstu, og einnig hvernig á að miðla þessu til hagsmunaaðila.

Dæmi um svar: Við viljum að ADR hafi fimm lífsferilsstig: Upphaf → Rannsókn → Mat → Útfærsla → Viðhald → Lok.

### Hver eru viðmið fyrir lífsferilsskref ADR?

Íhugaðu svið eins og samþykkisviðmið fyrir ADR, það er hvernig veistu að hún sé nógu góð til að halda áfram úr einu lífsferilsskrefi í það næsta? Er vandamálið skýrt orðað? Hafa valkostirnir verið skoðaðir? Eru málamiðlanir nógu vel skildar og skjalfestar?
Er allt viðeigandi samhengi til staðar? Eru allir viðeigandi hagsmunaaðilar með? Hafa allar athugasemdir verið teknar inn?

Dæmi um svar: Við viljum að hagsmunaaðilar kjósi um ADR þegar virka teymið hefur 1) lokið rannsókn sinni, 2) lokið mati sínu, 3) birt ADR-tillöguna fyrir hagsmunaaðilum með beiðni um athugasemdir og eins vikna tímaramma, 4) allar athugasemdir hagsmunaaðila hafa verið teknar inn og brugðist hefur verið við þeim.

### Hvaða hlutverk og ábyrgð tengjast ADR?

Íhugaðu hlutverk eins og tillöguaðila, rannsakanda, matsaðila, rýnanda, samþykkjanda, viðhaldsaðila og þess háttar. Íhugaðu ábyrgð eins og samskipti við hagsmunaaðila, að tryggja að væntingar séu uppfylltar, miðlun á vefsíðu eða innra neti og reglubundna rýni á vinnunni, sérstaklega þegar viðeigandi breytingar verða.

Dæmi um svar: Við viljum að hver ADR hafi alltaf aðaltengilið, varatengilið og ábyrgt teymi; þessir aðilar bera ábyrgð á samskiptum, birtingu, viðhaldi, reglubundinni rýni að minnsta kosti árlega og endanlegum lokum þegar þörf krefur.

### Hvernig tengjast stjórnarhættir ADR?

Íhugaðu svið eins og vinnulag stofnunarinnar, sérstakar kröfur um fylgni, til dæmis vegna lagalegra þátta eða mannauðsþátta, hvernig þú vilt meðhöndla samstöðu á móti ágreiningi á móti stigmögnun. Eru til svið, fólk eða teymi sem geta haft meiri áhrif en önnur varðandi ADR, til dæmis að geta samþykkt hana, kosið um hana eða beitt neitunarvaldi?

Dæmi um svar: Stjórnarhættir ADR eru í þessari forgangsröð: forstjórinn, tæknistjórinn, lögfræðistjórinn, teymið sem útfærir ADR, sérfræðingar teymisins sem þekkja AD-ákvörðunina best. Enginn annar hefur stjórnarhætti nema það sé tekið fram í ADR.

### Hvaða meginreglur tengjast ADR?

Íhugaðu svið eins og vinnulag stofnunarinnar sem felur í sér að hreyfa sig hratt á móti hægt, fyrir ákvörðunarsamstöðu á móti ákvörðunarágreiningi, og fyrir áhættuhneigð á móti öryggishneigð, opna umræðu á móti lokaðri umræðu og þess háttar.

Dæmi um svar: Við notum forystureglurnar tilhneiging til athafna, ósammála-en-skuldbundin, 70% mat er nógu gott fyrir auðafturkræfar og auðeinangranlegar ákvarðanir, og opið vinnulag að undanskildum trúnaðarupplýsingum eins og lýst er í trúnaðarsamningi stofnunarinnar okkar.

## Hugtök fyrir næsta skref ADR

[Arc42](https://arc42.org/) svarar tveimur spurningum á hagnýtan hátt og hægt er að laga það að þínum sérstöku þörfum. Hvað ættir þú að skjalfesta/miðla um arkitektúrinn þinn? Hvernig ættir þú að skjalfesta/miðla? Arc42 inniheldur arkitektúrákvörðunarskrár ásamt leiðbeiningum um markmið, takmarkanir, samhengi, gæði, áhættu og fleira.

[C4-líkanið](https://c4model.com/) er auðlært, þróunaraðilavæn nálgun við gerð skýringarmynda af hugbúnaðararkitektúr. C4 er safn stigskiptra mynda fyrir samhengi, gáma, íhluti og kóða, auk stoðmynda fyrir kerfislandslag, kviku og uppsetningu.

## Arkitektúrskýringarmyndir, sýnir og sjónarhorn

Arkitektúrskýringarmynd er kölluð „arkitektúrsýn“.

„Arkitektúrsýn“ er tilvik af „arkitektúrsjónarhorni“.

„Arkitektúrsjónarhorn“ hefur tiltekinn markhóp með tiltekin áhyggjuefni í huga.

Dæmi um arkitektúrsjónarhorn, sýnir og skýringarmyndir:

- Viðskiptageta

- Viðskiptaferli á háu stigi

- [Virðisstraumar](https://en.wikipedia.org/wiki/Value_stream)

- Hugbúnaðarföll varpað á forritaíhluti

- [C4-líkan](https://en.wikipedia.org/wiki/C4_model) samhengismynd (TIL-BÚIÐ / NÚVERANDI)

- [C4-líkan](https://en.wikipedia.org/wiki/C4_model) gámamynd (TIL-BÚIÐ / NÚVERANDI)

- [Eininga-tengslamynd](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) til að varpa gagnaeiningum á forritaíhluti

- [Runumyndir](https://en.wikipedia.org/wiki/Sequence_diagram) til að lýsa virknisflæði innan kerfa og fyrir samþættingar

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) myndir til að lýsa gagnaflæði milli forritaíhluta

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) myndir til að lýsa viðskiptaferlum / sviðsmyndum notenda

- [Auðkennis- og aðgangsstýring](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) myndir

- [Hlutverkamiðuð aðgangsstýring](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) myndir með hlutverkum fyrir hvern forritaíhlut

- [Eigindamiðuð aðgangsstýring](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) myndir með eigindum fyrir hvern forritaíhlut

- Persónuverndarmyndir

Tengdar myndir:

- Notkunartilvikamynd sýnir notkunartilvik fyrir stjórnendur/viðskiptavini, sem fer á undan kröfum, sem fara á undan hugbúnaðararkitektúrnum.

- Uppsetningarmynd sýnir vélbúnaðinn/tölvurnar sem hugbúnaðaríhlutirnir eru settir upp á.
- Gagnaflæðismynd sýnir hvernig gögn færast í gegnum kerfið og er umbreytt.
- Runumynd er notuð til að sýna hvernig samskiptareglur eins og HTTP virka á tímaás.

- Virknimynd lýsir vinnuflæði aðgerða sem hugbúnaðarkerfi framkvæmir, eins og gervigreind persónu sem ekki er leikmaður (NPC AI).

## Hæfnisföll fyrir ákvarðanir sem kóða

Hæfnisföll eru hlutlægar sjálfvirkar athuganir, skrifaðar með forritunarkóða, sem sannreyna að ákvörðunum sé fylgt.

- Hæfnisföll gera ákvarðanir prófanlegar og tryggjanlegar.

- Hæfnisföll fyrir ákvarðanir geta stórlega hjálpað gæðatryggingu, regluverksferlum og stjórnarháttamarkmiðum.

### Hvernig hæfnisföll tengjast ákvörðunum

Ákvörðunarskrá skjalfestir ákvörðunina, en hæfnisfall tryggir hana.

- Dæmi um ákvörðun: Við notum atburðaupprunann (event sourcing) vegna kröfu um endurskoðunarslóð.

- Dæmi um hæfnisfall: Við notum þjón fyrir samfellda samþættingu til að prófa að allar stöðubreytingar verði að búa til atburði.

### Hvers vegna hæfnisföll hjálpa ákvörðunum

Hlutlægar mælingar: Hæfnisföll standast eða falla, svo vinnan er sýnileg og skýr.

Stöðug notkun: Hæfnisföll eru lifandi reglur þínar, keyrðar við hverja skráningu (commit) og smíði.

Öryggi til að endurskipuleggja kóða: Hæfnisföll grípa sjálfkrafa villur í ákvörðunarreglum.

Stigstærð stjórnarhættir: Hæfnisföll tryggja staðla án þess að skapa flöskuhálsa.

### Geta hæfnisföll notað gervigreind?

Hæfnisföll geta nýtt gervigreindar-tungumálalíkön (LLM) fyrir ákvarðanir með því að spyrja spurninga um vinnuna þína,
svo sem áætlanir, kóða, skema, API og fleira:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Einingaprófanir á arkitektúr

[ArchUnit](https://www.archunit.org/): athugaðu arkitektúrreglur Java-kóða með hvaða venjulega Java-einingaprófunarramma sem er.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): athugaðu arkitektúrreglur TypeScript-kóða og JavaScript-kóða með Jest, Vitest, Jasmine o.fl.

## Ákvörðunarvarnir fyrir pull request

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
dregur sjálfkrafa fram réttu ákvörðunarskrárnar á réttu augnabliki — þegar
þróunaraðili er að breyta kóðanum sem þessar ákvarðanir ná yfir. Í stað þess að
vona að þróunaraðilar lesi skjalamöppu áður en þeir sameina birtist viðeigandi
samhengi beint á pull request.

Þetta virkar fyrir hvers kyns ákvörðunarskrár: arkitektúrákvarðanir, gagnaákvarðanir,
ákvarðanir um fylgni, klínískar og læknisfræðilegar ákvarðanir, öryggisákvarðanir
og fleira.

Virkar með hvaða CI-kerfi sem er (GitLab, Jenkins, CircleCI) og sem pre-commit krókur.
Opið. MIT-leyfi.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) er GitHub
Action sem fellir pull request þegar fylgst er með kóðaslóðum sem breytast án þess að
arkitektúrákvörðunarskrá sé bætt við eða uppfærð. Undanþágur eru skýrar: lína
`ADR-Exempt:` með ástæðu hleypir í gegnum hliðið og er skráð í samantekt
verksins. Óháð sniðmáti, engin ávirkni. Opið. MIT-leyfi.

## Frekari upplýsingar

Inngangur:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Sniðmát:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Ítarefni:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - ókeypis mánaðarleg kennslustund í hugbúnaðararkitektúr

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Verkfæri:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Leiðbeiningar einstakra fyrirtækja:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Dæmi:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Myndbönd:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Hlaðvörp:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Bækur:

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

Sjá einnig:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Söluaðilaóháð, vélalæsilegt YAML/JSON-snið til að tákna ákvarðanir með skýrum rökstuðningi, forsendum, vitrænu ástandi og málamiðlunum. Bætir ADR-skrár með því að bæta skipulögðum, sannreynanlegum rökstuðningi við ákvörðunarskjölun.
