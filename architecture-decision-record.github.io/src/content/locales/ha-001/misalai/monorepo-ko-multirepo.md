# Monorepo ko multirepo

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

Aikinmu ya ƙunshi haɓaka manyan rukunoni uku na manhaja:

  * GUI na gaba
  * Ayyukan tsakiya
  * Sabobi na baya

Lokacin da muke haɓakawa, tsarin sarrafa nau’i (VCS) na sarrafa lambar tushe (SCM) ɗinmu shi ne git.

Muna buƙatar zaɓar yadda muke amfani da git don tsara lambarmu.

Zaɓin matakin sama shi ne a tsara a matsayin “monorepo” ko “polyrepo” ko “gauraye”:

  * Monorepo yana nufin muna sa dukkan guntuwa a cikin babban repo ɗaya
  * Polyrepo yana nufin muna sa kowane guntu a cikin nasa repo
  * Gauraye yana nufin wani haɗin monorepo da polyrepo

Don ƙarin bayani da fatan ku duba https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Shawara

Monorepo lokacin da ƙungiya/tawaga/aiki ƙanana ne, kuma saurin maimaitawa ya fi muhimmanci fiye da kiyaye dorewa.

Polyrepo lokacin da ƙungiya/tawaga/aiki manya ne, kuma kiyaye dorewa ya fi muhimmanci fiye da saurin maimaitawa.


### Matsayi

An yanke shawara. A buɗe don sake dubawa idan/lokacin da sababbin kayan aiki suka samu don sarrafa monorepos da/ko polyrepos.


## Cikakkun bayanai


### Zato

Duk lambar da muke haɓakawa don kayayyakin ƙungiya ɗaya ne, ba don jama’a ba. Wato Broker-Dealer ba shi da niyyar samun wani abu kamar masu haɓaka sa kai na jama’a.


### Ƙuntatawa

An rubuta ƙuntatawa da kyau a https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Ra’ayoyi

Mun yi la’akari da monorepos irin na Google, Facebook, da sauransu. Muna ganin duk matsalolin faɗaɗa monorepo suna da nisa a nan gaba har za mu iya amfani da ayyuka iri ɗaya da Google da Facebook, a lokacin da muke buƙatar su.

Mun yi la’akari da polyrepos irin na ayyukan buɗaɗɗen tushe na Git na yau da kullum, kamar Google Android, Facebook React, da sauransu. Muna ganin waɗannan su ne mafi kyawun zaɓi don shigar jama’a (misali kowa a duniya zai iya yin aiki a kan lambar) da samuwar kowane ɗaya (misali ana amfani da aikin shi kaɗai, ba tare da wasu guntuwa ba).


### Hujja

Lokacin da ƙungiya/tawaga/aiki ƙanana ne, muna zaɓar monorepo, domin saurin maimaitawa ya fi fifiko sosai fiye da kiyaye dorewa

Lokacin da ƙungiya/tawaga/aiki manya ne, muna zaɓar polyrepo, domin kiyaye dorewa ya fi fifiko sosai fiye da saurin maimaitawa.


### Tasiri

Idan akwai bututun CI+CD da ke akwai, to za mu iya buƙatar daidaita shi don gwada ayyuka da yawa a cikin repo ɗaya.

CI+CD zai iya ɗaukar ƙarin lokaci don cikakken gini na monorepo, domin CI+CD zai iya gina dukkan ayyukan da ke cikin monorepo.

Idan ƙungiya/tawaga/aiki ya girma, to monorepo zai fuskanci matsalolin faɗaɗawa.

Matsalolin faɗaɗa monorepo na iya sa sauyawa zuwa polyrepo ya ƙara zama mai daraja.

Sauyawa daga monorepo zuwa polyrepo babban aikin devops ne, kuma zai buƙaci a tsara shi, a sarrafa shi, kuma a shirya shi.


## Mai alaƙa


### Shawarwari masu alaƙa

Za mu ƙirƙiri shawarwari don kayan aikin sarrafa monorepos masu alaƙa (misali Google Bazel) da polyrepos (misali Lyft Refactorator).


### Buƙatu masu alaƙa

Muna buƙatar haɓaka bututun CI+CD ya yi aiki da kyau da git.


### Kayayyakin da aka samar masu alaƙa

Muna sa ran tsarin repo ya kasance yana da kayayyakin da aka samar masu alaƙa don samarwa, sarrafa saiti, gwaji, da makamantan fannonin devops. 


### Ƙa’idoji masu alaƙa

Mai sauƙin sakewa. Idan monorepo bai yi aiki a aikace ba, ko shugabanci ba ya son shi, abu ne mai sauƙi a sauya zuwa polyrepo.

Damuwa da Abokin Ciniki. Muna daraja sa aikin a hannun abokan ciniki, kuma mun yi imanin cewa monorepo na iya kai mu can da sauri fiye da polyrepo, kuma ya taimaka mana mu maimaita da sauri.

Yi tunani babba. Google da Facebook masu goyon bayan monorepos ne sosai fiye da polyrepos, domin duk manyan kayayyaki za a iya haɓaka/gwada/ɗora su tare.


## Bayanan kula

Ƙara duk wani bayanin kula a nan.
