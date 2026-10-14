# Șablon de înregistrare a deciziilor de Jeff Tyree și Art Akerman

Acesta este șablonul de descriere a deciziei de arhitectură publicat în ["Architecture Decisions: Demystifying Architecture" de Jeff Tyree și Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Problemă (Issue)**: Descrie problema de proiectare arhitecturală pe care o abordezi, fără să lași întrebări despre motivul pentru care o abordezi acum. Urmând o abordare minimalistă, abordează și documentează doar problemele care trebuie abordate în diferite momente ale ciclului de viață.

* **Decizie (Decision)**: Formulează clar direcția arhitecturii — adică poziția pe care ai ales-o.

* **Stare (Status)**: Starea deciziei, de exemplu în așteptare, luată sau aprobată.

* **Grup (Group)**: Poți folosi o grupare simplă — de exemplu integrare, prezentare, date etc. — pentru a organiza setul de decizii. Poți folosi și o ontologie de arhitectură mai sofisticată, cum ar fi cea a lui John Kyaruzi și Jan van Katwijk, care include categorii mai abstracte precum eveniment, calendar și locație. De exemplu, folosind această ontologie, ai grupa sub eveniment deciziile care se referă la întâmplări pentru care sistemul are nevoie de informații.

* **Ipoteze (Assumptions)**: Descrie clar ipotezele de bază din mediul în care iei decizia — cost, calendar, tehnologie etc. Reține că restricțiile de mediu (precum standardele tehnologice acceptate, arhitectura enterprise, tiparele folosite în mod obișnuit etc.) pot limita alternativele pe care le iei în considerare.

* **Constrângeri (Constraints)**: Consemnează orice constrângeri suplimentare pentru mediu pe care alternativa aleasă (decizia) le-ar putea impune.

* **Poziții (Positions)**: Enumeră pozițiile (opțiunile viabile sau alternativele) pe care le-ai luat în considerare. Acestea necesită adesea explicații lungi, uneori chiar modele și diagrame. Lista nu este exhaustivă. Totuși, nu vrei să auzi întrebarea „Te-ai gândit la...?” în timpul analizei finale; aceasta duce la pierderea credibilității și la punerea la îndoială a altor decizii arhitecturale. Această secțiune ajută și la asigurarea că ai ascultat opiniile altora; formularea explicită a altor opinii ajută la câștigarea susținătorilor lor pentru decizia ta.

* **Argument**: Prezintă pe scurt de ce ai ales o poziție, incluzând elemente precum costul de implementare, costul total de proprietate, timpul de lansare pe piață și disponibilitatea resurselor de dezvoltare necesare. Acesta este probabil la fel de important ca decizia însăși.

* **Implicații (Implications)**: O decizie vine cu multe implicații, după cum arată metamodelul REMAP. De exemplu, o decizie poate introduce nevoia de a lua alte decizii, poate crea cerințe noi sau modifica cerințe existente, poate impune constrângeri suplimentare mediului, poate necesita renegocierea domeniului sau a calendarului cu clienții ori poate necesita instruirea suplimentară a personalului. Înțelegerea și formularea clară a implicațiilor deciziei tale poate fi foarte eficientă pentru obținerea adeziunii și crearea unei foi de parcurs pentru execuția arhitecturii.

* **Decizii conexe (Related decisions)**: Este evident că multe decizii sunt legate între ele; le poți enumera aici. Totuși, am constatat că în practică o matrice de trasabilitate, arbori de decizie sau metamodele sunt mai utile. Metamodelele sunt utile pentru a arăta diagramatic relații complexe (de exemplu modelele Rose).

* **Cerințe conexe (Related requirements)**: Deciziile ar trebui să fie conduse de business. Pentru a arăta responsabilitatea, mapează explicit deciziile tale pe obiective sau cerințe. Poți enumera aici aceste cerințe conexe, dar am constatat că este mai convenabil să faci trimitere la o matrice de trasabilitate. Poți evalua contribuția fiecărei decizii de arhitectură la îndeplinirea fiecărei cerințe, apoi poți evalua cât de bine este îndeplinită cerința de toate deciziile. Dacă o decizie nu contribuie la îndeplinirea unei cerințe, nu lua acea decizie.

* **Artefacte conexe (Related artifacts)**: Enumeră documentele de arhitectură, de proiectare sau de domeniu conexe pe care această decizie le afectează.

* **Principii conexe (Related principles)**: Dacă întreprinderea are un set de principii agreat, asigură-te că decizia este în concordanță cu unul sau mai multe dintre ele. Aceasta ajută la asigurarea alinierii pe domenii sau sisteme.

* **Note (Notes)**: Deoarece procesul decizional poate dura săptămâni, am constatat că este util să consemnăm notele și problemele pe care echipa le discută în timpul procesului de socializare.

