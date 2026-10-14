# Záznam architektonického rozhodnutí (ADR)

Záznam architektonického rozhodnutí (ADR) je dokument, který zachycuje důležité architektonické rozhodnutí spolu s jeho kontextem a důsledky.

> [!IMPORTANT]
> Před použitím těchto zdrojů v jakýchkoli kritických systémech proveďte vlastní náležitou kontrolu.

Obsah:

- [Co je záznam architektonického rozhodnutí?](#co-je-záznam-architektonického-rozhodnutí)
- [Jak začít používat ADR](#jak-začít-používat-adr)
- [Jak začít používat ADR s nástroji](#jak-začít-používat-adr-s-nástroji)
- [Jak začít používat ADR s gitem](#jak-začít-používat-adr-s-gitem)
- [Dovednosti Claude Code pro ADR](#dovednosti-claude-code-pro-adr)
- [Konvence pojmenování souborů ADR](#konvence-pojmenování-souborů-adr)
- [Tipy pro psaní dobrých ADR](#tipy-pro-psaní-dobrých-adr)
- [Příklady šablon ADR](#příklady-šablon-adr)
- [Rady k týmové práci pro ADR](#rady-k-týmové-práci-pro-adr)
- [Otázky k týmové práci pro ADR](#otázky-k-týmové-práci-pro-adr)
- [Koncepty dalšího kroku pro ADR](#koncepty-dalšího-kroku-pro-adr)
- [Architektonické diagramy, pohledy a hlediska](#architektonické-diagramy-pohledy-a-hlediska)
- [Fitness funkce pro rozhodnutí jako kód](#fitness-funkce-pro-rozhodnutí-jako-kód)
- [Ochranná pravidla rozhodnutí pro pull requesty](#ochranná-pravidla-rozhodnutí-pro-pull-requesty)
- [Další informace](#další-informace)

Šablony:

- [Šablona záznamu rozhodnutí od Jeffa Tyreeho a Arta Akermana](sablony/sablona-zaznamu-rozhodnuti-jeff-tyree-a-art-akerman/)
- [Šablona záznamu rozhodnutí od Michaela Nygarda](sablony/sablona-zaznamu-rozhodnuti-michael-nygard/)
- [Šablona záznamu rozhodnutí od EdgeX](sablony/sablona-zaznamu-rozhodnuti-edgex/)
- [Šablona záznamu rozhodnutí od arc42](sablony/sablona-zaznamu-rozhodnuti-arc42/)
- [Šablona záznamu rozhodnutí pro alexandrijský vzor](sablony/sablona-zaznamu-rozhodnuti-alexandrijsky-vzor/)
- [Šablona záznamu rozhodnutí pro podnikatelský záměr](sablony/sablona-zaznamu-rozhodnuti-podnikatelsky-zamer/)
- [Šablona záznamu rozhodnutí projektu MADR](sablony/sablona-zaznamu-rozhodnuti-projekt-madr/)
- [Šablona záznamu rozhodnutí s Planguage](sablony/sablona-zaznamu-rozhodnuti-s-planguage/)
- [Šablona záznamu rozhodnutí od Paula Mersona](https://github.com/pmerson/ADR-template)
- [Šablona záznamu rozhodnutí od Olafa Zimmermanna](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Šablona záznamu rozhodnutí od Garetha Morgana](sablony/sablona-zaznamu-rozhodnuti-gareth-morgan/)
- [Šablona záznamu rozhodnutí od GIG Cymru NHS Wales](sablony/sablona-zaznamu-rozhodnuti-gig-cymru-nhs-wales/)
- [Šablona záznamu rozhodnutí pro Důležitá technická rozhodnutí (ITD) od Ignacia Larrañagy](sablony/sablona-zaznamu-rozhodnuti-dulezita-technicka-rozhodnuti/)

Příklady:

- [CSS framework](priklady/framework-css/)
- [Konfigurace proměnných prostředí](priklady/konfigurace-promennych-prostredi/)
- [Metriky, monitory, upozornění](priklady/metriky-monitory-upozorneni/)
- [Microsoft Azure DevOps](priklady/microsoft-azure-devops/)
- [Monorepo nebo multirepo](priklady/monorepo-nebo-multirepo/)
- [Programovací jazyky](priklady/programovaci-jazyky/)
- [Ukládání tajemství](priklady/ukladani-tajemstvi/)
- [Formát časového razítka](priklady/format-casoveho-razitka/)
- [A mnoho dalších...](priklady/)

## Co je záznam architektonického rozhodnutí?

**Záznam architektonického rozhodnutí** (anglicky architecture decision record, ADR) je dokument, který zachycuje důležité architektonické rozhodnutí spolu s jeho kontextem a důsledky.

**Architektonické rozhodnutí** (anglicky architecture decision, AD) je volba v návrhu softwaru, která řeší významný požadavek.

**Protokol architektonických rozhodnutí** (anglicky architecture decision log, ADL) je soubor všech ADR vytvořených a udržovaných pro daný projekt (nebo organizaci).

**Architektonicky významný požadavek** (anglicky architecturally-significant requirement, ASR) je požadavek, který má měřitelný vliv na architekturu softwarového systému.

To vše spadá do tématu **správy architektonických znalostí** (anglicky architecture knowledge management, AKM).

Cílem tohoto dokumentu je poskytnout rychlý přehled o ADR, o tom, jak je vytvářet, a kde hledat další informace.

Zkratky:

  * **AD**: architektonické rozhodnutí

  * **ADL**: protokol architektonických rozhodnutí

  * **ADR**: záznam architektonického rozhodnutí

  * **AKM**: správa architektonických znalostí

  * **ASR**: architektonicky významný požadavek

## Jak začít používat ADR

Chcete-li začít používat ADR, promluvte si se svými spolupracovníky o těchto oblastech.

Identifikace rozhodnutí:

  * Jak naléhavé a jak důležité je architektonické rozhodnutí?

  * Musí se učinit nyní, nebo může počkat, až se bude vědět víc?

  * Při identifikaci rozhodnutí může pomoci jak osobní a kolektivní zkušenost, tak uznávané metody a postupy návrhu.

  * V ideálním případě veďte seznam rozhodnutí k učinění, který doplňuje seznam úkolů produktu.

Rozhodování:

  * Existuje řada technik rozhodování, jak obecných, tak specifických pro softwarovou architekturu, například mapování dialogu (dialogue mapping).

  * Skupinové rozhodování je aktivní téma výzkumu.

Prosazení a vymáhání rozhodnutí:

  * Architektonická rozhodnutí se používají při návrhu softwaru; proto je nutné je sdělit zainteresovaným stranám systému, které jej financují, vyvíjejí a provozují, a získat jejich souhlas.

  * Dvě související praktiky jsou architektonicky zřejmé styly kódování a revize kódu zaměřené na architektonické otázky a rozhodnutí.

  * Architektonická rozhodnutí je třeba (znovu) zvážit také při modernizaci softwarového systému v rámci vývoje softwaru.

Sdílení rozhodnutí (volitelné):

  * Mnoho architektonických rozhodnutí se opakuje napříč projekty.

  * Zkušenosti s minulými rozhodnutími, dobré i špatné, proto mohou být cenným opakovaně použitelným majetkem, pokud se používá explicitní strategie správy znalostí.

Dokumentace rozhodnutí:

  * Existuje mnoho šablon a nástrojů pro zachycování rozhodnutí.

  * Viz agilní komunity, např. ADR M. Nygarda.

  * Viz tradiční procesy softwarového inženýrství a návrhu architektury, např. tabulková uspořádání navržená IBM UMF a Tyreem a Akermanem z CapitalOne.

Další informace:

  * Výše uvedené kroky jsou převzaty z hesla Wikipedie [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Jak začít používat ADR s nástroji

- [MySpec](https://myspec.dev) — Automatizovaná platforma pro specifikace a architektonická rozhodnutí, která strukturuje ústavu projektu, technickou architekturu a ADR do čistého Markdownu poskytovaného přes MCP.

S používáním ADR s nástroji můžete začít libovolným způsobem.

Například:

  * Pokud máte rádi Disk Google a online úpravy, můžete vytvořit dokument Google nebo tabulku Google.

  * Pokud máte rádi správu verzí zdrojového kódu, například git, můžete pro každé ADR vytvořit soubor.

  * Pokud máte rádi nástroje pro plánování projektů, například Atlassian Jira, můžete použít plánovací sledování nástroje.

  * Pokud máte rádi wiki, například MediaWiki, můžete vytvořit wiki s ADR.

## Jak začít používat ADR s gitem

Pokud máte rádi správu verzí v gitu, takto rádi začínáme používat ADR s gitem v typickém softwarovém projektu se zdrojovým kódem.

Vytvořte adresář pro soubory ADR:

```sh
$ mkdir adr
```

Pro každé ADR vytvořte textový soubor, například `choose-database.md`:

```sh
$ vi choose-database.md
```

Napište do ADR cokoli chcete. Nápady najdete v šablonách v tomto repozitáři.

Odevzdejte ADR (commit) do svého repozitáře git.

## Dovednosti Claude Code pro ADR

Tento repozitář obsahuje dvě dovednosti (skills) pro [Claude Code](https://claude.com/claude-code) v adresáři [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), aby programovací agent s umělou inteligencí mohl psát a udržovat ADR tak, jak tento projekt doporučuje:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — univerzální, pro každého, kdo píše ADR v jakémkoli projektu. Pomáhá rozhodnout, zda rozhodnutí potřebuje ADR, vytvoří adresář `adr/` nebo `decisions/`, pojmenuje soubor, vybere šablonu z jedenácti dodaných náčrtů a napíše pevné sekce Kontext/Rozhodnutí/Důsledky.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — specificky pro správce tohoto repozitáře. Dokumentuje uspořádání repozitáře, konvenci zrcadlení README/locales a přesné kroky pro přidání nové šablony, příkladu nebo odkazu na nástroj.

Chcete-li dovednost použít, zkopírujte její složku do `.claude/skills/` v kořeni repozitáře, ve kterém pracujete (nebo do `~/.claude/skills/`, aby byla dostupná ve všech projektech), a poté požádejte Claude Code o napsání nebo revizi ADR.

## Konvence pojmenování souborů ADR

Pokud se rozhodnete vytvářet ADR v běžných textových souborech, možná budete chtít vymyslet vlastní konvenci pojmenování souborů ADR.

My preferujeme konvenci pojmenování souborů s určitým formátem.

Příklady:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Naše konvence pojmenování souborů:

  * Název obsahuje slovesnou frázi v rozkazovacím způsobu (v angličtině přítomný čas). Zlepšuje to čitelnost a odpovídá to formátu našich zpráv commitů.

  * Název používá malá písmena a pomlčky (stejně jako tento repozitář). Je to kompromis mezi čitelností a použitelností v systému.

  * Přípona je markdown. To může být užitečné pro snadné formátování.

## Tipy pro psaní dobrých ADR

Vlastnosti dobrého ADR:

* Odůvodnění: Vysvětlete důvody pro dané architektonické rozhodnutí. Může zahrnovat kontext (viz níže), výhody a nevýhody různých možných voleb, srovnání funkcí, diskuse o nákladech a přínosech a další.

* Konkrétnost: Každé ADR by mělo být o jednom architektonickém rozhodnutí, ne o více.

* Časová razítka: Uveďte, kdy byla napsána každá položka ADR. Je to zvlášť důležité u aspektů, které se mohou v čase měnit, jako jsou náklady, harmonogramy, škálování a podobně.

* Neměnnost: Neměňte existující informace v ADR. Místo toho ADR doplňte přidáním nových informací nebo ho nahraďte vytvořením nového ADR.

Vlastnosti dobré sekce „Kontext“ v ADR:

* Vysvětlete situaci své organizace a obchodní priority.

* Zahrňte zdůvodnění a úvahy vycházející ze sociálního složení a dovedností vašich týmů.

* Zahrňte relevantní výhody a nevýhody a popište je pojmy, které odpovídají vašim potřebám a cílům.

Vlastnosti dobré sekce „Důsledky“ v ADR:

* Vysvětlete, co z učinění rozhodnutí vyplývá. Může zahrnovat dopady, výsledky, výstupy, navazující kroky a další.

* Zahrňte informace o případných následných ADR. Je poměrně běžné, že jedno ADR vyvolá potřebu dalších ADR, například když jedno ADR učiní velkou zastřešující volbu, která zase vytváří potřebu dalších menších rozhodnutí.

* Zahrňte případné procesy zpětného hodnocení. Je typické, že týmy každé ADR přezkoumají po měsíci, aby porovnaly informace v ADR s tím, co se stalo v praxi, a mohly se poučit a růst.

Nové ADR může nahradit předchozí ADR:

* Když se učiní architektonické rozhodnutí, které nahrazuje nebo ruší předchozí ADR, měl by se vytvořit nové ADR

## Příklady šablon ADR

Příklady šablon ADR shromážděné z internetu:

- [Šablona ADR od Michaela Nygarda](sablony/sablona-zaznamu-rozhodnuti-michael-nygard/) (jednoduchá a oblíbená)

- [Šablona ADR od Jeffa Tyreeho a Arta Akermana](sablony/sablona-zaznamu-rozhodnuti-jeff-tyree-a-art-akerman/) (propracovanější)

- [Šablona ADR pro alexandrijský vzor](sablony/sablona-zaznamu-rozhodnuti-alexandrijsky-vzor/) (jednoduchá, s podrobnostmi o kontextu)

- [Šablona ADR pro podnikatelský záměr](sablony/sablona-zaznamu-rozhodnuti-podnikatelsky-zamer/) (více orientovaná na MBA, s náklady, SWOT a více stanovisky)

- [Šablona ADR projektu Markdown Any Decision Records (MADR)](sablony/sablona-zaznamu-rozhodnuti-projekt-madr/) (jednoduchá i rozpracovaná verze; ta druhá zdůrazňuje možnosti a jejich klady a zápory)

- [Šablona ADR s Planguage](sablony/sablona-zaznamu-rozhodnuti-s-planguage/) (více orientovaná na zajištění kvality)

- [Šablona pro Důležitá technická rozhodnutí (ITD) od Ignacia Larrañagy](sablony/sablona-zaznamu-rozhodnuti-dulezita-technicka-rozhodnuti/) (štíhlá a zaměřená na rozhodnutí, optimalizovaná pro rychlou revizi vedením)

## Rady k týmové práci pro ADR

Pokud uvažujete o používání záznamů rozhodnutí ve svém týmu, zde je několik rad, které jsme se naučili při práci s mnoha týmy.

Máte příležitost vést své spolupracovníky tím, že společně mluvíte o „proč“, místo abyste nařizovali „co“. Například záznamy rozhodnutí jsou způsob, jak týmy mohou chytřeji myslet a lépe komunikovat; záznamy rozhodnutí nemají hodnotu, pokud jsou jen dodatečným vynuceným papírováním.

Některé týmy mnohem více preferují název „rozhodnutí“ před zkratkou „ADR“. Když některé týmy použijí název adresáře „decisions“, je to, jako by se rozsvítila žárovka, a tým začne do adresáře vkládat více informací, například rozhodnutí o dodavatelích, plánovací rozhodnutí, rozhodnutí o harmonogramech atd. Všechny tyto druhy informací mohou používat stejnou šablonu. Domníváme se, že se lidé učí rychleji se slovy („rozhodnutí“) než se zkratkami („ADR“), že jsou více motivováni psát rozpracované dokumenty, když se odstraní slovo „záznam“, a také že někteří vývojáři a někteří manažeři slovo „architektura“ nemají rádi.

Teoreticky je neměnnost ideální. V praxi se našim týmům osvědčila spíše měnitelnost. Novou informaci vkládáme do stávajícího ADR s datem a poznámkou, že informace přišla po rozhodnutí. Tento přístup vede k „živému dokumentu“, který můžeme všichni aktualizovat. Typické aktualizace nastávají, když získáme informace díky novým kolegům, novým nabídkám, skutečným výsledkům našeho používání nebo dodatečným změnám třetích stran, jako jsou schopnosti dodavatelů, cenové plány, licenční smlouvy atd.

## Otázky k týmové práci pro ADR

### Kdo může vytvořit ADR?

Zvažte oblasti jako konkrétní osoby, konkrétní role, konkrétní týmy nebo konkrétní oddělení; zvažte také, zda existují osoby, role, týmy nebo oddělení, které mohou ADR zadat, tedy požádat o ADR, které napíše někdo jiný. 

Příklad odpovědi: Každá osoba v naší organizaci, která si přečetla stránku README o záznamech architektonických rozhodnutí, může navrhnout ADR, tedy začít ho psát a sdílet ho s týmem.

### Co ospravedlňuje zahájení ADR?

Zvažte oblasti jako způsoby práce týmů vaší organizace, strukturu vašeho softwarového systému, koordinaci mezi týmy, dlouhodobou udržovatelnost, externí rozhraní, komu chcete prospět a podobně. 

Příklad odpovědi: Chceme vytvořit ADR, když chceme, aby budoucí vývojáři pochopili „proč“ děláme to, co děláme.

### Co ospravedlňuje nezahájení ADR?

Zvažte oblasti jako rozhodnutí, která nejsou o architektuře nebo jsou drobná, například s minimálním rizikem, samostatná nebo týkající se jednoho vývojáře, nebo jsou již plně pokryta jinde, například standardy, zásadami nebo dokumentací, nebo jsou dočasná, například náhradní řešení, ověření konceptu nebo experimenty. 

Příklad odpovědi: ADR vynecháme, když je rozhodnutí omezené rozsahem, časem, rizikem i náklady nebo je již pokryto jinde.

### Jaký je životní cyklus ADR?

Zvažte oblasti jako proces vytváření, proces zkoumání, proces rozhodování, proces implementace a proces vyřazování. Zvažte, jak sledovat životní cyklus ADR v čase, například jak přesunout ADR z jednoho stavu do dalšího a jak to sdělit zainteresovaným stranám. 

Příklad odpovědi: Chceme, aby ADR mělo pět fází životního cyklu: Zahájení → Zkoumání → Hodnocení → Implementace → Údržba → Vyřazení.

### Jaká jsou kritéria pro kroky životního cyklu ADR?

Zvažte oblasti jako kritéria přijetí ADR, tedy jak poznáte, že je dost dobré, aby postoupilo z jednoho kroku životního cyklu do dalšího? Je problém jasně formulován? Byly zváženy alternativy? Jsou kompromisy dostatečně pochopeny a zdokumentovány?
Je k dispozici veškerý relevantní kontext? Jsou zapojeny všechny relevantní zainteresované strany? Byla zapracována veškerá zpětná vazba? 

Příklad odpovědi: Chceme, aby o ADR hlasovaly zainteresované strany, když aktivní tým 1) dokončil svůj výzkum, 2) dokončil své hodnocení, 3) zveřejnil návrh ADR zainteresovaným stranám s žádostí o připomínky a lhůtou jednoho týdne, 4) všechny připomínky zainteresovaných stran byly zapracovány a vyřešeny.

### Jaké role a odpovědnosti souvisejí s ADR?

Zvažte role jako navrhovatel, výzkumník, hodnotitel, recenzent, schvalovatel, správce a podobně. Zvažte odpovědnosti jako komunikace se zainteresovanými stranami, zajištění splnění očekávání, sdílení na webu nebo intranetu a pravidelná revize práce, zejména když nastanou relevantní změny.

Příklad odpovědi: Chceme, aby každé ADR mělo vždy primární kontaktní osobu, sekundární kontaktní osobu a odpovědný tým; ti odpovídají za komunikaci, publikace, údržbu, pravidelnou revizi alespoň jednou ročně a případné vyřazení podle potřeby.

### Jak souvisí správa a řízení (governance) s ADR?

Zvažte oblasti jako způsoby práce vaší organizace, případné zvláštní potřeby souladu, například právní aspekty nebo aspekty lidských zdrojů, a jak chcete zacházet s konsensem, konfliktem a eskalací. Existují oblasti, osoby nebo týmy, které mohou mít na ADR větší vliv než ostatní, například ho mohou schválit, hlasovat o něm nebo ho vetovat?

Příklad odpovědi: Řízení ADR probíhá v tomto pořadí priority: generální ředitel (CEO), technický ředitel (CTO), právní ředitel (CLO), tým, který ADR implementuje, odborníci v týmu, kteří o architektonickém rozhodnutí vědí nejvíce. Nikdo jiný řízení nemá, pokud to není popsáno v ADR. 

### Jaké principy souvisejí s ADR?

Zvažte oblasti jako způsoby práce vaší organizace, které zahrnují rychlý versus pomalý postup, konsensus versus konflikt při rozhodování, preference rizika versus preference bezpečí, veřejná diskuse versus soukromá diskuse a podobně.

Příklad odpovědi: Používáme principy vedení: sklon k akci, nesouhlas a závazek (disagree-and-commit), odhady na 70 % jsou dost dobré pro snadno vratná a snadno izolovatelná rozhodnutí a veřejné způsoby práce s výjimkou důvěrných informací popsaných v dohodě o mlčenlivosti naší organizace.

## Koncepty dalšího kroku pro ADR

[Arc42](https://arc42.org/) pragmaticky odpovídá na dvě otázky a lze ji přizpůsobit vašim konkrétním potřebám. Co by měla vaše dokumentace/komunikace o architektuře obsahovat? Jak ji dokumentovat/komunikovat? Arc42 zahrnuje záznamy architektonických rozhodnutí a také pokyny k cílům, omezením, kontextu, kvalitě, rizikům a dalším tématům.

[Model C4](https://c4model.com/) je snadno naučitelný přístup k diagramování softwarové architektury, přívětivý pro vývojáře. C4 je hierarchická sada diagramů pro kontext, kontejnery, komponenty, kód a doplňkové diagramy pro krajinu systémů, dynamiku a nasazení.

## Architektonické diagramy, pohledy a hlediska

Architektonický diagram se nazývá „architektonický pohled“.

„Architektonický pohled“ je instancí „architektonického hlediska“.

„Architektonické hledisko“ má konkrétní publikum s konkrétními zájmy.

Příklady architektonických hledisek, pohledů a diagramů:

- Obchodní schopnosti

- Obchodní procesy na vysoké úrovni

- [Hodnotové toky](https://en.wikipedia.org/wiki/Value_stream)

- Softwarové funkce namapované na aplikační komponenty

- Kontextový diagram [modelu C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- Diagram kontejnerů [modelu C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- [Diagram entit a vztahů](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) pro mapování datových entit na aplikační komponenty

- [Sekvenční diagramy](https://en.wikipedia.org/wiki/Sequence_diagram) popisující funkční toky uvnitř systémů i integrační toky

- Diagramy [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) popisující datové toky mezi aplikačními komponentami

- Diagramy [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) popisující obchodní procesy / uživatelské scénáře

- Diagramy [Identity and Access Management](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM)

- Diagramy [Role-Based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) s rolemi podle aplikačních komponent

- Diagramy [Attribute-Based Access Control](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) s atributy podle aplikačních komponent

- Diagramy ochrany osobních údajů

Související diagramy:

- Diagram případů užití ukazuje případy užití vedení/zákazníkům, což předchází požadavkům, které předchází softwarové architektuře.

- Diagram nasazení ukazuje fyzický hardware/počítače, na kterých jsou nasazeny softwarové komponenty.
- Diagram datových toků ukazuje, jak se data v systému pohybují a jak se transformují.
- Sekvenční diagram slouží k ukázání toho, jak fungují protokoly, například HTTP, v časové ose.

- Diagram aktivit zobrazuje pracovní tok aktivit prováděných softwarovým systémem, například AI NPC.

## Fitness funkce pro rozhodnutí jako kód

Fitness funkce (fitness functions) jsou objektivní automatizované kontroly napsané programovým kódem, které ověřují, že se rozhodnutí dodržují.

- Fitness funkce činí rozhodnutí testovatelnými a zajistitelnými.

- Fitness funkce pro rozhodnutí mohou výrazně pomoci při zajištění kvality, regulačních procesech a cílech správy a řízení.

### Jak fitness funkce souvisejí s rozhodnutími

Záznam rozhodnutí dokumentuje rozhodnutí, zatímco fitness funkce ho zajišťuje.

- Příklad rozhodnutí: Pro požadavky na audit používáme event sourcing.

- Příklad fitness funkce: Server kontinuální integrace používáme k testování, že každá změna stavu musí vytvářet události.

### Proč fitness funkce rozhodnutím pomáhají

Objektivní měření: Fitness funkce uspějí nebo selžou, takže práce je viditelná a jasná.

Nepřetržité používání: Fitness funkce jsou vaše živá pravidla, spouštěná při každém commitu a buildu.

Jistota při refaktorování: Fitness funkce automaticky zachytí chyby v pravidlech rozhodnutí.

Škálovatelná správa: Fitness funkce zajišťují standardy bez vytváření úzkých míst.

### Mohou fitness funkce využívat AI?

Fitness funkce mohou pro rozhodnutí využívat velké jazykové modely (LLM) AI tím, že kladou otázky k vaší práci,
například k vašim plánům, kódu, schématům, API a dalším:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Jednotkové testování architektury

[ArchUnit](https://www.archunit.org/): kontrola architektonických pravidel kódu v Javě pomocí libovolného běžného frameworku jednotkových testů pro Javu.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kontrola architektonických pravidel kódu v TypeScriptu a JavaScriptu pomocí Jest, Vitest, Jasmine atd.

## Ochranná pravidla rozhodnutí pro pull requesty

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
automaticky zobrazí správné záznamy o rozhodnutích ve správný okamžik — když
vývojář aktivně mění kód, který tato rozhodnutí pokrývají. Místo spoléhání na to,
že vývojáři před sloučením prostudují složku s dokumentací, se relevantní kontext
objeví přímo v pull requestu.

Funguje s jakýmkoli typem záznamu o rozhodnutí: architektonická rozhodnutí, datová rozhodnutí,
rozhodnutí o souladu s předpisy, klinická a lékařská rozhodnutí, bezpečnostní rozhodnutí a další.

Funguje také s jakýmkoli systémem CI (GitLab, Jenkins, CircleCI) a jako pre-commit hook.
Open source. Licence MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) je GitHub
Action, která neprojde pull requestem, pokud se sledované cesty kódu změní
bez přidání nebo aktualizace záznamu architektonického rozhodnutí. Výjimky
jsou explicitní: řádek `ADR-Exempt:` s odůvodněním propustí bránu a zapíše se do souhrnu
úlohy. Nezávislé na šabloně, bez závislostí. Open source. Licence MIT.

## Další informace

Úvod:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Šablony:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Do hloubky:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - bezplatná měsíční lekce softwarové architektury

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Nástroje:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Pokyny specifické pro společnosti:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Příklady:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Videa:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcasty:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Knihy:

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

Viz také:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Dodavatelsky neutrální, strojově čitelný formát YAML/JSON pro reprezentaci rozhodnutí s explicitním zdůvodněním, předpoklady, kognitivním stavem a kompromisy. Doplňuje ADR přidáním strukturovaného, validovatelného zdůvodnění do dokumentace rozhodnutí.
