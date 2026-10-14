# Arkitektúrákvörðunarskrá: API með JSON eða gRPC

## Staða

Samþykkt

## Samhengi

Við erum að hanna API fyrir nýja þjónustu sem verður notuð af mörgum biðlurum. Við höfum íhugað tvo valkosti við útfærslu API: að nota JSON yfir HTTP eða að nota gRPC.

JSON yfir HTTP er víða notuð nálgun við smíði API og er studd af mörgum forritunarmálum og römmum. Þessi nálgun er einföld, létt og auðskilin, sem gerir hana að góðum kosti fyrir mörg verkefni. Hún getur þó verið óskilvirkari en aðrir valkostir, sérstaklega þegar kemur að meðhöndlun mikils magns gagna.

gRPC er hins vegar nýrri tækni sem býður upp á skilvirkari leið til að smíða API. Hún notar tvíundarsíun (binary serialization) til að flytja gögn, sem getur verið hraðara og þéttara en að nota JSON. gRPC styður einnig tvíátta straumspilun, sem gerir hana að góðum kosti fyrir rauntímaforrit.

## Ákvörðun

Eftir að hafa vegið kosti og galla beggja valkosta höfum við ákveðið að nota gRPC fyrir API okkar. Þótt JSON yfir HTTP sé einfaldari valkostur teljum við að gRPC veiti skilvirkari og stigstærðari lausn fyrir þjónustu okkar. Við búumst einnig við því að API okkar muni meðhöndla mikið magn gagna og tvíundarsíun gRPC verður skilvirkari fyrir þetta notkunartilvik.

Að auki teljum við að stuðningur gRPC við tvíátta straumspilun muni nýtast í rauntímaforritum sem við gætum þróað í framtíðinni.

## Afleiðingar

Með því að velja gRPC þurfum við að nota annað safn verkfæra og safna til að smíða API okkar samanborið við JSON yfir HTTP. Þetta gæti krafist aukins tíma og fyrirhafnar til að læra og útfæra þessa tækni. Að auki þurfa biðlarar sem vilja nota API okkar að nota söfn sem eru samhæfð við gRPC, sem eru hugsanlega ekki jafn víða studd og söfn fyrir JSON yfir HTTP.

Við teljum þó að ávinningurinn af gRPC vegi þyngra en þessir hugsanlegu ókostir og erum fullviss um að þessi ákvörðun leiði til skilvirkara og stigstærðara API.
