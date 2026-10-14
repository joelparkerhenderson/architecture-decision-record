# Záznam architektonického rozhodnutia pre Google Cloud Platform

## Kontext

Google Cloud Platform (GCP) je významná platforma cloudového počítačstva, ktorá ponúka rôzne cloudové služby vrátane riešení pre výpočty, úložisko a siete. Tento ADR má za cieľ zdokumentovať architektonické rozhodnutia prijaté pre vývoj a implementáciu infraštruktúry založenej na GCP pre našu organizáciu.

## Rozhodnutie

Naša organizácia sa rozhodla použiť Google Cloud Platform ako cloudovú infraštruktúru pre našu aplikáciu. Primárne zváženia pre toto rozhodnutie sú:

   - Nákladová efektívnosť

   - Škálovateľnosť

   - Spoľahlivosť

   - Flexibilita

## Voľby

Na splnenie našich požiadaviek boli vybrané tieto služby z GCP:

   - Compute Engine pre virtuálne stroje a výpočtové zdroje

   - Cloud Storage pre objektové úložisko a hosting súborov

   - Cloud SQL pre spravovanú databázovú službu

   - Firebase pre vývoj a hosting aplikácií

## Zdôvodnenie

   - Nákladová efektívnosť: Google Cloud Platform je vysoko nákladovo efektívna v porovnaní s inými cloudovými platformami, čo z nej robí atraktívnu možnosť pre organizácie s rozpočtovými obmedzeniami.

   - Škálovateľnosť: Ľahko škálovateľná infraštruktúra GCP umožňuje spracovať ľubovoľné množstvo prevádzky v reálnom čase.

   - Spoľahlivosť: Spravované služby GCP ponúkajú vysokú spoľahlivosť s automatizovanými zálohami a schopnosťami obnovy po havárii, ktoré zaisťujú vysokú dostupnosť zdrojov a dát.

   - Flexibilita: Platforma poskytuje rôzne nástroje a služby v rôznych doménach ako AI, analytika dát a IoT, vďaka čomu je vysoko univerzálna.

## Dôsledky

Migrácia na Google Cloud Platform si bude vyžadovať školenie našich tímov o službách GCP, prearchitektúrovanie aplikácie tak, aby bola kompatibilná s vybranými službami, a aktualizáciu kódu infraštruktúry na podporu služieb GCP. Očakáva sa však, že po dokončení migrácie budeme mať vysoko škálovateľnú, spoľahlivú a nákladovo efektívnu infraštruktúru na hosting našej aplikácie. Budeme tiež musieť spravovať priebežné náklady na zabezpečenie zdrojov v GCP.

## Záver

Google Cloud Platform je výborná voľba pre našu cloudovú infraštruktúru vďaka svojej nákladovej efektívnosti, škálovateľnosti, spoľahlivosti a flexibilite. Využitím vybraných služieb môžeme poskytnúť vysoko dostupnú a robustnú infraštruktúru pre našu aplikáciu.