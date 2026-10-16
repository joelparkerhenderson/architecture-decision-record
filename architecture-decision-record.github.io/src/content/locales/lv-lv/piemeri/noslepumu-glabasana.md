# Noslēpumu glabāšana

Saturs:

* [Kopsavilkums](#kopsavilkums)
  * [Jautājums](#jautājums)
  * [Lēmums](#lēmums)
  * [Statuss](#statuss)
* [Detaļas](#detaļas)
  * [Pieņēmumi](#pieņēmumi)
  * [Ierobežojumi](#ierobežojumi)
  * [Pozīcijas](#pozīcijas)
  * [Arguments](#arguments)
  * [Sekas](#sekas)
* [Saistītais](#saistītais)
  * [Saistītie lēmumi](#saistītie-lēmumi)
  * [Saistītās prasības](#saistītās-prasības)
  * [Saistītie artefakti](#saistītie-artefakti)
  * [Saistītie principi](#saistītie-principi)
* [Piezīmes](#piezīmes)
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Kopsavilkums


### Jautājums

Mums jāglabā noslēpumi, piemēram, paroles, privātās atslēgas, autentifikācijas marķieri utt.

Daži noslēpumi ir orientēti uz lietotājiem. Piemēram, mūsu izstrādātājs vēlas ar savu mobilo tālruni varēt atrast pakalpojuma paroli.

Daži noslēpumi ir orientēti uz sistēmām. Piemēram, mūsu nepārtrauktās piegādes cauruļvadam jāspēj atrast mūsu mākoņmitināšanas akreditācijas dati.


### Lēmums

Bitwarden lietotājiem orientētiem noslēpumiem

Vault by HashiCorp sistēmām orientētiem noslēpumiem.


### Statuss

Izlemts. Esam atvērti jaunām alternatīvām, kad tās parādās.


## Detaļas


### Pieņēmumi

Šim nolūkam un mūsu pašreizējam stāvoklim mēs vērtējam lietotājam orientētu ērtību, piemēram, lietojamas mobilās lietotnes.

  * Mēs vēlamies nodrošināt ātru un vieglu piekļuvi ceļā, piemēram, izstrādātājam, kas veic dežūras sistēmu uzticamības inženieriju.

  * Mēs vēlamies varēt kopīgot dažus noslēpumus starp izvēlētām personām, piemēram, komandu.

Mēs nemēģinām risināt vienam nodrošinātājam, piemēram, visu noslēpumu glabāšanai tikai Amazon vai Azure vai Google.

Mēs nevēlamies ad hoc pieejas, piemēram, „atceries to” vai „uzraksti uz zīmītes” vai „izdomā savu veidu, kā to glabāt”.

Mūsu drošības modelis šim nolūkam ir piemērots labi cienītu COTS piegādātāju, piemēram, SaaS paroļu pārvaldības rīku, izmantošanai.


### Ierobežojumi

Pašlaik mēs vēlamies kaut ko vieglu, t. i., nav jāraksta kods, nav jāinstalē serveri, nav jāuzņemas liela apņemšanās, nav visi jāstandartizē.


### Pozīcijas

Mēs apsvērām:

1. Lietotājam orientētus gatavus paroļu pārvaldniekus: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG utt.

2. Sistēmām orientētus COTS paroļu pārvaldniekus: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Uz kopīgošanu orientētas pieejas: koplietojama Google dokumenta, koplietojama Slack kanāla vai koplietojamas tīkla mapes utt. izmantošana.

4. Zemu tehnoloģiju ad hoc pieejas, piemēram, atcerēšanās, zīmītes rakstīšana vai paļaušanās uz to, ka katrs lietotājs izdomās savu pieeju.


### Arguments

Bitwarden, LastPass, 1Password un Dashlane visi ir komerciāli gatavi produkti (COTS).

  * Līdzīgi funkciju veidi lietotājiem, komandām, organizācijām utt.

  * Darbvirsmas iespējas Windows un Mac un mobilās iespējas Android un iOS.

  * Pārlūkprogrammu paplašinājumi Chrome un Firefox automātiskai veidlapu aizpildīšanai utt.

Bitwarden ir divas priekšrocības salīdzinājumā ar pārējiem:

  * Bitwarden ir atvērtā pirmkoda, kas nozīmē, ka drošību var pārskatīt kolēģi un uzņēmumu arī plaši novērtē uz drošību orientēti izstrādātāji.

  * Programmatūras darbinieku anekdotes apraksta ievērojamu priekšroku Bitwarden pār pārējiem.

Tipisks labs piemērs: https://jcs.org/2017/11/17/bitwarden

Tipiska blakus salīdzināšanas balsošanas vietne: https://stackshare.io/stackups/bitwarden-vs-dashlane

Mēs atliekam KeyPass, pass, GPG utt., jo ir papildu sarežģītība. Visi no tiem izskatās kā labi risinājumi tehniskiem lietotājiem. GPG izskatās īpaši labs tehniskiem lietotājiem, kuri vēlas starpsistēmu uz komandām orientētas iespējas.

Mēs atliekam KMS, jo tam ir viena nodrošinātāja piesaiste.

Mēs izvēlamies Vault sistēmām orientētām vajadzībām, jo atsauksmes ir pārsteidzoši pozitīvas un jo HashiCorp ir teicama vēsture augstākās kvalitātes programmatūras un atbalsta ziņā.

Mēs liekam veto pieejām ar kopīgošanu, piemēram, izmantojot koplietojamus dokumentus, koplietojamus kanālus, koplietojamas tīkla mapes utt. Tās nenodrošina drošības īpašības, kuras mēs vēlamies.

Mēs liekam veto ad hoc zemo tehnoloģiju pieejām, jo mēs visi piekrītam, ka tas nav ilgtermiņa ceļš uz priekšu.


### Sekas

Izstrādātājiem var būt jāseko noslēpumiem divās vietās: Bitwarden lietotājiem orientētai piekļuvei un Vault sistēmām orientētai piekļuvei.


## Saistītais


### Saistītie lēmumi

Lēmumam par to, kurš CI/CD serveris, jāietver spēju pierādījums piekļuvei noslēpumiem.

Mums būs jāizlemj, kā pārvaldīt noslēpumus attiecībā uz politikām, rotācijām, organizācijām utt.


### Saistītās prasības

Noslēpumiem būs saistītas prasības attiecībā uz atbilstību, revīziju un HR ievadīšanu/izvadīšanu.


### Saistītie artefakti

Mēs sagaidām, ka mēs varētu eksportēt dažus noslēpumus uz vides mainīgajiem.


### Saistītie principi

Viegli atgriezenisks.

Viegli paralēls, t. i., ir viegli izmantot dažādus paroļu pārvaldniekus.

Lēts izmēģināšanai, t. i., ir bezmaksas izmēģinājums un nav jāuzņemas apņemšanās.


## Piezīmes

Šeit ir izvērtēšanas piezīmes. Piezīmes ir visi publiskie komentāri dažādos DevOps diskusiju forumos.


### Vault by HashiCorp

Vault ir tieši tas, ko jūs šeit vēlaties. 

Taču nemetiet Vault uzreiz ražošanā, vispirms to uzstādiet testa vidē, jo HashiCorp dokumentācija var būt diezgan trūcīga, pat ja viņu produkti ir apbrīnojami.

Ļoti stāva mācīšanās līkne, un uzstādīšana nav triviāla. 

Sākotnējā uzstādīšana ir mazliet sāpīga. Tas tomēr ir ļoti vērts, un kopiena to atbalsta pietiekami labi, lai jūs tiktu galā.

Briesmīga dokumentācija, bet tiešsaistē ir daudz ceļvežu no cilvēkiem, kuri to ir uzstādījuši, un, ja jūs apvienosiet dažus no tiem, jums būs strādājoša uzstādīšana.

Sākotnējā uzstādīšana prasīja ņemties ar viņu helm diagrammām (vault un consul). Lai gan tehniski var izmantot daudz citu aizmugures sistēmu, es to patiešām patiešām neiesaku. Aizmugure/consul var būt ļoti maza, ja nav jāglabā liels datu apjoms.

Noteikti apgūstiet un iepazīstieties ar CLI lietošanu, jo GUI ir vairāk kā koncepcijas pierādījums/reklāmas portāls viņu uzņēmumu izdevumam.

Fakts, ka to nevar vienkārši „piepildīt”, ir sāpīgs. Piemēram, ja jums ir 5 lauki, jums katram vienumam manuāli jāpievieno katrs lauks. Tātad tas nav tā, ka jūs iepriekš definējat laukus konkrētai kategorijai un aizpildāt šos laukus visiem vienumiem šajā kategorijā, tas ir vairāk „jūs ģenerējat visu katru reizi”, kas (pēc manām domām) ir sāpe.

Iespējams, vēlēsities apskatīt arī goldfish kā UI virs vault. Tas diezgan labi palīdz iesaistīt jūsu komandu. Viņiem ir arī demonstrācija. 1. Uzstādiet consul. 2. Uzstādiet vault, kas norāda uz consul. 3. Uzstādiet goldfish, kas norāda uz vault. 3. Iestatiet kādu cron darbu, lai palaistu consul snapshot rezerves kopijām.



### LastPass

LastPass Teams. Mēs to lietojam, tam ir pielāgotas veidnes, ACL, pēc manām domām, nekā netrūkst.

Es ieviesu LastPass savā organizācijā un vērtēju to ar C+/B-. Lielākā problēma pēdējā laikā ir uzticamības trūkums. Pēdējo 90 dienu laikā ir bijušas vairākas stundas, kad velves tika piespiestas pārslēgt bezsaistes režīmā. Tas manai organizācijai nav ideāli, jo burtiski ir 4000+ paroļu, kas glabājas 20+ koplietojamās mapēs. Kā varat iedomāties, ar tik daudz parolēm vismaz dažas tiek atjauninātas vai pievienotas katru dienu. Mums ir DR plāns, ja problēmas ilgst vairāk nekā stundu vai divas: skripts katru nakti paraksta un šifrē velves CSV izgāzumu, ko var importēt keepass.

LastPass ir bijuši nepaziņoti pasliktināta pakalpojuma traucējumi: pieteikšanās „darbojas”, bet neizvelk vietnes, nejaušas funkcijas administratora panelī ir bojātas, un atslēgas netiek pareizi kopīgotas jaunām augstākā līmeņa koplietojamām mapēm. Man ir īpašs „atslēgu pūšanas”/rezerves kopēšanas lietotājs, kas ir katrā grupā. Parasti pieteikšanās kā šim lietotājam novērsīs atslēgu kopīgošanas problēmas, bet ne tad, kad pakalpojums ir pasliktināts, neskatoties uz to, ko saka statusa lapa...

Integrācijai tā var būt viegla, ja jums ir pareizas ACL ar mazāko privilēģiju modeli, piem., ja lietotājam ir lasīšana un rakstīšana un tikai lasīšana uz ierakstu vai mapi, viņš saņem tikai lasīšanas atļaujas. Diemžēl manas organizācijas ACL nav labākās, tāpēc es galu galā izmantoju JSON nodrošināšanas API un ~500 Python rindiņu, jo mūsu simtiem ACL atkarīgais raksturs labi nekartējas uz mazākās privilēģijas modeli. Es galu galā ieguvu visas ACL, kurās lietotājs bija, un veicu sava veida atkarību apstaigāšanu.

Ja jūsu ACL vai grupu struktūra jau ir veidota ar mazākās privilēģijas struktūru prātā, AD/LDAP sinhronizācijas rīks Windows darbosies labi.

Sazinieties ar viņu pārdošanas komandu, un viņi var nodrošināt garāku Enterprise izmēģinājumu. Pārliecinieties, ka pilnībā izprotat tā ierobežojumus, pirms pieņemat lēmumu. Mums bija diezgan daudz augšanas sāpju, bet, izņemot servera puses pārtraukumus vai traucējumus, viss ir bijis neticami gludi.


### Bitwarden

Bitwarden ir jauki rīki ap sevi (WebUI, CLI, mobilais, darbvirsma). Pašmitināms un diezgan viegli uzstādāms. Diezgan laba dokumentācija un PrivacyTools ieteikts rīks.


### EnvKey

https://www.envkey.com/ ir saas. Ļoti viegli ieviešams, integrējams un pārvaldāms.

Funkcijas:

  * Aizsargā API atslēgas un akreditācijas datus.

  * Uztur konfigurāciju sinhronizētu visur.

  * Gudra, no gala līdz galam šifrēta konfigurācijas un noslēpumu pārvaldība. 

  * Novērš nedrošu kopīgošanu un konfigurācijas izplūšanu. 

  * Integrācija dažās minūtēs.

Iespējas:

  * Pārvaldiet konfigurāciju un piekļuves līmeņus visām savām lietotnēm, vidēm un komandām vienuviet.

  * Konfigurējiet jebkuru izstrādes vai servera vidi tikai ar vienu vides mainīgo.

Priekšrocības:

  * Laba sākumlapa.

  * Skaidrs vērtības piedāvājums.

  * Vizuāli izcila tīmekļa lietotne.

  * Izcili piemēru dati, piem., Algolia, AWS, Datadog, GitHub, Stripe utt.

  * 30 minūtes runāju ar dibinātāju par uzņēmumu, UI utt. Dane šķiet labi informēts, godīgs par priekšrocībām/trūkumiem un dzīvotspējīgs partneris.

  * Uzņēmums būtībā ir tipisks Y Combinator uzņēmums ar 1 dibinātāju. 2018-01 piesaistīja 120 000 USD.

  * Uzmanības centrā ir uzņēmuma līmeņa funkciju sasniegšana, īpaši pāreja no EnvKey mākoņmitināšanas uz vai nu uz vietas, vai BYOC.

  * Potenciāls ceļš uz priekšu: sākt ar EnvKey vieglas lietošanas dēļ, vēlāk (vai paralēli) pievienojot Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant ir atvērtā pirmkoda noslēpumu pārvaldības pakalpojums, kas nodrošina lietotājam draudzīgu noslēpumu glabāšanu un piekļuvi tiem drošā veidā, no Lyft izstrādātājiem.

KMS autentifikācija: Confidant atrisina autentifikācijas problēmu „vista vai ola”, izmantojot AWS KMS un IAM, lai IAM lomas varētu ģenerēt drošus autentifikācijas marķierus, ko Confidant var pārbaudīt. Confidant pārvalda arī KMS piešķīrumus jūsu IAM lomām, kas ļauj IAM lomām ģenerēt marķierus, kurus var izmantot pakalpojumu savstarpējai autentifikācijai vai šifrētu ziņojumu nodošanai starp pakalpojumiem.

Versionēto noslēpumu šifrēšana miera stāvoklī: Confidant glabā noslēpumus tikai pievienošanas veidā DynamoDB, ģenerējot unikālu KMS datu atslēgu katrai katra noslēpuma revīzijai, izmantojot Fernet simetrisko autentificēto kriptogrāfiju.

Lietotājam draudzīga tīmekļa saskarne noslēpumu pārvaldībai: Confidant nodrošina AngularJS tīmekļa saskarni, kas ļauj gala lietotājiem viegli pārvaldīt noslēpumus, noslēpumu kartējumus uz pakalpojumiem un izmaiņu vēsturi.


### Devolutions Password Server

https://server.devolutions.net/

Nodrošiniet, pārvaldiet un uzraugiet piekļuvi privileģētiem kontiem un sesijām.

Visaptveroša, ļoti aizsargāta paroļu velve, kas ļauj kontrolēt piekļuvi jūsu privileģētajiem kontiem, vienlaikus uzlabojot kopējo tīkla redzamību sistēmu administratoriem un nodrošinot nevainojamu pieredzi gala lietotājiem.

Funkcijas: centralizēta organizācijas paroļu velve, lietotājam specifiska privātā velve, paroļu pārvaldnieks, akreditācijas datu ievadīšana,
Active Directory integrācija, uz lomām balstīta piekļuves kontrole, divfaktoru autentifikācija, gatavs uzņēmumiem, IP ierobežojumi, pārvaldības iespējas, automatizēts paroļu ģenerators, piekļuve mobilajai lietotnei, paroļu vēsture, piekļuves pārskati, e-pasta brīdinājumi.

  * atbalsta datu šifrēšanu

  * atbalsta vairākas autentifikācijas shēmas, tostarp LDAP, O365 un vietējos lietotājus AR MFA atbalstu no vairākiem avotiem

  * vairākas repozitorijas/velves ar smalku piekļuves kontroli vairākām komandām

  * moderns Web UI

  * privātas akreditācijas datu un savienojumu velves personīgajiem akreditācijas datiem/savienojumiem

  * mobilās lietotnes iOS/Android

  * katra ieraksta revīzijas žurnāli, kurš/ko/kad ar izvēles uzaicinājumu uz to, kāpēc viņi piekļūst

  * pielāgojamas veidnes (lai gan viņi dabiski atbalsta simtiem savienojumu veidu)

  * daudz vairāk funkciju un Windows/Mac biezais klients (Remote Desktop Manager), ar kuru varat sinhronizēties un kas ievērojami paplašina iespējas... savienojumi ar vienu klikšķi

  * cena nav tik slikta – līdz 15 lietotājiem paroļu serverim maksā 500 USD gadā


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Uz vietas versijas funkcijas: 

  * Pilnīga kontrole pār jūsu no gala līdz galam drošības sistēmām un infrastruktūru

  * Programmatūras izvietošana jūsu uz vietas datu centrā vai jūsu pašu virtuālā privātā mākoņa instancē

  * Atbilstība juridiskajām un regulatīvajām saistībām, kas prasa, lai visi dati un sistēmas atrastos uz vietas

Mākoņversijas funkcijas:

  * Programmatūras kā pakalpojuma modelis ļauj reģistrēties un sākt uzreiz

  * Elastīga mērogojamība, jums augot

  * Kontroli un redundanci nodrošina Azure ar 99,9 % darbspējas SLA

Lietotāju atsauksmes:

  * Mēs agrāk izmantojām šo produktu. To bija tik viegli apiet, un noteikumi darbojas tikai gudriem cilvēkiem. Slinki vai muļķīgi lietotāji to var viegli sabojāt komandas zonā. Cenas ir sarunājamas, kad ar viņiem runājat.

  * Jūs varat to darbināt, izmantojot SQL Express un Win 7 kasti. 

  * Lēts.
