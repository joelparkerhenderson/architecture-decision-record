# आर्किटेक्चर फैसला रिकॉर्ड (ADR)

आर्किटेक्चर फैसला रिकॉर्ड (ADR) एगो अइसन दस्तावेज ह जे कवनो जरूरी आर्किटेक्चर फैसला के ओकर संदर्भ आ नतीजा संगे दर्ज करेला।

> [!IMPORTANT]
> एह संसाधन के कवनो भी नाजुक सिस्टम में इस्तेमाल करे से पहिले आपन खुद के पूरा जाँच-पड़ताल करीं।

सामग्री:

- [आर्किटेक्चर फैसला रिकॉर्ड का ह?](#आर्किटेक्चर-फैसला-रिकॉर्ड-का-ह)
- [ADR इस्तेमाल शुरू करे के तरीका](#adr-इस्तेमाल-शुरू-करे-के-तरीका)
- [औजार संगे ADR इस्तेमाल शुरू करे के तरीका](#औजार-संगे-adr-इस्तेमाल-शुरू-करे-के-तरीका)
- [गिट संगे ADR इस्तेमाल शुरू करे के तरीका](#गिट-संगे-adr-इस्तेमाल-शुरू-करे-के-तरीका)
- [ADR खातिर Claude Code स्किल](#adr-खातिर-claude-code-स्किल)
- [ADR खातिर फाइल नाम के नियम](#adr-खातिर-फाइल-नाम-के-नियम)
- [नीमन ADR लिखे खातिर सुझाव](#नीमन-adr-लिखे-खातिर-सुझाव)
- [ADR के उदाहरण टेम्पलेट](#adr-के-उदाहरण-टेम्पलेट)
- [ADR खातिर टीम के मिलजुल काम के सलाह](#adr-खातिर-टीम-के-मिलजुल-काम-के-सलाह)
- [ADR खातिर टीम के मिलजुल काम के सवाल](#adr-खातिर-टीम-के-मिलजुल-काम-के-सवाल)
- [ADR खातिर अगिला कदम के अवधारणा](#adr-खातिर-अगिला-कदम-के-अवधारणा)
- [आर्किटेक्चर आरेख, दृश्य, आ दृष्टिकोण](#आर्किटेक्चर-आरेख-दृश्य-आ-दृष्टिकोण)
- [कोड जइसन फैसला खातिर फिटनेस फंक्शन](#कोड-जइसन-फैसला-खातिर-फिटनेस-फंक्शन)
- [पुल रिक्वेस्ट खातिर फैसला के गार्डरेल](#पुल-रिक्वेस्ट-खातिर-फैसला-के-गार्डरेल)
- [आउर जानकारी खातिर](#आउर-जानकारी-खातिर)

टेम्पलेट:

- [जेफ टायरी आ आर्ट अकरमैन के फैसला रिकॉर्ड टेम्पलेट](टेम्पलेट/जेफ-टायरी-आ-आर्ट-अकरमैन-के-फैसला-रिकॉर्ड-टेम्पलेट/)
- [माइकल नाइगार्ड के फैसला रिकॉर्ड टेम्पलेट](टेम्पलेट/माइकल-नाइगार्ड-के-फैसला-रिकॉर्ड-टेम्पलेट/)
- [EdgeX के फैसला रिकॉर्ड टेम्पलेट](टेम्पलेट/edgex-के-फैसला-रिकॉर्ड-टेम्पलेट/)
- [arc42 के फैसला रिकॉर्ड टेम्पलेट](टेम्पलेट/arc42-के-फैसला-रिकॉर्ड-टेम्पलेट/)
- [अलेक्जेंड्रियन पैटर्न खातिर फैसला रिकॉर्ड टेम्पलेट](टेम्पलेट/अलेक्जेंड्रियन-पैटर्न-खातिर-फैसला-रिकॉर्ड-टेम्पलेट/)
- [कारोबारी मामला खातिर फैसला रिकॉर्ड टेम्पलेट](टेम्पलेट/कारोबारी-मामला-खातिर-फैसला-रिकॉर्ड-टेम्पलेट/)
- [MADR परियोजना के फैसला रिकॉर्ड टेम्पलेट](टेम्पलेट/madr-परियोजना-के-फैसला-रिकॉर्ड-टेम्पलेट/)
- [Planguage वाला फैसला रिकॉर्ड टेम्पलेट](टेम्पलेट/planguage-वाला-फैसला-रिकॉर्ड-टेम्पलेट/)
- [पाउलो मर्सन के फैसला रिकॉर्ड टेम्पलेट](https://github.com/pmerson/ADR-template)
- [ओलाफ जिमरमैन के फैसला रिकॉर्ड टेम्पलेट](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [गैरेथ मॉर्गन के फैसला रिकॉर्ड टेम्पलेट](टेम्पलेट/गैरेथ-मॉर्गन-के-फैसला-रिकॉर्ड-टेम्पलेट/)
- [GIG Cymru NHS Wales के फैसला रिकॉर्ड टेम्पलेट](टेम्पलेट/gig-cymru-nhs-wales-के-फैसला-रिकॉर्ड-टेम्पलेट/)
- [इग्नासियो लारानागा के जरूरी तकनीकी फैसला (ITD) खातिर फैसला रिकॉर्ड टेम्पलेट](टेम्पलेट/जरूरी-तकनीकी-फैसला-खातिर-फैसला-रिकॉर्ड-टेम्पलेट/)

उदाहरण:

- [CSS फ्रेमवर्क](उदाहरण/css-फ्रेमवर्क/)
- [एनवायरनमेंट वेरिएबल कॉन्फिगरेशन](उदाहरण/एनवायरनमेंट-वेरिएबल-कॉन्फिगरेशन/)
- [मेट्रिक, मॉनिटर, अलर्ट](उदाहरण/मेट्रिक-मॉनिटर-अलर्ट/)
- [Microsoft Azure DevOps](उदाहरण/microsoft-azure-devops/)
- [मोनोरेपो चाहे मल्टीरेपो](उदाहरण/मोनोरेपो-चाहे-मल्टीरेपो/)
- [प्रोग्रामिंग भाषा सभ](उदाहरण/प्रोग्रामिंग-भाषा-सभ/)
- [गुप्त जानकारी के भंडारन](उदाहरण/गुप्त-जानकारी-के-भंडारन/)
- [टाइमस्टैंप फॉर्मेट](उदाहरण/टाइमस्टैंप-फॉर्मेट/)
- [आउर बहुत कुछ...](उदाहरण/)

## आर्किटेक्चर फैसला रिकॉर्ड का ह?

**आर्किटेक्चर फैसला रिकॉर्ड** (ADR) एगो अइसन दस्तावेज ह जवन कवनो जरूरी आर्किटेक्चर फैसला के ओकर संदर्भ आ नतीजा के संगे दर्ज करेला।

**आर्किटेक्चर फैसला** (AD) सॉफ्टवेयर डिजाइन के एगो अइसन चुनाव ह जवन कवनो महत्त्वपूर्ण जरूरत के हल करेला।

**आर्किटेक्चर फैसला लॉग** (ADL) कवनो खास परियोजना (चाहे संगठन) खातिर बनावल आ संभालल सब ADR के संग्रह ह।

**आर्किटेक्चर के लिहाज से महत्त्वपूर्ण जरूरत** (ASR) अइसन जरूरत ह जवन सॉफ्टवेयर सिस्टम के आर्किटेक्चर पर नापे लायक असर डालेला।

ई सब **आर्किटेक्चर ज्ञान प्रबंधन** (AKM) के विषय में आवेला।

एह दस्तावेज के मकसद ह ADR के जल्दी से जानकारी देवे, ई बतावे कि ओकरा के कइसे बनावल जाला, आ आगे जानकारी कहाँ देखे के चाहीं।

संक्षिप्त रूप:

  * **AD**: आर्किटेक्चर फैसला

  * **ADL**: आर्किटेक्चर फैसला लॉग

  * **ADR**: आर्किटेक्चर फैसला रिकॉर्ड

  * **AKM**: आर्किटेक्चर ज्ञान प्रबंधन

  * **ASR**: आर्किटेक्चर के लिहाज से महत्त्वपूर्ण जरूरत

## ADR इस्तेमाल शुरू करे के तरीका

ADR इस्तेमाल शुरू करे खातिर, अपना टीम के साथी लोग से एह बात सभ पर बतकही करीं।

फैसला के पहचान:

  * AD केतना जरूरी बा आ केतना जल्दी चाहीं?

  * का ई अबहिन लेवे के पड़ी, कि कुछ आउर जानकारी मिले तक रुकल जा सकेला?

  * निजी आ सामूहिक अनुभव, आ मानल-जानल डिजाइन तरीका आ अभ्यास, फैसला के पहचान में मदद कर सकेला।

  * आदर्श रूप से, उत्पाद के करे-वाला-काम सूची के पूरक के रूप में फैसला के करे-वाला-काम सूची राखीं।

फैसला लिहल:

  * फैसला लिहे के कई गो तरीका मौजूद बा, आम तरीका भी आ सॉफ्टवेयर आर्किटेक्चर खातिर खास तरीका भी, जइसे संवाद मानचित्रण।

  * सामूहिक फैसला लिहल एगो सक्रिय शोध के विषय ह।

फैसला लागू करे आ पालन करावे के:

  * AD सॉफ्टवेयर डिजाइन में काम आवेला; एहसे ओकरा के सिस्टम के ओह हितधारक लोग तक पहुँचावे के पड़ी आ उनकर मंजूरी लेवे के पड़ी जे ओकरा खातिर पइसा लगावेला, ओकरा के बनावेला, आ चलावेला।

  * आर्किटेक्चर के हिसाब से साफ-साफ कोडिंग शैली आ आर्किटेक्चर के चिंता आ फैसला पर ध्यान देवे वाला कोड समीक्षा, दू गो जुड़ल अभ्यास हवे।

  * सॉफ्टवेयर विकास के दौरान कवनो सॉफ्टवेयर सिस्टम के आधुनिक बनावे घरी AD पर फेर से विचार करे के पड़ेला।

फैसला साझा करे के (वैकल्पिक):

  * कई गो AD कई परियोजना में बेर-बेर आवेला।

  * एहसे, पहिले के फैसला के अनुभव, नीमन आ बाउर दूनो, साफ ज्ञान प्रबंधन रणनीति अपनावे घरी कीमती आ फेर से काम आवे वाला संपत्ति हो सकेला।

फैसला के दस्तावेज बनावल:

  * फैसला दर्ज करे खातिर कई गो टेम्पलेट आ औजार मौजूद बा।

  * फुर्तीला समुदाय देखीं, जइसे M. Nygard के ADR।

  * पारंपरिक सॉफ्टवेयर इंजीनियरिंग आ आर्किटेक्चर डिजाइन प्रक्रिया देखीं, जइसे IBM UMF आ CapitalOne के Tyree आ Akerman के सुझावल तालिका ढाँचा।

आउर जानकारी खातिर:

  * ऊपर के कदम सभ विकिपीडिया के [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision) प्रविष्टि से लिहल गइल बा

## औजार संगे ADR इस्तेमाल शुरू करे के तरीका

- [MySpec](https://myspec.dev) — स्वचालित विनिर्देश आ आर्किटेक्चर फैसला के मंच, जवन परियोजना के संविधान, तकनीकी आर्किटेक्चर, आ ADR के साफ-सुथरा Markdown में सजा के MCP के जरिए उपलब्ध करावेला।

रउआ औजार संगे ADR इस्तेमाल जइसे चाहीं, ओइसे शुरू कर सकीले।

जइसे:

  * अगर रउआ Google Drive आ ऑनलाइन संपादन पसंद करीले, त Google Doc, चाहे Google Sheet बना सकीले।

  * अगर रउआ git जइसन सोर्स कोड संस्करण नियंत्रण पसंद करीले, त हर ADR खातिर एगो फाइल बना सकीले।

  * अगर रउआ Atlassian Jira जइसन परियोजना योजना औजार पसंद करीले, त औजार के योजना ट्रैकर इस्तेमाल कर सकीले।

  * अगर रउआ MediaWiki जइसन विकि पसंद करीले, त एगो ADR विकि बना सकीले।

## गिट संगे ADR इस्तेमाल शुरू करे के तरीका

अगर रउआ git संस्करण नियंत्रण पसंद करीले, त सोर्स कोड वाली आम सॉफ्टवेयर परियोजना खातिर git संगे ADR शुरू करे के हमनी के तरीका ई बा।

ADR फाइल खातिर एगो डायरेक्टरी बनाईं:

```sh
$ mkdir adr
```

हर ADR खातिर एगो टेक्स्ट फाइल बनाईं, जइसे `choose-database.md`:

```sh
$ vi choose-database.md
```

ADR में जवन चाहीं लिखीं। विचार खातिर एह रिपॉजिटरी के टेम्पलेट देखीं।

ADR के अपना git रिपॉजिटरी में कमिट करीं।

## ADR खातिर Claude Code स्किल

ई रिपॉजिटरी [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) में दू गो [Claude Code](https://claude.com/claude-code) स्किल देला, ताकि AI कोडिंग एजेंट ADR के ओइसहीं लिख आ संभाल सके जइसन ई परियोजना सिफारिश करेला:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — आम इस्तेमाल खातिर, कवनो भी परियोजना में ADR लिखे वाला हर आदमी खातिर। ई तय करे में मदद करेला कि कवनो फैसला के ADR चाहीं कि ना, `adr/` चाहे `decisions/` डायरेक्टरी सेट करेला, फाइल के नाम रखेला, शामिल ग्यारह ढाँचा में से कवनो टेम्पलेट चुनेला, आ संदर्भ/फैसला/नतीजा खंड ठीक से लिखेला।

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — खास कर एह रिपॉजिटरी के रखवाला लोग खातिर। ई रिपॉजिटरी के बनावट, README/locales के मिलान के परंपरा, आ नया टेम्पलेट, उदाहरण, चाहे औजार लिंक जोड़े के ठीक-ठीक कदम दर्ज करेला।

कवनो स्किल इस्तेमाल करे खातिर, ओकर फोल्डर के उ रिपॉजिटरी के जड़ में `.claude/skills/` में कॉपी करीं जेमें रउआ काम कर रहल बानी (चाहे हर परियोजना में उपलब्ध करावे खातिर `~/.claude/skills/` में), फेर Claude Code से ADR लिखे चाहे समीक्षा करे के कहीं।

## ADR खातिर फाइल नाम के नियम

अगर रउआ आपन ADR आम टेक्स्ट फाइल में बनावे के चुनीले, त रउआ अपना ADR फाइल नाम के आपन नियम तय करे चाहेब।

हमनी एगो खास रूप वाला फाइल नाम नियम पसंद करीले।

उदाहरण:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

हमनी के फाइल नाम नियम:

  * नाम में वर्तमान काल के आदेश वाला क्रिया-वाक्यांश होला। एह से पढ़े में आसानी होला आ ई हमनी के कमिट संदेश के रूप से मेल खाला।

  * नाम में छोट अक्षर आ डैश होला (एह रिपॉजिटरी जइसने)। ई पढ़े में आसानी आ सिस्टम के इस्तेमाल के बीच संतुलन ह।

  * एक्सटेंशन markdown होला। एह से आसान फॉर्मेटिंग में फायदा हो सकेला।

## नीमन ADR लिखे खातिर सुझाव

नीमन ADR के विशेषता:

* तर्क: खास AD काहे कइल गइल, एकर कारण समझाईं। एह में संदर्भ (नीचे देखीं), अलग-अलग संभावित चुनाव के फायदा-नुकसान, फीचर तुलना, लागत/लाभ पर बतकही, आ आउर चीज शामिल हो सकेला।

* खास: हर ADR एके गो AD के बारे में होखे के चाहीं, कई गो AD के बारे में ना।

* टाइमस्टैंप: ADR में हर चीज कब लिखल गइल, ई बताईं। ई खास कर के ओह बात खातिर जरूरी बा जे समय के संगे बदल सकेला, जइसे लागत, समय-सारणी, पैमाना बढ़ावल, आ अइसने।

* अपरिवर्तनीय: ADR में मौजूद जानकारी मत बदलीं। एकरा बदले, नया जानकारी जोड़ के ADR में संशोधन करीं, चाहे नया ADR बना के पुरान ADR के जगह ले लीं।

ADR के नीमन "संदर्भ" खंड के विशेषता:

* अपना संगठन के हालात आ कारोबारी प्राथमिकता समझाईं।

* अपना टीम के सामाजिक आ कौशल बनावट पर आधारित तर्क आ विचार शामिल करीं।

* जवन फायदा-नुकसान प्रासंगिक बा ओकरा के शामिल करीं, आ ओकरा के अपना जरूरत आ लक्ष्य से मेल खाए वाला शब्द में बताईं।

ADR के नीमन "नतीजा" खंड के विशेषता:

* समझाईं कि फैसला लिहला से का-का होई। एह में असर, नतीजा, उत्पाद, आगे के काम, आ आउर चीज शामिल हो सकेला।

* कवनो बाद वाला ADR के जानकारी शामिल करीं। एगो ADR से आउर ADR के जरूरत पड़ल अपेक्षाकृत आम बात ह, जइसे जब कवनो ADR एगो बड़ आ सब पर लागू चुनाव करेला, जवन आगे चल के आउर छोट फैसला के जरूरत बनावेला।

* कवनो कार्रवाई-के-बाद के समीक्षा प्रक्रिया शामिल करीं। टीम खातिर हर ADR के एक महीना बाद समीक्षा कइल आम बात ह, ताकि ADR के जानकारी के असल अभ्यास में जवन भइल ओकरा से मिलावल जा सके, आ सीखल आ आगे बढ़ल जा सके।

नया ADR पहिले वाला ADR के जगह ले सकेला:

* जब कवनो AD अइसन लिहल जाला जे पहिले वाला ADR के बदल देला चाहे बेकार कर देला, त नया ADR बनावे के चाहीं

## ADR के उदाहरण टेम्पलेट

ADR के उदाहरण टेम्पलेट जे हमनी नेट से जुटवले बानी:

- [माइकल नाइगार्ड के ADR टेम्पलेट](टेम्पलेट/माइकल-नाइगार्ड-के-फैसला-रिकॉर्ड-टेम्पलेट/) (सादा आ लोकप्रिय)

- [जेफ टायरी आ आर्ट अकरमैन के ADR टेम्पलेट](टेम्पलेट/जेफ-टायरी-आ-आर्ट-अकरमैन-के-फैसला-रिकॉर्ड-टेम्पलेट/) (जादा परिष्कृत)

- [अलेक्जेंड्रियन पैटर्न खातिर ADR टेम्पलेट](टेम्पलेट/अलेक्जेंड्रियन-पैटर्न-खातिर-फैसला-रिकॉर्ड-टेम्पलेट/) (संदर्भ के ब्योरा संगे सादा)

- [कारोबारी मामला खातिर ADR टेम्पलेट](टेम्पलेट/कारोबारी-मामला-खातिर-फैसला-रिकॉर्ड-टेम्पलेट/) (जादा MBA-उन्मुख, लागत, SWOT, आ आउर राय संगे)

- [Markdown Any Decision Records (MADR) परियोजना के ADR टेम्पलेट](टेम्पलेट/madr-परियोजना-के-फैसला-रिकॉर्ड-टेम्पलेट/) (सादा आ विस्तृत दूनो संस्करण; बाद वाला विकल्प आ उनके फायदा-नुकसान पर जोर देला)

- [Planguage वाला ADR टेम्पलेट](टेम्पलेट/planguage-वाला-फैसला-रिकॉर्ड-टेम्पलेट/) (जादा गुणवत्ता आश्वासन-उन्मुख)

- [इग्नासियो लारानागा के जरूरी तकनीकी फैसला (ITD) खातिर टेम्पलेट](टेम्पलेट/जरूरी-तकनीकी-फैसला-खातिर-फैसला-रिकॉर्ड-टेम्पलेट/) (दुबला आ फैसला-पहिले, तेज कार्यकारी समीक्षा खातिर बेहतर बनावल)

## ADR खातिर टीम के मिलजुल काम के सलाह

अगर रउआ अपना टीम संगे फैसला रिकॉर्ड इस्तेमाल करे के सोचत बानी, त हमनी के बहुत टीम संगे काम कके सीखल कुछ सलाह ई बा।

रउआ लग अपना साथी लोग के अगुवाई करे के मौका बा, "का" थोपे के बजाय "काहे" पर मिलजुल के बतकही कके। जइसे, फैसला रिकॉर्ड टीम खातिर समझदारी से सोचे आ नीमन तरी से बतियावे के एगो तरीका ह; अगर ई बस काम के बाद जबरदस्ती के कागजी जरूरत होखे, त फैसला रिकॉर्ड के कवनो कीमत नइखे।

कुछ टीम "ADR" संक्षिप्त रूप के बजाय "फैसला" नाम बहुत पसंद करेले। जब कुछ टीम डायरेक्टरी के नाम "decisions" राखेले, त जइसे बत्ती जल जाला, आ टीम ओह डायरेक्टरी में आउर जानकारी डाले लागेले, जइसे विक्रेता के फैसला, योजना के फैसला, समय-सारणी के फैसला, वगैरह। एह सब तरह के जानकारी एके टेम्पलेट इस्तेमाल कर सकेला। हमनी के अंदाजा बा कि लोग संक्षिप्त रूप ("ADR") के बजाय शब्द ("फैसला") से जल्दी सीखेला, आ "रिकॉर्ड" शब्द हटला पर लोग काम-चालू दस्तावेज लिखे खातिर जादा प्रेरित होखेला, आ कुछ डेवलपर आ कुछ प्रबंधक "आर्किटेक्चर" शब्द ना पसंद करेले।

सिद्धांत में, अपरिवर्तनीयता आदर्श ह। अभ्यास में, हमनी के टीम खातिर परिवर्तनीयता बेहतर काम कइलस। हमनी मौजूदा ADR में नया जानकारी डालीले, तारीख के छाप संगे, आ एगो टिप्पणी कि ई जानकारी फैसला के बाद आइल। एह तरह के तरीका से एगो "जियत दस्तावेज" बनेला जवन हमनी सभे अपडेट कर सकीले। आम अपडेट तब होला जब हमनी के नया साथी, नया पेशकश, हमनी के इस्तेमाल के असल नतीजा, चाहे फैसला के बाद तीसरा पक्ष के बदलाव जइसे विक्रेता के क्षमता, कीमत योजना, लाइसेंस समझौता, वगैरह के चलते जानकारी मिलेला।

## ADR खातिर टीम के मिलजुल काम के सवाल

### ADR के बना सकेला?

खास लोग, खास भूमिका, खास टीम, चाहे खास विभाग जइसन बात पर विचार करीं; इहो सोचीं कि का कुछ लोग, भूमिका, टीम, चाहे विभाग अइसन बा जे ADR कमीशन कर सकेला, यानी ADR के मांग कर सकेला जेकरा के कवनो आउर आदमी लिखी।

उदाहरण जवाब: हमनी के संगठन के कवनो भी आदमी जे आर्किटेक्चर फैसला रिकॉर्ड के README पन्ना पढ़ले बा, ऊ ADR के प्रस्ताव दे सकेला, यानी ऊ ओकरा के लिखल शुरू कर सकेला, आ टीम संगे साझा कर सकेला।

### ADR उठावे के का सही ठहरावेला?

अपना संगठन के टीम के काम करे के तरीका, अपना सॉफ्टवेयर सिस्टम के बनावट, टीम-टीम के बीच तालमेल, लमहर समय तक संभाल सके के क्षमता, बाहरी इंटरफेस, रउआ केकरा फायदा पहुँचावल चाहत बानी, आ अइसने बात पर विचार करीं।

उदाहरण जवाब: जब हमनी चाहत बानी कि आगे के डेवलपर लोग समझे कि हमनी जवन करत बानी ओकर "काहे" का ह, तब हमनी ADR बनावल चाहेनी।

### ADR ना उठावे के का सही ठहरावेला?

अइसन फैसला पर विचार करीं जे आर्किटेक्चर के बारे में नइखे, चाहे बहुते छोट बा जइसे कम जोखिम वाला चाहे अपना में पूरा चाहे एके डेवलपर वाला, चाहे पहिलहीं कहीं आउर पूरा तरी से कवर हो चुकल बा जइसे मानक चाहे नीति चाहे दस्तावेज में, चाहे अस्थायी बा जइसे जुगाड़ चाहे सिद्धांत के सबूत चाहे प्रयोग।

उदाहरण जवाब: जब कवनो फैसला दायरा आ समय आ जोखिम आ लागत में सीमित बा, चाहे पहिलहीं कहीं आउर कवर हो चुकल बा, त हमनी ADR छोड़ल चाहेनी।

### ADR के जीवनचक्र का ह?

निर्माण प्रक्रिया, शोध प्रक्रिया, फैसला प्रक्रिया, लागू करे के प्रक्रिया, आ समाप्ति प्रक्रिया जइसन बात पर विचार करीं। इहो सोचीं कि ADR के जीवनचक्र के समय के संगे कइसे ट्रैक कइल जाई, जइसे ADR के एक स्थिति से दोसरा स्थिति में कइसे ले जाइल जाई, आ ई बात हितधारक लोग के कइसे बतावल जाई।

उदाहरण जवाब: हमनी चाहेनी कि ADR के जीवनचक्र के पाँच चरण होखे: शुरुआत → शोध → मूल्यांकन → लागू करे → संभाल → समाप्ति।

### ADR के जीवनचक्र के कदम खातिर कसौटी का बा?

ADR खातिर स्वीकृति कसौटी जइसन बात पर विचार करीं, यानी रउआ कइसे जानेब कि ऊ एक जीवनचक्र कदम से अगिला कदम में बढ़े खातिर काफी नीमन बा? का समस्या साफ-साफ बतावल गइल बा? का विकल्प पर विचार कइल गइल बा? का समझौता सभ के ठीक से समझल आ दर्ज कइल गइल बा?
का सब प्रासंगिक संदर्भ मौजूद बा? का सब प्रासंगिक हितधारक शामिल बा? का सब प्रतिक्रिया शामिल कर लिहल गइल बा?

उदाहरण जवाब: हमनी चाहेनी कि ADR पर हितधारक लोग मतदान करे जब सक्रिय टीम 1) आपन शोध पूरा कर लेले होखे, 2) आपन मूल्यांकन पूरा कर लेले होखे, 3) ADR प्रस्ताव के टिप्पणी के निहोरा आ एक हफ्ता के समय-सीमा संगे हितधारक लोग के बीच प्रकाशित कर देले होखे, 4) सब हितधारक के टिप्पणी शामिल आ संबोधित कर लिहल गइल होखे।

### ADR संगे कवन भूमिका आ जिम्मेदारी जुड़ल बा?

प्रस्तावक, शोधकर्ता, मूल्यांकनकर्ता, समीक्षक, मंजूरीकर्ता, संभालनिहार, आ अइसने भूमिका पर विचार करीं। हितधारक लोग संगे संवाद, अपेक्षा पूरा होखे के पक्का करे, वेबसाइट चाहे इंट्रानेट पर साझा करे, आ समय-समय पर खास कर के प्रासंगिक बदलाव होखे पर काम के समीक्षा करे जइसन जिम्मेदारी पर विचार करीं।

उदाहरण जवाब: हमनी चाहेनी कि हर ADR के हमेशा एगो मुख्य संपर्क आदमी, एगो दोसर संपर्क आदमी, आ एगो जवाबदेह टीम होखे; ई लोग संवाद, प्रकाशन, संभाल, साल में कम से कम एक बेर समय-समय पर समीक्षा, आ जरूरत पड़ला पर आखिर में समाप्ति खातिर जिम्मेदार हवे।

### शासन के ADR संगे कइसे नाता बा?

अपना संगठन के काम करे के तरीका, कवनो खास अनुपालन जरूरत जइसे कानूनी पक्ष चाहे मानव संसाधन पक्ष, आ सहमति बनाम टकराव बनाम ऊपर भेजे के मामला के रउआ कइसे संभालल चाहत बानी, जइसन बात पर विचार करीं। का कुछ क्षेत्र चाहे लोग चाहे टीम अइसन बा जे ADR के बारे में आउर के मुकाबले जादा असर रख सकेला, जइसे ओकरा के मंजूर करे, चाहे ओकरा पर मतदान करे, चाहे ओकरा के रोके के काबिल होखे?

उदाहरण जवाब: ADR के शासन एह प्राथमिकता क्रम में बा: CEO, CTO, CLO, ADR लागू करे वाली टीम, टीम के ऊ विशेषज्ञ लोग जे AD के बारे में सबसे जादा जानकार हवे। जबले ADR में बतावल ना होखे, कवनो आउर के शासन के अधिकार नइखे।

### ADR संगे कवन सिद्धांत जुड़ल बा?

अपना संगठन के काम करे के तरीका जइसन बात पर विचार करीं जवना में तेजी से चले बनाम धीरे चले, फैसला पर सहमति बनाम फैसला पर टकराव, जोखिम के पसंद बनाम सुरक्षा के पसंद, सार्वजनिक बतकही बनाम निजी बतकही, आ अइसने बात शामिल बा।

उदाहरण जवाब: हमनी कार्रवाई के झुकाव, असहमत-होके-भी-मानल, आसानी से पलटे-लायक आसानी से अलग-करे-लायक फैसला खातिर 70% अनुमान काफी बा, आ सार्वजनिक काम करे के तरीका (गोपनीय जानकारी के छोड़ के जइसन हमनी के संगठन के गोपनीयता समझौता में बतावल बा) के नेतृत्व सिद्धांत इस्तेमाल करेनी।

## ADR खातिर अगिला कदम के अवधारणा

[Arc42](https://arc42.org/) दू सवाल के व्यावहारिक तरी से जवाब देला आ रउआ के खास जरूरत के हिसाब से ढालल जा सकेला। रउआ के अपना आर्किटेक्चर के बारे में का दर्ज/संवाद करे के चाहीं? कइसे दर्ज/संवाद करे के चाहीं? Arc42 में आर्किटेक्चर फैसला रिकॉर्ड के साथे लक्ष्य, बंदिश, संदर्भ, गुणवत्ता, जोखिम, आ आउर के बारे में मार्गदर्शन शामिल बा।

[C4 मॉडल](https://c4model.com/) सॉफ्टवेयर आर्किटेक्चर के आरेख बनावे के सीखे में आसान, डेवलपर-अनुकूल तरीका ह। C4 संदर्भ, कंटेनर, घटक, कोड खातिर पदानुक्रमित आरेख के सेट ह, संगे सिस्टम परिदृश्य, गतिशील, आ डिप्लॉयमेंट खातिर सहायक आरेख।

## आर्किटेक्चर आरेख, दृश्य, आ दृष्टिकोण

आर्किटेक्चर आरेख के "आर्किटेक्चर दृश्य" कहल जाला।

"आर्किटेक्चर दृश्य" एगो "आर्किटेक्चर दृष्टिकोण" के उदाहरण ह।

"आर्किटेक्चर दृष्टिकोण" के एगो खास दर्शक होला जेकर खास चिंता मन में रहेला।

आर्किटेक्चर दृष्टिकोण के उदाहरण, दृश्य के उदाहरण, आ आरेख के उदाहरण:

- कारोबारी क्षमता (Business Capabilities)

- उच्च-स्तर के कारोबारी प्रक्रिया

- [मूल्य धारा (Value Streams)](https://en.wikipedia.org/wiki/Value_stream)

- एप्लिकेशन घटक पर मैप कइल सॉफ्टवेयर फंक्शन

- [C4 मॉडल](https://en.wikipedia.org/wiki/C4_model) संदर्भ आरेख (TO-BE / AS-IS)

- [C4 मॉडल](https://en.wikipedia.org/wiki/C4_model) कंटेनर आरेख (TO-BE / AS-IS)

- डेटा इकाई के एप्लिकेशन घटक पर मैप करे खातिर [इकाई-संबंध आरेख (Entity-relationship Diagram)](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD)

- सिस्टम के भीतर आ इंटीग्रेशन खातिर कार्यात्मक प्रवाह के बतावे खातिर [क्रम आरेख (Sequence Diagrams)](https://en.wikipedia.org/wiki/Sequence_diagram)

- एप्लिकेशन घटक में डेटा प्रवाह के बतावे खातिर [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) आरेख

- कारोबारी प्रक्रिया / उपयोगकर्ता परिदृश्य के बतावे खातिर [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) आरेख

- [पहचान आ पहुँच प्रबंधन (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) आरेख

- हर एप्लिकेशन घटक खातिर भूमिका संगे [भूमिका-आधारित पहुँच नियंत्रण (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) आरेख

- हर एप्लिकेशन घटक खातिर गुण संगे [गुण-आधारित पहुँच नियंत्रण (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) आरेख

- गोपनीयता आरेख

संबंधित आरेख:

- उपयोग-मामला आरेख (Use Case Diagram) प्रबंधन/ग्राहक के उपयोग के मामला देखावेला, जे जरूरत से पहिले आवेला, जे सॉफ्टवेयर आर्किटेक्चर से पहिले आवेला।

- डिप्लॉयमेंट आरेख (Deployment Diagram) ऊ भौतिक हार्डवेयर/कंप्यूटर देखावेला जेपर सॉफ्टवेयर घटक डिप्लॉय कइल जाला।
- डेटा प्रवाह आरेख (Data Flow Diagram) देखावेला कि डेटा सिस्टम से कइसे गुजरेला आ बदलेला।
- क्रम आरेख (Sequence Diagram) ई देखावे खातिर इस्तेमाल होला कि HTTP जइसन प्रोटोकॉल समय अक्ष पर कइसे काम करेला।

- गतिविधि आरेख (Activity Diagram) ऊ गतिविधि के कार्यप्रवाह देखावेला जे सॉफ्टवेयर सिस्टम चलावेला, जइसे NPC AI।

## कोड जइसन फैसला खातिर फिटनेस फंक्शन

फिटनेस फंक्शन प्रोग्रामिंग कोड से लिखल वस्तुनिष्ठ स्वचालित जाँच हवे, जे पक्का करेला कि फैसला सभ बनल रहल बा।

- फिटनेस फंक्शन फैसला सभ के जाँचे-लायक आ भरोसा-दियावे-लायक बनावेला।

- फैसला खातिर फिटनेस फंक्शन गुणवत्ता आश्वासन, नियामक प्रक्रिया, आ शासन के लक्ष्य में बहुत मदद कर सकेला।

### फिटनेस फंक्शन फैसला से कइसे जुड़ेला

फैसला रिकॉर्ड फैसला के दर्ज करेला, जबकि फिटनेस फंक्शन फैसला के पक्का करेला।

- उदाहरण फैसला: हमनी ऑडिट जरूरत खातिर इवेंट सोर्सिंग इस्तेमाल करेनी।

- उदाहरण फिटनेस फंक्शन: हमनी निरंतर इंटीग्रेशन सर्वर से जाँचेनी कि सब स्थिति बदलाव से इवेंट पैदा होखे के चाहीं।

### फिटनेस फंक्शन फैसला के कइसे मदद करेला

वस्तुनिष्ठ माप: फिटनेस फंक्शन पास चाहे फेल होखेला, एहसे काम साफ आ देखे-लायक रहेला।

लगातार इस्तेमाल: फिटनेस फंक्शन रउआ के जियत नियम हवे, जे हर कमिट आ बिल्ड पर चलेला।

रिफैक्टर करे के भरोसा: फिटनेस फंक्शन फैसला के नियम के गलती अपने आप पकड़ लेला।

पैमाना बढ़ावे-लायक शासन: फिटनेस फंक्शन बिना रुकावट बनवले मानक के भरोसा देला।

### का फिटनेस फंक्शन AI इस्तेमाल कर सकेला?

फिटनेस फंक्शन फैसला खातिर AI LLM के फायदा उठा सकेला, रउआ के काम, जइसे योजना, कोड, स्कीमा, API, आ आउर, के बारे में सवाल पूछ के:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### आर्किटेक्चर यूनिट टेस्टिंग

[ArchUnit](https://www.archunit.org/): कवनो सादा Java यूनिट टेस्ट फ्रेमवर्क इस्तेमाल कके Java कोड के आर्किटेक्चर नियम जाँचीं।

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): Jest, Vitest, Jasmine, वगैरह इस्तेमाल कके TypeScript कोड आ JavaScript कोड के आर्किटेक्चर नियम जाँचीं।

## पुल रिक्वेस्ट खातिर फैसला के गार्डरेल

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
सही फैसला रिकॉर्ड के सही समय पर अपने आप सामने ले आवेला — जब
कवनो डेवलपर सक्रिय रूप से ऊ कोड बदल रहल बा जेकरा के ऊ फैसला कवर करेला। डेवलपर मर्ज करे से
पहिले दस्तावेज के फोल्डर पढ़िहें, एह उम्मीद में रहे के बजाय, संबंधित संदर्भ सीधा पुल रिक्वेस्ट पर
देखाई देला।

ई हर तरह के फैसला रिकॉर्ड खातिर काम करेला: आर्किटेक्चर फैसला, डेटा
फैसला, अनुपालन फैसला, नैदानिक आ चिकित्सा फैसला, सुरक्षा फैसला, आ आउर।

कवनो भी CI प्रणाली (GitLab, Jenkins, CircleCI) संगे आ प्री-कमिट हुक के रूप में काम करेला।
ओपन सोर्स। MIT लाइसेंस।

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) एगो GitHub
Action ह जे पुल रिक्वेस्ट के फेल कर देला जब निगरानी वाला कोड रास्ता बदलेला आ
आर्किटेक्चर फैसला रिकॉर्ड जोड़ल चाहे अपडेट ना कइल जाला। छूट साफ बा: कारन संगे
`ADR-Exempt:` लाइन गेट पार करा देला आ जॉब सारांश में लिखल जाला।
टेम्पलेट-निरपेक्ष, कवनो निर्भरता नइखे। ओपन सोर्स। MIT लाइसेंस।

## आउर जानकारी खातिर

परिचय:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

टेम्पलेट:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

गहराई से:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - मुफ्त मासिक सॉफ्टवेयर आर्किटेक्चर पाठ

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

औजार:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

कंपनी-विशेष मार्गदर्शन:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

उदाहरण:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

वीडियो:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

पॉडकास्ट:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

किताब:

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

इहो देखीं:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - फैसला के साफ तर्क, मान्यता, संज्ञानात्मक स्थिति, आ समझौता संगे दर्शावे खातिर विक्रेता-निरपेक्ष, मशीन-पठनीय YAML/JSON फॉर्मेट। ई फैसला के दस्तावेज में संरचित, सत्यापन-योग्य तर्क जोड़ के ADR के पूरक बनेला।
