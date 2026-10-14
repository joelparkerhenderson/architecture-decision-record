# Zapis arhitekturne odluke: snake_case ili camelCase za REST API?

Odluka: Za krajnje točke REST API-ja koristit će se konvencija imenovanja snake_case

Status: Prihvaćeno

## Kontekst

U konvencijama imenovanja za REST API-je postoje dva popularna formata: snake_case i camelCase. Format snake_case je onaj u kojem je svaka riječ u nazivu odvojena podcrtama, dok je camelCase onaj u kojem je prva riječ naziva napisana malim slovima, a sljedeće riječi imaju veliko početno slovo. Ova će odluka odrediti koju konvenciju imenovanja treba koristiti za REST API.

## Pokretači odluke

- Dosljednost s postojećim konvencijama imenovanja u projektu

- Čitljivost i jasnoća za svakoga tko može raditi na API-ju

- Usklađenost s najboljim industrijskim praksama za konvencije imenovanja REST API-ja

- Jednostavnost implementacije i održavanja

## Odluka

Za krajnje točke REST API-ja koristit će se konvencija imenovanja snake_case. Taj izbor vode sljedeći čimbenici:

1. **Dosljednost**: Projekt već koristi konvenciju imenovanja snake_case za sve krajnje točke i bilo bi korisno zadržati tu konvenciju kako bi se osigurala dosljednost u cijelom projektu.

2. **Čitljivost i jasnoća**: Konvencija snake_case čitljivija je i lakše razumljiva. Podcrte pružaju jasno razdvajanje riječi, što olakšava raščlambu i razumijevanje značenja naziva.

3. **Usklađenost s najboljim industrijskim praksama**: Konvencija snake_case široko se koristi u industriji i smatra se najboljom praksom za REST API-je, što je čini dobrim izborom za projekt.

4. **Jednostavnost implementacije i održavanja**: Zadržavanje postojeće konvencije imenovanja lakše je za implementaciju i održavanje jer bi se, da je odabrana nova konvencija, sav postojeći kod i dokumentacija morali ažurirati.

## Posljedice

Postoje potencijalne posljedice ove odluke. 

* Ako novi članovi tima koji se pridružuju projektu nisu upoznati s konvencijom imenovanja snake_case, to može dovesti do zabune i pogrešaka u razvoju. Međutim, budući da je snake_case široko korištena konvencija, takav je rizik minimalan. 
  
* Ako se u projektu koriste drugi alati ili okviri koji su uvelike utemeljeni na konvenciji camelCase, može biti potreban dodatni trud za pretvorbu između konvencija imenovanja. Međutim, to nije značajna briga jer je projekt standardiziran na konvenciji snake_case. 
 
Sveukupno, odluka o korištenju konvencije imenovanja snake_case za krajnje točke REST API-ja rezultira dosljednim, čitljivim i industrijski standardnim pristupom, a istodobno je lako provediva i održiva.

<h6>Izvor: ovu stranicu generirao je ChatGPT, a zatim je uređena radi jasnoće i oblika.</h6>