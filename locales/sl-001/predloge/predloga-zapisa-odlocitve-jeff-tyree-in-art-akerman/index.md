# Predloga zapisa odločitve Jeffa Tyreeja in Arta Akermana

To je predloga opisa arhitekturne odločitve, objavljena v članku [»Architecture Decisions: Demystifying Architecture« Jeffa Tyreeja in Arta Akermana, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Vprašanje (Issue)**: Opišite arhitekturno oblikovalsko vprašanje, ki ga obravnavate, tako da ne ostane noben dvom, zakaj to vprašanje obravnavate zdaj. V duhu minimalizma obravnavajte in dokumentirajte le vprašanja, ki jih je treba obravnavati v različnih točkah življenjskega cikla.

* **Odločitev (Decision)**: Jasno navedite smer arhitekture – to pomeni stališče, ki ste ga izbrali.

* **Stanje (Status)**: Stanje odločitve, na primer v obravnavi, sprejeta ali odobrena.

* **Skupina (Group)**: Za lažjo organizacijo nabora odločitev lahko uporabite preprosto združevanje – na primer integracija, predstavitev, podatki itd. Uporabite lahko tudi bolj dovršeno arhitekturno ontologijo, na primer ontologijo Johna Kyaruzija in Jana van Katwijka, ki vključuje bolj abstraktne kategorije, kot so dogodek, koledar in lokacija. Na primer, s to ontologijo bi odločitve, ki se nanašajo na pojave, pri katerih sistem potrebuje informacije, združili pod dogodek.

* **Predpostavke (Assumptions)**: Jasno opišite temeljne predpostavke v okolju, v katerem sprejemate odločitev – stroški, urnik, tehnologija itd. Upoštevajte, da lahko omejitve okolja (kot so sprejeti tehnološki standardi, podjetniška arhitektura, pogosto uporabljeni vzorci itd.) omejijo alternative, ki jih preučujete.

* **Omejitve (Constraints)**: Zajemite vse dodatne omejitve za okolje, ki jih lahko povzroči izbrana alternativa (odločitev).

* **Stališča (Positions)**: Navedite stališča (izvedljive možnosti ali alternative), ki ste jih preučili. Ta pogosto zahtevajo dolge razlage, včasih celo modele in diagrame. To ni izčrpen seznam. Vendar pa si pri končnem pregledu ne želite slišati vprašanja »Ali ste razmislili o ...?«; to vodi do izgube verodostojnosti in dvomov o drugih arhitekturnih odločitvah. Ta razdelek tudi pomaga zagotoviti, da ste slišali mnenja drugih; izrecno navajanje drugih mnenj pomaga pridobiti njihove zagovornike za vašo odločitev.

* **Argument (Argument)**: Orišite, zakaj ste izbrali določeno stališče, vključno s postavkami, kot so stroški izvedbe, skupni stroški lastništva, čas do trga in razpoložljivost potrebnih razvojnih virov. To je verjetno enako pomembno kot sama odločitev.

* **Posledice (Implications)**: Odločitev prinaša številne posledice, kot označuje metamodel REMAP. Odločitev lahko na primer povzroči potrebo po sprejetju drugih odločitev, ustvari nove zahteve ali spremeni obstoječe zahteve; naloži dodatne omejitve za okolje; zahteva ponovna pogajanja s strankami o obsegu ali urniku; ali zahteva dodatno usposabljanje osebja. Jasno razumevanje in navajanje posledic vaše odločitve je lahko zelo učinkovito pri pridobivanju podpore in ustvarjanju načrta za izvedbo arhitekture.

* **Povezane odločitve (Related decisions)**: Očitno je, da je veliko odločitev povezanih; lahko jih navedete tukaj. Vendar smo v praksi ugotovili, da so uporabnejše matrika sledljivosti, odločitvena drevesa ali metamodeli. Metamodeli so uporabni za diagramski prikaz kompleksnih razmerij (na primer modeli Rose).

* **Povezane zahteve (Related requirements)**: Odločitve morajo biti poslovno vodene. Da pokažete odgovornost, svoje odločitve izrecno preslikajte na cilje ali zahteve. Te povezane zahteve lahko naštejete tukaj, vendar smo ugotovili, da je priročneje sklicevanje na matriko sledljivosti. Lahko ocenite prispevek vsake arhitekturne odločitve k izpolnjevanju posamezne zahteve in nato ocenite, kako dobro je zahteva izpolnjena v vseh odločitvah. Če odločitev ne prispeva k izpolnjevanju zahteve, te odločitve ne sprejmite.

* **Povezani artefakti (Related artifacts)**: Navedite povezane dokumente arhitekture, oblikovanja ali obsega, na katere ta odločitev vpliva.

* **Povezana načela (Related principles)**: Če ima podjetje dogovorjen nabor načel, zagotovite, da je odločitev skladna z enim ali več njimi. To pomaga zagotoviti usklajenost po domenah ali sistemih.

* **Opombe (Notes)**: Ker lahko postopek odločanja traja tedne, smo ugotovili, da je koristno zajeti opombe in vprašanja, o katerih ekipa razpravlja med postopkom usklajevanja.

