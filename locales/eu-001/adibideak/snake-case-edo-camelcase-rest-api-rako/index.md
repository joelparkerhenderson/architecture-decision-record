# Arkitektura-erabakien erregistroa: snake_case edo camelCase REST API baterako?

Erabakia: snake_case izendapen-konbentzioa erabiliko da REST API amaiera-puntuetarako

Egoera: Onartua

## Testuingurua

REST API-etarako izendapen-konbentzioetan, bi formatu ezagun daude: snake_case eta camelCase. snake_case formatuan izenaren hitz bakoitza azpimarra batzuekin bereizten da, camelCase formatuan, berriz, izenaren lehen hitza minuskulaz dago, eta hurrengo hitzek lehen letra maiuskulaz dute. Erabaki honek zehaztuko du zein izendapen-konbentzio erabili behar den REST API baterako.

## Erabakiaren bultzatzaileak

- Proiektuan lehendik dauden izendapen-konbentzioekiko koherentzia

- API-an lan egin dezakeen edonorentzat irakurgarritasuna eta argitasuna

- REST API-en izendapenerako industriako jardunbide onekin lerrokatzea

- Ezartzeko eta mantentzeko erraztasuna

## Erabakia

snake_case izendapen-konbentzioa erabiliko da REST API amaiera-puntuetarako. Aukera hau faktore hauek bultzatzen dute:

1. **Koherentzia**: Proiektuak dagoeneko snake_case izendapen-konbentzioa erabiltzen du amaiera-puntu guztietarako, eta onuragarria litzateke konbentzio hori mantentzea proiektu osoan koherentzia ziurtatzeko.

2. **Irakurgarritasuna eta argitasuna**: snake_case konbentzioa irakurgarriagoa eta ulertzeko errazagoa da. Azpimarrek hitzen arteko bereizketa argia ematen dute, izenaren esanahia aztertzea eta ulertzea errazten dutenak.

3. **Industriako jardunbide onekin lerrokatzea**: snake_case konbentzioa industrian zabal erabiltzen da eta REST API-etarako jardunbide ontzat hartzen da, proiekturako aukera ona bihurtuz.

4. **Ezartzeko eta mantentzeko erraztasuna**: Lehendik dagoen izendapen-konbentzioarekin jarraitzea errazagoa da ezartzeko eta mantentzeko, konbentzio berri bat aukeratuko balitz lehendik dagoen kode eta dokumentazio guztia eguneratu beharko litzatekeelako.

## Ondorioak

Erabaki honen ondorio potentzialak daude. 

* Proiektuan sartzen den taldekide berriren bat snake_case izendapen-konbentzioarekin ohituta ez badago, nahasmena eta akatsak sor ditzake garapenean. Hala ere, snake_case oso erabilia den konbentzioa denez, arrisku hori minimoa da. 
  
* Proiektuan camelCase konbentzioan oso oinarritutako beste tresna edo esparru batzuk erabiltzen badira, baliteke ahalegin gehigarria behar izatea izendapen-konbentzioen artean bihurtzeko. Hala ere, ez da kezka esanguratsua, proiektuak snake_case konbentzioan estandarizatu duelako. 
 
Orokorrean, REST API amaiera-puntuetarako snake_case izendapen-konbentzioa erabiltzeko erabakiak ikuspegi koherente, irakurgarri eta industria-estandarra dakar, ezartzeko eta mantentzeko erraza izanik.

<h6>Kreditua: orri hau ChatGPT-k sortu du, eta gero argitasunerako eta formaturako editatu da.</h6>
