# Arhitektuuriotsuse kirje: snake_case või camelCase REST API jaoks?

Otsus: REST API lõpp-punktide jaoks kasutatakse nimetamiskonventsiooni snake_case

Olek: Aktsepteeritud

## Kontekst

REST API-de nimetamiskonventsioonides on kaks populaarset vormingut: snake_case ja camelCase. Snake_case'i puhul eraldatakse iga nimes olev sõna allkriipsudega, camelCase'i puhul on nime esimene sõna väiketähtedega ja järgnevatel sõnadel on esimene täht suur. See otsus määrab, millist nimetamiskonventsiooni REST API jaoks kasutada.

## Otsuse liikumapanevad jõud

- Järjepidevus projekti olemasolevate nimetamiskonventsioonidega

- Loetavus ja selgus kõigile, kes API-ga töötavad

- Vastavus valdkonna parimatele tavadele REST API nimetamiskonventsioonide osas

- Teostuse ja hoolduse lihtsus

## Otsus

REST API lõpp-punktide jaoks kasutatakse nimetamiskonventsiooni snake_case. Seda valikut ajendavad järgmised tegurid:

1. **Järjepidevus**: projekt kasutab juba kõigi lõpp-punktide jaoks nimetamiskonventsiooni snake_case ja selle konventsiooni säilitamine on kasulik järjepidevuse tagamiseks kogu projektis.

2. **Loetavus ja selgus**: konventsioon snake_case on loetavam ja lihtsamini mõistetav. Allkriipsud pakuvad sõnade vahel selget eraldust, muutes nime tähenduse parsimise ja mõistmise lihtsamaks.

3. **Vastavus valdkonna parimatele tavadele**: konventsiooni snake_case kasutatakse valdkonnas laialdaselt ja seda peetakse REST API-de parimaks tavaks, muutes selle projekti jaoks heaks valikuks.

4. **Teostuse ja hoolduse lihtsus**: olemasoleva nimetamiskonventsiooni säilitamine on lihtsam teostada ja hooldada, kuna uue konventsiooni valimisel tuleks kogu olemasolev kood ja dokumentatsioon uuendada.

## Tagajärjed

Sellel otsusel on võimalikke tagajärgi. 

* Kui projektiga liituvad uued meeskonnaliikmed ei ole nimetamiskonventsiooniga snake_case tuttavad, võib see viia segaduse ja vigadeni arenduses. Kuna snake_case on laialdaselt kasutatav konventsioon, on selline risk minimaalne. 
  
* Kui projektis kasutatakse teisi tööriistu või raamistikke, mis põhinevad suuresti konventsioonil camelCase, võib nimetamiskonventsioonide vaheline teisendamine nõuda lisapingutust. See ei ole aga oluline mure, kuna projekt on standardiseeritud konventsioonile snake_case. 
 
Üldiselt viib otsus kasutada REST API lõpp-punktide jaoks nimetamiskonventsiooni snake_case järjepideva, loetava ja valdkonna standardile vastava lähenemiseni, olles samal ajal hõlpsasti teostatav ja hooldatav.

<h6>Allikaviide: see leht on loodud ChatGPT-ga ja seejärel selguse ja vormingu huvides toimetatud.</h6>
