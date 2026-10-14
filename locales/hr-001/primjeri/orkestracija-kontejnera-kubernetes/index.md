# Zapis arhitekturne odluke: orkestracija kontejnera Kubernetes

## Opis problema 

Moramo odabrati platformu za orkestraciju kontejnera za naš rastući portfelj cloud-native aplikacija. Naša trenutačna naslijeđena implementacija platforme presporo je i nedovoljno agilna da bi pratila naše rastuće potrebe. Tražimo sustav koji će nam omogućiti skaliranje naših usluga na najučinkovitiji mogući način bez kompromisa u agilnosti ili jednostavnosti uporabe.

## Razmatrane alternative

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Donesena odluka

Nakon temeljite analize svake platforme za orkestraciju kontejnera odlučili smo usvojiti Kubernetes kao najbolju opciju za potrebe našeg poduzeća. Naši razlozi za odabir Kubernetesa su sljedeći:

1. **Skalabilnost:**  Kubernetesov jedinstveni dizajn savršen je za skaliranje aplikacija, a kako se naši zahtjevi za skalabilnošću tijekom vremena razvijaju, Kubernetes ima ugrađenu sposobnost odgovoriti na te promjene bez ikakvih problema.

2. **Decentralizirana arhitektura:**  Kubernetesova master-worker topologija osigurava decentraliziranu arhitekturu koja jamči da ne postoji jedinstvena točka otkaza.

3. **Podrška zajednice:**  Kubernetes ima najveću i najaktivniju zajednicu otvorenog koda, što znači da ima velik broj suradnika, programera i dobavljača, zbog čega nam je lakše dobiti pomoć i pronaći resurse.

4. **Podrška ekosustava:**  Kubernetes ima rastući ekosustav s raznim alatima trećih strana, integracijama s registrima kontejnera, CI/CD cjevovodima, pohranom podataka i više.

Stoga smo odlučili usvojiti Kubernetes kao našu platformu za orkestraciju kontejnera za sadašnjost i neposrednu budućnost.

<h6>Izvor: ovu stranicu generirao je ChatGPT, a zatim je uređena radi jasnoće i oblika.</h6>