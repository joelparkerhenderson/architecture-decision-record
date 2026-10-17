# Tsarin tambarin lokaci

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

Muna son mu iya bin diddigin lokacin da abubuwa ke faruwa ta amfani da tambarin lokaci da kuma amfani da tsarin tambarin lokaci mai daidaito wanda ke aiki da kyau a duk tsarukanmu da tsarukan wasu kamfanoni.

Muna mu’amala da tsarukan da ke da tsarin tambarin lokaci daban-daban:

* Saƙonnin JSON ba su da tsarin tambarin lokaci na asali, don haka muna buƙatar zaɓar yadda za a mayar da tambarin lokaci zuwa zare, da mayar da zare zuwa tambarin lokaci, wato yadda za a yi serialize/deserialize.

* Wasu aikace-aikace an saita su don amfani da lokacin gida, maimakon lokacin UTC. Wannan na iya zama da amfani ga ayyukan da dole ne su daidaita da lokacin gida, kamar ayyukan da ke tayar da abubuwan da suka faru bisa lokacin gida.

* Wasu tsarukan suna da buƙatu da iyawar daidaiton lokaci daban-daban, kamar amfani da ƙudurin lokaci na dakiku da milli-dakiku da nano-dakiku. Misali, umarnin `date` na tsarin aiki na Linux yana amfani da tsohon daidaiton lokaci na dakiku, yayin da kasuwar hannayen jari ta Nasdaq ke son tsohon daidaiton lokaci na nano-dakiku.


### Shawara

Mun zaɓi ma’aunin tsarin tambarin lokaci ISO 8601 mai daidaiton nano-dakiku, musamman “YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ”.

Tsarin yana nuna shekara, wata, rana, awa, minti, daƙiƙa, nano-dakiku, da yankin lokaci na Zulu wato UTC, GMT.


### Matsayi

An yanke shawara.


## Cikakkun bayanai


### Zato

Muna buƙatar sarrafa waɗannan zaren rubutu na tambarin lokaci, don mayar da tambarin lokaci zuwa zare (wato serialize) da mayar da zare zuwa tambarin lokaci (wato deserialize).

Muna son tsari wanda gabaɗaya yake da sauƙin amfani, sauƙin sauyawa, da sauƙin karantawa ga mutum.

Muna son dacewa da faffadan tsarukan waje da ba za mu iya sarrafawa ba, kamar tsarukan nazari, tsarukan rumbun bayanai, tsarukan kuɗi.


### Ƙuntatawa

Wasu tsarukan suna da iyakokin daidaiton lokaci. Misali, umarnin `date` na tsarin aiki na macOS na iya buga daidaiton lokaci a dakiku, amma ba a nano-dakiku ba.


### Ra’ayoyi

Mun yi la’akari da jerin zaɓuɓɓuka:

* Unix epoch wato lamba ɗaya mai ƙaruwa.

* Tsarin rubutu a taƙaice “YYYYMMDDTHHMMSSNNNNNNNNN”.

* Amfani da yankin lokaci na gida da yankin lokaci na UTC.


### Hujja

Don amfani na yau da kullum, muna daraja sauƙin karantawa/rubutu ga mutane fiye da gudun/girman tsantsa.

Don amfani na yau da kullum, muna son tsari da ke aiki daidai a tsarukan inji, kuma yana aiki da kyau da hannu, kamar rubuta bayanan samfuri, karanta fitarwar JSON, grep a fayil log, da sauransu.

Don amfani mara na yau da kullum, kamar lissafi mai babban aiki, muna sa ran za mu so inganta duk tsarin rubutu da muka zaɓa ta mayar da rubutun zuwa tsari mafi sauri, kamar nau’in abu na kwanan wata na ciki na harshen shirye-shirye. Don haka tsarin rubutu ba shi da muhimmanci sosai ga HPC.


### Tasiri

Tsarukanmu daban-daban na rubutu da tsarukan lokaci za su haɗu a kan wannan tsari.


## Mai alaƙa


### Shawarwari masu alaƙa

Wataƙila muna son hanya mai sauri/sauƙi ta bin diddigin bambancin lokaci wato tsawon lokaci. Waɗannan suna da sauƙi da tambarin lokaci na Unix epoch.


### Buƙatu masu alaƙa

Wataƙila muna son daidaita shawararmu misali idan muna da buƙata mai alaƙa ta takamaiman nau’in tambarin saƙon log, kamar na Splunk, Sumo, ELK, da sauransu.


### Kayayyakin da aka samar masu alaƙa

Masu tsara tsari da masu fassara na harshe:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Misalan Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Misalan SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Ƙa’idoji masu alaƙa

Mai sauƙin sakewa. Za mu iya sauyawa cikin sauƙi zuwa wani tsari daban, kamar Unix epoch.

Jinkirta ingantawa kafin lokaci. Don amfani na yau da kullum ba mu damu sosai da ƴan ƙarin haruffa ba kamar tsarin da ke amfani da dashes da colons.


## Bayanan kula

Ƙara bayanan kula a nan.
