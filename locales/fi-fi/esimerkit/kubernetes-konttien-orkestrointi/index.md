# Arkkitehtuuripäätöstietue: Kubernetes-konttien orkestrointi

## Ongelmanasettelu 

Meidän on valittava konttien orkestrointialusta kasvavalle pilvinatiivien sovellustemme salkulle. Nykyinen vanha alustamme on käyttöönotoltaan liian hidas eikä riittävän ketterä pysyäkseen kasvavien tarpeidemme mukana. Etsimme järjestelmää, jonka avulla voimme skaalata palvelujamme mahdollisimman tehokkaalla tavalla tinkimättä ketteryydestä tai käytön helppoudesta.

## Harkitut vaihtoehdot

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Tehty päätös

Jokaisen konttien orkestrointialustan perusteellisen analyysin jälkeen olemme päättäneet ottaa Kubernetesin käyttöön parhaana vaihtoehtona yritystarpeisiimme. Syymme valita Kubernetes ovat seuraavat:

1. **Skaalautuvuus:**  Kubernetesin ainutlaatuinen rakenne sopii täydellisesti sovellusten skaalaamiseen, ja skaalautuvuusvaatimustemme kehittyessä ajan myötä Kubernetesilla on sisäänrakennettu kyky vastata näihin muutoksiin ongelmitta.

2. **Hajautettu arkkitehtuuri:**  Kubernetesin isäntä–työläinen-topologia varmistaa hajautetun arkkitehtuurin, jossa ei ole yhtä vikaantumispistettä.

3. **Yhteisön tuki:**  Kubernetesilla on suurin ja aktiivisin avoimen lähdekoodin yhteisö, mikä tarkoittaa suurta määrää osallistujia, kehittäjiä ja toimittajia, ja se helpottaa avun ja resurssien löytämistä.

4. **Ekosysteemin tuki:**  Kubernetesilla on kasvava ekosysteemi, jossa on erilaisia kolmannen osapuolen työkaluja, integraatioita konttirekistereihin, CI/CD-putkiin, tietojen tallennukseen ja muuhun.

Siksi olemme päättäneet ottaa Kubernetesin käyttöön konttien orkestrointialustanamme nykyhetkeksi ja lähitulevaisuudeksi.

<h6>Kunnianosoitus: tämän sivun on luonut ChatGPT, minkä jälkeen sitä on muokattu selkeyden ja muodon vuoksi.</h6>
