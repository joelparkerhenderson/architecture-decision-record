# Arkitektúrákvörðunarskrá: vefforritarammi, allt innifalið, fullur stafli, fyrir sprotavöru

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Meginmarkmið:**  
Að smíða vefforrit þar sem greiðandi viðskiptavinir geta skráð sig inn, hlaðið upp skrám, unnið úr gögnum og skoðað skýrslur, með áherslu á lipra þróun, virkni fulls stafla og sterka samhæfni við gervigreindar-/vélnámstól, einkum Project Jupyter notebooks.

### Samhengi og kröfur:

1. **Lipur þróun (mikill forgangur)**: Sem sprotafyrirtæki þurfum við hraða þróun í áföngum og sveigjanleika. Lipurar starfsvenjur, svo sem hröð frumgerðasmíði, þróun í áföngum og aðlögunarhæfni að breytingum, eru lykilatriði í þróunarlotu okkar.

2. **Rammi fyrir fullan stafla (mikill forgangur)**: Við stefnum að því að lágmarka yfirbyggingu með því að velja ramma sem getur meðhöndlað bæði bakenda og framenda á skilvirkan hátt og dregur úr þörf fyrir sérstaka ramma á framenda.

3. **Samhæfni við gervigreindar-/vélnámstól (mikill forgangur)**: Hæfileikinn til að samþættast auðveldlega við gagnagreiningartól eins og Jupyter notebooks og gagnavísindavistkerfi Python (NumPy, Pandas, TensorFlow o.s.frv.) er nauðsynlegur. Þetta myndi auðvelda skilvirka gagnavinnslu og skýrslugerð.

4. **Viðmið með lítinn forgang**:
   - **Keyrsluhraði**: Þótt afköst skipti máli eru þau ekki mikilvægasti þátturinn í upphafi því við höfum meiri áhyggjur af þróunarhraða og fullkomleika eiginleika.
   - **Stigstærð**: Við gerum ráð fyrir vexti, en hægt er að taka á áhyggjum af stigstærð síðar og þetta er ekki aðalkrafa núna.
   - **Afturábak samhæfni**: Við einbeitum okkur að núverandi tækni og höfum ekki miklar áhyggjur af afturábak samhæfni við eldri kerfi.

### Rammar sem voru metnir:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Yfirlit**:  
Django er veframmi á háu stigi fyrir Python sem stuðlar að hraðri þróun og hreinni, hagnýtri hönnun. Hann er þekktur fyrir „allt innifalið“ hugmyndafræði sína, sem þýðir að hann inniheldur marga eiginleika eins og auðkenningu, leiðarval, ORM og meðhöndlun eyðublaða beint úr kassanum.

**Styrkleikar**:  
- **Fullur stafli**: Django er alhliða rammi fyrir fullan stafla sem getur annast þarfir bæði bakenda og framenda með samþættum eiginleikum (t.d. sniðmátsvél, stjórnunarviðmót).
- **Lipur þróun**: Vel skilgreind uppbygging og venjur Django leyfa hraða þróun og aðlögunarhæfni, sem er mikilvægt í sprotaumhverfi. Ramminn kemur með framúrskarandi skjölun og ríku vistkerfi pakka frá þriðju aðilum, sem flýtir þróun.
- **Gervigreindar-/vélnámssamþætting**: Vistkerfi Python á engan sinn líka þegar kemur að gagnavísindum og vélnámi. Django, sem er byggt á Python, samþættist snurðulaust við tól eins og Jupyter notebooks, Pandas, NumPy, TensorFlow og scikit-learn.
- **Samfélag og vistkerfi**: Django á umfangsmikið samfélag, öfluga skjölun og fjölbreytt úrval viðbóta og framlenginga, sem flýtir verulega þróun og bilanaleit.
  
**Veikleikar**:  
- **Keyrsluhraði**: Python er yfirleitt hægara en mál eins og Rust eða Elixir. Hins vegar, í þessu notkunartilviki þar sem afköst eru ekki aðalatriði, þarf þetta ekki að vera úrslitaatriði.
- **Stigstærð**: Þótt Django sé mjög stigstætt geta komið upp áskoranir í mjög stórum stíl án vandaðrar fínstillingar (t.d. við meðhöndlun mikils fjölda samhliða beiðna). Django er þó áfram hægt að stækka á skilvirkan hátt með álagsdreifingu og skyndiminnistækni.

