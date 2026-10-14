# Ukládání tajemství

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Shrnutí


### Problém

Potřebujeme ukládat tajemství, například hesla, soukromé klíče, autentizační tokeny atd.

Některá tajemství jsou orientována na uživatele. Náš vývojář například chce mít možnost vyhledat si heslo ke službě pomocí mobilního telefonu.

Některá tajemství jsou orientována na systém. Naše pipeline kontinuálního doručování například potřebuje umět vyhledat přihlašovací údaje k našemu cloudovému hostingu.


### Rozhodnutí

Bitwarden pro tajemství orientovaná na uživatele

Vault by HashiCorp pro tajemství orientovaná na systém.


### Stav

Rozhodnuto. Jsme otevřeni novým alternativám, jakmile se objeví.


## Podrobnosti


### Předpoklady

Pro tento účel a náš současný stav si ceníme pohodlí orientovaného na uživatele, například použitelných mobilních aplikací.

  * Chceme zajistit rychlý a snadný přístup na cestách, například pro vývojáře, který zajišťuje pohotovostní inženýrství spolehlivosti systémů.

  * Chceme mít možnost sdílet některá tajemství mezi vybranými lidmi, například týmem.

Nesnažíme se řešit jediného poskytovatele, například ukládání všech tajemství výhradně u Amazonu, Azure nebo Googlu.

Nechceme ad hoc přístupy, jako „zapamatuj si to“ nebo „napiš si to na papírek“ nebo „vymysli si vlastní způsob ukládání“.

Náš bezpečnostní model pro tento účel je v pořádku s používáním vysoce respektovaných komerčních hotových (COTS) dodavatelů, například SaaS nástrojů pro správu hesel.


### Omezení

Právě teď chceme něco snadného, tj. bez nutnosti psát kód, bez nutnosti instalovat servery, bez nutnosti velkého závazku, bez nutnosti všechny sjednocovat.


### Stanoviska

Zvažovali jsme:

1. Hotové správce hesel orientované na uživatele: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG atd.

2. Komerční hotové správce hesel orientované na systém: AWS KMS, Vault by HashiCorp, EnvKy, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Přístupy orientované na sdílení: použití sdíleného dokumentu Google, sdíleného kanálu Slack, sdílené síťové složky atd.

4. Nízkotechnologické ad hoc přístupy, například zapamatování, napsání poznámky nebo spoléhání na to, že si každý uživatel vymyslí vlastní postup.


### Argument

Bitwarden, LastPass, 1Password a Dashlane jsou všechno komerční hotové produkty.

  * Podobné druhy funkcí pro uživatele, týmy, organizace atd.

  * Desktopové možnosti pro Windows a Mac a mobilní možnosti pro Android a iOS.

  * Rozšíření prohlížeče pro Chrome a Firefox pro automatické vyplňování formulářů atd.

Bitwarden má oproti ostatním dvě výhody:

  * Bitwarden je open source, což znamená, že zabezpečení může být podrobeno vzájemné kontrole a také že společnost je široce oceňována vývojáři zaměřenými na bezpečnost.

  * Anekdoty pracovníků v softwaru popisují výraznou preferenci Bitwardenu před ostatními.

Typický dobrý článek: https://jcs.org/2017/11/17/bitwarden

Typický web s hlasováním porovnávajícím nástroje vedle sebe: https://stackshare.io/stackups/bitwarden-vs-dashlane

KeyPass, pass, GPG atd. odkládáme, protože přinášejí další složitost. Všechna tato řešení vypadají jako skvělá řešení pro technické uživatele. GPG vypadá obzvlášť dobře pro technické uživatele, kteří chtějí příkazově orientované schopnosti napříč systémy.

KMS odkládáme, protože má závislost na jediném poskytovateli.

Pro potřeby orientované na systém volíme Vault, protože recenze jsou úžasně pozitivní a protože HashiCorp má vynikající historii v softwaru a podpoře nejvyšší kvality.

Vetujeme přístupy sdílení, například pomocí sdílených dokumentů, sdílených kanálů, sdílených síťových složek atd. Ty neposkytují bezpečnostní kvality, které chceme.

Vetujeme ad hoc nízkotechnologické přístupy, protože se všichni shodujeme, že to není dlouhodobá cesta vpřed.


### Důsledky

Vývojáři možná budou muset sledovat tajemství na dvou místech: v Bitwardenu pro přístup orientovaný na uživatele a ve Vaultu pro přístup orientovaný na systém.


## Související


### Související rozhodnutí

Rozhodnutí o tom, který CI/CD server použít, musí zahrnovat důkaz schopnosti přistupovat k tajemstvím.

Budeme se muset rozhodnout, jak tajemství spravovat, pokud jde o zásady, rotace, organizace atd.


### Související požadavky

Tajemství budou mít související požadavky na compliance, auditování a nástup/odchod zaměstnanců v HR.


### Související artefakty

Očekáváme, že některá tajemství exportujeme do proměnných prostředí.


### Související principy

Snadno vratné.

Snadno paralelní, tj. je snadné používat různé správce hesel.

