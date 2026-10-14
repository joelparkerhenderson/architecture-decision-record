# Rekodi ya Uamuzi wa Usanifu: maktaba ya chati kwa taswira ya data kwa TypeScript na JSON

<!--

ChatGPT prompt:

Long software architecture decision record 
chart library toolkit for data visualization using TypeScript and JSON

Evaluate Charts: Apache ECharts, Chart.js, ApexCharts, AG Charts, Highcharts, Carbon Charts, Layer Cake, D3.

Primary need: advanced interactive charts, especially for financial data, scientific data, and government data.

High importance: 1. Agile development because this is for a startup. 2. Doughnut Chart, Radar Chart, Clustering Process
Chart, Area Chart with Time Axis, Candlestick Chart, Nightingale Chart, Geo SVG Map. 3. Free open source.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Lengo Kuu:**  
Kuchagua zana ya hali ya juu ya chati ya kuunda taswira zenye mwingiliano, ikizingatia data ya kifedha, data ya kisayansi, na data ya serikali kwa kutumia TypeScript na JSON. Maktaba inapaswa kutoa vipengele thabiti, unyumbufu, na iwe ya chanzo huria.

### Muktadha na Mahitaji:

1. **Uundaji wenye Wepesi (Kipaumbele cha Juu)**: Kama kampuni changa, marudio ya haraka, utengenezaji wa mifano ya awali, na unyumbufu katika uundaji ni muhimu. Maktaba ya chati lazima iruhusu mizunguko ya haraka ya uundaji.
   
2. **Aina za Chati (Kipaumbele cha Juu)**:
   - **Chati ya Donati (Doughnut)**
   - **Chati ya Rada (Radar)**
   - **Chati ya Mchakato wa Kuunganisha (Clustering Process Chart)**
   - **Chati ya Eneo yenye Mhimili wa Wakati**
   - **Chati ya Mshumaa (Candlestick)**
   - **Chati ya Nightingale**
   - **Ramani ya Geo SVG**
   
   Aina hizi za chati ni muhimu hasa kwa kuonyesha seti changamano za data, kama mienendo ya kifedha, vipimo vya kisayansi, na taarifa za kijiografia.

3. **Bure na Chanzo Huria (Kipaumbele cha Juu)**: Zana inapaswa kuwa chanzo huria ili kuepuka gharama za leseni, kutoa uwazi, na kutoa unyumbufu wa ubinafsishaji.

4. **Vigezo vya Umuhimu wa Chini**:
   - **Kasi ya Utekelezaji**: Ingawa utendaji ni muhimu, si kipaumbele cha juu kwa uamuzi huu.
   - **Uwezo wa Kupanuka**: Ingawa uwezo wa kupanuka kwa ujumla ni muhimu, hitaji la haraka ni kujenga MVP ambayo inaweza kukua kwa muda. Masuala ya uwezo wa kupanuka yanaweza kushughulikiwa baadaye.
   - **Upatanifu wa Nyuma**: Si jambo kuu kwa ujenzi wa awali, mradi maktaba ni ya kisasa na inadumishwa kikamilifu.

### Maktaba Zilizotathminiwa:

1. **Apache ECharts**
2. **Chart.js**
3. **ApexCharts**
4. **AG Charts**
5. **Highcharts**
6. **Carbon Charts**
7. **Layer Cake**
8. **D3.js**

---

### 1. **Apache ECharts**

**Muhtasari**:  
Apache ECharts ni maktaba yenye nguvu, inayobadilika ya chati kwa taswira zenye mwingiliano, zinazoweza kubinafsishwa. Inatoa usaidizi kwa anuwai pana ya chati na ni imara hasa katika taswira changamano, zinazobadilika.

**Nguvu**:
- **Mwingiliano wa Hali ya Juu**: ECharts hufanya vizuri katika kutoa chati zenye mwingiliano, ikitoa vipengele kama kukuza, kusogeza, na masasisho ya data yanayobadilika.
- **Donati, Rada, Mshumaa, Ramani za Geo SVG**: ECharts inasaidia aina nyingi za chati zinazohitajika, ikiwa ni pamoja na donati, rada, mshumaa, na taswira za ramani za kijiografia.
- **Bure na Chanzo Huria**: ECharts ni maktaba ya chanzo huria, inayolingana na asili ya kuzingatia bajeti ya kampuni changa na inatoa uhuru wa kurekebisha msimbo.
- **Unyumbufu na Uwezo wa Kupanuliwa**: Inaweza kubinafsishwa sana, ikiwa na usaidizi mpana wa uhuishaji, taswira maalum, na mbinu za hali ya juu za chati.
  
