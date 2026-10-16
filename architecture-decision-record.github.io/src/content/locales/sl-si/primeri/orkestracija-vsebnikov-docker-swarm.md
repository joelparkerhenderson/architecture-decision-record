# Zapis arhitekturne odločitve: orkestracija vsebnikov Docker Swarm

Številka odločitve: 001

Odločevalec: [Vaše ime ali položaj]

Datum: [Datum odločitve]

## Kontekst

Preučujemo različna orodja za orkestracijo vsebnikov za upravljanje naše arhitekture, ki temelji na mikrostoritvah. Ovrednotili smo različne rešitve, kot so Kubernetes, Docker Swarm in Mesosphere DC/OS. Vendar smo se odločili osredotočiti na Docker Swarm zaradi njegove preprostosti, integracije z Dockerjem in vgrajenega uravnoteženja obremenitve.

## Odločitev

Odločili smo se, da bomo kot orodje za orkestracijo vsebnikov uporabljali Docker Swarm. Docker Swarm zagotavlja preprost in intuitiven način upravljanja vsebniških aplikacij po gruči vozlišč. Omogoča nam tudi izkoriščanje obstoječih potekov dela in infrastrukture, ki temeljijo na Dockerju. Z Docker Swarm lahko preprosto uvajamo, skaliramo in upravljamo svoje aplikacije, pri tem pa izkoriščamo vgrajeno uravnoteženje obremenitve.

## Prednosti

- **Preprostost:**  Docker Swarm sledi enakim načelom kot Docker, zato se ni treba učiti nove tehnologije. Krivulja učenja je za razvijalce, ki poznajo Docker, razmeroma ploska.

- **Integracija:**  Docker Swarm se brezhibno integrira z orodji Docker, kot je Docker Compose, zato je upravljanje vseh naših vsebnikov in storitev z enega mesta lažje.

- **Uravnoteženje obremenitve:**  Docker Swarm zagotavlja vgrajeno uravnoteženje obremenitve, ki zagotavlja, da so naše aplikacije vedno razpoložljive in enakomerno porazdeljene po gruči.

- **Razširljivost:**  Docker Swarm omogoča preprosto vodoravno skaliranje naših aplikacij z dodajanjem ali odstranjevanjem vozlišč iz gruče.

- **Visoka razpoložljivost:**  Docker Swarm samodejno porazdeli naše storitve po vozliščih, kar zagotavlja visoko razpoložljivost v primeru odpovedi vozlišča.

## Tveganja

- **Omejena funkcionalnost:**  Docker Swarm morda nima nekaterih naprednih funkcij, ki jih najdemo v Kubernetes ali Mesosphere DC/OS, kot sta samodejno skaliranje ali samozdravljenje.

- **Osredotočenost na Docker:**  Docker Swarm je tesno povezan z Dockerjem, kar lahko omeji našo prilagodljivost, če bi se kdaj morali odmakniti od rešitev, ki temeljijo na Dockerju.

- **Nezrelost:**  Docker Swarm je še vedno razmeroma nova tehnologija, zato lahko pride do težav s stabilnostjo ali vrzeli v dokumentaciji.

## Alternative

- **Kubernetes:**  Kubernetes je najpogosteje uporabljana platforma za orkestracijo vsebnikov in ponuja napredne funkcije ter zrelejši ekosistem. Vendar ima strmejšo krivuljo učenja in je lahko za naše potrebe pretirano.

- **Mesosphere DC/OS:**  Mesosphere DC/OS je zmogljivo orodje, ki ponuja napredne funkcije, kot sta podpora za več oblakov in izvorne zmožnosti platforme za velike podatke in umetno inteligenco. Vendar zahteva precej strokovnega znanja za izvedbo in je za naše zahteve morda prezapleteno.

## Sklep

Po skrbnem premisleku smo se odločili, da bomo kot orodje za orkestracijo vsebnikov uporabljali Docker Swarm. Docker Swarm zagotavlja preprostost, integracijo in vgrajeno uravnoteženje obremenitve, ki jih potrebujemo za upravljanje svojih vsebniških aplikacij. Čeprav morda nima nekaterih naprednih funkcij, verjamemo, da koristi Docker Swarm odtehtajo njegova tveganja za naše trenutne zahteve.

<h6>Zasluge: to stran je ustvaril ChatGPT, nato pa je bila urejena zaradi jasnosti in oblike.</h6>