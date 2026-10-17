# Architektur-Decisiounsopzeechnung: API mat JSON vs gRPC

## Zoustand

Akzeptéiert

## Kontext

Mir designen eng API fir en neie Service, deen vu verschiddene Clienten benotzt gëtt. Mir hunn zwou Optioune fir d'Ëmsetzung vun der API berécksiichtegt: JSON iwwer HTTP oder gRPC.

JSON iwwer HTTP ass en dacks benotzten Usaz, fir APIen ze bauen, an et gëtt vu ville Programméiersproochen a Frameworks ënnerstëtzt. Dësen Usaz ass einfach, liichtgewiichteg a liicht ze verstoen, wat en zu enger gudder Wiel fir vill Projeten mécht. Hien ka manner effizient sinn wéi aner Optiounen, besonnesch wann et ëm grouss Datenmengen geet.

gRPC, am Géigesaz, ass eng méi nei Technologie, déi eng méi effizient Manéier bitt, APIen ze bauen. Si benotzt binär Serialiséierung, fir Daten ze transferéieren, wat méi séier a kompakter ka sinn wéi JSON ze benotzen. gRPC ënnerstëtzt och bidirektionalt Streaming, wat et zu enger gudder Wiel fir Echtzäit-Applikatioune mécht.

## Decisioun

Nodeems mir d'Virdeeler an d'Nodeeler vu béiden Optioune berécksiichtegt hunn, hu mir decidéiert, gRPC fir eis API ze benotzen. Och wann JSON iwwer HTTP eng méi einfach Optioun ass, gleewen mir, datt gRPC eng méi effizient a skaléierbar Léisung fir eise Service bitt. Mir erwaarden och, datt eis API eng grouss Mass u Daten wäert verschaffen, an d'binär Serialiséierung vu gRPC wäert fir dëse Fall méi effizient sinn.

Zousätzlech gleewen mir, datt d'Ënnerstëtzung vu gRPC fir bidirektionalt Streaming fir Echtzäit-Applikatiounen nëtzlech wäert sinn, déi mir an Zukunft entwéckele kënnten.

## Konsequenzen

Wa mir gRPC wielen, musse mir e verschiddene Set u Tools a Bibliothéiken benotzen, fir eis API ze bauen, am Verglach mam Benotze vu JSON iwwer HTTP. Dat kann zousätzlech Zäit an Effort erfuerderen, fir dës Technologien ze léieren an ëmzesetzen. Zousätzlech mussen d'Clienten, déi eis API benotze wëllen, gRPC-kompatibel Bibliothéike benotzen, déi vläicht net sou breet ënnerstëtzt sinn wéi JSON-iwwer-HTTP-Bibliothéiken.

Mir gleewen awer, datt d'Virdeeler vum Benotze vu gRPC dës potenziell Nodeeler iwwerwiegen, a mir si sécher, datt dës Decisioun zu enger méi effizienter a skaléierbarer API féiere wäert.
