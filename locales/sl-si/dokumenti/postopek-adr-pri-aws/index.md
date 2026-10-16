# Postopek zapisov arhitekturnih odločitev pri AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Zapis arhitekturne odločitve (ADR) je dokument, ki opisuje izbiro, ki jo ekipa sprejme glede pomembnega vidika programske arhitekture, ki jo namerava zgraditi. Vsak ADR opisuje arhitekturno odločitev, njen kontekst in njene posledice. ADR imajo stanja in zato sledijo življenjskemu ciklu. Za primer ADR glejte dodatek.

Postopek ADR kot rezultat ustvari zbirko zapisov arhitekturnih odločitev. Ta zbirka tvori dnevnik odločitev. Dnevnik odločitev zagotavlja kontekst projekta ter podrobne informacije o izvedbi in oblikovanju. Člani projekta preletijo naslove posameznih ADR, da dobijo pregled nad kontekstom projekta. ADR preberejo, da se poglobijo v izvedbe projekta in oblikovalske izbire.

Ko ekipa sprejme ADR, ta postane nespremenljiv. Če nova spoznanja zahtevajo drugačno odločitev, ekipa predlaga nov ADR. Ko ekipa sprejme novi ADR, ta nadomesti prejšnjega.

## Obseg postopka ADR

Člani projekta naj ustvarijo ADR za vsako arhitekturno pomembno odločitev, ki vpliva na programski projekt ali izdelek, vključno z naslednjim (Richards in Ford 2020):

* Struktura (na primer vzorci, kot so mikrostoritve)

* Nefunkcionalne zahteve (varnost, visoka razpoložljivost in odpornost na napake)

* Odvisnosti (sklopljenost komponent)

* Vmesniki (API-ji in objavljene pogodbe)

* Tehnike gradnje (knjižnice, ogrodja, orodja in procesi)

* Funkcionalne in nefunkcionalne zahteve so najpogostejši vhodni podatki postopka ADR.


## Vsebina ADR

Ko ekipa ugotovi potrebo po ADR, član ekipe začne pisati ADR na podlagi predloge za ves projekt. (Primere predlog si oglejte v organizaciji ADR na GitHubu.) Predloga poenostavi ustvarjanje ADR in zagotovi, da ADR zajame vse pomembne informacije. Vsak ADR naj vsaj opredeli kontekst odločitve, samo odločitev ter posledice odločitve za projekt in njegove izdelke. (Primere teh razdelkov glejte v dodatku.) Eden najmočnejših vidikov strukture ADR je, da se osredotoča na razlog za odločitev in ne na to, kako jo je ekipa izvedla. Razumevanje, zakaj je ekipa sprejela odločitev, drugim članom ekipe olajša sprejetje odločitve in preprečuje, da bi drugi arhitekti, ki niso sodelovali v postopku odločanja, to odločitev v prihodnosti razveljavili.


## Postopek uvedbe ADR

Vsak član ekipe lahko ustvari ADR, vendar naj ekipa vzpostavi opredelitev lastništva ADR. Vsak avtor, ki je lastnik ADR, naj dejavno vzdržuje in sporoča vsebino ADR. Zaradi jasnosti lastništva ta vodnik v nadaljevanju avtorje ADR imenuje lastniki ADR. Drugi člani ekipe lahko vedno prispevajo k ADR. Če se vsebina ADR spremeni, preden ekipa sprejme ADR, naj lastnik te spremembe odobri.

Ko ekipa prepozna arhitekturno odločitev in njenega lastnika, lastnik ADR na začetku postopka predloži ADR v stanju **Predlagan** (Proposed). ADR v stanju Predlagan so pripravljeni na pregled.

Lastnik ADR nato sproži postopek pregleda ADR. Cilj postopka pregleda ADR je odločiti, ali ekipa ADR sprejme, ugotovi, da ga je treba predelati, ali ga zavrne. ADR pregleda projektna ekipa, vključno z lastnikom. Sestanek za pregled naj se začne z namenskim časovnim oknom za branje ADR. V povprečju bi moralo zadostovati 10 do 15 minut. V tem času vsak član ekipe prebere dokument ter doda komentarje in vprašanja, da označi nejasne teme. Po fazi pregleda lastnik ADR prebere in z ekipo obravnava vsak komentar.

Če ekipa najde ukrepe za izboljšanje ADR, stanje ADR ostane **Predlagan**. Lastnik ADR oblikuje ukrepe in v sodelovanju z ekipo vsakemu ukrepu doda izvajalca. Vsak član ekipe lahko prispeva k ukrepom in jih razrešuje. Lastnik ADR je odgovoren za ponovno načrtovanje postopka pregleda.

Ekipa se lahko odloči tudi, da ADR zavrne. V tem primeru lastnik ADR doda razlog za zavrnitev, da prepreči prihodnje razprave o isti temi. Lastnik spremeni stanje ADR v **Zavrnjen** (Rejected).

Če ekipa ADR odobri, lastnik doda časovni žig, različico in seznam deležnikov. Lastnik nato posodobi stanje v **Sprejet** (Accepted).

ADR in dnevnik odločitev, ki ga ustvarjajo, predstavljajo odločitve, ki jih je sprejela ekipa, in zagotavljajo zgodovino vseh odločitev. Ekipa ADR, kjer je mogoče, uporablja kot referenco med pregledi kode in arhitekture. Poleg izvajanja pregledov kode, oblikovalskih nalog in izvedbenih nalog naj člani ekipe za strateške odločitve o izdelku pregledajo ADR.

Kot dobra praksa naj vsaka sprememba programske opreme gre skozi pregled s strani sodelavcev in zahteva vsaj eno odobritev. Med pregledom kode lahko pregledovalec kode najde spremembe, ki kršijo enega ali več ADR. V tem primeru pregledovalec avtorja spremembe kode prosi, naj kodo posodobi, in deli povezavo do ADR. Ko avtor kodo posodobi, jo sodelavci pregledovalci odobrijo in se združi v glavno kodno bazo.


## Postopek pregleda ADR

Ekipa naj ADR po sprejetju ali zavrnitvi obravnava kot nespremenljive dokumente. Spremembe obstoječega ADR zahtevajo ustvarjanje novega ADR, vzpostavitev postopka pregleda za novi ADR in odobritev ADR. Če ekipa novi ADR odobri, naj lastnik stanje starega ADR spremeni v **Nadomeščen** (Superseded).
