# Architektūros sprendimo įrašas: Kubernetes konteinerių orkestravimas

## Problemos formulavimas 

Turime pasirinkti konteinerių orkestravimo platformą savo augančiam debesijai natūralių programų portfeliui. Dabartinė paveldėtos platformos diegimo eiga per lėta ir nepakankamai lanksti, kad atitiktų mūsų augančius poreikius. Ieškome sistemos, kuri leistų kuo efektyviau keisti mūsų paslaugų mastelį nepakenkiant lankstumui ar naudojimo paprastumui.

## Svarstytos alternatyvos

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Priimtas sprendimas

Atlikę kruopščią kiekvienos konteinerių orkestravimo platformos analizę, nusprendėme priimti Kubernetes kaip geriausią variantą mūsų įmonės poreikiams. Mūsų priežastys rinktis Kubernetes yra šios:

1. **Mastelio keitimas:**  unikalus Kubernetes dizainas puikiai tinka programų mastelio keitimui, o kai mūsų mastelio keitimo reikalavimai laikui bėgant kinta, Kubernetes turi integruotą gebėjimą be problemų prisitaikyti prie šių pokyčių.

2. **Decentralizuota architektūra:**  Kubernetes pagrindinio-darbinio mazgo (master-worker) topologija užtikrina decentralizuotą architektūrą, kurioje nėra vienos gedimo vietos.

3. **Bendruomenės parama:**  Kubernetes turi didžiausią ir aktyviausią atvirojo kodo bendruomenę, o tai reiškia, kad yra daug prisidedančiųjų, programuotojų ir tiekėjų, todėl mums lengviau gauti pagalbos ir rasti išteklių.

4. **Ekosistemos parama:**  Kubernetes turi augančią ekosistemą su įvairiais trečiųjų šalių įrankiais, integracijomis su konteinerių registrais, CI/CD konvejeriais, duomenų saugojimu ir kt.

Todėl nusprendėme priimti Kubernetes kaip savo konteinerių orkestravimo platformą dabartiniam ir artimiausiam laikotarpiui.

<h6>Padėka: šį puslapį sugeneravo ChatGPT, vėliau jis buvo redaguotas aiškumui ir formatui pagerinti.</h6>