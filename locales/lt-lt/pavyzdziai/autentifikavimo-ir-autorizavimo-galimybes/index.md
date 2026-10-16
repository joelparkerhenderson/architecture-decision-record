# Architektūros sprendimo įrašas: autentifikavimo ir autorizavimo galimybės

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Interneto programų autentifikavimas ir autorizavimas yra dvi esminės sąvokos saugant prieigą prie programų ir paslaugų. Abi susijusios su naudotojų tapatybe ir tuo, kaip suteikiamos teisės, tačiau sutelkia dėmesį į skirtingus aspektus:

- **Autentifikavimas** yra naudotojo ar sistemos tapatybės patikrinimo procesas.
- **Autorizavimas** yra procesas, kuriuo nustatoma, prie kokių išteklių ar veiksmų gali prieiti autentifikuotas naudotojas ar sistema.

Dabar pasigilinkime į jūsų paminėtus konkrečius protokolus ir technologijas, kurios dažnai naudojamos šiuolaikinėse interneto programose autentifikavimui ir autorizavimui valdyti.

### 1. **OAuth (Open Authorization)**

**OAuth** yra atvirasis autorizavimo standartas. Jis leidžia naudotojui suteikti trečiosios šalies programai ribotą prieigą prie savo išteklių nesidalijant savo prisijungimo duomenimis. Pagrindinė idėja – **deleguota prieiga**. OAuth dažnai naudojamas situacijose, kai naudotojai gali prisijungti prie trečiosios šalies paslaugos (pvz., prisijungimas per „Google“) tiesiogiai nepateikdami trečiajai šaliai savo naudotojo vardo ir slaptažodžio.

- **Eiga**: OAuth paprastai laikosi **žetonais grįstos** eigos, kai autorizavimo serveris išduoda prieigos žetoną trečiosios šalies programai. Šis žetonas atspindi naudotojo teises, o programa jį naudoja naudotojo duomenims ar ištekliams pasiekti per API.
- **Pavyzdys**: naudotojas prisijungia prie trečiosios šalies programos naudodamas „Google“ paskyrą. „Google“ patikrina naudotojo tapatybę ir išduoda žetoną, leidžiantį trečiosios šalies programai pasiekti tam tikrus „Google“ duomenis (pvz., „Google“ kalendorių).

OAuth **netvarko** autentifikavimo tiesiogiai; jis skirtas prieigai suteikti. Autentifikavimui OAuth dažnai derinamas su kitais protokolais, pavyzdžiui, **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** yra tapatybės sluoksnis, sukurtas ant **OAuth 2.0**, kuris prie OAuth autorizavimo galimybių prideda autentifikavimą. Iš esmės OpenID Connect išplečia OAuth, kad jis tvarkytų **naudotojų autentifikavimą**, ir suteikia standartizuotą būdą programoms patikrinti naudotojo tapatybę.

- **Eiga**: kai naudotojas prisijungia per OpenID Connect, trečiosios šalies programa (be OAuth prieigos žetono) paprašo ir ID žetono. ID žetone yra informacija apie naudotoją (pvz., jo naudotojo vardas, el. paštas ir kiti teiginiai). Tai leidžia programai žinoti, kas yra naudotojas ir ar jis autentifikuotas.
- **Pavyzdys**: prisijungimas prie tokios paslaugos kaip „Slack“ naudojant „Google“ paskyrą („Google“ yra OpenID Connect teikėjas) apima autentifikavimą per OpenID Connect, o OAuth valdo prieigą prie jūsų „Google“ išteklių.

OIDC trečiųjų šalių programoms palengvina **naudotojų autentifikavimą**, tuo pat metu leisdamas smulkiai kontroliuoti, prie kokių išteklių tos programos gali prieiti.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** yra senesnis, XML pagrįstas standartas, naudojamas autentifikavimo ir autorizavimo duomenims keistis tarp šalių, ypač **vienkartinio prisijungimo (SSO)** scenarijuose. Jis daugiausia naudojamas įmonių aplinkose, kad naudotojai galėtų autentifikuotis vieną kartą ir pasiekti kelias programas iš naujo neįvesdami prisijungimo duomenų.

- **Eiga**: naudotojas pirmiausia autentifikuojasi pas tapatybės teikėją (IdP). IdP sugeneruoja pasirašytą **SAML tvirtinimą**, kuriame yra naudotojo tapatybė ir susiję atributai. Tvirtinimas siunčiamas paslaugos teikėjui (SP), kuris jį naudoja prieigai prie programos autorizuoti.
- **Pavyzdys**: darbuotojas prisijungia prie savo įmonės portalo (IdP) ir automatiškai prisijungia prie kitų sistemų, tokių kaip el. paštas, CRM ir kt., iš naujo neįvesdamas prisijungimo duomenų. Autentifikavimo procesas grindžiamas IdP išsiųstu SAML tvirtinimu.

SAML dažnai naudojamas **įmonių SSO sprendimuose** ir gerai tinka interneto programoms įmonių aplinkose, tačiau yra mažiau tinkamas mobiliesiems nei OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** yra dar vienas protokolas, naudojamas **vienkartiniam prisijungimui (SSO)**, ypač „Microsoft“ pagrįstose įmonių aplinkose. Jis yra **WS-* (Web Services)** specifikacijų šeimos dalis ir leidžia federuoti tapatybę tarp skirtingų saugumo sričių (pvz., tarp skirtingų organizacijų ar tarp skirtingų paslaugų).

