# Architectuurbeslissingsdocument: snake_case of camelCase voor een REST-API?

Beslissing: voor REST-API-endpoints wordt de naamgevingsconventie snake_case gebruikt

Status: Geaccepteerd

## Context

Bij naamgevingsconventies voor REST-API's zijn er twee populaire formaten: snake_case en camelCase. Bij snake_case wordt elk woord in de naam gescheiden door underscores, terwijl bij camelCase het eerste woord van de naam in kleine letters staat en de volgende woorden hun eerste letter met een hoofdletter hebben. Deze beslissing bepaalt welke naamgevingsconventie voor een REST-API moet worden gebruikt.

## Beslissingsdrijfveren

- Consistentie met bestaande naamgevingsconventies in het project

- Leesbaarheid en duidelijkheid voor iedereen die aan de API werkt

- Aansluiting bij best practices uit de branche voor naamgevingsconventies van REST-API's

- Gemak van implementatie en onderhoud

## Beslissing

Voor REST-API-endpoints wordt de naamgevingsconventie snake_case gebruikt. Deze keuze wordt gedreven door de volgende factoren:

1. **Consistentie**: het project gebruikt al de naamgevingsconventie snake_case voor alle endpoints, en het is nuttig deze conventie te behouden om consistentie in het hele project te waarborgen.

2. **Leesbaarheid en duidelijkheid**: de conventie snake_case is leesbaarder en gemakkelijker te begrijpen. De underscores zorgen voor een duidelijke scheiding tussen woorden, waardoor het gemakkelijker is de betekenis van de naam te ontleden en te begrijpen.

3. **Aansluiting bij best practices uit de branche**: de conventie snake_case wordt veel gebruikt in de branche en wordt beschouwd als een best practice voor REST-API's, waardoor het een goede keuze is voor het project.

4. **Gemak van implementatie en onderhoud**: het behouden van de bestaande naamgevingsconventie is gemakkelijker te implementeren en te onderhouden, omdat alle bestaande code en documentatie zouden moeten worden bijgewerkt als een nieuwe conventie zou worden gekozen.

## Gevolgen

Deze beslissing heeft mogelijke gevolgen. 

* Als nieuwe teamleden die zich bij het project voegen niet bekend zijn met de naamgevingsconventie snake_case, kan dit leiden tot verwarring en fouten bij de ontwikkeling. Omdat snake_case echter een veelgebruikte conventie is, is dat risico minimaal. 
  
* Als in het project andere tools of frameworks worden gebruikt die sterk op de conventie camelCase zijn gebaseerd, kan extra inspanning nodig zijn om tussen naamgevingsconventies te converteren. Dat is echter geen groot punt van zorg, omdat het project is gestandaardiseerd op de conventie snake_case. 
 
Over het geheel genomen resulteert de beslissing om de naamgevingsconventie snake_case te gebruiken voor REST-API-endpoints in een consistente, leesbare aanpak die voldoet aan de branchestandaard en tegelijk gemakkelijk te implementeren en te onderhouden is.

<h6>Bronvermelding: deze pagina is gegenereerd door ChatGPT en daarna bewerkt voor duidelijkheid en opmaak.</h6>
