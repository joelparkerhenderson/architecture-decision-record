# Architecture Decision Record: API mit JSON oder gRPC

## Status

Angenommen

## Kontext

Wir entwerfen eine API für einen neuen Dienst, der von mehreren Clients genutzt werden soll. Wir haben zwei Optionen zur Implementierung der API erwogen: JSON über HTTP oder gRPC.

JSON über HTTP ist ein weit verbreiteter Ansatz zum Aufbau von APIs und wird von vielen Programmiersprachen und Frameworks unterstützt. Dieser Ansatz ist einfach, leichtgewichtig und leicht verständlich, was ihn für viele Projekte zu einer guten Wahl macht. Er kann jedoch weniger effizient sein als andere Optionen, besonders bei der Verarbeitung großer Datenmengen.

gRPC dagegen ist eine neuere Technologie, die eine effizientere Möglichkeit zum Aufbau von APIs bietet. Es nutzt binäre Serialisierung zur Datenübertragung, die schneller und kompakter sein kann als JSON. gRPC unterstützt außerdem bidirektionales Streaming, was es zu einer guten Wahl für Echtzeitanwendungen macht.

## Entscheidung

Nach Abwägung der Vor- und Nachteile beider Optionen haben wir beschlossen, gRPC für unsere API zu verwenden. Obwohl JSON über HTTP die einfachere Option ist, glauben wir, dass gRPC eine effizientere und skalierbarere Lösung für unseren Dienst bietet. Wir rechnen außerdem damit, dass unsere API eine große Datenmenge verarbeiten wird, und die binäre Serialisierung von gRPC wird für diesen Anwendungsfall effizienter sein.

Zudem glauben wir, dass die Unterstützung von bidirektionalem Streaming durch gRPC für Echtzeitanwendungen, die wir künftig entwickeln könnten, von Vorteil sein wird.

## Konsequenzen

Durch die Wahl von gRPC müssen wir zum Aufbau unserer API andere Werkzeuge und Bibliotheken verwenden als bei JSON über HTTP. Dies kann zusätzliche Zeit und Mühe erfordern, um diese Technologien zu erlernen und zu implementieren. Außerdem müssen Clients, die unsere API nutzen möchten, gRPC-kompatible Bibliotheken verwenden, die möglicherweise nicht so weit verbreitet unterstützt werden wie Bibliotheken für JSON über HTTP.

Wir sind jedoch überzeugt, dass die Vorteile von gRPC diese möglichen Nachteile überwiegen, und wir sind zuversichtlich, dass diese Entscheidung zu einer effizienteren und skalierbareren API führen wird.
