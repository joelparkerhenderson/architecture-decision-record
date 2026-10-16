# Zapis arhitekturne odločitve za ogrodje Python Django

Datum odločitve: 2021-07-15

Stanje: Sprejeto

## Kontekst

Naša organizacija načrtuje razvoj spletne aplikacije za upravljanje podatkov o strankah. Za programski jezik smo izbrali Python in kot spletno ogrodje za razvoj aplikacije preučujemo Django.

## Odločitev

Odločili smo se, da za razvoj spletne aplikacije uporabimo spletno ogrodje Django. Django zagotavlja robusten nabor orodij in funkcij za hitro in učinkovito gradnjo spletnih aplikacij. 

## Dejavniki

Nekateri dejavniki, ki so vplivali na našo odločitev, vključujejo:

1. Objektno-relacijsko preslikavanje (ORM): Django ima vgrajen ORM, ki nam omogoča interakcijo s podatkovno bazo brez pisanja poizvedb SQL. To olajša razvoj aplikacije in njeno dolgoročno vzdrževanje.

2. Ogrodje MVC: Django sledi arhitekturi Model-View-Controller (MVC), kar olajša ločevanje poslovne logike in predstavitvenih plasti aplikacije.

3. Razširljivost: Django je znan po svojih zmožnostih razširljivosti, zato je odlična izbira za razvoj obsežnih aplikacij.

4. Varnost: Django ima vgrajene varnostne funkcije, kot je zaščita pred pogostimi spletnimi napadi, na primer skriptiranjem med spletnimi mesti (XSS) in vstavljanjem SQL.

5. Podpora skupnosti: Django ima veliko in dejavno skupnost, ki zagotavlja podporo in prispeva k razvoju ogrodja.

## Preučene alternative

Preučili smo druga spletna ogrodja, kot sta Flask in Pyramid. Vendar smo ugotovili, da je Django zrelejše in uveljavljenejše ogrodje z robustnim naborom funkcij.

Razpravljali smo tudi o razvoju aplikacije brez spletnega ogrodja z uporabo knjižnic, kot sta SQLAlchemy in Flask-RESTful. Vendar smo ugotovili, da Django ponuja širšo funkcionalnost, zato je boljša izbira za celotno spletno aplikacijo.

## Posledice

Uvedba ogrodja Django bo imela naslednje posledice:

1. Lažji razvoj in vzdrževanje aplikacije zaradi vgrajenih orodij in funkcij ogrodja Django.

2. Ločitev poslovne logike in predstavitvene plasti, kar vodi do bolj organizirane kode, ki jo je lažje vzdrževati.

3. Razširljivost in robustnost aplikacije.

4. Vgrajene varnostne funkcije, ki pomagajo zaščititi aplikacijo pred pogostimi spletnimi napadi.

5. Dostop do velike in dejavne skupnosti za podporo.

Zavedamo se, da ima Django strmejšo krivuljo učenja kot druga ogrodja, vendar menimo, da se naložba splača zaradi dolgoročnih koristi, ki jih zagotavlja.

## Sklep

Na podlagi preučenih dejavnikov smo se odločili, da za razvoj spletne aplikacije uporabimo spletno ogrodje Django. Verjamemo, da so funkcije, podpora skupnosti in zmožnosti razširljivosti ogrodja Django zaradi tega najboljša izbira za gradnjo celotne spletne aplikacije. Naše razvijalce bomo usposobili za uporabo ogrodja Django, da zagotovimo njegovo učinkovito in uspešno rabo.
