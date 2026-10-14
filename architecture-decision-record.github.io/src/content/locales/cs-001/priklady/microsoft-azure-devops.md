# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: neuspokojivé dobrodružství](#microsoft-devops-ci-neuspokojivé-dobrodružství)
  * [Hlavní body diskuse na Hacker News](#hlavní-body-diskuse-na-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Shrnutí Edwarda Thomsona (Azure PM)](#shrnutí-edwarda-thomsona-azure-pm)


## Shrnutí


### Problém

Chceme používat devops k sestavování, integraci, nasazování a hostování našich projektů. Zvažujeme Microsoft Azure DevOps.

  * Chceme, aby zkušenost vývojáře byla rychlá a spolehlivá, jak při nastavení devops, např. konfiguraci, tak při průběžném používání, např. rychlé doby sestavení.
  
  * Chceme zvážit použití Microsoft Azure jako celku pro hostování aplikací projektu, databází atd.


### Rozhodnutí

Rozhodnuto proti Microsoft Azure DevOps.


### Stav

Rozhodnuto. Jsme otevřeni přehodnocení, pokud a když přijdou nové významné informace.


## Podrobnosti


### Předpoklady

Všechny obvyklé devops předpoklady, například z knihy Accelerate.

  * Rychlá sestavení jsou významnou pomocí. Zrychlují zpětnovazební smyčky.

  * Můžeme vyměňovat části od alternativních dodavatelů, tj. možná budeme chtít přinést vlastní rychlejší build servery nebo použít vlastní volbu systému správy verzí nebo koordinovat s vlastním hostovaným serverem kontinuální integrace.
  
  * Zjednodušená použitelnost je významnou pomocí pro zkušenost vývojáře a následně i pro jemné oblasti, jako je konzistence, srozumitelnost, bezpečnost a snadnost křivky učení.

  * Když je cokoli rozbité nebo problematické, chceme účinný způsob, jak problém nahlásit. To je obzvlášť důležité u jakýchkoli problémů souvisejících s bezpečností.


### Omezení

Žádná známá. Azure má zveřejněný závazek dobře spolupracovat s externími nástroji.


### Stanoviska

Zvažovali jsme použití Microsoft Azure Devops oproti AWS, které je zavedeným řešením.

Experimentovali jsme s Azure DevOps, Azure Pipelines, Azure Repo a zprovozněním nového serveru v Azure přes Terraform.

Experimentovali jsme se získáním podpory od zástupců Microsoftu.

Informace jsme sbírali od kolegů na blozích a na Hacker News.


### Argument

Azure DevOps inzeruje vynikající sadu nabídek, ale ty neobstojí, nefungují dobře dohromady a podpora je špatná.

Naše přímá zkušenost:

  * Nastavení Azure je změť UI, z nichž některá se překrývají s účty Microsoft a některá ne. Např. existuje přihlášení do Azure, přihlášení na Microsoft.com, přihlášení na Live.com atd. a všechna jsou současně ve hře.

  * Při nastavování jsme narazili na drobný bezpečnostní problém a nenašli jsme řešení. Zkoušeli jsme ho nahlásit mnoha způsoby mnoha zástupcům Microsoftu, bez úspěchu. Úspěšně jsme ho nahlásili bezpečnostnímu týmu Microsoftu, který odpověděl, že to opravovat nebude.

  * Dokumentace je často buď chybná, nebo zastaralá. Alespoň část z toho je způsobena špatným vyhledávačem Microsoftu a část podprůměrným SEO.
  
  * Nastavení Terraformu je dobře zdokumentováno a funguje. Podpora Terraformu je však ve srovnání s AWS slabá, protože Microsoft buduje obchodní vztahy s dodavateli, aby vytvářeli ukázky navazujícího nastavení přes Terraform.

Zkušenosti kolegů:

  * Poté, co jsme provedli vlastní slepé hodnocení, hledali jsme zkušenosti kolegů. To, co jsme našli, potvrdilo naše zkušenosti.

  * Kolegové uváděli další problémy s dobami sestavení a problémy s vlastním build serverem (bring-your-own). Tyto problémy jsou výrazně závažnější než problémy s UI, protože provádění sestavení je hlavním účelem build pipeline a očekáváme, že jich budeme dělat mnoho denně.

  * Našli jsme vynikající účast kolegů z Azure v diskusních oblastech. Za to patří Microsoftu uznání. Zvlášť nás zaujal Edward Thomson, PM a programátor Azure, kvůli své účasti, přímosti a technickým vysvětlením.


### Důsledky

Volba Microsoft Azure DevOps se jeví jako pravděpodobně dražší (~3x) co do času a nákladů než nevolba Azure.


## Související


### Související rozhodnutí

Pokud zvolíme Azure DevOps, existuje mnoho souvisejících nabídek, včetně Azure Repo, Azure Pipeline atd. Domníváme se, že pokud zvolíme Azure Devops, může nám to usnadnit používání dalších schopností Azure, nebo ztížit používání schopností jiných dodavatelů.

Domníváme se, že Microsoft dělá velké pokroky ve zkušenosti vývojářů, a vidíme, že Microsoft provádí velké akvizice vývojářských nástrojů (např. GitHub) a závislostí (např. Citus).

Pokud zvolíme Azure DevOps, možná budeme chtít zdůraznit volbu nabídek z akvizic Microsoftu a také se možná budeme chtít k akvizičním nabídkám stavět s větší péčí/hodnocením kvůli možnému odmítnutí tkáně, např. riziku fluktuace zaměstnanců.


### Související požadavky

Chceme, aby doby sestavení byly velmi rychlé. Jsme ochotni za to platit vysokou přirážku. Je to proto, že chceme iterovat velmi rychle.

Chceme velmi vysokou spolehlivost. Jsme ochotni za to platit vysokou přirážku. Je to proto, že testujeme případy použití s vysokou hodnotou, včetně finančních transakcí, důvěrných transakcí atd.

Naše čtyři hlavní devops KPI zahrnují střední dobu obnovy, což vyžaduje rychlá sestavení a vysokou spolehlivost.


### Související artefakty

Chceme, aby build systém vytvářel artefakty vhodné pro použití v jiných systémech, například Artifactory.


### Související principy

Snadno vratné. Azure DevOps můžeme hodnotit paralelně s zavedeným AWS.


## Poznámky


### Microsoft Devops CI: neuspokojivé dobrodružství

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Příspěvek na blogu.

„Jako softwarový vývojář z první ruky vím, jak obtížné je vytvářet kvalitní produkty rychle a levně. Je to umělecká forma, která se nám někdy daří, a jindy se zvrtne v něco podobného vládnímu zdravotnickému webu z éry Obamy. Naše míra kontroly nad výsledným produktem se liší a vina za neúspěch často padá na špatné lidi v rozhodovací hierarchii. Microsoft Azure DevOps (dříve známý jako Visual Studio Team Services) je navzdory zjevně dobrým úmyslům dokonalou bouří špatných rozhodnutí a slabého provedení.“


### Hlavní body diskuse na Hacker News

https://news.ycombinator.com/item?id=18983586

„V práci intenzivně používáme Azure DevOps a poté, co jsem používal GitHub, Gitlab, vlastní hostovaná řešení, Jenkins, TeamCity... Azure DevOps se umisťuje úplně poslední.“

„UI je všude strašně těžkopádné. Nejhorší jsou pro mě pull requesty. Neuvěřitelně těžké pracovat s lidmi na pull requestu. Ani vám nedokážu ukázat „jeden“ konkrétní problém – u nás je to rozbité všude.“

„Azure Devops je něco, co bych chtěl milovat. UI se neustále mění, ale neopravuje základní chyby, které existují už věky.“

„Nástroje nejsou dobře integrovány, UI je opravdu pomalé, neexistuje dashboard aktivních pull requestů, sestavení, vydání atd. pro mé oblíbené repozitáře. Doby sestavení/nasazení jsou šíleně pomalé.“

„Zkoušeli jsme používat i Azure Boards (Work Items, Boards, Backlogs atd.). Au. Je to naprostá změť UI nesouvisejících nápadů. Místo aby implementovali jednu věc dobře, implementovali dvacet čtyři věcí hrozně.“


### Windows Development MVP

Jsem Windows Development MVP. Cítím, že musím nést část odpovědnosti za to, že jsem o těchto problémech nemluvil hlasitěji. Ale musím říct, že jsem zklamaný, když slyším, že jste „překvapeni“ problémy s UX. Říkám vašim lidem, že UX je hrozné (např. už před spuštěním), a pořád jsem slyšel „víme, opravujeme to“. Začnu zpětnou vazbu formalizovat a protlačím ji kanály, zůstaňte naladěni. Jsem také místní (Bellevue), rád bych přišel a zkusil vytvořit pipeline pro naši poměrně jednoduchou oss aplikaci .net/wpf/uwp. Tuším, že to bude pro oba z nás oči otevírající.

Některé příklady:

* Nelze vytvořit pipeline s git repozitářem, který obsahuje submoduly

* Zjistil jsem, že je nemožné upravit PATH pro nějaké vlastní nástroje

* Zážitek z nové pipeline prostě nedává velký smysl, noví uživatelé, kteří klikají kolem, nakonec skončí u špatné dokumentace.


### Shrnutí Edwarda Thomsona (Azure PM)

Napsal jsem kód, který slučuje vaše pull requesty. Program Manager v Microsoftu pro Azure DevOps; dříve softwarový inženýr na nástrojích správy verzí v GitHubu, Microsoftu, SourceGear.

https://www.edwardthomson.com/

Spoluudržovatel libgit2. https://libgit2.github.io

Spoluhostitel All Things Git, podcastu o Gitu. https://www.allthingsgit.com/

Kurátor Developer Tools Weekly, newsletteru o vývojářských nástrojích. https://developertoolsweekly.com/