**Úrskurður**:  
Django samræmist vel kröfum um lipra þróun, stuðning við fullan stafla og samhæfni við gervigreind/vélnám. Python-samþætting þess veitir snurðulausan aðgang að gagnavísindatólum og söfnum sem forritið þarfnast.

---

### 2. **Ruby on Rails (Ruby)**

**Yfirlit**:  
Ruby on Rails (RoR) er þroskaður veframmi fyrir fullan stafla, þekktur fyrir nálgun þar sem venjur ganga fyrir uppsetningu, sem auðveldar hraða þróun.

**Styrkleikar**:  
- **Fullur stafli**: RoR kemur með innbyggðum verkfærum fyrir þróun bæði bakenda og framenda (t.d. sýnir, sniðmát, vinnupalla), og ríkt safn gems gerir kleift að útfæra ýmsa eiginleika fljótt.
- **Lipur þróun**: Ruby on Rails er sérstaklega þekkt fyrir hraðar endurtekningarlotur, sem er kostur fyrir sprotafyrirtæki sem vilja þróa eiginleika hratt í áföngum. RoR styður prófunardrifna þróun (TDD) og hefur rótgróið vistkerfi fyrir lipur vinnuflæði.
- **Samfélag og vistkerfi**: RoR á rótgróið, sterkt samfélag og fjölbreytt úrval gems sem geta flýtt þróun.
- **Auðveld notkun**: Rails hefur mjög þróunaraðilavæna setningafræði og er þekkt fyrir að gera verk eins og gagnagrunnsflutninga, Model-View-Controller (MVC) arkitektúr og leiðarval fljótleg og einföld.

**Veikleikar**:  
- **Afköst**: Ruby hefur yfirleitt hægari keyrsluafköst en Python eða Elixir. Þótt RoR geti stækkað með réttum innviðum gætu afköst Ruby orðið flöskuháls fyrir forrit sem krefjast mikillar rauntímavinnslu eða mikillar samhliða umferðar.
- **Gervigreindar-/vélnámssamþætting**: Þótt Ruby hafi einhver vélnámssöfn er það ekki jafn víða tekið upp í gervigreindar-/vélnámssamfélaginu og Python. Samþætting við tól eins og Jupyter notebooks er ekki jafn snurðulaus, sem gerir Python sterkari kost fyrir gagnaþung forrit.
  
**Úrskurður**:  
Þótt Ruby on Rails skari fram úr í liprri þróun og hraðri frumgerðasmíði stendur það Python (Django) að baki hvað varðar samhæfni við gervigreind/vélnám. Það er raunhæfur kostur fyrir sprotafyrirtæki sem setja hraða þróun í áföngum í forgang umfram djúpa samþættingu gagnagreiningar.

---

### 3. **Phoenix (Elixir)**

**Yfirlit**:  
Phoenix er veframmi smíðaður með Elixir, fallaforritunarmáli hönnuðu fyrir stigstærð og samhliðun. Phoenix nýtir Erlang VM, sem er þekkt fyrir að meðhöndla gríðarlega samhliðun og bilanaþolin kerfi.

**Styrkleikar**:  
- **Stigstærð og afköst**: Phoenix skarar fram úr í stigstærð og meðhöndlun mikillar samhliðunar. Það er byggt á Erlang VM, sem getur stutt þúsundir (eða jafnvel milljónir) samhliða tenginga, sem gerir það að sterkum kandídat fyrir forrit sem krefjast rauntímagagnavinnslu eða mikillar umferðar.
- **Fullur stafli**: Phoenix inniheldur allt sem þarf til að smíða bæði bakenda og framenda forrits. Það styður lifandi sýnir (live views) fyrir gagnvirkar uppfærslur á viðmóti og inniheldur sniðmátsvél.
- **Lipur þróun**: Phoenix er mjög einingaskipt, sem leyfir hraða þróun eiginleika í áföngum. Það hentar vel sprotafyrirtækjum sem þurfa að hreyfa sig hratt.
- **Samhæfni við gervigreind/vélnám**: Þótt Elixir hafi vaxandi vélnámssöfn er það ekki jafn víða stutt fyrir gervigreindar-/vélnámsverkefni og Python. Samþætting við tól eins og Jupyter notebooks myndi krefjast krókaleiða, þar sem vistkerfi Elixir fyrir gagnavísindi er ekki jafn þroskað og Python.

