# Tsarin rikodin shawarar gine-gine na AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Rikodin shawarar gine-gine (ADR) takarda ce da ke bayyana zaɓin da tawaga ta yi game da wani muhimmin ɓangare na gine-ginen manhajar da take shirin ginawa. Kowane ADR yana bayyana shawarar gine-gine, mahallinta, da sakamakonta. ADR suna da yanayi don haka suna bin zagayen rayuwa. Don misalin ADR, duba ƙari.

Tsarin ADR yana fitar da tarin rikodin shawarwarin gine-gine. Wannan tarin yana ƙirƙirar rajistar shawarwari. Rajistar shawarwari tana ba da mahallin aikin da kuma cikakkun bayanan aiwatarwa da ƙira. Membobin aiki suna duba kanun kowane ADR don samun bayyani na mahallin aikin. Suna karanta ADR don nutsewa cikin aiwatarwa da zaɓin ƙira na aikin.

Lokacin da tawaga ta karɓi ADR, ya zama maras canzawa. Idan sababbin fahimta suna buƙatar wata shawara dabam, tawagar tana ba da shawarar sabon ADR. Lokacin da tawagar ta karɓi sabon ADR, yana maye gurbin ADR na baya.

## Fannin tsarin ADR

Ya kamata membobin aiki su ƙirƙiri ADR ga kowace shawara mai muhimmanci ta fuskar gine-gine wadda ke shafar aikin manhaja ko samfur, ciki har da waɗannan (Richards da Ford 2020):

* Tsari (misali, tsarin kamar microservices)

* Buƙatu marasa aiki (tsaro, samuwa mai yawa, da juriyar kuskure)

* Dogaro (haɗin kayan aiki)

* Hanyoyin sadarwa (API da kwangilolin da aka wallafa)

* Dabarun gini (laburare, tsarin aiki, kayan aiki, da hanyoyi)

* Buƙatu masu aiki da marasa aiki su ne mafi yawan shigarwa na tsarin ADR.


## Abubuwan da ke cikin ADR

Lokacin da tawaga ta gano buƙatar ADR, wani memba na tawaga yana fara rubuta ADR bisa samfurin da ke aiki a duk aikin. (Duba ƙungiyar ADR ta GitHub don samfuran misali.) Samfurin yana sauƙaƙa ƙirƙirar ADR kuma yana tabbatar da ADR ya ɗauki duk bayanan da suka dace. Aƙalla, kowane ADR ya kamata ya bayyana mahallin shawarar, shawarar kanta, da sakamakon shawarar ga aikin da abubuwan da zai kawo. (Don misalan waɗannan sassa, duba ƙari.) Ɗaya daga cikin mafi ƙarfin fannonin tsarin ADR shi ne cewa yana mai da hankali ne kan dalilin shawarar maimakon yadda tawagar ta aiwatar da ita. Fahimtar dalilin da ya sa tawagar ta yanke shawarar yana sauƙaƙa wa sauran membobin tawaga su karɓi shawarar, kuma yana hana sauran masu gine-gine waɗanda ba su shiga tsarin yanke shawarar ba su soke ta a nan gaba.


## Tsarin karɓar ADR

Kowane memba na tawaga zai iya ƙirƙirar ADR, amma ya kamata tawagar ta kafa ma’anar mallaka ga ADR. Kowane marubuci wanda shi ne mai mallakar ADR ya kamata ya kula kuma ya sanar da abubuwan da ke cikin ADR a hankali. Don fayyace wannan mallaka, wannan jagorar tana kiran marubutan ADR masu mallakar ADR a sassan da ke gaba. Sauran membobin tawaga na iya ba da gudummawa ga ADR koyaushe. Idan abubuwan da ke cikin ADR sun canza kafin tawagar ta karɓi ADR, mai mallaka ya kamata ya amince da waɗannan canje-canje.

Bayan tawagar ta gano shawarar gine-gine da mai mallakarta, mai mallakar ADR yana ba da ADR a yanayin **An ba da shawara** a farkon tsarin. ADR a yanayin An ba da shawara suna shirye don bita.

Daga nan mai mallakar ADR yana fara tsarin bita na ADR. Manufar tsarin bitar ADR ita ce a yanke shawara ko tawagar ta karɓi ADR, ta ƙaddara yana buƙatar sake aiki, ko ta ƙi ADR. Tawagar aikin, ciki har da mai mallaka, tana bitar ADR. Taron bita ya kamata ya fara da lokacin da aka keɓe don karanta ADR. A matsakaici, minti 10 zuwa 15 ya kamata su isa. A wannan lokacin, kowane memba na tawaga yana karanta takardar kuma yana ƙara sharhi da tambayoyi don yiwa batutuwan da ba su bayyana alama. Bayan matakin bita, mai mallakar ADR yana karanta kuma yana tattauna kowane sharhi da tawagar.

Idan tawagar ta sami abubuwan aiki don inganta ADR, yanayin ADR yana kasancewa **An ba da shawara**. Mai mallakar ADR yana tsara ayyukan, kuma, tare da haɗin gwiwar tawagar, yana ƙara wanda aka ba wa kowane aiki. Kowane memba na tawaga na iya ba da gudummawa kuma ya warware abubuwan aiki. Alhakin mai mallakar ADR ne ya sake tsara tsarin bita.

Tawagar kuma za ta iya yanke shawarar ƙin ADR. A wannan yanayin, mai mallakar ADR yana ƙara dalilin ƙi don hana tattaunawa a nan gaba kan wannan batu. Mai mallaka yana canza yanayin ADR zuwa **An ƙi**.

Idan tawagar ta amince da ADR, mai mallaka yana ƙara tambarin lokaci, sigar, da jerin masu ruwa da tsaki. Daga nan mai mallaka yana sabunta yanayin zuwa **An karɓa**.

ADR da rajistar shawarwari da suke ƙirƙira suna wakiltar shawarwarin da tawagar ta yanke kuma suna ba da tarihin duk shawarwari. Tawagar tana amfani da ADR a matsayin tunani yayin bitar lamba da gine-gine duk inda zai yiwu. Baya ga yin bitar lamba, ayyukan ƙira, da ayyukan aiwatarwa, ya kamata membobin tawaga su duba ADR don shawarwari masu dabara na samfurin.

A matsayin kyakkyawar al’ada, kowane canjin manhaja ya kamata ya wuce bitar abokan aiki kuma yana buƙatar amincewa ɗaya aƙalla. Yayin bitar lamba, mai bitar lamba na iya samun canje-canjen da suka karya ADR ɗaya ko fiye. A wannan yanayin, mai bita yana roƙon marubucin canjin lamba ya sabunta lambar, kuma yana raba hanyar haɗin ADR. Lokacin da marubucin ya sabunta lambar, abokan aiki masu bita suna amincewa da ita kuma a haɗa ta cikin babban tushen lamba.


## Tsarin bitar ADR

Ya kamata tawagar ta ɗauki ADR a matsayin takardu marasa canzawa bayan tawagar ta karɓa ko ta ƙi su. Canje-canje ga ADR da ke akwai yana buƙatar ƙirƙirar sabon ADR, kafa tsarin bita ga sabon ADR, da amincewa da ADR. Idan tawagar ta amince da sabon ADR, mai mallaka ya kamata ya canza yanayin tsohon ADR zuwa **An maye gurbinsa**.
