# Arkitektura-erabakien erregistroa: JSON edo gRPC erabiltzen duen API-a

## Egoera

Onartua

## Testuingurua

Hainbat bezerok erabiliko duten zerbitzu berri baterako API bat diseinatzen ari gara. API-a ezartzeko bi aukera aztertu ditugu: JSON HTTP gainean erabiltzea edo gRPC erabiltzea.

JSON HTTP gainean API-ak eraikitzeko modu oso hedatua da, eta programazio-lengoaia eta esparru askok onartzen dute. Ikuspegi hau sinplea, arina eta ulertzeko erraza da, eta horrek aukera ona bihurtzen du proiektu askotarako. Hala ere, beste aukerak baino eraginkortasun txikiagokoa izan daiteke, bereziki datu-kantitate handiak kudeatzeko orduan.

gRPC, berriz, teknologia berriagoa da, API-ak eraikitzeko modu eraginkorragoa eskaintzen duena. Serializazio bitarra erabiltzen du datuak transferitzeko, JSON erabiltzea baino azkarragoa eta trinkoagoa izan daitekeena. gRPC-k bi norabideko streaming-a ere onartzen du, eta horrek denbora errealeko aplikazioetarako aukera ona bihurtzen du.

## Erabakia

Bi aukeren alde onak eta txarrak aztertu ondoren, gure API-arentzat gRPC erabiltzea erabaki dugu. JSON HTTP gainean aukera sinpleagoa den arren, uste dugu gRPC-k gure zerbitzuarentzat soluzio eraginkorrago eta eskalagarriagoa emango duela. Gainera, aurreikusten dugu gure API-ak datu-kantitate handia kudeatuko duela, eta gRPC-ren serializazio bitarra eraginkorragoa izango dela erabilera-kasu honetarako.

Gainera, uste dugu gRPC-k bi norabideko streaming-a onartzeak etorkizunean garatu ditzakegun denbora errealeko aplikazioetarako onuragarria izango dela.

## Ondorioak

gRPC aukeratuz, gure API-a eraikitzeko JSON HTTP gainean erabiltzearekin alderatuta tresna eta liburutegi sorta desberdina erabili beharko dugu. Horrek denbora eta ahalegin gehigarria eska dezake teknologia horiek ikasteko eta ezartzeko. Gainera, gure API-a erabili nahi duten bezeroek gRPC-rekin bateragarriak diren liburutegiak erabili beharko dituzte, eta baliteke horiek JSON HTTP gaineko liburutegiak bezain zabal onartuta ez egotea.

Hala ere, uste dugu gRPC erabiltzearen onurak potentzialki eragozpen horiek baino handiagoak direla, eta konfiantza dugu erabaki honek API eraginkorrago eta eskalagarriagoa emango duela.
