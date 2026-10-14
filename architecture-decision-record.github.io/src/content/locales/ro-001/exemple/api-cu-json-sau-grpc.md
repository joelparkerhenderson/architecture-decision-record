# Înregistrare a deciziei de arhitectură: API cu JSON sau gRPC

## Stare

Acceptată

## Context

Proiectăm un API pentru un serviciu nou care va fi folosit de mai mulți clienți. Am luat în considerare două opțiuni de implementare a API-ului: JSON peste HTTP sau gRPC.

JSON peste HTTP este o abordare larg utilizată pentru construirea API-urilor și este suportată de multe limbaje de programare și framework-uri. Această abordare este simplă, ușoară și ușor de înțeles, ceea ce o face o alegere bună pentru multe proiecte. Totuși, poate fi mai puțin eficientă decât alte opțiuni, în special la manipularea unor cantități mari de date.

gRPC, pe de altă parte, este o tehnologie mai nouă care oferă un mod mai eficient de a construi API-uri. Folosește serializare binară pentru transferul datelor, care poate fi mai rapidă și mai compactă decât JSON. gRPC suportă și streaming bidirecțional, ceea ce îl face o alegere bună pentru aplicațiile în timp real.

## Decizie

După ce am cântărit avantajele și dezavantajele ambelor opțiuni, am decis să folosim gRPC pentru API-ul nostru. Deși JSON peste HTTP este o opțiune mai simplă, credem că gRPC va oferi o soluție mai eficientă și mai scalabilă pentru serviciul nostru. Anticipăm, de asemenea, că API-ul nostru va gestiona o cantitate mare de date, iar serializarea binară a gRPC va fi mai eficientă pentru acest caz de utilizare.

În plus, credem că suportul gRPC pentru streaming bidirecțional va fi benefic pentru aplicațiile în timp real pe care le-am putea dezvolta în viitor.

## Consecințe

Alegând gRPC, va trebui să folosim un set diferit de instrumente și biblioteci pentru a construi API-ul față de cazul JSON peste HTTP. Aceasta poate necesita timp și efort suplimentar pentru a învăța și a implementa aceste tehnologii. În plus, clienții care vor să folosească API-ul nostru vor trebui să folosească biblioteci compatibile cu gRPC, care pot fi mai puțin răspândite decât bibliotecile JSON peste HTTP.

Totuși, credem că beneficiile utilizării gRPC depășesc aceste potențiale dezavantaje și suntem încrezători că această decizie va avea ca rezultat un API mai eficient și mai scalabil.
