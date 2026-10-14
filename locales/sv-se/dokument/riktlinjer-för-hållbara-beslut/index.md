# Riktlinjer för hållbara beslut

<https://www.infoq.com/articles/sustainable-architectural-design-decisions/>

Vi drog följande lärdomar i vårt arbete som kan fungera som riktlinjer och bedömning för att uppnå hållbara beslut:

1. Använd ett slimmat/minimalistiskt tillvägagångssätt för den inledande beslutsdokumentationen.

2. Prioritera och fånga alla viktiga beslut som är tillräckligt relevanta för att dokumentera och förstå målarkitekturen.

3. Detaljera de särskilt viktiga besluten med fullfjädrade mallar först efter att det inledande arbetet är gjort (det vill säga när beslutsfattarna är nöjda med de arkitekturbeslut som fattats och säkra på att besluten inte behöver ses över inom kort).

4. Använd de slimmade/minimalistiska versionerna från steg 1 som en kortversion av dokumenterade beslut med rätt granularitetsnivå för att ge en överblick över de detaljerade besluten, samt för triviala eller självklara beslut.

5. Använd om möjligt befintlig arkitekturkunskap, antingen från vägledningsmodeller eller från andra källor. Granska och utöka sådan kunskap och anpassa den till det specifika beslutets sammanhang.

6. Se till att spårbarhetslänkar upprättas mellan beslut och både krav och arkitekturdesigner/kod. 

7. Tillhandahåll automatiserad konsekvenskontroll för att säkerställa att spårbarhetslänkarna är synkroniserade efter en ändring. Begränsa antalet beroenden mellan beslut och andra programvaruartefakter.

8. Tillämpa riktlinjerna för motiveringar konsekvent och kraftfullt – de är den viktigaste delen av beslutsdokumentationen eftersom de ger skälen.
