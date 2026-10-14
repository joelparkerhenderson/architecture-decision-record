# Ferli AWS fyrir arkitektúrákvörðunarskrár

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Arkitektúrákvörðunarskrá (ADR) er skjal sem lýsir vali sem teymið tekur varðandi mikilvægan þátt í hugbúnaðararkitektúrnum sem það ætlar að smíða. Hver ADR lýsir arkitektúrákvörðuninni, samhengi hennar og afleiðingum. ADR-skrár hafa stöður og fylgja því lífsferli. Dæmi um ADR er að finna í viðaukanum.

ADR-ferlið skilar safni arkitektúrákvörðunarskráa. Þetta safn myndar ákvörðunarannálinn. Ákvörðunarannállinn veitir samhengi verkefnisins ásamt ítarlegum upplýsingum um útfærslu og hönnun. Verkefnisfólk rennir yfir fyrirsagnir hverrar ADR til að fá yfirsýn yfir samhengi verkefnisins. Það les ADR-skrárnar til að kafa djúpt í útfærslur og hönnunarval verkefnisins.

Þegar teymið samþykkir ADR verður hún óbreytanleg. Ef nýjar innsýnir kalla á aðra ákvörðun, leggur teymið til nýja ADR. Þegar teymið samþykkir nýju ADR kemur hún í stað fyrri ADR.

## Umfang ADR-ferlisins

Verkefnisfólk ætti að búa til ADR fyrir sérhverja arkitektúrlega mikilvæga ákvörðun sem hefur áhrif á hugbúnaðarverkefnið eða vöruna, þar á meðal eftirfarandi (Richards og Ford 2020):

* Uppbygging (til dæmis mynstur eins og örþjónustur)

* Óvirkar kröfur (öryggi, mikið aðgengi og bilanaþol)

* Ávirkni (tengsl milli íhluta)

* Viðmót (API og útgefnir samningar)

* Smíðatækni (söfn, rammar, verkfæri og ferli)

* Virkar og óvirkar kröfur eru algengustu inntök ADR-ferlisins.


## Innihald ADR

Þegar teymið greinir þörf fyrir ADR byrjar einn úr teyminu að skrifa hana út frá sniðmáti sem gildir fyrir allt verkefnið. (Sjá ADR-stofnunina á GitHub fyrir dæmi um sniðmát.) Sniðmátið einfaldar gerð ADR og tryggir að hún fangi allar viðeigandi upplýsingar. Að lágmarki ætti hver ADR að skilgreina samhengi ákvörðunarinnar, ákvörðunina sjálfa og afleiðingar hennar fyrir verkefnið og afurðir þess. (Dæmi um þessa kafla er að finna í viðaukanum.) Einn öflugasti eiginleiki ADR-uppbyggingarinnar er að hún beinist að ástæðu ákvörðunarinnar en ekki að því hvernig teymið útfærði hana. Að skilja hvers vegna teymið tók ákvörðunina auðveldar öðru teymisfólki að tileinka sér hana og kemur í veg fyrir að aðrir arkitektar, sem tóku ekki þátt í ákvarðanatökunni, hnekki henni síðar.


## Ferli við innleiðingu ADR

Hver og einn í teyminu getur búið til ADR, en teymið ætti að koma sér upp skilgreiningu á eignarhaldi á ADR. Hver höfundur sem á ADR ætti að viðhalda og miðla innihaldi hennar af virkni. Til að skýra þetta eignarhald vísar þessi leiðarvísir til ADR-höfunda sem ADR-eigenda í köflunum hér á eftir. Annað teymisfólk getur alltaf lagt til efni í ADR. Ef innihald ADR breytist áður en teymið samþykkir hana, ætti eigandinn að samþykkja þessar breytingar.

Eftir að teymið hefur greint arkitektúrákvörðun og eiganda hennar leggur ADR-eigandinn fram ADR í stöðunni **Proposed** (Lögð fram) í upphafi ferlisins. ADR-skrár í stöðunni Lögð fram eru tilbúnar til rýni.

ADR-eigandinn hefur síðan rýniferli ADR. Markmið rýniferlisins er að ákveða hvort teymið samþykkir ADR, kemst að þeirri niðurstöðu að hún þarfnist endurvinnslu eða hafnar henni. Verkefnateymið, þar með talinn eigandinn, rýnir ADR. Rýnifundurinn ætti að hefjast á sérstöku tímabili til að lesa ADR. Að meðaltali ættu 10 til 15 mínútur að nægja. Á þessum tíma les hver og einn í teyminu skjalið og bætir við athugasemdum og spurningum til að merkja óljós atriði. Eftir rýnifasann les ADR-eigandinn upp og ræðir hverja athugasemd við teymið.

Ef teymið finnur aðgerðaatriði til að bæta ADR, helst staða hennar **Proposed** (Lögð fram). ADR-eigandinn mótar aðgerðirnar og, í samvinnu við teymið, bætir ábyrgðaraðila við hverja aðgerð. Hver og einn í teyminu getur lagt sitt af mörkum og leyst aðgerðaatriðin. Það er á ábyrgð ADR-eigandans að endurskipuleggja rýniferlið.

Teymið getur einnig ákveðið að hafna ADR. Í því tilviki bætir ADR-eigandinn við ástæðu synjunarinnar til að koma í veg fyrir frekari umræður um sama efni. Eigandinn breytir stöðu ADR í **Rejected** (Hafnað).

Ef teymið samþykkir ADR bætir eigandinn við tímastimpli, útgáfu og lista yfir hagsmunaaðila. Eigandinn uppfærir síðan stöðuna í **Accepted** (Samþykkt).

ADR-skrár og ákvörðunarannállinn sem þær mynda endurspegla ákvarðanir teymisins og veita sögu allra ákvarðana. Teymið notar ADR-skrárnar sem viðmiðun við kóða- og arkitektúrrýni þar sem það er hægt. Auk þess að framkvæma kóðarýni, hönnunarverkefni og útfærsluverkefni ætti teymisfólk að leita til ADR-skráa varðandi stefnumótandi ákvarðanir um vöruna.

Sem góð venja ætti hver hugbúnaðarbreyting að fara í gegnum jafningjarýni og krefjast að minnsta kosti eins samþykkis. Við kóðarýni gæti rýnandi fundið breytingar sem brjóta í bága við eina eða fleiri ADR. Í því tilviki biður rýnandinn höfund kóðabreytingarinnar um að uppfæra kóðann og deilir tengli á ADR. Þegar höfundurinn uppfærir kóðann er hann samþykktur af jafningjarýnendum og sameinaður aðalkóðagrunninum.


## Rýniferli ADR

Teymið ætti að líta á ADR-skrár sem óbreytanleg skjöl eftir að teymið samþykkir eða hafnar þeim. Breytingar á núverandi ADR krefjast þess að ný ADR sé búin til, rýniferli sett upp fyrir nýju ADR og hún samþykkt. Ef teymið samþykkir nýju ADR ætti eigandinn að breyta stöðu gömlu ADR í **Superseded** (Leyst af hólmi).