**Veikleikar**:  
- **Gervigreindar-/vélnámsvistkerfi**: Elixir er ekki aðalmálið sem notað er í gagnavísindum eða vélnámi og vistkerfið er ekki jafn þroskað og Python. Því verður samþætting við tól eins og Jupyter notebooks eða vinsæl gervigreindarsöfn (TensorFlow, PyTorch) óþjál.
- **Námsferill**: Ef teymið þekkir ekki fallaforritun og Elixir gæti námsferillinn verið brattari.

**Úrskurður**:  
Phoenix er framúrskarandi kostur ef stigstærð og samhliðun eru aðaláhyggjuefni. Hins vegar, miðað við forgang samhæfni við gervigreind/vélnám, er Phoenix hugsanlega ekki besta passunin vegna takmarkaðs vistkerfis Elixir á þessu sviði.

---

### 4. **Loco (Rust)**

**Yfirlit**:  
Loco er veframmi smíðaður með Rust, kerfisforritunarmáli sem er þekkt fyrir afköst, minnisöryggi og samhliðun. Rust nýtur vaxandi vinsælda við smíði afkastamikilla forrita.

**Styrkleikar**:  
- **Afköst**: Helsti styrkur Rust liggur í miklum afköstum og minnisöryggi, sem gerir það að framúrskarandi kosti fyrir forrit sem krefjast lágstigsstjórnar eða afar mikilla afkasta.
- **Samhliðun**: Eignarhaldskerfi Rust tryggir minnisöryggi og leyfir um leið örugga samhliða forritun, sem gerir það tilvalið fyrir kerfi sem þurfa að stækka á skilvirkan hátt og meðhöndla samhliðun.

**Veikleikar**:  
- **Þróun fulls stafla**: Loco, þótt efnilegt sé, er ekki jafn þroskað og hinir rammarnir hvað varðar að veita fullkomna lausn fyrir fullan stafla. Það hentar betur til þróunar á bakenda og vistkerfi framenda í kringum Rust er enn að koma fram.
- **Lipur þróun**: Þróun með Rust getur verið hægari samanborið við háþróaðri mál eins og Python eða Ruby vegna lægra stigs eðlis þess og brattari námsferils.
- **Gervigreindar-/vélnámsvistkerfi**: Rust hefur ekki sama umfangsmikla vistkerfið fyrir gervigreind/vélnám og Python. Þótt vaxandi söfn séu til í Rust fyrir tölulega útreikninga eru þau langt frá því að vera jafn þroskuð og framboð Python, svo sem Jupyter notebooks eða vélnámsrammar.
  
**Úrskurður**:  
Þótt Rust og rammi þess Loco bjóði upp á framúrskarandi afköst gera skortur á stuðningi við fullan stafla, ávinningi lipurrar þróunar og vistkerfi fyrir gervigreind/vélnám það síður tilvalið fyrir þetta tiltekna notkunartilvik. Það hentar betur fyrir afkastakritísk forrit en hraða vefþróun með samþættum gagnavísindatólum.

---

### Niðurstaða

Eftir að hafa metið valkostina út frá kröfum verkefnisins er **Django (Python)** hentugasti kosturinn. Það býður upp á eftirfarandi kosti:

- **Geta fulls stafla**: Django er rammi fyrir fullan stafla sem samþættir þróun bæði bakenda og framenda.
- **Lipur þróun**: Ramminn hentar vel fyrir hraða frumgerðasmíði og þróun í áföngum, sem er nauðsynlegt í sprotaumhverfi.
- **Samhæfni við gervigreind/vélnám**: Python er leiðandi málið í gervigreind/vélnámi og samhæfni Django við söfn eins og Jupyter notebooks tryggir snurðulausa samþættingu fyrir gagnagreiningu og -vinnslu.
- **Samfélag og vistkerfi**: Sterkur stuðningur samfélags Django og umfangsmikið vistkerfi safna veita fjölmörg verkfæri til að flýta þróun.

Þótt **Ruby on Rails** sé einnig sterkur keppinautur fyrir lipra þróun gerir takmarkaður stuðningur þess við gervigreind/vélnám það síður tilvalið fyrir þetta tiltekna notkunartilvik. **Phoenix (Elixir)** og **Loco (Rust)**, þótt framúrskarandi séu fyrir stigstærð og afköst, falla á prófinu hvað varðar samþættingu við gervigreind/vélnám og þróun fulls stafla. Þess vegna er Django ráðlagður rammi fyrir þetta verkefni.
