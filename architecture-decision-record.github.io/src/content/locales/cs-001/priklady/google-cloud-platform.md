# Záznam architektonického rozhodnutí pro Google Cloud Platform

## Kontext

Google Cloud Platform (GCP) je významná platforma cloudového počítání, která nabízí různé cloudové služby, včetně výpočetních, úložných a síťových řešení. Cílem tohoto ADR je zdokumentovat architektonická rozhodnutí učiněná pro vývoj a implementaci infrastruktury založené na GCP pro naši organizaci.

## Rozhodnutí

Naše organizace se rozhodla používat Google Cloud Platform jako cloudovou infrastrukturu pro naši aplikaci. Hlavní úvahy pro toto rozhodnutí jsou:

   - Nákladová efektivita

   - Škálovatelnost

   - Spolehlivost

   - Flexibilita

## Výběry

K naplnění našich požadavků byly vybrány následující služby GCP:

   - Compute Engine pro virtuální stroje a výpočetní zdroje

   - Cloud Storage pro objektové úložiště a hostování souborů

   - Cloud SQL pro spravovanou databázovou službu

   - Firebase pro vývoj a hostování aplikací

## Odůvodnění

   - Nákladová efektivita: Google Cloud Platform je ve srovnání s jinými cloudovými platformami velmi nákladově efektivní, což z ní činí atraktivní možnost pro organizace s rozpočtovými omezeními.

   - Škálovatelnost: Snadno škálovatelná infrastruktura GCP umožňuje zvládnout jakékoli množství provozu v reálném čase.

   - Spolehlivost: Spravované služby GCP nabízejí vysokou spolehlivost s automatickými zálohami a schopnostmi obnovy po havárii, které zajišťují vysokou dostupnost zdrojů a dat.

   - Flexibilita: Platforma poskytuje různé nástroje a služby napříč různými doménami, jako je AI, analýza dat a IoT, což ji činí vysoce univerzální.

## Důsledky

Migrace na Google Cloud Platform bude vyžadovat školení našich týmů v oblasti služeb GCP, přepracování aplikace tak, aby byla kompatibilní s vybranými službami, a aktualizaci kódu infrastruktury pro podporu služeb GCP. Očekává se však, že po dokončení migrace budeme mít vysoce škálovatelnou, spolehlivou a nákladově efektivní infrastrukturu pro hostování naší aplikace. Budeme také muset řídit průběžné náklady na poskytování zdrojů v GCP.

## Závěr

Google Cloud Platform je výbornou volbou pro naši cloudovou infrastrukturu díky své nákladové efektivitě, škálovatelnosti, spolehlivosti a flexibilitě. Využitím vybraných služeb můžeme poskytnout vysoce dostupnou a robustní infrastrukturu pro naši aplikaci.