**Udhaifu**:
- **Mkondo wa Kujifunza**: ECharts, ingawa ina nguvu, inaweza kuwa na mkondo mkali zaidi wa kujifunza kutokana na unyumbufu wake na API yake pana.
- **Utata wa Nyaraka**: Nyaraka ni za kina lakini zinaweza kuwa nyingi mno kwa waundaji wanaoanza tu kuitumia.

**Hukumu**:  
ECharts inafaa sana kwa mradi kutokana na usaidizi wake wa chati zenye mwingiliano, ikiwa ni pamoja na aina zote zinazohitajika kama chati za mshumaa, chati za rada, na ramani za geo. Asili yake ya chanzo huria inaendana na hitaji la mradi la unyumbufu na ufanisi wa gharama.

---

### 2. **Chart.js**

**Muhtasari**:  
Chart.js ni maktaba rahisi, rahisi kutumia ya chati kwa kujenga aina za kawaida za chati. Inajulikana kwa urahisi wake na urahisi wa ujumuishaji.

**Nguvu**:
- **Urahisi wa Matumizi**: Chart.js ni rahisi sana kusanidi na kutumia, ikiwa na mkondo mdogo wa kujifunza.
- **Chanzo Huria**: Chart.js ni bure na ya chanzo huria, jambo muhimu kwa kupunguza gharama.
- **Aina za Kawaida za Chati**: Inasaidia chati za msingi kama donati, eneo, rada, na chati za mstari, zinazofunika mahitaji mengi ya msingi.

**Udhaifu**:
- **Chati za Hali ya Juu Chache**: Chart.js haisaidii asilia aina changamano za chati kama chati za mshumaa, ramani za geo SVG, au chati za mchakato wa kuunganisha. Ingawa vipengele hivi vinaweza kuongezwa kupitia programu-jalizi au ubinafsishaji, si rahisi kama ilivyo kwa maktaba nyingine.
- **Mwingiliano**: Ingawa Chart.js inasaidia mwingiliano wa msingi (mf., vidokezo na athari za kuelea), haitoi vipengele vya hali ya juu kama ECharts au D3.js.

**Hukumu**:  
Chart.js ni nzuri kwa miradi rahisi, ya haraka, lakini ukosefu wake wa usaidizi wa aina changamano za chati hufanya isifae kwa programu nzito ya data yenye mahitaji ya hali ya juu kama chati za mshumaa na ramani za geo. Ni chaguo zuri kwa utengenezaji wa mifano ya awali, lakini kwa aina za chati zinazohitajika, zana za hali ya juu zaidi zinapendekezwa.

---

### 3. **ApexCharts**

**Muhtasari**:  
ApexCharts ni maktaba ya kisasa ya chati inayotoa aina mbalimbali za chati na inazingatia taswira zenye mwingiliano kwa API rahisi kutumia.

**Nguvu**:
- **Vipengele vyenye Mwingiliano**: ApexCharts hutoa chati zenye mwingiliano zenye vidokezo, kukuza, kusogeza, na masasisho.
- **Usaidizi wa Chati za Kifedha na Kisayansi**: Inasaidia anuwai pana ya aina za chati, ikiwa ni pamoja na chati za mshumaa, chati za rada, na chati za eneo.
- **Urahisi wa Matumizi**: Ina API ya moja kwa moja na ni rahisi kuunganisha katika mradi.
- **Bure na Chanzo Huria**: ApexCharts hutoa toleo la bure la chanzo huria linalofaa kwa visa vingi vya matumizi.
  
**Udhaifu**:
- **Ubinafsishaji Changamano**: Ingawa inatoa vipengele vingi, chaguo za ubinafsishaji si rahisi kama ECharts au D3.js kwa mahitaji changamano sana au maalum ya chati.
- **Ramani za Geo**: ApexCharts haisaidii asilia ramani za geo au chati za mchakato wa kuunganisha, ambazo zinahitajika kwa mradi huu.

**Hukumu**:  
ApexCharts ni mshindani mwenye nguvu kutokana na urahisi wa matumizi na mwingiliano wake, lakini inapungukiwa katika aina fulani za chati za hali ya juu, hasa hitaji la ramani za geo na chati za kuunganisha. Ni chaguo zuri kwa chati rahisi zaidi lakini inakosa baadhi ya vipengele vinavyohitajika.

