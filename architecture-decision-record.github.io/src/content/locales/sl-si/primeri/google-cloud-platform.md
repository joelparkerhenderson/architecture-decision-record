# Zapis arhitekturne odločitve za Google Cloud Platform

## Kontekst

Google Cloud Platform (GCP) je ugledna platforma za računalništvo v oblaku, ki ponuja različne oblačne storitve, vključno z rešitvami za računanje, shranjevanje in omrežje. Namen tega ADR je dokumentirati arhitekturne odločitve, sprejete za razvoj in izvedbo infrastrukture, ki temelji na GCP, za našo organizacijo.

## Odločitev

Naša organizacija se je odločila, da bo kot oblačno infrastrukturo za svojo aplikacijo uporabljala Google Cloud Platform. Glavni premisleki za to odločitev so:

   - Stroškovna učinkovitost

   - Razširljivost

   - Zanesljivost

   - Prilagodljivost

## Izbire

Za izpolnitev naših zahtev so bile izbrane naslednje storitve GCP:

   - Compute Engine za virtualne stroje in računalniške vire

   - Cloud Storage za shranjevanje objektov in gostovanje datotek

   - Cloud SQL za upravljano storitev podatkovne baze

   - Firebase za razvoj in gostovanje aplikacij

## Utemeljitev

   - Stroškovna učinkovitost: Google Cloud Platform je v primerjavi z drugimi oblačnimi platformami zelo stroškovno učinkovit, zato je privlačna možnost za organizacije s proračunskimi omejitvami.

   - Razširljivost: Infrastruktura GCP, ki jo je enostavno skalirati, omogoča obvladovanje poljubne količine prometa v realnem času.

   - Zanesljivost: Upravljane storitve GCP nudijo visoko zanesljivost z avtomatiziranimi varnostnimi kopijami in zmožnostmi obnovitve po nesrečah, ki zagotavljajo visoko razpoložljivost virov in podatkov.

   - Prilagodljivost: Platforma ponuja različna orodja in storitve na različnih področjih, kot so umetna inteligenca, analitika podatkov in IoT, zaradi česar je zelo vsestranska.

## Posledice

Selitev na Google Cloud Platform bo zahtevala usposabljanje naših ekip za storitve GCP, ponovno zasnovo aplikacije, da bo združljiva z izbranimi storitvami, in posodobitev infrastrukturne kode za podporo storitvam GCP. Vendar se pričakuje, da bomo po zaključeni selitvi imeli zelo razširljivo, zanesljivo in stroškovno učinkovito infrastrukturo za gostovanje naše aplikacije. Prav tako bomo morali obvladovati tekoče stroške zagotavljanja virov na GCP.

## Sklep

Google Cloud Platform je odlična izbira za našo oblačno infrastrukturo zaradi stroškovne učinkovitosti, razširljivosti, zanesljivosti in prilagodljivosti. Z uporabo izbranih storitev lahko za našo aplikacijo zagotovimo zelo razpoložljivo in robustno infrastrukturo.
