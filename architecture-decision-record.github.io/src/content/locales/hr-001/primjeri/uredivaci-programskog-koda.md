# Zapis arhitekturne odluke: uređivači programskog koda

## Kontekst

Uređivači programskog koda ključan su alat za programere za pisanje i uređivanje koda. Dostupni su brojni uređivači koda, svaki sa svojim skupom značajki, prednosti i nedostataka. Svrha ovog ADR-a je dokumentirati arhitekturne odluke donesene za uređivače programskog koda.

## Prioriteti

Arhitektura uređivača programskog koda trebala bi davati prednost sljedećem:

* **Modularnost**: Uređivač koda trebao bi biti dizajniran modularno, omogućujući programerima da ga prilagode i prošire prema potrebi. To omogućuje fleksibilnu arhitekturu koja se može prilagoditi potrebama različitih programera i timova.

* **Performanse**: Uređivač koda trebao bi biti performantan i brzo reagirati, omogućujući programerima da rade učinkovito bez usporavanja alatom koji koriste.

* **Korisničko sučelje**: Korisničko sučelje trebalo bi biti intuitivno i jednostavno za uporabu, omogućujući programerima da se usredotoče na svoj kod umjesto da se bore s uređivačem.

* **Proširivost**: Uređivač koda trebao bi biti dizajniran tako da omogućuje jednostavno proširenje dodacima i integracijama trećih strana.

* **Kompatibilnost**: Uređivač koda trebao bi biti kompatibilan sa širokim rasponom programskih jezika i tehnologija, što ga čini korisnim alatom za širok krug programera.

## Odluka

Na temelju tih prioriteta arhitektura uređivača programskog koda trebala bi biti dizajnirana sa sljedećim komponentama:

* **Jezgra**: Ova komponenta pruža osnovnu funkcionalnost uređivača koda, poput isticanja sintakse, uređivanja teksta i upravljanja datotekama.

* **UI**: Ova komponenta pruža korisničko sučelje uređivača koda, uključujući izbornike, alatne trake i tipkovničke prečace.

* **Dodaci**: Ova komponenta omogućuje programerima da prošire funkcionalnost uređivača koda instaliranjem dodataka trećih strana. Dodaci mogu pružati dodatne značajke, poput dovršavanja koda, lintanja ili otklanjanja pogrešaka.

* **Integracije**: Ova komponenta omogućuje uređivaču koda integraciju s drugim alatima i tehnologijama, poput sustava za kontrolu verzija, sustava za izgradnju ili alata za otklanjanje pogrešaka.

## Obrazloženje

Modularnost uređivača koda omogućuje programerima da ga prilagode i prošire prema potrebi. To je važno jer različiti programeri i timovi imaju različite potrebe i tijekove rada, a fleksibilna arhitektura može prihvatiti te razlike.

* **Performanse**: ključne jer programeri moraju moći raditi učinkovito bez usporavanja svojim alatima. Performantan uređivač koda nužan je za produktivnost i može pomoći programerima da zadrže fokus i koncentraciju.

* **UI**: važan jer omogućuje programerima da se usredotoče na svoj kod umjesto da se bore s uređivačem. To može dovesti do bolje produktivnosti i manje frustracije programera.

* **Proširivost**: moćna jer omogućuje prilagodbu uređivača koda različitim potrebama i tijekovima rada. Dodaci i integracije trećih strana mogu pružiti dodatne značajke i mogućnosti koje nisu uključene u osnovni uređivač.

* **Kompatibilnost**: vrijedna jer omogućuje korištenje uređivača koda sa širokim rasponom programskih jezika i tehnologija. To uređivač čini korisnijim alatom za širok krug programera.

Komponente jezgre, dodataka, integracija i UI-ja pružaju jasno razdvajanje odgovornosti i omogućuju modularnu arhitekturu koja se lako može proširivati i prilagođavati. Ta je arhitektura fleksibilna, performantna i kompatibilna sa širokim rasponom programskih jezika i tehnologija, što je čini korisnim alatom za programere.