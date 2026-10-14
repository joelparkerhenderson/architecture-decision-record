# Arkitekturbeslutningspost: API med JSON eller gRPC

## Status

Accepteret

## Kontekst

Vi designer et API til en ny service, som vil blive brugt af flere klienter. Vi har overvejet to muligheder for at implementere API'et: JSON over HTTP eller gRPC.

JSON over HTTP er en udbredt tilgang til at bygge API'er og understøttes af mange programmeringssprog og frameworks. Denne tilgang er enkel, let og nem at forstå, hvilket gør den til et godt valg til mange projekter. Den kan dog være mindre effektiv end andre muligheder, især når der skal håndteres store datamængder.

gRPC er derimod en nyere teknologi, der tilbyder en mere effektiv måde at bygge API'er på. Den bruger binær serialisering til at overføre data, hvilket kan være hurtigere og mere kompakt end JSON. gRPC understøtter også tovejs-streaming, hvilket gør det til et godt valg til realtidsapplikationer.

## Beslutning

Efter at have overvejet fordele og ulemper ved begge muligheder har vi besluttet at bruge gRPC til vores API. Selv om JSON over HTTP er en enklere mulighed, tror vi, at gRPC vil give en mere effektiv og skalerbar løsning til vores service. Vi forventer også, at vores API vil håndtere en stor mængde data, og gRPC's binære serialisering vil være mere effektiv til dette anvendelsestilfælde.

Derudover tror vi, at gRPC's understøttelse af tovejs-streaming vil være gavnlig for realtidsapplikationer, som vi måske udvikler i fremtiden.

## Konsekvenser

Ved at vælge gRPC skal vi bruge et andet sæt værktøjer og biblioteker til at bygge vores API end ved JSON over HTTP. Det kan kræve ekstra tid og indsats at lære og implementere disse teknologier. Derudover skal klienter, der vil bruge vores API, bruge gRPC-kompatible biblioteker, som måske ikke er lige så udbredt understøttet som biblioteker til JSON over HTTP.

Vi tror dog, at fordelene ved gRPC opvejer disse potentielle ulemper, og vi er overbeviste om, at denne beslutning vil resultere i et mere effektivt og skalerbart API.
