# Predložak zapisa odluke – Jeff Tyree i Art Akerman

Ovo je predložak opisa arhitekturne odluke objavljen u ["Architecture Decisions: Demystifying Architecture" Jeffa Tyreea i Arta Akermana, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Problem**: Opišite problem arhitekturnog dizajna koji rješavate, ne ostavljajući nikakvih pitanja o tome zašto ga rješavate baš sada. Slijedeći minimalistički pristup, obradite i dokumentirajte samo probleme koje je potrebno riješiti u različitim točkama životnog ciklusa.

* **Odluka**: Jasno navedite smjer arhitekture – to jest, poziciju koju ste odabrali.

* **Status**: Status odluke, primjerice na čekanju, donesena ili odobrena.

* **Grupa**: Možete koristiti jednostavno grupiranje – poput integracije, prezentacije, podataka itd. – kako biste pomogli organizirati skup odluka. Možete koristiti i sofisticiraniju arhitekturnu ontologiju, poput one Johna Kyaruzija i Jana van Katwijka, koja uključuje apstraktnije kategorije kao što su događaj, kalendar i lokacija. Na primjer, koristeći tu ontologiju, odluke koje se bave događajima u kojima sustav zahtijeva informacije grupirali biste pod događaj.

* **Pretpostavke**: Jasno opišite temeljne pretpostavke u okruženju u kojem donosite odluku – trošak, raspored, tehnologija itd. Imajte na umu da ograničenja okruženja (poput prihvaćenih tehnoloških standarda, arhitekture poduzeća, često korištenih obrazaca itd.) mogu ograničiti alternative koje razmatrate.

* **Ograničenja**: Zabilježite sva dodatna ograničenja okruženju koja bi odabrana alternativa (odluka) mogla nametnuti.

* **Pozicije**: Navedite pozicije (održive opcije ili alternative) koje ste razmatrali. One često zahtijevaju duga objašnjenja, ponekad čak modele i dijagrame. Ovo nije iscrpan popis. Međutim, ne želite čuti pitanje „Jeste li razmislili o...?“ tijekom završnog pregleda; to dovodi do gubitka vjerodostojnosti i dovođenja u pitanje drugih arhitekturnih odluka. Ovaj odjeljak također pomaže osigurati da ste čuli tuđa mišljenja; eksplicitno navođenje drugih mišljenja pomaže pridobiti njihove zagovornike za vašu odluku.

* **Argument**: Opišite zašto ste odabrali poziciju, uključujući stavke kao što su trošak implementacije, ukupni trošak vlasništva, vrijeme izlaska na tržište i dostupnost potrebnih razvojnih resursa. To je vjerojatno jednako važno kao i sama odluka.

* **Implikacije**: Odluka dolazi s mnogim implikacijama, kako označava metamodel REMAP. Na primjer, odluka može uvesti potrebu za donošenjem drugih odluka, stvoriti nove zahtjeve ili izmijeniti postojeće zahtjeve; nametnuti dodatna ograničenja okruženju; zahtijevati ponovno pregovaranje o opsegu ili rasporedu s klijentima; ili zahtijevati dodatnu obuku osoblja. Jasno razumijevanje i navođenje implikacija vaše odluke može biti vrlo učinkovito u dobivanju podrške i stvaranju plana za izvršenje arhitekture.

* **Povezane odluke**: Očito je da su mnoge odluke povezane; možete ih ovdje navesti. Međutim, utvrdili smo da su u praksi korisniji matrica sljedivosti, stabla odluka ili metamodeli. Metamodeli su korisni za dijagramski prikaz složenih odnosa (kao što su Rose modeli).

* **Povezani zahtjevi**: Odluke bi trebale biti vođene poslovanjem. Kako biste pokazali odgovornost, eksplicitno preslikajte svoje odluke na ciljeve ili zahtjeve. Ove povezane zahtjeve možete nabrojiti ovdje, ali utvrdili smo da je prikladnije pozivati se na matricu sljedivosti. Možete procijeniti doprinos svake arhitekturne odluke ispunjavanju svakog zahtjeva, a zatim procijeniti koliko je dobro zahtjev ispunjen kroz sve odluke. Ako odluka ne doprinosi ispunjavanju zahtjeva, nemojte donositi tu odluku.

* **Povezani artefakti**: Navedite povezane dokumente arhitekture, dizajna ili opsega na koje ova odluka utječe.

* **Povezana načela**: Ako poduzeće ima dogovoren skup načela, pobrinite se da je odluka dosljedna s jednim ili više njih. To pomaže osigurati usklađenost među domenama ili sustavima.

* **Bilješke**: Budući da proces donošenja odluka može trajati tjednima, utvrdili smo da je korisno bilježiti napomene i probleme o kojima tim raspravlja tijekom procesa socijalizacije.
