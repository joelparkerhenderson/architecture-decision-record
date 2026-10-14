# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: epätyydyttävä seikkailu](#microsoft-devops-ci-epätyydyttävä-seikkailu)
  * [Hacker News -keskustelun kohokohdat](#hacker-news--keskustelun-kohokohdat)
  * [Windows Development MVP](#windows-development-mvp)
  * [Edward Thomsonin (Azure PM) yhteenveto](#edward-thomsonin-azure-pm-yhteenveto)


## Yhteenveto


### Ongelma

Haluamme käyttää devopsia projektiemme rakentamiseen, integrointiin, käyttöönottoon ja isännöintiin. Harkitsemme Microsoft Azure DevOpsia.

  * Haluamme kehittäjäkokemuksen olevan nopea ja luotettava, sekä devopsin käyttöönoton, esim. konfiguroinnin, että jatkuvan käytön, esim. nopeiden koontiaikojen, osalta.
  
  * Haluamme harkita Microsoft Azuren käyttöä kokonaisuutena projektisovellusten, tietokantojen jne. isännöintiin.


### Päätös

Päätettiin Microsoft Azure DevOpsia vastaan.


### Tila

Päätetty. Olemme avoimia uudelleenarvioinnille, jos/kun uutta merkittävää tietoa ilmaantuu.


## Yksityiskohdat


### Oletukset

Kaikki tavanomaiset devops-oletukset, kuten kirjassa Accelerate.

  * Nopeat koonnit auttavat merkittävästi. Tämä nopeuttaa palautesilmukoita.

  * Voimme vaihtaa osia sisään/ulos vaihtoehtoisilta toimittajilta eli saatamme haluta tuoda omat nopeammat koontipalvelimemme tai käyttää omaa valintaamme versionhallintajärjestelmästä tai koordinoida itseisännöidyn jatkuvan integroinnin palvelimen kanssa.
  
  * Sujuva käytettävyys auttaa merkittävästi kehittäjäkokemuksessa ja sen kautta hienovaraisilla alueilla, kuten johdonmukaisuus, selkeys, tietoturva ja oppimiskäyrän helppous.

  * Kun jokin on rikki tai ongelmallinen, haluamme tehokkaan tavan raportoida ongelmasta. Tämä on erityisen tärkeää kaikkien tietoturvaan liittyvien ongelmien osalta.


### Rajoitteet

Ei tiedossa. Azurella on julkaistu sitoumus toimia hyvin ulkoisten työkalujen kanssa.


### Kannat

Harkitsimme Microsoft Azure Devopsin käyttöä verrattuna AWS:ään, joka on vakiintunut toimija.

Kokeilimme Azure DevOpsia, Azure Pipelinesia, Azure Repoa ja uuden palvelimen käynnistämistä Azuressa Terraformin kautta.

Kokeilimme tuen saamista Microsoftin edustajilta.

Keräsimme tietoa vertaisilta blogeista ja Hacker Newsista.


### Perustelu

Azure DevOps mainostaa erinomaista tarjontaa, mutta ne eivät pidä paikkaansa, eivät toimi hyvin yhdessä, ja tuki on heikkoa.

Omakohtainen kokemuksemme:

  * Azuren käyttöönotto on sotkua käyttöliittymiä, joista osa menee päällekkäin Microsoft-tilien kanssa ja osa ei. Esim. on Azure-kirjautuminen, Microsoft.com-kirjautuminen, Live.com-kirjautuminen jne. ja kaikki ovat samanaikaisesti pelissä.

  * Kohtasimme pienen tietoturvaongelman käyttöönoton aikana emmekä löytäneet ratkaisua. Yritimme monin tavoin raportoida siitä useille Microsoftin edustajille ilman tulosta. Raportoimme siitä onnistuneesti Microsoftin tietoturvalle, joka vastasi, ettei korjaa (won't fix).

  * Dokumentaatio on usein joko väärää tai vanhentunutta. Ainakin osa tästä johtuu Microsoftin heikosta hakukoneesta ja osa heikosta hakukoneoptimoinnista.
  
  * Terraform-käyttöönotto on hyvin dokumentoitu ja toimii. Terraform-tuki on kuitenkin heikkoa verrattuna AWS:ään, koska Microsoft rakentaa liikesuhteita toimittajien kanssa tehdäkseen ketjutettuja Terraform-käyttöönotto-esimerkkejä.

Vertaisten kokemukset:

  * Tehtyämme oman sokean arviomme etsimme vertaisten kokemuksia. Se, mitä löysimme, vahvisti kokemuksemme.

  * Vertaiset raportoivat lisäongelmista koontiajoissa ja ongelmista tuo-oma-koontipalvelin -vaihtoehdon kanssa. Nämä ongelmat ovat merkittävästi vakavampia kuin käyttöliittymäongelmat, koska koontien tekeminen on koontiputken ydintarkoitus, ja odotamme tekevämme niitä paljon päivässä.

  * Löysimme erinomaista Azure-tiimiläisten osallistumista keskustelualueilla. Kiitos Microsoftille tästä. Olemme erityisen vaikuttuneita Edward Thomsonista, Azure PM:stä ja koodaajasta, hänen osallistumisensa, suorapuheisuutensa ja teknisten selitystensä vuoksi.


### Seuraukset

Microsoft Azure DevOpsin valitseminen näyttää todennäköisesti olevan kalliimpaa (~3x) ajassa ja kustannuksissa kuin Azuren valitsematta jättäminen.


## Liittyvät


### Liittyvät päätökset

Jos valitsemme Azure DevOpsin, on monia liittyviä tarjouksia, mukaan lukien Azure Repo, Azure Pipeline jne. Uskomme, että jos valitsemme Azure Devopsin, tämä voi helpottaa useampien Azuren ominaisuuksien käyttöä tai vaikeuttaa muiden toimittajien ominaisuuksien käyttöä.

Uskomme, että Microsoft ottaa suuria edistysaskelia kehittäjäkokemuksessa, ja näemme Microsoftin tekevän suuria yritysostoja kehittäjätyökaluista (esim. GitHub) ja riippuvuuksista (esim. Citus).

Jos valitsemme Azure DevOpsin, saatamme haluta painottaa Microsoftin yritysostettujen tarjousten valitsemista, ja saatamme haluta lähestyä yritysostettuja tarjouksia suuremmalla huolella/arvioinnilla mahdollisen kudoshylkimisreaktion, esim. henkilöstövaihtuvuusriskin, vuoksi.


### Liittyvät vaatimukset

Haluamme koontiaikojen olevan erittäin nopeita. Hyväksymme korkean lisähinnan tästä. Tämä johtuu siitä, että haluamme iteroida erittäin nopeasti.

Haluamme luotettavuuden olevan erittäin korkea. Hyväksymme korkean lisähinnan tästä. Tämä johtuu siitä, että testaamme korkea-arvoisia käyttötapauksia, mukaan lukien rahoitustransaktiot, luottamukselliset transaktiot jne.

Neljä tärkeintä devops-KPI-mittariamme sisältävät keskimääräisen palautumisajan, mikä edellyttää nopeita koonteja ja korkeaa luotettavuutta.


### Liittyvät artefaktit

Haluamme koontijärjestelmän tuottavan artefakteja, jotka sopivat käytettäviksi muissa järjestelmissä, kuten Artifactoryssa.


### Liittyvät periaatteet

Helposti peruttavissa. Voimme arvioida Azure DevOpsia rinnakkain vakiintuneen AWS:n kanssa.


## Huomiot


### Microsoft Devops CI: epätyydyttävä seikkailu

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Blogikirjoitus.

"Ohjelmistokehittäjänä tiedän omakohtaisesti, kuinka vaikeaa on rakentaa laadukkaita tuotteita nopeasti ja halvalla. Se on taiteenlaji, jonka teemme joskus oikein, ja toisinaan se rapistuu joksikin Obaman ajan terveydenhuollon valtionsivuston kaltaiseksi. Hallintamme lopputuotteeseen vaihtelee, ja syy epäonnistumiseen osuu usein väärille ihmisille päätöksentekohierarkiassa. Microsoftin Azure DevOps (aiemmin Visual Studio Team Services) on selvistä hyvistä aikeista huolimatta täydellinen myrsky huonoja päätöksiä ja heikkoa toteutusta."


### Hacker News -keskustelun kohokohdat

https://news.ycombinator.com/item?id=18983586

"Käytämme Azure DevOpsia laajasti työpaikallani ja käytettyäni GitHubia, Gitlabia, itseisännöityjä ratkaisuja, Jenkinsiä, TeamCityä... Azure DevOps on aivan viimeisenä."

"Käyttöliittymä on kauhean kömpelö kaikkialla. Pahinta minulle ovat vetopyynnöt (pull request). Uskomattoman vaikeaa työskennellä ihmisten kanssa vetopyynnössä. En voi edes osoittaa "yhtä" tiettyä ongelmaa - meillä se on rikki kaikkialla."

"Azure Devops on jotain, mistä haluan pitää. Käyttöliittymä muuttuu jatkuvasti, mutta ei korjaa pohjimmaisia vikoja, jotka ovat olleet olemassa ikuisuuden."

"Työkalut eivät ole hyvin integroituja, käyttöliittymä on todella hidas, ei ole kojelautanäkymää aktiivisista vetopyynnöistä, koonneista, julkaisuista jne. lempitietovarastoilleni. Koonti-/käyttöönottoajat ovat älyttömän hitaita."

"Yritimme käyttää myös Azure Boardsia (Work Items, Boards, Backlogs jne.). Auts. Se on täydellinen käyttöliittymäsotku irrallisia ideoita. Yhden asian hyvin toteuttamisen sijaan he toteuttivat kaksi tusinaa asiaa kauheasti."


### Windows Development MVP

Windows Development MVP täällä. Tuntuu, että minun on kannettava osa vastuusta siitä, etten ole ollut äänekkäämpi näistä ongelmista. Mutta on sanottava, että olen pettynyt kuullessani sinun olevan "yllättynyt" käyttökokemusongelmista. Olen kertonut väellesi käyttökokemuksen olevan kauhea (esim. jo ennen julkaisua) ja kuullut toistuvasti vastauksen "tiedämme, korjaamme sitä". Alan muotoilla palautetta virallisesti ja viedä sen putkien läpi, pysy kuulolla. Olen myös paikallinen (Bellevue) ja tulisin mielelläni käymään ja yrittämään viedä suhteellisen yksinkertaista oss .net/wpf/uwp-sovellustamme putkeen. Epäilen, että se avaa silmämme molemmille.

Joitakin esimerkkejä:

* Putkea ei voi rakentaa git-tietovarastolle, joka sisältää alimoduuleja

* Totesin mahdottomaksi muokata PATHia joillekin mukautetuille työkaluille

* Uuden putken kokemus ei vain ole kovin järkevä, uudet käyttäjät, jotka klikkailevat ympäriinsä, päätyvät lopulta väärään dokumentaatioon.


### Edward Thomsonin (Azure PM) yhteenveto

Kirjoitin koodin, joka yhdistää vetopyyntösi. Ohjelmapäällikkö Microsoftilla Azure DevOpsille; aiemmin ohjelmistoinsinööri versionhallintatyökalujen parissa GitHubilla, Microsoftilla, SourceGearilla.

https://www.edwardthomson.com/

libgit2:n yhteisylläpitäjä. https://libgit2.github.io

All Things Git -podcastin, Git-podcastin, yhteisjuontaja. https://www.allthingsgit.com/

Developer Tools Weekly -uutiskirjeen, kehitystyökaluista kertovan uutiskirjeen, kuraattori. https://developertoolsweekly.com/
