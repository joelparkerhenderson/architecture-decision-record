# Zapis arhitekturne odločitve: izbira podatkovne tehnologije

## Stanje

Sprejeto

## Kontekst

Oblikujemo novo aplikacijo, ki zahteva shranjevanje in pridobivanje podatkov na razširljiv in zmogljiv način. Opredelili smo tri vrste podatkovnih tehnologij, ki se običajno uporabljajo: relacijske podatkovne baze, dokumentne podatkovne baze in dogodkovne podatkovne baze.

Relacijske podatkovne baze shranjujejo podatke v tabelah s fiksnimi shemami in uveljavljajo stroge omejitve celovitosti podatkov. Primerne so za aplikacije, ki zahtevajo zapletena razmerja med podatki in transakcije. Primeri so MySQL, PostgreSQL in Oracle.

Dokumentne podatkovne baze shranjujejo podatke v dokumentih, podobnih JSON, in so brez sheme. Dobro so primerne za aplikacije, ki zahtevajo prilagodljive podatkovne modele in vodoravno skaliranje. Primeri so MongoDB, Couchbase in Amazon DynamoDB.

Dogodkovne podatkovne baze shranjujejo podatke kot zaporedje dogodkov in beležijo vsako spremembo podatkov. Primerne so za aplikacije, ki zahtevajo revidiranje, dogodkovno shranjevanje (event sourcing) in zapleteno obdelavo podatkov. Primeri so Apache Kafka, Apache Pulsar in AWS Kinesis.
Odločitev

Po skrbnem vrednotenju zahtev in omejitev naše aplikacije smo se odločili za uporabo dokumentne podatkovne baze.

## Utemeljitev

Dokumentno podatkovno bazo smo izbrali, ker:

1. Naša aplikacija zahteva prilagodljiv podatkovni model, ki se lahko sčasoma razvija. Dokumentne podatkovne baze nam omogočajo shranjevanje podatkov v obliki brez sheme, kar pomeni, da lahko dodajamo nova polja ali spreminjamo strukturo obstoječih dokumentov, ne da bi morali spreminjati shemo podatkovne baze.

2. Naša aplikacija se mora vodoravno skalirati, da obvladuje velike količine podatkov in prometa. Dokumentne podatkovne baze imajo vgrajeno podporo za razdeljevanje (sharding) in podvajanje (replication), kar nam omogoča porazdelitev podatkov na več strežnikov in obvladovanje visoke prepustnosti branja in pisanja.

3. Naša aplikacija zahteva hitro in učinkovito pridobivanje podatkov. Dokumentne podatkovne baze nudijo zmogljive zmožnosti indeksiranja in poizvedovanja, ki nam omogočajo hitro in učinkovito pridobivanje podatkov.

4. Naša aplikacija ne zahteva zapletenih transakcij ali razmerij med podatki. Čeprav so relacijske podatkovne baze odlične pri uveljavljanju omejitev celovitosti podatkov in obravnavi zapletenih transakcij, naša aplikacija takih zahtev nima. Dokumentne podatkovne baze lahko za naš primer uporabe zagotovijo zadostna jamstva doslednosti in trajnosti.

## Posledice

Z izbiro dokumentne podatkovne baze bomo morali vlagati v učenje in razumevanje posamezne tehnologije, ki jo bomo izbrali. Poleg tega bomo morali zagotoviti, da se podatkovni model naše aplikacije dobro ujema s podatkovnim modelom dokumentne podatkovne baze, da povečamo zmogljivost in razširljivost.

Vendar verjamemo, da koristi uporabe dokumentne podatkovne baze odtehtajo stroške in da je najboljša izbira glede na zahteve in omejitve naše aplikacije.
