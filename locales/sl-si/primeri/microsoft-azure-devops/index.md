# Microsoft Azure DevOps

Vsebina:

* [Povzetek](#povzetek)
  * [Vprašanje](#vprašanje)
  * [Odločitev](#odločitev)
  * [Stanje](#stanje)
* [Podrobnosti](#podrobnosti)
  * [Predpostavke](#predpostavke)
  * [Omejitve](#omejitve)
  * [Stališča](#stališča)
  * [Argument](#argument)
  * [Posledice](#posledice)
* [Povezano](#povezano)
  * [Povezane odločitve](#povezane-odločitve)
  * [Povezane zahteve](#povezane-zahteve)
  * [Povezani artefakti](#povezani-artefakti)
  * [Povezana načela](#povezana-načela)
* [Opombe](#opombe)
  * [Microsoft Devops CI: nezadovoljiva dogodivščina](#microsoft-devops-ci-nezadovoljiva-dogodivščina)
  * [Poudarki razprave na Hacker News](#poudarki-razprave-na-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Povzetek Edwarda Thomsona (Azure PM)](#povzetek-edwarda-thomsona-azure-pm)


## Povzetek


### Vprašanje

Za gradnjo, integracijo, uvajanje in gostovanje svojih projektov želimo uporabljati DevOps. Preučujemo Microsoft Azure DevOps.

  * Želimo, da je izkušnja razvijalcev hitra in zanesljiva, tako pri postavitvi DevOps, npr. konfiguriranju, kot pri tekoči uporabi, npr. hitrih časih gradnje.
  
  * Želimo preučiti uporabo Microsoft Azure kot celote za gostovanje aplikacij projekta, podatkovnih baz itd.


### Odločitev

Odločili smo se proti Microsoft Azure DevOps.


### Stanje

Odločeno. Odprti smo za ponovno preučitev, če in ko prispejo nove pomembne informacije.


## Podrobnosti


### Predpostavke

Vse običajne predpostavke DevOps, kot so v knjigi Accelerate.

  * Hitre gradnje so velika pomoč. To pospeši povratne zanke.

  * Dele lahko zamenjamo z deli drugih dobaviteljev, tj. morda bi radi uporabili svoje hitrejše strežnike za gradnjo, svoj sistem za nadzor različic ali se uskladili z lastnim strežnikom za neprekinjeno integracijo.
  
  * Poenostavljena uporabnost je velika pomoč za izkušnjo razvijalcev in posledično za subtilna področja, kot so doslednost, jasnost, varnost in lažja krivulja učenja.

  * Kadar je karkoli pokvarjeno ali problematično, želimo učinkovit način za prijavo težave. To je še posebej pomembno pri težavah, povezanih z varnostjo.


### Omejitve

Nobene znane. Azure ima objavljeno zavezo, da dobro sodeluje z zunanjimi orodji.


### Stališča

Preučili smo uporabo Microsoft Azure DevOps v primerjavi z AWS, ki je obstoječa izbira.

Eksperimentirali smo z Azure DevOps, Azure Pipelines, Azure Repo in zagonom novega strežnika v Azure prek Terraform.

Poskusili smo pridobiti podporo od predstavnikov Microsofta.

Informacije smo zbrali od kolegov na blogih in na Hacker News.


### Argument

Azure DevOps oglašuje odličen nabor ponudb, vendar ne zdržijo preizkusa, ne delujejo dobro skupaj in podpora je slaba.

Naša neposredna izkušnja:

  * Postavitev Azure je zmeda uporabniških vmesnikov, od katerih se nekateri prekrivajo z računi Microsoft, nekateri pa ne. Npr. obstaja prijava v Azure, prijava na Microsoft.com, prijava na Live.com itd. in vse so hkrati v igri.

  * Med postavitvijo smo naleteli na manjšo varnostno težavo in nismo našli rešitve. Poskusili smo jo prijaviti na mnogo načinov mnogim predstavnikom Microsofta, brez uspeha. Uspešno smo jo prijavili varnostni službi Microsofta, ki je odgovorila z »won't fix« (ne bo popravljeno).

  * Dokumentacija je pogosto napačna ali zastarela. Vsaj nekaj tega je posledica Microsoftovega slabega iskalnika, nekaj pa podpovprečne SEO.
  
  * Postavitev s Terraform je dobro dokumentirana in deluje. Vendar je podpora za Terraform v primerjavi z AWS šibka, ker Microsoft gradi poslovne odnose z dobavitelji za izdelavo verižnih primerov postavitve prek Terraform.

Izkušnje naših kolegov:

  * Potem ko smo opravili lastno slepo oceno, smo poiskali izkušnje kolegov. To, kar smo našli, je potrdilo naše izkušnje.

  * Kolegi so poročali o dodatnih težavah s časi gradnje in težavah z uporabo lastnega strežnika za gradnjo. Te težave so občutno hujše od težav z uporabniškim vmesnikom, ker je izvajanje gradenj osnovni namen cevovoda za gradnjo, mi pa pričakujemo, da jih bomo izvedli veliko na dan.

  * Našli smo odlično sodelovanje članov ekipe Azure v razpravnih območjih. Pohvala Microsoftu za to. Še posebej nas je navdušil Edward Thomson, Azure PM in programer, zaradi svojega sodelovanja, neposrednosti in tehničnih razlag.


### Posledice

Izbira Microsoft Azure DevOps bo verjetno dražja (~3-krat) po času in stroških, kot če Azure ne izberemo.


## Povezano


### Povezane odločitve

Če izberemo Azure DevOps, obstaja veliko sorodnih ponudb, vključno z Azure Repo, Azure Pipeline itd. Verjamemo, da nam bo izbira Azure DevOps morda olajšala uporabo več zmožnosti Azure ali pa otežila uporabo zmožnosti drugih dobaviteljev.

Verjamemo, da Microsoft dela velike korake pri izkušnji razvijalcev, in vidimo, da Microsoft izvaja velike prevzeme razvijalskih orodij (npr. GitHub) in odvisnosti (npr. Citus).

Če izberemo Azure DevOps, bomo morda želeli poudariti izbiro ponudb, prevzetih s strani Microsofta, in morda bomo tudi želeli k prevzetim ponudbam pristopiti z več previdnosti/ocenjevanja zaradi možnega zavrnitvenega odziva tkiva (tissue-rejection), npr. tveganja fluktuacije osebja.


### Povezane zahteve

Želimo, da so časi gradnje zelo hitri. Za to sprejemamo plačilo visoke premije. To zato, ker želimo zelo hitro iterirati.

Želimo, da je zanesljivost zelo visoka. Za to sprejemamo plačilo visoke premije. To zato, ker preizkušamo primere uporabe z visoko vrednostjo, vključno s finančnimi transakcijami, zaupnimi transakcijami itd.

Naši štirje najpomembnejši KPI-ji DevOps vključujejo povprečni čas do obnovitve, kar zahteva hitre gradnje in visoko zanesljivost.


### Povezani artefakti

Želimo, da sistem za gradnjo izdaja artefakte, primerne za uporabo v drugih sistemih, kot je Artifactory.


### Povezana načela

Lahko povratljivo. Azure DevOps lahko ovrednotimo vzporedno z obstoječim AWS.


## Opombe


### Microsoft Devops CI: nezadovoljiva dogodivščina

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Objava na blogu.

»Kot razvijalec programske opreme iz prve roke vem, kako težko je hitro in poceni izdelati kakovostne izdelke. Je umetniška oblika, ki nam včasih uspe, drugič pa se sprevrže v nekaj podobnega vladnemu spletnemu mestu za zdravstveno varstvo iz obdobja Obame. Naša raven nadzora nad končnim izdelkom je različna, krivda za neuspeh pa pogosto pade na napačne ljudi v hierarhiji odločanja. Microsoftov Azure DevOps (prej znan kot Visual Studio Team Services) je kljub očitno dobrim namenom popolna nevihta slabih odločitev in slabe izvedbe.«


### Poudarki razprave na Hacker News

https://news.ycombinator.com/item?id=18983586

»Azure DevOps pri svojem delu uporabljamo obsežno in po uporabi GitHuba, Gitlaba, samostojno gostovanih rešitev, Jenkinsa, TeamCityja ... je Azure DevOps na zadnjem mestu.«

»Uporabniški vmesnik je povsod strašno okoren. Najhuje se mi zdijo zahteve za združitev (pull requests). Neverjetno težko je sodelovati z ljudmi pri zahtevi za združitev. Ne morem niti pokazati na »eno« posamezno težavo – pri nas je povsod pokvarjeno.«

»Azure Devops je nekaj, kar bi rad ljubil. Uporabniški vmesnik se nenehno spreminja, vendar ne odpravlja osnovnih hroščev, ki obstajajo že od nekdaj.«

»Orodja niso dobro integrirana, uporabniški vmesnik je zelo počasen, ni pregleda z nadzorno ploščo aktivnih zahtev za združitev, gradenj, izdaj itd. za moje priljubljene repozitorije. Časi gradnje/uvajanja so noro počasni.«

»Poskusili smo uporabiti tudi Azure Boards (delovne postavke, table, zaostanki itd.). Joj. To je popolna zmeda uporabniškega vmesnika z nepovezanimi zamislimi. Namesto da bi eno stvar izvedli dobro, so izvedli dvaducata stvari grozno.«


### Windows Development MVP

Tu Windows Development MVP. Čutim, da moram nositi del odgovornosti za to, ker nisem bil glasnejši glede teh težav. Moram pa reči, da sem razočaran, ko slišim, da ste »presenečeni« nad težavami z UX. Vašim ljudem sem govoril, da je UX grozen (npr. že pred lansiranjem), in vedno znova slišal »vemo, popravljamo«. Začel bom formalizirati povratne informacije in jih potisnil po cevovodih, ostanite z nami. Sem tudi lokalen (Bellevue) in bi z veseljem prišel in poskusil zgraditi cevovod za našo razmeroma preprosto odprtokodno aplikacijo .net/wpf/uwp. Slutim, da bo to odprlo oči nam obema.

Nekaj primerov:

* Cevovoda ni mogoče zgraditi z repozitorijem git, ki vsebuje podmodule

* Urejanje PATH za nekatera orodja po meri se je izkazalo za nemogoče

* Izkušnja Novi cevovod preprosto nima smisla, novi uporabniki, ki klikajo naokoli, bodo sčasoma pristali na napačni dokumentaciji.


### Povzetek Edwarda Thomsona (Azure PM)

Napisal sem kodo, ki združuje vaše zahteve za združitev. Programski vodja (Program Manager) pri Microsoftu za Azure DevOps; prej programski inženir za orodja za nadzor različic pri GitHubu, Microsoftu, SourceGear.

https://www.edwardthomson.com/

Soskrbnik libgit2. https://libgit2.github.io

Sovoditelj All Things Git, podcasta o Gitu. https://www.allthingsgit.com/

Urednik Developer Tools Weekly, glasila o razvojnih orodjih. https://developertoolsweekly.com/
