# Lingwi tal-programmazzjoni

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

Neħtieġu nagħżlu lingwi tal-programmazzjoni għas-software tagħna. Għandna żewġ bżonnijiet ewlenin: lingwa tal-programmazzjoni front-end adattata għal applikazzjonijiet tal-web, u lingwa tal-programmazzjoni back-end adattata għal applikazzjonijiet tas-server.


### Deċiżjoni

Qed nagħżlu TypeScript għall-front-end.

Qed nagħżlu Rust għall-back-end.


### Stat

Deċiż. Aħna miftuħin għal alternattivi ġodda hekk kif jinqalgħu.


## Dettalji


### Suppożizzjonijiet

L-applikazzjonijiet front-end huma tipiċi:

  * Utenti u interazzjonijiet tipiċi

  * Browsers u sistemi tipiċi

  * Żviluppi u deployments tipiċi

L-applikazzjonijiet front-end x'aktarx jevolvu malajr:

  * Irridu niżguraw żviluppi, deployments, iterazzjonijiet, eċċ. faċli u mgħaġġla.

  * Napprezzaw il-provabbiltà, bħas-sikurezza tat-tipi, u aħna kuntenti nagħmlu ftit aktar xogħol biex niksbuha.

  * Ma neħtieġux kompatibbiltà legacy.

L-applikazzjonijiet back-end huma ogħla mit-tipiku:

  * Għanijiet ogħla mit-tipiku għall-kwalità, speċjalment il-provabbiltà, l-affidabbiltà, is-sigurtà, eċċ.

  * Għanijiet ogħla mit-tipiku għal kważi-żmien-reali, jiġifieri ma rridux pawżi minħabba l-garbage collection tal-magna virtwali.

  * Għanijiet ogħla mit-tipiku għall-programmazzjoni funzjonali, speċjalment għall-parallelizzazzjoni, l-ipproċessar multi-core, u s-sikurezza tal-memorja.

Naċċettaw veloċitajiet aktar baxxi ta' compile-time favur is-sikurezza fil-compile-time u veloċitajiet tar-runtime.


### Restrizzjonijiet

Għandna restrizzjoni qawwija fuq lingwi li jistgħu jintużaw ma' servizzi ewlenin ta' fornituri tal-cloud għal funzjonijiet, bħal Amazon Lambda.


### Pożizzjonijiet

Ikkunsidrajna dawn il-lingwi:

  * C

  * C++

  * Clojure
  
  * Elixir
  
  * Erlang
  
  * Elm
  
  * Flow
  
  * Go
  
  * Haskell
  
  * Java
  
  * JavaScript
  
  * Kotlin
  
  * Python
  
  * Ruby
  
  * Rust
  
  * TypeScript



### Argument

Sommarju għal kull lingwa:

  * C: miċħuda minħabba sikurezza baxxa; Rust tista' tagħmel kważi kollox aħjar.

  * C++: miċħuda għax hija taħlita mħawda; Rust tista' tagħmel kważi kollox aħjar.

  * Clojure: immudellar eċċellenti; l-aħjar approssimazzjoni ta' Lisp; runtime kbir fuq il-JVM.
  
  * Elixir: runtime eċċellenti inkluża d-deployabbiltà u l-konkorrenza; esperjenza eċċellenti tal-iżviluppatur; ekosistema relattivament żgħira.

  * Erlang: runtime eċċellenti inkluża d-deployabbiltà u l-konkorrenza; esperjenza sfidanti tal-iżviluppatur; ekosistema relattivament żgħira.

  * Elm: tidher wisq promettenti; IBM qed tippubblika studji ta' każ ewlenin b'riżultati tajbin; ekosistema iżgħar.

  * Flow: titjib interessanti fuq JavaScript; madankollu; l-iżviluppaturi qed jitbiegħdu minnha.

  * Go: esperjenza eċċellenti tal-iżviluppatur; konkorrenza eċċellenti; iżda rekord ta' deċiżjonijiet ħżiena li jxellfu l-lingwa.

  * Haskell: l-aħjar lingwa funzjonali; komunità iżgħar ta' żviluppaturi; ma kisbitx biżżejjed suċċessi ppubblikati fil-produzzjoni.

  * Java: runtime eċċellenti; ekosistema eċċellenti; esperjenza tal-iżviluppatur taħt il-livell.

  * JavaScript: l-aktar lingwa popolari li qatt kienet; l-aktar ekosistema mifruxa.

  * Kotlin: tirranġa tant minn Java; appoġġ eċċellenti minn JetBrains; każijiet ippubblikati tajbin ta' portar minn Java għal Kotlin.
  
  * Python: l-aktar lingwa popolari għall-amministrazzjoni tas-sistemi; għodod kbar ta' analitika; frameworks tajbin tal-web; iżda abbandunata minn Google favur Go.

  * Ruby: l-aħjar esperjenza tal-iżviluppatur li qatt kien hemm; l-aħjar frameworks tal-web; l-isbaħ komunità; iżda bil-mod ħafna; kemmxejn diffiċli biex tiġi ppakkjata.

  * Rust: l-aħjar lingwa ġdida; enfasi fuq żero-astrazzjoni; enfasi fuq il-konkorrenza; madankollu ekosistema relattivament żgħira; u għandha limiti deliberati fuq xi tipi ta' aċċelerazzjonijiet tal-kompilatur eż. l-aċċess dirett għall-memorja jrid ikun espliċitament unsafe.

  * TypeScript: iżżid tipi ma' JavaScript; transpiler kbir; enfasi dejjem tikber tal-iżviluppaturi fuq il-portar minn JavaScript għal TypeScript; appoġġ qawwi minn Microsoft.