---

### 4. **AG Charts**

**Muhtasari**:  
AG Charts ni maktaba ya chati ya kiwango cha kibiashara iliyobuniwa kwa utendaji na usahihi. Inafaa sana kwa kuunda dashibodi za kifedha, kisayansi, na za biashara.

**Nguvu**:
- **Aina za Hali ya Juu za Chati**: AG Charts inasaidia aina nyingi za hali ya juu za chati, ikiwa ni pamoja na chati za mshumaa, chati za eneo, chati za rada, na zaidi. Pia hutoa ujumuishaji wa kina na bidhaa nyingine za AG-Grid.
- **Utendaji wa Juu**: Inatoa utendaji bora, hasa inaposhughulika na seti kubwa za data.
- **Mwingiliano**: AG Charts inasaidia vipengele mbalimbali vya mwingiliano kama kukuza, vidokezo, na masasisho yanayobadilika.

**Udhaifu**:
- **Si Bure Kabisa**: Ingawa AG Charts inatoa toleo la bure, toleo lenye vipengele vyote ni la kulipia, jambo linaloweza kuwa kikwazo kwa kampuni changa zinazotaka kupunguza gharama.
- **Utata**: Ingawa maktaba ina vipengele vingi, inaweza kuwa kubwa mno kwa miradi rahisi zaidi na inaweza kuhitaji usanidi na usanidi zaidi ikilinganishwa na chaguo nyingine.

**Hukumu**:  
AG Charts ina nguvu na ina vipengele vingi lakini huenda isiwe inayofaa zaidi kutokana na asili yake ya kibiashara na muundo wa gharama. Kufaa kwake kunategemea kama bajeti inaweza kuhimili matoleo ya kulipia au kama njia mbadala za chanzo huria zinapendelewa.

---

### 5. **Highcharts**

**Muhtasari**:  
Highcharts ni maktaba maarufu ya chati inayojulikana kwa anuwai pana ya aina za chati na chaguo zenye nguvu za ubinafsishaji.

**Nguvu**:
- **Aina Kamili za Chati**: Highcharts inasaidia anuwai pana ya chati, ikiwa ni pamoja na mshumaa, rada, eneo, na ramani za geo.
- **Yenye Mwingiliano na Inayobadilika**: Highcharts hutoa vipengele tajiri vya mwingiliano, ikiwa ni pamoja na kuchimba kwa undani, kukuza, na kusogeza.
- **Urahisi wa Matumizi**: Ina API rafiki kwa mtumiaji na nyaraka nzuri, na kurahisisha kuanza.

**Udhaifu**:
- **Leseni ya Kibiashara**: Ingawa Highcharts inatoa toleo la bure kwa matumizi yasiyo ya kibiashara, leseni ya kibiashara ni ghali, jambo linaloweza kuwa hasara kubwa kwa kampuni changa.
- **Mkondo wa Kujifunza**: Ingawa si mkali kama wa ECharts, mkondo wa kujifunza wa Highcharts bado unaweza kuwa changamoto kwa wanaoanza.

**Hukumu**:  
Highcharts ni maktaba yenye vipengele vingi, lakini leseni yake ya kibiashara huifanya isifae sana kwa miradi ya chanzo huria na inayozingatia gharama. Chaguo zake kamili za chati ni faida, lakini suala la leseni linapunguza mvuto wake kwa kisa hiki cha matumizi.

---

### 6. **Carbon Charts**

**Muhtasari**:  
Carbon Charts ni maktaba ya chati iliyoundwa na IBM, iliyobuniwa kuunda chati zinazovutia kwa macho na zinazoweza kubinafsishwa sana.

**Nguvu**:
- **Uwezo wa Kubinafsishwa**: Carbon Charts inaruhusu ubinafsishaji mpana wa mwonekano na tabia ya chati.
- **Chanzo Huria**: Ni bure na ya chanzo huria, jambo linaloendana na hitaji la mradi la suluhisho rafiki kwa bajeti.
- **Usaidizi wa Chati za Kawaida**: Inasaidia aina za kawaida za chati kama donati, rada, na chati za eneo, ingawa inakosa usaidizi wa aina za hali ya juu zaidi kama ramani za geo au chati za mshumaa.

