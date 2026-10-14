# Sniðmát ákvörðunarskrár frá Jeff Tyree og Art Akerman

Þetta er sniðmátið fyrir lýsingu á arkitektúrákvörðunum sem birt er í ["Architecture Decisions: Demystifying Architecture" eftir Jeff Tyree og Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Vandamál (Issue)**: Lýstu arkitektúrhönnunarvandamálinu sem þú tekur á, svo að engar spurningar standi eftir um hvers vegna þú tekur á því núna. Með naumhyggjulegri nálgun skaltu aðeins takast á við og skjalfesta þau vandamál sem þarf að leysa á hverjum stað í lífsferlinum.

* **Ákvörðun (Decision)**: Settu skýrt fram stefnu arkitektúrsins — það er afstöðuna sem þú hefur valið.

* **Staða (Status)**: Staða ákvörðunarinnar, svo sem í bið, ákveðin eða samþykkt.

* **Hópur (Group)**: Þú getur notað einfalda hópun — svo sem samþætting, framsetning, gögn og svo framvegis — til að skipuleggja safn ákvarðana. Þú gætir einnig notað flóknari arkitektúrhugtakafræði, eins og John Kyaruzi og Jan van Katwijk, sem inniheldur óhlutbundnari flokka eins og atburð, dagatal og staðsetningu. Til dæmis, með þessari hugtakafræði myndirðu hópa ákvarðanir sem fjalla um tilvik þar sem kerfið krefst upplýsinga undir atburði.

* **Forsendur (Assumptions)**: Lýstu skýrt undirliggjandi forsendum í umhverfinu þar sem þú tekur ákvörðunina — kostnaði, tímaáætlun, tækni og svo framvegis. Athugaðu að takmarkanir umhverfisins (svo sem viðurkenndir tæknistaðlar, fyrirtækjaarkitektúr, algeng mynstur og svo framvegis) gætu takmarkað valkostina sem þú skoðar.

* **Takmarkanir (Constraints)**: Skráðu allar viðbótartakmarkanir á umhverfið sem valinn kostur (ákvörðunin) gæti sett.

* **Afstöður (Positions)**: Skráðu afstöðurnar (raunhæfa valkosti eða kosti) sem þú skoðaðir. Þessar krefjast oft langra útskýringa, stundum jafnvel líkana og skýringarmynda. Þetta er ekki tæmandi listi. Þú vilt hins vegar ekki heyra spurninguna „Datt þér í hug…?“ við lokarýni; það leiðir til trúverðugleikataps og efasemda um aðrar arkitektúrákvarðanir. Þessi hluti hjálpar einnig til við að tryggja að þú hafir heyrt skoðanir annarra; að setja aðrar skoðanir skýrt fram hjálpar til við að fá talsmenn þeirra til liðs við ákvörðun þína.

* **Röksemd (Argument)**: Settu fram hvers vegna þú valdir afstöðu, þar á meðal atriði eins og útfærslukostnað, heildareignarkostnað, tíma á markað og framboð á nauðsynlegum þróunarauðlindum. Þetta er líklega jafn mikilvægt og ákvörðunin sjálf.

* **Afleiðingar (Implications)**: Ákvörðun hefur margar afleiðingar, eins og REMAP-frumlíkanið tilgreinir. Til dæmis gæti ákvörðun skapað þörf fyrir að taka aðrar ákvarðanir, búið til nýjar kröfur eða breytt núverandi kröfum; sett frekari takmarkanir á umhverfið; krafist endursamninga um umfang eða tímaáætlun við viðskiptavini; eða krafist viðbótarþjálfunar starfsfólks. Að skilja og setja skýrt fram afleiðingar ákvörðunar þinnar getur verið mjög áhrifaríkt til að afla stuðnings og búa til vegvísi fyrir framkvæmd arkitektúrsins.

* **Tengdar ákvarðanir (Related decisions)**: Augljóst er að margar ákvarðanir eru tengdar; þú getur skráð þær hér. Við höfum þó komist að því að í reynd eru rekjanleikafylki, ákvörðunartré eða frumlíkön gagnlegri. Frumlíkön eru gagnleg til að sýna flókin tengsl á skýringarmynd (svo sem Rose-líkön).

* **Tengdar kröfur (Related requirements)**: Ákvarðanir ættu að vera knúnar af viðskiptum. Til að sýna ábyrgð skaltu skýrt tengja ákvarðanir þínar við markmið eða kröfur. Þú getur talið þessar tengdu kröfur upp hér, en við höfum komist að því að þægilegra er að vísa í rekjanleikafylki. Þú getur metið framlag hverrar arkitektúrákvörðunar til að uppfylla hverja kröfu og síðan metið hversu vel krafan er uppfyllt yfir allar ákvarðanir. Ef ákvörðun leggur ekki sitt af mörkum til að uppfylla kröfu, ekki taka þá ákvörðun.

* **Tengdar afurðir (Related artifacts)**: Skráðu tengd arkitektúr-, hönnunar- eða umfangsskjöl sem þessi ákvörðun hefur áhrif á.

* **Tengdar meginreglur (Related principles)**: Ef fyrirtækið hefur samþykkt safn meginreglna, tryggðu að ákvörðunin sé í samræmi við eina eða fleiri þeirra. Þetta hjálpar til við að tryggja samræmi milli sviða eða kerfa.

* **Athugasemdir (Notes)**: Þar sem ákvarðanataka getur tekið vikur höfum við komist að því að gagnlegt er að skrá athugasemdir og mál sem teymið ræðir í kynningarferlinu.
