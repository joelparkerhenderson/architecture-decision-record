# Architekturális döntési feljegyzés: snake_case vagy camelCase egy REST API-hoz?

Döntés: A REST API végpontjaihoz a snake_case elnevezési konvenciót használjuk

Állapot: Elfogadott

## Háttér

A REST API-k elnevezési konvenciói között két népszerű formátum létezik: a snake_case és a camelCase. A snake_case formátumban a név minden szavát aláhúzás választja el, míg a camelCase-ben a név első szava kisbetűs, a következő szavak első betűje pedig nagybetűs. Ez a döntés fogja meghatározni, melyik elnevezési konvenciót kell használni egy REST API-hoz.

## Döntési tényezők

- Összhang a projekt meglévő elnevezési konvencióival

- Olvashatóság és érthetőség bárki számára, aki az API-n dolgozhat

- Összhang a REST API-k elnevezésére vonatkozó iparági legjobb gyakorlatokkal

- A megvalósítás és karbantartás egyszerűsége

## Döntés

A REST API végpontjaihoz a snake_case elnevezési konvenciót használjuk. Ezt a választást a következő tényezők vezérlik:

1. **Következetesség**: A projekt már minden végponthoz a snake_case elnevezési konvenciót használja, és előnyös lenne megtartani ezt a konvenciót a teljes projekt következetességének biztosításához.

2. **Olvashatóság és érthetőség**: A snake_case konvenció olvashatóbb és könnyebben érthető. Az aláhúzások világos elválasztást adnak a szavak között, megkönnyítve a név értelmének elemzését és megértését.

3. **Összhang az iparági legjobb gyakorlatokkal**: A snake_case konvenciót széles körben használják az iparágban, és a REST API-k legjobb gyakorlatának tekintik, ami jó választássá teszi a projekthez.

4. **A megvalósítás és karbantartás egyszerűsége**: A meglévő elnevezési konvenció megtartása könnyebben megvalósítható és karbantartható, mivel új konvenció választása esetén az összes meglévő kódot és dokumentációt frissíteni kellene.

## Következmények

E döntésnek lehetséges következményei vannak. 

* Ha a projekthez csatlakozó új csapattagok nem ismerik a snake_case elnevezési konvenciót, az zavarhoz és hibákhoz vezethet a fejlesztésben. Mivel azonban a snake_case széles körben használt konvenció, az ilyen kockázat minimális. 
  
* Ha a projektben olyan más eszközöket vagy keretrendszereket használnak, amelyek erősen a camelCase konvencióra épülnek, az elnevezési konvenciók közötti átalakítás extra erőfeszítést igényelhet. Ez azonban nem jelentős aggály, mivel a projekt a snake_case konvencióra szabványosított. 
 
Összességében a snake_case elnevezési konvenció használatáról szóló döntés következetes, olvasható és iparági szabványnak megfelelő megközelítést eredményez, miközben könnyen megvalósítható és karbantartható.

<h6>Forrás: ezt az oldalt a ChatGPT generálta, majd az érthetőség és a formázás érdekében szerkesztették.</h6>