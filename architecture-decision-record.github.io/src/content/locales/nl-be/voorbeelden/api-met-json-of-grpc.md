# Architectuurbeslissingsdocument: API met JSON of gRPC

## Status

Geaccepteerd

## Context

We ontwerpen een API voor een nieuwe service die door meerdere clients zal worden gebruikt. We hebben twee opties overwogen voor de implementatie van de API: JSON over HTTP of gRPC.

JSON over HTTP is een veelgebruikte aanpak voor het bouwen van API's en wordt door veel programmeertalen en frameworks ondersteund. Deze aanpak is eenvoudig, lichtgewicht en gemakkelijk te begrijpen, waardoor het een goede keuze is voor veel projecten. Het kan echter minder efficiënt zijn dan andere opties, vooral bij het verwerken van grote hoeveelheden data.

gRPC daarentegen is een nieuwere technologie die een efficiëntere manier biedt om API's te bouwen. Het gebruikt binaire serialisatie om data over te dragen, wat sneller en compacter kan zijn dan JSON. gRPC ondersteunt ook bidirectionele streaming, waardoor het een goede keuze is voor realtimetoepassingen.

## Beslissing

Na het afwegen van de voor- en nadelen van beide opties hebben we besloten gRPC te gebruiken voor onze API. Hoewel JSON over HTTP een eenvoudiger optie is, geloven we dat gRPC een efficiëntere en schaalbaardere oplossing voor onze service zal bieden. We verwachten ook dat onze API een grote hoeveelheid data zal verwerken, en de binaire serialisatie van gRPC zal efficiënter zijn voor dit gebruiksscenario.

Daarnaast geloven we dat de ondersteuning van gRPC voor bidirectionele streaming nuttig zal zijn voor realtimetoepassingen die we in de toekomst mogelijk ontwikkelen.

## Gevolgen

Door voor gRPC te kiezen, moeten we een andere set tools en bibliotheken gebruiken om onze API te bouwen dan bij JSON over HTTP. Dit kan extra tijd en moeite kosten om deze technologieën te leren en te implementeren. Bovendien moeten clients die onze API willen gebruiken gRPC-compatibele bibliotheken gebruiken, die mogelijk niet zo breed worden ondersteund als bibliotheken voor JSON over HTTP.

We geloven echter dat de voordelen van gRPC zwaarder wegen dan deze mogelijke nadelen, en we zijn ervan overtuigd dat deze beslissing zal leiden tot een efficiëntere en schaalbaardere API.
