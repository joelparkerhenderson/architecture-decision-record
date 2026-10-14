# Zapis arhitekturne odluke: orkestracija kontejnera Docker Swarm

Broj odluke: 001

Donositelj odluke: [Vaše ime ili položaj]

Datum: [Datum odluke]

## Kontekst

Razmatramo različite alate za orkestraciju kontejnera za upravljanje našom arhitekturom temeljenom na mikroservisima. Vrednovali smo različita rješenja poput Kubernetesa, Docker Swarma i Mesosphere DC/OS. Ipak, odlučili smo se usredotočiti na Docker Swarm zbog njegove jednostavnosti, integracije s Dockerom i ugrađenog uravnoteživanja opterećenja.

## Odluka

Odlučili smo koristiti Docker Swarm kao naš alat za orkestraciju kontejnera. Docker Swarm pruža jednostavan i intuitivan način upravljanja kontejneriziranim aplikacijama u klasteru čvorova. Također nam omogućuje iskorištavanje naših postojećih tijekova rada i infrastrukture temeljenih na Dockeru. S Docker Swarmom možemo jednostavno implementirati, skalirati i upravljati svojim aplikacijama, a pritom iskoristiti ugrađeno uravnoteživanje opterećenja.

## Prednosti

- **Jednostavnost:**  Docker Swarm slijedi ista načela kao Docker, pa nema potrebe za učenjem nove tehnologije. Krivulja učenja relativno je plitka za programere koji poznaju Docker.

- **Integracija:**  Docker Swarm besprijekorno se integrira s Dockerovim alatima, poput Docker Composea, što olakšava upravljanje svim našim kontejnerima i uslugama s jednog mjesta.

- **Uravnoteživanje opterećenja:**  Docker Swarm pruža ugrađeno uravnoteživanje opterećenja, osiguravajući da su naše aplikacije uvijek dostupne i ravnomjerno raspoređene po klasteru.

- **Skalabilnost:**  Docker Swarm olakšava horizontalno skaliranje naših aplikacija dodavanjem ili uklanjanjem čvorova iz klastera.

- **Visoka dostupnost:**  Docker Swarm automatski distribuira naše usluge po čvorovima, pružajući visoku dostupnost u slučaju otkaza čvora.

## Rizici

- **Ograničena funkcionalnost:**  Docker Swarmu mogu nedostajati neke napredne značajke koje se nalaze u Kubernetesu ili Mesosphere DC/OS-u, poput automatskog skaliranja ili samoizlječenja.

- **Usmjerenost na Docker:**  Docker Swarm čvrsto je povezan s Dockerom, što može ograničiti našu fleksibilnost ako ikada budemo trebali odmaknuti se od rješenja temeljenih na Dockeru.

- **Nezrelost:**  Docker Swarm je još uvijek relativno nova tehnologija i mogu postojati problemi sa stabilnošću ili praznine u dokumentaciji.

## Alternative

- **Kubernetes:**  Kubernetes je najšire korištena platforma za orkestraciju kontejnera i pruža napredne značajke te zreliji ekosustav. Međutim, ima strmiju krivulju učenja i mogao bi biti prekomjeran za naše potrebe.

- **Mesosphere DC/OS:**  Mesosphere DC/OS je moćan alat koji pruža napredne značajke poput podrške za više clouda te izvornih mogućnosti platforme za velike podatke i umjetnu inteligenciju. Međutim, zahtijeva znatnu stručnost za implementaciju i mogao bi biti previše složen za naše zahtjeve.

## Zaključak

Nakon pažljivog razmatranja odlučili smo koristiti Docker Swarm kao naš alat za orkestraciju kontejnera. Docker Swarm pruža jednostavnost, integraciju i ugrađeno uravnoteživanje opterećenja koji su nam potrebni za upravljanje kontejneriziranim aplikacijama. Iako mu možda nedostaju neke napredne značajke, vjerujemo da koristi Docker Swarma nadmašuju njegove rizike za naše trenutačne zahtjeve.

<h6>Izvor: ovu stranicu generirao je ChatGPT, a zatim je uređena radi jasnoće i oblika.</h6>