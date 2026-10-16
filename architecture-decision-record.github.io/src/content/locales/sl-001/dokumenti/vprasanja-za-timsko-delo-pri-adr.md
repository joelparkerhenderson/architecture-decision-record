
### Kdo lahko ustvari ADR?

Upoštevajte področja, kot so določene osebe, določene vloge, določene ekipe ali določeni oddelki; upoštevajte tudi, ali obstajajo osebe, vloge, ekipe ali oddelki, ki lahko naročijo ADR, kar pomeni, da zahtevajo ADR, ki ga bo napisal nekdo drug. 

Primer odgovora: Vsaka oseba v naši organizaciji, ki je prebrala stran README o zapisu arhitekturne odločitve, lahko predlaga ADR, kar pomeni, da ga lahko začne pisati in ga deli z ekipo.

### Kaj upravičuje pripravo ADR?

Upoštevajte področja, kot so načini dela ekip v vaši organizaciji, struktura vašega programskega sistema, usklajevanje med ekipami, dolgoročna vzdržljivost, zunanji vmesniki, kdo naj ima korist in podobno. 

Primer odgovora: ADR želimo ustvariti, kadar želimo, da bi prihodnji razvijalci razumeli »zakaj« tega, kar počnemo.

### Kaj upravičuje opustitev priprave ADR?

Upoštevajte področja, kot so odločitve, ki niso arhitekturne ali so drobne, na primer z minimalnim tveganjem, samostojne ali ki jih sprejme en sam razvijalec, ali so že v celoti pokrite drugje, na primer s standardi, politikami ali dokumentacijo, ali so začasne, na primer obvodi, dokazi o izvedljivosti ali poskusi. 

Primer odgovora: ADR želimo preskočiti, kadar je odločitev omejena po obsegu, času, tveganju in stroških ali je že pokrita drugje.

### Kakšen je življenjski cikel ADR?

Upoštevajte področja, kot so postopek ustvarjanja, postopek raziskovanja, postopek odločanja, postopek izvajanja in postopek opustitve. Razmislite, kako spremljati življenjski cikel ADR skozi čas, na primer kako ADR premakniti iz enega stanja v naslednje in kako to sporočiti deležnikom. 

Primer odgovora: Želimo, da ima ADR pet stopenj življenjskega cikla: Uvedba → Raziskovanje → Vrednotenje → Izvajanje → Vzdrževanje → Opustitev.

### Kakšna so merila za korake življenjskega cikla ADR?

Upoštevajte področja, kot so merila sprejemljivosti za ADR, kar pomeni, kako veste, da je dovolj dober za prehod iz enega koraka življenjskega cikla v naslednjega? Ali je problem jasno opredeljen? Ali so bile upoštevane alternative? Ali so kompromisi dovolj dobro razumljeni in dokumentirani?
Ali je ves ustrezen kontekst na mestu? Ali so vključeni vsi ustrezni deležniki? Ali so bile vse povratne informacije upoštevane? 

Primer odgovora: Želimo, da o ADR glasujejo deležniki, ko je dejavna ekipa 1) zaključila raziskavo, 2) zaključila vrednotenje, 3) deležnikom objavila predlog ADR z zahtevo za komentarje in časovnim oknom enega tedna, 4) so bili vsi komentarji deležnikov upoštevani in obravnavani.

### Katere vloge in odgovornosti sodelujejo pri ADR?

Upoštevajte vloge, kot so predlagatelj, raziskovalec, ocenjevalec, pregledovalec, odobritelj, vzdrževalec in podobno. Upoštevajte odgovornosti, kot so komunikacija z deležniki, zagotavljanje izpolnitve pričakovanj, deljenje na spletnem mestu ali intranetu ter redno pregledovanje dela, še posebej ob pomembnih spremembah.

Primer odgovora: Želimo, da ima vsak ADR vedno primarno kontaktno osebo, sekundarno kontaktno osebo in odgovorno ekipo; te so odgovorne za komunikacijo, objave, vzdrževanje, redni pregled vsaj enkrat na leto in morebitno opustitev po potrebi.

### Kako upravljanje (governance) vpliva na ADR?

Upoštevajte področja, kot so načini dela v vaši organizaciji, posebne potrebe po skladnosti, na primer pravni vidiki ali vidiki kadrovskih virov, ter kako želite ravnati s soglasjem, konflikti in stopnjevanjem. Ali obstajajo področja, osebe ali ekipe, ki imajo lahko glede ADR večji vpliv kot druge, na primer da ga lahko odobrijo, o njem glasujejo ali nanj vložijo veto?

Primer odgovora: Upravljanje ADR poteka v tem vrstnem redu prednosti: generalni direktor (CEO), tehnični direktor (CTO), pravni direktor (CLO), ekipa, ki izvaja ADR, strokovnjaki v ekipi, ki najbolje poznajo AD. Nihče drug nima pristojnosti upravljanja, razen če je to opisano v ADR. 

### Katera načela vplivajo na ADR?

Upoštevajte področja, kot so načini dela v vaši organizaciji, ki vključujejo hitro ali počasno ukrepanje, soglasje ali nesoglasje pri odločitvah, prednost tveganja ali prednost varnosti, javno ali zasebno razpravo in podobno.

Primer odgovora: Uporabljamo vodstvena načela nagnjenosti k ukrepanju (bias for action), nestrinjanja z zavezanostjo (disagree-and-commit), 70-odstotne ocene zadoščajo za lahko povratljive in lahko izolirane odločitve ter javne načine dela, razen pri zaupnih informacijah, kot je opisano v dogovoru o zaupnosti naše organizacije.
