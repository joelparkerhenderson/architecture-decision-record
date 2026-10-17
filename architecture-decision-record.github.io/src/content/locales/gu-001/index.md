# આર્કિટેક્ચર નિર્ણય રેકોર્ડ (ADR)

આર્કિટેક્ચર નિર્ણય રેકોર્ડ (ADR) એ એક દસ્તાવેજ છે જે લેવાયેલા મહત્વપૂર્ણ આર્કિટેક્ચર નિર્ણયને તેના સંદર્ભ અને પરિણામો સાથે નોંધે છે.

> [!IMPORTANT]
> આ સંસાધનોને કોઈપણ નિર્ણાયક સિસ્ટમમાં વાપરતા પહેલાં તમારી પોતાની પૂરતી તપાસ કરો.

સામગ્રી:

- [આર્કિટેક્ચર નિર્ણય રેકોર્ડ શું છે?](#આર્કિટેક્ચર-નિર્ણય-રેકોર્ડ-શું-છે)
- [ADR નો ઉપયોગ શરૂ કરવાની રીત](#adr-નો-ઉપયોગ-શરૂ-કરવાની-રીત)
- [સાધનો સાથે ADR નો ઉપયોગ શરૂ કરવાની રીત](#સાધનો-સાથે-adr-નો-ઉપયોગ-શરૂ-કરવાની-રીત)
- [ગિટ સાથે ADR નો ઉપયોગ શરૂ કરવાની રીત](#ગિટ-સાથે-adr-નો-ઉપયોગ-શરૂ-કરવાની-રીત)
- [ADR માટે Claude Code સ્કિલ્સ](#adr-માટે-claude-code-સ્કિલ્સ)
- [ADR માટે ફાઇલ નામની પરંપરાઓ](#adr-માટે-ફાઇલ-નામની-પરંપરાઓ)
- [સારા ADR લખવા માટેના સૂચનો](#સારા-adr-લખવા-માટેના-સૂચનો)
- [ADR ઉદાહરણ ટેમ્પલેટ્સ](#adr-ઉદાહરણ-ટેમ્પલેટ્સ)
- [ADR માટે ટીમવર્કની સલાહ](#adr-માટે-ટીમવર્કની-સલાહ)
- [ADR માટે ટીમવર્કના પ્રશ્નો](#adr-માટે-ટીમવર્કના-પ્રશ્નો)
- [ADR માટે આગલા પગલાના ખ્યાલો](#adr-માટે-આગલા-પગલાના-ખ્યાલો)
- [આર્કિટેક્ચર આકૃતિઓ, દૃશ્યો અને દૃષ્ટિકોણ](#આર્કિટેક્ચર-આકૃતિઓ-દૃશ્યો-અને-દૃષ્ટિકોણ)
- [કોડ તરીકે નિર્ણયો માટે ફિટનેસ ફંક્શન](#કોડ-તરીકે-નિર્ણયો-માટે-ફિટનેસ-ફંક્શન)
- [પુલ રિક્વેસ્ટ માટે નિર્ણય ગાર્ડરેલ](#પુલ-રિક્વેસ્ટ-માટે-નિર્ણય-ગાર્ડરેલ)
- [વધુ માહિતી માટે](#વધુ-માહિતી-માટે)

ટેમ્પલેટ્સ:

- [Jeff Tyree અને Art Akerman નો નિર્ણય રેકોર્ડ ટેમ્પલેટ](ટેમ્પલેટ્સ/જેફ-ટાયરી-અને-આર્ટ-અકરમેનનો-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/)
- [Michael Nygard નો નિર્ણય રેકોર્ડ ટેમ્પલેટ](ટેમ્પલેટ્સ/માઇકલ-નાયગાર્ડનો-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/)
- [EdgeX નો નિર્ણય રેકોર્ડ ટેમ્પલેટ](ટેમ્પલેટ્સ/edgex-નો-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/)
- [arc42 નો નિર્ણય રેકોર્ડ ટેમ્પલેટ](ટેમ્પલેટ્સ/arc42-નો-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/)
- [એલેક્ઝાન્ડ્રિયન પેટર્ન માટે નિર્ણય રેકોર્ડ ટેમ્પલેટ](ટેમ્પલેટ્સ/એલેક્ઝાન્ડ્રિયન-પેટર્ન-માટે-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/)
- [બિઝનેસ કેસ માટે નિર્ણય રેકોર્ડ ટેમ્પલેટ](ટેમ્પલેટ્સ/બિઝનેસ-કેસ-માટે-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/)
- [MADR પ્રોજેક્ટનો નિર્ણય રેકોર્ડ ટેમ્પલેટ](ટેમ્પલેટ્સ/madr-પ્રોજેક્ટનો-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/)
- [Planguage વાપરતો નિર્ણય રેકોર્ડ ટેમ્પલેટ](ટેમ્પલેટ્સ/planguage-વાપરતો-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/)
- [Paulo Merson નો નિર્ણય રેકોર્ડ ટેમ્પલેટ](https://github.com/pmerson/ADR-template)
- [Olaf Zimmermann નો નિર્ણય રેકોર્ડ ટેમ્પલેટ](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Gareth Morgan નો નિર્ણય રેકોર્ડ ટેમ્પલેટ](ટેમ્પલેટ્સ/ગેરેથ-મોર્ગનનો-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/)
- [GIG Cymru NHS Wales નો નિર્ણય રેકોર્ડ ટેમ્પલેટ](ટેમ્પલેટ્સ/gig-cymru-nhs-wales-નો-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/)
- [Ignacio Larrañaga દ્વારા મહત્વપૂર્ણ તકનીકી નિર્ણયો (ITD) માટે નિર્ણય રેકોર્ડ ટેમ્પલેટ](ટેમ્પલેટ્સ/મહત્વપૂર્ણ-તકનીકી-નિર્ણયો-માટે-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/)

ઉદાહરણો:

- [CSS ફ્રેમવર્ક](ઉદાહરણો/css-ફ્રેમવર્ક/)
- [પર્યાવરણ ચલ રૂપરેખાંકન](ઉદાહરણો/પર્યાવરણ-ચલ-રૂપરેખાંકન/)
- [મેટ્રિક્સ, મોનિટર, ચેતવણીઓ](ઉદાહરણો/મેટ્રિક્સ-મોનિટર-ચેતવણીઓ/)
- [Microsoft Azure DevOps](ઉદાહરણો/microsoft-azure-devops/)
- [મોનોરેપો અથવા મલ્ટીરેપો](ઉદાહરણો/મોનોરેપો-અથવા-મલ્ટીરેપો/)
- [પ્રોગ્રામિંગ ભાષાઓ](ઉદાહરણો/પ્રોગ્રામિંગ-ભાષાઓ/)
- [ગુપ્ત માહિતીનો સંગ્રહ](ઉદાહરણો/ગુપ્ત-માહિતીનો-સંગ્રહ/)
- [ટાઇમસ્ટેમ્પ ફોર્મેટ](ઉદાહરણો/ટાઇમસ્ટેમ્પ-ફોર્મેટ/)
- [અને ઘણું વધુ...](ઉદાહરણો/)

## આર્કિટેક્ચર નિર્ણય રેકોર્ડ શું છે?

**આર્કિટેક્ચર નિર્ણય રેકોર્ડ** (ADR) એ એક દસ્તાવેજ છે જે લેવાયેલા મહત્વપૂર્ણ આર્કિટેક્ચરલ નિર્ણયને તેના સંદર્ભ અને પરિણામો સાથે નોંધે છે.

**આર્કિટેક્ચર નિર્ણય** (AD) એ સોફ્ટવેર ડિઝાઇનની એવી પસંદગી છે જે કોઈ મહત્વપૂર્ણ જરૂરિયાતને સંબોધે છે.

**આર્કિટેક્ચર નિર્ણય લોગ** (ADL) એ કોઈ ચોક્કસ પ્રોજેક્ટ (અથવા સંસ્થા) માટે બનાવાયેલા અને જાળવાયેલા તમામ ADR નો સંગ્રહ છે.

**આર્કિટેક્ચરની દૃષ્ટિએ મહત્વપૂર્ણ જરૂરિયાત** (ASR) એ એવી જરૂરિયાત છે જે સોફ્ટવેર સિસ્ટમના આર્કિટેક્ચર પર માપી શકાય તેવી અસર કરે છે.

આ બધું **આર્કિટેક્ચર જ્ઞાન વ્યવસ્થાપન** (AKM) ના વિષયમાં આવે છે.

આ દસ્તાવેજનો હેતુ ADR વિશે ઝડપી ઝાંખી આપવાનો છે, તે કેવી રીતે બનાવવા અને વધુ માહિતી ક્યાં જોવી.

સંક્ષિપ્ત રૂપો:

  * **AD**: આર્કિટેક્ચર નિર્ણય

  * **ADL**: આર્કિટેક્ચર નિર્ણય લોગ

  * **ADR**: આર્કિટેક્ચર નિર્ણય રેકોર્ડ

  * **AKM**: આર્કિટેક્ચર જ્ઞાન વ્યવસ્થાપન

  * **ASR**: આર્કિટેક્ચરની દૃષ્ટિએ મહત્વપૂર્ણ જરૂરિયાત

## ADR નો ઉપયોગ શરૂ કરવાની રીત

ADR નો ઉપયોગ શરૂ કરવા માટે, આ ક્ષેત્રો વિશે તમારા ટીમના સાથીદારો સાથે વાત કરો.

નિર્ણયની ઓળખ:

  * AD કેટલો તાકીદનો અને કેટલો મહત્વપૂર્ણ છે?

  * શું તે હમણાં જ લેવો પડશે, કે વધુ માહિતી મળે ત્યાં સુધી રાહ જોઈ શકાય?

  * વ્યક્તિગત અને સામૂહિક અનુભવ, તેમજ માન્ય ડિઝાઇન પદ્ધતિઓ અને પ્રથાઓ, નિર્ણયની ઓળખમાં મદદ કરી શકે છે.

  * આદર્શ રીતે ઉત્પાદનની કરવા-યોગ્ય-કામોની યાદીને પૂરક બને તેવી નિર્ણયોની કરવા-યોગ્ય-કામોની યાદી જાળવો.

નિર્ણય લેવો:

  * નિર્ણય લેવાની ઘણી તકનીકો અસ્તિત્વમાં છે, સામાન્ય અને સોફ્ટવેર આર્કિટેક્ચર માટે ચોક્કસ પણ, ઉદાહરણ તરીકે સંવાદ મેપિંગ.

  * જૂથ નિર્ણય લેવો એ સક્રિય સંશોધનનો વિષય છે.

નિર્ણયનો અમલ અને અનુપાલન:

  * AD નો ઉપયોગ સોફ્ટવેર ડિઝાઇનમાં થાય છે; તેથી તે સિસ્ટમના એવા હિતધારકોને જણાવવા અને તેમની મંજૂરી મેળવવી જરૂરી છે જેઓ તેને ભંડોળ આપે, વિકસાવે અને ચલાવે છે.

  * આર્કિટેક્ચરની દૃષ્ટિએ સ્પષ્ટ કોડિંગ શૈલીઓ અને આર્કિટેક્ચરલ ચિંતાઓ અને નિર્ણયો પર કેન્દ્રિત કોડ સમીક્ષાઓ બે સંબંધિત પ્રથાઓ છે.

  * સોફ્ટવેર ઉત્ક્રાંતિમાં સોફ્ટવેર સિસ્ટમનું આધુનિકીકરણ કરતી વખતે AD ને (ફરી) ધ્યાનમાં લેવા પણ જરૂરી છે.

નિર્ણય વહેંચણી (વૈકલ્પિક):

  * ઘણા AD પ્રોજેક્ટ્સમાં પુનરાવર્તિત થાય છે.

  * તેથી, ભૂતકાળના નિર્ણયો સાથેના અનુભવો, સારા અને ખરાબ બંને, સ્પષ્ટ જ્ઞાન વ્યવસ્થાપન વ્યૂહરચના અપનાવતી વખતે મૂલ્યવાન પુનઃઉપયોગી સંપત્તિ બની શકે છે.

નિર્ણય દસ્તાવેજીકરણ:

  * નિર્ણય નોંધવા માટે ઘણા ટેમ્પલેટ અને સાધનો અસ્તિત્વમાં છે.

  * ચપળ સમુદાયો જુઓ, ઉદાહરણ તરીકે M. Nygard ના ADR.

  * પરંપરાગત સોફ્ટવેર એન્જિનિયરિંગ અને આર્કિટેક્ચર ડિઝાઇન પ્રક્રિયાઓ જુઓ, ઉદાહરણ તરીકે IBM UMF અને CapitalOne ના Tyree અને Akerman દ્વારા સૂચવાયેલા ટેબલ લેઆઉટ.

વધુ માટે:

  * ઉપરના પગલાં વિકિપીડિયા પ્રવેશ [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision) માંથી લેવાયા છે

## સાધનો સાથે ADR નો ઉપયોગ શરૂ કરવાની રીત

- [MySpec](https://myspec.dev) — સ્વચાલિત સ્પષ્ટીકરણ અને આર્કિટેક્ચર નિર્ણય પ્લેટફોર્મ જે પ્રોજેક્ટ બંધારણ, તકનીકી આર્કિટેક્ચર અને ADR ને સ્વચ્છ Markdown માં ગોઠવે છે અને MCP દ્વારા પીરસે છે.

તમે સાધનો સાથે ADR નો ઉપયોગ તમને ગમે તે રીતે શરૂ કરી શકો છો.

ઉદાહરણ તરીકે:

  * જો તમને Google Drive અને ઓનલાઇન સંપાદન ગમતું હોય, તો તમે Google Doc અથવા Google Sheet બનાવી શકો છો.

  * જો તમને git જેવું સ્રોત કોડ સંસ્કરણ નિયંત્રણ વાપરવું ગમતું હોય, તો તમે દરેક ADR માટે એક ફાઇલ બનાવી શકો છો.

  * જો તમને Atlassian Jira જેવા પ્રોજેક્ટ આયોજન સાધનો વાપરવા ગમતા હોય, તો તમે સાધનના આયોજન ટ્રેકરનો ઉપયોગ કરી શકો છો.

  * જો તમને MediaWiki જેવી વિકિ વાપરવી ગમતી હોય, તો તમે ADR વિકિ બનાવી શકો છો.

## ગિટ સાથે ADR નો ઉપયોગ શરૂ કરવાની રીત

જો તમને git સંસ્કરણ નિયંત્રણ વાપરવું ગમતું હોય, તો સ્રોત કોડ ધરાવતા સામાન્ય સોફ્ટવેર પ્રોજેક્ટ માટે git સાથે ADR નો ઉપયોગ શરૂ કરવાની અમારી રીત અહીં છે.

ADR ફાઇલો માટે ડિરેક્ટરી બનાવો:

```sh
$ mkdir adr
```

દરેક ADR માટે, ટેક્સ્ટ ફાઇલ બનાવો, જેમ કે `choose-database.md`:

```sh
$ vi choose-database.md
```

ADR માં તમને જે જોઈએ તે લખો. વિચારો માટે આ રિપોઝિટરીમાંના ટેમ્પલેટ જુઓ.

ADR ને તમારી git રિપોઝિટરીમાં કમિટ કરો.

## ADR માટે Claude Code સ્કિલ્સ

આ રિપોઝિટરી [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) હેઠળ બે [Claude Code](https://claude.com/claude-code) સ્કિલ્સ આપે છે, જેથી AI કોડિંગ એજન્ટ આ પ્રોજેક્ટ જે રીતે ભલામણ કરે છે તે રીતે ADR લખી અને જાળવી શકે:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — સામાન્ય હેતુ માટે, કોઈપણ પ્રોજેક્ટમાં ADR લખનાર કોઈપણ માટે. તે નક્કી કરવામાં મદદ કરે છે કે નિર્ણયને ADR ની જરૂર છે કે નહીં, `adr/` કે `decisions/` ડિરેક્ટરી સેટ કરે છે, ફાઇલનું નામ આપે છે, સાથે આપેલા અગિયાર માળખામાંથી ટેમ્પલેટ પસંદ કરે છે, અને સંદર્ભ/નિર્ણય/પરિણામો વિભાગો મજબૂત રીતે લખે છે.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — ખાસ કરીને આ રિપોઝિટરીના જાળવણીકર્તાઓ માટે. તે રિપોઝિટરીનું લેઆઉટ, README/locales મિરરિંગ પરંપરા, અને નવો ટેમ્પલેટ, ઉદાહરણ કે સાધન લિંક ઉમેરવાના ચોક્કસ પગલાં દસ્તાવેજીકૃત કરે છે.

સ્કિલ વાપરવા માટે, તેનું ફોલ્ડર તમે જે રિપોઝિટરીમાં કામ કરી રહ્યા છો તેના મૂળમાં `.claude/skills/` માં (અથવા દરેક પ્રોજેક્ટમાં ઉપલબ્ધ બનાવવા `~/.claude/skills/` માં) કૉપિ કરો, પછી Claude Code ને ADR લખવા કે સમીક્ષા કરવા કહો.

## ADR માટે ફાઇલ નામની પરંપરાઓ

જો તમે તમારા ADR સામાન્ય ટેક્સ્ટ ફાઇલોમાં બનાવવાનું પસંદ કરો, તો તમે તમારી પોતાની ADR ફાઇલ નામની પરંપરા ઘડવા માગી શકો છો.

અમે ચોક્કસ સ્વરૂપ ધરાવતી ફાઇલ નામની પરંપરા વાપરવાનું પસંદ કરીએ છીએ.

ઉદાહરણો:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

અમારી ફાઇલ નામની પરંપરા:

  * નામમાં વર્તમાનકાળનું આદેશાત્મક ક્રિયાપદ-વાક્યાંશ હોય છે. આ વાંચનક્ષમતામાં મદદ કરે છે અને અમારા કમિટ સંદેશના સ્વરૂપ સાથે મેળ ખાય છે.

  * નામમાં નાના અક્ષરો અને ડેશનો ઉપયોગ થાય છે (આ રિપોઝિટરી જેમ). આ વાંચનક્ષમતા અને સિસ્ટમની ઉપયોગિતા વચ્ચેનું સંતુલન છે.

  * એક્સ્ટેન્શન markdown છે. આ સરળ ફોર્મેટિંગ માટે ઉપયોગી થઈ શકે છે.

## સારા ADR લખવા માટેના સૂચનો

સારા ADR ની લાક્ષણિકતાઓ:

* તર્ક: ચોક્કસ AD શા માટે કરવામાં આવ્યો તેનાં કારણો સમજાવો. આમાં સંદર્ભ (નીચે જુઓ), વિવિધ સંભવિત પસંદગીઓના ફાયદા અને ગેરફાયદા, સુવિધાઓની તુલના, ખર્ચ/લાભ ચર્ચાઓ અને વધુ શામેલ હોઈ શકે.

* ચોક્કસ: દરેક ADR એક AD વિશે હોવો જોઈએ, અનેક AD વિશે નહીં.

* ટાઇમસ્ટેમ્પ: ADR માં દરેક વસ્તુ ક્યારે લખાઈ તે ઓળખો. આ ખાસ કરીને સમય સાથે બદલાઈ શકે તેવા પાસાં માટે મહત્વનું છે, જેમ કે ખર્ચ, સમયપત્રક, સ્કેલિંગ અને તેવી બાબતો.

* અપરિવર્તનશીલ: ADR માં હાલની માહિતી બદલશો નહીં. તેના બદલે, નવી માહિતી ઉમેરીને ADR માં સુધારો કરો, અથવા નવો ADR બનાવીને ADR ને બદલો.

ADR ના સારા "સંદર્ભ" વિભાગની લાક્ષણિકતાઓ:

* તમારી સંસ્થાની પરિસ્થિતિ અને વ્યવસાયિક પ્રાથમિકતાઓ સમજાવો.

* તમારી ટીમોની સામાજિક અને કૌશલ્ય રચના પર આધારિત તર્ક અને વિચારણાઓ શામેલ કરો.

* સુસંગત હોય તેવા ફાયદા અને ગેરફાયદા શામેલ કરો, અને તેમને તમારી જરૂરિયાતો અને લક્ષ્યો સાથે મેળ ખાતા શબ્દોમાં વર્ણવો.

ADR ના સારા "પરિણામો" વિભાગની લાક્ષણિકતાઓ:

* નિર્ણય લેવાથી શું અનુસરે છે તે સમજાવો. આમાં અસરો, પરિણામો, ઉત્પાદનો, ફોલો-અપ અને વધુ શામેલ હોઈ શકે.

* કોઈપણ પછીના ADR વિશે માહિતી શામેલ કરો. એક ADR વધુ ADR ની જરૂરિયાત ઊભી કરે તે પ્રમાણમાં સામાન્ય છે, જેમ કે જ્યારે એક ADR મોટી સર્વવ્યાપી પસંદગી કરે અને તે બદલામાં વધુ નાના નિર્ણયોની જરૂરિયાત ઊભી કરે.

* કોઈપણ કાર્યવાહી-પછીની સમીક્ષા પ્રક્રિયાઓ શામેલ કરો. ટીમો દરેક ADR ની એક મહિના પછી સમીક્ષા કરે તે સામાન્ય છે, ADR ની માહિતીને વાસ્તવિક વ્યવહારમાં જે બન્યું તેની સાથે સરખાવવા, શીખવા અને વિકસવા માટે.

નવો ADR અગાઉના ADR નું સ્થાન લઈ શકે છે:

* જ્યારે અગાઉના ADR ને બદલતો અથવા અમાન્ય કરતો AD લેવામાં આવે, ત્યારે નવો ADR બનાવવો જોઈએ

## ADR ઉદાહરણ ટેમ્પલેટ્સ

અમે નેટ પરથી એકત્રિત કરેલા ADR ઉદાહરણ ટેમ્પલેટ્સ:

- [Michael Nygard નો ADR ટેમ્પલેટ](ટેમ્પલેટ્સ/માઇકલ-નાયગાર્ડનો-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/) (સરળ અને લોકપ્રિય)

- [Jeff Tyree અને Art Akerman નો ADR ટેમ્પલેટ](ટેમ્પલેટ્સ/જેફ-ટાયરી-અને-આર્ટ-અકરમેનનો-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/) (વધુ અત્યાધુનિક)

- [એલેક્ઝાન્ડ્રિયન પેટર્ન માટે ADR ટેમ્પલેટ](ટેમ્પલેટ્સ/એલેક્ઝાન્ડ્રિયન-પેટર્ન-માટે-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/) (સંદર્ભની વિગતો સાથે સરળ)

- [બિઝનેસ કેસ માટે ADR ટેમ્પલેટ](ટેમ્પલેટ્સ/બિઝનેસ-કેસ-માટે-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/) (વધુ MBA-લક્ષી, ખર્ચ, SWOT અને વધુ મંતવ્યો સાથે)

- [Markdown Any Decision Records (MADR) પ્રોજેક્ટનો ADR ટેમ્પલેટ](ટેમ્પલેટ્સ/madr-પ્રોજેક્ટનો-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/) (સરળ અને વિસ્તૃત બંને સંસ્કરણ; પછીનું વિકલ્પો અને તેમના ફાયદા-ગેરફાયદા પર ભાર મૂકે છે)

- [Planguage વાપરતો ADR ટેમ્પલેટ](ટેમ્પલેટ્સ/planguage-વાપરતો-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/) (વધુ ગુણવત્તા ખાતરી-લક્ષી)

- [Ignacio Larrañaga દ્વારા મહત્વપૂર્ણ તકનીકી નિર્ણયો (ITD) માટે ટેમ્પલેટ](ટેમ્પલેટ્સ/મહત્વપૂર્ણ-તકનીકી-નિર્ણયો-માટે-નિર્ણય-રેકોર્ડ-ટેમ્પલેટ/) (દુબળો અને નિર્ણય-પ્રથમ, ઝડપી કાર્યકારી સમીક્ષા માટે શ્રેષ્ઠ બનાવાયેલ)

## ADR માટે ટીમવર્કની સલાહ

જો તમે તમારી ટીમ સાથે નિર્ણય રેકોર્ડનો ઉપયોગ કરવાનું વિચારી રહ્યા હોવ, તો ઘણી ટીમો સાથે કામ કરીને અમે શીખેલી કેટલીક સલાહ અહીં છે.

તમારી પાસે "શું" ફરજિયાત બનાવવાને બદલે "શા માટે" વિશે સાથે મળીને વાત કરીને તમારા સાથીદારોને દોરવાની તક છે. ઉદાહરણ તરીકે, નિર્ણય રેકોર્ડ એ ટીમો માટે વધુ સ્માર્ટ રીતે વિચારવાનો અને વધુ સારી રીતે સંવાદ કરવાનો માર્ગ છે; જો તે માત્ર કામ થયા પછી ફરજિયાત કાગળકામની જરૂરિયાત હોય તો નિર્ણય રેકોર્ડ મૂલ્યવાન નથી.

કેટલીક ટીમો "ADR" ટૂંકાક્ષરને બદલે "નિર્ણયો" નામ વધુ પસંદ કરે છે. જ્યારે કેટલીક ટીમો "decisions" ડિરેક્ટરી નામ વાપરે છે, ત્યારે જાણે બલ્બ પ્રગટે છે, અને ટીમ ડિરેક્ટરીમાં વધુ માહિતી મૂકવા લાગે છે, જેમ કે વિક્રેતા નિર્ણયો, આયોજન નિર્ણયો, સમયપત્રક નિર્ણયો વગેરે. આ તમામ પ્રકારની માહિતી એક જ ટેમ્પલેટ વાપરી શકે છે. અમારી ધારણા છે કે લોકો ટૂંકાક્ષરો ("ADR") કરતાં શબ્દો ("નિર્ણયો") થી વધુ ઝડપથી શીખે છે, અને "રેકોર્ડ" શબ્દ હટાવવામાં આવે ત્યારે લોકો કામ-ચાલુ દસ્તાવેજો લખવા માટે વધુ પ્રેરિત થાય છે, અને કેટલાક ડેવલપર્સ અને કેટલાક મેનેજરોને "આર્કિટેક્ચર" શબ્દ ગમતો નથી.

સિદ્ધાંતમાં, અપરિવર્તનશીલતા આદર્શ છે. વ્યવહારમાં, પરિવર્તનશીલતા અમારી ટીમો માટે વધુ સારી રીતે કામ કરી છે. અમે હાલના ADR માં નવી માહિતી તારીખના સિક્કા સાથે અને આ માહિતી નિર્ણય પછી આવી એવી નોંધ સાથે ઉમેરીએ છીએ. આ પ્રકારનો અભિગમ "જીવંત દસ્તાવેજ" તરફ દોરી જાય છે જેને આપણે બધા અપડેટ કરી શકીએ. સામાન્ય અપડેટ ત્યારે થાય છે જ્યારે અમને નવા ટીમના સભ્યો, નવી ઓફર, અમારા ઉપયોગના વાસ્તવિક પરિણામો, અથવા નિર્ણય પછીના તૃતીય-પક્ષ ફેરફારો જેવા કે વિક્રેતાની ક્ષમતાઓ, કિંમત યોજનાઓ, લાઇસન્સ કરારો વગેરેને કારણે માહિતી મળે.

## ADR માટે ટીમવર્કના પ્રશ્નો

### ADR કોણ બનાવી શકે?

ચોક્કસ વ્યક્તિઓ, ચોક્કસ ભૂમિકાઓ, ચોક્કસ ટીમો અથવા ચોક્કસ વિભાગો જેવા ક્ષેત્રોનો વિચાર કરો; એ પણ વિચારો કે શું એવી વ્યક્તિઓ, ભૂમિકાઓ, ટીમો અથવા વિભાગો છે જે ADR કમિશન કરી શકે, એટલે કે તેઓ એવો ADR માગે જે બીજું કોઈ લખશે.

ઉદાહરણ જવાબ: અમારી સંસ્થાની કોઈપણ વ્યક્તિ જેણે આર્કિટેક્ચર નિર્ણય રેકોર્ડનું README પાનું વાંચ્યું હોય તે ADR નો પ્રસ્તાવ મૂકી શકે, એટલે કે તે વ્યક્તિ તેને લખવાનું શરૂ કરી શકે અને ટીમ સાથે વહેંચી શકે.

### ADR ઊભો કરવાનું શું ન્યાયી ઠેરવે છે?

તમારી સંસ્થાની ટીમોની કામ કરવાની રીતો, તમારા સોફ્ટવેર સિસ્ટમનું માળખું, ટીમો વચ્ચે સંકલન, લાંબા ગાળાની જાળવણીક્ષમતા, બાહ્ય ઇન્ટરફેસ, તમે કોને લાભ આપવા માગો છો, અને તેવી બાબતો જેવા ક્ષેત્રોનો વિચાર કરો.

ઉદાહરણ જવાબ: જ્યારે અમે ઇચ્છીએ કે ભવિષ્યના ડેવલપર્સ અમે જે કરી રહ્યા છીએ તેનું "શા માટે" સમજે, ત્યારે અમે ADR બનાવવા માગીએ છીએ.

### ADR ઊભો ન કરવાનું શું ન્યાયી ઠેરવે છે?

એવા નિર્ણયો જેવા ક્ષેત્રોનો વિચાર કરો જે આર્કિટેક્ચર વિશે ન હોય, અથવા નાના હોય જેમ કે ન્યૂનતમ જોખમવાળા કે પોતાનામાં સંપૂર્ણ કે એક ડેવલપરના, અથવા અન્યત્ર પહેલેથી સંપૂર્ણપણે આવરી લેવાયેલા હોય જેમ કે ધોરણો, નીતિઓ કે દસ્તાવેજીકરણમાં, અથવા કામચલાઉ હોય જેમ કે વૈકલ્પિક ઉપાયો, વિચારના પુરાવા અથવા પ્રયોગો.

ઉદાહરણ જવાબ: જ્યારે કોઈ નિર્ણય વ્યાપ, સમય, જોખમ અને ખર્ચમાં મર્યાદિત હોય, અથવા અન્યત્ર પહેલેથી આવરી લેવાયેલો હોય, ત્યારે અમે ADR છોડી દેવા માગીએ છીએ.

### ADR નું જીવનચક્ર શું છે?

નિર્માણ પ્રક્રિયા, સંશોધન પ્રક્રિયા, નિર્ણય પ્રક્રિયા, અમલીકરણ પ્રક્રિયા અને સમાપ્તિ પ્રક્રિયા જેવા ક્ષેત્રોનો વિચાર કરો. સમય સાથે ADR ના જીવનચક્રને કેવી રીતે ટ્રેક કરવું, જેમ કે ADR ને એક સ્થિતિમાંથી આગલી સ્થિતિમાં કેવી રીતે લઈ જવો, અને આ હિતધારકોને કેવી રીતે જણાવવું તેનો પણ વિચાર કરો.

ઉદાહરણ જવાબ: અમે ઇચ્છીએ છીએ કે ADR ના જીવનચક્રના પાંચ તબક્કા હોય: શરૂઆત → સંશોધન → મૂલ્યાંકન → અમલ → જાળવણી → સમાપ્તિ.

### ADR ના જીવનચક્ર પગલાં માટેના માપદંડ શું છે?

ADR માટે સ્વીકૃતિ માપદંડ જેવા ક્ષેત્રોનો વિચાર કરો, એટલે કે તમે કેવી રીતે જાણશો કે એક જીવનચક્ર પગલાથી બીજામાં આગળ વધવા માટે તે પૂરતું સારું છે? શું સમસ્યા સ્પષ્ટ રીતે રજૂ થઈ છે? શું વિકલ્પોની વિચારણા થઈ છે? શું સમાધાનો પૂરતી રીતે સમજાયા અને દસ્તાવેજીકૃત થયા છે?
શું બધો સંબંધિત સંદર્ભ છે? શું બધા સંબંધિત હિતધારકો સામેલ છે? શું બધો પ્રતિસાદ સમાવાયો છે?

ઉદાહરણ જવાબ: અમે ઇચ્છીએ છીએ કે ADR પર હિતધારકો મત આપે જ્યારે સક્રિય ટીમે 1) સંશોધન પૂર્ણ કર્યું હોય, 2) મૂલ્યાંકન પૂર્ણ કર્યું હોય, 3) ટિપ્પણીઓની વિનંતી અને એક અઠવાડિયાની સમય-મર્યાદા સાથે ADR પ્રસ્તાવ હિતધારકોને પ્રકાશિત કર્યો હોય, 4) બધા હિતધારકોની ટિપ્પણીઓ સમાવાઈ અને સંબોધાઈ હોય.

### કઈ ભૂમિકાઓ અને જવાબદારીઓ ADR સાથે જોડાયેલી છે?

પ્રસ્તાવક, સંશોધક, મૂલ્યાંકનકર્તા, સમીક્ષક, મંજૂરીકર્તા, જાળવણીકર્તા અને તેવી ભૂમિકાઓનો વિચાર કરો. હિતધારકો સાથે સંવાદ, અપેક્ષાઓ પૂર્ણ થાય તેની ખાતરી, વેબસાઇટ કે ઇન્ટ્રાનેટ પર વહેંચણી, અને કામની સમયાંતરે સમીક્ષા ખાસ કરીને સંબંધિત ફેરફારો થાય ત્યારે, જેવી જવાબદારીઓનો વિચાર કરો.

ઉદાહરણ જવાબ: અમે ઇચ્છીએ છીએ કે દરેક ADR ના હંમેશા એક પ્રાથમિક સંપર્ક વ્યક્તિ, એક ગૌણ સંપર્ક વ્યક્તિ અને એક જવાબદાર ટીમ હોય; આ લોકો સંવાદ, પ્રકાશન, જાળવણી, ઓછામાં ઓછા વર્ષમાં એકવાર સમયાંતરે સમીક્ષા, અને જરૂર પડ્યે અંતે સમાપ્તિ માટે જવાબદાર છે.

### શાસન ADR સાથે કેવી રીતે સંકળાયેલું છે?

તમારી સંસ્થાની કામ કરવાની રીતો, કાનૂની પાસાં કે માનવ સંસાધન પાસાં માટે કોઈ ખાસ અનુપાલન જરૂરિયાતો, તમે સર્વસંમતિ વિરુદ્ધ સંઘર્ષ વિરુદ્ધ ઉપર લઈ જવાનું કેવી રીતે સંભાળવા માગો છો, જેવા ક્ષેત્રોનો વિચાર કરો. શું એવાં ક્ષેત્રો, વ્યક્તિઓ કે ટીમો છે જે ADR અંગે અન્ય કરતાં વધુ પ્રભાવ ધરાવી શકે, જેમ કે તેને મંજૂર કરવા, તેના પર મત આપવા અથવા તેને વીટો કરવા સક્ષમ હોવું?

ઉદાહરણ જવાબ: ADR નું શાસન આ અગ્રતા ક્રમમાં છે: CEO, CTO, CLO, ADR નો અમલ કરતી ટીમ, ટીમના તે નિષ્ણાતો જે AD વિશે સૌથી વધુ જાણકાર છે. ADR માં વર્ણવેલ ન હોય ત્યાં સુધી અન્ય કોઈ પાસે શાસન નથી.

### કયા સિદ્ધાંતો ADR સાથે સંકળાયેલા છે?

તમારી સંસ્થાની કામ કરવાની રીતો જેમાં ઝડપથી ચાલવું વિરુદ્ધ ધીમે ચાલવું, નિર્ણય સર્વસંમતિ વિરુદ્ધ નિર્ણય સંઘર્ષ, જોખમ પસંદગીઓ વિરુદ્ધ સલામતી પસંદગીઓ, જાહેર ચર્ચા વિરુદ્ધ ખાનગી ચર્ચા, અને તેવી બાબતો જેવા ક્ષેત્રોનો વિચાર કરો.

ઉદાહરણ જવાબ: અમે કાર્ય તરફના ઝુકાવ, અસંમત-થઈને-પ્રતિબદ્ધ-થવું, સરળતાથી પલટાવી-શકાય-તેવા સરળતાથી અલગ-કરી-શકાય-તેવા નિર્ણયો માટે 70% અંદાજ પૂરતા છે, અને અમારી સંસ્થાના ગુપ્તતા કરારમાં વર્ણવ્યા મુજબ ગોપનીય માહિતીના અપવાદ સાથે જાહેર કામ કરવાની રીતો જેવા નેતૃત્વ સિદ્ધાંતો વાપરીએ છીએ.

## ADR માટે આગલા પગલાના ખ્યાલો

[Arc42](https://arc42.org/) બે પ્રશ્નોના વ્યવહારુ રીતે જવાબ આપે છે અને તમારી ચોક્કસ જરૂરિયાતો અનુસાર ગોઠવી શકાય છે. તમારા આર્કિટેક્ચર વિશે તમારે શું દસ્તાવેજીકૃત/સંવાદ કરવું જોઈએ? કેવી રીતે દસ્તાવેજીકૃત/સંવાદ કરવું જોઈએ? Arc42 માં આર્કિટેક્ચર નિર્ણય રેકોર્ડ ઉપરાંત લક્ષ્યો, મર્યાદાઓ, સંદર્ભો, ગુણવત્તા, જોખમો અને વધુ અંગેનું માર્ગદર્શન શામેલ છે.

[C4 મોડેલ](https://c4model.com/) સોફ્ટવેર આર્કિટેક્ચર આકૃતિ બનાવવાનો શીખવામાં સરળ, ડેવલપર-મૈત્રીપૂર્ણ અભિગમ છે. C4 એ સંદર્ભ, કન્ટેનર, ઘટકો, કોડ માટેની પદાનુક્રમિક આકૃતિઓનો સમૂહ છે, ઉપરાંત સિસ્ટમ લેન્ડસ્કેપ, ગતિશીલ અને ડિપ્લોયમેન્ટ માટે સહાયક આકૃતિઓ.

## આર્કિટેક્ચર આકૃતિઓ, દૃશ્યો અને દૃષ્ટિકોણ

આર્કિટેક્ચર આકૃતિને "આર્કિટેક્ચર દૃશ્ય" કહેવાય છે.

"આર્કિટેક્ચર દૃશ્ય" એ "આર્કિટેક્ચર દૃષ્ટિકોણ" નું ઉદાહરણ છે.

"આર્કિટેક્ચર દૃષ્ટિકોણ" ના ચોક્કસ પ્રેક્ષકો હોય છે જેમની ચોક્કસ ચિંતાઓ ધ્યાનમાં હોય છે.

આર્કિટેક્ચર દૃષ્ટિકોણના ઉદાહરણો, દૃશ્યના ઉદાહરણો અને આકૃતિના ઉદાહરણો:

- વ્યવસાયિક ક્ષમતાઓ (Business Capabilities)

- ઉચ્ચ-સ્તરીય વ્યવસાયિક પ્રક્રિયાઓ

- [મૂલ્ય પ્રવાહો (Value Streams)](https://en.wikipedia.org/wiki/Value_stream)

- એપ્લિકેશન ઘટકો સાથે મેપ કરાયેલા સોફ્ટવેર ફંક્શન્સ

- [C4 મોડેલ](https://en.wikipedia.org/wiki/C4_model) સંદર્ભ આકૃતિ (TO-BE / AS-IS)

- [C4 મોડેલ](https://en.wikipedia.org/wiki/C4_model) કન્ટેનર આકૃતિ (TO-BE / AS-IS)

- ડેટા એન્ટિટીઓને એપ્લિકેશન ઘટકો સાથે મેપ કરવા [એન્ટિટી-રિલેશનશિપ આકૃતિ](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD)

- સિસ્ટમોની અંદર અને ઇન્ટિગ્રેશન માટે કાર્યાત્મક પ્રવાહોનું વર્ણન કરવા [સિક્વન્સ આકૃતિઓ](https://en.wikipedia.org/wiki/Sequence_diagram)

- એપ્લિકેશન ઘટકોમાં ડેટા પ્રવાહોનું વર્ણન કરવા [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) આકૃતિઓ

- વ્યવસાયિક પ્રક્રિયાઓ / વપરાશકર્તા દૃશ્યોનું વર્ણન કરવા [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) આકૃતિઓ

- [ઓળખ અને ઍક્સેસ વ્યવસ્થાપન (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) આકૃતિઓ

- દરેક એપ્લિકેશન ઘટક માટે ભૂમિકાઓ સાથે [ભૂમિકા-આધારિત ઍક્સેસ નિયંત્રણ (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) આકૃતિઓ

- દરેક એપ્લિકેશન ઘટક માટે લક્ષણો સાથે [લક્ષણ-આધારિત ઍક્સેસ નિયંત્રણ (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) આકૃતિઓ

- ગોપનીયતા આકૃતિઓ

સંબંધિત આકૃતિઓ:

- ઉપયોગ કેસ આકૃતિ (Use Case Diagram) વ્યવસ્થાપન/ગ્રાહકોને ઉપયોગ કેસ બતાવે છે, જે જરૂરિયાતોની પહેલાં આવે છે, જે સોફ્ટવેર આર્કિટેક્ચરની પહેલાં આવે છે.

- ડિપ્લોયમેન્ટ આકૃતિ (Deployment Diagram) સોફ્ટવેર ઘટકો જેના પર ડિપ્લોય થાય છે તે ભૌતિક હાર્ડવેર/કમ્પ્યુટર્સ બતાવે છે.
- ડેટા ફ્લો આકૃતિ (Data Flow Diagram) બતાવે છે કે ડેટા સિસ્ટમમાંથી કેવી રીતે પસાર થાય છે અને રૂપાંતરિત થાય છે.
- સિક્વન્સ આકૃતિ (Sequence Diagram) HTTP જેવા પ્રોટોકોલ સમય અક્ષ પર કેવી રીતે કામ કરે છે તે બતાવવા માટે વપરાય છે.

- પ્રવૃત્તિ આકૃતિ (Activity Diagram) સોફ્ટવેર સિસ્ટમ જે પ્રવૃત્તિઓનો કાર્યપ્રવાહ હાથ ધરે છે તે દર્શાવે છે, જેમ કે NPC AI.

## કોડ તરીકે નિર્ણયો માટે ફિટનેસ ફંક્શન

ફિટનેસ ફંક્શન એ પ્રોગ્રામિંગ કોડથી લખાયેલ ઉદ્દેશ્ય સ્વચાલિત તપાસ છે જે ચકાસે છે કે નિર્ણયો જળવાઈ રહ્યા છે.

- ફિટનેસ ફંક્શન નિર્ણયોને પરીક્ષણક્ષમ અને ખાતરીપાત્ર બનાવે છે.

- નિર્ણયો માટેના ફિટનેસ ફંક્શન ગુણવત્તા ખાતરી, નિયમનકારી પ્રક્રિયાઓ અને શાસનના લક્ષ્યોમાં ખૂબ મદદ કરી શકે છે.

### ફિટનેસ ફંક્શન નિર્ણયો સાથે કેવી રીતે જોડાય છે

નિર્ણય રેકોર્ડ નિર્ણયનું દસ્તાવેજીકરણ કરે છે, જ્યારે ફિટનેસ ફંક્શન નિર્ણયની ખાતરી આપે છે.

- ઉદાહરણ નિર્ણય: અમે ઓડિટ જરૂરિયાતો માટે ઇવેન્ટ સોર્સિંગનો ઉપયોગ કરીએ છીએ.

- ઉદાહરણ ફિટનેસ ફંક્શન: અમે સતત ઇન્ટિગ્રેશન સર્વરનો ઉપયોગ કરીને ચકાસીએ છીએ કે બધા સ્થિતિ ફેરફારોએ ઇવેન્ટ ઉત્પન્ન કરવી જ જોઈએ.

### ફિટનેસ ફંક્શન નિર્ણયોમાં શા માટે મદદ કરે છે

ઉદ્દેશ્ય માપ: ફિટનેસ ફંક્શન પાસ અથવા ફેલ થાય છે, તેથી કામ દેખાય છે અને સ્પષ્ટ છે.

સતત ઉપયોગ: ફિટનેસ ફંક્શન તમારા જીવંત નિયમો છે, જે દરેક કમિટ અને બિલ્ડ પર ચાલે છે.

રિફેક્ટર કરવાનો વિશ્વાસ: ફિટનેસ ફંક્શન નિર્ણય નિયમોની ભૂલોને આપમેળે પકડે છે.

માપી શકાય તેવું શાસન: ફિટનેસ ફંક્શન અવરોધો ઊભા કર્યા વિના ધોરણોની ખાતરી આપે છે.

### શું ફિટનેસ ફંક્શન AI નો ઉપયોગ કરી શકે?

ફિટનેસ ફંક્શન તમારા કામ વિશે પ્રશ્નો પૂછીને નિર્ણયો માટે AI LLM નો લાભ લઈ શકે,
જેમ કે તમારી યોજનાઓ, કોડ, સ્કીમા, API અને વધુ:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### આર્કિટેક્ચર યુનિટ પરીક્ષણ

[ArchUnit](https://www.archunit.org/): કોઈપણ સાદા Java યુનિટ ટેસ્ટ ફ્રેમવર્કનો ઉપયોગ કરીને Java કોડના આર્કિટેક્ચર નિયમો તપાસો.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): Jest, Vitest, Jasmine વગેરેનો ઉપયોગ કરીને TypeScript કોડ અને JavaScript કોડના આર્કિટેક્ચર નિયમો તપાસો.

## પુલ રિક્વેસ્ટ માટે નિર્ણય ગાર્ડરેલ

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
યોગ્ય સમયે યોગ્ય નિર્ણય રેકોર્ડ આપમેળે સપાટી પર લાવે છે — જ્યારે
ડેવલપર સક્રિય રીતે તે કોડ બદલી રહ્યો હોય જે તે નિર્ણયો આવરે છે. મર્જ કરતાં પહેલાં
ડેવલપર્સ દસ્તાવેજ ફોલ્ડર વાંચશે એવી આશા રાખવાને બદલે, સંબંધિત સંદર્ભ સીધો
પુલ રિક્વેસ્ટ પર દેખાય છે.

આ દરેક પ્રકારના નિર્ણય રેકોર્ડ માટે કામ કરે છે: આર્કિટેક્ચર નિર્ણયો, ડેટા
નિર્ણયો, અનુપાલન નિર્ણયો, ક્લિનિકલ અને તબીબી નિર્ણયો, સુરક્ષા નિર્ણયો અને વધુ.

કોઈપણ CI સિસ્ટમ (GitLab, Jenkins, CircleCI) સાથે અને પ્રી-કમિટ હૂક તરીકે કામ કરે છે.
ઓપન સોર્સ. MIT લાઇસન્સ.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) એક GitHub
Action છે જે નિરીક્ષિત કોડ પાથ બદલાય અને આર્કિટેક્ચર નિર્ણય રેકોર્ડ ઉમેરાય કે અપડેટ
ન થાય ત્યારે પુલ રિક્વેસ્ટ નિષ્ફળ કરે છે. મુક્તિઓ સ્પષ્ટ છે: કારણ સાથેની
`ADR-Exempt:` લાઇન ગેટ પસાર કરાવે છે અને જોબ સારાંશમાં લખાય છે.
ટેમ્પલેટ-નિરપેક્ષ, કોઈ નિર્ભરતા નથી. ઓપન સોર્સ. MIT લાઇસન્સ.

## વધુ માહિતી માટે

પરિચય:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

ટેમ્પલેટ્સ:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

ઊંડાણપૂર્વક:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - મફત માસિક સોફ્ટવેર આર્કિટેક્ચર પાઠ

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

સાધનો:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

કંપની-વિશિષ્ટ માર્ગદર્શન:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

ઉદાહરણો:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

વિડિઓ:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

પોડકાસ્ટ:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

પુસ્તકો:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

આ પણ જુઓ:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - નિર્ણયોને સ્પષ્ટ તર્ક, ધારણાઓ, જ્ઞાનાત્મક સ્થિતિ અને સમાધાનો સાથે દર્શાવવા માટેનું વિક્રેતા-તટસ્થ, મશીન-વાંચી શકાય તેવું YAML/JSON ફોર્મેટ. નિર્ણય દસ્તાવેજીકરણમાં સંરચિત, ચકાસી શકાય તેવો તર્ક ઉમેરીને ADR ને પૂરક બને છે.
