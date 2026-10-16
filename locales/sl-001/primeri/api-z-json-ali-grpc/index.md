# Zapis arhitekturne odločitve: API z JSON ali gRPC

## Stanje

Sprejeto

## Kontekst

Oblikujemo API za novo storitev, ki jo bo uporabljalo več odjemalcev. Preučujemo dve možnosti za izvedbo API: uporabo JSON prek HTTP ali uporabo gRPC.

JSON prek HTTP je široko uporabljen pristop za gradnjo API, podpira ga veliko programskih jezikov in ogrodij. Ta pristop je preprost, lahek in lahko razumljiv, zato je dobra izbira za mnoge projekte. Vendar je lahko manj učinkovit kot druge možnosti, zlasti pri obdelavi velikih količin podatkov.

gRPC je po drugi strani novejša tehnologija, ki ponuja učinkovitejši način gradnje API. Za prenos podatkov uporablja binarno serializacijo, ki je lahko hitrejša in bolj kompaktna kot JSON. gRPC podpira tudi dvosmerno pretakanje (bidirectional streaming), zato je dobra izbira za aplikacije v realnem času.

## Odločitev

Po preudarku prednosti in slabosti obeh možnosti smo se odločili, da za naš API uporabimo gRPC. Čeprav je JSON prek HTTP preprostejša možnost, verjamemo, da bo gRPC zagotovil učinkovitejšo in razširljivejšo rešitev za našo storitev. Pričakujemo tudi, da bo naš API obdeloval veliko količino podatkov, in binarna serializacija gRPC bo za ta primer uporabe učinkovitejša.

Poleg tega verjamemo, da bo podpora gRPC za dvosmerno pretakanje koristna za aplikacije v realnem času, ki jih bomo morda razvili v prihodnosti.

## Posledice

Z izbiro gRPC bomo morali za gradnjo svojega API uporabiti drugačen nabor orodij in knjižnic kot pri uporabi JSON prek HTTP. To bo morda zahtevalo dodaten čas in trud za učenje in izvedbo teh tehnologij. Poleg tega bodo morali odjemalci, ki želijo uporabljati naš API, uporabljati knjižnice, združljive z gRPC, ki morda niso tako široko podprte kot knjižnice za JSON prek HTTP.

Vendar verjamemo, da koristi uporabe gRPC odtehtajo te morebitne pomanjkljivosti, in smo prepričani, da bo ta odločitev prinesla učinkovitejši in razširljivejši API.
