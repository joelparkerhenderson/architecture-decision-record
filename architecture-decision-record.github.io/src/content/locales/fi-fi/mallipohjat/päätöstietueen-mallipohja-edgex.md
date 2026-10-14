# Arkkitehtuuripäätöstietueen (ADR) mallipohja <!-- Korvaa ADR-tietueen otsikolla -->

Tämä on mallipohja EdgeX Foundryn ADR-tietueille.

Lähde: https://docs.edgexfoundry.org/2.3/design/adr/template/


### Esittäjät

Luettele ADR-tietueen esittäjät.

Muoto:

- Nimi (Organisaatio)


## Muutosloki

Luettele dokumentin muutokset, mukaan lukien tila, päivämäärä ja vetopyynnön (PR) URL.

Tila on yksi seuraavista: odottaa, hyväksytty, muutettu, vanhentunut.

Päivämäärä on ISO 8601 -merkkijono (VVVV-KK-PP).

PR on vetopyyntö (pull request), jolla muutos esitettiin, sisältäen tietoja kuten erot, osallistujat ja katselmoijat.

Muoto:

- \[ADR-tietueen tila esim. hyväksytty, muutettu jne.\]\(vetopyynnön URL\) VVVV-KK-PP


## Viitatut käyttötapaukset

Luettele kaikki olennaiset käyttötapaus- / vaatimusdokumentit.

ADR vaatii vähintään yhden olennaisen, hyväksytyn käyttötapauksen.

Muoto:

- \[Käyttötapauksen nimi\]\(URL\)

Lisää selityksiä, jos ADR ei käsittele kaikkia käyttötapauksen vaatimuksia.


## Konteksti

Kuvaile:

- miten suunnittelu on arkkitehtuurisesti merkittävä — oikeuttaen ADR-tietueen (verrattuna yksinkertaiseen ongelmaraporttiin ja PR:ään ongelman korjaamiseksi)

- korkean tason suunnittelulähestymistapa (yksityiskohdat kuvataan alla olevassa ehdotetussa suunnitelmassa)


## Ehdotettu suunnitelma

Suunnitelman yksityiskohdat (ilman toteutukseen menemistä, kun mahdollista).

Jäsennys:

- palvelut/moduulit, joihin vaikutetaan (muutetaan)

- lisättävät uudet palvelut/moduulit

- malli- ja DTO-vaikutukset (muutokset/lisäykset/poistot)

- API-vaikutukset (muutokset/lisäykset/poistot)

- yleiset konfiguraatiovaikutukset (uusien osioiden perustaminen, muutokset/lisäykset/poistot)

- devops-vaikutukset


## Huomioon otettavat seikat

Dokumentoi vaihtoehdot, huolenaiheet, oheiset tai liittyvät kysymykset ja ADR-tietueen keskustelussa esiin nousseet kysymykset. 

Ilmoita, onko ne ratkaistu tai lievennetty ja miten.


## Päätös

Dokumentoi kaikki sovitut tärkeät toteutusyksityiskohdat, varaumat, tulevaisuuden huomiot sekä jäljellä olevat tai lykätyt suunnitteluongelmat.

Dokumentoi kaikki vaatimusten osat, joita ehdotettu suunnitelma ei täytä.


## Muut liittyvät ADR-tietueet

Luettele kaikki olennaiset ADR-tietueet — kuten suunnittelupäätös ominaisuuden osakomponentille, tämän suunnitelman seurauksena vanhentunut suunnitelma jne. 

Muoto:

- \[ADR-tietueen otsikko\]\(URL\) - Olennaisuus


## Viitteet

Luettele lisäviitteet.

Muoto:

- \[Otsikko\]\(URL\)
