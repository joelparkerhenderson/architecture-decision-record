# Architektur-Decisiounsopzeechnung: Wiel vun enger Datebank-Technologie

## Zoustand

Akzeptéiert

## Kontext

Mir designen eng nei Applikatioun, déi Daten op eng skaléierbar a performant Manéier muss späicheren an ofruffen. Mir hunn dräi Zorte vun Datebank-Technologie identifizéiert, déi allgemeng benotzt ginn: relationell Datebanken, Dokument-Datebanken an Event-Datebanken.

Relationell Datebanke späichere Daten an Tabellen mat fixe Schemaen an erzwéngen strikt Restriktioune fir d'Dateintegritéit. Si si gëeegent fir Applikatiounen, déi komplex Datebezéiungen an Transaktioune brauchen. Beispiller sinn MySQL, PostgreSQL an Oracle.

Dokument-Datebanke späichere Daten a JSON-ähnlechen Dokumenter a si schemalos. Si si gutt gëeegent fir Applikatiounen, déi flexibel Datemodeller an horizontal Skaléierung brauchen. Beispiller sinn MongoDB, Couchbase an Amazon DynamoDB.

Event-Datebanke späichere Daten als Rei vun Evenementer a erfaasse all Ännerung vun den Daten. Si si gëeegent fir Applikatiounen, déi Auditing, Event Sourcing a komplex Dateveraarbechtung brauchen. Beispiller sinn Apache Kafka, Apache Pulsar an AWS Kinesis.
Decisioun

Nodeems mir d'Ufuerderungen a Restriktioune vun eiser Applikatioun suergfälteg evaluéiert hunn, hu mir decidéiert, eng Dokument-Datebank ze benotzen.

## Begrënnung

Mir hunn eng Dokument-Datebank gewielt, well:

1. Eis Applikatioun brauch e flexiblen Datemodell, deen sech mat der Zäit ka weiderentwéckelen. Dokument-Datebanke loossen eis Daten an engem schemalose Format späichere, wat heescht, datt mir nei Felder derbäifügen oder d'Struktur vu bestoenden Dokumenter änneren kënnen, ouni dat Datebankschema ze ännere mussen.

2. Eis Applikatioun muss horizontal skaléieren, fir grouss Volumen u Daten a Verkéier ze handhaben. Dokument-Datebanke bidden agebaut Ënnerstëtzung fir Sharding a Replikatioun, wat et eis erméiglecht, Daten iwwer méi Server ze verdeelen an en héijen Duerchsatz bei Liesen a Schreiwe ze handhaben.

3. Eis Applikatioun brauch séier an effizient Dateofruff. Dokument-Datebanke bidden mächteg Indexéierungs- an Ofroumméiglechkeeten, déi et eis erlaben, Daten séier an effizient ofzeruffen.

4. Eis Applikatioun brauch keng komplex Transaktiounen oder Datebezéiungen. Och wann relationell Datebanke beim Erzwénge vun Dateintegritéitsrestriktioune a beim Handhabe vu komplexen Transaktiounen exzelléieren, huet eis Applikatioun esou Ufuerderungen net. Dokument-Datebanke kënne fir eisen Notzungsfall genuch Konsistenz- an Duerabilitéitsgarantië bidden.

## Konsequenzen

Wa mir eng Dokument-Datebank wielen, musse mir an d'Léiere an d'Verständnis vun der spezifescher Technologie investéieren, déi mir wielen. Zousätzlech musse mir sécherstellen, datt den Datemodell vun eiser Applikatioun gutt zum Datemodell vun der Dokument-Datebank passt, fir d'Performance a Skaléierbarkeet ze maximéieren.

Mir gleewen awer, datt d'Virdeeler vum Benotze vun enger Dokument-Datebank d'Käschte iwwerwiegen an datt se am beschte fir d'Ufuerderungen a Restriktioune vun eiser Applikatioun passt.
