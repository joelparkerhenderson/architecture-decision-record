# Zapis arhitekturne odluke: API s JSON-om ili gRPC-om

## Status

Prihvaćeno

## Kontekst

Dizajniramo API za novu uslugu koju će koristiti više klijenata. Razmatrali smo dvije opcije za implementaciju API-ja: korištenje JSON-a preko HTTP-a ili korištenje gRPC-a.

JSON preko HTTP-a široko je korišten pristup izgradnji API-ja i podržavaju ga mnogi programski jezici i okviri. Taj je pristup jednostavan, lagan i lako razumljiv, što ga čini dobrim izborom za mnoge projekte. Međutim, može biti manje učinkovit od drugih opcija, osobito kada je riječ o obradi velikih količina podataka.

gRPC je, s druge strane, novija tehnologija koja nudi učinkovitiji način izgradnje API-ja. Koristi binarnu serijalizaciju za prijenos podataka, koja može biti brža i kompaktnija od korištenja JSON-a. gRPC također podržava dvosmjerno strujanje, što ga čini dobrim izborom za aplikacije u stvarnom vremenu.

## Odluka

Nakon razmatranja prednosti i nedostataka obiju opcija odlučili smo koristiti gRPC za naš API. Iako je JSON preko HTTP-a jednostavnija opcija, vjerujemo da će gRPC pružiti učinkovitije i skalabilnije rješenje za našu uslugu. Također očekujemo da će naš API obrađivati veliku količinu podataka, a binarna serijalizacija gRPC-a bit će učinkovitija za taj slučaj uporabe.

Osim toga, vjerujemo da će podrška gRPC-a za dvosmjerno strujanje biti korisna za aplikacije u stvarnom vremenu koje bismo mogli razviti u budućnosti.

## Posljedice

Odabirom gRPC-a morat ćemo koristiti drukčiji skup alata i biblioteka za izgradnju našeg API-ja u usporedbi s korištenjem JSON-a preko HTTP-a. To može zahtijevati dodatno vrijeme i trud za učenje i implementaciju tih tehnologija. Osim toga, klijenti koji žele koristiti naš API morat će koristiti biblioteke kompatibilne s gRPC-om, koje možda nisu tako široko podržane kao biblioteke za JSON preko HTTP-a.

Međutim, vjerujemo da koristi od korištenja gRPC-a nadmašuju te potencijalne nedostatke i uvjereni smo da će ova odluka rezultirati učinkovitijim i skalabilnijim API-jem.