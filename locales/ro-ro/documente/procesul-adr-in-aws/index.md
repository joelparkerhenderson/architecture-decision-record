# Procesul înregistrărilor deciziilor de arhitectură în AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

O înregistrare a deciziilor de arhitectură (ADR) este un document care descrie o alegere pe care echipa o face cu privire la un aspect semnificativ al arhitecturii software pe care plănuiește să o construiască. Fiecare ADR descrie decizia arhitecturală, contextul și consecințele ei. ADR-urile au stări și, prin urmare, urmează un ciclu de viață. Pentru un exemplu de ADR, consultă anexa.

Procesul ADR produce o colecție de înregistrări ale deciziilor de arhitectură. Această colecție formează jurnalul deciziilor. Jurnalul deciziilor oferă contextul proiectului, precum și informații detaliate despre implementare și proiectare. Membrii proiectului parcurg rapid titlurile fiecărui ADR pentru a obține o imagine de ansamblu asupra contextului proiectului. Citesc ADR-urile pentru a aprofunda implementările și alegerile de proiectare ale proiectului.

Când echipa acceptă un ADR, acesta devine imuabil. Dacă noi perspective cer o decizie diferită, echipa propune un nou ADR. Când echipa acceptă noul ADR, acesta îl înlocuiește pe cel anterior.

## Domeniul de aplicare al procesului ADR

Membrii proiectului ar trebui să creeze un ADR pentru fiecare decizie semnificativă pentru arhitectură care afectează proiectul sau produsul software, inclusiv următoarele (Richards și Ford 2020):

* Structura (de exemplu, tipare precum microserviciile)

* Cerințe non-funcționale (securitate, disponibilitate ridicată și toleranță la erori)

* Dependențe (cuplarea componentelor)

* Interfețe (API-uri și contracte publicate)

* Tehnici de construcție (biblioteci, framework-uri, instrumente și procese)

* Cerințele funcționale și non-funcționale sunt cele mai frecvente date de intrare ale procesului ADR.


## Conținutul unui ADR

Când echipa identifică nevoia unui ADR, un membru al echipei începe să scrie ADR-ul pe baza unui șablon valabil pentru întreg proiectul. (Vezi organizația ADR de pe GitHub pentru exemple de șabloane.) Șablonul simplifică crearea ADR-urilor și asigură că ADR-ul cuprinde toate informațiile relevante. Cel puțin, fiecare ADR ar trebui să definească contextul deciziei, decizia propriu-zisă și consecințele deciziei pentru proiect și livrabilele sale. (Pentru exemple ale acestor secțiuni, consultă anexa.) Unul dintre cele mai puternice aspecte ale structurii ADR este faptul că se concentrează pe motivul deciziei, nu pe modul în care echipa a implementat-o. Înțelegerea motivului pentru care echipa a luat decizia face mai ușoară adoptarea ei de către ceilalți membri ai echipei și împiedică alți arhitecți care nu au participat la procesul decizional să o anuleze în viitor.


## Procesul de adoptare a ADR

Orice membru al echipei poate crea un ADR, dar echipa ar trebui să stabilească o definiție a proprietății asupra unui ADR. Fiecare autor care este proprietarul unui ADR ar trebui să mențină activ și să comunice conținutul ADR-ului. Pentru a clarifica această proprietate, în secțiunile următoare acest ghid se referă la autorii ADR ca la proprietari ai ADR. Ceilalți membri ai echipei pot contribui oricând la un ADR. Dacă conținutul unui ADR se schimbă înainte ca echipa să îl accepte, proprietarul ar trebui să aprobe aceste modificări.

După ce echipa identifică o decizie arhitecturală și proprietarul ei, proprietarul ADR prezintă ADR-ul în starea **Proposed** (Propus) la începutul procesului. ADR-urile în starea Proposed sunt gata de analiză.

Apoi, proprietarul ADR inițiază procesul de analiză a ADR-ului. Scopul procesului de analiză a ADR este de a decide dacă echipa acceptă ADR-ul, stabilește că necesită refacere sau îl respinge. Echipa proiectului, inclusiv proprietarul, analizează ADR-ul. Ședința de analiză ar trebui să înceapă cu un interval de timp dedicat citirii ADR-ului. În medie, 10 până la 15 minute ar trebui să fie suficiente. În acest timp, fiecare membru al echipei citește documentul și adaugă comentarii și întrebări pentru a semnala subiectele neclare. După faza de analiză, proprietarul ADR citește și discută fiecare comentariu cu echipa.

Dacă echipa găsește puncte de acțiune pentru îmbunătățirea ADR-ului, starea ADR rămâne **Proposed**. Proprietarul ADR formulează acțiunile și, în colaborare cu echipa, adaugă un responsabil pentru fiecare acțiune. Fiecare membru al echipei poate contribui și poate rezolva punctele de acțiune. Este responsabilitatea proprietarului ADR să reprogrameze procesul de analiză.

Echipa poate decide și respingerea ADR-ului. În acest caz, proprietarul ADR adaugă un motiv al respingerii pentru a preveni discuții viitoare pe același subiect. Proprietarul schimbă starea ADR în **Rejected** (Respins).

Dacă echipa aprobă ADR-ul, proprietarul adaugă un marcaj de timp, o versiune și lista părților interesate. Apoi proprietarul actualizează starea la **Accepted** (Acceptat).

ADR-urile și jurnalul deciziilor pe care îl creează reprezintă deciziile luate de echipă și oferă un istoric al tuturor deciziilor. Echipa folosește ADR-urile ca referință în timpul analizelor de cod și de arhitectură, ori de câte ori este posibil. Pe lângă analizele de cod, sarcinile de proiectare și sarcinile de implementare, membrii echipei ar trebui să consulte ADR-urile pentru deciziile strategice privind produsul.

Ca bună practică, fiecare modificare software ar trebui să treacă prin analize între colegi și să necesite cel puțin o aprobare. În timpul analizei de cod, un recenzent poate găsi modificări care încalcă unul sau mai multe ADR-uri. În acest caz, recenzentul îi cere autorului modificării de cod să actualizeze codul și partajează un link către ADR. Când autorul actualizează codul, acesta este aprobat de colegii recenzenți și integrat în baza principală de cod.


## Procesul de analiză a ADR

Echipa ar trebui să trateze ADR-urile ca documente imuabile după ce le acceptă sau le respinge. Modificarea unui ADR existent necesită crearea unui nou ADR, stabilirea unui proces de analiză pentru noul ADR și aprobarea lui. Dacă echipa aprobă noul ADR, proprietarul ar trebui să schimbe starea vechiului ADR în **Superseded** (Înlocuit). 
