# Rekord ta' deċiżjoni arkitettonika: orkestrazzjoni tal-kontenituri Kubernetes

## Dikjarazzjoni tal-problema 

Neħtieġu nagħżlu pjattaforma ta' orkestrazzjoni tal-kontenituri għall-portafoll tagħna ta' applikazzjonijiet cloud-native li qed jikber. Id-deployment attwali tal-pjattaforma legacy tagħna huwa bil-mod wisq, u mhux agile biżżejjed biex iżomm ritmu mal-ħtiġijiet tagħna li qed jiżdiedu. Qed infittxu sistema li tippermettilna niskalaw is-servizzi tagħna bl-aktar mod effiċjenti possibbli mingħajr ma nikkompromettu l-agilità jew il-faċilità tal-użu.

## Alternattivi kkunsidrati

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Deċiżjoni meħuda

Wara analiżi bir-reqqa ta' kull pjattaforma ta' orkestrazzjoni tal-kontenituri, iddeċidejna li nadottaw Kubernetes bħala l-aħjar għażla għall-ħtiġijiet tal-intrapriża tagħna. Ir-raġunijiet tagħna biex għażilna Kubernetes huma dawn:

1. **Skalabbiltà:**  Id-disinn uniku ta' Kubernetes huwa perfett biex jiskala applikazzjonijiet, u hekk kif ir-rekwiżiti tagħna ta' skalabbiltà jevolvu maż-żmien, Kubernetes għandu l-kapaċità integrata li jlaħħaq ma' dawn il-bidliet mingħajr xkiel.

2. **Arkitettura deċentralizzata:**  It-topoloġija master-worker ta' Kubernetes tiżgura arkitettura deċentralizzata li tiżgura li ma jkun hemm ebda punt uniku ta' falliment.

3. **Appoġġ tal-komunità:**  Kubernetes għandu l-akbar u l-aktar komunità open-source attiva, li jfisser li għandu numru kbir ta' kontributuri, żviluppaturi, u fornituri, u dan jagħmilha eħfef għalina biex niksbu għajnuna u nsibu riżorsi.

4. **Appoġġ tal-ekosistema:**  Kubernetes għandu ekosistema li qed tikber b'varjetà ta' għodod ta' partijiet terzi, integrazzjonijiet ma' registries tal-kontenituri, pipelines CI/CD, ħażna tad-data, u aktar.

Għalhekk, iddeċidejna li nadottaw Kubernetes bħala l-pjattaforma tagħna ta' orkestrazzjoni tal-kontenituri għal issa u għall-futur immedjat.

<h6>Kreditu: din il-paġna ġiet iġġenerata minn ChatGPT, imbagħad editjata għall-ċarezza u l-format.</h6>
