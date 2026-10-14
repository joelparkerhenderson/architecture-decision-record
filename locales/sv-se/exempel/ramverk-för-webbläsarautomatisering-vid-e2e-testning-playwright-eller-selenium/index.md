## Arkitekturbeslutspost: ramverk för webbläsarautomatisering vid E2E-testning (Playwright eller Selenium)

### 1. **Sammanhang**

Vi är i färd med att välja ett ramverk för webbläsarautomatisering för vår pipeline för end-to-end-testning (E2E). Det här ramverket kommer att vara en integrerad del av våra CI/CD-processer och köra tester som simulerar verkliga användarinteraktioner på vår plattform. Mer specifikt kommer testerna att täcka scenarier som användarregistrering/inloggning, filuppladdningar, instrumentpanelsinteraktioner och nedladdning av rapporter.

Som en **startup** ligger vårt fokus på **agil utveckling**, med ett behov av att snabbt iterera och utvecklas. Vårt team arbetar huvudsakligen med **TypeScript** och **Python**, och förmågan att skriva tester i dessa språk är avgörande. Dessutom innehåller plattformen **interaktiva diagram och instrumentpaneler**, vilket gör det kritiskt att automatiseringsverktyget stöder rika, dynamiska UI:n väl.

De två kandidaterna för den här uppgiften är **Playwright** och **Selenium**, var och en med sina styrkor och avvägningar. Vi behöver utvärdera dessa ramverk utifrån funktionerna och kraven som beskrivs nedan.

### 2. **Övervägda alternativ**

- **Playwright** (av Microsoft)
- **Selenium** (av Selenium Project)

### 3. **Beslutsdrivkrafter**

Faktorerna som påverkar vårt beslut är följande:

1. **Agil utveckling**: Det valda verktyget måste möjliggöra snabba, flexibla utvecklingscykler.
2. **Språkstöd**: Vårt team kräver stöd för både **TypeScript** och **Python**.
3. **Testning av interaktiva UI:n**: Förmågan att tillförlitligt testa interaktiva diagram, instrumentpaneler och dynamiska element är avgörande.
4. **Körtidshastighet**: Även om det inte är en huvudsaklig oro är prestanda i CI/CD-pipelines ett övervägande.
5. **Skalbarhet**: Vi planerar inte massiv skalning inom den närmaste framtiden, men vi vill säkerställa att lösningen kan hantera framtida tillväxt.
6. **Bakåtkompatibilitet**: Äldre system och kompatibilitet med äldre webbläsare är inte kritiska för vårt projekt just nu.
7. **Mobiltestning**: Även om det inte är ett omedelbart fokus bör ramverket kunna testa mobilresponsiva funktioner eller vara utökningsbart för sådana användningsfall.
8. **Testning med flera skärmar**: Stöd för konfigurationer med flera skärmar är ett sekundärt krav, särskilt om vi någon gång skalar upp till att testa mer komplexa användararbetsflöden.
9. **Testning av filuppladdning**: Ramverket måste hantera filuppladdningar effektivt, ett kärnkrav i våra testbehov.

### 4. **Utvärderingskriterier**

- **Användarvänlighet**: Hur enkelt är det att skriva och underhålla tester?
- **Språkstöd**: Stöder ramverket TypeScript och Python, de två språk som vårt team använder oftast?
- **Testning av interaktiva UI:n**: Hur väl hanterar ramverket komplexa, interaktiva användargränssnitt som diagram, filuppladdningar och dynamisk data?
- **CI/CD-integration**: Hur väl integreras ramverket i vanliga CI/CD-verktyg och -tjänster?
- **Stöd för flera webbläsare**: Vilka webbläsare stöds och hur väl presterar de?
- **Prestanda och hastighet**: Hur snabbt körs testerna, särskilt i en CI/CD-pipeline?
- **Skalbarhet**: Hur väl kan ramverket skalas om fler tester eller mer komplexa scenarier läggs till?
- **Gemenskap och ekosystem**: Hur aktiv är ramverkets gemenskap? Finns det gott om integrationer och tillägg?

### 5. **Överväganden**

#### 5.1 **Playwright**

##### **Fördelar**:
1. **Smartare API för uppladdning av lokala filer**: Playwrights API för att interagera med lokala filer och utföra filuppladdningar är enklare och mer intuitivt. Det skulle göra tester av filuppladdning enklare att implementera och underhålla.
2. **Syntax och kodgenerering**: Playwright har en kortare, mer koncis syntax. Det ger mindre standardkod, vilket förbättrar underhållbarheten och utvecklarnas effektivitet. Dessutom förbättrar den kortare syntaxen kvaliteten på OpenAIs kodgenerering, vilket gör det enklare att automatiskt generera testskript.
3. **Testning av interaktiva UI:n**: Playwright utmärker sig i att testa dynamiska, interaktiva webbapplikationer, till exempel sådana med rika diagram, komplexa användarinteraktioner och realtidsuppdateringar. Det hanterar WebSockets, WebRTC, shadow DOM och andra moderna webbtekniker mycket effektivt.
4. **Stöd för flera webbläsare**: Playwright stöder **Chromium**, **WebKit** och **Firefox**. Det har konsekvent prestanda över dessa webbläsare, vilket bör täcka de flesta av våra testbehov.
5. **CI/CD-integration**: Playwright integreras sömlöst med moderna CI/CD-plattformar (GitHub Actions, Jenkins osv.). Det kan köra tester parallellt över olika webbläsare, vilket optimerar testkörningstiderna och gör det lämpligt för snabb utveckling.
6. **Snabbt och pålitligt**: Playwright är generellt snabbare än Selenium, särskilt i headless-läge, och mer motståndskraftigt när det gäller asynkrona webbelement.

