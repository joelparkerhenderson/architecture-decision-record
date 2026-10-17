# Rekord ta' deċiżjoni arkitettonika: snake_case vs camelCase għal API REST?

Deċiżjoni: Il-konvenzjoni tal-għoti ta' ismijiet snake_case se tintuża għall-endpoints tal-API REST

Stat: Aċċettat

## Kuntest

Fil-konvenzjonijiet tal-għoti ta' ismijiet għall-API REST, hemm żewġ formati popolari: snake_case u camelCase. Il-format snake_case huwa fejn kull kelma fl-isem hija separata b'underscores, filwaqt li camelCase huwa fejn l-ewwel kelma tal-isem tkun b'ittri żgħar, u l-kliem sussegwenti jkollhom l-ewwel ittra kapitali. Din id-deċiżjoni se tiddetermina liema konvenzjoni tal-għoti ta' ismijiet għandha tintuża għal API REST.

## Fatturi tad-deċiżjoni

- Konsistenza mal-konvenzjonijiet eżistenti tal-għoti ta' ismijiet fil-proġett

- Qari faċli u ċarezza għal kull min jista' jkun qed jaħdem fuq l-API

- Allinjament mal-aħjar prattiki tal-industrija għall-konvenzjonijiet tal-għoti ta' ismijiet tal-API REST

- Faċilità ta' implimentazzjoni u manutenzjoni

## Deċiżjoni

Il-konvenzjoni tal-għoti ta' ismijiet snake_case se tintuża għall-endpoints tal-API REST. Din l-għażla hija mmexxija mill-fatturi li ġejjin:

1. **Konsistenza**: Il-proġett diġà juża l-konvenzjoni tal-għoti ta' ismijiet snake_case għall-endpoints kollha, u jkun ta' benefiċċju li tinżamm din il-konvenzjoni biex tiġi żgurata l-konsistenza madwar il-proġett kollu.

2. **Qari faċli u ċarezza**: Il-konvenzjoni snake_case hija aktar faċli biex tinqara u tinftiehem. L-underscores jipprovdu separazzjoni ċara bejn il-kliem, u jagħmluha eħfef biex jiġi analizzat u mifhum it-tifsira tal-isem.

3. **Allinjament mal-aħjar prattiki tal-industrija**: Il-konvenzjoni snake_case tintuża b'mod wiesa' fl-industrija u hija meqjusa bħala l-aħjar prattika għall-API REST, u dan jagħmilha għażla tajba għall-proġett.

4. **Faċilità ta' implimentazzjoni u manutenzjoni**: Li tinżamm il-konvenzjoni eżistenti tal-għoti ta' ismijiet hija eħfef biex tiġi implimentata u miżmuma peress li l-kodiċi u d-dokumentazzjoni eżistenti kollha jkollhom bżonn jiġu aġġornati kieku tintgħażel konvenzjoni ġdida.

## Konsegwenzi

Hemm konsegwenzi potenzjali ta' din id-deċiżjoni. 

* Jekk xi membri ġodda tat-tim li jingħaqdu mal-proġett mhumiex familjari mal-konvenzjoni tal-għoti ta' ismijiet snake_case, jista' jwassal għal konfużjoni u żbalji fl-iżvilupp. Madankollu, peress li snake_case hija konvenzjoni użata b'mod wiesa', riskju bħal dan huwa minimu. 
  
* Jekk fil-proġett jintużaw għodod jew frameworks oħra li huma bbażati ħafna fuq il-konvenzjoni camelCase, jista' jirrikjedi sforz addizzjonali biex isir il-konvertiment bejn il-konvenzjonijiet tal-għoti ta' ismijiet. Madankollu, mhuwiex tħassib sinifikanti peress li l-proġett standardizza fuq il-konvenzjoni snake_case. 
 
B'mod ġenerali, id-deċiżjoni li tintuża l-konvenzjoni tal-għoti ta' ismijiet snake_case għall-endpoints tal-API REST tirriżulta f'approċċ konsistenti, faċli biex jinqara, u standard tal-industrija filwaqt li hija faċli biex tiġi implimentata u miżmuma.

<h6>Kreditu: din il-paġna ġiet iġġenerata minn ChatGPT, imbagħad editjata għall-ċarezza u l-format.</h6>
