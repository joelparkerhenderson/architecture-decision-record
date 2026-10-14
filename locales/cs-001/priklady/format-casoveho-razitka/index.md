# Formát časového razítka

Obsah:

* [Shrnutí](#shrnutí)
  * [Problém](#problém)
  * [Rozhodnutí](#rozhodnutí)
  * [Stav](#stav)
* [Podrobnosti](#podrobnosti)
  * [Předpoklady](#předpoklady)
  * [Omezení](#omezení)
  * [Stanoviska](#stanoviska)
  * [Argument](#argument)
  * [Důsledky](#důsledky)
* [Související](#související)
  * [Související rozhodnutí](#související-rozhodnutí)
  * [Související požadavky](#související-požadavky)
  * [Související artefakty](#související-artefakty)
  * [Související principy](#související-principy)
* [Poznámky](#poznámky)


## Shrnutí


### Problém

Chceme mít možnost sledovat, kdy se věci dějí, pomocí časových razítek a konzistentního formátu časového razítka, který dobře funguje napříč všemi našimi systémy a systémy třetích stran.

Komunikujeme se systémy, které mají různé formáty časových razítek:

* Zprávy JSON nemají nativní formát časového razítka, takže musíme zvolit, jak převést časové razítko na řetězec a řetězec na časové razítko, tj. jak serializovat/deserializovat.

* Některé aplikace jsou nastaveny na místní čas místo času UTC. To může být pohodlné pro projekty, které se musí přizpůsobit místnímu času, například projekty, které spouštějí události založené na místním čase.

* Některé systémy mají různé potřeby a schopnosti časové přesnosti, například používají časové rozlišení sekund versus milisekund versus nanosekund. Například příkaz `date` operačního systému Linux používá výchozí časovou přesnost sekund, zatímco burza Nasdaq chce výchozí časovou přesnost nanosekund.


### Rozhodnutí

Volíme standardní formát časového razítka ISO 8601 s přesností na nanosekundy, konkrétně „YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ“.

Formát ukazuje rok, měsíc, den, hodinu, minutu, sekundu, nanosekundy a časové pásmo Zulu, neboli UTC, GMT.


### Stav

Rozhodnuto.


## Podrobnosti


### Předpoklady

Potřebujeme zpracovávat tyto textové řetězce časových razítek, převádět z časového razítka na řetězec (neboli serializovat) a z řetězce na časové razítko (neboli deserializovat).

Chceme formát, který se obecně snadno používá, snadno převádí a je snadno čitelný pro člověka.

Chceme kompatibilitu se širokou škálou externích systémů, které nemůžeme ovládat, například analytických systémů, databázových systémů, finančních systémů.


### Omezení

Některé systémy mají omezení časové přesnosti. Například příkaz `date` operačního systému macOS umí vypsat časovou přesnost v sekundách, ale ne v nanosekundách.


### Stanoviska

Zvažovali jsme řadu možností:

* Unix epocha, tj. jedno rostoucí číslo.

* Stručný textový formát „YYYYMMDDTHHMMSSNNNNNNNNN“.

* Použití místního časového pásma versus časového pásma UTC.


### Argument

Pro typické použití si ceníme snadného čtení/psaní lidmi více než čisté rychlosti/velikosti.

Pro typické použití chceme formát, který dobře funguje ve strojových systémech a také dobře funguje ručně, například při psaní ukázkových dat, čtení výstupu JSON, grepování logovacího souboru atd.

Pro netypické použití, například vysoce výkonné výpočty, očekáváme, že budeme chtít jakýkoli zvolený textový formát optimalizovat převodem textu na rychlejší formát, například vestavěný typ objektu data v programovacím jazyce. Textový formát tedy pro HPC příliš nezáleží.


### Důsledky

Naše různé textové systémy a časové systémy se na tomto formátu sjednotí.


## Související


### Související rozhodnutí

Možná budeme chtít rychlý/snadný způsob, jak sledovat také časové rozdíly, neboli doby trvání. Ty jsou snadné s časovými razítky Unix epochy.


### Související požadavky

Možná budeme chtít své rozhodnutí upravit, např. pokud budeme mít související požadavek na konkrétní druh razítka logovací zprávy, například pro Splunk, Sumo, ELK atd.


### Související artefakty

Formátovače a parsery pro jazyky:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Příklady z Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Příklady od SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Související principy

Snadno vratné. Můžeme poměrně snadno přejít na jiný formát, například Unix epochu.

Odložte předčasnou optimalizaci. Pro typické použití nám na hrstce znaků navíc, například ve formátu s pomlčkami a dvojtečkami, příliš nezáleží.


## Poznámky

Sem přidejte poznámky.