Iddeċidejna li l-VMs għandhom sett ta' kompromessi li ma neħtieġuhomx bħalissa, bħall-kumplessità addizzjonali li tipprovdi kapaċitajiet fir-runtime.

Aħna nemmnu li d-deċiżjoni ewlenija tagħna hija mmexxija minn żewġ tħassib trasversali:

  * Għall-aqwa veloċità fir-runtime u l-aktar aċċess dirett għas-sistema, nagħżlu JavaScript u C.

  * Għal veloċità fir-runtime qrib l-aqwa u aċċess għas-sistema qrib l-aktar dirett, nagħżlu TypeScript u Rust.

Msemmijin onorevolment huma l-lingwi VM u l-frameworks tal-web li konna nagħżlu kieku rridu lingwa VM:

  * Clojure u Luminus

  * Java u Spring

  * Elixir u Phoenix


### Implikazzjonijiet

L-iżviluppaturi front-end se jkollhom bżonn jitgħallmu TypeScript. Dan x'aktarx ikun kurva tat-tagħlim faċli jekk l-esperjenza primarja tal-iżviluppatur hija bl-użu ta' JavaScript.

L-iżviluppaturi back-end se jkollhom bżonn jitgħallmu Rust. Dan x'aktarx ikun kurva tat-tagħlim moderata jekk l-esperjenza primarja tal-iżviluppatur hija bl-użu ta' C/C++, u kurva tat-tagħlim iebsa jekk l-esperjenza primarja tal-iżviluppatur hija bl-użu ta' Java, Python, Ruby, jew lingwi simili b'memorja ġestita. 

TypeScript u Rust it-tnejn huma relattivament ġodda. Dan ifisser li ħafna għodod għad m'għandhomx dokumentazzjoni għal dawn il-lingwi. Pereżempju, il-pipeline tad-devops se jkollha bżonn tiġi ssettjata għal dawn il-lingwi, u s'issa, l-ebda waħda mill-għodod devops li qed nevalwaw m'għandha eżempji default għal dawn il-lingwi.

Il-ħinijiet tal-kompilazzjoni għal TypeScript u Rust huma pjuttost bil-mod. Parti minn dan jista' jkun minħabba l-ġdid tal-lingwi. Jista' jkun li rridu nħarsu lejn kif nimmitigaw il-ħinijiet bil-mod tal-kompilazzjoni, bħal compile-on-demand, compile-concurrency, eċċ.

L-appoġġ tal-IDE għal dawn il-lingwi għadu mhux mifrux kullimkien u għadu mhux ta' klassi ewlenija. Pereżempju, JetBrains tbiegħ l-IDE PyCharm għal appoġġ ta' klassi ewlenija għal Python, iżda ma tbiegħx IDE b'appoġġ ta' klassi ewlenija għal Rust; minflok, JetBrains tista' tuża plug-in ta' Rust li jipprovdi forsi 80% tal-appoġġ tal-lingwa Rust vis a vis l-appoġġ tal-lingwa Python.


## Relatati


### Deċiżjonijiet relatati

Se nimmiraw lejn għażliet tal-ekosistema li jaqblu ma' dawn il-lingwi.

Pereżempju, irridu nagħżlu IDE li għandha kapaċitajiet tajbin għal dawn il-lingwi.

Pereżempju, għall-qafas tagħna tal-web front-end, aħna aktar probabbli niddeċiedu fuq qafas li għandu t-tendenza li jimmira lejn TypeScript (eż. Vue) milli qafas li għandu t-tendenza li jimmira lejn JavaScript sempliċi (eż. React).


### Rekwiżiti relatati

Is-sett kollu tal-għodod tagħna jrid jappoġġa dawn il-lingwi.


### Artefatti relatati

Nistennew li jista' jkun li neżportaw xi sigrieti għal varjabbli tal-ambjent.


### Prinċipji relatati

Kejjel darbtejn, ibni darba. Qed nagħtu prijorità lil ftit sikurezza fuq ftit veloċità.

Ir-runtime huwa aktar prezzjuż mill-compile time. Qed nagħtu prijorità lill-użu tal-klijenti fuq l-użu tal-iżviluppaturi.


## Noti

Kwalunkwe noti hawn.
