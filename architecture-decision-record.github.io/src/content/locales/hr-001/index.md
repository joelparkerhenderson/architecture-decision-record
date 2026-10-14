# Zapis arhitekturne odluke (ADR)

Zapis arhitekturne odluke (ADR) je dokument koji bilježi važnu arhitekturnu odluku zajedno s njezinim kontekstom i posljedicama.

> [!IMPORTANT]
> Sami provedite dubinsku provjeru ovih resursa prije nego što ih koristite u bilo kojim kritičnim sustavima.

Sadržaj:

- [Što je zapis arhitekturne odluke?](#što-je-zapis-arhitekturne-odluke)
- [Kako početi koristiti ADR](#kako-početi-koristiti-adr)
- [Kako početi koristiti ADR s alatima](#kako-početi-koristiti-adr-s-alatima)
- [Kako početi koristiti ADR s gitom](#kako-početi-koristiti-adr-s-gitom)
- [Claude Code vještine za ADR-ove](#claude-code-vještine-za-adr-ove)
- [Konvencije imenovanja datoteka za ADR](#konvencije-imenovanja-datoteka-za-adr)
- [Savjeti za pisanje dobrih ADR-ova](#savjeti-za-pisanje-dobrih-adr-ova)
- [Primjeri predložaka za ADR](#primjeri-predložaka-za-adr)
- [Savjeti za timski rad za ADR](#savjeti-za-timski-rad-za-adr)
- [Pitanja za timski rad za ADR-ove](#pitanja-za-timski-rad-za-adr-ove)
- [Koncepti sljedećeg koraka za ADR-ove](#koncepti-sljedećeg-koraka-za-adr-ove)
- [Arhitekturni dijagrami, pogledi i gledišta](#arhitekturni-dijagrami-pogledi-i-gledišta)
- [Fitness funkcije za odluke kao kod](#fitness-funkcije-za-odluke-kao-kod)
- [Zaštitne ograde odluka za pull requestove](#zaštitne-ograde-odluka-za-pull-requestove)
- [Više informacija](#više-informacija)

Predlošci:

- [Predložak zapisa odluke – Jeff Tyree i Art Akerman](predlosci/predlozak-zapisa-odluke-jeff-tyree-i-art-akerman/)
- [Predložak zapisa odluke – Michael Nygard](predlosci/predlozak-zapisa-odluke-michael-nygard/)
- [Predložak zapisa odluke – EdgeX](predlosci/predlozak-zapisa-odluke-edgex/)
- [Predložak zapisa odluke – arc42](predlosci/predlozak-zapisa-odluke-arc42/)
- [Predložak zapisa odluke za aleksandrijski obrazac](predlosci/predlozak-zapisa-odluke-za-aleksandrijski-obrazac/)
- [Predložak zapisa odluke za poslovni slučaj](predlosci/predlozak-zapisa-odluke-za-poslovni-slucaj/)
- [Predložak zapisa odluke projekta MADR](predlosci/predlozak-zapisa-odluke-projekta-madr/)
- [Predložak zapisa odluke s Planguageom](predlosci/predlozak-zapisa-odluke-s-planguageom/)
- [Predložak zapisa odluke – Paulo Merson](https://github.com/pmerson/ADR-template)
- [Predložak zapisa odluke – Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Predložak zapisa odluke – Gareth Morgan](predlosci/predlozak-zapisa-odluke-gareth-morgan/)
- [Predložak zapisa odluke – GIG Cymru NHS Wales](predlosci/predlozak-zapisa-odluke-gig-cymru-nhs-wales/)
- [Predložak zapisa odluke za važne tehničke odluke (ITD) – Ignacio Larrañaga](predlosci/predlozak-zapisa-odluke-za-vazne-tehnicke-odluke/)

Primjeri:

- [CSS okvir](primjeri/css-okvir/)
- [Konfiguracija varijabli okruženja](primjeri/konfiguracija-varijabli-okruzenja/)
- [Metrike, monitori, upozorenja](primjeri/metrike-monitori-upozorenja/)
- [Microsoft Azure DevOps](primjeri/microsoft-azure-devops/)
- [Monorepo ili multirepo](primjeri/monorepo-ili-multirepo/)
- [Programski jezici](primjeri/programski-jezici/)
- [Pohrana tajni](primjeri/pohrana-tajni/)
- [Format vremenske oznake](primjeri/format-vremenske-oznake/)
- [I još mnogo toga...](primjeri/)

## Što je zapis arhitekturne odluke?

**Zapis arhitekturne odluke** (ADR) je dokument koji bilježi važnu arhitekturnu odluku zajedno s njezinim kontekstom i posljedicama.

**Arhitekturna odluka** (AD) je odabir u dizajnu softvera koji odgovara na značajan zahtjev.

**Dnevnik arhitekturnih odluka** (ADL) je zbirka svih ADR-ova stvorenih i održavanih za određeni projekt (ili organizaciju).

**Arhitekturno značajan zahtjev** (ASR) je zahtjev koji ima mjerljiv učinak na arhitekturu softverskog sustava.

Sve to spada u područje **upravljanja arhitekturnim znanjem** (AKM).

Cilj ovog dokumenta je pružiti brz pregled ADR-ova, kako ih stvarati i gdje potražiti više informacija.

Kratice:

  * **AD**: arhitekturna odluka

  * **ADL**: dnevnik arhitekturnih odluka

  * **ADR**: zapis arhitekturne odluke

  * **AKM**: upravljanje arhitekturnim znanjem

  * **ASR**: arhitekturno značajan zahtjev

## Kako početi koristiti ADR

Za početak korištenja ADR-ova razgovarajte sa suradnicima o ovim područjima.

Identifikacija odluka:

  * Koliko je AD hitna i koliko važna?

  * Mora li se donijeti sada ili može pričekati dok se ne sazna više?

  * I osobno i kolektivno iskustvo, kao i priznate metode i prakse dizajna, mogu pomoći pri identifikaciji odluka.

  * Idealno održavajte popis odluka za donošenje koji nadopunjuje popis zadataka proizvoda.

Donošenje odluka:

  * Postoji niz tehnika donošenja odluka, i općenitih i specifičnih za softversku arhitekturu, na primjer mapiranje dijaloga.

  * Grupno donošenje odluka aktivna je istraživačka tema.

Provedba i nametanje odluka:

  * AD-ovi se koriste u dizajnu softvera; stoga se moraju komunicirati dionicima sustava koji ga financiraju, razvijaju i upravljaju njime te ih oni moraju prihvatiti.

  * Arhitekturno očiti stilovi kodiranja i pregledi koda koji se usredotočuju na arhitekturne brige i odluke dvije su povezane prakse.

  * AD-ove također treba (ponovno) razmotriti pri modernizaciji softverskog sustava u softverskoj evoluciji.

Dijeljenje odluka (neobavezno):

  * Mnoge se AD-ove ponavljaju kroz projekte.

  * Stoga iskustva s prošlim odlukama, i dobra i loša, mogu biti vrijedna ponovno iskoristiva imovina pri primjeni eksplicitne strategije upravljanja znanjem.

Dokumentiranje odluka:

  * Postoje mnogi predlošci i alati za bilježenje odluka.

  * Pogledajte agilne zajednice, npr. ADR-ove M. Nygarda.

  * Pogledajte tradicionalne procese softverskog inženjerstva i arhitekturnog dizajna, npr. tablične rasporede koje predlažu IBM UMF te Tyree i Akerman iz CapitalOnea.

Za više informacija:

  * Gornji koraci preuzeti su iz Wikipedijina članka o [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Kako početi koristiti ADR s alatima

- [MySpec](https://myspec.dev) — Platforma za automatiziranu specifikaciju i arhitekturne odluke koja strukturira projektni ustav, tehničku arhitekturu i ADR-ove u čist Markdown poslužen putem MCP-a.

ADR-ove s alatima možete početi koristiti na bilo koji način koji želite.

Na primjer:

  * Ako volite koristiti Google Drive i mrežno uređivanje, možete stvoriti Google Doc ili Google Sheet.

  * Ako volite koristiti kontrolu verzija izvornog koda, poput gita, možete stvoriti datoteku za svaki ADR.

  * Ako volite koristiti alate za planiranje projekata, poput Atlassian Jire, možete koristiti alat za praćenje planiranja.

  * Ako volite koristiti wikije, poput MediaWikija, možete stvoriti ADR wiki.

## Kako početi koristiti ADR s gitom

Ako volite koristiti git kontrolu verzija, evo kako mi volimo početi koristiti ADR-ove s gitom za tipičan softverski projekt s izvornim kodom.

Stvorite direktorij za ADR datoteke:

```sh
$ mkdir adr
```

Za svaki ADR stvorite tekstualnu datoteku, poput `choose-database.md`:

```sh
$ vi choose-database.md
```

Napišite što god želite u ADR. Pogledajte predloške u ovom repozitoriju za ideje.

Commitajte ADR u svoj git repozitorij.

## Claude Code vještine za ADR-ove

Ovaj repozitorij isporučuje dvije [Claude Code](https://claude.com/claude-code) vještine (skills) u direktoriju [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) kako bi AI agent za programiranje mogao pisati i održavati ADR-ove na način koji ovaj projekt preporučuje:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — opće namjene, za svakoga tko piše ADR-ove u bilo kojem projektu. Pomaže odlučiti treba li odluka ADR, stvara direktorij `adr/` ili `decisions/`, imenuje datoteku, odabire predložak iz jedanaest priloženih skica i piše čvrste odjeljke Kontekst/Odluka/Posljedice.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — posebno za održavatelje ovog repozitorija. Dokumentira raspored repozitorija, konvenciju zrcaljenja README/locales i točne korake za dodavanje novog predloška, primjera ili poveznice na alat.

Za korištenje vještine kopirajte njezinu mapu u `.claude/skills/` u korijenu repozitorija u kojem radite (ili u `~/.claude/skills/` kako bi bila dostupna u svim projektima), a zatim zamolite Claude Code da napiše ili pregleda ADR.

## Konvencije imenovanja datoteka za ADR

Ako odlučite stvarati svoje ADR-ove pomoću tipičnih tekstualnih datoteka, možda ćete htjeti osmisliti vlastitu konvenciju imenovanja datoteka za ADR.

Preferiramo konvenciju imenovanja datoteka koja ima određeni format.

Primjeri:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Naša konvencija imenovanja datoteka:

  * Naziv sadrži glagolsku frazu u imperativu u sadašnjem vremenu. To pomaže čitljivosti i odgovara našem formatu poruka commita.

  * Naziv koristi mala slova i crtice (kao i ovaj repozitorij). To je ravnoteža između čitljivosti i upotrebljivosti sustava.

  * Ekstenzija je markdown. To može biti korisno za jednostavno oblikovanje.

## Savjeti za pisanje dobrih ADR-ova

Karakteristike dobrog ADR-a:

* Obrazloženje: Objasnite razloge za konkretnu AD. To može uključivati kontekst (vidi dolje), prednosti i nedostatke različitih mogućih izbora, usporedbe značajki, rasprave o trošku i koristi i više.

* Specifičnost: Svaki ADR trebao bi biti o jednoj AD, a ne o više AD-ova.

* Vremenske oznake: Navedite kada je napisana svaka stavka u ADR-u. To je osobito važno za aspekte koji se mogu mijenjati tijekom vremena, kao što su troškovi, rasporedi, skaliranje i slično.

* Nepromjenjivost: Ne mijenjajte postojeće informacije u ADR-u. Umjesto toga dopunite ADR dodavanjem novih informacija ili zamijenite ADR stvaranjem novog ADR-a.

Karakteristike dobrog odjeljka „Kontekst“ u ADR-u:

* Objasnite situaciju svoje organizacije i poslovne prioritete.

* Uključite obrazloženje i razmatranja temeljena na društvenom i vještinskom sastavu vaših timova.

* Uključite relevantne prednosti i nedostatke i opišite ih izrazima koji su u skladu s vašim potrebama i ciljevima.

Karakteristike dobrog odjeljka „Posljedice“ u ADR-u:

* Objasnite što slijedi iz donošenja odluke. To može uključivati učinke, ishode, izlaze, nastavke i više.

* Uključite informacije o svim naknadnim ADR-ovima. Relativno je uobičajeno da jedan ADR potakne potrebu za više ADR-ova, na primjer kada jedan ADR donosi veliki sveobuhvatni izbor koji zauzvrat stvara potrebe za više manjih odluka.

* Uključite sve procese pregleda nakon akcije. Tipično je da timovi pregledavaju svaki ADR mjesec dana kasnije, kako bi usporedili informacije iz ADR-a s onim što se dogodilo u stvarnoj praksi, da bi učili i rasli.

Novi ADR može zauzeti mjesto prethodnog ADR-a:

* Kada se donese AD koja zamjenjuje ili poništava prethodni ADR, treba stvoriti novi ADR

## Primjeri predložaka za ADR

Primjeri predložaka za ADR prikupljeni s interneta:

- [Predložak ADR-a – Michael Nygard](predlosci/predlozak-zapisa-odluke-michael-nygard/) (jednostavan i popularan)

- [Predložak ADR-a – Jeff Tyree i Art Akerman](predlosci/predlozak-zapisa-odluke-jeff-tyree-i-art-akerman/) (sofisticiraniji)

- [Predložak ADR-a za aleksandrijski obrazac](predlosci/predlozak-zapisa-odluke-za-aleksandrijski-obrazac/) (jednostavan, s pojedinostima o kontekstu)

- [Predložak ADR-a za poslovni slučaj](predlosci/predlozak-zapisa-odluke-za-poslovni-slucaj/) (više usmjeren na MBA, s troškovima, SWOT-om i više mišljenja)

- [Predložak ADR-a projekta Markdown Any Decision Records (MADR)](predlosci/predlozak-zapisa-odluke-projekta-madr/) (i jednostavna i razrađena verzija; potonja naglašava opcije i njihove prednosti i nedostatke)

- [Predložak ADR-a s Planguageom](predlosci/predlozak-zapisa-odluke-s-planguageom/) (više usmjeren na osiguranje kvalitete)

- [Predložak za važne tehničke odluke (ITD) – Ignacio Larrañaga](predlosci/predlozak-zapisa-odluke-za-vazne-tehnicke-odluke/) (vitak i usmjeren na odluku, optimiziran za brz pregled rukovodstva)

## Savjeti za timski rad za ADR

Ako razmišljate o korištenju zapisa odluka sa svojim timom, evo nekoliko savjeta koje smo naučili radeći s mnogim timovima.

Imate priliku voditi svoje suradnike zajedničkim razgovorom o „zašto“, umjesto da naređujete „što“. Na primjer, zapisi odluka način su na koji timovi mogu pametnije razmišljati i bolje komunicirati; zapisi odluka nisu vrijedni ako su samo naknadno nametnut papirološki zahtjev.

Neki timovi mnogo više vole naziv „odluke“ nego kraticu „ADR“. Kada neki timovi koriste naziv direktorija „decisions“, kao da se upali žarulja i tim počne stavljati više informacija u direktorij, poput odluka o dobavljačima, odluka o planiranju, odluka o rasporedima i tako dalje. Sve te vrste informacija mogu koristiti isti predložak. Pretpostavljamo da ljudi brže uče uz riječi („odluke“) nego uz kratice („ADR-ovi“), da su ljudi motiviraniji pisati dokumente o radu u tijeku kada se ukloni riječ „zapis“, a također da neki programeri i neki menadžeri ne vole riječ „arhitektura“.

U teoriji je nepromjenjivost idealna. U praksi je promjenjivost za naše timove radila bolje. Umećemo nove informacije u postojeći ADR, s vremenskom oznakom i napomenom da su informacije stigle nakon odluke. Ovakav pristup vodi do „živog dokumenta“ koji svi možemo ažurirati. Tipična ažuriranja događaju se kada dobijemo informacije zahvaljujući novim suradnicima, novim ponudama ili stvarnim rezultatima naše upotrebe, ili nakon naknadnih promjena trećih strana kao što su mogućnosti dobavljača, cjenovni planovi, licencni ugovori i tako dalje.

## Pitanja za timski rad za ADR-ove

### Tko može stvoriti ADR?

Razmotrite područja poput određenih osoba, određenih uloga, određenih timova ili određenih odjela; razmotrite i postoje li osobe, uloge, timovi ili odjeli koji mogu naručiti ADR, odnosno zatražiti ga da ga napiše netko drugi. 

Primjer odgovora: Svaka osoba u našoj organizaciji koja je pročitala stranicu README zapisa arhitekturne odluke može predložiti ADR, što znači da ga može početi pisati i podijeliti s timom.

### Što opravdava pokretanje ADR-a?

Razmotrite područja poput načina rada tima u vašoj organizaciji, strukture vašeg softverskog sustava, koordinacije među timovima, dugoročnog održavanja, vanjskih sučelja, tko želite da ima koristi i slično. 

Primjer odgovora: Želimo stvoriti ADR kada želimo da budući programeri razumiju „zašto“ onoga što radimo.

### Što opravdava nepokretanje ADR-a?

Razmotrite područja poput odluka koje nisu o arhitekturi ili su sitne, primjerice minimalnog rizika, samostalne ili za jednog programera, ili su već u potpunosti pokrivene drugdje, primjerice standardima, politikama ili dokumentacijom, ili su privremene, primjerice zaobilazna rješenja, dokazi koncepta ili eksperimenti. 

Primjer odgovora: Želimo preskočiti ADR kada je odluka ograničena opsegom, vremenom, rizikom i troškom ili je već pokrivena drugdje.

### Koji je životni ciklus ADR-a?

Razmotrite područja poput procesa stvaranja, procesa istraživanja, procesa donošenja odluke, procesa implementacije i procesa povlačenja. Razmotrite kako pratiti životni ciklus ADR-a tijekom vremena, na primjer kako premjestiti ADR iz jednog stanja u sljedeće te kako to priopćiti dionicima. 

Primjer odgovora: Želimo da ADR ima pet faza životnog ciklusa: Pokretanje → Istraživanje → Vrednovanje → Implementacija → Održavanje → Povlačenje.

### Koji su kriteriji za korake životnog ciklusa ADR-a?

Razmotrite područja poput kriterija prihvaćanja ADR-a, odnosno kako znate da je dovoljno dobar za prelazak iz jednog koraka životnog ciklusa u sljedeći? Je li problem jasno artikuliran? Jesu li razmotrene alternative? Jesu li kompromisi dovoljno dobro shvaćeni i dokumentirani?
Je li sav relevantni kontekst na mjestu? Jesu li uključeni svi relevantni dionici? Je li uključena sva povratna informacija? 

Primjer odgovora: Želimo da dionici glasaju o ADR-u kada je aktivni tim 1) dovršio svoje istraživanje, 2) dovršio svoje vrednovanje, 3) objavio prijedlog ADR-a dionicima sa zahtjevom za komentare i rokom od jednog tjedna, 4) svi komentari dionika su ugrađeni i obrađeni.

### Koje uloge i odgovornosti djeluju s ADR-om?

Razmotrite uloge poput predlagatelja, istraživača, ocjenjivača, recenzenta, odobravatelja, održavatelja i slično. Razmotrite odgovornosti poput komunikacije s dionicima, osiguravanja ispunjenja očekivanja, dijeljenja na web-mjestu ili intranetu te povremenog pregleda rada, osobito kada se dogode relevantne promjene.

Primjer odgovora: Želimo da svaki ADR uvijek ima primarnu kontakt osobu, sekundarnu kontakt osobu i odgovorni tim; oni su odgovorni za komunikaciju, objave, održavanje, povremeni pregled najmanje jednom godišnje i eventualno povlačenje prema potrebi.

### Kako upravljanje (governance) djeluje s ADR-om?

Razmotrite područja poput načina rada vaše organizacije, posebnih potreba usklađenosti, primjerice za pravne aspekte ili aspekte ljudskih resursa, kako želite postupati s konsenzusom naspram sukoba naspram eskalacije. Postoje li područja, osobe ili timovi koji mogu imati veći utjecaj od drugih u pogledu ADR-a, primjerice mogu li ga odobriti, glasati o njemu ili staviti veto?

Primjer odgovora: Upravljanje ADR-om je ovim redoslijedom prioriteta: izvršni direktor, tehnički direktor, pravni direktor, tim koji implementira ADR, stručnjaci u timu koji najbolje poznaju AD. Nitko drugi nema upravljačku ovlast osim ako je opisano u ADR-u. 

### Koja načela djeluju s ADR-om?

Razmotrite područja poput načina rada vaše organizacije koji uključuju brzo kretanje naspram sporog kretanja, za konsenzus odluka naspram sukoba odluka, te za sklonosti riziku naspram sklonosti sigurnosti, javnu raspravu naspram privatne rasprave i slično.

Primjer odgovora: Koristimo načela vodstva sklonosti djelovanju, neslaganja i predanosti (disagree-and-commit), 70 % procjene dovoljno su dobre za lako reverzibilne i lako izolirane odluke, te javne načine rada uz iznimku povjerljivih informacija kako je opisano u ugovoru o povjerljivosti naše organizacije.

## Koncepti sljedećeg koraka za ADR-ove

[Arc42](https://arc42.org/) pragmatično odgovara na dva pitanja i može se prilagoditi vašim specifičnim potrebama. Što vrijedi dokumentirati/komunicirati o vašoj arhitekturi? Kako to vrijedi dokumentirati/komunicirati? Arc42 uključuje zapise arhitekturnih odluka kao i smjernice o ciljevima, ograničenjima, kontekstu, kvaliteti, rizicima i drugome.

[Model C4](https://c4model.com/) je lako naučiv, programerima prijazan pristup dijagramiranju softverske arhitekture. C4 je hijerarhijski skup dijagrama za kontekst, kontejnere, komponente, kod te dodatni dijagrami za krajolik sustava, dinamiku i implementaciju.

## Arhitekturni dijagrami, pogledi i gledišta

Arhitekturni dijagram naziva se „arhitekturni pogled“.

„Arhitekturni pogled“ je instanca „arhitekturnog gledišta“.

„Arhitekturno gledište“ ima određenu publiku s određenim interesima.

Primjeri arhitekturnih gledišta, pogleda i dijagrama:

- Poslovne sposobnosti

- Poslovni procesi na visokoj razini

- [Tokovi vrijednosti](https://en.wikipedia.org/wiki/Value_stream)

- Softverske funkcije preslikane na komponente aplikacije

- Kontekstni dijagram [modela C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- Dijagram kontejnera [modela C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- [Dijagram entiteta i veza](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) za preslikavanje podatkovnih entiteta na komponente aplikacije

- [Sekvencijski dijagrami](https://en.wikipedia.org/wiki/Sequence_diagram) koji opisuju funkcionalne tokove unutar sustava i integracijske tokove

- Dijagrami [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) koji opisuju tokove podataka među komponentama aplikacije

- Dijagrami [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) koji opisuju poslovne procese / korisničke scenarije

- Dijagrami [Identity and Access Management](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM)

- Dijagrami [Role-Based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) s ulogama po komponentama aplikacije

- Dijagrami [Attribute-Based Access Control](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) s atributima po komponentama aplikacije

- Dijagrami privatnosti

Povezani dijagrami:

- Dijagram slučajeva uporabe prikazuje slučajeve uporabe upravi/klijentima, što prethodi zahtjevima, koji prethode softverskoj arhitekturi.

- Dijagram razmještaja prikazuje fizički hardver/računala na kojima su softverske komponente razmještene.
- Dijagram toka podataka prikazuje kako se podaci kreću kroz sustav i kako se transformiraju.
- Sekvencijski dijagram služi za prikaz načina rada protokola, na primjer HTTP-a, na vremenskoj crti.

- Dijagram aktivnosti prikazuje tijek rada aktivnosti koje izvodi softverski sustav, na primjer UI NPC-a.

## Fitness funkcije za odluke kao kod

Fitness funkcije su objektivne automatizirane provjere, napisane programskim kodom, koje potvrđuju da se odluke održavaju.

- Fitness funkcije čine odluke provjerljivima i osiguranima.

- Fitness funkcije za odluke mogu uvelike pomoći osiguranju kvalitete, regulatornim procesima i ciljevima upravljanja.

### Kako se fitness funkcije povezuju s odlukama

Zapis odluke dokumentira odluku, dok fitness funkcija osigurava odluku.

- Primjer odluke: Koristimo event sourcing zbog zahtjeva revizije.

- Primjer fitness funkcije: Koristimo poslužitelj za kontinuiranu integraciju kako bismo testirali da sve promjene stanja moraju proizvoditi događaje.

### Zašto fitness funkcije pomažu odlukama

Objektivna mjerenja: Fitness funkcije prolaze ili padaju, pa je rad vidljiv i jasan.

Kontinuirana upotreba: Fitness funkcije su vaša živa pravila, pokreću se pri svakom commitu i buildu.

Povjerenje za refaktoriranje: Fitness funkcije automatski hvataju pogreške u pravilima odluka.

Skalabilno upravljanje: Fitness funkcije osiguravaju standarde bez stvaranja uskih grla.

### Mogu li fitness funkcije koristiti umjetnu inteligenciju?

Fitness funkcije mogu koristiti AI LLM-ove za odluke postavljanjem pitanja o vašem radu,
poput vaših planova, koda, shema, API-ja i drugog:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Jedinično testiranje arhitekture

[ArchUnit](https://www.archunit.org/): provjerava arhitekturna pravila Java koda pomoću bilo kojeg običnog okvira za jedinično testiranje u Javi.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): provjerava arhitekturna pravila TypeScript koda i JavaScript koda pomoću Jesta, Vitesta, Jasmine i drugih.

## Zaštitne ograde odluka za pull requestove

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
automatski izlaže prave zapise odluka u pravom trenutku — kada
programer aktivno mijenja kod koji te odluke pokrivaju. Umjesto oslanjanja na to da
programeri prije spajanja pročitaju mapu dokumentacije, relevantni kontekst
pojavljuje se izravno na pull requestu.

Radi s bilo kojom vrstom zapisa odluke: arhitekturnim odlukama, odlukama o podacima,
odlukama o usklađenosti, kliničkim i medicinskim odlukama, sigurnosnim odlukama i drugima.

Radi i s bilo kojim CI sustavom (GitLab, Jenkins, CircleCI) te kao pre-commit hook.
Otvorenog koda. Licenca MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) je GitHub
Action koji obara pull request ako se nadzirane putanje koda promijene
bez dodavanja ili ažuriranja zapisa arhitekturne odluke. Izuzeća
su eksplicitna: redak `ADR-Exempt:` s obrazloženjem propušta vrata i upisuje se u sažetak
zadatka. Neovisan o predlošku, bez ovisnosti. Otvorenog koda. Licenca MIT.

## Više informacija

Uvod:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Predlošci:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Dubinski:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - besplatna mjesečna lekcija o softverskoj arhitekturi

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Alati:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Smjernice specifične za tvrtke:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Primjeri:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Videozapisi:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcasti:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Knjige:

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

Vidi također:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Format YAML/JSON neutralan prema dobavljačima i strojno čitljiv za prikaz odluka s eksplicitnim obrazloženjem, pretpostavkama, kognitivnim stanjem i kompromisima. Nadopunjuje ADR-ove dodavanjem strukturiranog, provjerljivog obrazloženja u dokumentaciju odluka.
