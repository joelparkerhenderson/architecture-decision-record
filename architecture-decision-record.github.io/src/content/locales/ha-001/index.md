# Rikodin shawarar gine-gine (ADR)

Rikodin shawarar gine-gine (ADR) takarda ce da ke rubuta wata muhimmiyar shawarar gine-gine da aka yanke tare da mahallinta da sakamakonta.

> [!IMPORTANT]
> Ku yi isasshen bincikenku kafin amfani da waɗannan albarkatu a kowane tsari mai muhimmanci.

Abubuwan da ke ciki:

- [Menene rikodin shawarar gine-gine?](#menene-rikodin-shawarar-gine-gine)
- [Yadda ake fara amfani da ADR](#yadda-ake-fara-amfani-da-adr)
- [Yadda ake fara amfani da ADR da kayan aiki](#yadda-ake-fara-amfani-da-adr-da-kayan-aiki)
- [Yadda ake fara amfani da ADR da git](#yadda-ake-fara-amfani-da-adr-da-git)
- [Ƙwarewar Claude Code don ADR](#ƙwarewar-claude-code-don-adr)
- [Ka’idojin sunan fayil na ADR](#kaidojin-sunan-fayil-na-adr)
- [Shawarwari kan rubuta ADR masu kyau](#shawarwari-kan-rubuta-adr-masu-kyau)
- [Samfuran misali na ADR](#samfuran-misali-na-adr)
- [Shawarwarin aiki tare na ADR](#shawarwarin-aiki-tare-na-adr)
- [Tambayoyin aiki tare na ADR](#tambayoyin-aiki-tare-na-adr)
- [Ra’ayoyin mataki na gaba don ADR](#raayoyin-mataki-na-gaba-don-adr)
- [Zane-zanen gine-gine, ra’ayoyi, da mahangogi](#zane-zanen-gine-gine-raayoyi-da-mahangogi)
- [Ayyukan lafiya na shawarwari a matsayin lamba](#ayyukan-lafiya-na-shawarwari-a-matsayin-lamba)
- [Shingen shawara don pull requests](#shingen-shawara-don-pull-requests)
- [Don ƙarin bayani](#don-ƙarin-bayani)

Samfura:

- [Samfurin rikodin shawara na Jeff Tyree da Art Akerman](samfura/samfurin-rikodin-shawara-na-jeff-tyree-da-art-akerman/)
- [Samfurin rikodin shawara na Michael Nygard](samfura/samfurin-rikodin-shawara-na-michael-nygard/)
- [Samfurin rikodin shawara na EdgeX](samfura/samfurin-rikodin-shawara-na-edgex/)
- [Samfurin rikodin shawara na arc42](samfura/samfurin-rikodin-shawara-na-arc42/)
- [Samfurin rikodin shawara don tsarin Alexandrian](samfura/samfurin-rikodin-shawara-don-tsarin-alexandrian/)
- [Samfurin rikodin shawara don lamarin kasuwanci](samfura/samfurin-rikodin-shawara-don-lamarin-kasuwanci/)
- [Samfurin rikodin shawara na aikin MADR](samfura/samfurin-rikodin-shawara-na-aikin-madr/)
- [Samfurin rikodin shawara mai amfani da Planguage](samfura/samfurin-rikodin-shawara-mai-amfani-da-planguage/)
- [Samfurin rikodin shawara na Paulo Merson](https://github.com/pmerson/ADR-template)
- [Samfurin rikodin shawara na Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Samfurin rikodin shawara na Gareth Morgan](samfura/samfurin-rikodin-shawara-na-gareth-morgan/)
- [Samfurin rikodin shawara na GIG Cymru NHS Wales](samfura/samfurin-rikodin-shawara-na-gig-cymru-nhs-wales/)
- [Samfurin rikodin shawara don muhimman shawarwarin fasaha (ITD) na Ignacio Larrañaga](samfura/samfurin-rikodin-shawara-don-muhimman-shawarwarin-fasaha/)

Misalai:

- [Tsarin CSS](misalai/tsarin-css/)
- [Saitin sauye-sauyen muhalli](misalai/saitin-sauye-sauyen-muhalli/)
- [Ma’auni, masu sa ido, fadakarwa](misalai/ma-auni-masu-sa-ido-da-fadakarwa/)
- [Microsoft Azure DevOps](misalai/microsoft-azure-devops/)
- [Monorepo ko multirepo](misalai/monorepo-ko-multirepo/)
- [Harsunan shirye-shirye](misalai/harsunan-shirye-shirye/)
- [Ajiyar sirri](misalai/ajiyar-sirri/)
- [Tsarin tambarin lokaci](misalai/tsarin-tambarin-lokaci/)
- [da ƙari da yawa...](misalai/)

## Menene rikodin shawarar gine-gine?

**Rikodin shawarar gine-gine** (ADR) takarda ce da ke rubuta wata muhimmiyar shawarar gine-gine da aka yanke tare da mahallinta da sakamakonta.

**Shawarar gine-gine** (AD) zaɓi ne na tsarin manhaja wanda ke magance wata muhimmiyar buƙata.

**Rajistar shawarwarin gine-gine** (ADL) tarin dukkan ADR ne da aka ƙirƙira kuma ake kula da su don wani aiki (ko ƙungiya) na musamman.

**Buƙata mai muhimmanci ta fuskar gine-gine** (ASR) buƙata ce da ke da tasiri mai aunuwa a kan tsarin gine-ginen tsarin manhaja.

Dukan waɗannan suna ƙarƙashin batun **gudanar da ilimin gine-gine** (AKM).

Manufar wannan takarda ita ce ta ba da taƙaitaccen bayani game da ADR, yadda ake ƙirƙirar su, da kuma inda za a nemi ƙarin bayani.

Gajarta:

  * **AD**: shawarar gine-gine

  * **ADL**: rajistar shawarwarin gine-gine

  * **ADR**: rikodin shawarar gine-gine

  * **AKM**: gudanar da ilimin gine-gine

  * **ASR**: buƙata mai muhimmanci ta fuskar gine-gine

## Yadda ake fara amfani da ADR

Don fara amfani da ADR, ku tattauna waɗannan fannoni da abokan tawagarku.

Gano shawara:

  * Yaya AD yake da gaggawa kuma yaya yake da muhimmanci?

  * Shin dole ne a yanke shi yanzu, ko kuwa zai iya jira har sai an san ƙarin bayani?

  * Ƙwarewar mutum da ta gamayya, da kuma hanyoyin ƙira da ayyukan da aka sani, na iya taimakawa wajen gano shawara.

  * A manufa, a riƙa kula da jerin shawarwarin da ake buƙata wanda ya cika jerin ayyukan samfurin.

Yanke shawara:

  * Akwai dabaru da yawa na yanke shawara, na gama gari da kuma na musamman ga gine-ginen manhaja, misali taswirar tattaunawa.

  * Yanke shawara a rukuni batu ne na bincike mai ci gaba.

Aiwatar da shawara da tabbatar da bin ta:

  * Ana amfani da AD a ƙirar manhaja; saboda haka dole ne a sanar da masu ruwa da tsaki na tsarin, waɗanda ke ba da kuɗi, ke gina shi, kuma ke tafiyar da shi, kuma su amince da shi.

  * Salon rubuta lamba mai bayyana a gine-gine da bita-bitar lamba da ke mai da hankali kan damuwa da shawarwarin gine-gine ayyuka biyu ne masu alaƙa.

  * Dole ne kuma a (sake) yin la’akari da AD lokacin sabunta tsarin manhaja a cikin juyin manhaja.

Raba shawara (na zaɓi):

  * AD da yawa suna maimaita kansu a cikin ayyuka.

  * Saboda haka, abubuwan da aka koya daga shawarwarin da suka gabata, masu kyau da marasa kyau, na iya zama kadarori masu amfani da za a sake amfani da su lokacin da ake bin dabarar gudanar da ilimi a fili.

Rubuta shawara:

  * Akwai samfura da kayan aiki da yawa na rubuta shawara.

  * Duba al’ummomin masu sassauci, misali ADR na M. Nygard.

  * Duba hanyoyin injiniyan manhaja da ƙirar gine-gine na gargajiya, misali tsarin tebur da IBM UMF da Tyree da Akerman na CapitalOne suka ba da shawara.

Don ƙarin bayani:

  * An ɗauko matakan da ke sama daga shigarwar Wikipedia kan [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Yadda ake fara amfani da ADR da kayan aiki

- [MySpec](https://myspec.dev) — dandamalin ƙayyadaddun bayanai da shawarwarin gine-gine na atomatik wanda ke tsara kundin tsarin aiki, gine-ginen fasaha, da ADR a cikin Markdown mai tsabta da ake samarwa ta MCP.

Kuna iya fara amfani da ADR da kayan aiki yadda kuke so.

Misali:

  * Idan kuna son amfani da Google Drive da gyara ta yanar gizo, za ku iya ƙirƙirar Google Doc, ko Google Sheet.

  * Idan kuna son amfani da sarrafa nau’ikan lamba kamar git, za ku iya ƙirƙirar fayil ga kowane ADR.

  * Idan kuna son amfani da kayan tsara ayyuka kamar Atlassian Jira, za ku iya amfani da na’urar bin diddigin tsarin kayan aikin.

  * Idan kuna son amfani da wikis kamar MediaWiki, za ku iya ƙirƙirar wiki na ADR.

## Yadda ake fara amfani da ADR da git

Idan kuna son amfani da sarrafa nau’ikan git, ga yadda muke so mu fara amfani da ADR da git don aikin manhaja na yau da kullum mai lambar tushe.

Ƙirƙiri kundin adireshi don fayilolin ADR:

```sh
$ mkdir adr
```

Ga kowane ADR, ƙirƙiri fayil ɗin rubutu, misali `choose-database.md`:

```sh
$ vi choose-database.md
```

Rubuta duk abin da kuke so a cikin ADR. Duba samfuran da ke wannan ma’ajiyar don samun ra’ayoyi.

Yi commit na ADR zuwa ma’ajiyar git ɗinku.

## Ƙwarewar Claude Code don ADR

Wannan ma’ajiya tana ba da ƙwarewar [Claude Code](https://claude.com/claude-code) guda biyu a ƙarƙashin [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), don wakilin rubuta lamba na AI ya iya rubuta da kula da ADR yadda wannan aikin ke ba da shawara:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — don amfani gabaɗaya, ga duk wanda ke rubuta ADR a kowane aiki. Yana taimakawa wajen yanke ko shawara tana buƙatar ADR, yana kafa kundin `adr/` ko `decisions/`, yana sanya sunan fayil, yana zaɓar samfuri daga cikin tsare-tsare goma sha ɗaya da aka haɗa, kuma yana rubuta sassan Mahalli/Shawara/Sakamako da ƙarfi.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — musamman ga masu kula da wannan ma’ajiya. Yana rubuta tsarin ma’ajiyar, ƙa’idar madubin README/locales, da takamaiman matakan ƙara sabon samfuri, misali, ko hanyar haɗin kayan aiki.

Don amfani da ƙwarewa, kwafi kundinta zuwa `.claude/skills/` a tushen ma’ajiyar da kuke aiki a ciki (ko zuwa `~/.claude/skills/` don samun ta a kowane aiki), sannan ku nemi Claude Code ya rubuta ko ya bita ADR.

## Ka’idojin sunan fayil na ADR

Idan kun zaɓi ƙirƙirar ADR ɗinku a cikin fayilolin rubutu na yau da kullum, kuna iya son ƙirƙirar ƙa’idar sunan fayil ɗin ADR ɗinku.

Muna fifita amfani da ƙa’idar sunan fayil mai tsari na musamman.

Misalai:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Ƙa’idar sunan fayil ɗinmu:

  * Sunan yana da jimlar aikatau ta umarni a halin yanzu. Wannan yana taimakawa wajen karantawa kuma yana dacewa da tsarin saƙonnin commit ɗinmu.

  * Sunan yana amfani da ƙananan haruffa da dashes (kamar wannan ma’ajiyar). Wannan daidaito ne tsakanin sauƙin karantawa da amfanin tsarin.

  * Tsawo markdown ne. Wannan na iya zama da amfani don sauƙin tsarawa.

## Shawarwari kan rubuta ADR masu kyau

Siffofin ADR mai kyau:

* Dalili: Bayyana dalilan yin AD na musamman. Wannan na iya haɗawa da mahalli (duba ƙasa), fa’idodi da rashin fa’idodi na zaɓuɓɓuka daban-daban masu yiwuwa, kwatancen siffofi, tattaunawar kuɗi/riba, da ƙari.

* Na musamman: Kowane ADR ya kamata ya zama game da AD ɗaya, ba AD da yawa ba.

* Tambarin lokaci: Gano lokacin da aka rubuta kowane abu a cikin ADR. Wannan yana da muhimmanci musamman ga abubuwan da za su iya canzawa da lokaci, kamar kuɗi, jadawali, faɗaɗawa, da makamantansu.

* Maras canzawa: Kada ku canza bayanan da ke cikin ADR. Maimakon haka, ku gyara ADR ta ƙara sabon bayani, ko ku maye gurbin ADR ta ƙirƙirar sabon ADR.

Siffofin kyakkyawan sashen “Mahalli” a cikin ADR:

* Bayyana yanayin ƙungiyar ku da fifikon kasuwancinta.

* Haɗa dalilai da la’akari bisa tsarin zamantakewa da ƙwarewar tawagarku.

* Haɗa fa’idodi da rashin fa’idodi masu alaƙa, kuma ku siffanta su da kalmomin da suka dace da buƙatunku da manufofinku.

Siffofin kyakkyawan sashen “Sakamako” a cikin ADR:

* Bayyana abin da ke biyo bayan yanke shawara. Wannan na iya haɗawa da tasiri, sakamako, abubuwan da aka samar, bin diddigi, da ƙari.

* Haɗa bayani game da duk wasu ADR da suka biyo baya. Yana da kusan al’ada ADR ɗaya ya jawo buƙatar ƙarin ADR, kamar lokacin da ADR ɗaya ya yi babban zaɓi wanda kuma ya haifar da buƙatar ƙarin ƙananan shawarwari.

* Haɗa duk wasu hanyoyin bitar bayan aiki. Yana da al’ada tawaga ta yi bitar kowane ADR bayan wata ɗaya, don kwatanta bayanan ADR da abin da ya faru a zahiri, domin koyo da ci gaba.

Sabon ADR na iya maye gurbin ADR na baya:

* Lokacin da aka yanke AD wanda ya maye gurbin ko ya ɓata ADR na baya, ya kamata a ƙirƙiri sabon ADR

## Samfuran misali na ADR

Samfuran misali na ADR da muka tattara daga intanet:

- [Samfurin ADR na Michael Nygard](samfura/samfurin-rikodin-shawara-na-michael-nygard/) (mai sauƙi kuma sananne)

- [Samfurin ADR na Jeff Tyree da Art Akerman](samfura/samfurin-rikodin-shawara-na-jeff-tyree-da-art-akerman/) (ya fi ƙwarewa)

- [Samfurin ADR don tsarin Alexandrian](samfura/samfurin-rikodin-shawara-don-tsarin-alexandrian/) (mai sauƙi tare da cikakkun bayanan mahalli)

- [Samfurin ADR don lamarin kasuwanci](samfura/samfurin-rikodin-shawara-don-lamarin-kasuwanci/) (ya fi karkata zuwa MBA, tare da kuɗi, SWOT, da ƙarin ra’ayoyi)

- [Samfurin ADR na aikin Markdown Any Decision Records (MADR)](samfura/samfurin-rikodin-shawara-na-aikin-madr/) (sigar mai sauƙi da ta cikakke; ta ƙarshe tana jaddada zaɓuɓɓuka da fa’idodinsu da rashin fa’idodinsu)

- [Samfurin ADR mai amfani da Planguage](samfura/samfurin-rikodin-shawara-mai-amfani-da-planguage/) (ya fi karkata zuwa tabbatar da inganci)

- [Samfuri don muhimman shawarwarin fasaha (ITD) na Ignacio Larrañaga](samfura/samfurin-rikodin-shawara-don-muhimman-shawarwarin-fasaha/) (ƙaranci kuma mai fara da shawara, an inganta shi don saurin bitar zartarwa)

## Shawarwarin aiki tare na ADR

Idan kuna tunanin amfani da rikodin shawarwari tare da tawagarku, ga wasu shawarwari da muka koya ta yin aiki da tawagogi da yawa.

Kuna da damar jagorantar abokan tawagarku, ta hanyar tattaunawa tare game da “dalili”, maimakon tilasta “abin da”. Misali, rikodin shawarwari hanya ce ta tawagogi don yin tunani cikin hikima da sadarwa mafi kyau; rikodin shawarwari ba shi da amfani idan kawai buƙatar takardu ce ta tilas bayan abin ya riga ya faru.

Wasu tawagogi sun fi son suna “shawarwari” fiye da gajartar “ADR”. Lokacin da wasu tawagogi ke amfani da sunan kundin adireshi “decisions”, kamar fitila ta kunna ce, kuma tawagar ta fara saka ƙarin bayani a cikin kundin, kamar shawarwarin masu sayarwa, shawarwarin tsarawa, shawarwarin jadawali, da sauransu. Duk waɗannan nau’ikan bayani na iya amfani da samfuri ɗaya. Muna hasashen cewa mutane suna koyo da sauri da kalmomi (“shawarwari”) fiye da gajarta (“ADR”), kuma mutane suna da ƙwazo wajen rubuta takardun aiki mai gudana idan an cire kalmar “rikodi”, kuma wasu masu haɓakawa da wasu manajoji ba sa son kalmar “gine-gine”.

A ka’ida, rashin canzawa ya fi dacewa. A aikace, canzawa ya fi yin aiki ga tawagoginmu. Muna saka sabon bayani cikin ADR da ke akwai, tare da tambarin kwanan wata, da bayanin cewa bayanin ya zo bayan shawarar. Wannan hanya tana kaiwa ga “takarda mai rai” da dukanmu za mu iya sabuntawa. Sabuntawa na yau da kullum na faruwa lokacin da muka sami bayani saboda sababbin abokan tawaga, sababbin tayi, sakamakon amfaninmu na zahiri, ko sauye-sauyen wasu bayan shawarar kamar iyawar masu sayarwa, tsare-tsaren farashi, yarjejeniyoyin lasisi, da sauransu.

## Tambayoyin aiki tare na ADR

### Wa zai iya ƙirƙirar ADR?

Yi la’akari da fannoni kamar mutane na musamman, ko matsayi na musamman, ko tawagogi na musamman, ko sassa na musamman; kuma ku yi la’akari ko akwai mutane, ko matsayi, ko tawagogi, ko sassa da za su iya ba da umarnin ADR, wato su nemi ADR da wani na daban zai rubuta.

Misalin amsa: Duk wani mutum a ƙungiyarmu wanda ya karanta shafin README na rikodin shawarar gine-gine zai iya ba da shawarar ADR, wato mutumin zai iya fara rubuta shi, ya raba shi da tawaga.

### Me ke tabbatar da buƙatar ɗaga ADR?

Yi la’akari da fannoni kamar hanyoyin aikin tawagogin ƙungiyarku, tsarin tsarin manhajarku, daidaita aiki tsakanin tawagogi, dorewar kulawa na dogon lokaci, hanyoyin sadarwa na waje, wanda kuke so ya amfana, da makamantansu.

Misalin amsa: Muna son ƙirƙirar ADR lokacin da muke son masu haɓakawa na nan gaba su fahimci “dalilin” abin da muke yi.

### Me ke tabbatar da rashin ɗaga ADR?

Yi la’akari da fannoni kamar shawarwarin da ba su shafi gine-gine ba, ko ƙanana kamar masu ƙarancin haɗari ko masu cikakken kansu ko na mai haɓakawa ɗaya, ko waɗanda aka riga aka rufe su sosai a wani wuri kamar ƙa’idoji ko manufofi ko takardu, ko na ɗan lokaci kamar mafita na ɗan lokaci ko shaidar ra’ayi ko gwaje-gwaje.

Misalin amsa: Muna son tsallake ADR lokacin da shawara ta iyakance a fanni da lokaci da haɗari da kuɗi, ko kuma an riga an rufe ta a wani wuri.

### Menene zagayen rayuwar ADR?

Yi la’akari da fannoni kamar tsarin ƙirƙira, tsarin bincike, tsarin yanke shawara, tsarin aiwatarwa, da tsarin ƙarewa. Yi la’akari da yadda za a bi diddigin zagayen rayuwar ADR a kan lokaci, misali yadda za a motsa ADR daga wani yanayi zuwa na gaba, da kuma yadda za a sanar da masu ruwa da tsaki wannan.

Misalin amsa: Muna son ADR ya kasance yana da matakai biyar na zagayen rayuwa: Farawa → Bincike → Kimantawa → Aiwatarwa → Kulawa → Ƙarewa.

### Menene ma’aunin matakan zagayen rayuwar ADR?

Yi la’akari da fannoni kamar ma’aunin karɓa na ADR, wato ta yaya za ku san ya isa ya ci gaba daga mataki ɗaya na zagayen rayuwa zuwa na gaba? An bayyana matsalar a fili? An yi la’akari da madadin? An fahimci musanyar fa’ida da rashin fa’ida kuma an rubuta su yadda ya kamata?
Dukkan mahallin da ya dace yana nan? Dukkan masu ruwa da tsaki da suka dace suna ciki? An haɗa dukkan ra’ayoyi?

Misalin amsa: Muna son masu ruwa da tsaki su kaɗa ƙuri’a kan ADR lokacin da tawagar mai aiki ta 1) kammala bincikenta, 2) kammala kimantawarta, 3) ta buga shawarar ADR ga masu ruwa da tsaki tare da buƙatar ra’ayoyi da iyakar lokaci na mako ɗaya, 4) an haɗa dukkan ra’ayoyin masu ruwa da tsaki kuma an magance su.

### Waɗanne matsayi da nauyi ne ke hulɗa da ADR?

Yi la’akari da matsayi kamar mai ba da shawara, mai bincike, mai kimantawa, mai bita, mai amincewa, mai kulawa, da makamantansu. Yi la’akari da nauyi kamar sadarwa da masu ruwa da tsaki, tabbatar da cika buri, raba a gidan yanar gizo ko intranet, da bitar aikin lokaci-lokaci musamman lokacin da canje-canje masu dacewa suka faru.

Misalin amsa: Muna son kowane ADR ya kasance yana da mutum na farko na tuntuɓa, mutum na biyu na tuntuɓa, da tawagar mai alhaki; waɗannan suna da alhakin sadarwa, wallafawa, kulawa, bita lokaci-lokaci aƙalla sau ɗaya a shekara, da ƙarshe ƙarewa idan an buƙata.

### Ta yaya mulki ke hulɗa da ADR?

Yi la’akari da fannoni kamar hanyoyin aikin ƙungiyarku, duk wasu buƙatun bin ƙa’ida na musamman kamar na shari’a ko albarkatun ɗan adam, yadda kuke son magance yarjejeniya da rikici da ɗaga batu zuwa sama. Akwai fannoni ko mutane ko tawagogi da za su iya samun tasiri fiye da sauran game da ADR, kamar samun damar amincewa da shi, ko kaɗa ƙuri’a a kansa, ko hana shi?

Misalin amsa: Mulkin ADR yana cikin wannan jerin fifiko: CEO, CTO, CLO, tawagar da ke aiwatar da ADR, ƙwararrun tawagar da suka fi sanin AD. Babu wani da ke da mulki sai dai idan an bayyana a cikin ADR.

### Waɗanne ƙa’idoji ne ke hulɗa da ADR?

Yi la’akari da fannoni kamar hanyoyin aikin ƙungiyarku waɗanda suka haɗa da tafiya da sauri da tafiya a hankali, yarjejeniyar shawara da rikicin shawara, fifikon haɗari da fifikon aminci, tattaunawar jama’a da tattaunawar sirri, da makamantansu.

Misalin amsa: Muna amfani da ƙa’idojin jagoranci na son aiki, rashin yarda-amma-a-yi, kiyasin 70% sun isa ga shawarwari masu sauƙin sakewa da sauƙin keɓewa, da hanyoyin aiki na jama’a ban da bayanan sirri kamar yadda aka bayyana a yarjejeniyar sirri ta ƙungiyarmu.

## Ra’ayoyin mataki na gaba don ADR

[Arc42](https://arc42.org/) yana amsa tambayoyi biyu ta hanya mai amfani kuma ana iya daidaita shi da takamaiman buƙatunku. Me ya kamata ku rubuta/sadar game da gine-ginenku? Yaya ya kamata ku rubuta/sadar da shi? Arc42 ya haɗa da jagora kan manufofi, ƙuntatawa, mahalli, inganci, haɗari da ƙari, ban da rikodin shawarar gine-gine.

[Samfurin C4](https://c4model.com/) hanya ce mai sauƙin koyo, mai dacewa da masu haɓakawa, ta zana zane-zanen gine-ginen manhaja. C4 tarin zane-zane ne na matsayi don mahalli, kwantena, ɓangarori, lamba, tare da zane-zane na taimako don yanayin tsari, motsi, da ɗora tsari.

## Zane-zanen gine-gine, ra’ayoyi, da mahangogi

Zanen gine-gine ana kiransa “ra’ayin gine-gine”.

“Ra’ayin gine-gine” misali ne na “mahangar gine-gine”.

“Mahangar gine-gine” tana da takamaiman masu sauraro waɗanda ke da takamaiman damuwa a zuciya.

Misalan mahangogin gine-gine, misalan ra’ayoyi, da misalan zane-zane:

- Iyawar Kasuwanci (Business Capabilities)

- Hanyoyin kasuwanci na matakin sama

- [Kwararar Daraja (Value Streams)](https://en.wikipedia.org/wiki/Value_stream)

- Ayyukan manhaja da aka yi wa taswira zuwa ɓangarorin aikace-aikace

- Zanen mahalli na [samfurin C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- Zanen kwantena na [samfurin C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- [Zanen alaƙar-ƙungiya](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) don yin taswirar ƙungiyoyin bayanai zuwa ɓangarorin aikace-aikace

- [Zane-zanen jerin (Sequence diagrams)](https://en.wikipedia.org/wiki/Sequence_diagram) don bayyana kwararar aiki a cikin tsarukan da kuma don haɗewa

- Zane-zanen [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) don bayyana kwararar bayanai a cikin ɓangarorin aikace-aikace

- Zane-zanen [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) don bayyana hanyoyin kasuwanci / yanayin masu amfani

- Zane-zanen [Gudanar da Ainihi da Samun Dama (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM)

- Zane-zanen [Ikon Samun Dama bisa Matsayi (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) tare da matsayi ga kowane ɓangaren aikace-aikace

- Zane-zanen [Ikon Samun Dama bisa Hali (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) tare da halaye ga kowane ɓangaren aikace-aikace

- Zane-zanen sirri

Zane-zane masu alaƙa:

- Zanen Yanayin Amfani (Use Case Diagram) yana nuna wa gudanarwa/abokan ciniki yanayin amfani, wanda ke zuwa kafin buƙatu, wanda ke zuwa kafin gine-ginen manhaja.

- Zanen Ɗora Tsari (Deployment Diagram) yana nuna kayan aiki/kwamfutoci na zahiri da ake ɗora ɓangarorin manhaja a kansu.
- Zanen Kwararar Bayanai (Data Flow Diagram) yana nuna yadda bayanai ke wucewa da canzawa ta tsarin.
- Zanen Jerin (Sequence Diagram) ana amfani da shi don nuna yadda ƙa’idodin sadarwa kamar HTTP ke aiki a kan axis na lokaci.

- Zanen Ayyuka (Activity Diagram) yana nuna kwararar ayyukan da tsarin manhaja ke aiwatarwa, kamar NPC AI.

## Ayyukan lafiya na shawarwari a matsayin lamba

Ayyukan lafiya (fitness functions) bincike ne na atomatik mai manufa wanda aka rubuta da lambar shirye-shirye, wanda ke tabbatar da cewa ana kiyaye shawarwari.

- Ayyukan lafiya suna sa shawarwari su zama masu gwaji da tabbatarwa.

- Ayyukan lafiya na shawarwari na iya taimakawa sosai wajen tabbatar da inganci, tsarin ƙa’idoji, da manufofin mulki.

### Yadda ayyukan lafiya ke haɗuwa da shawarwari

Rikodin shawara yana rubuta shawarar, yayin da aikin lafiya ke tabbatar da ita.

- Misalin shawara: Muna amfani da event sourcing don buƙatun bincike.

- Misalin aikin lafiya: Muna amfani da sabar haɗewa ta ci gaba don gwada cewa duk canje-canjen yanayi dole ne su samar da abubuwan da suka faru.

### Dalilin da ya sa ayyukan lafiya ke taimakon shawarwari

Ma’auni masu manufa: Ayyukan lafiya suna ci ko faɗuwa, don haka aiki yana bayyane kuma a fili.

Amfani mai ci gaba: Ayyukan lafiya ƙa’idojinku ne masu rai, waɗanda ake gudanarwa a kowane commit da build.

Kwarin gwiwa don sake tsarawa: Ayyukan lafiya suna kama kurakuran ƙa’idar shawara ta atomatik.

Mulki mai faɗaɗa: Ayyukan lafiya suna tabbatar da ƙa’idodi ba tare da ƙirƙirar cikas ba.

### Shin ayyukan lafiya za su iya amfani da AI?

Ayyukan lafiya za su iya amfani da AI LLM don shawarwari ta yin tambayoyi game da aikinku,
kamar tsare-tsarenku, lambarku, tsare-tsaren bayanai, API, da ƙari:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Gwajin raka’o’in gine-gine

[ArchUnit](https://www.archunit.org/): duba ƙa’idojin gine-gine na lambar Java ta amfani da kowane tsarin gwajin raka’a na Java na yau da kullum.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): duba ƙa’idojin gine-gine na lambar TypeScript da lambar JavaScript ta amfani da Jest, Vitest, Jasmine, da sauransu.

## Shingen shawara don pull requests

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
yana fito da rikodin shawara da ya dace ta atomatik a daidai lokacin — lokacin da
mai haɓakawa ke canza lambar da waɗannan shawarwari suka rufe. Maimakon fatan masu haɓakawa
su karanta kundin takardu kafin haɗawa, mahallin da ya dace yana bayyana kai tsaye a
pull request.

Yana aiki ga kowane nau’in rikodin shawara: shawarwarin gine-gine, shawarwarin bayanai,
shawarwarin bin ƙa’ida, shawarwarin asibiti da likitanci, shawarwarin tsaro, da ƙari.

Yana aiki da kowane tsarin CI (GitLab, Jenkins, CircleCI) da kuma a matsayin pre-commit hook.
Buɗaɗɗen tushe. Lasisin MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) GitHub
Action ne wanda ke sa pull request ya gaza lokacin da hanyar lamba da ake sa ido a kanta ta canza
kuma ba a ƙara ko sabunta rikodin shawarar gine-gine ba. Keɓancewa a bayyane suke: layin
`ADR-Exempt:` tare da dalili yana barin shinge ya wuce kuma ana rubuta shi a taƙaitaccen aikin.
Ba ya dogara da samfuri, babu dogaro. Buɗaɗɗen tushe. Lasisin MIT.

## Don ƙarin bayani

Gabatarwa:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Samfura:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Cikin zurfi:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - darasin gine-ginen manhaja na wata-wata kyauta

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Kayan aiki:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Jagora na musamman ga kamfani:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Misalai:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Bidiyo:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcast:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Littattafai:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

Duba kuma:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Tsarin YAML/JSON mara sha’awar mai sayarwa, wanda injin zai iya karantawa, don wakiltar shawarwari tare da bayyananne dalili, zato, yanayin fahimta, da musanyar fa’ida. Yana cika ADR ta ƙara tunani mai tsari, mai iya tabbatarwa a takardun shawara.
