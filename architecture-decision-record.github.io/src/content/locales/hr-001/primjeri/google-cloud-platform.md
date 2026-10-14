# Zapis arhitekturne odluke za Google Cloud Platform

## Kontekst

Google Cloud Platform (GCP) istaknuta je platforma za računalstvo u oblaku koja nudi razne cloud usluge, uključujući rješenja za računanje, pohranu i umrežavanje. Ovaj ADR ima za cilj dokumentirati arhitekturne odluke donesene za razvoj i implementaciju infrastrukture temeljene na GCP-u za našu organizaciju.

## Odluka

Naša je organizacija odlučila koristiti Google Cloud Platform kao cloud infrastrukturu za našu aplikaciju. Primarna razmatranja za ovu odluku su:

   - Isplativost

   - Skalabilnost

   - Pouzdanost

   - Fleksibilnost

## Odabiri

Sljedeće usluge iz GCP-a odabrane su kako bi zadovoljile naše zahtjeve:

   - Compute Engine za virtualne strojeve i računalne resurse

   - Cloud Storage za objektnu pohranu i hosting datoteka

   - Cloud SQL za upravljanu uslugu baze podataka

   - Firebase za razvoj i hosting aplikacija

## Obrazloženje

   - Isplativost: Google Cloud Platform vrlo je isplativ u usporedbi s drugim cloud platformama, što ga čini privlačnom opcijom za organizacije s proračunskim ograničenjima.

   - Skalabilnost: Infrastruktura GCP-a koja se lako skalira omogućuje obradu bilo koje količine prometa u stvarnom vremenu.

   - Pouzdanost: Upravljane usluge GCP-a nude visoku pouzdanost, s automatiziranim sigurnosnim kopijama i mogućnostima oporavka od katastrofe koje osiguravaju visoku dostupnost resursa i podataka.

   - Fleksibilnost: Platforma pruža razne alate i usluge u različitim domenama poput umjetne inteligencije, analitike podataka i IoT-a, što je čini vrlo svestranom.

## Posljedice

Migracija na Google Cloud Platform zahtijevat će obuku naših timova o uslugama GCP-a, ponovno arhitekturiranje aplikacije kako bi bila kompatibilna s odabranim uslugama i ažuriranje koda infrastrukture za podršku uslugama GCP-a. Međutim, očekuje se da ćemo nakon dovršetka migracije imati vrlo skalabilnu, pouzdanu i isplativu infrastrukturu za hosting naše aplikacije. Također ćemo morati upravljati tekućim troškovima osiguravanja resursa na GCP-u.

## Zaključak

Google Cloud Platform izvrstan je izbor za našu cloud infrastrukturu zbog svoje isplativosti, skalabilnosti, pouzdanosti i fleksibilnosti. Korištenjem odabranih usluga možemo pružiti vrlo dostupnu i robusnu infrastrukturu za našu aplikaciju.