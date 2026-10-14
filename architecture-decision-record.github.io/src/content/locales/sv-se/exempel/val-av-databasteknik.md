# Arkitekturbeslutspost: Val av databasteknik

## Tillstånd

Godkänd

## Sammanhang

Vi utformar en ny applikation som behöver lagra och hämta data på ett skalbart och högpresterande sätt. Vi har identifierat tre typer av databastekniker som ofta används: relationsdatabaser, dokumentdatabaser och händelsedatabaser.

Relationsdatabaser lagrar data i tabeller med fasta scheman och tillämpar strikta begränsningar för dataintegritet. De lämpar sig för applikationer som kräver komplexa datarelationer och transaktioner. Exempel är MySQL, PostgreSQL och Oracle.

Dokumentdatabaser lagrar data i JSON-liknande dokument och är schemalösa. De passar väl för applikationer som kräver flexibla datamodeller och horisontell skalning. Exempel är MongoDB, Couchbase och Amazon DynamoDB.

Händelsedatabaser lagrar data som en serie händelser och fångar varje ändring av datan. De lämpar sig för applikationer som kräver granskning, event sourcing och komplex databehandling. Exempel är Apache Kafka, Apache Pulsar och AWS Kinesis.
Beslut

Efter noggrann utvärdering av vår applikations krav och begränsningar har vi beslutat att använda en dokumentdatabas.

## Motivering

Vi har valt en dokumentdatabas eftersom:

1. Vår applikation kräver en flexibel datamodell som kan utvecklas över tid. Dokumentdatabaser låter oss lagra data i ett schemalöst format, vilket innebär att vi kan lägga till nya fält eller ändra strukturen på befintliga dokument utan att behöva ändra databasschemat.

2. Vår applikation behöver skalas horisontellt för att hantera stora datamängder och stor trafik. Dokumentdatabaser har inbyggt stöd för sharding och replikering, vilket gör att vi kan distribuera data över flera servrar och hantera hög läs- och skrivgenomströmning.

3. Vår applikation kräver snabb och effektiv datahämtning. Dokumentdatabaser erbjuder kraftfull indexering och frågefunktionalitet som gör att vi kan hämta data snabbt och effektivt.

4. Vår applikation kräver inte komplexa transaktioner eller datarelationer. Medan relationsdatabaser utmärker sig i att upprätthålla begränsningar för dataintegritet och hantera komplexa transaktioner har vår applikation inte sådana krav. Dokumentdatabaser kan ge tillräckliga garantier för konsekvens och hållbarhet för vårt användningsfall.

## Konsekvenser

Genom att välja en dokumentdatabas kommer vi att behöva investera i att lära oss och förstå den specifika teknik vi väljer att använda. Dessutom måste vi säkerställa att vår applikations datamodell passar väl med dokumentdatabasens datamodell för att maximera prestanda och skalbarhet.

Vi tror dock att fördelarna med att använda en dokumentdatabas överväger kostnaderna och att den är den bästa passningen för vår applikations krav och begränsningar.
