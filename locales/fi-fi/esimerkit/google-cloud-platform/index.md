# Arkkitehtuuripäätöstietue: Google Cloud Platform

## Konteksti

Google Cloud Platform (GCP) on merkittävä pilvilaskenta-alusta, joka tarjoaa erilaisia pilvipalveluja, mukaan lukien laskenta-, tallennus- ja verkkoratkaisuja. Tämän ADR-tietueen tarkoituksena on dokumentoida arkkitehtuuripäätökset, jotka on tehty GCP-pohjaisen infrastruktuurin kehittämiseksi ja toteuttamiseksi organisaatiollemme.

## Päätös

Organisaatiomme on päättänyt käyttää Google Cloud Platformia sovelluksemme pilvi-infrastruktuurina. Päätöksen ensisijaiset näkökohdat ovat:

   - Kustannustehokkuus

   - Skaalautuvuus

   - Luotettavuus

   - Joustavuus

## Valinnat

Vaatimustemme täyttämiseksi on valittu seuraavat GCP:n palvelut:

   - Compute Engine virtuaalikoneille ja laskentaresursseille

   - Cloud Storage objektitallennukseen ja tiedostojen isännöintiin

   - Cloud SQL hallinnoituun tietokantapalveluun

   - Firebase sovelluskehitykseen ja isännöintiin

## Perustelut

   - Kustannustehokkuus: Google Cloud Platform on erittäin kustannustehokas verrattuna muihin pilvialustoihin, mikä tekee siitä houkuttelevan vaihtoehdon organisaatioille, joilla on budjettirajoituksia.

   - Skaalautuvuus: GCP:n helposti skaalattava infrastruktuuri mahdollistaa minkä tahansa liikennemäärän käsittelyn reaaliajassa.

   - Luotettavuus: GCP:n hallinnoidut palvelut tarjoavat korkean luotettavuuden, automaattisilla varmuuskopioilla ja katastrofipalautusominaisuuksilla, jotka varmistavat resurssien ja tietojen korkean käytettävyyden.

   - Joustavuus: Alusta tarjoaa erilaisia työkaluja ja palveluja eri aloille, kuten tekoäly, data-analytiikka ja IoT, mikä tekee siitä erittäin monipuolisen.

## Seuraukset

Siirtyminen Google Cloud Platformiin vaatii tiimiemme kouluttamista GCP-palveluihin, sovelluksen uudelleenarkkitehtuuria valittujen palvelujen kanssa yhteensopivaksi ja infrastruktuurikoodin päivittämistä GCP-palvelujen tukemiseksi. Odotamme kuitenkin, että siirron valmistuttua meillä on erittäin skaalautuva, luotettava ja kustannustehokas infrastruktuuri sovelluksemme isännöintiin. Lisäksi meidän on hallittava resurssien varaamisesta GCP:ssä aiheutuvia jatkuvia kustannuksia.

## Johtopäätös

Google Cloud Platform on erinomainen valinta pilvi-infrastruktuurillemme sen kustannustehokkuuden, skaalautuvuuden, luotettavuuden ja joustavuuden vuoksi. Käyttämällä valittuja palveluja voimme tarjota sovelluksellemme erittäin käytettävissä olevan ja vankan infrastruktuurin.
