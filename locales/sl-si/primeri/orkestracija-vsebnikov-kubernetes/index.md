# Zapis arhitekturne odločitve: orkestracija vsebnikov Kubernetes

## Izjava o problemu 

Za naš rastoči portfelj oblačno izvornih aplikacij moramo izbrati platformo za orkestracijo vsebnikov. Naše trenutno podedovano uvajanje na platformi je prepočasno in premalo agilno, da bi sledilo našim rastočim potrebam. Iščemo sistem, ki nam bo omogočil najučinkovitejše skaliranje naših storitev, ne da bi pri tem žrtvovali agilnost ali enostavnost uporabe.

## Preučene alternative

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Sprejeta odločitev

Po temeljiti analizi vsake platforme za orkestracijo vsebnikov smo se odločili, da kot najboljšo možnost za potrebe našega podjetja uvedemo Kubernetes. Razlogi za izbiro Kubernetes so naslednji:

1. **Razširljivost:**  Edinstvena zasnova Kubernetes je odlična za skaliranje aplikacij, in ko se bodo naše zahteve glede razširljivosti sčasoma razvijale, ima Kubernetes vgrajeno zmožnost, da se brez težav odzove na te spremembe.

2. **Decentralizirana arhitektura:**  Topologija glavno vozlišče–delavec (master-worker) v Kubernetes zagotavlja decentralizirano arhitekturo, ki zagotavlja, da ni enotne točke odpovedi.

3. **Podpora skupnosti:**  Kubernetes ima največjo in najbolj dejavno odprtokodno skupnost, kar pomeni, da ima veliko prispevnikov, razvijalcev in ponudnikov, zaradi česar lažje dobimo pomoč in najdemo vire.

4. **Podpora ekosistema:**  Kubernetes ima rastoč ekosistem z različnimi orodji tretjih oseb, integracijami z registri vsebnikov, cevovodi CI/CD, shranjevanjem podatkov in drugim.

Zato smo se odločili, da Kubernetes uvedemo kot svojo platformo za orkestracijo vsebnikov za zdaj in bližnjo prihodnost.

<h6>Zasluge: to stran je ustvaril ChatGPT, nato pa je bila urejena zaradi jasnosti in oblike.</h6>
