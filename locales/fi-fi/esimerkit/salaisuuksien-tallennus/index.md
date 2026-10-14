# Salaisuuksien tallennus

Sisällys:

* [Yhteenveto](#yhteenveto)
  * [Ongelma](#ongelma)
  * [Päätös](#päätös)
  * [Tila](#tila)
* [Yksityiskohdat](#yksityiskohdat)
  * [Oletukset](#oletukset)
  * [Rajoitteet](#rajoitteet)
  * [Kannat](#kannat)
  * [Perustelu](#perustelu)
  * [Seuraukset](#seuraukset)
* [Liittyvät](#liittyvät)
  * [Liittyvät päätökset](#liittyvät-päätökset)
  * [Liittyvät vaatimukset](#liittyvät-vaatimukset)
  * [Liittyvät artefaktit](#liittyvät-artefaktit)
  * [Liittyvät periaatteet](#liittyvät-periaatteet)
* [Huomiot](#huomiot)
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Yhteenveto


### Ongelma

Meidän on tallennettava salaisuuksia, kuten salasanoja, yksityisiä avaimia, tunnistautumistunnisteita jne.

Jotkin salaisuudet ovat käyttäjälähtöisiä. Esimerkiksi kehittäjämme haluavat pystyä käyttämään matkapuhelintaan palvelun salasanan hakemiseen.

Jotkin salaisuudet ovat järjestelmälähtöisiä. Esimerkiksi jatkuvan toimituksen putkemme on pystyttävä hakemaan pilvi-isännöintimme tunnistetiedot.


### Päätös

Bitwarden käyttäjälähtöisille salaisuuksille

Vault by HashiCorp järjestelmälähtöisille salaisuuksille.


### Tila

Päätetty. Olemme avoimia uusille vaihtoehdoille niiden ilmaantuessa.


## Yksityiskohdat


### Oletukset

Tässä tarkoituksessa ja nykytilassamme arvostamme käyttäjälähtöistä mukavuutta, kuten käyttökelpoisia mobiilisovelluksia.

  * Haluamme varmistaa nopean ja helpon pääsyn liikkeellä ollessa, esimerkiksi kehittäjälle, joka tekee päivystysluonteista järjestelmien luotettavuustekniikkaa.

  * Haluamme pystyä jakamaan joitakin salaisuuksia valittujen henkilöiden, kuten tiimin, kesken.

Emme yritä ratkaista yhden toimittajan ratkaisua, kuten kaikkien salaisuuksien tallentamista yksinomaan Amazoniin tai Azureen tai Googleen.

Emme halua ad hoc -lähestymistapoja kuten "muista se" tai "kirjoita se lappuun" tai "keksi oma tapasi tallentaa se".

Tietoturvamallimme tähän tarkoitukseen sopii hyvin yhteen hyvämaineisten COTS-toimittajien, kuten SaaS-salasananhallintatyökalujen, käytön kanssa.


### Rajoitteet

Juuri nyt haluamme jotain helppoa eli ei tarvitse kirjoittaa koodia, ei tarvitse asentaa palvelimia, ei tarvitse tehdä suurta sitoumusta, ei tarvitse standardoida kaikkia.


### Kannat

Harkitsimme:

1. Käyttäjälähtöisiä valmiita salasananhallintaohjelmia: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG jne.

2. Järjestelmälähtöisiä COTS-salasananhallintaohjelmia: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Jakamislähtöisiä lähestymistapoja: jaetun Google-dokumentin, jaetun Slack-kanavan tai jaetun verkkokansion jne. käyttö.

4. Vähätekniikkaisia ad hoc -lähestymistapoja, kuten muistaminen, lapun kirjoittaminen tai luottaminen siihen, että jokainen käyttäjä keksii oman tapansa.


### Perustelu

Bitwarden, LastPass, 1Password ja Dashlane ovat kaikki kaupallisia valmistuotteita.

  * Samankaltaiset ominaisuudet käyttäjille, tiimeille, organisaatioille jne.

  * Työpöytäominaisuudet Windowsille ja Macille sekä mobiiliominaisuudet Androidille ja iOS:lle.

  * Selainlaajennukset Chromelle ja Firefoxille lomakkeiden automaattiseen täyttöön jne.

Bitwardenilla on kaksi etua muihin nähden:

  * Bitwarden on avointa lähdekoodia, mikä tarkoittaa, että tietoturvaa voidaan vertaisarvioida ja että yritystä arvostetaan laajasti tietoturvalähtöisten kehittäjien keskuudessa.

  * Ohjelmistotyöntekijöiden anekdootit kuvaavat merkittävää mieltymystä Bitwardeniin muihin nähden.

Tyypillinen hyvä kirjoitus: https://jcs.org/2017/11/17/bitwarden

Tyypillinen rinnakkaisvertailuäänestyssivusto: https://stackshare.io/stackups/bitwarden-vs-dashlane

Lykkäämme KeePassin, passin, GPG:n jne. koska niissä on lisäkompleksisuutta. Kaikki nämä näyttävät hyviltä ratkaisuilta teknisille käyttäjille. GPG näyttää erityisen hyvältä teknisille käyttäjille, jotka haluavat järjestelmärajat ylittäviä komentolähtöisiä ominaisuuksia.

Lykkäämme KMS:n, koska siinä on yhden toimittajan lukitus.

Valitsemme Vaultin järjestelmälähtöisiin tarpeisiin, koska arvostelut ovat hämmästyttävän myönteisiä ja koska HashiCorpilla on erinomainen tuloshistoria huippulaatuisten ohjelmistojen ja tuen osalta.

Kiellämme jakamislähestymistavat, kuten jaettujen dokumenttien, jaettujen kanavien, jaettujen verkkokansioiden jne. kautta. Nämä eivät tarjoa tietoturvaominaisuuksia, joita haluamme.

Kiellämme ad hoc -vähätekniikkalähestymistavat, koska olemme kaikki samaa mieltä siitä, ettei se ole pitkän aikavälin tie eteenpäin.


### Seuraukset

Kehittäjien on ehkä seurattava salaisuuksia kahdessa paikassa: Bitwarden käyttäjälähtöiseen pääsyyn ja Vault järjestelmälähtöiseen pääsyyn.


## Liittyvät


### Liittyvät päätökset

Päätöksen siitä, mikä CI/CD-palvelin valitaan, on sisällettävä todiste kyvystä päästä käsiksi salaisuuksiin.

Meidän on päätettävä, miten salaisuuksia hallitaan politiikkojen, kierrätysten, organisaatioiden jne. osalta.


### Liittyvät vaatimukset

Salaisuuksilla on liittyviä vaatimuksia vaatimustenmukaisuudelle, auditoinnille sekä henkilöstöhallinnon perehdytykselle/poistumiselle.


### Liittyvät artefaktit

Odotamme, että saatamme viedä joitakin salaisuuksia ympäristömuuttujiin.


### Liittyvät periaatteet

Helposti peruttavissa.

Helposti rinnakkainen eli on helppo käyttää useita salasananhallintaohjelmia.

Halpa kokeilla eli on ilmainen kokeilu eikä sitoumusta.


## Huomiot

Arviointihuomiot tässä. Huomiot ovat kaikki julkisia kommentteja eri devops-keskustelufoorumeilla.


### Vault by HashiCorp

Vault on täsmälleen se, mitä haluat tässä. 

Älä kuitenkaan heitä Vaultia suoraan tuotantoon, pystytä se ensin testiympäristöön, koska HashiCorpin dokumentaatio voi olla melko puutteellista vaikka heidän tuotteensa ovat mahtavia.

Erittäin jyrkkä oppimiskäyrä, eikä sitä ole triviaalia pystyttää. 

Alkuasennus on hieman vaivalloinen. Se on kuitenkin ehdottomasti vaivan arvoinen, ja yhteisö tukee sitä riittävän hyvin, jotta pärjäät.

Kamalat dokumentit, mutta verkossa on paljon oppaita ihmisiltä, jotka ovat pystyttäneet sen, ja jos yhdistät muutaman niistä, sinulla on toimiva käyttöönotto.

Alkuasennus vaati näpertelyä heidän helm-kaavioidensa (vault ja consul) kanssa. Vaikka teknisesti voit käyttää monia muita taustajärjestelmiä, en todellakaan suosittele sitä. Taustajärjestelmä/consul voi olla pienen pieni, jos sinulla ei ole paljon tallennettavaa dataa.

Totu ehdottomasti CLI:n käyttöön, koska graafinen käyttöliittymä on enemmän konseptitodistus/mainosportaali heidän yritysversiolleen.

Se, ettet voi vain "täyttää sitä", on vaivalloista. Esimerkiksi jos sinulla on 5 kenttää, sinun on lisättävä jokainen kenttä manuaalisesti jokaiselle kohteelle. Eli ei ole niin, että määrittelisit kentät ennalta tietylle kategorialle ja täyttäisit nämä kentät kaikille kategorian kohteille, vaan se on enemmän "luot kaiken joka kerta", mikä (minun mielestäni) on kiusallista.

Voit myös tutustua goldfishiin Vaultin päälle tulevana käyttöliittymänä. Tekee tiimisi mukaan saamisesta melko mukavaa. Heillä on myös demo. 1. Pystytä consul. 2. Pystytä vault osoittamaan consuliin. 3. Pystytä goldfish osoittamaan vaultiin. 3. Pystytä jokin cron-työ ajamaan consul snapshot varmuuskopioita varten.



### LastPass

LastPass Teams. Käytämme sitä, siinä on mukautetut mallipohjat, ACL, mielestäni mitään ei puutu.

Otin LastPassin käyttöön organisaatiossani ja annan sille C+/B-. Suurin ongelma viime aikoina on luotettavuuden puute. Viimeisen 90 päivän aikana on ollut useita tunteja, jolloin holvit pakotettiin offline-tilaan. Tämä ei ole ihanteellista organisaatiolleni, koska meillä on kirjaimellisesti yli 4 000 salasanaa tallennettuna yli 20 jaettuun kansioon. Kuten voit kuvitella, näin monella salasanalla ainakin muutama päivittyy tai lisätään päivittäin. Meillä on katastrofipalautussuunnitelma, jos ongelmat kestävät yli tunnin tai kaksi: skripti allekirjoittaa ja salaa holvin CSV-vedoksen joka yö, ja se voidaan tuoda keepassiin.

LastPassilla on ollut raportoimattomia heikentyneen palvelun hetkiä: kirjautuminen "toimii" mutta ei hae sivustoja, satunnaisia ominaisuuksia rikki hallintapaneelissa, eikä avaimia jaeta oikein uusille ylimmän tason jaetuille kansioille. Minulla on erityinen "avaintyöntö"/varmuuskopiokäyttäjä, joka on jokaisessa ryhmässä. Yleensä kirjautuminen tuona käyttäjänä korjaa kaikki avaintenjakoon liittyvät ongelmat, mutta ei silloin kun palvelu on heikentynyt riippumatta siitä, mitä tilasivu sanoo...

Integraatiossa se voi olla helppoa, jos sinulla on asianmukaiset ACL:t vähimmän oikeuden mallilla, esim. jos käyttäjällä on sekä luku- ja kirjoitus- että vain lukuoikeus kohteeseen tai kansioon, hän saa vain lukuoikeuden. Valitettavasti organisaationi ACL:t eivät ole parhaita, joten päädyin käyttämään JSON-provisiointirajapintaa ja ~500 riviä pythonia, koska satojen ACL:iemme riippuvaisuudet eivät kartoitu hyvin vähimmän oikeuden malliin. Päädyin hakemaan kaikki ACL:t, joissa käyttäjä oli, ja tekemään jonkinlaisen riippuvuuskävelyn.

Jos ACL- tai ryhmärakenteesi on jo rakennettu vähimmän oikeuden rakenne mielessä, Windowsin AD/LDAP-synkronointityökalu toimii hyvin.

Ota yhteyttä heidän myyntitiimiinsä, ja he voivat järjestää sinulle pidemmän Enterprise-kokeilun. Varmista, että ymmärrät sen rajoitukset täysin ennen kuin painat liipaisinta. Meillä oli melko paljon kasvukipuja, mutta palvelinpuolen katkoksia tai heikentymisiä lukuun ottamatta se on ollut uskomattoman sujuva.


### Bitwarden

Bitwardenin ympärillä on hienot työkalut (verkkokäyttöliittymä, CLI, mobiili, työpöytä). Itseisännöitävissä ja melko helppo pystyttää. Melko hyvä dokumentaatio ja PrivacyToolsin suosittelema työkalu.


### EnvKey

https://www.envkey.com/ on saas. Todella helppo toteuttaa, integroida ja hallita.

Ominaisuudet:

  * Suojaa API-avaimet ja tunnistetiedot.

  * Pidä konfiguraatio synkronissa kaikkialla.

  * Älykäs, päästä päähän salattu konfiguraation ja salaisuuksien hallinta. 

  * Estä turvaton jakaminen ja konfiguraation hajaantuminen. 

  * Integroi minuuteissa.

Kyvykkyydet:

  * Hallitse konfiguraatiota ja pääsytasoja kaikille sovelluksillesi, ympäristöillesi ja tiimeillesi yhdessä paikassa.

  * Konfiguroi mikä tahansa kehitys- tai palvelinympäristö yhdellä ainoalla ympäristömuuttujalla.

Hyvät puolet:

  * Hyvä kotisivu.

  * Selkeä arvolupaus.

  * Visuaalisesti erinomainen verkkosovellus.

  * Ylivoimainen esimerkkidata esim. Algolia, AWS, Datadog, GitHub, Stripe jne.

  * Puhuin perustajan kanssa 30 minuuttia yrityksestä, käyttöliittymästä jne. Dane vaikuttaa hyvin perehtyneeltä, rehelliseltä hyvistä/huonoista puolista ja toteuttamiskelpoiselta kumppanilta.

  * Yritys on pohjimmiltaan tyypillinen Y Combinator -yritys, jossa on 1 perustaja. Keräsi 120 000 dollaria tammikuussa 2018.

  * Painopiste on yritysominaisuuksien saavuttamisessa, erityisesti siirtymässä EnvKeyn pilvi-isännöinnistä joko paikalliseen tai BYOC:hen.

  * Mahdollinen tie eteenpäin aloittamalla EnvKeyllä helppokäyttöisyyden vuoksi, sitten myöhemmin (tai rinnakkain) lisäämällä Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant on avoimen lähdekoodin salaisuuksienhallintapalvelu, joka tarjoaa käyttäjäystävällisen tallennuksen ja pääsyn salaisuuksiin turvallisella tavalla, Lyftin kehittäjiltä.

KMS-tunnistautuminen: Confidant ratkaisee tunnistautumisen muna–kana-ongelman käyttämällä AWS KMS:ää ja IAM:ia, jotta IAM-roolit voivat luoda turvallisia tunnistautumistunnisteita, jotka Confidant voi varmentaa. Confidant hallitsee myös KMS-myöntöjä IAM-rooleillesi, mikä sallii IAM-roolien luoda tunnisteita, joita voidaan käyttää palvelusta palveluun tunnistautumiseen tai salattujen viestien välittämiseen palvelujen välillä.

Versioitujen salaisuuksien lepotilan salaus: Confidant tallentaa salaisuudet vain lisäämällä DynamoDB:hen, luoden yksilöllisen KMS-datavaimen jokaiselle jokaisen salaisuuden versiolle käyttäen Fernet-symmetristä tunnistettua kryptografiaa.

Käyttäjäystävällinen verkkokäyttöliittymä salaisuuksien hallintaan: Confidant tarjoaa AngularJS-verkkokäyttöliittymän, jonka avulla loppukäyttäjät voivat helposti hallita salaisuuksia, salaisuuksien kytkemistä palveluihin ja muutoshistoriaa.


### Devolutions Password Server

https://server.devolutions.net/

Suojaa, hallitse ja valvo pääsyä etuoikeutettuihin tileihin ja istuntoihin.

Kattava, erittäin turvattu salasanaholvi, jonka avulla voit hallita pääsyä etuoikeutettuihin tileihisi, parantaen samalla yleistä verkon näkyvyyttä järjestelmänvalvojille ja tarjoten saumattoman kokemuksen loppukäyttäjille.

Ominaisuudet: keskitetty organisaation salasanaholvi, käyttäjäkohtainen yksityinen holvi, salasananhallinta, tunnistetietojen injektointi,
Active Directory -integraatio, roolipohjainen pääsynhallinta, kaksivaiheinen tunnistautuminen, yrityskäyttövalmis, IP-rajoitukset, hallintaominaisuudet, automaattinen salasanageneraattori, mobiilisovelluspääsy, salasanahistoria, pääsyraportit, sähköpostihälytykset.

  * tukee tietojen salausta

  * tukee useita tunnistautumismalleja, mukaan lukien LDAP, O365 ja paikalliset käyttäjät MFA-tuella useista lähteistä

  * useita tietovarastoja/holveja hienojakoisilla pääsynhallinnoilla usealle tiimille

  * moderni verkkokäyttöliittymä

  * yksityiset tunnistetieto- ja yhteysholvit henkilökohtaisille tunnuksille/yhteyksille

  * mobiilisovellukset iOS:lle/Androidille

  * auditointilokit jokaiselle merkinnälle, kuka/mitä/milloin ja valinnaisella kehotteella siitä, miksi he käyttävät

  * mukautettavat mallipohjat (vaikka ne tukevat satoja yhteystyyppejä natiivisti)

  * tonnia lisää ominaisuuksia ja Windows/Mac-paksu asiakas (Remote Desktop Manager), jonka kanssa voit synkronoida ja joka laajentaa vaihtoehtoja huomattavasti... yhden napsautuksen yhteydet

  * hinnoittelu ei ole ollenkaan paha - jopa 15 käyttäjää salasanapalvelimelle maksaa 500 dollaria vuodessa


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Paikallisen version ominaisuudet: 

  * Täysi hallinta päästä päähän -tietoturvajärjestelmiisi ja infrastruktuuriisi

  * Ota ohjelmisto käyttöön omassa paikallisessa datakeskuksessasi tai omassa virtuaalisessa yksityisessä pilviesiintymässäsi

  * Täytä lakisääteiset ja sääntelyvelvoitteet, jotka edellyttävät kaikkien tietojen ja järjestelmien sijaitsemista paikallisesti

Pilviversion ominaisuudet:

  * Ohjelmisto palveluna -malli antaa sinun rekisteröityä ja aloittaa heti

  * Joustava skaalautuvuus kasvaessasi

  * Azuren tarjoamat hallinnat ja redundanssi 99,9 %:n käyttöaikalupauksella (SLA)

Käyttäjäpalaute:

  * Käytimme aiemmin sitä tuotetta. Se oli niin helppo ohittaa ja säännöt toimivat vain älykkäille ihmisille. Laiskat tai tyhmät käyttäjät voivat helposti sotkea sen tiimialueella. Hinnat ovat neuvoteltavissa, kun puhut heidän kanssaan.

  * Voit ajaa sitä SQL expressillä ja Win 7 -koneella. 

  * Halpa.
