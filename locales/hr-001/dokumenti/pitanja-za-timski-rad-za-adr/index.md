
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