- **Eiga**: WS-Federation leidžia **patikimam tapatybės teikėjui (IdP)** autentifikuoti naudotojus ir išduoti žetonus, kuriuos paslaugos teikėjas gali naudoti autorizavimui. Jis panašus į SAML, bet dažnai naudojamas scenarijuose, kurie labai priklauso nuo „Microsoft“ technologijų.
- **Pavyzdys**: naudotojas prisijungia prie įmonės programos, talpinamos „Microsoft Azure Active Directory“ (AD), ir jo tapatybė gali būti naudojama prieigai prie kitų federuotų paslaugų, įskaitant trečiųjų šalių tiekėjų talpinamas programas.

Nors WS-Federation daugelyje šiuolaikinių interneto aplinkų daugiausia pakeistas naujesniais protokolais, tokiais kaip OAuth 2.0 ir OpenID Connect, jis vis dar naudojamas paveldėtose sistemose, ypač „Microsoft“ orientuotose įmonėse.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** yra protokolas, naudojamas katalogų paslaugoms pasiekti ir valdyti; dažnai naudojamas **naudotojų prisijungimo duomenims saugoti** ir prieigos kontrolei valdyti centralizuotame kataloge (dažnai vadinamame **katalogų paslauga**). LDAP nėra skirtas būtent autentifikavimui ar autorizavimui, bet naudojamas tapatybės duomenims saugoti ir gauti, kurie vėliau naudojami šiuose procesuose.

- **Autentifikavimas**: LDAP leidžia programai autentifikuoti naudotojus užklausiant katalogų paslaugos prisijungimo duomenų (pvz., slaptažodžių).
- **Autorizavimas**: jis taip pat valdo naudotojų vaidmenis ir teises, padėdamas nustatyti, ar naudotojas turi prieigą prie tam tikrų išteklių.
- **Pavyzdys**: daugelis įmonių autentifikavimui ir autorizavimui naudoja LDAP pagrįstus katalogus (pvz., **Active Directory**), ypač „Windows“ aplinkose.

LDAP yra labai svarbus įmonėms valdant naudotojų prieigą prie vidinių sistemų, tačiau šiuolaikiniame interneto kontekste LDAP dažnai integruojamas su kitais protokolais, tokiais kaip SAML ar OAuth, kad tapatybės valdymas būtų išsamesnis.

### 6. **Socialinių tinklų SSO teikėjai**

Socialinių tinklų **vienkartinio prisijungimo (SSO)** teikėjai, tokie kaip **Facebook**, **Google**, **Twitter**, **GitHub** ir kiti, leidžia naudotojams autentifikuotis trečiųjų šalių programose naudojant savo socialinių tinklų prisijungimo duomenis. Tai **OAuth pagrįsto autentifikavimo** rūšis, kai trečiosios šalies paslauga (pvz., „Google“) yra tapatybės teikėjas.

- **Eiga**: naudotojas spusteli „Prisijungti per Google“ (pavyzdžiui). Programa nukreipia į „Google“, kur naudotojas prisijungia (jei dar neprisijungęs). Tada „Google“ pateikia prieigos žetoną arba ID žetoną trečiosios šalies programai, kurį galima naudoti naudotojui autentifikuoti ir galbūt jo duomenims pasiekti.
- **Pavyzdys**: daugelis programų leidžia prisijungti naudojant „Google“ ar „Facebook“ prisijungimo duomenis. Programa užkulisiuose naudos OAuth arba OpenID Connect, kad patikrintų jūsų tapatybę ir kai kuriais atvejais pasiektų tam tikrus socialinių tinklų duomenis.

Socialinių tinklų SSO yra patogus ir plačiai priimtas autentifikavimo metodas, nes sumažina trintį naudotojams, kurie gali nenorėti kurti dar vieno naudotojo vardo ir slaptažodžio.

---

### Skirtumų santrauka:

- **OAuth**: naudojamas autorizavimui, leidžia trečiųjų šalių programoms pasiekti naudotojo duomenis neatskleidžiant prisijungimo duomenų.
- **OpenID Connect**: išplečia OAuth, kad suteiktų autentifikavimą, leidžiantį programoms patikrinti naudotojo tapatybę.
- **SAML**: XML pagrįstas protokolas, naudojamas SSO, dažnai įmonių aplinkose.
- **WS-Federation**: „Microsoft“ specifinis tapatybės federavimo protokolas, naudojamas paveldėtose sistemose.
- **LDAP**: protokolas katalogų paslaugoms užklausti, kad būtų autentifikuojami naudotojai ir valdomas autorizavimas.
- **Socialinių tinklų SSO teikėjai**: OAuth pagrįstos sistemos (pvz., „Google“, „Facebook“), leidžiančios trečiųjų šalių programoms autentifikuoti naudotojus naudojant jų socialinių tinklų prisijungimo duomenis.

Kiekviena iš šių technologijų turi savo stipriąsias puses ir naudojimo atvejus, o šiuolaikinėse programose galite matyti jų derinį, naudojamą skirtingiems saugumo aspektams (pvz., OAuth/OIDC prieigai prie API, SAML įmonių SSO).
