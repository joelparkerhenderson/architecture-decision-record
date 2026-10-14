# Jeff Tyree'lt ja Art Akermanilt pärit otsusekirje mall

See on arhitektuuriotsuste kirjeldamise mall väljaandest ["Architecture Decisions: Demystifying Architecture", Jeff Tyree ja Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Küsimus (Issue)**: Kirjelda arhitektuuridisaini probleemi, mida käsitled, nii et ei jää kahtlust, miks sa seda praegu käsitled. Minimalistliku lähenemise kohaselt käsitle ja dokumenteeri ainult neid küsimusi, mis vajavad elutsükli teatud punktides tähelepanu.

* **Otsus (Decision)**: Näita selgelt arhitektuurisuunda, st valitud seisukohta.

* **Olek (Status)**: Otsuse olek, näiteks pending, decided, approved.

* **Rühm (Group)**: Otsuste kogumi korrastamiseks võid kasutada lihtsaid rühmitusi nagu integratsioon, esitlus, andmed jne. Võid kasutada ka täpsemat arhitektuuriontoloogiat, näiteks John Kyaruzi ja Jan van Katwijki oma, mis sisaldab abstraktsemaid kategooriaid nagu sündmused, kalendrid ja asukohad. Selle ontoloogiaga rühmitaksid näiteks otsused, mis käsitlevad olukordi, kus süsteem vajab teavet, sündmuste alla.

* **Eeldused (Assumptions)**: Kirjelda selgelt keskkonna aluseks olevaid eeldusi, milles otsus tehakse: kulu, ajakava, tehnoloogia jne. Pane tähele, et keskkonna piirangud (nagu aktsepteeritud tehnoloogiastandardid, ettevõtte arhitektuur, tavaliselt kasutatavad mustrid) võivad piirata kaalutavaid alternatiive.

* **Piirangud (Constraints)**: Jäädvusta kõik täiendavad piirangud, mida valitud alternatiiv (otsus) võib keskkonnale seada.

* **Seisukohad (Positions)**: Loetle kaalutud seisukohad (teostatavad valikud või alternatiivid). See nõuab sageli pikka selgitust ja mõnikord isegi mudeleid ja diagramme. See ei ole tingimata ammendav loetelu. Sa ei taha aga lõplikul ülevaatusel kuulda küsimust "Kas sa mõtlesid ...-le?". See viib usalduse kaotuseni ja kahtlusteni teiste arhitektuuriotsuste suhtes. See jaotis aitab ka kinnitada, et oled teiste arvamusi kuulanud. Teiste arvamuste selgesõnaliseks tegemine aitab nende pooldajad sinu otsuse taha saada.

* **Argument**: Visanda, miks valisid ühe seisukoha, teemadega nagu teostuskulu, kogu omamiskulu, turuletuleku aeg ja vajalike arendusressursside kättesaadavus. See on tõenäoliselt sama oluline kui otsus ise.

* **Tagajärjed (Implications)**: Otsusel on palju tagajärgi, nagu REMAP-i metamudel näitab. Näiteks võib otsus tekitada vajaduse teha teisi otsuseid, luua uusi nõudeid või muuta olemasolevaid, seada keskkonnale täiendavaid piiranguid, nõuda kliendiga ulatuse või ajakava uuesti läbirääkimist või nõuda lisakoolitust töötajatele. Otsuse tagajärgede selge mõistmine ja väljendamine võib olla väga tõhus nõusoleku saamiseks ja arhitektuuri täideviimise teekaardi loomiseks.

* **Seotud otsused**: On ilmne, et paljud otsused on omavahel seotud; võid need siin loetleda. Praktikas leiame aga, et jälgitavusmaatriks, otsustepuu või metamudel on kasulikum. Metamudelid on kasulikud keerukate seoste kuvamiseks diagrammidel (nt Rose'i mudelid).

* **Seotud nõuded**: Otsused peaksid olema ärist lähtuvad. Vastutuse näitamiseks seo otsused selgesõnaliselt eesmärkide või nõuetega. Võid need seotud nõuded siin loetleda, kuid leiame mugavamaks viidata jälgitavusmaatriksile. Hindad, mil määral iga arhitektuuriotsus aitab täita iga nõuet, ja seejärel, kui hästi nõuded on kõigi otsuste lõikes täidetud. Kui otsus ei aita nõuet täita, ära seda otsust tee.

* **Seotud artefaktid**: Loetle asjakohased arhitektuuri-, disaini- või ulatusdokumendid, mida see otsus mõjutab.

* **Seotud põhimõtted**: Kui ettevõttel on kokku lepitud põhimõtete kogum, veendu, et otsus on kooskõlas vähemalt ühega neist. See aitab tagada kooskõla valdkondade või süsteemide vahel.

* **Märkmed**: Kuna otsustusprotsess võib võtta nädalaid, leiame kasulikuks jäädvustada märkmeid ja küsimusi, mida meeskond eelneva jagamise käigus arutab.

