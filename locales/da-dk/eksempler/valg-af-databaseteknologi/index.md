# Arkitekturbeslutningspost: valg af databaseteknologi

## Status

Accepteret

## Kontekst

Vi designer en ny applikation, der skal gemme og hente data på en skalerbar og effektiv måde. Vi har identificeret tre typer databaseteknologier, der almindeligvis bruges: relationsdatabaser, dokumentdatabaser og hændelsesdatabaser.

Relationsdatabaser gemmer data i tabeller med faste skemaer og håndhæver strenge dataintegritetsbegrænsninger. De er egnede til applikationer, der kræver komplekse datarelationer og transaktioner. Eksempler er MySQL, PostgreSQL og Oracle.

Dokumentdatabaser gemmer data i JSON-lignende dokumenter og er skemaløse. De er velegnede til applikationer, der kræver fleksible datamodeller og horisontal skalering. Eksempler er MongoDB, Couchbase og Amazon DynamoDB.

Hændelsesdatabaser gemmer data som en række hændelser og registrerer hver ændring af dataene. De er egnede til applikationer, der kræver revision, event sourcing og kompleks databehandling. Eksempler er Apache Kafka, Apache Pulsar og AWS Kinesis.
Beslutning

Efter omhyggelig evaluering af vores applikations krav og begrænsninger har vi besluttet at bruge en dokumentdatabase.

## Begrundelse

Vi har valgt en dokumentdatabase, fordi:

1. Vores applikation kræver en fleksibel datamodel, der kan udvikle sig over tid. Dokumentdatabaser lader os gemme data i et skemaløst format, hvilket betyder, at vi kan tilføje nye felter eller ændre strukturen af eksisterende dokumenter uden at ændre databaseskemaet.

2. Vores applikation skal skalere horisontalt for at håndtere store datamængder og meget trafik. Dokumentdatabaser har indbygget understøttelse af sharding og replikering, hvilket gør det muligt at fordele data på flere servere og håndtere høj læse- og skrivegennemstrømning.

3. Vores applikation kræver hurtig og effektiv datahentning. Dokumentdatabaser tilbyder stærke indekserings- og forespørgselsfunktioner, der gør det muligt at hente data hurtigt og effektivt.

4. Vores applikation kræver ikke komplekse transaktioner eller datarelationer. Mens relationsdatabaser udmærker sig ved at håndhæve dataintegritetsbegrænsninger og håndtere komplekse transaktioner, har vores applikation ikke sådanne krav. Dokumentdatabaser kan give tilstrækkelige konsistens- og holdbarhedsgarantier til vores anvendelsestilfælde.

## Konsekvenser

Ved at vælge en dokumentdatabase skal vi investere i at lære og forstå den specifikke teknologi, vi vælger at bruge. Derudover skal vi sikre, at vores applikations datamodel passer godt til dokumentdatabasens datamodel for at maksimere ydeevne og skalerbarhed.

Vi tror dog, at fordelene ved at bruge en dokumentdatabase opvejer omkostningerne, og at det er det bedste match til vores applikations krav og begrænsninger.
