# Entscheidungsprotokoll-Vorlage von Jeff Tyree und Art Akerman

Dies ist die Vorlage zur Beschreibung von Architekturentscheidungen, die in ["Architecture Decisions: Demystifying Architecture" von Jeff Tyree und Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf) veröffentlicht wurde.

* **Problem (Issue)**: Beschreiben Sie das Architekturentwurfsproblem, das Sie angehen, und lassen Sie keine Fragen offen, warum Sie dieses Problem jetzt angehen. Gehen Sie minimalistisch vor und behandeln und dokumentieren Sie nur die Probleme, die an verschiedenen Punkten im Lebenszyklus angegangen werden müssen.

* **Entscheidung (Decision)**: Geben Sie die Richtung der Architektur klar an, das heißt die Position, die Sie gewählt haben.

* **Status**: Der Status der Entscheidung, etwa pending, decided oder approved.

* **Gruppe (Group)**: Sie können eine einfache Gruppierung – etwa Integration, Präsentation, Daten usw. – verwenden, um die Menge der Entscheidungen zu ordnen. Sie könnten auch eine ausgefeiltere Architekturontologie verwenden, etwa die von John Kyaruzi und Jan van Katwijk, die abstraktere Kategorien wie Ereignis, Kalender und Ort enthält. Mit dieser Ontologie würden Sie zum Beispiel Entscheidungen, die sich mit Vorkommnissen befassen, bei denen das System Informationen benötigt, unter Ereignis gruppieren.

* **Annahmen (Assumptions)**: Beschreiben Sie klar die zugrunde liegenden Annahmen im Umfeld, in dem Sie die Entscheidung treffen – Kosten, Zeitplan, Technologie usw. Beachten Sie, dass Umfeldeinschränkungen (wie akzeptierte Technologiestandards, Unternehmensarchitektur, häufig eingesetzte Muster usw.) die von Ihnen betrachteten Alternativen einschränken können.

* **Einschränkungen (Constraints)**: Erfassen Sie alle zusätzlichen Einschränkungen für das Umfeld, die die gewählte Alternative (die Entscheidung) mit sich bringen könnte.

* **Positionen (Positions)**: Listen Sie die Positionen (tragfähige Optionen oder Alternativen) auf, die Sie erwogen haben. Diese erfordern oft lange Erklärungen, manchmal sogar Modelle und Diagramme. Dies ist keine erschöpfende Liste. Sie möchten jedoch in einer abschließenden Überprüfung nicht die Frage „Haben Sie an ... gedacht?“ hören; das führt zu Glaubwürdigkeitsverlust und zum Infragestellen anderer Architekturentscheidungen. Dieser Abschnitt hilft auch sicherzustellen, dass Sie die Meinungen anderer gehört haben; das ausdrückliche Nennen anderer Meinungen hilft, deren Befürworter für Ihre Entscheidung zu gewinnen.

* **Argument**: Skizzieren Sie, warum Sie eine Position gewählt haben, einschließlich Punkten wie Umsetzungskosten, Gesamtbetriebskosten, Markteinführungszeit und Verfügbarkeit der erforderlichen Entwicklungsressourcen. Das ist wahrscheinlich ebenso wichtig wie die Entscheidung selbst.

* **Implikationen (Implications)**: Eine Entscheidung hat viele Implikationen, wie das REMAP-Metamodell zeigt. Eine Entscheidung kann zum Beispiel die Notwendigkeit mit sich bringen, weitere Entscheidungen zu treffen, neue Anforderungen schaffen oder bestehende Anforderungen ändern, dem Umfeld zusätzliche Einschränkungen auferlegen, eine Neuverhandlung von Umfang oder Zeitplan mit Kunden erfordern oder zusätzliche Mitarbeiterschulungen verlangen. Die Implikationen Ihrer Entscheidung klar zu verstehen und zu benennen, kann sehr wirksam sein, um Zustimmung zu gewinnen und einen Fahrplan für die Umsetzung der Architektur zu erstellen.

* **Zugehörige Entscheidungen**: Es ist offensichtlich, dass viele Entscheidungen zusammenhängen; Sie können sie hier auflisten. Wir haben jedoch festgestellt, dass in der Praxis eine Rückverfolgbarkeitsmatrix, Entscheidungsbäume oder Metamodelle nützlicher sind. Metamodelle sind nützlich, um komplexe Beziehungen diagrammatisch darzustellen (etwa Rose-Modelle).

* **Zugehörige Anforderungen**: Entscheidungen sollten geschäftsgetrieben sein. Um Rechenschaftspflicht zu zeigen, ordnen Sie Ihre Entscheidungen ausdrücklich den Zielen oder Anforderungen zu. Sie können diese zugehörigen Anforderungen hier aufzählen, aber wir haben es bequemer gefunden, auf eine Rückverfolgbarkeitsmatrix zu verweisen. Sie können den Beitrag jeder Architekturentscheidung zur Erfüllung jeder Anforderung bewerten und dann beurteilen, wie gut die Anforderung über alle Entscheidungen hinweg erfüllt wird. Wenn eine Entscheidung nicht zur Erfüllung einer Anforderung beiträgt, treffen Sie diese Entscheidung nicht.

* **Zugehörige Artefakte**: Listen Sie die zugehörigen Architektur-, Entwurfs- oder Umfangsdokumente auf, auf die sich diese Entscheidung auswirkt.

* **Zugehörige Prinzipien**: Wenn das Unternehmen einen vereinbarten Satz von Prinzipien hat, stellen Sie sicher, dass die Entscheidung mit einem oder mehreren davon im Einklang steht. Das hilft, die Ausrichtung über Domänen oder Systeme hinweg sicherzustellen.

* **Notizen**: Da der Entscheidungsprozess Wochen dauern kann, haben wir es als nützlich empfunden, Notizen und Themen festzuhalten, die das Team während des Abstimmungsprozesses bespricht.

