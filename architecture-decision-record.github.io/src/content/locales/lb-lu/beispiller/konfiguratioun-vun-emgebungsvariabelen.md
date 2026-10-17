# Konfiguratioun vun Emgebungsvariabelen

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

Mir wëllen, datt eis Applikatioune iwwer Artefakten/Binaries/Quellcode eraus konfiguréierbar sinn, sou datt een Build sech jee no Deployment-Ëmfeld anescht verhale kann.

  * Fir dat z'erreechen, wëlle mir d'Konfiguratioun mat Emgebungsvariabele benotzen.

  * Mir wëllen d'Konfiguratioun verwalten, andeems mir Dateie benotzen, déi mir versionéiere kënnen.

  * Mir wëllen eng gewësse Entwécklerergonomie bidden, wéi ze wëssen, wat konfiguréiert ka ginn a wat déi relevant Standardwäerter sinn.


### Decisioun

Fir .env-Dateien mat verbonnener Standarddatei a Schema-Datei decidéiert.


### Zoustand

Decidéiert. Oppe fir nei Fäegkeeten, soubal se opkommen.


## Detailer


### Viraussetzungen

Mir bevirzugen d'Trennung vum Applikatiounscode an dem Ëmfeldcode. Mir huelen un, datt d'App a verschiddene Ëmfelder anescht muss funktionéieren, wéi an engem Entwécklungsëmfeld, Testëmfeld, Demoëmfeld, Produktiounsëmfeld, asw.

Mir bevirzugen d'Branchepraxis vun der "12 factor app" a nach méi déi verwandte Praxis vun der "15 factor app".

Vill vun eise fréiere Projeten hunn d'Konventioun vun enger `.env`-Datei oder engem ähnleche `.env`-Verzeechnes benotzt. Et ass typesch, dës aus der Versiounskontroll eraus ze halen an amplaz eng aner Manéier ze benotzen, fir se ze deployen, ze versionéieren an ze verwalten.


### Restriktiounen

Mir wëllen Geheimnisser aus eisem Quellcode-Management-(SCM)-Versiounskontrollsystem (VCS) eraushalen.

Mir wëllen no Kompatibilitéit mat populäre Software-Frameworks a Bibliothéike striewen. Zum Beispill huet Node e Modul "dotenv" fir d'Lies vun der Konfiguratioun mat Emgebungsvariabelen.


### Positiounen

Mir hunn e puer Usätz iwwerluecht:

  * D'Konfiguratioun an der App späichere, zum Beispill an enger Datei `config.js`.

  * D'Konfiguratioun am Ëmfeld späichere, zum Beispill an enger Datei `.env`.

  * D'Konfiguratioun vun enger bekannter Plaz ofruffen, wéi engem Lizenzserver.


### Argument

Mir hunn den Usaz vun enger Datei .env gewielt, well:

  * Hien ass populär, och ënner Experten.

  * Hie follegt dem Muster vun `.env`-Dateien, déi eis Teams vill Mol a ville Projeten erfollegräich benotzt hunn.

  * Hie ass einfach. Besonnesch sinn mir fir de Moment mat de bedeitende Kompromësser zefridden, déi mir gesinn, wéi e Mangel u Audit-Fäegkeeten am Verglach zu engem Lizenzserver-Usaz.


### Implikatiounen 

Mir musse erausfannen, wéi mir ëffentlech Konfiguratioun vun Emgebungsvariabelen vum Geheimnismanagement trennen.


## Verwandt


### Verwandt Decisiounen

Mir erwaarden, datt all eis Applikatioune dësen Usaz benotzen.

Mir plange, all eis Applikatiounen, déi e manner fäegen Usaz benotzen, wéi Hardcoding an engem Binary oder am Quellcode, ze aktualiséieren.

Mir loossen all eis Applikatiounen, déi e méi fäegen Usaz benotzen, wéi e Lizenzserver, esou wéi se sinn.


### Verwandt Ufuerderungen

Mir ginn Devops-Fäegkeeten fir d'Dateien derbäi, dorënner Hooks, Tester a kontinuéierlech Integratioun.

Mir mussen all Entwécklerkollegen iwwer dës Decisioun formatéieren.



### Verwandt Artefakten

All Beräich, wou mir deployen, brauch seng eege .env-Datei a verwandte Dateien.


### Verwandt Prinzipien

Einfach réckgängeg ze maachen.


## Notizen


Beispill-Datei `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Beispill-Datei `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Beispill-Datei `.env.schema` mat just de Schlësselen:

```env
NAME
EMAIL
```
