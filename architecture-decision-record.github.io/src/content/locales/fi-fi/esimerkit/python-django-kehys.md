# Arkkitehtuuripäätöstietue: Python Django -kehys

Päätöksen päivämäärä: 2021-07-15

Tila: Hyväksytty

## Konteksti

Organisaatiomme suunnittelee verkkosovelluksen kehittämistä asiakastietojen hallintaan. Olemme valinneet Pythonin ohjelmointikieleksi ja harkitsemme Djangoa verkkokehykseksi sovelluksen kehittämiseen.

## Päätös

Olemme päättäneet käyttää Django-verkkokehystä verkkosovelluksen kehittämiseen. Django tarjoaa vankan joukon työkaluja ja ominaisuuksia verkkosovellusten rakentamiseen nopeasti ja tehokkaasti. 

## Tekijät

Joitakin päätökseemme vaikuttaneita tekijöitä ovat:

1. Objekti-relaatiomappaus (ORM): Djangossa on sisäänrakennettu ORM, jonka avulla voimme olla vuorovaikutuksessa tietokannan kanssa kirjoittamatta SQL-kyselyjä. Tämä helpottaa sovelluksen kehittämistä ja ylläpitoa pitkällä aikavälillä.

2. MVC-kehys: Django noudattaa Model-View-Controller (MVC) -arkkitehtuuria, mikä helpottaa sovelluksen liiketoimintalogiikan ja esityskerroksen erottamista.

3. Skaalautuvuus: Django tunnetaan skaalautuvuusominaisuuksistaan, mikä tekee siitä erinomaisen valinnan laajamittaisten sovellusten kehittämiseen.

4. Tietoturva: Djangossa on sisäänrakennettuja tietoturvaominaisuuksia, kuten suojaus yleisiltä verkkohyökkäyksiltä, kuten sivustojen väliseltä komentosarjahyökkäykseltä (XSS) ja SQL-injektiolta.

5. Yhteisön tuki: Djangolla on suuri ja aktiivinen yhteisö, joka tarjoaa tukea ja osallistuu kehyksen kehittämiseen.

## Harkitut vaihtoehdot

Harkitsimme muita verkkokehyksiä kuten Flask ja Pyramid. Havaitsimme kuitenkin, että Django on kypsempi ja vakiintuneempi kehys, jolla on vankka ominaisuusjoukko.

Keskustelimme myös sovelluksen kehittämisestä ilman verkkokehystä käyttäen kirjastoja kuten SQLAlchemy ja Flask-RESTful. Havaitsimme kuitenkin, että Django tarjoaa laajemman toiminnallisuuden, mikä tekee siitä paremman valinnan täydelliseen verkkosovellukseen.

## Seuraukset

Djangon käyttöönotto johtaa seuraaviin seurauksiin:

1. Sovelluksen kehittäminen ja ylläpito on helpompaa Djangon sisäänrakennettujen työkalujen ja ominaisuuksien ansiosta.

2. Liiketoimintalogiikan ja esityskerroksen erottaminen, mikä johtaa järjestäytyneempään ja helpommin ylläpidettävään koodiin.

3. Sovelluksen skaalautuvuus ja vakaus.

4. Sisäänrakennetut tietoturvaominaisuudet, jotka auttavat suojaamaan sovellusta yleisiltä verkkohyökkäyksiltä.

5. Pääsy suureen ja aktiiviseen yhteisöön tuen saamiseksi.

Ymmärrämme, että Djangon oppimiskäyrä on jyrkempi kuin muilla kehyksillä, mutta pidämme sitä investoinnin arvoisena sen tarjoamien pitkän aikavälin hyötyjen vuoksi.

## Johtopäätös

Huomioon otettujen tekijöiden perusteella olemme päättäneet käyttää Django-verkkokehystä verkkosovelluksen kehittämiseen. Uskomme, että Djangon ominaisuudet, yhteisön tuki ja skaalautuvuusominaisuudet tekevät siitä parhaan valinnan täydellisen verkkosovelluksen rakentamiseen. Koulutamme kehittäjämme käyttämään Djangoa varmistaaksemme, että kehystä käytetään tehokkaasti ja vaikuttavasti.
