# Konfigurace proměnných prostředí

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
  * [Důsledky ](#důsledky)
* [Související](#související)
  * [Související rozhodnutí](#související-rozhodnutí)
  * [Související požadavky](#související-požadavky)
  * [Související artefakty](#související-artefakty)
  * [Související principy](#související-principy)
* [Poznámky](#poznámky)


## Shrnutí


### Problém

Chceme, aby naše aplikace byly konfigurovatelné nad rámec artefaktů/binárních souborů/zdrojového kódu, takže jedno sestavení se může chovat odlišně podle prostředí nasazení.

  * K tomu chceme použít konfiguraci proměnnými prostředí.

  * Chceme konfiguraci spravovat pomocí souborů, které můžeme verzovat.

  * Chceme poskytnout určitý komfort pro vývojáře, například vědět, co lze konfigurovat a jaké jsou relevantní výchozí hodnoty.


### Rozhodnutí

Rozhodnuto pro soubory .env s přidruženým souborem výchozích hodnot a souborem schématu.


### Stav

Rozhodnuto. Jsme otevřeni zvážení nových možností, jakmile se objeví.


## Podrobnosti


### Předpoklady

Preferujeme oddělení kódu aplikace a kódu prostředí. Předpokládáme, že aplikace musí v různých prostředích fungovat různě, například ve vývojovém prostředí, testovacím prostředí, ukázkovém prostředí, produkčním prostředí atd.

Preferujeme průmyslovou praxi „12 factor app“ a ještě více související praxi „15 factor app“.

Mnoho našich předchozích projektů používalo konvenci souboru `.env` nebo podobného adresáře `.env`. Typickou praxí je udržovat je mimo správu verzí a místo toho použít jiný způsob jejich nasazení, verzování a správy.


### Omezení

Chceme udržet tajemství mimo náš systém správy verzí (VCS) pro správu zdrojového kódu (SCM).

Chceme usilovat o kompatibilitu s oblíbenými softwarovými frameworky a knihovnami. Například Node má modul „dotenv“ pro čtení konfigurace proměnných prostředí.


### Stanoviska

Zvažovali jsme několik přístupů:

  * Ukládat konfiguraci do aplikace, například do souboru `config.js`.

  * Ukládat konfiguraci do prostředí, například do souboru `.env`.

  * Načítat konfiguraci ze známého umístění, například z licenčního serveru.


### Argument

Zvolili jsme přístup se souborem .env, protože:

  * Je oblíbený, včetně odborníků.

  * Sleduje vzor souborů `.env`, které naše týmy úspěšně mnohokrát použily v mnoha projektech.

  * Je jednoduchý. Zejména prozatím jsme v pořádku s významnými kompromisy, které vidíme, jako je nedostatek schopností auditu ve srovnání s přístupem licenčního serveru.


### Důsledky 

Musíme vymyslet způsob, jak oddělit veřejnou konfiguraci proměnných prostředí od správy tajemství.


## Související


### Související rozhodnutí

Očekáváme, že všechny naše aplikace budou tento přístup používat.

Naplánujeme modernizaci všech našich aplikací, které používají méně schopný přístup, například pevné zakódování v binárním souboru nebo ve zdrojovém kódu.

Ponecháme beze změny všechny naše aplikace, které používají schopnější přístup, například licenční server.


### Související požadavky

Přidáme pro soubory možnosti devops, včetně hooků, testů a kontinuální integrace.

Musíme proškolit všechny kolegy vývojáře v tomto rozhodnutí.



### Související artefakty

Každá oblast, kam nasazujeme, bude potřebovat svůj vlastní soubor .env a související soubory.


### Související principy

Snadno vratné.


## Poznámky


Příklad souboru `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Příklad souboru `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Příklad souboru `.env.schema` jen s klíči:

```env
NAME
EMAIL
```
