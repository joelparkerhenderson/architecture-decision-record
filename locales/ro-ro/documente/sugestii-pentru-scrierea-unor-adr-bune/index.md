## Sugestii pentru scrierea unor ADR bune

Caracteristicile unui ADR bun:

* Justificare: Explică motivele pentru care se ia decizia de arhitectură respectivă. Aceasta poate include contextul (vezi mai jos), avantajele și dezavantajele diferitelor alegeri posibile, comparații de funcționalități, discuții cost/beneficiu și altele.

* Specific: Fiecare ADR ar trebui să se refere la o singură decizie de arhitectură, nu la mai multe.

* Marcaje de timp: Indică momentul în care a fost scris fiecare element din ADR. Acest lucru este deosebit de important pentru aspectele care se pot schimba în timp, cum ar fi costurile, calendarele, scalarea și altele asemenea.

* Imuabil: Nu modifica informațiile existente dintr-un ADR. În schimb, completează ADR-ul adăugând informații noi sau înlocuiește-l creând un ADR nou.

Caracteristicile unei secțiuni „Context” bune într-un ADR:

* Explică situația organizației tale și prioritățile de business.

* Include justificări și considerații bazate pe componența socială și competențele echipelor tale.

* Include avantajele și dezavantajele relevante și descrie-le în termeni care se aliniază nevoilor și obiectivelor tale.

Caracteristicile unei secțiuni „Consecințe” bune într-un ADR:

* Explică ce rezultă din luarea deciziei. Aceasta poate include efecte, rezultate, produse, acțiuni ulterioare și altele.

* Include informații despre orice ADR-uri ulterioare. Este relativ obișnuit ca un ADR să genereze nevoia de alte ADR-uri, de exemplu atunci când un ADR face o alegere mare, generală, care la rândul ei creează nevoia unor decizii mai mici.

* Include orice procese de analiză ulterioară. Este tipic ca echipele să analizeze fiecare ADR după o lună, pentru a compara informațiile din ADR cu ceea ce s-a întâmplat în practică, pentru a învăța și a evolua.

Un ADR nou poate lua locul unui ADR anterior:

* Când se ia o decizie de arhitectură care înlocuiește sau invalidează un ADR anterior, trebuie creat un ADR nou
