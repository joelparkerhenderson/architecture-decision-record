# Rekord ta' deċiżjoni arkitettonika: API bl-użu ta' JSON vs gRPC

## Stat

Aċċettat

## Kuntest

Qed niddisinjaw API għal servizz ġdid li se jintuża minn klijenti multipli. Konna qed nikkunsidraw żewġ għażliet għall-implimentazzjoni tal-API: l-użu ta' JSON fuq HTTP jew l-użu ta' gRPC.

JSON fuq HTTP huwa approċċ użat ħafna biex jinbnew l-API, u huwa appoġġat minn ħafna lingwi tal-programmazzjoni u frameworks. Dan l-approċċ huwa sempliċi, ħafif, u faċli biex jinftiehem, u dan jagħmlu għażla tajba għal ħafna proġetti. Madankollu, jista' jkun inqas effiċjenti minn għażliet oħra, speċjalment meta jkun hemm bżonn li tiġi mmaniġġjata ammont kbir ta' data.

gRPC, min-naħa l-oħra, huwa teknoloġija aktar ġdida li toffri mod aktar effiċjenti kif jinbnew l-API. Juża serjalizzazzjoni binarja biex jittrasferixxi d-data, li tista' tkun aktar mgħaġġla u aktar kompatta mill-użu ta' JSON. gRPC jappoġġa wkoll l-istreaming bidirezzjonali, u dan jagħmlu għażla tajba għal applikazzjonijiet fi żmien reali.

## Deċiżjoni

Wara li kkunsidrajna l-vantaġġi u l-iżvantaġġi taż-żewġ għażliet, iddeċidejna li nużaw gRPC għall-API tagħna. Għalkemm JSON fuq HTTP huwa għażla aktar sempliċi, aħna nemmnu li gRPC se jipprovdi soluzzjoni aktar effiċjenti u skalabbli għas-servizz tagħna. Nantiċipaw ukoll li l-API tagħna se timmaniġġja ammont kbir ta' data, u s-serjalizzazzjoni binarja ta' gRPC se tkun aktar effiċjenti għal dan il-każ ta' użu.

Barra minn hekk, aħna nemmnu li l-appoġġ ta' gRPC għall-istreaming bidirezzjonali se jkun ta' benefiċċju għal applikazzjonijiet fi żmien reali li nistgħu niżviluppaw fil-futur.

## Konsegwenzi

Billi nagħżlu gRPC, se jkollna bżonn nużaw sett differenti ta' għodod u librerijiet biex nibnu l-API tagħna meta mqabbel mal-użu ta' JSON fuq HTTP. Dan jista' jeħtieġ ħin u sforz addizzjonali biex nitgħallmu u nimplimentaw dawn it-teknoloġiji. Barra minn hekk, il-klijenti li jixtiequ jużaw l-API tagħna se jkollhom bżonn jużaw librerijiet kompatibbli ma' gRPC, li jistgħu ma jkunux appoġġati daqs il-librerijiet ta' JSON fuq HTTP.

Madankollu, aħna nemmnu li l-benefiċċji tal-użu ta' gRPC jisbqu dawn l-iżvantaġġi potenzjali, u aħna kunfidenti li din id-deċiżjoni se tirriżulta f'API aktar effiċjenti u skalabbli.
