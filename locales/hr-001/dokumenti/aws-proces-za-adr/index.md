# AWS-ov proces zapisa arhitekturnih odluka

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Zapis arhitekturne odluke (ADR) je dokument koji opisuje izbor koji tim donosi o značajnom aspektu softverske arhitekture koju planira izgraditi. Svaki ADR opisuje arhitekturnu odluku, njezin kontekst i njezine posljedice. ADR-ovi imaju stanja i stoga slijede životni ciklus. Za primjer ADR-a pogledajte dodatak.

Proces ADR-a rezultira zbirkom zapisa arhitekturnih odluka. Ta zbirka čini dnevnik odluka. Dnevnik odluka pruža kontekst projekta kao i detaljne informacije o implementaciji i dizajnu. Članovi projekta prelistavaju naslove svakog ADR-a kako bi dobili pregled konteksta projekta. Čitaju ADR-ove kako bi se detaljno upoznali s implementacijama projekta i odabirima dizajna.

Kada tim prihvati ADR, on postaje nepromjenjiv. Ako nova saznanja zahtijevaju drukčiju odluku, tim predlaže novi ADR. Kada tim prihvati novi ADR, on zamjenjuje prethodni ADR.

## Opseg procesa ADR-a

Članovi projekta trebali bi stvoriti ADR za svaku arhitekturno značajnu odluku koja utječe na softverski projekt ili proizvod, uključujući sljedeće (Richards and Ford 2020):

* Struktura (na primjer, obrasci kao što su mikroservisi)

* Nefunkcionalni zahtjevi (sigurnost, visoka dostupnost i otpornost na pogreške)

* Ovisnosti (povezanost komponenti)

* Sučelja (API-ji i objavljeni ugovori)

* Tehnike izgradnje (biblioteke, okviri, alati i procesi)

* Funkcionalni i nefunkcionalni zahtjevi najčešći su ulazi u proces ADR-a.


## Sadržaj ADR-a

Kada tim utvrdi potrebu za ADR-om, član tima počinje pisati ADR na temelju predloška za cijeli projekt. (Pogledajte organizaciju ADR na GitHubu za primjere predložaka.) Predložak pojednostavljuje stvaranje ADR-a i osigurava da ADR obuhvaća sve relevantne informacije. U najmanju ruku, svaki ADR trebao bi definirati kontekst odluke, samu odluku i posljedice odluke za projekt i njegove isporučevine. (Za primjere tih odjeljaka pogledajte dodatak.) Jedan od najmoćnijih aspekata strukture ADR-a je to što se usredotočuje na razlog odluke, a ne na to kako ju je tim implementirao. Razumijevanje zašto je tim donio odluku olakšava ostalim članovima tima da je prihvate i sprječava druge arhitekte koji nisu sudjelovali u procesu donošenja odluka da tu odluku ubuduće nadjačaju.


## Proces usvajanja ADR-a

Svaki član tima može stvoriti ADR, ali tim bi trebao uspostaviti definiciju vlasništva nad ADR-om. Svaki autor koji je vlasnik ADR-a trebao bi aktivno održavati i komunicirati sadržaj ADR-a. Kako bi pojasnio to vlasništvo, ovaj vodič u sljedećim odjeljcima autore ADR-a naziva vlasnicima ADR-a. Ostali članovi tima uvijek mogu doprinijeti ADR-u. Ako se sadržaj ADR-a promijeni prije nego što ga tim prihvati, vlasnik bi trebao odobriti te promjene.

Nakon što tim utvrdi arhitekturnu odluku i njezina vlasnika, vlasnik ADR-a na početku procesa dostavlja ADR u stanju **Predloženo**. ADR-ovi u stanju Predloženo spremni su za pregled.

Vlasnik ADR-a zatim pokreće proces pregleda ADR-a. Cilj procesa pregleda ADR-a je odlučiti hoće li tim prihvatiti ADR, utvrditi da je potrebna dorada ili odbiti ADR. Projektni tim, uključujući vlasnika, pregledava ADR. Sastanak za pregled trebao bi započeti namjenskim terminom za čitanje ADR-a. U prosjeku bi trebalo biti dovoljno 10 do 15 minuta. Tijekom tog vremena svaki član tima čita dokument i dodaje komentare i pitanja kako bi označio nejasne teme. Nakon faze pregleda vlasnik ADR-a čita naglas i raspravlja o svakom komentaru s timom.

Ako tim pronađe točke djelovanja za poboljšanje ADR-a, stanje ADR-a ostaje **Predloženo**. Vlasnik ADR-a formulira radnje i, u suradnji s timom, dodjeljuje izvršitelja svakoj radnji. Svaki član tima može doprinijeti i riješiti točke djelovanja. Odgovornost je vlasnika ADR-a ponovno zakazati proces pregleda.

Tim također može odlučiti odbiti ADR. U tom slučaju vlasnik ADR-a dodaje razlog odbijanja kako bi se spriječile buduće rasprave o istoj temi. Vlasnik mijenja stanje ADR-a u **Odbijeno**.

Ako tim odobri ADR, vlasnik dodaje vremensku oznaku, verziju i popis dionika. Vlasnik zatim ažurira stanje u **Prihvaćeno**.

ADR-ovi i dnevnik odluka koji oni stvaraju predstavljaju odluke koje je donio tim i pružaju povijest svih odluka. Tim koristi ADR-ove kao referencu tijekom pregleda koda i arhitekture gdje je to moguće. Osim provođenja pregleda koda, dizajnerskih zadataka i implementacijskih zadataka, članovi tima trebali bi se konzultirati s ADR-ovima za strateške odluke o proizvodu.

Kao dobra praksa, svaka softverska promjena trebala bi proći kroz recenzije kolega i zahtijevati barem jedno odobrenje. Tijekom pregleda koda recenzent može pronaći promjene koje krše jedan ili više ADR-ova. U tom slučaju recenzent traži od autora promjene koda da ažurira kod i dijeli poveznicu na ADR. Kada autor ažurira kod, recenzenti kolege ga odobravaju i spaja se u glavnu bazu koda.


## Proces pregleda ADR-a

Tim bi ADR-ove trebao tretirati kao nepromjenjive dokumente nakon što ih prihvati ili odbije. Promjene postojećeg ADR-a zahtijevaju stvaranje novog ADR-a, uspostavljanje procesa pregleda za novi ADR i odobravanje ADR-a. Ako tim odobri novi ADR, vlasnik bi trebao promijeniti stanje starog ADR-a u **Zamijenjeno**. 
