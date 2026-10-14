# Architectuurbeslissingsdocument: een databasetechnologie kiezen

## Status

Geaccepteerd

## Context

We ontwerpen een nieuwe applicatie die data op een schaalbare en goed presterende manier moet opslaan en ophalen. We hebben drie typen databasetechnologieën geïdentificeerd die vaak worden gebruikt: relationele databases, documentdatabases en eventdatabases.

Relationele databases slaan data op in tabellen met vaste schema's en dwingen strikte data-integriteitsbeperkingen af. Ze zijn geschikt voor applicaties die complexe datarelaties en transacties vereisen. Voorbeelden zijn MySQL, PostgreSQL en Oracle.

Documentdatabases slaan data op in JSON-achtige documenten en zijn schemaloos. Ze zijn zeer geschikt voor applicaties die flexibele datamodellen en horizontale schaling vereisen. Voorbeelden zijn MongoDB, Couchbase en Amazon DynamoDB.

Eventdatabases slaan data op als een reeks gebeurtenissen en leggen elke wijziging in de data vast. Ze zijn geschikt voor applicaties die auditing, event sourcing en complexe dataverwerking vereisen. Voorbeelden zijn Apache Kafka, Apache Pulsar en AWS Kinesis.
Beslissing

Na zorgvuldige evaluatie van de eisen en beperkingen van onze applicatie hebben we besloten een documentdatabase te gebruiken.

## Onderbouwing

We hebben een documentdatabase gekozen omdat:

1. Onze applicatie een flexibel datamodel nodig heeft dat in de loop van de tijd kan evolueren. Documentdatabases laten ons data opslaan in een schemaloos formaat, wat betekent dat we nieuwe velden kunnen toevoegen of de structuur van bestaande documenten kunnen wijzigen zonder het databaseschema aan te passen.

2. Onze applicatie horizontaal moet schalen om grote hoeveelheden data en verkeer te verwerken. Documentdatabases bieden ingebouwde ondersteuning voor sharding en replicatie, waarmee we data over meerdere servers kunnen verdelen en een hoge lees- en schrijfdoorvoer aankunnen.

3. Onze applicatie snelle en efficiënte dataopvraging vereist. Documentdatabases bieden krachtige indexerings- en querymogelijkheden waarmee we data snel en efficiënt kunnen ophalen.

4. Onze applicatie geen complexe transacties of datarelaties vereist. Hoewel relationele databases uitblinken in het afdwingen van data-integriteitsbeperkingen en het afhandelen van complexe transacties, heeft onze applicatie dergelijke eisen niet. Documentdatabases kunnen voldoende consistentie- en duurzaamheidsgaranties bieden voor ons gebruiksscenario.

## Gevolgen

Door voor een documentdatabase te kiezen, moeten we investeren in het leren en begrijpen van de specifieke technologie die we kiezen. Daarnaast moeten we ervoor zorgen dat het datamodel van onze applicatie goed past bij het datamodel van de documentdatabase om prestaties en schaalbaarheid te maximaliseren.

We geloven echter dat de voordelen van een documentdatabase zwaarder wegen dan de kosten, en dat het de beste keuze is voor de eisen en beperkingen van onze applicatie.