Levné vyzkoušet, tj. existuje bezplatná zkušební verze a žádný závazek.


## Poznámky

Poznámky k hodnocení zde. Všechny poznámky jsou veřejné komentáře na různých diskusních fórech o devops.


### Vault by HashiCorp

Vault je přesně to, co tady chcete. 

Nenasazujte však Vault rovnou do produkce, nejprve ho zprovozněte v testovacím prostředí, protože dokumentace HashiCorp může být dost nedostatečná, i když jsou jejich produkty úžasné.

Velmi strmá křivka učení a není triviální ho zprovoznit. 

Počáteční nastavení je trochu bolest. Stojí to ale za to a komunita ho podporuje dost na to, abyste se obešli.

Příšerná dokumentace, ale online je spousta návodů od lidí, kteří ho nastavovali, a když jich pár spojíte, budete mít funkční nastavení.

Počáteční nastavení vyžadovalo laborování s jejich helm charty (vault a consul). Technicky můžete použít mnoho dalších back-endů, ale opravdu, opravdu to nedoporučuji. Back-end/consul může být maličký, pokud nemáte hodně dat k uložení.

Určitě si zvykněte na používání CLI, protože GUI je spíš proof-of-concept/reklamní portál pro jejich enterprise edici.

To, že ho nemůžete jen „naplnit“, je bolest. Například pokud máte 5 polí, musíte ručně přidat každé pole pro každou položku. Takže to není tak, že byste předem definovali pole pro konkrétní kategorii a vyplnili tato pole pro všechny položky v kategorii, je to spíš „vše generujete pokaždé znovu“, což je (podle mě) pěkná otrava.

Možná se také podívejte na goldfish jako UI nad vaultem. Docela usnadňuje získat tým na svou stranu. Mají také demo. 1. Nastavte consul. 2. Nastavte vault ukazující na consul. 3. Nastavte goldfish ukazující na vault. 3. Nastavte nějakou úlohu cron pro spouštění consul snapshot pro zálohy.



### LastPass

LastPass Teams. Používáme ho, má vlastní šablony, ACL, podle mě nic nechybí.

Implementoval jsem LastPass ve své organizaci a dávám mu C+/B-. Největším problémem v poslední době je nedostatek spolehlivosti. Za posledních 90 dní bylo několik hodin, kdy byly trezory vynuceně přepnuty do offline režimu. To není pro mou organizaci ideální, protože máme doslova 4 000+ hesel uložených ve 20+ sdílených složkách. Jak si dokážete představit, při takovém počtu hesel se alespoň několik denně aktualizuje nebo přidá. Máme plán DR pro případ, že problémy trvají déle než hodinu nebo dvě: skript každou noc podepíše a zašifruje CSV výpis trezoru, který lze importovat do keepass.

LastPass měl nehlášené výkyvy zhoršené služby: přihlášení „funguje“, ale nenačte weby, v administrátorském panelu jsou náhodně nefunkční funkce a nesdílí správně klíče pro nové sdílené složky nejvyšší úrovně. Mám speciálního uživatele pro „key push“/zálohování, který je ve všech skupinách. Přihlášení jako tento uživatel obvykle opraví jakékoli problémy se sdílením klíčů, ale ne když je služba zhoršená, bez ohledu na to, co říká stavová stránka...

Pro integraci to může být snadné, pokud máte správné ACL s modelem nejmenších oprávnění, např. pokud má uživatel u položky nebo složky oprávnění ke čtení i zápisu a jen ke čtení, dostane jen oprávnění jen ke čtení. Bohužel ACL v mé organizaci nejsou nejlepší, takže jsem nakonec použil JSON provisioning API a ~500 řádků Pythonu, protože závislá povaha našich stovek ACL se špatně mapovala na model nejmenších oprávnění. Nakonec jsem získal všechna ACL, ve kterých uživatel byl, a provedl jakýsi průchod závislostmi.

Pokud je vaše ACL nebo struktura skupin už postavena s ohledem na strukturu nejmenších oprávnění, nástroj pro synchronizaci AD/LDAP pro Windows bude fungovat dobře.

Obraťte se na jejich prodejní tým a mohou vám zajistit delší zkušební verzi Enterprise. Ujistěte se, že plně rozumíte jejím omezením, než se rozhodnete. Měli jsme spoustu růstových bolestí, ale kromě výpadků nebo zhoršení na straně serveru to bylo neuvěřitelně hladké.


### Bitwarden

Bitwarden má kolem sebe pěkné nástroje (WebUI, CLI, mobilní, desktopové). Lze ho hostovat samostatně a poměrně snadno se nastavuje. Poměrně dobrá dokumentace a nástroj doporučovaný PrivacyTools.


### EnvKey

https://www.envkey.com/ je SaaS. Opravdu snadno se implementuje, integruje a spravuje.

Funkce:

  * Chraňte klíče API a přihlašovací údaje.

  * Udržujte konfiguraci synchronizovanou všude.

  * Chytrá, end-to-end šifrovaná správa konfigurace a tajemství. 

  * Zabraňte nezabezpečenému sdílení a rozrůstání konfigurace. 

  * Integrujte za pár minut.

