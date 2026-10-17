# Saitin sauye-sauyen muhalli

Abubuwan da ke ciki:

* [Taƙaitawa](#taƙaitawa)
  * [Matsala](#matsala)
  * [Shawara](#shawara)
  * [Matsayi](#matsayi)
* [Cikakkun bayanai](#cikakkun-bayanai)
  * [Zato](#zato)
  * [Ƙuntatawa](#ƙuntatawa)
  * [Ra’ayoyi](#raayoyi)
  * [Hujja](#hujja)
  * [Tasiri](#tasiri)
* [Mai alaƙa](#mai-alaƙa)
  * [Shawarwari masu alaƙa](#shawarwari-masu-alaƙa)
  * [Buƙatu masu alaƙa](#buƙatu-masu-alaƙa)
  * [Kayayyakin da aka samar masu alaƙa](#kayayyakin-da-aka-samar-masu-alaƙa)
  * [Ƙa’idoji masu alaƙa](#ƙaidoji-masu-alaƙa)
* [Bayanan kula](#bayanan-kula)


## Taƙaitawa


### Matsala

Muna son aikace-aikacenmu su kasance masu saitawa fiye da kayayyakin da aka samar/binaries/tushe, ta yadda gini ɗaya zai iya yin aiki daban dangane da muhallin ɗora shi.

  * Don cimma haka, muna son amfani da saitin sauye-sauyen muhalli.

  * Muna son sarrafa saitin ta amfani da fayiloli da za mu iya sarrafa nau’insu.

  * Muna son samar da wasu sauƙin ƙwarewar masu haɓakawa, kamar sanin abin da za a iya saitawa da duk wasu tsoffin ƙima masu dacewa.


### Shawara

An yanke shawara kan fayilolin .env tare da fayil ɗin tsoffin ƙima da fayil ɗin tsari masu alaƙa.


### Matsayi

An yanke shawara. A buɗe don la’akari da sababbin iyawa idan sun taso.


## Cikakkun bayanai


### Zato

Muna fifita raba lambar aikace-aikace da lambar muhalli. Muna zaton aikace-aikacen yana buƙatar yin aiki daban a muhalli daban-daban, kamar muhallin ci gaba, muhallin gwaji, muhallin nuni, muhallin samarwa, da sauransu.

Muna fifita ayyukan masana’antu na “12 factor app” kuma har ma fiye da haka aikin da ke da alaƙa na “15 factor app”.

Da yawa daga cikin ayyukanmu na baya sun yi amfani da ƙa’idar fayil `.env` ko makamancin kundin `.env`. Akwai al’ada ta yau da kullum ta ajiye waɗannan a wajen sarrafa nau’i, kuma maimakon haka a yi amfani da wata hanya ta daban don ɗora su, sarrafa nau’insu, da kula da su.


### Ƙuntatawa

Muna son ajiye sirri a wajen tsarin sarrafa nau’i (VCS) na sarrafa lambar tushe (SCM).

Muna da niyyar dacewa da shahararrun tsarin manhaja da laburare. Misali, Node yana da module “dotenv” don karanta saitin sauye-sauyen muhalli.


### Ra’ayoyi

Mun yi la’akari da hanyoyi kaɗan:

  * Ajiye saiti a cikin aikace-aikacen kamar a fayil `config.js`.

  * Ajiye saiti a cikin muhalli kamar a fayil `.env`.

  * Ɗauko saiti daga wuri sananne kamar sabar lasisi.


### Hujja

Mun zaɓi hanyar fayil .env saboda:

  * Ta shahara, ciki har da tsakanin ƙwararru.

  * Ta bi tsarin fayilolin `.env` waɗanda tawagoginmu suka yi amfani da su cikin nasara sau da yawa a ayyuka da yawa.

  * Mai sauƙi ce. Musamman, mun yarda a yanzu da muhimman musanyar da muke gani, kamar rashin iyawar bincike idan aka kwatanta da hanyar sabar lasisi.


### Tasiri 

Muna buƙatar gano hanyar raba saitin sauye-sauyen muhalli da ke na jama’a daga duk wani sarrafa sirri.


## Mai alaƙa


### Shawarwari masu alaƙa

Muna sa ran dukkan aikace-aikacenmu su yi amfani da wannan hanya.

Za mu shirya haɓaka duk aikace-aikacenmu da ke amfani da hanya mara iyawa sosai, kamar rubuta ƙima kai tsaye a cikin binary ko lambar tushe.

Za mu bar yadda yake duk aikace-aikacenmu da ke amfani da hanya mafi iyawa, kamar sabar lasisi.


### Buƙatu masu alaƙa

Za mu ƙara iyawar devops don fayilolin, ciki har da hooks, gwaje-gwaje, da haɗewa ta ci gaba.

Muna buƙatar horar da duk abokan tawagar masu haɓakawa kan wannan shawara.



### Kayayyakin da aka samar masu alaƙa

Kowane wuri da muke ɗora zai buƙaci nasa fayil ɗin .env da fayiloli masu alaƙa.


### Ƙa’idoji masu alaƙa

Mai sauƙin sakewa.


## Bayanan kula


Misalin fayil `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Misalin fayil `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Misalin fayil `.env.schema` da maɓallai kawai:

```env
NAME
EMAIL
```
