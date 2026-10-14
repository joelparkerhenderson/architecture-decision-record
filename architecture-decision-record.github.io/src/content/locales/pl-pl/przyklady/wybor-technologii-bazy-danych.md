# Rejestr decyzji architektonicznych: wybór technologii bazy danych

## Status

Zaakceptowany

## Kontekst

Projektujemy nową aplikację, która wymaga skalowalnego i wydajnego przechowywania oraz pobierania danych. Zidentyfikowaliśmy trzy powszechnie używane rodzaje technologii baz danych: relacyjne bazy danych, bazy dokumentów i bazy zdarzeń.

Relacyjne bazy danych przechowują dane w tabelach o stałych schematach i egzekwują ścisłe ograniczenia integralności danych. Nadają się do aplikacji wymagających złożonych relacji między danymi i transakcji. Przykłady to MySQL, PostgreSQL i Oracle.

Bazy dokumentów przechowują dane w dokumentach podobnych do JSON i nie mają schematu. Dobrze nadają się do aplikacji wymagających elastycznych modeli danych i skalowania poziomego. Przykłady to MongoDB, Couchbase i Amazon DynamoDB.

Bazy zdarzeń przechowują dane jako serię zdarzeń, rejestrując każdą zmianę danych. Nadają się do aplikacji wymagających audytu, event sourcingu i złożonego przetwarzania danych. Przykłady to Apache Kafka, Apache Pulsar i AWS Kinesis.

## Decyzja

Po dokładnej ocenie wymagań i ograniczeń naszej aplikacji postanowiliśmy użyć bazy dokumentów.

## Uzasadnienie

Wybraliśmy bazę dokumentów, ponieważ:

1. Nasza aplikacja wymaga elastycznego modelu danych, który może ewoluować w czasie. Bazy dokumentów pozwalają przechowywać dane w formacie bez schematu, co oznacza, że możemy dodawać nowe pola lub zmieniać strukturę istniejących dokumentów bez modyfikowania schematu bazy danych.

2. Nasza aplikacja musi skalować się poziomo, aby obsłużyć duże ilości danych i ruchu. Bazy dokumentów mają wbudowaną obsługę shardingu i replikacji, co pozwala nam rozdzielać dane na wiele serwerów i obsługiwać wysoką przepustowość odczytów i zapisów.

3. Nasza aplikacja wymaga szybkiego i efektywnego pobierania danych. Bazy dokumentów oferują potężne możliwości indeksowania i zapytań, które pozwalają nam pobierać dane szybko i efektywnie.

4. Nasza aplikacja nie wymaga złożonych transakcji ani relacji między danymi. Choć relacyjne bazy danych doskonale egzekwują ograniczenia integralności danych i obsługują złożone transakcje, nasza aplikacja nie ma takich wymagań. Bazy dokumentów mogą zapewnić wystarczające gwarancje spójności i trwałości w naszym przypadku.

## Konsekwencje

Wybierając bazę dokumentów, będziemy musieli zainwestować w naukę i zrozumienie konkretnej technologii, której użyjemy. Ponadto będziemy musieli zadbać o to, aby model danych naszej aplikacji dobrze pasował do modelu danych bazy dokumentów, aby zmaksymalizować wydajność i skalowalność.

Wierzymy jednak, że korzyści z użycia bazy dokumentów przeważają nad kosztami i że jest to najlepsze dopasowanie do wymagań i ograniczeń naszej aplikacji.
