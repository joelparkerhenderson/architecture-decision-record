# Architecture Decision Record: snake_case oder camelCase für eine REST-API?

Entscheidung: Für REST-API-Endpunkte wird die Namenskonvention snake_case verwendet

Status: Angenommen

## Kontext

Bei den Namenskonventionen für REST-APIs gibt es zwei verbreitete Formate: snake_case und camelCase. Bei snake_case ist jedes Wort im Namen durch Unterstriche getrennt, während bei camelCase das erste Wort des Namens kleingeschrieben wird und die folgenden Wörter mit einem Großbuchstaben beginnen. Diese Entscheidung bestimmt, welche Namenskonvention für eine REST-API verwendet werden soll.

## Entscheidungstreiber

- Konsistenz mit bestehenden Namenskonventionen im Projekt

- Lesbarkeit und Klarheit für alle, die an der API arbeiten

- Übereinstimmung mit Branchen-Best-Practices für Namenskonventionen von REST-APIs

- Einfache Umsetzung und Wartung

## Entscheidung

Für REST-API-Endpunkte wird die Namenskonvention snake_case verwendet. Diese Wahl wird von folgenden Faktoren getrieben:

1. **Konsistenz**: Das Projekt verwendet bereits die Namenskonvention snake_case für alle Endpunkte, und es wäre von Vorteil, diese Konvention beizubehalten, um Konsistenz im gesamten Projekt sicherzustellen.

2. **Lesbarkeit und Klarheit**: Die Konvention snake_case ist lesbarer und leichter verständlich. Die Unterstriche sorgen für eine klare Trennung zwischen den Wörtern, wodurch sich die Bedeutung des Namens leichter erfassen und verstehen lässt.

3. **Übereinstimmung mit Branchen-Best-Practices**: Die Konvention snake_case ist in der Branche weit verbreitet und gilt als Best Practice für REST-APIs, was sie zu einer guten Wahl für das Projekt macht.

4. **Einfache Umsetzung und Wartung**: Die Beibehaltung der bestehenden Namenskonvention ist einfacher umzusetzen und zu warten, da bei Wahl einer neuen Konvention der gesamte vorhandene Code und die Dokumentation aktualisiert werden müssten.

## Konsequenzen

Diese Entscheidung hat mögliche Konsequenzen. 

* Wenn neue Teammitglieder, die dem Projekt beitreten, mit der Namenskonvention snake_case nicht vertraut sind, könnte das zu Verwirrung und Fehlern in der Entwicklung führen. Da snake_case jedoch eine weit verbreitete Konvention ist, ist ein solches Risiko minimal. 
  
* Wenn im Projekt andere Werkzeuge oder Frameworks verwendet werden, die stark auf der Konvention camelCase beruhen, kann zusätzlicher Aufwand für die Umwandlung zwischen Namenskonventionen nötig sein. Das ist jedoch kein erhebliches Problem, da das Projekt sich auf die Konvention snake_case standardisiert hat. 
 
Insgesamt führt die Entscheidung, für REST-API-Endpunkte die Namenskonvention snake_case zu verwenden, zu einem konsistenten, lesbaren und branchenüblichen Ansatz, der zugleich einfach umzusetzen und zu warten ist.

<h6>Quellenangabe: Diese Seite wurde von ChatGPT erstellt und anschließend für Klarheit und Format bearbeitet.</h6>
