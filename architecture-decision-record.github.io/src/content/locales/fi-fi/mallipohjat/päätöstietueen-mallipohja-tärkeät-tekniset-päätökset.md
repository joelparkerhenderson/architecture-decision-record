# Päätöstietueen mallipohja: tärkeät tekniset päätökset (ITD)

Tämä on Important Technical Decisions (ITD) -mallipohja, joka on kuvattu artikkelissa
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

ITD-tietueet ovat ADR-tietueiden kohdennettu kehitysaskel, optimoitu nopeuteen, selkeyteen
ja johdon validointiin. Siinä missä ADR dokumentoi, mitä päätettiin, ITD on
kevyt, päätös edellä oleva artefakti, joka tekee itse päätöksestä katselmoitavan, jolloin
sidosryhmät voivat silmäillä sen nopeasti ja haastaa sen helposti. ITD-tietueet sopivat hyvin
teknisiin päätöksiin, jotka eivät ole tiukasti arkkitehtuurisia, kuten mallin,
kirjaston tai CI/CD-strategian valinta.

Kirjoita jokaiseen ITD-tiedostoon nämä osiot:

# Otsikko

Ilmaise itse päätös, ei aiheen kuvausta.
Esimerkiksi "Käytä Qwen2.5 1.5B Instruct -mallia laitteella tapahtuvaan käännökseen".

## Ongelma

Yksi lause, joka kertoo, mitä yritämme ratkaista.

## Harkitut vaihtoehdot

Vaihtoehdot, jotka olivat pöydällä, valittu vaihtoehto **lihavoituna**.

## Perustelut

Vain ratkaisevat tekijät, jotka johtivat valintaan, ei tyhjentävää luetteloa
kaikista hyvistä ja huonoista puolista.

## Huomiot

Valinnainen. Mikä tahansa lisäkonteksti, joka kannattaa kirjata, kuten rajoitteet,
oletukset tai linkit.
