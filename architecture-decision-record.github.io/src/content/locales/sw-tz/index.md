# Rekodi ya uamuzi wa usanifu (ADR)

Rekodi ya uamuzi wa usanifu (ADR) ni hati inayonasa uamuzi muhimu wa usanifu uliofanywa pamoja na muktadha wake na matokeo yake.

> [!IMPORTANT]
> Fanya uchunguzi wako mwenyewe wa kina kuhusu rasilimali hizi kabla ya kuzitumia katika mifumo yoyote muhimu.

Yaliyomo:

- [Rekodi ya uamuzi wa usanifu ni nini?](#rekodi-ya-uamuzi-wa-usanifu-ni-nini)
- [Jinsi ya kuanza kutumia ADR](#jinsi-ya-kuanza-kutumia-adr)
- [Jinsi ya kuanza kutumia ADR na zana](#jinsi-ya-kuanza-kutumia-adr-na-zana)
- [Jinsi ya kuanza kutumia ADR na git](#jinsi-ya-kuanza-kutumia-adr-na-git)
- [Ujuzi wa Claude Code kwa ADR](#ujuzi-wa-claude-code-kwa-adr)
- [Kanuni za majina ya faili za ADR](#kanuni-za-majina-ya-faili-za-adr)
- [Mapendekezo ya kuandika ADR nzuri](#mapendekezo-ya-kuandika-adr-nzuri)
- [Mifano ya violezo vya ADR](#mifano-ya-violezo-vya-adr)
- [Ushauri wa kazi ya timu kwa ADR](#ushauri-wa-kazi-ya-timu-kwa-adr)
- [Maswali ya kazi ya timu kwa ADR](#maswali-ya-kazi-ya-timu-kwa-adr)
- [Dhana za hatua inayofuata kwa ADR](#dhana-za-hatua-inayofuata-kwa-adr)
- [Michoro ya usanifu na mionekano na mitazamo](#michoro-ya-usanifu-na-mionekano-na-mitazamo)
- [Kazi za ufaafu kwa maamuzi kama msimbo](#kazi-za-ufaafu-kwa-maamuzi-kama-msimbo)
- [Walinzi wa maamuzi kwa pull request](#walinzi-wa-maamuzi-kwa-pull-request)
- [Taarifa zaidi](#taarifa-zaidi)

Violezo:

- [Kiolezo cha rekodi ya uamuzi cha Jeff Tyree na Art Akerman](violezo/kiolezo-cha-rekodi-ya-uamuzi-cha-jeff-tyree-na-art-akerman/)
- [Kiolezo cha rekodi ya uamuzi cha Michael Nygard](violezo/kiolezo-cha-rekodi-ya-uamuzi-cha-michael-nygard/)
- [Kiolezo cha rekodi ya uamuzi cha EdgeX](violezo/kiolezo-cha-rekodi-ya-uamuzi-cha-edgex/)
- [Kiolezo cha rekodi ya uamuzi cha arc42](violezo/kiolezo-cha-rekodi-ya-uamuzi-cha-arc42/)
- [Kiolezo cha rekodi ya uamuzi kwa mtindo wa Alexander](violezo/kiolezo-cha-rekodi-ya-uamuzi-kwa-mtindo-wa-alexander/)
- [Kiolezo cha rekodi ya uamuzi kwa hoja ya biashara](violezo/kiolezo-cha-rekodi-ya-uamuzi-kwa-hoja-ya-biashara/)
- [Kiolezo cha rekodi ya uamuzi cha Mradi wa MADR](violezo/kiolezo-cha-rekodi-ya-uamuzi-cha-mradi-wa-madr/)
- [Kiolezo cha rekodi ya uamuzi kwa kutumia Planguage](violezo/kiolezo-cha-rekodi-ya-uamuzi-kwa-kutumia-planguage/)
- [Kiolezo cha rekodi ya uamuzi cha Paulo Merson](https://github.com/pmerson/ADR-template)
- [Kiolezo cha rekodi ya uamuzi cha Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Kiolezo cha rekodi ya uamuzi cha Gareth Morgan](violezo/kiolezo-cha-rekodi-ya-uamuzi-cha-gareth-morgan/)
- [Kiolezo cha rekodi ya uamuzi cha GIG Cymru NHS Wales](violezo/kiolezo-cha-rekodi-ya-uamuzi-cha-gig-cymru-nhs-wales/)
- [Kiolezo cha rekodi ya uamuzi kwa Maamuzi Muhimu ya Kiufundi (ITD) na Ignacio Larrañaga](violezo/kiolezo-cha-rekodi-ya-uamuzi-kwa-maamuzi-muhimu-ya-kiufundi/)

Mifano:

- [Mfumo wa CSS](mifano/mfumo-wa-css/)
- [Usanidi wa vigeu vya mazingira](mifano/usanidi-wa-vigeu-vya-mazingira/)
- [Vipimo, ufuatiliaji, tahadhari](mifano/vipimo-ufuatiliaji-na-tahadhari/)
- [Microsoft Azure DevOps](mifano/microsoft-azure-devops/)
- [Monorepo au multirepo](mifano/monorepo-au-multirepo/)
- [Lugha za programu](mifano/lugha-za-programu/)
- [Uhifadhi wa siri](mifano/uhifadhi-wa-siri/)
- [Muundo wa muhuri wa muda](mifano/muundo-wa-muhuri-wa-muda/)
- [Mengi zaidi...](mifano/)

## Rekodi ya uamuzi wa usanifu ni nini?

**Rekodi ya uamuzi wa usanifu** (ADR) ni hati inayonasa uamuzi muhimu wa usanifu uliofanywa pamoja na muktadha wake na matokeo yake.

**Uamuzi wa usanifu** (AD) ni chaguo la muundo wa programu linalokidhi hitaji muhimu.

**Kumbukumbu ya maamuzi ya usanifu** (ADL) ni mkusanyiko wa ADR zote zilizoundwa na kudumishwa kwa mradi (au shirika) fulani.

**Hitaji muhimu kiusanifu** (ASR) ni hitaji lenye athari inayopimika kwa usanifu wa mfumo wa programu.

Yote haya yako chini ya mada ya **usimamizi wa maarifa ya usanifu** (AKM).

Lengo la hati hii ni kutoa muhtasari wa haraka wa ADR, jinsi ya kuziunda, na mahali pa kutafuta taarifa zaidi.

Vifupisho:

  * **AD**: uamuzi wa usanifu

  * **ADL**: kumbukumbu ya maamuzi ya usanifu

  * **ADR**: rekodi ya uamuzi wa usanifu

  * **AKM**: usimamizi wa maarifa ya usanifu

  * **ASR**: hitaji muhimu kiusanifu

## Jinsi ya kuanza kutumia ADR

Ili kuanza kutumia ADR, zungumza na wenzako wa timu kuhusu maeneo haya.

Utambuzi wa uamuzi:

  * AD ina uharaka na umuhimu kiasi gani?

  * Je, lazima ifanywe sasa, au inaweza kusubiri hadi zaidi ijulikane?

  * Uzoefu wa kibinafsi na wa pamoja, pamoja na mbinu na mazoea ya usanifu yanayotambulika, vinaweza kusaidia katika kutambua maamuzi.

  * Kwa hali bora, dumisha orodha ya maamuzi ya kufanya inayokamilisha orodha ya kazi za bidhaa.

Kufanya uamuzi:

  * Mbinu kadhaa za kufanya maamuzi zipo, za jumla na zile mahsusi kwa usanifu wa programu, kwa mfano, ramani ya mazungumzo.

  * Kufanya maamuzi ya kikundi ni mada hai ya utafiti.

Kutekeleza na kusimamia utekelezaji wa uamuzi:

  * AD hutumika katika usanifu wa programu; kwa hivyo lazima ziwasilishwe kwa, na zikubaliwe na, wadau wa mfumo wanaoufadhili, kuutengeneza, na kuuendesha.

  * Mitindo ya uandishi wa msimbo inayoonyesha usanifu wazi na mapitio ya msimbo yanayolenga masuala na maamuzi ya usanifu ni mazoea mawili yanayohusiana.

  * AD pia lazima zifikiriwe upya (tena) wakati wa kuboresha mfumo wa programu katika mageuzi ya programu.

Kushiriki uamuzi (hiari):

  * AD nyingi hurudia katika miradi.

  * Kwa hivyo, uzoefu na maamuzi ya zamani, mazuri na mabaya, unaweza kuwa mali yenye thamani inayoweza kutumika tena unapotumia mkakati wa wazi wa usimamizi wa maarifa.

Kuandika uamuzi:

  * Violezo na zana nyingi za kunasa maamuzi zipo.

  * Tazama jumuiya za wepesi, mf. ADR za M. Nygard.

  * Tazama michakato ya jadi ya uhandisi wa programu na usanifu, mf. mipangilio ya jedwali inayopendekezwa na IBM UMF na Tyree na Akerman wa CapitalOne.

Kwa zaidi:

  * Hatua zilizo hapo juu zimechukuliwa kutoka makala ya Wikipedia kuhusu [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Jinsi ya kuanza kutumia ADR na zana

- [MySpec](https://myspec.dev) — Jukwaa la otomatiki la vipimo na maamuzi ya usanifu linalopanga katiba ya mradi, usanifu wa kiufundi, na ADR kuwa Markdown safi inayohudumiwa kupitia MCP.

Unaweza kuanza kutumia ADR na zana kwa njia yoyote unayotaka.

Kwa mfano:

  * Ikiwa unapenda kutumia Google Drive na uhariri wa mtandaoni, basi unaweza kuunda Google Doc, au Google Sheet.

  * Ikiwa unapenda kutumia udhibiti wa matoleo wa msimbo chanzi, kama git, basi unaweza kuunda faili kwa kila ADR.

  * Ikiwa unapenda kutumia zana za kupanga miradi, kama Atlassian Jira, basi unaweza kutumia kifuatiliaji cha upangaji cha zana hiyo.

  * Ikiwa unapenda kutumia wiki, kama MediaWiki, basi unaweza kuunda wiki ya ADR.

## Jinsi ya kuanza kutumia ADR na git

Ikiwa unapenda kutumia udhibiti wa matoleo wa git, basi hivi ndivyo tunavyopenda kuanza kutumia ADR na git kwa mradi wa kawaida wa programu wenye msimbo chanzi.

Unda saraka ya faili za ADR:

```sh
$ mkdir adr
```

Kwa kila ADR, unda faili ya maandishi, kama vile `choose-database.md`:

```sh
$ vi choose-database.md
```

Andika chochote unachotaka kwenye ADR. Tazama violezo katika hifadhi hii kwa mawazo.

Weka ADR kwenye hifadhi yako ya git (commit).

## Ujuzi wa Claude Code kwa ADR

Hifadhi hii ina ujuzi (skills) mbili za [Claude Code](https://claude.com/claude-code) chini ya [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), ili wakala wa AI wa uandishi wa msimbo aweze kuandika na kudumisha ADR kwa njia ambayo mradi huu unapendekeza:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — ya matumizi ya jumla, kwa yeyote anayeandika ADR katika mradi wowote. Husaidia kuamua kama uamuzi unahitaji ADR, huweka saraka ya `adr/` au `decisions/`, hupa faili jina, huchagua kiolezo kutoka kwa mifupa kumi na moja iliyojumuishwa, na huandika sehemu imara za Muktadha/Uamuzi/Matokeo.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — kwa wadumishaji wa hifadhi hii mahsusi. Huandika mpangilio wa hifadhi, kanuni ya kuakisi README/lugha, na hatua kamili za kuongeza kiolezo, mfano, au kiungo cha zana kipya.

Ili kutumia ujuzi, nakili folda yake kwenye `.claude/skills/` kwenye mzizi wa hifadhi unayofanyia kazi (au kwenye `~/.claude/skills/` ili ipatikane katika kila mradi), kisha mwombe Claude Code kuandika au kupitia ADR.

## Kanuni za majina ya faili za ADR

Ikiwa utachagua kuunda ADR zako ukitumia faili za kawaida za maandishi, basi unaweza kutaka kubuni kanuni yako ya majina ya faili za ADR.

Tunapendelea kutumia kanuni ya majina ya faili yenye muundo mahsusi.

Mifano:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Kanuni yetu ya majina ya faili:

  * Jina lina kishazi cha kitenzi cha amri cha wakati uliopo. Hii husaidia usomaji na inalingana na muundo wetu wa ujumbe wa commit.

  * Jina hutumia herufi ndogo na vistari (sawa na hifadhi hii). Huu ni usawa kati ya usomaji na urahisi wa matumizi ya mfumo.

  * Kiendelezi ni markdown. Hii inaweza kuwa na manufaa kwa uumbizaji rahisi.

## Mapendekezo ya kuandika ADR nzuri

Sifa za ADR nzuri:

* Sababu: Eleza sababu za kufanya AD mahsusi. Hii inaweza kujumuisha muktadha (tazama hapa chini), faida na hasara za chaguo mbalimbali zinazowezekana, ulinganisho wa vipengele, mijadala ya gharama/faida, na zaidi.

* Mahsusi: Kila ADR inapaswa kuhusu AD moja, si AD nyingi.

* Mihuri ya muda: Tambua wakati kila kipengele katika ADR kinapoandikwa. Hii ni muhimu hasa kwa vipengele vinavyoweza kubadilika kwa muda, kama gharama, ratiba, upanuzi, na vinavyofanana na hivyo.

* Isiyobadilika: Usibadilishe taarifa zilizopo katika ADR. Badala yake, rekebisha ADR kwa kuongeza taarifa mpya, au iondoe nafasi kwa kuunda ADR mpya.

Sifa za sehemu nzuri ya "Muktadha" katika ADR:

* Eleza hali ya shirika lako na vipaumbele vya biashara.

* Jumuisha sababu na mazingatio kulingana na muundo wa kijamii na ujuzi wa timu zako.

* Jumuisha faida na hasara zinazohusika, na uzieleze kwa maneno yanayolingana na mahitaji na malengo yako.

Sifa za sehemu nzuri ya "Matokeo" katika ADR:

* Eleza kinachofuata kutokana na kufanya uamuzi. Hii inaweza kujumuisha athari, matokeo, pato, ufuatiliaji, na zaidi.

* Jumuisha taarifa kuhusu ADR zozote zinazofuata. Ni jambo la kawaida kiasi kwamba ADR moja huchochea hitaji la ADR zaidi, kama ADR moja inapofanya chaguo kubwa la kuvuka mipaka, ambalo nalo huunda mahitaji ya maamuzi madogo zaidi.

* Jumuisha michakato yoyote ya mapitio baada ya kitendo. Ni kawaida kwa timu kupitia kila ADR mwezi mmoja baadaye, kulinganisha taarifa za ADR na kilichotokea katika utendaji halisi, ili kujifunza na kukua.

ADR mpya inaweza kuchukua nafasi ya ADR ya awali:

* Wakati AD inapofanywa inayochukua nafasi au kubatilisha ADR ya awali, basi ADR mpya inapaswa kuundwa

## Mifano ya violezo vya ADR

Mifano ya violezo vya ADR tulivyokusanya mtandaoni:

- [Kiolezo cha ADR cha Michael Nygard](violezo/kiolezo-cha-rekodi-ya-uamuzi-cha-michael-nygard/) (rahisi na maarufu)

- [Kiolezo cha ADR cha Jeff Tyree na Art Akerman](violezo/kiolezo-cha-rekodi-ya-uamuzi-cha-jeff-tyree-na-art-akerman/) (cha hali ya juu zaidi)

- [Kiolezo cha ADR kwa mtindo wa Alexander](violezo/kiolezo-cha-rekodi-ya-uamuzi-kwa-mtindo-wa-alexander/) (rahisi chenye maelezo ya muktadha)

- [Kiolezo cha ADR kwa hoja ya biashara](violezo/kiolezo-cha-rekodi-ya-uamuzi-kwa-hoja-ya-biashara/) (kinaelekea zaidi MBA, chenye gharama, SWOT, na maoni zaidi)

- [Kiolezo cha ADR cha mradi wa Markdown Any Decision Records (MADR)](violezo/kiolezo-cha-rekodi-ya-uamuzi-cha-mradi-wa-madr/) (toleo rahisi na la kina; la pili linasisitiza chaguo na faida na hasara zake)

- [Kiolezo cha ADR kwa kutumia Planguage](violezo/kiolezo-cha-rekodi-ya-uamuzi-kwa-kutumia-planguage/) (kinaelekea zaidi uhakikisho wa ubora)

- [Kiolezo cha Maamuzi Muhimu ya Kiufundi (ITD) na Ignacio Larrañaga](violezo/kiolezo-cha-rekodi-ya-uamuzi-kwa-maamuzi-muhimu-ya-kiufundi/) (chepesi na kinachotanguliza uamuzi, kimeboreshwa kwa mapitio ya haraka ya watendaji)

## Ushauri wa kazi ya timu kwa ADR

Ikiwa unafikiria kutumia rekodi za maamuzi na timu yako, basi huu hapa ni ushauri tuliojifunza kwa kufanya kazi na timu nyingi.

Una nafasi ya kuongoza wenzako wa timu, kwa kuzungumza pamoja kuhusu "kwa nini", badala ya kulazimisha "nini". Kwa mfano, rekodi za maamuzi ni njia kwa timu kufikiri kwa busara zaidi na kuwasiliana vizuri zaidi; rekodi za maamuzi hazina thamani ikiwa ni sharti la makaratasi ya kulazimishwa baada ya tukio.

Timu zingine hupendelea sana jina "maamuzi" kuliko kifupi "ADR". Timu zingine zinapotumia jina la saraka "decisions", ni kana kwamba taa imewaka, na timu huanza kuweka taarifa zaidi kwenye saraka, kama maamuzi ya wauzaji, maamuzi ya upangaji, maamuzi ya ratiba, n.k. Aina hizi zote za taarifa zinaweza kutumia kiolezo kilekile. Tunakisia kwamba watu hujifunza haraka zaidi kwa maneno ("maamuzi") kuliko vifupisho ("ADR"), na watu wana motisha zaidi ya kuandika hati za kazi inayoendelea neno "rekodi" linapoondolewa, na pia baadhi ya waundaji na baadhi ya mameneja hawapendi neno "usanifu".

Kwa nadharia, kutobadilika ni bora. Kwa vitendo, kubadilika kumefanya kazi vizuri zaidi kwa timu zetu. Tunaingiza taarifa mpya kwenye ADR iliyopo, na muhuri wa tarehe, na dokezo kwamba taarifa ilifika baada ya uamuzi. Mbinu hii inaongoza kwenye "hati hai" ambayo sote tunaweza kuisasisha. Masasisho ya kawaida ni tunapopata taarifa kutokana na wenzetu wapya wa timu, au huduma mpya, au matokeo halisi ya matumizi yetu, au mabadiliko ya wahusika wengine baada ya tukio kama uwezo wa muuzaji, mipango ya bei, makubaliano ya leseni, n.k.

## Maswali ya kazi ya timu kwa ADR

### Nani anaweza kuunda ADR?

Zingatia maeneo kama watu mahsusi, au majukumu mahsusi, au timu mahsusi, au idara mahsusi; pia zingatia kama kuna watu, au majukumu, au timu, au idara zinazoweza kuagiza ADR, yaani wanaomba moja ambayo mtu mwingine ataiandika.

Mfano wa jibu: Mtu yeyote katika shirika letu ambaye amesoma ukurasa wa README wa rekodi ya uamuzi wa usanifu anaweza kupendekeza ADR, yaani mtu huyo anaweza kuanza kuiandika, na kuishiriki na timu.

### Nini kinahalalisha kuanzisha ADR?

Zingatia maeneo kama njia za kufanya kazi za timu za shirika lako, muundo wa mfumo wako wa programu, uratibu kati ya timu, udumishaji wa muda mrefu, violesura vya nje, nani unataka anufaike, na yanayofanana na hayo.

Mfano wa jibu: Tunataka kuunda ADR tunapotaka waundaji wa baadaye waelewe "kwa nini" ya kile tunachofanya.

### Nini kinahalalisha kutoanzisha ADR?

Zingatia maeneo kama maamuzi ambayo si kuhusu usanifu, au ni madogo sana kama yenye hatari ndogo kabisa au yanayojitegemea au ya mwundaji mmoja, au tayari yameshughulikiwa kikamilifu mahali pengine kama kwa viwango au sera au nyaraka, au ni ya muda kama suluhisho za muda au uthibitisho wa dhana au majaribio.

Mfano wa jibu: Tunataka kuruka ADR wakati uamuzi una wigo mdogo wa mada na muda na hatari na gharama, au tayari umeshughulikiwa mahali pengine.

### Mzunguko wa maisha wa ADR ni upi?

Zingatia maeneo kama mchakato wa uundaji, mchakato wa utafiti, mchakato wa kufanya uamuzi, mchakato wa utekelezaji, na mchakato wa kuondoa. Zingatia jinsi ya kufuatilia mzunguko wa maisha wa ADR kwa muda, kama jinsi ya kuhamisha ADR kutoka hali moja hadi hali inayofuata, na pia jinsi ya kuwasilisha hili kwa wadau.

Mfano wa jibu: Tunataka ADR iwe na hatua tano za mzunguko wa maisha: Kuanzisha → Kutafiti → Kutathmini → Kutekeleza → Kudumisha → Kuondoa.

### Vigezo vya hatua za mzunguko wa maisha wa ADR ni vipi?

Zingatia maeneo kama vigezo vya kukubalika kwa ADR, yaani unajuaje ni nzuri vya kutosha kuendelea kutoka hatua moja ya mzunguko wa maisha hadi inayofuata? Je, tatizo limeelezwa wazi? Je, njia mbadala zimezingatiwa? Je, mabadilishano yanaeleweka na kuandikwa vya kutosha?
Je, muktadha wote husika upo? Je, wadau wote husika wanahusika? Je, maoni yote yamejumuishwa?

Mfano wa jibu: Tunataka ADR ipigiwe kura na wadau wakati timu hai imekamilisha 1) utafiti wao, 2) tathmini yao, 3) kuchapisha pendekezo la ADR kwa wadau pamoja na ombi la maoni na kikomo cha muda cha wiki moja, 4) maoni yote ya wadau yamejumuishwa na kushughulikiwa.

### Majukumu na wajibu gani huingiliana na ADR?

Zingatia majukumu kama mpendekezaji, mtafiti, mtathmini, mkaguzi, mwidhinishaji, mdumishaji, na yanayofanana na hayo. Zingatia wajibu kama mawasiliano na wadau, kuhakikisha matarajio yanatimizwa, kushiriki kwenye tovuti au intraneti, na kupitia kazi mara kwa mara na hasa wakati mabadiliko husika yanapotokea.

Mfano wa jibu: Tunataka kila ADR iwe na mtu mkuu wa mawasiliano, mtu wa pili wa mawasiliano, na timu inayowajibika; hawa wanawajibika kwa mawasiliano, machapisho, udumishaji, mapitio ya mara kwa mara angalau mara moja kwa mwaka, na kuondoa hatimaye inapohitajika.

### Usimamizi huingilianaje na ADR?

Zingatia maeneo kama njia za kufanya kazi za shirika lako, mahitaji yoyote maalum ya kufuata sheria kama kwa vipengele vya kisheria au vipengele vya rasilimali watu, jinsi unavyotaka kushughulikia makubaliano dhidi ya mgogoro dhidi ya kupandisha ngazi. Je, kuna maeneo au watu au timu zinazoweza kuwa na ushawishi zaidi kuliko wengine kuhusu ADR, kama kuweza kuiidhinisha, au kuipigia kura, au kuipinga kwa kura ya turufu?

Mfano wa jibu: Usimamizi wa ADR uko katika mpangilio huu wa kipaumbele: Mkurugenzi Mtendaji, Mkuu wa Teknolojia, Mkuu wa Sheria, timu inayotekeleza ADR, wataalamu wa timu wanaoijua AD vizuri zaidi. Hakuna mwingine aliye na usimamizi isipokuwa imeelezwa kwenye ADR.

### Kanuni gani huingiliana na ADR?

Zingatia maeneo kama njia za kufanya kazi za shirika lako zinazojumuisha kusonga haraka dhidi ya polepole, kwa makubaliano ya uamuzi dhidi ya mgogoro wa uamuzi, na kwa mapendeleo ya hatari dhidi ya mapendeleo ya usalama, mjadala wa hadharani dhidi ya mjadala wa faragha, na yanayofanana na hayo.

Mfano wa jibu: Tunatumia kanuni za uongozi za kuelekea vitendo, kutokubaliana-na-kujitolea, makadirio ya 70% yanatosha kwa maamuzi yanayoweza kurudishwa kwa urahisi na kutengwa kwa urahisi, na njia za kufanya kazi hadharani isipokuwa taarifa za siri kama zilivyoelezwa katika makubaliano ya usiri ya shirika letu.

## Dhana za hatua inayofuata kwa ADR

[Arc42](https://arc42.org/) hujibu maswali mawili kwa njia ya vitendo na inaweza kurekebishwa kulingana na mahitaji yako mahsusi. Unapaswa kuandika/kuwasilisha nini kuhusu usanifu wako? Unapaswa kuandika/kuwasilisha vipi? Arc42 inajumuisha rekodi za maamuzi ya usanifu pamoja na mwongozo kuhusu malengo, vikwazo, miktadha, ubora, hatari, na zaidi.

[Modeli ya C4](https://c4model.com/) ni mbinu rahisi kujifunza, rafiki kwa waundaji ya kuchora michoro ya usanifu wa programu. C4 ni seti ya michoro ya madaraja kwa muktadha, kontena, vipengele, msimbo, pamoja na michoro ya kusaidia kwa mandhari ya mfumo, mabadiliko, na uwekaji.

## Michoro ya usanifu na mionekano na mitazamo

Mchoro wa usanifu huitwa "mwonekano wa usanifu".

"Mwonekano wa usanifu" ni mfano wa "mtazamo wa usanifu".

"Mtazamo wa usanifu" una hadhira maalum yenye masuala maalum akilini.

Mifano ya mitazamo ya usanifu, mifano ya mionekano, na mifano ya michoro:

- Uwezo wa Biashara

- Michakato ya Biashara ya Kiwango cha Juu

- [Misururu ya Thamani](https://en.wikipedia.org/wiki/Value_stream)

- Kazi za Programu zilizopangwa kwa vipengele vya programu

- [Modeli ya C4](https://en.wikipedia.org/wiki/C4_model) Mchoro wa Muktadha (UTAKAVYOKUWA / ULIVYO SASA)

- [Modeli ya C4](https://en.wikipedia.org/wiki/C4_model) Mchoro wa Kontena (UTAKAVYOKUWA / ULIVYO SASA)

- [Mchoro wa Uhusiano wa Vyombo](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) kupanga vyombo vya data kwa vipengele vya programu

- [Michoro ya Mfuatano](https://en.wikipedia.org/wiki/Sequence_diagram) kueleza mtiririko wa kiutendaji ndani ya mifumo na kwa ujumuishaji

- Michoro ya [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) kueleza mtiririko wa data katika vipengele vya programu

- Michoro ya [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) kueleza michakato ya biashara / hali za watumiaji

- Michoro ya [Usimamizi wa Utambulisho na Ufikiaji](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM)

- Michoro ya [Udhibiti wa Ufikiaji Unaotegemea Majukumu](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) yenye majukumu kwa kila kipengele cha programu

- Michoro ya [Udhibiti wa Ufikiaji Unaotegemea Sifa](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) yenye sifa kwa kila kipengele cha programu

- Michoro ya faragha

Michoro inayohusiana:

- Mchoro wa Kisa cha Matumizi unaonyesha visa vya matumizi kwa usimamizi/wateja, ambao hutangulia mahitaji, ambayo hutangulia usanifu wa programu.

- Mchoro wa Uwekaji unaonyesha maunzi/kompyuta halisi ambazo vipengele vya programu vimewekwa juu yake.
- Mchoro wa Mtiririko wa Data unaonyesha jinsi data inavyosogea kupitia mfumo na kubadilishwa.
- Mchoro wa Mfuatano hutumika kuonyesha jinsi itifaki kama HTTP zinavyofanya kazi kwenye mhimili wa wakati.

- Mchoro wa Shughuli unaonyesha mtiririko wa kazi wa shughuli ambazo mfumo wa programu hufanya, kama AI ya NPC.

## Kazi za ufaafu kwa maamuzi kama msimbo

Kazi za ufaafu (fitness functions) ni ukaguzi wa kiotomatiki wa kiobjektivu, ulioandikwa kwa msimbo wa programu, unaothibitisha kwamba maamuzi yanadumishwa.

- Kazi za ufaafu hufanya maamuzi yaweze kujaribiwa na kuhakikishwa.

- Kazi za ufaafu kwa maamuzi zinaweza kusaidia sana uhakikisho wa ubora, michakato ya udhibiti, na malengo ya usimamizi.

### Jinsi kazi za ufaafu zinavyohusiana na maamuzi

Rekodi ya uamuzi huandika uamuzi, huku kazi ya ufaafu ikihakikisha uamuzi.

- Mfano wa uamuzi: Tunatumia event sourcing kwa mahitaji ya ukaguzi.

- Mfano wa kazi ya ufaafu: Tunatumia seva ya ujumuishaji endelevu kujaribu kwamba mabadiliko yote ya hali lazima yazalishe matukio.

### Kwa nini kazi za ufaafu husaidia maamuzi

Vipimo vya kiobjektivu: Kazi za ufaafu hufaulu au hushindwa, kwa hivyo kazi huonekana na iko wazi.

Matumizi endelevu: Kazi za ufaafu ni kanuni zako hai, zinazoendeshwa kwa kila commit na ujenzi.

Kujiamini kurekebisha msimbo: Kazi za ufaafu hunasa kiotomatiki makosa ya kanuni za maamuzi.

Usimamizi unaoweza kupanuka: Kazi za ufaafu huhakikisha viwango bila kuunda vikwazo.

### Je, kazi za ufaafu zinaweza kutumia akili bandia?

Kazi za ufaafu zinaweza kutumia modeli kubwa za lugha za akili bandia (LLM) kwa maamuzi kwa kuuliza maswali kuhusu kazi yako,
kama vile mipango yako, msimbo, skima, API, na zaidi:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Majaribio ya kitengo ya usanifu

[ArchUnit](https://www.archunit.org/): kagua kanuni za usanifu za msimbo wa Java kwa kutumia mfumo wowote wa kawaida wa majaribio ya kitengo wa Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kagua kanuni za usanifu za msimbo wa TypeScript na msimbo wa JavaScript kwa kutumia Jest, Vitest, Jasmine, n.k.

## Walinzi wa maamuzi kwa pull request

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
huleta kiotomatiki rekodi sahihi za maamuzi kwa wakati sahihi — wakati
mwundaji anapobadilisha kikamilifu msimbo ambao maamuzi hayo yanahusu. Badala ya
kutumaini waundaji wasome folda ya nyaraka kabla ya kuunganisha, muktadha
husika huonekana moja kwa moja kwenye pull request.

Hii inafanya kazi kwa aina yoyote ya rekodi ya uamuzi: maamuzi ya usanifu, maamuzi ya data,
maamuzi ya utiifu, maamuzi ya kikliniki na ya kimatibabu, maamuzi ya usalama,
na zaidi.

Inafanya kazi na mfumo wowote wa CI (GitLab, Jenkins, CircleCI) na kama ndoano ya pre-commit.
Chanzo huria. Leseni ya MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) ni GitHub
Action inayofelisha pull request pale njia za msimbo zinazofuatiliwa zinapobadilika bila
rekodi ya uamuzi wa usanifu kuongezwa au kusasishwa. Msamaha uko wazi: mstari wa
`ADR-Exempt:` wenye sababu hupitisha lango na huandikwa kwenye muhtasari wa
kazi. Haitegemei kiolezo, haina utegemezi. Chanzo huria. Leseni ya MIT.

## Taarifa zaidi

Utangulizi:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Violezo:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Kwa kina:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - somo la bure la kila mwezi la usanifu wa programu

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Zana:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Mwongozo Mahsusi wa Kampuni:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Mifano:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Video:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podikasti:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Vitabu:

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

Tazama pia:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Muundo wa YAML/JSON usiotegemea muuzaji, unaosomeka na mashine kwa kuwakilisha maamuzi yenye sababu wazi, dhana, hali ya kiakili, na mabadilishano. Hukamilisha ADR kwa kuongeza hoja zilizopangwa, zinazoweza kuthibitishwa kwenye nyaraka za maamuzi.
