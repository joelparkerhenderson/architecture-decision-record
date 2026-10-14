# Kriterier för hållbara beslut

<https://www.infoq.com/articles/sustainable-architectural-design-decisions/>

För att definiera beslutens hållbarhet i detalj har vi härlett fem nyckelkriterier.

## Strategiskt

Vid beslutsfattande bör den som tittar på strategiska konsekvenser beakta saker som beslutens långsiktiga inverkan, till exempel framtida drifts- och underhållsinsatser.

## Mätbart och hanterbart

Du kan mäta och utvärdera ett besluts utfall över tid utifrån objektiva kriterier, helst numeriska sådana (som till exempel förespråkas av kvalitetsattributscenarier och workshops4). Det är inte möjligt att fånga alla finkorniga beslut, så arkitekter måste begränsa beslutens granularitet till en viss detaljnivå (som att skapa en designklass). Detta leder till en mer hållbar uppsättning beslut och färre spårbarhetslänkar. Dessutom minskar en begränsning av antalet beroenden mellan beslut ringeffekten av förändringar.

## Uppnåeligt och realistiskt

Motiveringen för att anpassa lösningen till problemet bör väljas pragmatiskt och göras explicit. Arkitekter kan till exempel ange att de har tagit hänsyn till att undvika över- eller underdimensionering (det vill säga att de bör tillämpa ansatsen ”tillräckligt bra”).

## Förankrat i krav

Beslutsfattandet bör grundas i domänspecifik arkitekturerfarenhet och kontext. Det bör beakta företagets miljö samt projektets krav och begränsningar, inklusive utvecklingsteamets nuvarande färdigheter, utbildningsbudget och process.

## Tidlöst

Beslut bör bygga på erfarenhet och kunskap som sannolikt inte snart blir föråldrad. Arkitekter kan till exempel välja plattformsneutrala arkitekturmönster eller taktiker.
