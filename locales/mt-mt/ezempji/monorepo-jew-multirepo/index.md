# Monorepo jew multirepo

Werrej:

* [Sommarju](#sommarju)
  * [Kwistjoni](#kwistjoni)
  * [Deċiżjoni](#deċiżjoni)
  * [Stat](#stat)
* [Dettalji](#dettalji)
  * [Suppożizzjonijiet](#suppożizzjonijiet)
  * [Restrizzjonijiet](#restrizzjonijiet)
  * [Pożizzjonijiet](#pożizzjonijiet)
  * [Argument](#argument)
  * [Implikazzjonijiet](#implikazzjonijiet)
* [Relatati](#relatati)
  * [Deċiżjonijiet relatati](#deċiżjonijiet-relatati)
  * [Rekwiżiti relatati](#rekwiżiti-relatati)
  * [Artefatti relatati](#artefatti-relatati)
  * [Prinċipji relatati](#prinċipji-relatati)
* [Noti](#noti)


## Sommarju


### Kwistjoni

Il-proġett tagħna jinvolvi l-iżvilupp ta' tliet kategoriji ewlenin ta' software:

  * GUIs front-end
  * Servizzi middleware
  * Servers back-end

Meta nżviluppaw, is-sistema tagħna tal-kontroll tal-verżjonijiet (VCS) tal-ġestjoni tal-kodiċi sors (SCM) hija git.

Neħtieġu nagħżlu kif nużaw git biex niorganizzaw il-kodiċi tagħna.

L-għażla ta' livell għoli hija li niorganizzaw bħala "monorepo" jew "polyrepo" jew "ibrida":

  * Monorepo ifisser li npoġġu l-biċċiet kollha f'repo kbir wieħed
  * Polyrepo ifisser li npoġġu kull biċċa fir-repo tagħha stess
  * Ibrida tfisser taħlita ta' monorepo u polyrepo

Għal aktar jekk jogħġbok ara https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Deċiżjoni

Monorepo meta organizzazzjoni/tim/proġett ikun relattivament żgħir, u l-iterazzjoni mgħaġġla tkun ta' prijorità ogħla mill-żamma tal-istabbiltà.

Polyrepo meta organizzazzjoni/tim/proġett ikun relattivament kbir, u ż-żamma tal-istabbiltà tkun ta' prijorità ogħla mill-iterazzjoni mgħaġġla.


### Stat

Deċiż. Miftuħin biex nerġgħu nirrevedu jekk/meta jsiru disponibbli għodod ġodda għall-ġestjoni ta' monorepos u/jew polyrepos.


## Dettalji


### Suppożizzjonijiet

Il-kodiċi kollu li qed niżviluppaw huwa għall-offerti ta' organizzazzjoni waħda, u mhux għall-pubbliku ġenerali. Jiġifieri l-Broker-Dealer m'għandux l-għan li jkollu xi ħaġa bħal żviluppaturi voluntiera mill-pubbliku ġenerali.


### Restrizzjonijiet

Ir-restrizzjonijiet huma dokumentati tajjeb f'https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Pożizzjonijiet

Ikkunsidrajna monorepos fl-istil ta' Google, Facebook, eċċ. Aħna naħsbu li kwalunkwe kwistjoni ta' skalar ta' monorepo hija tant 'il bogħod fil-futur li se nkunu nistgħu nisfruttaw l-istess prattiki ta' Google u Facebook, sa meta nkunu neħtieġuhom.

Ikkunsidrajna polyrepos fl-istil ta' proġetti open source tipiċi ta' Git, bħal Google Android, Facebook React, eċċ. Aħna naħsbu li dawn huma l-aħjar għażla għall-parteċipazzjoni tal-pubbliku ġenerali (eż. kulħadd fid-dinja jista' jaħdem fuq il-kodiċi) u d-disponibbiltà individwali (eż. il-proġett jintuża waħdu, mingħajr ebda biċċa oħra).


### Argument

Meta organizzazzjoni/tim/proġett ikun relattivament żgħir, nagħżlu monorepo, għax l-iterazzjoni mgħaġġla hija ferm ogħla fil-prijorità mill-żamma tal-istabbiltà

Meta organizzazzjoni/tim/proġett ikun relattivament kbir, nagħżlu polyrepo, għax iż-żamma tal-istabbiltà hija ferm ogħla fil-prijorità mill-iterazzjoni mgħaġġla.


### Implikazzjonijiet

Jekk hemm pipeline eżistenti għal CI+CD, allura jista' jkun li neħtieġu naġġustawha biex tittestja proġetti multipli fi ħdan repo wieħed.

CI+CD jista' jieħu aktar ħin għal bini sħiħ ta' monorepo, għax CI+CD jista' jibni l-proġetti kollha fil-monorepo.

Jekk organizzazzjoni/tim/proġett jikber, allura monorepo se jkollu kwistjonijiet ta' skalar.

Il-kwistjonijiet ta' skalar tal-monorepo jistgħu jagħmlu tranżizzjoni għal polyrepo dejjem aktar siewja.

It-tranżizzjoni minn monorepo għal polyrepo hija kompitu devops sinifikanti, u se jkollha bżonn tiġi ppjanata, immaniġġjata, u mprogrammata.


## Relatati


### Deċiżjonijiet relatati

Se noħolqu deċiżjonijiet għall-għodod relatati biex jimmaniġġjaw monorepos (eż. Google Bazel) u polyrepos (eż. Lyft Refactorator).


### Rekwiżiti relatati

Neħtieġu nżviluppaw il-pipeline CI+CD biex taħdem tajjeb ma' git.


### Artefatti relatati

Nistennew li l-organizzazzjoni tar-repo jkollha artefatti relatati għall-provvediment, il-ġestjoni tal-konfigurazzjoni, l-ittestjar, u oqsma devops simili. 


### Prinċipji relatati

Faċilment riversibbli. Jekk il-monorepo ma jaħdimx fil-prattika, jew ma jkunx mixtieq mit-tmexxija, huwa sempliċi li jinbidel għal polyrepo.

Ossessjoni mal-klijent. Aħna napprezzaw li l-proġett jitpoġġa f'idejn il-klijenti, u nemmnu li monorepo jista' jwassalna hemm aktar malajr minn polyrepo, u jgħinna wkoll nirripetu aktar malajr.

Aħseb kbir. Google u Facebook huma sostenituri b'saħħithom ħafna tal-monorepos fuq il-polyrepos, għax l-offerti ewlenin kollha jistgħu jiġu żviluppati/ittestjati/mqiegħda flimkien.


## Noti

Żid kwalunkwe noti hawn.
