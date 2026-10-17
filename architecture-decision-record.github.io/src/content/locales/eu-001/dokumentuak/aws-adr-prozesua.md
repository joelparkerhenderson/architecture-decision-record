# AWS arkitektura-erabakien erregistroen prozesua

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Arkitektura-erabakien erregistroa (ADR) taldeak eraikitzeko asmoa duen software-arkitekturaren alderdi esanguratsu bati buruz hartzen duen aukera bat deskribatzen duen dokumentua da. ADR bakoitzak arkitektura-erabakia, bere testuingurua eta bere ondorioak deskribatzen ditu. ADR-ek egoerak dituzte eta, beraz, bizi-zikloa jarraitzen dute. ADR baten adibide baterako, ikus eranskina.

ADR prozesuak arkitektura-erabakien erregistro bilduma bat sortzen du. Bilduma horrek erabaki-egunkaria osatzen du. Erabaki-egunkariak proiektuaren testuingurua eta ezarpen- eta diseinu-informazio xehatua ematen ditu. Proiektuko kideek ADR bakoitzaren tituluak arakatzen dituzte proiektuaren testuinguruaren ikuspegi orokorra lortzeko. ADR-ak irakurtzen dituzte proiektuaren ezarpenetan eta diseinu-aukeretan sakontzeko.

Taldeak ADR bat onartzen duenean, aldaezin bihurtzen da. Ikuspegi berriek beste erabaki bat eskatzen badute, taldeak ADR berri bat proposatzen du. Taldeak ADR berria onartzen duenean, aurreko ADR-a ordezkatzen du.

## ADR prozesuaren irismena

Proiektuko kideek ADR bat sortu behar dute software-proiektuari edo -produktuari eragiten dion arkitekturaren ikuspegitik esanguratsua den erabaki bakoitzerako, besteak beste hauetarako (Richards eta Ford 2020):

* Egitura (adibidez, mikrozerbitzuak bezalako ereduak)

* Funtzionalak ez diren eskakizunak (segurtasuna, erabilgarritasun handia eta akats-tolerantzia)

* Mendekotasunak (osagaien akoplamendua)

* Interfazeak (API-ak eta argitaratutako kontratuak)

* Eraikuntza-teknikak (liburutegiak, esparruak, tresnak eta prozesuak)

* Eskakizun funtzionalak eta ez-funtzionalak dira ADR prozesuaren sarrera ohikoenak.


## ADR-aren edukia

Taldeak ADR baten beharra identifikatzen duenean, taldekide batek ADR-a idazten hasten da proiektu osoko txantiloi batean oinarrituta. (Ikus ADR GitHub erakundea adibide-txantiloietarako.) Txantiloiak ADR-aren sorrera sinplifikatzen du eta ADR-ak informazio garrantzitsu guztia jasotzen duela ziurtatzen du. Gutxienez, ADR bakoitzak erabakiaren testuingurua, erabakia bera eta erabakiak proiektuarentzat eta bere entregagarrientzat dituen ondorioak definitu behar ditu. (Atal hauen adibideetarako, ikus eranskina.) ADR egituraren alderdirik indartsuenetako bat da erabakiaren arrazoian zentratzen dela, taldeak nola ezarri zuenean baino. Taldeak erabakia zergatik hartu zuen ulertzeak errazten du beste taldekideek erabakia onartzea, eta erabakitze-prozesuan parte hartu ez zuten beste arkitektoek etorkizunean erabaki hori baliogabetzea saihesten du.


## ADR-a onartzeko prozesua

Taldekide guztiek sor dezakete ADR bat, baina taldeak ADR baten jabetzaren definizio bat ezarri behar du. ADR baten jabea den egile bakoitzak ADR-aren edukia aktiboki mantendu eta komunikatu behar du. Jabetza hori argitzeko, gida honek ADR egileei ADR jabe deitzen die ondorengo ataletan. Beste taldekideek beti egin dezakete ekarpena ADR batean. ADR baten edukia aldatzen bada taldeak ADR-a onartu aurretik, jabeak aldaketa horiek onartu behar ditu.

Taldeak arkitektura-erabaki bat eta bere jabea identifikatu ondoren, ADR jabeak ADR-a **Proposatua** egoeran eskaintzen du prozesuaren hasieran. Proposatua egoeran dauden ADR-ak berrikusteko prest daude.

ADR jabeak ADR-aren berrikuspen-prozesua hasten du ondoren. ADR berrikuspen-prozesuaren helburua da erabakitzea taldeak ADR-a onartzen duen, berriz lan egin behar duela erabakitzen duen, ala ADR-a baztertzen duen. Proiektu-taldeak, jabea barne, ADR-a berrikusten du. Berrikuspen-bilerak ADR-a irakurtzeko denbora-tarte bat izan behar du hasieran. Batez beste, 10 eta 15 minutu nahikoak izan behar dira. Denbora horretan, taldekide bakoitzak dokumentua irakurtzen du eta iruzkinak eta galderak gehitzen ditu argi ez dauden gaiak markatzeko. Berrikuspen-fasearen ondoren, ADR jabeak iruzkin bakoitza ozen irakurri eta taldearekin eztabaidatzen du.

Taldeak ADR-a hobetzeko ekintza-puntuak aurkitzen baditu, ADR-aren egoerak **Proposatua** izaten jarraitzen du. ADR jabeak ekintzak formulatzen ditu, eta, taldearekin lankidetzan, ekintza bakoitzari arduraduna gehitzen dio. Taldekide bakoitzak ekarpena egin eta ekintza-puntuak ebatzi ditzake. ADR jabearen ardura da berrikuspen-prozesua berriz programatzea.

Taldeak ADR-a baztertzea ere erabaki dezake. Kasu horretan, ADR jabeak baztertzearen arrazoia gehitzen du, gai bererako etorkizuneko eztabaidak saihesteko. Jabeak ADR-aren egoera **Baztertua** bihurtzen du.

Taldeak ADR-a onartzen badu, jabeak denbora-zigilua, bertsioa eta interesdunen zerrenda gehitzen ditu. Gero egoera **Onartua** bihurtzen du.

ADR-ek eta sortzen duten erabaki-egunkariak taldeak hartutako erabakiak adierazten dituzte eta erabaki guztien historia ematen dute. Taldeak ADR-ak erreferentzia gisa erabiltzen ditu kode- eta arkitektura-berrikuspenetan, ahal den guztietan. Kode-berrikuspenak, diseinu-lanak eta ezarpen-lanak egiteaz gain, taldekideek ADR-ak kontsultatu behar dituzte produktuaren erabaki estrategikoetarako.

Praktika on gisa, software-aldaketa bakoitzak kideen berrikuspenak pasatu behar ditu eta gutxienez onarpen bat behar du. Kode-berrikuspenean, kode-berrikusle batek ADR bat edo gehiago urratzen dituzten aldaketak aurkitu ditzake. Kasu horretan, berrikusleak kode-aldaketaren egileari kodea eguneratzeko eskatzen dio, eta ADR-aren esteka partekatzen du. Egileak kodea eguneratzen duenean, kideen berrikusleek onartzen dute eta kode-oinarri nagusian batzen da.


## ADR berrikuspen-prozesua

Taldeak ADR-ak dokumentu aldaezin gisa tratatu behar ditu onartu edo baztertu ondoren. Lehendik dagoen ADR baten aldaketek ADR berri bat sortzea, ADR berriarentzat berrikuspen-prozesu bat ezartzea eta ADR-a onartzea eskatzen dute. Taldeak ADR berria onartzen badu, jabeak ADR zaharraren egoera **Ordeztua** bihurtu behar du.
