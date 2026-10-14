# Šablona záznamu rozhodnutí od Jeffa Tyreeho a Arta Akermana

Toto je šablona popisu architektonického rozhodnutí zveřejněná v ["Architecture Decisions: Demystifying Architecture" od Jeffa Tyreeho a Arta Akermana, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Problém (Issue)**: Popište problém architektonického návrhu, který řešíte, a nenechte žádné otázky o tom, proč jej řešíte právě nyní. Při minimalistickém přístupu řešte a dokumentujte jen ty problémy, které je třeba řešit v různých bodech životního cyklu.

* **Rozhodnutí (Decision)**: Jasně uveďte směr architektury — tedy zvolené stanovisko.

* **Stav (Status)**: Stav rozhodnutí, například nevyřízené, rozhodnuté nebo schválené.

* **Skupina (Group)**: Můžete použít jednoduché seskupení — například integrace, prezentace, data atd. — k uspořádání množiny rozhodnutí. Můžete také použít sofistikovanější ontologii architektury, například ontologii Johna Kyaruziho a Jana van Katwijka, která obsahuje abstraktnější kategorie jako událost, kalendář a místo. Například s touto ontologií byste rozhodnutí týkající se výskytů, kde systém vyžaduje informace, seskupili pod událost.

* **Předpoklady (Assumptions)**: Jasně popište základní předpoklady prostředí, ve kterém rozhodnutí činíte — náklady, harmonogram, technologie atd. Všimněte si, že omezení prostředí (jako přijaté technologické standardy, podniková architektura, běžně používané vzory atd.) mohou omezit alternativy, které zvažujete.

* **Omezení (Constraints)**: Zachyťte jakákoli další omezení prostředí, která zvolená alternativa (rozhodnutí) může představovat.

* **Stanoviska (Positions)**: Uveďte stanoviska (schůdné možnosti nebo alternativy), která jste zvažovali. Ta často vyžadují dlouhá vysvětlení, někdy dokonce modely a diagramy. Není to vyčerpávající seznam. Přesto nechcete při závěrečné revizi slyšet otázku „Přemýšleli jste o...?“; vede to ke ztrátě důvěryhodnosti a zpochybňování jiných architektonických rozhodnutí. Tato sekce také pomáhá zajistit, že jste vyslechli názory druhých; výslovné uvedení jiných názorů pomáhá získat jejich zastánce pro vaše rozhodnutí.

* **Argument (Argument)**: Nastiňte, proč jste zvolili stanovisko, včetně položek jako náklady na implementaci, celkové náklady na vlastnictví, doba uvedení na trh a dostupnost potřebných vývojových zdrojů. To je pravděpodobně stejně důležité jako samotné rozhodnutí.

* **Důsledky (Implications)**: Rozhodnutí přináší mnoho důsledků, jak naznačuje metamodel REMAP. Rozhodnutí může například vyvolat potřebu učinit další rozhodnutí, vytvořit nové požadavky nebo změnit stávající, klást na prostředí další omezení, vyžadovat přehodnocení rozsahu nebo harmonogramu se zákazníky, nebo vyžadovat další školení personálu. Jasné pochopení a vyjádření důsledků vašeho rozhodnutí může být velmi účinné při získávání podpory a vytváření plánu pro provedení architektury.

* **Související rozhodnutí (Related decisions)**: Je zřejmé, že mnoho rozhodnutí spolu souvisí; můžete je zde uvést. Zjistili jsme však, že v praxi jsou užitečnější matice dohledatelnosti, rozhodovací stromy nebo metamodely. Metamodely jsou užitečné pro diagramové zobrazení složitých vztahů (například modely Rose).

* **Související požadavky (Related requirements)**: Rozhodnutí by měla být řízena obchodem. Pro prokázání odpovědnosti výslovně přiřaďte svá rozhodnutí k cílům nebo požadavkům. Tyto související požadavky můžete vyjmenovat zde, ale zjistili jsme, že je pohodlnější odkazovat na matici dohledatelnosti. Můžete posoudit příspěvek každého architektonického rozhodnutí ke splnění každého požadavku a poté posoudit, jak dobře je požadavek splněn napříč všemi rozhodnutími. Pokud rozhodnutí k plnění požadavku nepřispívá, toto rozhodnutí neděláte.

* **Související artefakty (Related artifacts)**: Uveďte související dokumenty architektury, návrhu nebo rozsahu, které toto rozhodnutí ovlivňuje.

* **Související principy (Related principles)**: Pokud má podnik dohodnutou sadu principů, ujistěte se, že je rozhodnutí v souladu s jedním nebo více z nich. To pomáhá zajistit sladění napříč doménami nebo systémy.

* **Poznámky (Notes)**: Protože rozhodovací proces může trvat týdny, zjistili jsme, že je užitečné zaznamenávat poznámky a problémy, které tým probírá během procesu seznamování s rozhodnutím.

