# Architektūros sprendimo įrašas dėl Python Django karkaso

Sprendimo data: 2021-07-15

Būsena: priimtas

## Kontekstas

Mūsų organizacija planuoja sukurti interneto programą, valdančią klientų duomenis. Kaip programavimo kalbą pasirinkome Python ir svarstome Django kaip interneto karkasą programai kurti.

## Sprendimas

Nusprendėme interneto programai kurti naudoti Django interneto karkasą. Django suteikia tvirtą įrankių ir funkcijų rinkinį interneto programoms kurti greitai ir efektyviai. 

## Veiksniai

Kai kurie sprendimą lėmę veiksniai:

1. Objektinis-reliacinis susiejimas (ORM): Django turi integruotą ORM, leidžiantį sąveikauti su duomenų baze nerašant SQL užklausų. Tai palengvina programos kūrimą ir ilgalaikę priežiūrą.

2. MVC karkasas: Django laikosi Model-View-Controller (MVC) architektūros, todėl lengviau atskirti programos verslo logikos ir pateikimo sluoksnius.

3. Mastelio keitimas: Django žinomas dėl savo mastelio keitimo galimybių, todėl yra puikus pasirinkimas didelio masto programoms kurti.

4. Saugumas: Django turi integruotas saugumo funkcijas, tokias kaip apsauga nuo dažnų interneto atakų, pavyzdžiui, kryžminio svetainių scenarijų vykdymo (XSS) ir SQL injekcijos.

5. Bendruomenės parama: Django turi didelę ir aktyvią bendruomenę, teikiančią paramą ir prisidedančią prie karkaso kūrimo.

## Svarstytos alternatyvos

Svarstėme kitus interneto karkasus, tokius kaip Flask ir Pyramid. Tačiau nustatėme, kad Django yra brandesnis ir labiau įsitvirtinęs karkasas su tvirtu funkcijų rinkiniu.

Taip pat aptarėme programos kūrimą be interneto karkaso ir naudojant bibliotekas, tokias kaip SQLAlchemy ir Flask-RESTful. Tačiau nustatėme, kad Django siūlo platesnį funkcionalumą, todėl yra geresnis pasirinkimas visaverčiai interneto programai.

## Pasekmės

Django priėmimas lems šias pasekmes:

1. Lengviau kurti ir prižiūrėti programą dėl Django integruotų įrankių ir funkcijų.

2. Verslo logikos ir pateikimo sluoksnio atskyrimas, lemiantis labiau susistemintą ir lengviau prižiūrimą kodą.

3. Programos mastelio keitimas ir tvirtumas.

4. Integruotos saugumo funkcijos, padedančios apsaugoti programą nuo dažnų interneto atakų.

5. Prieiga prie didelės ir aktyvios bendruomenės paramai gauti.

Suprantame, kad Django mokymosi kreivė statesnė nei kitų karkasų, tačiau manome, kad tai verta investicija dėl ilgalaikių suteikiamų privalumų.

## Išvada

Remdamiesi apsvarstytais veiksniais, nusprendėme interneto programai kurti naudoti Django interneto karkasą. Manome, kad Django funkcijos, bendruomenės parama ir mastelio keitimo galimybės daro jį geriausiu pasirinkimu visaverčiai interneto programai kurti. Apmokysime savo programuotojus naudotis Django, kad karkasas būtų naudojamas veiksmingai ir efektyviai.
