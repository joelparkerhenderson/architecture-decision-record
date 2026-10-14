# Záznam architektonického rozhodnutí: API s JSON nebo gRPC

## Stav

Přijaté

## Kontext

Navrhujeme API pro novou službu, kterou bude používat více klientů. Zvažovali jsme dvě možnosti implementace API: JSON přes HTTP nebo gRPC.

JSON přes HTTP je široce používaný přístup k budování API a podporuje ho mnoho programovacích jazyků a frameworků. Tento přístup je jednoduchý, lehký a snadno pochopitelný, což z něj činí dobrou volbu pro mnoho projektů. Může být však méně efektivní než jiné možnosti, zejména při zpracování velkého množství dat.

gRPC je naproti tomu novější technologie, která nabízí efektivnější způsob budování API. Pro přenos dat používá binární serializaci, která může být rychlejší a kompaktnější než JSON. gRPC také podporuje obousměrné streamování, což z něj činí dobrou volbu pro aplikace v reálném čase.

## Rozhodnutí

Po zvážení výhod a nevýhod obou možností jsme se rozhodli použít pro naše API gRPC. Přestože je JSON přes HTTP jednodušší možností, věříme, že gRPC poskytne efektivnější a škálovatelnější řešení pro naši službu. Předpokládáme také, že naše API bude zpracovávat velké množství dat a binární serializace gRPC bude pro tento případ použití efektivnější.

Kromě toho věříme, že podpora obousměrného streamování v gRPC bude přínosná pro aplikace v reálném čase, které bychom mohli v budoucnu vyvinout.

## Důsledky

Volbou gRPC budeme muset k vybudování našeho API použít jinou sadu nástrojů a knihoven než v případě JSON přes HTTP. To může vyžadovat další čas a úsilí na naučení a implementaci těchto technologií. Klienti, kteří chtějí naše API používat, navíc budou muset používat knihovny kompatibilní s gRPC, které nemusí být podporovány tak široce jako knihovny JSON přes HTTP.

Věříme však, že přínosy používání gRPC převažují nad těmito potenciálními nevýhodami, a jsme přesvědčeni, že toto rozhodnutí povede k efektivnějšímu a škálovatelnějšímu API.