**Udhaifu**:
- **Aina Chache za Hali ya Juu za Chati**: Haisaidii ramani za geo, chati za mchakato wa kuunganisha, au chati za mshumaa, ambazo ni muhimu kwa mradi.
- **Mfumo Ikolojia Mdogo Zaidi**: Carbon Charts ina jamii na mfumo ikolojia mdogo zaidi ikilinganishwa na maktaba kubwa za chati kama ECharts au Highcharts.

**Hukumu**:  
Carbon Charts ni ya chanzo huria na inayoweza kubinafsishwa lakini inakosa usaidizi wa aina changamano zaidi za chati zinazohitajika kwa mradi huu. Inafaa zaidi kwa mahitaji rahisi zaidi ya chati.

---

### 7. **Layer Cake**

**Muhtasari**:  
Layer Cake ni maktaba ya taswira ya data iliyobuniwa kuunda taswira zinazobadilika, zenye tabaka.

**Nguvu**:
- **Tabaka Zinazoweza Kubinafsishwa**: Inatoa chaguo zenye nguvu za tabaka kwa taswira changamano.
- **Chanzo Huria**: Ni bure na ya chanzo huria, na kuifanya chaguo linalowezekana kwa miradi inayozingatia bajeti.

**Udhaifu**:
- **Nyaraka Chache**: Layer Cake haina nyaraka pana na usaidizi wa jamii, na kufanya iwe vigumu zaidi kufanya kazi nayo ikilinganishwa na maktaba zilizoimarika zaidi.
- **Haikujengwa kwa Chati**: Layer Cake inafaa zaidi kwa taswira zisizo za chati, kwa hivyo chaguo zake za chati zilizo tayari ni chache.

**Hukumu**:  
Ingawa inavutia kwa taswira za kipekee, Layer Cake si bora kwa mahitaji ya jadi ya chati kama chati za mshumaa au chati za rada. Inafaa zaidi kwa taswira maalum nje ya wigo wa chati za kawaida.

---

### 8. **D3.js**

**Muhtasari**:  
D3.js ni maktaba yenye nguvu ya JavaScript ya kuunda taswira zinazoendeshwa na data kupitia HTML, SVG, na CSS.

**Nguvu**:
- **Unyumbufu Usio na Kifani**: D3.js inaruhusu kuunda karibu aina yoyote ya taswira maalum, na kuifanya iwe na nguvu sana kwa chati za hali ya juu na zenye mwingiliano.
- **Vipengele Vingi**: Inasaidia aina zote za chati zinazohitajika, ikiwa ni pamoja na ramani za geo, chati za kuunganisha, na zaidi.
- **Inayoweza Kubinafsishwa**: Kiwango cha ubinafsishaji katika D3.js hakilingani, kikiruhusu waundaji kujenga taswira zilizoundwa mahsusi.

**Udhaifu**:
- **Mkondo Mkali wa Kujifunza**: D3.js ina mkondo mkali wa kujifunza na ni changamano zaidi kuunganisha ikilinganishwa na maktaba nyingine.
- **Inachukua Muda**: Kujenga chati katika D3.js kunaweza kuchukua muda, hasa kwa chati za kawaida kama chati za mshumaa au donati.

**Hukumu**:  
D3.js ina nguvu sana kwa chati za hali ya juu, zilizobinafsishwa lakini ni kubwa mno kwa visa vingi vya kawaida vya matumizi kutokana na mkondo wake mkali wa kujifunza na muda wa uundaji. Inafaa zaidi kwa hali ambapo maktaba nyingine za chati hazitoi kiwango kinachohitajika cha ubinafsishaji.

---

### Hitimisho

Baada ya kutathmini maktaba kulingana na mahitaji ya mradi, **Apache ECharts** inajitokeza kama chaguo bora zaidi. Inasaidia anuwai kamili ya chati zinazohitajika, ikiwa ni pamoja na ramani za geo, chati za mshumaa, na chati za kuunganisha. Ni ya chanzo huria, yenye vipengele vingi, na yenye mwingiliano wa hali ya juu, jambo linaloendana kikamilifu na malengo ya mradi. Ingawa **D3.js** inatoa unyumbufu mkubwa zaidi, utata wake na uwekezaji wa muda huifanya isiwe bora kwa kampuni changa inayotaka kurudia kwa haraka. **ApexCharts** na **Chart.js** ni mbadala mzuri kwa miradi rahisi zaidi lakini zinakosa usaidizi wa aina za hali ya juu za chati.