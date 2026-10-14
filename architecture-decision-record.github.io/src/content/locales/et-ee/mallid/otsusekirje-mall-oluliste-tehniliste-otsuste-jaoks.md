# Otsusekirje mall oluliste tehniliste otsuste (ITD) jaoks

See on oluliste tehniliste otsuste (Important Technical Decisions, ITD) mall, mida kirjeldatakse väljaandes
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

ITD on ADR-i keskendunud areng, mis on optimeeritud kiiruse, selguse ja
juhtkonna kinnitamise jaoks. Kui ADR dokumenteerib, mis otsustati, siis ITD on lean,
otsus-ees artefakt, mis teeb otsuse enda üle vaadatavaks, nii et huvirühmad saavad selle kiiresti
läbi lugeda ja hõlpsasti vaidlustada. ITD-d sobivad tehniliste otsuste jaoks, mis ei ole rangelt
arhitektuuri kohta, nagu mudeli, teegi või CI/CD strateegia valimine.

Igasse ITD-faili kirjuta need jaotised:

# Pealkiri

Sõnasta otsus ise, mitte teema kirjeldus.
Näiteks "Kasuta seadmesiseseks tõlkimiseks Qwen2.5 1.5B Instruct".

## Probleem

Üks lause, mis kirjeldab, mida üritame lahendada.

## Kaalutud valikud

Hinnatud alternatiivid, valitud valik **rasvases kirjas**.

## Põhjendus

Ainult otsustavad tegurid, mis valikuni viisid, mitte
kõigi plusside ja miinuste ammendav loetelu.

## Märkused

Valikuline. Lisakontekst, mida tasub jäädvustada, nagu piirangud, eeldused või lingid.
