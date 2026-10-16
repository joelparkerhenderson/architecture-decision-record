# Zapis arhitekturne odločitve: snake_case ali camelCase za API REST?

Odločitev: za končne točke API REST se bo uporabljala konvencija poimenovanja snake_case

Stanje: Sprejeto

## Kontekst

Pri konvencijah poimenovanja za API REST sta priljubljeni dve obliki: snake_case in camelCase. Pri snake_case so besede v imenu ločene s podčrtaji, pri camelCase pa je prva beseda imena napisana z malo začetnico, naslednje besede pa imajo veliko začetnico. Ta odločitev bo določila, katero konvencijo poimenovanja je treba uporabljati za API REST.

## Gonilniki odločitve

- Doslednost z obstoječimi konvencijami poimenovanja v projektu

- Berljivost in jasnost za vsakogar, ki bo morda delal na API

- Usklajenost z najboljšimi praksami panoge za konvencije poimenovanja API REST

- Enostavnost izvedbe in vzdrževanja

## Odločitev

Za končne točke API REST se bo uporabljala konvencija poimenovanja snake_case. To izbiro vodijo naslednji dejavniki:

1. **Doslednost**: Projekt že uporablja konvencijo poimenovanja snake_case za vse končne točke in koristno bi bilo to konvencijo ohraniti, da zagotovimo doslednost v celotnem projektu.

2. **Berljivost in jasnost**: Konvencija snake_case je bolj berljiva in lažja za razumevanje. Podčrtaji zagotavljajo jasno ločitev med besedami, zato je ime lažje razčleniti in razumeti njegov pomen.

3. **Usklajenost z najboljšimi praksami panoge**: Konvencija snake_case se v panogi široko uporablja in velja za najboljšo prakso za API REST, zato je dobra izbira za projekt.

4. **Enostavnost izvedbe in vzdrževanja**: Ohranitev obstoječe konvencije poimenovanja je enostavnejša za izvedbo in vzdrževanje, saj bi bilo treba ob izbiri nove konvencije posodobiti vso obstoječo kodo in dokumentacijo.

## Posledice

Ta odločitev ima možne posledice. 

* Če novi člani ekipe, ki se pridružijo projektu, konvencije poimenovanja snake_case ne poznajo, lahko to vodi do zmede in napak pri razvoju. Ker pa je snake_case široko uporabljena konvencija, je tako tveganje minimalno. 
  
* Če se v projektu uporabljajo druga orodja ali ogrodja, ki so močno zasnovana na konvenciji camelCase, bo morda potreben dodaten trud za pretvorbo med konvencijami poimenovanja. Vendar to ni pomembna skrb, ker je projekt standardiziran na konvencijo snake_case. 
 
Na splošno odločitev za uporabo konvencije poimenovanja snake_case za končne točke API REST vodi do doslednega, berljivega pristopa v skladu s standardi panoge, ki ga je hkrati enostavno izvesti in vzdrževati.

<h6>Zasluge: to stran je ustvaril ChatGPT, nato pa je bila urejena zaradi jasnosti in oblike.</h6>
