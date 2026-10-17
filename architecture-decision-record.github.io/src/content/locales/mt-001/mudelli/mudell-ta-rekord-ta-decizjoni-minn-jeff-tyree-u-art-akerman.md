# Mudell ta' rekord ta' deċiżjoni minn Jeff Tyree u Art Akerman

Dan huwa l-mudell għad-deskrizzjoni ta' deċiżjoni arkitettonika ppubblikat f'["Architecture Decisions: Demystifying Architecture" minn Jeff Tyree u Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Kwistjoni (Issue)**: Iddeskrivi l-kwistjoni tad-disinn arkitettoniku li qed tindirizza, mingħajr ma tħalli mistoqsijiet dwar għaliex qed tindirizza din il-kwistjoni issa. Skont approċċ minimalista, indirizza u iddokumenta biss il-kwistjonijiet li jeħtieġ jiġu indirizzati f'punti differenti taċ-ċiklu tal-ħajja.

* **Deċiżjoni (Decision)**: Iddikjara b'mod ċar id-direzzjoni tal-arkitettura—jiġifieri, il-pożizzjoni li għażilt.

* **Stat (Status)**: L-istat tad-deċiżjoni, bħal pendenti, deċiża, jew approvata.

* **Grupp (Group)**: Tista' tuża raggruppament sempliċi—bħal integrazzjoni, preżentazzjoni, data, u hekk għall-quddiem—biex tgħin torganizza s-sett ta' deċiżjonijiet. Tista' tuża wkoll ontoloġija tal-arkitettura aktar sofistikata, bħal dik ta' John Kyaruzi u Jan van Katwijk, li tinkludi kategoriji aktar astratti bħal avveniment (event), kalendarju (calendar), u post (location). Pereżempju, b'din l-ontoloġija, tiġbor fi grupp id-deċiżjonijiet li jittrattaw okkorrenzi fejn is-sistema teħtieġ informazzjoni taħt avveniment.

* **Suppożizzjonijiet (Assumptions)**: Iddeskrivi b'mod ċar is-suppożizzjonijiet sottostanti fl-ambjent li fih qed tieħu d-deċiżjoni—spiża, skeda, teknoloġija, u hekk għall-quddiem. Innota li restrizzjonijiet ambjentali (bħal standards teknoloġiċi aċċettati, arkitettura tal-intrapriża, xejriet komunement użati, u hekk għall-quddiem) jistgħu jillimitaw l-alternattivi li tikkunsidra.

* **Restrizzjonijiet (Constraints)**: Ġabar kwalunkwe restrizzjoni addizzjonali fuq l-ambjent li l-alternattiva magħżula (id-deċiżjoni) tista' timponi.

* **Pożizzjonijiet (Positions)**: Elenka l-pożizzjonijiet (għażliet vijabbli jew alternattivi) li kkunsidrajt. Spiss dawn jeħtieġu spjegazzjonijiet twal, kultant saħansitra mudelli u dijagrammi. Din mhijiex lista eżawrjenti. Madankollu, ma tridx tisma' l-mistoqsija "Ħsibt dwar...?" waqt reviżjoni finali; dan iwassal għal telf ta' kredibbiltà u kwestjonar ta' deċiżjonijiet arkitettoniċi oħra. Din it-taqsima tgħin ukoll biex tkun żgur li smajt l-opinjonijiet ta' oħrajn; li tiddikjara espliċitament opinjonijiet oħra jgħin biex is-sostenituri tagħhom jissieħbu fid-deċiżjoni tiegħek.

* **Argument (Argument)**: Iddeskrivi għaliex għażilt pożizzjoni, inklużi affarijiet bħall-ispiża tal-implimentazzjoni, l-ispiża totali tas-sjieda, iż-żmien għas-suq, u d-disponibbiltà tar-riżorsi meħtieġa għall-iżvilupp. Probabbilment dan huwa importanti daqs id-deċiżjoni nnifisha.

* **Implikazzjonijiet (Implications)**: Deċiżjoni ġġib magħha ħafna implikazzjonijiet, kif jindika l-metamudell REMAP. Pereżempju, deċiżjoni tista' toħloq il-ħtieġa li jittieħdu deċiżjonijiet oħra, toħloq rekwiżiti ġodda, jew timmodifika rekwiżiti eżistenti; timponi restrizzjonijiet addizzjonali fuq l-ambjent; teħtieġ li jerġa' jiġi nnegozjat l-ambitu jew l-iskeda mal-klijenti; jew teħtieġ taħriġ addizzjonali tal-persunal. Li tifhem u tiddikjara b'mod ċar l-implikazzjonijiet tad-deċiżjoni tiegħek jista' jkun effettiv ħafna biex tikseb l-appoġġ u toħloq pjan direzzjonali għall-eżekuzzjoni tal-arkitettura.

* **Deċiżjonijiet relatati (Related decisions)**: Huwa ovvju li ħafna deċiżjonijiet huma relatati; tista' telenkahom hawn. Madankollu, sibna li fil-prattika, matriċi ta' traċċabbiltà, siġar tad-deċiżjonijiet, jew metamudelli huma aktar utli. Il-metamudelli huma utli biex juru relazzjonijiet kumplessi b'mod dijagrammatiku (bħall-mudelli ta' Rose).

* **Rekwiżiti relatati (Related requirements)**: Id-deċiżjonijiet għandhom ikunu mmexxija min-negozju. Biex turi r-responsabbiltà, qabbad id-deċiżjonijiet tiegħek b'mod espliċitu mal-għanijiet jew mar-rekwiżiti. Tista' tenumera dawn ir-rekwiżiti relatati hawn, iżda sibna li huwa aktar konvenjenti li tirreferi għal matriċi ta' traċċabbiltà. Tista' tivvaluta l-kontribut ta' kull deċiżjoni arkitettonika biex jintlaħaq kull rekwiżit, u mbagħad tivvaluta kemm jintlaħaq sew ir-rekwiżit fid-deċiżjonijiet kollha. Jekk deċiżjoni ma tikkontribwixxix biex jintlaħaq rekwiżit, tieħux dik id-deċiżjoni.

* **Artefatti relatati (Related artifacts)**: Elenka d-dokumenti relatati tal-arkitettura, tad-disinn jew tal-ambitu li din id-deċiżjoni taffettwa.

* **Prinċipji relatati (Related principles)**: Jekk l-intrapriża għandha sett ta' prinċipji miftehma, kun żgur li d-deċiżjoni hija konsistenti ma' wieħed jew aktar minnhom. Dan jgħin biex jiġi żgurat l-allinjament fost id-dominji jew is-sistemi.

* **Noti (Notes)**: Minħabba li l-proċess tat-teħid tad-deċiżjonijiet jista' jieħu ġimgħat, sibna li huwa utli li jinġabru n-noti u l-kwistjonijiet li t-tim jiddiskuti matul il-proċess ta' soċjalizzazzjoni.
