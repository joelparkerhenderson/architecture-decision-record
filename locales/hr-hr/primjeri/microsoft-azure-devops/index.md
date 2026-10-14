# Microsoft Azure DevOps

Sadržaj:

* [Sažetak](#sažetak)
  * [Problem](#problem)
  * [Odluka](#odluka)
  * [Status](#status)
* [Pojedinosti](#pojedinosti)
  * [Pretpostavke](#pretpostavke)
  * [Ograničenja](#ograničenja)
  * [Pozicije](#pozicije)
  * [Argument](#argument)
  * [Implikacije](#implikacije)
* [Povezano](#povezano)
  * [Povezane odluke](#povezane-odluke)
  * [Povezani zahtjevi](#povezani-zahtjevi)
  * [Povezani artefakti](#povezani-artefakti)
  * [Povezana načela](#povezana-načela)
* [Bilješke](#bilješke)
  * [Microsoft Devops CI: nezadovoljavajuća avantura](#microsoft-devops-ci-nezadovoljavajuća-avantura)
  * [Istaknuto iz rasprave na Hacker Newsu](#istaknuto-iz-rasprave-na-hacker-newsu)
  * [Windows Development MVP](#windows-development-mvp)
  * [Sažetak Edwarda Thomsona (Azure PM)](#sažetak-edwarda-thomsona-azure-pm)


## Sažetak


### Problem

Želimo koristiti devops za izgradnju, integraciju, implementaciju i hosting naših projekata. Razmatramo Microsoft Azure DevOps.

  * Želimo da razvojno iskustvo bude brzo i pouzdano, i pri postavljanju devopsa, npr. konfiguriranju, i pri stalnoj uporabi, npr. brzim vremenima izgradnje.
  
  * Želimo razmotriti korištenje Microsoft Azurea kao cjeline, za hosting aplikacija projekta, baza podataka itd.


### Odluka

Odlučeno protiv Microsoft Azure DevOpsa.


### Status

Odlučeno. Otvoreni smo za ponovno razmatranje ako/kada stignu nove značajne informacije.


## Pojedinosti


### Pretpostavke

Sve uobičajene devops pretpostavke, poput onih iz knjige Accelerate.

  * Brze izgradnje značajna su pomoć. One ubrzavaju petlje povratnih informacija.

  * Možemo mijenjati dijelove od alternativnih dobavljača, tj. možda ćemo htjeti dovesti svoje brže poslužitelje za izgradnju, ili koristiti vlastiti izbor sustava kontrole verzija, ili se koordinirati sa samostalno hostiranim poslužiteljem kontinuirane integracije.
  
  * Pojednostavljena upotrebljivost značajna je pomoć za razvojno iskustvo, a time i za suptilna područja poput dosljednosti, jasnoće, sigurnosti i lakoće krivulje učenja.

  * Kada je nešto pokvareno ili problematično, želimo učinkovit način prijave problema. To je osobito važno za sve probleme povezane sa sigurnošću.


### Ograničenja

Nema poznatih. Azure ima objavljenu obvezu da dobro surađuje s vanjskim alatima.


### Pozicije

Razmatrali smo korištenje Microsoft Azure Devopsa naspram AWS-a, koji je postojeće rješenje.

Eksperimentirali smo s Azure DevOpsom, Azure Pipelinesom, Azure Repom i podizanjem novog poslužitelja u Azureu putem Terraforma.

Eksperimentirali smo s dobivanjem podrške od predstavnika Microsofta.

Prikupljali smo informacije od kolega na blogovima i Hacker Newsu.


### Argument

Azure DevOps oglašava izvrstan skup ponuda, ali one ne drže vodu, ne rade dobro zajedno, a podrška je loša.

Naše izravno iskustvo:

  * Postavljanje Azurea je zbrka UI-jeva, od kojih se neki preklapaju s Microsoftovim računima, a neki ne. Npr. postoji prijava u Azure, prijava na Microsoft.com, prijava na Live.com itd. i svi su istodobno u igri.

  * Naišli smo na manji sigurnosni problem tijekom postavljanja i nismo pronašli rješenje. Pokušali smo ga prijaviti na mnogo načina mnogim predstavnicima Microsofta, bez uspjeha. Uspješno smo ga prijavili Microsoftovu sigurnosnom timu, koji je odgovorio da neće popraviti.

  * Dokumentacija je često ili pogrešna ili zastarjela. Barem dio toga je zbog Microsoftove loše tražilice, a dio zbog ispodprosječnog SEO-a.
  
  * Postavljanje Terraforma dobro je dokumentirano i radi. Međutim, podrška za Terraform je slaba u usporedbi s AWS-om jer Microsoft gradi poslovne odnose s dobavljačima kako bi stvarali primjere postavljanja kroz Terraform u lancu.

Iskustva kolega:

  * Nakon što smo napravili vlastitu slijepu procjenu, potražili smo iskustva kolega. Ono što smo pronašli potvrdilo je naša iskustva.

  * Kolege su izvijestile o dodatnim problemima s vremenima izgradnje i problemima s poslužiteljem za izgradnju koji sami donosite (bring-your-own). Ti su problemi znatno ozbiljniji od problema s UI-jem jer je izvođenje izgradnji temeljna svrha cjevovoda izgradnje, a očekujemo da ćemo ih raditi mnogo dnevno.

  * Pronašli smo izvrsno sudjelovanje kolega iz Azurea u područjima rasprave. Pohvale Microsoftu na tome. Posebno nas je dojmio Edward Thomson, PM i programer u Azureu, zbog svog sudjelovanja, izravnosti i tehničkih objašnjenja.


### Implikacije

Odabir Microsoft Azure DevOpsa vjerojatno će biti skuplji (~3x) u vremenu i trošku nego neodabir Azurea.


## Povezano


### Povezane odluke

Ako odaberemo Azure DevOps, postoje mnoge povezane ponude, uključujući Azure Repo, Azure Pipeline itd. Vjerujemo da nam, ako odaberemo Azure Devops, to može olakšati korištenje više mogućnosti Azurea ili otežati korištenje mogućnosti drugih dobavljača.

Vjerujemo da Microsoft čini velike korake u razvojnom iskustvu i vidimo da Microsoft obavlja velika preuzimanja razvojnih alata (npr. GitHub) i ovisnosti (npr. Citus).

Ako odaberemo Azure DevOps, možda ćemo htjeti naglasiti odabir ponuda iz Microsoftovih preuzimanja, a možda ćemo ponudama iz preuzimanja htjeti pristupiti s većim oprezom/procjenom zbog potencijalnog odbacivanja tkiva, npr. rizika fluktuacije osoblja.


### Povezani zahtjevi

Želimo da vremena izgradnje budu vrlo brza. Prihvaćamo plaćanje visoke premije za to. To je zato što želimo iterirati vrlo brzo.

Želimo vrlo visoku pouzdanost. Prihvaćamo plaćanje visoke premije za to. To je zato što testiramo slučajeve uporabe visoke vrijednosti, uključujući financijske transakcije, povjerljive transakcije itd.

Naša 4 najvažnija devops KPI-ja uključuju srednje vrijeme oporavka, što zahtijeva brze izgradnje i visoku pouzdanost.


### Povezani artefakti

Želimo da sustav izgradnje proizvodi artefakte prikladne za korištenje u drugim sustavima, poput Artifactoryja.


### Povezana načela

Lako reverzibilno. Azure DevOps možemo vrednovati paralelno s postojećim AWS-om.


## Bilješke


### Microsoft Devops CI: nezadovoljavajuća avantura

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Blog objava.

„Kao softverski programer iz prve ruke znam koliko je teško brzo i jeftino izgraditi kvalitetne proizvode. To je umjetnost koja nam ponekad uspije, a drugi put se pretvori u nešto slično vladinoj zdravstvenoj web stranici iz Obaminih vremena. Naša razina kontrole nad nastalim proizvodom varira, a krivnja za neuspjeh često pada na pogrešne ljude u hijerarhiji odlučivanja. Microsoftov Azure DevOps (prije poznat kao Visual Studio Team Services), unatoč očito dobrim namjerama, savršena je oluja loših odluka i slabog izvođenja.“


### Istaknuto iz rasprave na Hacker Newsu

https://news.ycombinator.com/item?id=18983586

„Na poslu intenzivno koristimo Azure DevOps i, nakon što sam koristio GitHub, Gitlab, samostalno hostirana rješenja, Jenkins, TeamCity... Azure DevOps rangira potpuno posljednji.“

„UI je svugdje užasno nespretan. Najgori su za mene pull requestovi. Nevjerojatno je teško raditi s ljudima na pull requestu. Ne mogu vam čak ni pokazati „jedan“ određeni problem – kod nas je pokvareno svugdje.“

„Azure Devops je nešto što želim voljeti. UI se stalno mijenja, ali ne popravlja temeljne bugove koji postoje godinama.“

„Alati nisu dobro integrirani, UI je stvarno spor, nema pregleda nadzorne ploče aktivnih pull requestova, izgradnji, izdanja itd. za moje omiljene repozitorije. Vremena izgradnje/implementacije su suludo spora.“

„Pokušali smo koristiti i Azure Boards (Work Items, Boards, Backlogs itd.). Au. To je potpuna zbrka UI-ja nepovezanih ideja. Umjesto da dobro implementiraju jednu stvar, užasno su implementirali dvadeset četiri stvari.“


### Windows Development MVP

Ja sam Windows Development MVP. Osjećam da moram preuzeti dio odgovornosti što o tim problemima nisam govorio glasnije. Ali moram reći da sam razočaran što čujem da ste „iznenađeni“ problemima s UX-om. Govorim vašim ljudima da je UX užasan (npr. još prije lansiranja) i stalno sam čuo „znamo, popravljamo“. Počet ću formalizirati povratne informacije i provoditi ih kroz cijevi, ostanite u toku. Također sam lokalni (Bellevue), rado bih došao i pokušao napraviti cjevovod za našu relativno jednostavnu oss .net/wpf/uwp aplikaciju. Sumnjam da će to biti otkrovenje za obje strane.

Neki primjeri:

* Ne možete izgraditi cjevovod s git repozitorijem koji sadrži podmodule

* Utvrdio sam da je nemoguće urediti PATH za neke prilagođene alate

* Novo iskustvo cjevovoda jednostavno nema mnogo smisla, novi korisnici koji klikću okolo na kraju će završiti na pogrešnoj dokumentaciji.


### Sažetak Edwarda Thomsona (Azure PM)

Napisao sam kod koji spaja vaše pull requestove. Program Manager u Microsoftu za Azure DevOps; prije softverski inženjer na alatima kontrole verzija u GitHubu, Microsoftu, SourceGearu.

https://www.edwardthomson.com/

Su-održavatelj libgit2. https://libgit2.github.io

Su-voditelj All Things Git, podcasta o Gitu. https://www.allthingsgit.com/

Urednik Developer Tools Weekly, biltena o razvojnim alatima. https://developertoolsweekly.com/
