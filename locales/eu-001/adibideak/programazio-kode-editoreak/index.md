# Arkitektura-erabakien erregistroa: programazio-kode editoreak

## Testuingurua

Programazio-kode editoreak garatzaileentzat ezinbesteko tresna dira kodea idazteko eta editatzeko. Kode-editore asko daude eskuragarri, bakoitzak bere ezaugarri, abantaila eta desabantailekin. ADR honen helburua programazio-kode editoreentzat hartutako arkitektura-erabakiak dokumentatzea da.

## Lehentasunak

Programazio-kode editoreen arkitekturak honakoak lehenetsi behar ditu:

* **Modulartasuna**: Kode-editorea modu modularrean diseinatu behar da, garatzaileei behar den moduan pertsonalizatzeko eta hedatzeko aukera emanez. Horrek garatzaile eta talde desberdinen beharretara egokitu daitekeen arkitektura malgua ahalbidetzen du.

* **Errendimendua**: Kode-editoreak errendimendu onekoa eta erantzunkorra izan behar du, garatzaileei eraginkortasunez lan egiteko aukera emanez, erabiltzen ari diren tresnak moteldu gabe.

* **Erabiltzaile-interfazea**: Erabiltzaile-interfazea intuitiboa eta erabiltzeko erraza izan behar da, garatzaileek editorearekin borrokatu beharrean beren kodean zentratzeko aukera emanez.

* **Hedagarritasuna**: Kode-editorea hirugarrenen plugin eta integrazioekin erraz hedatzeko diseinatu behar da.

* **Bateragarritasuna**: Kode-editoreak programazio-lengoaia eta teknologia sorta zabalarekin bateragarria izan behar du, garatzaile sorta zabal baterako tresna baliagarria bihurtuz.

## Erabakia

Lehentasun hauetan oinarrituta, programazio-kode editoreen arkitektura osagai hauekin diseinatu behar da:

* **Nukleoa**: Osagai honek kode-editorearen oinarrizko funtzionalitatea eskaintzen du, hala nola sintaxi-nabarmentzea, testu-edizioa eta fitxategi-kudeaketa.

* **UI**: Osagai honek kode-editorearen erabiltzaile-interfazea eskaintzen du, menuak, tresna-barrak eta teklatu-lasterbideak barne.

* **Pluginak**: Osagai honek garatzaileei kode-editorearen funtzionalitatea hedatzeko aukera ematen die hirugarrenen pluginak instalatuz. Pluginek ezaugarri gehigarriak eskaini ditzakete, hala nola kode-osatzea, linting-a edo arazketa.

* **Integrazioak**: Osagai honek kode-editoreak beste tresna eta teknologiekin, hala nola bertsio-kontroleko sistemekin, build sistemekin edo arazketa-tresnekin, integratzea ahalbidetzen du.

## Arrazoibidea

Kode-editorearen modulartasunak garatzaileei behar den moduan pertsonalizatzeko eta hedatzeko aukera ematen die. Hori garrantzitsua da garatzaile eta talde desberdinek behar eta lan-fluxu desberdinak dituztelako, eta arkitektura malguak desberdintasun horiek hartu ditzakeelako.

* **Errendimendua**: funtsezkoa da garatzaileek eraginkortasunez lan egin ahal izan behar dutelako beren tresnek moteldu gabe. Errendimendu onekoa den kode-editorea ezinbestekoa da produktibitaterako eta garatzaileei beren fokua eta kontzentrazioa mantentzen lagun diezaieke.

* **UI**: garrantzitsua da garatzaileek editorearekin borrokatu beharrean beren kodean zentratzeko aukera ematen duelako. Horrek produktibitate hobea eta garatzaileentzako frustrazio gutxiago ekar dezake.

* **Hedagarritasuna**: ahaltsua da kode-editorea behar eta lan-fluxu desberdinetara egokitzeko aukera ematen duelako. Hirugarrenen plugin eta integrazioek editore nagusian sartzen ez diren ezaugarri eta gaitasun gehigarriak eskain ditzakete.

* **Bateragarritasuna**: baliotsua da kode-editorea programazio-lengoaia eta teknologia sorta zabalarekin erabiltzeko aukera ematen duelako. Horrek editorea garatzaile sorta zabal baterako tresna baliagarriagoa egiten du.

Nukleoak, pluginek, integrazioek eta UI osagaiek kezken bereizketa argia ematen dute eta erraz hedatu eta pertsonaliza daitekeen arkitektura modularra ahalbidetzen dute. Arkitektura hau malgua, errendimendu onekoa eta programazio-lengoaia eta teknologia sorta zabalarekin bateragarria da, garatzaileentzako tresna baliagarria bihurtuz.
