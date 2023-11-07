# Proses Cofnodion Penderfynol Pensaernïol AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Mae cofnod penderfyniad pensaernïol (ADR) yn ddogfen sy'n disgrifio dewis y mae'r tîm yn ei wneud am agwedd sylweddol ar y bensaernïaeth feddalwedd y maent yn bwriadu ei hadeiladu. Mae pob ADR yn disgrifio'r penderfyniad pensaernïol, ei gyd -destun, a'i ganlyniadau. Mae gan ADRs wladwriaethau ac felly'n dilyn cylch bywyd. Am enghraifft o ADR, gweler yr Atodiad.

Mae'r broses ADR yn allbynnu casgliad o gofnodion penderfyniadau pensaernïol. Mae'r casgliad hwn yn creu'r log penderfyniadau. Mae'r log penderfyniadau yn darparu cyd -destun y prosiect yn ogystal â gwybodaeth weithredu a dylunio fanwl. Mae aelodau'r prosiect yn sgimio penawdau pob ADR i gael trosolwg o gyd -destun y prosiect. Maent yn darllen yr ADRs i blymio'n ddwfn i weithrediadau prosiect a dewisiadau dylunio.

Pan fydd y tîm yn derbyn ADR, mae'n dod yn anadferadwy. Os oes angen penderfyniad gwahanol ar fewnwelediadau newydd, mae'r tîm yn cynnig ADR newydd. Pan fydd y tîm yn derbyn yr ADR newydd, mae'n disodli'r ADR blaenorol.

## Cwmpas y broses ADR

Dylai aelodau'r prosiect greu ADR ar gyfer pob penderfyniad pensaernïol arwyddocaol sy'n effeithio ar y prosiect meddalwedd neu'r cynnyrch, gan gynnwys y canlynol (Richards a Ford 2020):

* Strwythur (er enghraifft, patrymau fel microservices)

* Gofynion an swyddogaethol (diogelwch, argaeledd uchel, a goddefgarwch nam)

* Dibyniaethau (cyplu cydrannau)

* Rhyngwynebau (APIs a chontractau cyhoeddedig)

* Technegau adeiladu (llyfrgelloedd, fframweithiau, offer a phrosesau)

* Gofynion swyddogaethol ac an swyddogaethol yw'r mewnbynnau mwyaf cyffredin i'r broses ADR.


## CYNNWYS ADR

Pan fydd y tîm yn nodi'r angen am ADR, mae aelod o'r tîm yn dechrau ysgrifennu'r ADR yn seiliedig ar dempled ledled y prosiect. (Gweler Sefydliad ADR GitHub er enghraifft templedi.) Mae'r templed yn symleiddio creu ADR ac yn sicrhau bod yr ADR yn cyfleu'r holl wybodaeth berthnasol. O leiaf, dylai pob ADR ddiffinio cyd -destun y penderfyniad, y penderfyniad ei hun, a chanlyniadau'r penderfyniad ar gyfer y prosiect a'i gyflawniadau. (Am enghreifftiau o'r adrannau hyn, gweler yr Atodiad.) Un o agweddau mwyaf pwerus strwythur yr ADR yw ei fod yn canolbwyntio ar y rheswm dros y penderfyniad yn hytrach na sut y gwnaeth y tîm ei weithredu. Mae deall pam y gwnaeth y tîm y penderfyniad yn ei gwneud hi'n haws i aelodau eraill y tîm fabwysiadu'r penderfyniad, ac mae'n atal penseiri eraill nad oeddent yn rhan o'r broses benderfynu i ddiystyru'r penderfyniad hwnnw yn y dyfodol.


## Proses fabwysiadu ADR

Gall pob aelod o'r tîm greu ADR, ond dylai'r tîm sefydlu diffiniad o berchnogaeth ar gyfer ADR. Dylai pob awdur sy'n berchennog ADR gynnal a chyfleu'r cynnwys ADR yn weithredol. Er mwyn egluro'r berchnogaeth hon, mae'r canllaw hwn yn cyfeirio at awduron ADR fel perchnogion ADR yn yr adrannau canlynol. Gall aelodau eraill y tîm bob amser gyfrannu at ADR. Os yw cynnwys ADR yn newid cyn i'r tîm dderbyn yr ADR, dylai'r perchennog gymeradwyo'r newidiadau hyn.

