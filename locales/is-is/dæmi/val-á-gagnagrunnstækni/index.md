# Arkitektúrákvörðunarskrá: val á gagnagrunnstækni

## Staða

Samþykkt

## Samhengi

Við erum að hanna nýtt forrit sem krefst þess að geyma og sækja gögn á stigstærðan og afkastamikinn hátt. Við höfum greint þrjár tegundir gagnagrunnstækni sem algengt er að nota: venslagagnagrunna, skjalagagnagrunna og atburðagagnagrunna.

Venslagagnagrunnar geyma gögn í töflum með föstum skemum og framfylgja ströngum takmörkunum á gagnaheilleika. Þeir henta forritum sem krefjast flókinna gagnatengsla og færslna. Dæmi eru MySQL, PostgreSQL og Oracle.

Skjalagagnagrunnar geyma gögn í JSON-líkum skjölum og eru án skema. Þeir henta vel forritum sem krefjast sveigjanlegra gagnalíkana og láréttrar stækkunar. Dæmi eru MongoDB, Couchbase og Amazon DynamoDB.

Atburðagagnagrunnar geyma gögn sem röð atburða og fanga hverja breytingu á gögnunum. Þeir henta forritum sem krefjast endurskoðunarslóðar, atburðaupprunans (event sourcing) og flókinnar gagnavinnslu. Dæmi eru Apache Kafka, Apache Pulsar og AWS Kinesis.
Ákvörðun

Eftir vandlegt mat á kröfum og takmörkunum forritsins okkar höfum við ákveðið að nota skjalagagnagrunn.

## Rökstuðningur

Við höfum valið skjalagagnagrunn vegna þess að:

1. Forritið okkar krefst sveigjanlegs gagnalíkans sem getur þróast með tímanum. Skjalagagnagrunnar leyfa okkur að geyma gögn á sniði án skema, sem þýðir að við getum bætt við nýjum reitum eða breytt uppbyggingu fyrirliggjandi skjala án þess að þurfa að breyta skema gagnagrunnsins.

2. Forritið okkar þarf að stækka lárétt til að meðhöndla mikið magn gagna og umferðar. Skjalagagnagrunnar bjóða upp á innbyggðan stuðning við sundrun (sharding) og afritun, sem gerir okkur kleift að dreifa gögnum á marga þjóna og meðhöndla mikið lestrar- og skrifflæði.

3. Forritið okkar krefst hraðrar og skilvirkrar gagnaleitar. Skjalagagnagrunnar bjóða upp á öfluga vísitölugerð og fyrirspurnargetu sem gerir okkur kleift að sækja gögn hratt og skilvirkt.

4. Forritið okkar krefst ekki flókinna færslna eða gagnatengsla. Þótt venslagagnagrunnar skari fram úr í að framfylgja takmörkunum á gagnaheilleika og meðhöndla flóknar færslur hefur forritið okkar ekki slíkar kröfur. Skjalagagnagrunnar geta veitt nægilega tryggingu fyrir samræmi og varanleika fyrir okkar notkunartilvik.

## Afleiðingar

Með því að velja skjalagagnagrunn þurfum við að fjárfesta í því að læra og skilja þá tilteknu tækni sem við veljum að nota. Að auki þurfum við að tryggja að gagnalíkan forritsins okkar passi vel við gagnalíkan skjalagagnagrunnsins til að hámarka afköst og stigstærð.

Við teljum þó að ávinningurinn af því að nota skjalagagnagrunn vegi þyngra en kostnaðurinn og að hann sé besta passunin fyrir kröfur og takmarkanir forritsins okkar.
