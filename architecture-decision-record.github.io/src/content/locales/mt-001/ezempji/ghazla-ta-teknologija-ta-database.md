# Rekord ta' deċiżjoni arkitettonika: għażla ta' teknoloġija ta' database

## Stat

Aċċettat

## Kuntest

Qed niddisinjaw applikazzjoni ġdida li teħtieġ li taħżen u tirkupra d-data b'mod skalabbli u b'prestazzjoni tajba. Identifikajna tliet tipi ta' teknoloġiji ta' database li jintużaw komunement: databases relazzjonali, databases ta' dokumenti, u databases ta' avvenimenti.

Id-databases relazzjonali jaħżnu d-data f'tabelli b'skemi fissi u jinfurzaw restrizzjonijiet stretti ta' integrità tad-data. Huma adattati għal applikazzjonijiet li jeħtieġu relazzjonijiet kumplessi tad-data u tranżazzjonijiet. L-eżempji jinkludu MySQL, PostgreSQL, u Oracle.

Id-databases ta' dokumenti jaħżnu d-data f'dokumenti simili għal JSON u m'għandhomx skema. Huma adattati sew għal applikazzjonijiet li jeħtieġu mudelli flessibbli tad-data u skalar orizzontali. L-eżempji jinkludu MongoDB, Couchbase, u Amazon DynamoDB.

Id-databases ta' avvenimenti jaħżnu d-data bħala sensiela ta' avvenimenti, u jiġbru kull bidla fid-data. Huma adattati għal applikazzjonijiet li jeħtieġu awditjar, event sourcing, u proċessar kumpless tad-data. L-eżempji jinkludu Apache Kafka, Apache Pulsar, u AWS Kinesis.
Deċiżjoni

Wara li evalwajna bir-reqqa r-rekwiżiti u r-restrizzjonijiet tal-applikazzjoni tagħna, iddeċidejna li nużaw database ta' dokumenti.

## Raġunament

Għażilna database ta' dokumenti għax:

1. L-applikazzjoni tagħna teħtieġ mudell flessibbli tad-data li jista' jevolvi maż-żmien. Id-databases ta' dokumenti jippermettulna naħżnu d-data f'format mingħajr skema, li jfisser li nistgħu nżidu oqsma ġodda jew inbiddlu l-istruttura ta' dokumenti eżistenti mingħajr ma jkollna bżonn nimmodifikaw l-iskema tad-database.

2. L-applikazzjoni tagħna teħtieġ li tiskala orizzontalment biex tlaħħaq ma' volumi kbar ta' data u traffiku. Id-databases ta' dokumenti jipprovdu appoġġ integrat għas-sharding u r-replikazzjoni, li jippermettilna nqassmu d-data fuq servers multipli u nlaħħqu ma' throughput għoli ta' qari u kitba.

3. L-applikazzjoni tagħna teħtieġ rkupru mgħaġġel u effiċjenti tad-data. Id-databases ta' dokumenti jipprovdu kapaċitajiet qawwija ta' indiċjar u interrogazzjoni li jippermettulna nirkupraw id-data malajr u b'mod effiċjenti.

4. L-applikazzjoni tagħna ma teħtieġx tranżazzjonijiet jew relazzjonijiet kumplessi tad-data. Għalkemm id-databases relazzjonali jeċċellaw fl-infurzar ta' restrizzjonijiet tal-integrità tad-data u fl-immaniġġjar ta' tranżazzjonijiet kumplessi, l-applikazzjoni tagħna m'għandhiex tali rekwiżiti. Id-databases ta' dokumenti jistgħu jipprovdu garanziji suffiċjenti ta' konsistenza u durabbiltà għall-każ ta' użu tagħna.

## Konsegwenzi

Billi nagħżlu database ta' dokumenti, se jkollna bżonn ninvestu fit-tagħlim u fil-fehim tat-teknoloġija speċifika li nagħżlu li nużaw. Barra minn hekk, se jkollna bżonn niżguraw li l-mudell tad-data tal-applikazzjoni tagħna jaqbel sew mal-mudell tad-data tad-database ta' dokumenti biex timmassimizzaw il-prestazzjoni u l-iskalabbiltà.

Madankollu, aħna nemmnu li l-benefiċċji tal-użu ta' database ta' dokumenti jisbqu l-ispejjeż, u li hija l-aħjar waħda għar-rekwiżiti u r-restrizzjonijiet tal-applikazzjoni tagħna.
