# Arkitektúrákvörðunarskrá: forritunarritlar

## Samhengi

Forritunarritlar eru nauðsynlegt verkfæri fyrir þróunaraðila til að skrifa og breyta kóða. Fjöldi kóðaritla er í boði, hver með sitt eigið safn eiginleika, kosta og galla. Tilgangur þessarar ADR er að skjalfesta arkitektúrákvarðanir sem teknar voru fyrir forritunarritla.

## Forgangsatriði

Arkitektúr forritunarritla ætti að setja eftirfarandi í forgang:

* **Einingaskipting**: Kóðaritillinn ætti að vera hannaður á einingaskiptan hátt sem gerir þróunaraðilum kleift að sérsníða hann og víkka út eftir þörfum. Þetta gefur sveigjanlegan arkitektúr sem getur lagað sig að þörfum ólíkra þróunaraðila og teyma.

* **Afköst**: Kóðaritillinn ætti að vera afkastamikill og svörunarfús, sem gerir þróunaraðilum kleift að vinna skilvirkt án þess að tólið sem þeir nota hægi á þeim.

* **Notendaviðmót**: Notendaviðmótið ætti að vera innsæislegt og auðvelt í notkun, svo þróunaraðilar geti einbeitt sér að kóðanum sínum í stað þess að berjast við ritilinn.

* **Útvíkkanleiki**: Kóðaritillinn ætti að vera hannaður þannig að auðvelt sé að víkka hann út með viðbótum og samþættingum frá þriðju aðilum.

* **Samhæfni**: Kóðaritillinn ætti að vera samhæfður fjölbreyttu úrvali forritunarmála og tækni, sem gerir hann að gagnlegu tóli fyrir breiðan hóp þróunaraðila.

## Ákvörðun

Á grundvelli þessara forgangsatriða ætti að hanna arkitektúr forritunarritla með eftirfarandi íhlutum:

* **Kjarni**: Þessi íhlutur veitir grunnvirkni kóðaritilsins, svo sem setningafræðilitun, textavinnslu og skráastjórnun.

* **Notendaviðmót**: Þessi íhlutur veitir notendaviðmót kóðaritilsins, þar á meðal valmyndir, verkfærastikur og flýtilykla.

* **Viðbætur**: Þessi íhlutur gerir þróunaraðilum kleift að víkka út virkni kóðaritilsins með því að setja upp viðbætur frá þriðju aðilum. Viðbætur geta veitt viðbótareiginleika, svo sem kóðaklárun, kóðaathugun (linting) eða villuleit.

* **Samþættingar**: Þessi íhlutur gerir kóðaritlinum kleift að samþættast öðrum verkfærum og tækni, svo sem útgáfustýringarkerfum, smíðakerfum eða villuleitarverkfærum.

## Rökstuðningur

Einingaskipting kóðaritilsins gerir þróunaraðilum kleift að sérsníða hann og víkka út eftir þörfum. Þetta er mikilvægt því ólíkir þróunaraðilar og teymi hafa ólíkar þarfir og vinnuflæði, og sveigjanlegur arkitektúr getur mætt þessum mun.

* **Afköst**: afar mikilvæg því þróunaraðilar þurfa að geta unnið skilvirkt án þess að verkfæri þeirra hægi á þeim. Afkastamikill kóðaritill er nauðsynlegur fyrir framleiðni og getur hjálpað þróunaraðilum að halda einbeitingu og athygli.

* **Notendaviðmót**: mikilvægt því það gerir þróunaraðilum kleift að einbeita sér að kóðanum sínum í stað þess að berjast við ritilinn. Þetta getur leitt til betri framleiðni og minni gremju hjá þróunaraðilum.

* **Útvíkkanleiki**: öflugur því hann gerir kleift að laga kóðaritilinn að ólíkum þörfum og vinnuflæði. Viðbætur og samþættingar frá þriðju aðilum geta veitt viðbótareiginleika og getu sem eru ekki hluti af kjarna ritilsins.

* **Samhæfni**: verðmæt því hún gerir kleift að nota kóðaritilinn með fjölbreyttu úrvali forritunarmála og tækni. Þetta gerir ritilinn að gagnlegra tóli fyrir breiðan hóp þróunaraðila.

Kjarna-, viðbóta-, samþættinga- og notendaviðmótsíhlutirnir veita skýran aðskilnað ábyrgðar og leyfa einingaskiptan arkitektúr sem auðvelt er að víkka út og sérsníða. Þessi arkitektúr er sveigjanlegur, afkastamikill og samhæfður fjölbreyttu úrvali forritunarmála og tækni, sem gerir hann að gagnlegu tóli fyrir þróunaraðila.