# Zäitstempel-Format

Inhalt:

* [Zesummefaassung](#zesummefaassung)
  * [Problem](#problem)
  * [Decisioun](#decisioun)
  * [Zoustand](#zoustand)
* [Detailer](#detailer)
  * [Viraussetzungen](#viraussetzungen)
  * [Restriktiounen](#restriktiounen)
  * [Positiounen](#positiounen)
  * [Argument](#argument)
  * [Implikatiounen](#implikatiounen)
* [Verwandt](#verwandt)
  * [Verwandt Decisiounen](#verwandt-decisiounen)
  * [Verwandt Ufuerderungen](#verwandt-ufuerderungen)
  * [Verwandt Artefakten](#verwandt-artefakten)
  * [Verwandt Prinzipien](#verwandt-prinzipien)
* [Notizen](#notizen)


## Zesummefaassung


### Problem

Mir wëllen verfollege kënnen, wéini Saache geschéien, andeems mir Zäitstempel benotzen an e konsistent Zäitstempel-Format benotzen, dat gutt iwwer all eis Systemer an Drëtt-Systemer funktionéiert.

Mir interagéieren mat Systemer, déi ënnerschiddlech Zäitstempel-Formater hunn:

* JSON-Messagen hunn kee native Zäitstempel-Format, dofir mussen mir wielen, wéi mir en Zäitstempel an e String konvertéieren, an e String an en Zäitstempel konvertéieren, dat heescht, wéi mir serialiséieren/deserialiséieren.

* E puer Applikatioune si fir d'Lokalzäit amplaz fir d'UTC-Zäit agestallt. Dat kann praktesch si fir Projeten, déi sech un d'Lokalzäit upasse mussen, wéi Projeten, déi Evenementer ausléisen, déi op der Lokalzäit baséieren.

* E puer Systemer hunn ënnerschiddlech Besoine a Fäegkeeten bei der Zäitgenauegkeet, wéi d'Notze vun enger Zäitopléisung vu Sekonnen vs. Millisekonnen vs. Nanosekonnen. Zum Beispill benotzt de Linux-Betribssystem-Kommando `date` eng Standard-Zäitgenauegkeet vu Sekonnen, während d'Nasdaq-Bourse eng Standard-Zäitgenauegkeet vu Nanosekonne wëll.


### Decisioun

Mir wielen den Zäitstempel-Standardformat ISO 8601 mat Nanosekonne-Genauegkeet, konkret "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

D'Format weist d'Joer, de Mount, den Dag, d'Stonn, d'Minutt, d'Sekonn, d'Nanosekonnen an d'Zulu-Zäitzon, och bekannt als UTC, GMT.


### Zoustand

Decidéiert.


## Detailer


### Viraussetzungen

Mir mussen dës Zäitstempel-Textstrings handhaben, fir vun engem Zäitstempel an e String ze konvertéieren (och bekannt als serialiséieren) an vun engem String an en Zäitstempel ze konvertéieren (och bekannt als deserialiséieren).

Mir wëllen e Format, dat allgemeng einfach ze benotze, einfach ze konvertéieren an einfach fir e Mënsch ze liesen ass.

Mir wëllen Kompatibilitéit mat enger breeder Palette vun externe Systemer, déi mir net kontrolléiere kënnen, wéi Analytiksystemer, Datebanksystemer, Finanzsystemer.


### Restriktiounen

E puer Systemer hunn Limitatioune bei der Zäitgenauegkeet. Zum Beispill kann de macOS-Betribssystem-Kommando `date` d'Zäitgenauegkeet a Sekonne ausdrécken, awer net a Nanosekonnen.


### Positiounen

Mir hunn eng Rei vun Optiounen berécksiichtegt:

* Unix-Epoch, dat heescht eng eenzeg opsteigend Zuel.

* Kuerzt Textformat "YYYYMMDDTHHMMSSNNNNNNNNN".

* Eng lokal Zäitzon vs. d'UTC-Zäitzon benotzen.


### Argument

Fir typesch Notzung schätze mir einfach ze liesen/schreiwen fir Mënschen méi héich wéi réng Vitess/Gréisst.

Fir typesch Notzung wëlle mir e Format, dat gutt a Maschinnesystemer funktionéiert, a gutt och manuell funktionéiert, wéi beim Schreiwe vu Beispilldaten, Liese vu JSON-Output, Grep vun enger Logdatei, asw.

Fir atypesch Notzung, wéi High-Performance-Computing, erwaarde mir, datt mir all Textformat, dat mir wielen, optiméiere wëllen, andeems mir den Text an e méi séiert Format konvertéieren, wéi den agebaute Datum-Objekttyp vun enger Programméiersprooch. Dofir ass d'Textformat fir HPC net sou wichteg.


### Implikatiounen

Eis verschidden Textsystemer a Zäitsystemer konvergéieren op dëst Format.


## Verwandt


### Verwandt Decisiounen

Mir wëllen eventuell e séiere/einfache Wee, och Zäitdeltas, och bekannt als Dauer, ze verfollegen. Dës si mat Unix-Epoch-Zäitstempel einfach.


### Verwandt Ufuerderungen

Mir wëllen eventuell eis Decisioun upassen, z.B. wa mir eng verwandt Ufuerderung fir eng spezifesch Zort vu Logging-Message-Stempel hunn, wéi fir Splunk, Sumo, ELK, asw.


### Verwandt Artefakten

Sproochformatter a Parser:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Rosetta-Code-Beispiller:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

SixArm-Beispiller:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Verwandt Prinzipien

Einfach réckgängeg ze maachen. Mir kënnen zimlech einfach op e anert Format wiesselen, wéi Unix-Epoch.

Verfréite Optimiséierung opschiebe. Fir typesch Notzung ass et eis net vill drun gelegen, wéi vill e puer extra Zeechen, wéi e Format mat Bindestrécher an Doppelpunkten.


## Notizen

Füügt hei Notizen derbäi.
