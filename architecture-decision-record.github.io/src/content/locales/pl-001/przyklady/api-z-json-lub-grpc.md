# Rejestr decyzji architektonicznych: API z JSON lub gRPC

## Status

Zaakceptowany

## Kontekst

Projektujemy API dla nowej usługi, z której będzie korzystać wielu klientów. Rozważaliśmy dwie opcje implementacji API: JSON przez HTTP lub gRPC.

JSON przez HTTP to szeroko stosowane podejście do budowania API, obsługiwane przez wiele języków programowania i frameworków. Jest proste, lekkie i łatwe do zrozumienia, co czyni je dobrym wyborem dla wielu projektów. Może być jednak mniej wydajne niż inne opcje, zwłaszcza przy obsłudze dużych ilości danych.

gRPC z kolei jest nowszą technologią, która oferuje wydajniejszy sposób budowania API. Używa serializacji binarnej do przesyłania danych, która może być szybsza i bardziej zwarta niż JSON. gRPC obsługuje też dwukierunkowy streaming, co czyni je dobrym wyborem dla aplikacji czasu rzeczywistego.

## Decyzja

Po rozważeniu zalet i wad obu opcji postanowiliśmy użyć gRPC dla naszego API. Choć JSON przez HTTP jest prostszą opcją, wierzymy, że gRPC zapewni wydajniejsze i bardziej skalowalne rozwiązanie dla naszej usługi. Przewidujemy też, że nasze API będzie obsługiwać dużą ilość danych, a binarna serializacja gRPC będzie w tym zastosowaniu wydajniejsza.

Ponadto wierzymy, że obsługa dwukierunkowego streamingu w gRPC będzie korzystna dla aplikacji czasu rzeczywistego, które możemy opracować w przyszłości.

## Konsekwencje

Wybierając gRPC, będziemy musieli użyć innego zestawu narzędzi i bibliotek do zbudowania naszego API niż w przypadku JSON przez HTTP. Może to wymagać dodatkowego czasu i wysiłku na naukę i wdrożenie tych technologii. Ponadto klienci, którzy będą chcieli korzystać z naszego API, będą musieli używać bibliotek zgodnych z gRPC, które mogą być mniej powszechnie obsługiwane niż biblioteki JSON przez HTTP.

Wierzymy jednak, że korzyści z użycia gRPC przeważają nad tymi potencjalnymi wadami, i mamy pewność, że ta decyzja zaowocuje wydajniejszym i bardziej skalowalnym API.