Schopnosti:

  * Spravujte konfiguraci a úrovně přístupu pro všechny své aplikace, prostředí a týmy na jednom místě.

  * Nakonfigurujte jakékoli vývojové nebo serverové prostředí jedinou proměnnou prostředí.

Klady:

  * Dobrá domovská stránka.

  * Jasná hodnotová nabídka.

  * Vizuálně vynikající webová aplikace.

  * Vynikající ukázková data, např. Algolia, AWS, Datadog, GitHub, Stripe atd.

  * Mluvil jsem s zakladatelem 30 minut o společnosti, UI atd. Dane zní dobře informovaně, upřímně o kladech/záporech a jako životaschopný partner.

  * Společnost je v podstatě typická společnost z Y Combinator s 1 zakladatelem. V lednu 2018 získala 120 tisíc USD.

  * Důraz je na dosažení enterprise funkcí, zejména přechod z cloudového hostingu EnvKey buď na on-prem, nebo BYOC.

  * Potenciální cesta vpřed: začít s EnvKey kvůli snadnému použití a později (nebo souběžně) přidat Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant je open source služba pro správu tajemství, která poskytuje uživatelsky přívětivé ukládání tajemství a přístup k nim bezpečným způsobem, od vývojářů ve Lyftu.

Autentizace KMS: Confidant řeší problém slepice a vejce při autentizaci pomocí AWS KMS a IAM, aby role IAM mohly generovat bezpečné autentizační tokeny, které může Confidant ověřit. Confidant také spravuje granty KMS pro vaše role IAM, což rolím IAM umožňuje generovat tokeny použitelné pro autentizaci mezi službami nebo pro předávání šifrovaných zpráv mezi službami.

Šifrování verzovaných tajemství v klidu: Confidant ukládá tajemství způsobem jen pro přidávání do DynamoDB a pro každou revizi každého tajemství generuje jedinečný datový klíč KMS pomocí symetrické autentizované kryptografie Fernet.

Uživatelsky přívětivé webové rozhraní pro správu tajemství: Confidant poskytuje webové rozhraní AngularJS, které koncovým uživatelům umožňuje snadno spravovat tajemství, mapování tajemství na služby a historii změn.


### Devolutions Password Server

https://server.devolutions.net/

Zabezpečte, spravujte a monitorujte přístup k privilegovaným účtům a relacím.

Komplexní, vysoce zabezpečený trezor hesel, který vám umožňuje řídit přístup k vašim privilegovaným účtům a zároveň zlepšuje celkovou viditelnost sítě pro správce systémů a poskytuje bezproblémový zážitek koncovým uživatelům.

Funkce: centralizovaný organizační trezor hesel, soukromý trezor specifický pro uživatele, správce hesel, vkládání přihlašovacích údajů,
integrace s Active Directory, řízení přístupu na základě rolí, dvoufaktorová autentizace, připravenost pro enterprise, omezení IP, možnosti správy, automatický generátor hesel, přístup z mobilní aplikace, historie hesel, přístupové zprávy, e-mailová upozornění.

  * podporuje šifrování dat

  * podporuje více schémat autentizace včetně LDAP, O365 a lokálních uživatelů S podporou MFA z více zdrojů

  * více repozitářů/trezorů s jemně členěnými řízeními přístupu pro více týmů

  * moderní webové UI

  * soukromé trezory přihlašovacích údajů a připojení pro osobní přihlašovací údaje/připojení

  * mobilní aplikace pro iOS/Android

  * auditní logy pro každou položku, kdo/co/kdy s volitelnou výzvou, proč přistupují

  * přizpůsobitelné šablony (ačkoli nativně podporují stovky typů připojení)

  * spousta dalších funkcí a tlustý klient pro Windows/Mac (Remote Desktop Manager), se kterým můžete synchronizovat a který značně rozšiřuje možnosti... připojení jedním kliknutím

  * cena není tak zlá - až 15 uživatelů stojí 500 USD ročně za password server


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Funkce on-premise verze: 

  * Úplná kontrola nad vašimi end-to-end bezpečnostními systémy a infrastrukturou

  * Nasazení softwaru ve vašem on-premise datovém centru nebo ve vaší vlastní instanci virtuálního privátního cloudu

  * Splnění zákonných a regulatorních povinností, které vyžadují, aby všechna data a systémy sídlily on premise

Funkce cloudové verze:

  * Model software jako služba vám umožňuje zaregistrovat se a začít hned

  * Elastická škálovatelnost s růstem

  * Kontroly a redundanci zajišťuje Azure s SLA dostupnosti 99,9 %

Zpětná vazba uživatelů:

  * Dříve jsme tento produkt používali. Dalo se snadno obejít a pravidla fungují jen pro chytré lidi. Líní nebo hloupí uživatelé ho v týmové oblasti snadno pokazí. Ceny jsou při jednání s nimi vyjednatelné.

  * Můžete ho provozovat pomocí SQL express a stroje s Win 7. 

  * Levný.
