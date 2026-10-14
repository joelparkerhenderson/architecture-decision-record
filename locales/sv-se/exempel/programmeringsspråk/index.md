# Programmeringsspråk

Innehåll:

* [Sammanfattning](#sammanfattning)
  * [Problem](#problem)
  * [Beslut](#beslut)
  * [Status](#status)
* [Detaljer](#detaljer)
  * [Antaganden](#antaganden)
  * [Begränsningar](#begränsningar)
  * [Ståndpunkter](#ståndpunkter)
  * [Argument](#argument)
  * [Implikationer](#implikationer)
* [Relaterat](#relaterat)
  * [Relaterade beslut](#relaterade-beslut)
  * [Relaterade krav](#relaterade-krav)
  * [Relaterade artefakter](#relaterade-artefakter)
  * [Relaterade principer](#relaterade-principer)
* [Anteckningar](#anteckningar)


## Sammanfattning


### Problem

Vi behöver välja programmeringsspråk för vår programvara. Vi har två huvudsakliga behov: ett frontend-programmeringsspråk som lämpar sig för webbapplikationer och ett backend-programmeringsspråk som lämpar sig för serverapplikationer.


### Beslut

Vi väljer TypeScript för frontend.

Vi väljer Rust för backend.


### Status

Beslutat. Vi är öppna för nya alternativ när de dyker upp.


## Detaljer


### Antaganden

Frontend-applikationerna är typiska:

  * Typiska användare och interaktioner

  * Typiska webbläsare och system

  * Typisk utveckling och driftsättning

Frontend-applikationerna kommer sannolikt att utvecklas snabbt:

  * Vi vill säkerställa snabb, enkel utveckling, driftsättning, iteration osv.

  * Vi värdesätter bevisbarhet, till exempel typsäkerhet, och vi är nöjda med att göra lite mer arbete för att uppnå den.

  * Vi behöver ingen äldre kompatibilitet.

Backend-applikationerna ligger över det typiska:

  * Mål som ligger över det typiska för kvalitet, särskilt bevisbarhet, tillförlitlighet, säkerhet osv.

  * Mål som ligger över det typiska för nära realtid, dvs. vi vill inte ha pauser på grund av skräpinsamling i virtuella maskiner.

  * Mål som ligger över det typiska för funktionell programmering, särskilt för parallellisering, flerkärnig bearbetning och minnessäkerhet.

Vi accepterar lägre kompileringshastigheter till förmån för säkerhet vid kompilering och hastighet vid körning.


### Begränsningar

Vi har en stark begränsning avseende språk som kan användas med stora molnleverantörers funktionstjänster, till exempel Amazon Lambda.


### Ståndpunkter

Vi övervägde dessa språk:

  * C

  * C++

  * Clojure
  
  * Elixir
  
  * Erlang
  
  * Elm
  
  * Flow
  
  * Go
  
  * Haskell
  
  * Java
  
  * JavaScript
  
  * Kotlin
  
  * Python
  
  * Ruby
  
  * Rust
  
  * TypeScript



### Argument

Sammanfattning per språk:

  * C: avvisat på grund av låg säkerhet; Rust kan göra nästan allt bättre.

  * C++: avvisat eftersom det är ett kaos; Rust kan göra nästan allt bättre.

  * Clojure: utmärkt modellering; bästa Lisp-approximationen; stor körtidsmiljö på JVM.
  
  * Elixir: utmärkt körtidsmiljö inklusive driftsättningsbarhet och samtidighet; utmärkt utvecklarupplevelse; relativt litet ekosystem.

  * Erlang: utmärkt körtidsmiljö inklusive driftsättningsbarhet och samtidighet; utmanande utvecklarupplevelse; relativt litet ekosystem.

  * Elm: ser mycket lovande ut; IBM publicerar stora fallstudier med goda resultat; mindre ekosystem.

  * Flow: intressant förbättring jämfört med JavaScript; utvecklare rör sig dock bort från det.

  * Go: utmärkt utvecklarupplevelse; utmärkt samtidighet; men en historik av dåliga beslut som lamslår språket.

  * Haskell: bästa funktionella språket; mindre utvecklargemenskap; har inte uppnått tillräckligt många publicerade produktionsframgångar.

  * Java: utmärkt körtidsmiljö; utmärkt ekosystem; undermålig utvecklarupplevelse.

  * JavaScript: det mest populära språket någonsin; mest utbredda ekosystemet.

  * Kotlin: fixar så mycket av Java; utmärkt stöd från JetBrains; goda publicerade fall av portning från Java till Kotlin.
  
  * Python: mest populära språket för systemadministration; bra analysverktyg; bra webbramverk; men övergivet av Google till förmån för Go.

  * Ruby: bästa utvecklarupplevelsen någonsin; bästa webbramverken; trevligaste gemenskapen; men mycket långsamt; något svårt att paketera.

  * Rust: bästa nya språket; betoning på noll-abstraktion; betoning på samtidighet; dock relativt litet ekosystem; och har medvetna begränsningar för vissa typer av kompilatoraccelerationer, t.ex. måste direkt minnesåtkomst uttryckligen vara osäker (unsafe).

  * TypeScript: lägger till typer i JavaScript; bra transpilerare; växande fokus hos utvecklare på att portera från JavaScript till TypeScript; starkt stöd från Microsoft.

Vi beslutade att virtuella maskiner har en uppsättning avvägningar som vi inte behöver just nu, till exempel ytterligare komplexitet som ger körtidsförmågor.

Vi tror att vårt kärnbeslut drivs av två tvärgående hänsyn:

  * För snabbaste körtidshastighet och tätaste systemåtkomst skulle vi välja JavaScript och C.

  * För närmast snabbaste körtidshastighet och närmast tätaste systemåtkomst väljer vi TypeScript och Rust.

Hedersomnämnanden går till de VM-språk och webbramverk som vi skulle välja om vi ville ha ett VM-språk:

  * Clojure och Luminus

  * Java och Spring

  * Elixir och Phoenix


### Implikationer

Frontend-utvecklare kommer att behöva lära sig TypeScript. Det är sannolikt en lätt inlärningskurva om utvecklarens huvudsakliga erfarenhet är att använda JavaScript.

Backend-utvecklare kommer att behöva lära sig Rust. Det är sannolikt en måttlig inlärningskurva om utvecklarens huvudsakliga erfarenhet är att använda C/C++, och en svår inlärningskurva om utvecklarens huvudsakliga erfarenhet är att använda Java, Python, Ruby eller liknande minneshanterade språk. 

TypeScript och Rust är båda relativt nya. Det innebär att många verktyg ännu inte har dokumentation för dessa språk. Till exempel måste devops-pipelinen ställas in för dessa språk, och hittills har inget av de devops-verktyg vi utvärderar standardexempel för dessa språk.

Kompileringstiderna för TypeScript och Rust är ganska långsamma. En del av detta kan bero på att språken är nya. Vi kan behöva titta på hur vi kan mildra långsamma kompileringstider, till exempel genom kompilering på begäran, kompileringssamtidighet osv.

IDE-stödet för dessa språk är ännu inte allestädes närvarande och ännu inte förstklassigt. Till exempel säljer JetBrains IDE:n PyCharm för förstklassigt stöd för Python, men säljer ingen IDE med förstklassigt stöd för Rust; i stället kan JetBrains använda en Rust-insticksmodul som ger kanske 80 % av Rust-språkstödet jämfört med Python-språkstödet.


## Relaterat


### Relaterade beslut

Vi kommer att sträva efter ekosystemval som stämmer överens med dessa språk.

Till exempel vill vi välja en IDE som har goda förmågor för dessa språk.

Till exempel kommer vi för vårt webbramverk för frontend sannolikt att besluta oss för ett ramverk som tenderar att sikta mot TypeScript (t.ex. Vue) snarare än ett ramverk som tenderar att sikta mot ren JavaScript (t.ex. React).


### Relaterade krav

Vår hela verktygskedja måste stödja dessa språk.


### Relaterade artefakter

Vi förväntar oss att vi kan exportera vissa hemligheter till miljövariabler.


### Relaterade principer

Mät två gånger, bygg en gång. Vi prioriterar viss säkerhet framför viss hastighet.

Körtid är mer värdefull än kompileringstid. Vi prioriterar kundernas användning framför utvecklarnas användning.


## Anteckningar

Eventuella anteckningar här.