##### **Nackdelar**:
1. **Begränsad mobiltestning**: Även om Playwright stöder mobilemulering för webbläsare saknar det inbyggda mobiltestmöjligheter som Seleniums integration med Appium för äkta mobiltestning.
2. **Mindre ekosystem**: Playwright är fortfarande nyare och mindre etablerat än Selenium. Även om det har en snabbt växande gemenskap och bra dokumentation har det kanske ännu inte det stora ekosystem av insticksmoduler och integrationer som Selenium erbjuder.
3. **Begränsat webbläsarstöd**: Även om Playwright täcker de stora moderna webbläsarna (Chrome, Safari, Firefox) är dess stöd för äldre webbläsare (t.ex. Internet Explorer) inte lika robust som Seleniums.

#### 5.2 **Selenium**

##### **Fördelar**:
1. **Längre historia och mognad**: Selenium har funnits länge och har en beprövad meritlista. Det används brett av många team och branscher, vilket har lett till ett stort ekosystem av insticksmoduler, integrationer och resurser.
2. **Stöd för flera webbläsare och plattformar**: Selenium stöder ett **brett utbud av webbläsare** och versioner, inklusive **Internet Explorer**, och kan också integreras med olika verktyg som **Docker**, **Selenium Grid** och **molntjänster** för distribuerad testning.
3. **Mobiltestning**: Selenium är, genom sin integration med **Appium**, mycket mer robust för mobiltestning, inklusive både Android- och iOS-applikationer. Det gör det till det bättre valet för projekt med mobile-first- eller tungt mobilt fokus.
4. **Testning med flera skärmar**: Selenium ger bättre stöd för scenarier med **flera skärmar** eller komplexa interaktioner i flera fönster.

##### **Nackdelar**:
1. **Komplexitet**: Seleniums API är mer mångordigt och explicit. Även om det i vissa fall kan vara en fördel innebär det mer kod att skriva och underhålla, vilket kan minska utvecklarnas smidighet – särskilt viktigt i en startupmiljö.
2. **Prestanda**: Selenium körs generellt långsammare än Playwright, särskilt i headless-läge. Det kan påverka CI/CD-pipelines, särskilt när antalet tester växer.
3. **Testning av interaktiva UI:n**: Selenium är inte lika smidigt som Playwright när det gäller att testa moderna, interaktiva webb-UI:n, särskilt med diagram och realtidsdatauppdateringar. Det kräver mer konfiguration och hantering för att tillförlitligt interagera med dynamiskt innehåll.

### 6. **Jämförelsesammanfattning**

| Funktion                          | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Användarvänlighet**                   | Kortare syntax, mer intuitivt för moderna UI:n | Mer explicit, kräver mer standardkod  |
| **Språkstöd**              | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Testning av interaktiva UI:n**        | Utmärkt för dynamiska realtids-UI:n          | Hanterar grundläggande UI:n, men mer mångordigt och komplext för rika interaktioner |
| **Testning av filuppladdning**           | Smartare API för filuppladdningar                  | Mer mångordigt, mindre intuitivt API         |
| **CI/CD-integration**             | Enkel integration med GitHub Actions, Jenkins | Stark integration med många CI-verktyg    |
| **Mobiltestning**                | Begränsad, endast emulering                       | Fullt stöd via Appium               |
| **Stöd för flera webbläsare**         | Chromium, WebKit, Firefox                     | Fullt stöd över stora och äldre webbläsare |
| **Prestanda**                   | Snabbt, optimerat för headless-testning          | Långsammare, särskilt i headless-läge       |
| **Testning med flera skärmar**         | Begränsat                                       | Bra stöd för uppsättningar med flera skärmar    |
| **Gemenskap och ekosystem**       | Växande, bra dokumentation                   | Stort, moget, omfattande ekosystem       |

### 7. **Beslut**

Efter att ha övervägt kraven och avvägningarna är **Playwright** det bättre valet för våra nuvarande behov. Dess smartare API för testning av uppladdning av lokala filer, koncisa syntax och starka stöd för testning av interaktiva UI:n gör det till en idealisk passning för vår agila utvecklingscykel. Det faktum att det stöder både **TypeScript** och **Python** är avgörande för vårt team, och ramverkets moderna ansats till testning gör att vi kan skriva ren, underhållbar kod.

Även om **Selenium** förblir ett utmärkt verktyg, särskilt för mobiltestning, stöd för äldre webbläsare och uppsättningar med flera skärmar, är det mindre väl lämpat för våra nuvarande behov. Dess mångordighet, långsammare prestanda och mer komplexa hantering av dynamiska UI:n som diagram gör det mindre optimalt för vårt användningsfall.

### 8. **Konsekvenser**

- **Omedelbar åtgärd**: Vi kommer att anta **Playwright** för vår E2E-testning, med fokus på att testa användarflöden som involverar registrering, inloggning, filuppladdningar, instrumentpaneler och nedladdning av rapporter.
- **Långsiktiga överväganden**: Vi kommer att hålla ett öga på Playwrights utvecklande ekosystem. Om våra behov förändras, särskilt kring mobiltestning eller stöd för äldre webbläsare, kan vi ompröva Selenium.
- **Utbildning och dokumentation**: Utvecklingsteamen kommer att behöva bekanta sig med Playwrights API, särskilt för att hantera dynamiska UI:n och filuppladdningar.
- **Migrering**: Befintliga Selenium-tester (om några) kommer gradvis att migreras till Playwright.

### 9. **Framtida överväganden**