Ar ôl i'r tîm nodi penderfyniad pensaernïol a'i berchennog, mae perchennog yr ADR yn darparu'r ADR yn y wladwriaeth ** ** ** ar ddechrau'r broses. Mae ADRs yn y wladwriaeth arfaethedig yn barod i'w hadolygu.

Yna mae perchennog yr ADR yn cychwyn y broses adolygu ar gyfer yr ADR. Nod y broses adolygu ADR yw penderfynu a yw'r tîm yn derbyn yr ADR, yn penderfynu bod angen ei ailweithio, neu'n gwrthod yr ADR. Mae tîm y prosiect, gan gynnwys y perchennog, yn adolygu'r ADR. Dylai'r cyfarfod adolygu ddechrau gyda slot amser pwrpasol i ddarllen yr ADR. Ar gyfartaledd, dylai 10 i 15 munud fod yn ddigon. Yn ystod yr amser hwn, mae pob aelod o'r tîm yn darllen y ddogfen ac yn ychwanegu sylwadau a chwestiynau i dynnu sylw at bynciau aneglur. Ar ôl y cam adolygu, mae perchennog yr ADR yn darllen allan ac yn trafod pob sylw gyda'r tîm.

Os yw'r tîm yn dod o hyd i bwyntiau gweithredu i wella'r ADR, mae cyflwr yr ADR yn aros ** arfaethedig **. Mae perchennog ADR yn llunio'r gweithredoedd, ac, mewn cydweithrediad â'r tîm, yn ychwanegu aseinai at bob gweithred. Gall pob aelod o'r tîm gyfrannu a datrys y pwyntiau gweithredu. Cyfrifoldeb perchennog yr ADR yw aildrefnu'r broses adolygu.

Gall y tîm hefyd benderfynu gwrthod yr ADR. Yn yr achos hwn, mae perchennog yr ADR yn ychwanegu rheswm dros y gwrthod i atal trafodaethau ar yr un pwnc yn y dyfodol. Mae'r perchennog yn newid y wladwriaeth ADR i ** Gwrthod **.

Os yw'r tîm yn cymeradwyo'r ADR, mae'r perchennog yn ychwanegu stamp amser, fersiwn, a rhestr o randdeiliaid. Yna mae'r perchennog yn diweddaru'r wladwriaeth i ** a dderbynnir **.

Mae ADRs a'r log penderfyniadau y maent yn ei greu yn cynrychioli penderfyniadau a wneir gan y tîm ac yn darparu hanes o'r holl benderfyniadau. Mae'r tîm yn defnyddio'r ADRs fel cyfeiriad yn ystod adolygiadau cod a phensaernïol lle bo hynny'n bosibl. Yn ogystal â pherfformio adolygiadau cod, tasgau dylunio, a thasgau gweithredu, dylai aelodau'r tîm ymgynghori ag ADRs ar gyfer penderfyniadau strategol ar gyfer y cynnyrch.

Fel arfer da, dylai pob newid meddalwedd fynd trwy adolygiadau cymheiriaid ac mae angen o leiaf un gymeradwyaeth. Yn ystod yr adolygiad cod, gallai adolygydd cod ddod o hyd i newidiadau sy'n torri un neu fwy o ADRs. Yn yr achos hwn, mae'r adolygydd yn gofyn i awdur y newid cod ddiweddaru'r cod, ac mae'n rhannu dolen i'r ADR. Pan fydd yr awdur yn diweddaru'r cod, caiff ei gymeradwyo gan adolygwyr cymheiriaid a'i uno â'r prif sylfaen cod.


## Proses Adolygu ADR

Dylai'r tîm drin ADRs fel dogfennau na ellir eu symud ar ôl i'r tîm eu derbyn neu eu gwrthod. Mae angen creu ADR newydd, sefydlu proses adolygu ar gyfer yr ADR newydd i newidiadau i ADR sy'n bodoli eisoes, a chymeradwyo'r ADR. Os yw'r tîm yn cymeradwyo'r ADR newydd, dylai'r perchennog newid cyflwr yr hen ADR i ** disodli **.
