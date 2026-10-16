# Zapis arhitekturne odločitve: urejevalniki programske kode

## Kontekst

Urejevalniki programske kode so bistveno orodje za razvijalce pri pisanju in urejanju kode. Na voljo je veliko urejevalnikov kode, od katerih ima vsak svoj nabor funkcij, prednosti in slabosti. Namen tega ADR je dokumentirati arhitekturne odločitve, sprejete za urejevalnike programske kode.

## Prednostne naloge

Arhitektura urejevalnikov programske kode naj daje prednost naslednjemu:

* **Modularnost**: Urejevalnik kode naj bo zasnovan modularno, tako da ga lahko razvijalci po potrebi prilagajajo in razširjajo. To omogoča prilagodljivo arhitekturo, ki se lahko prilagodi potrebam različnih razvijalcev in ekip.

* **Zmogljivost**: Urejevalnik kode naj bo zmogljiv in odziven, da lahko razvijalci delajo učinkovito, ne da bi jih orodje, ki ga uporabljajo, upočasnjevalo.

* **Uporabniški vmesnik**: Uporabniški vmesnik naj bo intuitiven in enostaven za uporabo, da se lahko razvijalci osredotočijo na svojo kodo, namesto da bi se otepali z urejevalnikom.

* **Razširljivost z vtičniki**: Urejevalnik kode naj bo zasnovan tako, da omogoča preprosto razširitev z vtičniki in integracijami tretjih oseb.

* **Združljivost**: Urejevalnik kode naj bo združljiv s širokim naborom programskih jezikov in tehnologij, zaradi česar bo uporabno orodje za širok krog razvijalcev.

## Odločitev

Na podlagi teh prednostnih nalog naj bo arhitektura urejevalnikov programske kode zasnovana z naslednjimi komponentami:

* **Jedro**: Ta komponenta zagotavlja osnovno funkcionalnost urejevalnika kode, kot so barvanje sintakse, urejanje besedila in upravljanje datotek.

* **UI**: Ta komponenta zagotavlja uporabniški vmesnik urejevalnika kode, vključno z meniji, orodnimi vrsticami in bližnjicami na tipkovnici.

* **Vtičniki**: Ta komponenta razvijalcem omogoča razširitev funkcionalnosti urejevalnika kode z namestitvijo vtičnikov tretjih oseb. Vtičniki lahko zagotovijo dodatne funkcije, kot so dopolnjevanje kode, preverjanje kode (linting) ali razhroščevanje.

* **Integracije**: Ta komponenta omogoča, da se urejevalnik kode integrira z drugimi orodji in tehnologijami, kot so sistemi za nadzor različic, sistemi za gradnjo ali orodja za razhroščevanje.

## Utemeljitev

Modularnost urejevalnika kode razvijalcem omogoča, da ga po potrebi prilagajajo in razširjajo. To je pomembno, ker imajo različni razvijalci in ekipe različne potrebe in poteke dela, prilagodljiva arhitektura pa lahko te razlike upošteva.

* **Zmogljivost**: ključna, ker morajo razvijalci delati učinkovito, ne da bi jih orodja upočasnjevala. Zmogljiv urejevalnik kode je bistven za produktivnost in lahko razvijalcem pomaga ohraniti osredotočenost in koncentracijo.

* **UI**: pomemben, ker razvijalcem omogoča, da se osredotočijo na svojo kodo, namesto da bi se otepali z urejevalnikom. To lahko vodi do večje produktivnosti in manj frustracij pri razvijalcih.

* **Razširljivost z vtičniki**: zmogljiva, ker omogoča prilagoditev urejevalnika kode različnim potrebam in potekom dela. Vtičniki in integracije tretjih oseb lahko zagotovijo dodatne funkcije in zmožnosti, ki niso vključene v jedrni urejevalnik.

* **Združljivost**: dragocena, ker omogoča uporabo urejevalnika kode s širokim naborom programskih jezikov in tehnologij. To naredi urejevalnik uporabnejše orodje za širok krog razvijalcev.

Komponente jedra, vtičnikov, integracij in UI zagotavljajo jasno ločitev odgovornosti in omogočajo modularno arhitekturo, ki jo je mogoče preprosto razširiti in prilagoditi. Ta arhitektura je prilagodljiva, zmogljiva in združljiva s širokim naborom programskih jezikov in tehnologij, zaradi česar je uporabno orodje za razvijalce.
