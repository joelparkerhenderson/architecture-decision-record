# Jeff Tyree un Art Akerman lēmuma ieraksta veidne

Šī ir arhitektūras lēmuma apraksta veidne, kas publicēta rakstā [„Architecture Decisions: Demystifying Architecture”, autori Jeff Tyree un Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Jautājums (Issue)**: aprakstiet arhitektūras projektēšanas jautājumu, ko risināt, neatstājot nekādu šaubu par to, kāpēc šo jautājumu risināt tieši tagad. Ievērojot minimālisma pieeju, risiniet un dokumentējiet tikai tos jautājumus, kas jārisina dažādos dzīves cikla punktos.

* **Lēmums (Decision)**: skaidri norādiet arhitektūras virzienu – tas ir, pozīciju, ko esat izvēlējies.

* **Statuss (Status)**: lēmuma statuss, piemēram, gaida, pieņemts vai apstiprināts.

* **Grupa (Group)**: lai palīdzētu organizēt lēmumu kopu, varat izmantot vienkāršu grupēšanu – piemēram, integrācija, prezentācija, dati utt. Varat izmantot arī sarežģītāku arhitektūras ontoloģiju, piemēram, Džona Kjaruzi un Jana van Katvijka ontoloģiju, kas ietver abstraktākas kategorijas, piemēram, notikums, kalendārs un atrašanās vieta. Piemēram, izmantojot šo ontoloģiju, jūs grupētu lēmumus, kas attiecas uz gadījumiem, kad sistēmai nepieciešama informācija, zem notikuma.

* **Pieņēmumi (Assumptions)**: skaidri aprakstiet pamatā esošos pieņēmumus vidē, kurā pieņemat lēmumu – izmaksas, grafiks, tehnoloģija utt. Ņemiet vērā, ka vides ierobežojumi (piemēram, pieņemtie tehnoloģiju standarti, uzņēmuma arhitektūra, bieži izmantoti modeļi utt.) var ierobežot alternatīvas, ko apsverat.

* **Ierobežojumi (Constraints)**: fiksējiet jebkurus papildu vides ierobežojumus, ko izvēlētā alternatīva (lēmums) var radīt.

* **Pozīcijas (Positions)**: uzskaitiet pozīcijas (dzīvotspējīgas iespējas vai alternatīvas), ko apsvērāt. Tām bieži nepieciešami gari paskaidrojumi, dažkārt pat modeļi un diagrammas. Šis nav izsmeļošs saraksts. Tomēr galīgā pārskata laikā jūs nevēlaties dzirdēt jautājumu „Vai jūs padomājāt par...?”; tas noved pie uzticamības zaudēšanas un citu arhitektūras lēmumu apšaubīšanas. Šī sadaļa arī palīdz nodrošināt, ka esat uzklausījis citu viedokļus; citu viedokļu skaidra norādīšana palīdz piesaistīt viņu aizstāvjus jūsu lēmumam.

* **Arguments (Argument)**: izklāstiet, kāpēc izvēlējāties pozīciju, tostarp tādus aspektus kā īstenošanas izmaksas, kopējās piederības izmaksas, laiks līdz tirgum un nepieciešamo izstrādes resursu pieejamība. Tas, iespējams, ir tikpat svarīgi kā pats lēmums.

* **Sekas (Implications)**: lēmumam ir daudz seku, kā norāda REMAP metamodelis. Piemēram, lēmums var radīt nepieciešamību pieņemt citus lēmumus, radīt jaunas prasības vai mainīt esošās prasības; uzlikt papildu ierobežojumus videi; prasīt atkārtoti pārrunāt apjomu vai grafiku ar klientiem; vai prasīt papildu personāla apmācību. Skaidra sava lēmuma seku izpratne un norādīšana var būt ļoti efektīva, lai iegūtu atbalstu un izveidotu arhitektūras izpildes ceļvedi.

* **Saistītie lēmumi (Related decisions)**: ir skaidrs, ka daudzi lēmumi ir saistīti; varat tos uzskaitīt šeit. Tomēr praksē esam atklājuši, ka noderīgāka ir izsekojamības matrica, lēmumu koki vai metamodeļi. Metamodeļi ir noderīgi sarežģītu attiecību diagrammatiskai parādīšanai (piemēram, Rose modeļi).

* **Saistītās prasības (Related requirements)**: lēmumiem jābūt biznesa virzītiem. Lai parādītu atbildību, skaidri sasaistiet savus lēmumus ar mērķiem vai prasībām. Šīs saistītās prasības varat uzskaitīt šeit, taču esam atklājuši, ka ērtāk ir atsaukties uz izsekojamības matricu. Varat novērtēt katra arhitektūras lēmuma ieguldījumu katras prasības izpildē un pēc tam novērtēt, cik labi prasība tiek izpildīta visos lēmumos. Ja lēmums nesniedz ieguldījumu prasības izpildē, nepieņemiet šo lēmumu.

* **Saistītie artefakti (Related artifacts)**: uzskaitiet saistītos arhitektūras, projektēšanas vai apjoma dokumentus, ko šis lēmums ietekmē.

* **Saistītie principi (Related principles)**: ja uzņēmumam ir saskaņots principu kopums, pārliecinieties, ka lēmums atbilst vienam vai vairākiem no tiem. Tas palīdz nodrošināt saskaņotību pa domēniem vai sistēmām.

* **Piezīmes (Notes)**: tā kā lēmumu pieņemšanas process var ilgt nedēļas, esam atklājuši, ka ir noderīgi fiksēt piezīmes un jautājumus, ko komanda apspriež saskaņošanas procesā.

