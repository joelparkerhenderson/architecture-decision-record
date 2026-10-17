# आर्किटेक्चर निर्णय नोंद (ADR)

आर्किटेक्चर निर्णय नोंद (ADR) हा एक दस्तऐवज आहे जो घेतलेला एखादा महत्त्वाचा आर्किटेक्चरल निर्णय त्याच्या संदर्भ आणि परिणामांसह नोंदवतो.

> [!IMPORTANT]
> या संसाधनांचा कोणत्याही गंभीर प्रणालीत वापर करण्यापूर्वी तुमची स्वतःची पुरेशी तपासणी करा.

सामग्री:

- [आर्किटेक्चर निर्णय नोंद म्हणजे काय?](#आर्किटेक्चर-निर्णय-नोंद-म्हणजे-काय)
- [ADR वापरणे कसे सुरू करावे](#adr-वापरणे-कसे-सुरू-करावे)
- [साधनांसह ADR वापरणे कसे सुरू करावे](#साधनांसह-adr-वापरणे-कसे-सुरू-करावे)
- [git सह ADR वापरणे कसे सुरू करावे](#git-सह-adr-वापरणे-कसे-सुरू-करावे)
- [ADR साठी Claude Code कौशल्ये](#adr-साठी-claude-code-कौशल्ये)
- [ADR साठी फाईल नाव परंपरा](#adr-साठी-फाईल-नाव-परंपरा)
- [चांगले ADR लिहिण्यासाठी सूचना](#चांगले-adr-लिहिण्यासाठी-सूचना)
- [ADR उदाहरण साचे](#adr-उदाहरण-साचे)
- [ADR साठी सांघिक कामाचा सल्ला](#adr-साठी-सांघिक-कामाचा-सल्ला)
- [ADR साठी सांघिक कामाचे प्रश्न](#adr-साठी-सांघिक-कामाचे-प्रश्न)
- [ADR साठी पुढील पायरीच्या संकल्पना](#adr-साठी-पुढील-पायरीच्या-संकल्पना)
- [आर्किटेक्चर आकृत्या, दृश्ये आणि दृष्टिकोन](#आर्किटेक्चर-आकृत्या-दृश्ये-आणि-दृष्टिकोन)
- [कोड म्हणून निर्णयांसाठी फिटनेस फंक्शन्स](#कोड-म्हणून-निर्णयांसाठी-फिटनेस-फंक्शन्स)
- [पुल रिक्वेस्टसाठी निर्णय संरक्षक](#पुल-रिक्वेस्टसाठी-निर्णय-संरक्षक)
- [अधिक माहितीसाठी](#अधिक-माहितीसाठी)

साचे:

- [Jeff Tyree आणि Art Akerman यांचा निर्णय नोंद साचा](साचे/jeff-tyree-आणि-art-akerman-यांचा-निर्णय-नोंद-साचा/)
- [Michael Nygard यांचा निर्णय नोंद साचा](साचे/michael-nygard-यांचा-निर्णय-नोंद-साचा/)
- [EdgeX चा निर्णय नोंद साचा](साचे/edgex-चा-निर्णय-नोंद-साचा/)
- [arc42 चा निर्णय नोंद साचा](साचे/arc42-चा-निर्णय-नोंद-साचा/)
- [अलेक्झांड्रियन पॅटर्नसाठी निर्णय नोंद साचा](साचे/अलेक्झांड्रियन-पॅटर्नसाठी-निर्णय-नोंद-साचा/)
- [व्यवसाय प्रकरणासाठी निर्णय नोंद साचा](साचे/व्यवसाय-प्रकरणासाठी-निर्णय-नोंद-साचा/)
- [MADR प्रकल्पाचा निर्णय नोंद साचा](साचे/madr-प्रकल्पाचा-निर्णय-नोंद-साचा/)
- [Planguage वापरणारा निर्णय नोंद साचा](साचे/planguage-वापरणारा-निर्णय-नोंद-साचा/)
- [Paulo Merson यांचा निर्णय नोंद साचा](https://github.com/pmerson/ADR-template)
- [Olaf Zimmermann यांचा निर्णय नोंद साचा](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Gareth Morgan यांचा निर्णय नोंद साचा](साचे/gareth-morgan-यांचा-निर्णय-नोंद-साचा/)
- [GIG Cymru NHS Wales चा निर्णय नोंद साचा](साचे/gig-cymru-nhs-wales-चा-निर्णय-नोंद-साचा/)
- [Ignacio Larrañaga यांचा महत्त्वाच्या तांत्रिक निर्णयांसाठी (ITD) निर्णय नोंद साचा](साचे/महत्त्वाच्या-तांत्रिक-निर्णयांसाठी-निर्णय-नोंद-साचा/)

उदाहरणे:

- [CSS फ्रेमवर्क](उदाहरणे/css-फ्रेमवर्क/)
- [पर्यावरण चल कॉन्फिगरेशन](उदाहरणे/पर्यावरण-चल-कॉन्फिगरेशन/)
- [मेट्रिक्स, मॉनिटर, अलर्ट्स](उदाहरणे/मेट्रिक्स-मॉनिटर-अलर्ट्स/)
- [Microsoft Azure DevOps](उदाहरणे/microsoft-azure-devops/)
- [मोनोरेपो की मल्टीरेपो](उदाहरणे/मोनोरेपो-की-मल्टीरेपो/)
- [प्रोग्रामिंग भाषा](उदाहरणे/प्रोग्रामिंग-भाषा/)
- [गुपिते साठवणे](उदाहरणे/गुपिते-साठवणे/)
- [टाइमस्टॅम्प स्वरूप](उदाहरणे/टाइमस्टॅम्प-स्वरूप/)
- [आणि बरेच काही...](उदाहरणे/)

## आर्किटेक्चर निर्णय नोंद म्हणजे काय?

**आर्किटेक्चर निर्णय नोंद** (ADR) हा एक दस्तऐवज आहे जो घेतलेला एखादा महत्त्वाचा आर्किटेक्चरल निर्णय त्याच्या संदर्भ आणि परिणामांसह नोंदवतो.

**आर्किटेक्चर निर्णय** (AD) म्हणजे एखाद्या महत्त्वपूर्ण आवश्यकतेला उत्तर देणारी सॉफ्टवेअर डिझाइनमधील निवड.

**आर्किटेक्चर निर्णय नोंदवही** (ADL) म्हणजे एखाद्या विशिष्ट प्रकल्पासाठी (किंवा संस्थेसाठी) तयार केलेल्या आणि सांभाळलेल्या सर्व ADR चा संग्रह.

**आर्किटेक्चरदृष्ट्या महत्त्वाची आवश्यकता** (ASR) म्हणजे अशी आवश्यकता जिचा सॉफ्टवेअर प्रणालीच्या आर्किटेक्चरवर मोजता येण्याजोगा परिणाम होतो.

हे सर्व **आर्किटेक्चर ज्ञान व्यवस्थापन** (AKM) या विषयाच्या कक्षेत येते.

या दस्तऐवजाचे उद्दिष्ट ADR चे जलद विहंगावलोकन देणे, ते कसे तयार करायचे हे सांगणे आणि अधिक माहिती कुठे मिळेल हे दाखवणे हे आहे.

संक्षिप्त रूपे:

  * **AD**: आर्किटेक्चर निर्णय

  * **ADL**: आर्किटेक्चर निर्णय नोंदवही

  * **ADR**: आर्किटेक्चर निर्णय नोंद

  * **AKM**: आर्किटेक्चर ज्ञान व्यवस्थापन

  * **ASR**: आर्किटेक्चरदृष्ट्या महत्त्वाची आवश्यकता

## ADR वापरणे कसे सुरू करावे

ADR वापरणे सुरू करण्यासाठी, तुमच्या सहकाऱ्यांशी या क्षेत्रांबद्दल बोला.

निर्णय ओळखणे:

  * AD किती तातडीचा आणि किती महत्त्वाचा आहे?

  * तो आत्ताच घ्यावा लागेल का, की अधिक माहिती मिळेपर्यंत थांबता येईल?

  * वैयक्तिक आणि सामूहिक अनुभव, तसेच मान्यताप्राप्त डिझाइन पद्धती आणि प्रथा, निर्णय ओळखण्यात मदत करू शकतात.

  * आदर्शपणे, उत्पादनाच्या कामांच्या यादीला पूरक अशी निर्णयांची करायच्या कामांची यादी ठेवा.

निर्णय घेणे:

  * निर्णय घेण्याची अनेक तंत्रे अस्तित्वात आहेत, सर्वसाधारण तसेच सॉफ्टवेअर आर्किटेक्चरसाठी खास, उदाहरणार्थ संवाद नकाशा (dialogue mapping).

  * गटाने निर्णय घेणे हा संशोधनाचा सक्रिय विषय आहे.

निर्णयाची अंमलबजावणी आणि पालन:

  * AD सॉफ्टवेअर डिझाइनमध्ये वापरले जातात; म्हणून ते प्रणालीसाठी निधी देणाऱ्या, ती विकसित करणाऱ्या आणि चालवणाऱ्या भागधारकांना कळवले गेले पाहिजेत आणि त्यांनी ते स्वीकारले पाहिजेत.

  * आर्किटेक्चर स्पष्टपणे दिसणारी कोडिंग शैली आणि आर्किटेक्चरल चिंता व निर्णयांवर लक्ष केंद्रित करणारे कोड पुनरावलोकन या दोन संबंधित प्रथा आहेत.

  * सॉफ्टवेअर उत्क्रांतीमध्ये सॉफ्टवेअर प्रणाली आधुनिक करताना AD चा (पुन्हा) विचार करावा लागतो.

निर्णय वाटून घेणे (ऐच्छिक):

  * अनेक AD प्रकल्पांमध्ये पुन्हा पुन्हा येतात.

  * म्हणून, स्पष्ट ज्ञान व्यवस्थापन धोरण वापरताना, भूतकाळातील निर्णयांचे चांगले आणि वाईट अनुभव मौल्यवान पुनर्वापरयोग्य संपत्ती ठरू शकतात.

निर्णयाचे दस्तऐवजीकरण:

  * निर्णय नोंदवण्यासाठी अनेक साचे आणि साधने उपलब्ध आहेत.

  * चपळ (agile) समुदाय पहा, उदा. M. Nygard यांचे ADR.

  * पारंपरिक सॉफ्टवेअर अभियांत्रिकी आणि आर्किटेक्चर डिझाइन प्रक्रिया पहा, उदा. IBM UMF आणि CapitalOne चे Tyree व Akerman यांनी सुचवलेली सारणी मांडणी.

अधिक माहितीसाठी:

  * वरील पायऱ्या [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision) या Wikipedia नोंदीतून घेतल्या आहेत

## साधनांसह ADR वापरणे कसे सुरू करावे

- [MySpec](https://myspec.dev) — स्वयंचलित विनिर्देशन आणि आर्किटेक्चरल निर्णय व्यासपीठ, जे प्रकल्पाची घटना, तांत्रिक आर्किटेक्चर आणि ADR यांना MCP द्वारे दिल्या जाणाऱ्या स्वच्छ Markdown मध्ये मांडते.

तुम्ही साधनांसह ADR वापरणे तुम्हाला हवे तसे सुरू करू शकता.

उदाहरणार्थ:

  * तुम्हाला Google Drive आणि ऑनलाइन संपादन आवडत असल्यास, तुम्ही Google Doc किंवा Google Sheet तयार करू शकता.

  * तुम्हाला git सारखे स्रोत कोड आवृत्ती नियंत्रण आवडत असल्यास, तुम्ही प्रत्येक ADR साठी एक फाईल तयार करू शकता.

  * तुम्हाला Atlassian Jira सारखी प्रकल्प नियोजन साधने आवडत असल्यास, तुम्ही साधनाचा नियोजन ट्रॅकर वापरू शकता.

  * तुम्हाला MediaWiki सारखे विकी आवडत असल्यास, तुम्ही ADR विकी तयार करू शकता.

## git सह ADR वापरणे कसे सुरू करावे

तुम्हाला git आवृत्ती नियंत्रण आवडत असल्यास, स्रोत कोड असलेल्या सामान्य सॉफ्टवेअर प्रकल्पासाठी git सह ADR वापरणे आम्ही कसे सुरू करतो ते येथे आहे.

ADR फाईलींसाठी एक डिरेक्टरी तयार करा:

```sh
$ mkdir adr
```

प्रत्येक ADR साठी एक मजकूर फाईल तयार करा, उदा. `choose-database.md`:

```sh
$ vi choose-database.md
```

ADR मध्ये तुम्हाला हवे ते लिहा. कल्पनांसाठी या रिपॉझिटरीतील साचे पहा.

ADR तुमच्या git रिपॉझिटरीमध्ये कमिट करा.

## ADR साठी Claude Code कौशल्ये

ही रिपॉझिटरी [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) अंतर्गत दोन [Claude Code](https://claude.com/claude-code) कौशल्ये पुरवते, जेणेकरून AI कोडिंग एजंट हा प्रकल्प शिफारस करतो त्या पद्धतीने ADR लिहू आणि सांभाळू शकेल:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — सर्वसाधारण वापरासाठी, कोणत्याही प्रकल्पात ADR लिहिणाऱ्या कोणासाठीही. हे निर्णयाला ADR ची गरज आहे की नाही हे ठरवण्यास मदत करते, `adr/` किंवा `decisions/` डिरेक्टरी सेट करते, फाईलला नाव देते, समाविष्ट केलेल्या अकरा रचनांपैकी साचा निवडते, आणि संदर्भ/निर्णय/परिणाम हे विभाग ठामपणे लिहिते.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — विशेषतः या रिपॉझिटरीच्या देखभालकर्त्यांसाठी. हे रिपॉझिटरीची मांडणी, README/locales मिररिंग परंपरा, आणि नवीन साचा, उदाहरण किंवा साधनाचा दुवा जोडण्यासाठीच्या अचूक पायऱ्या दस्तऐवजीकृत करते.

कौशल्य वापरण्यासाठी, त्याचे फोल्डर तुम्ही ज्या रिपॉझिटरीत काम करत आहात तिच्या मुळाशी `.claude/skills/` मध्ये (किंवा प्रत्येक प्रकल्पात उपलब्ध करण्यासाठी `~/.claude/skills/` मध्ये) कॉपी करा, मग Claude Code ला ADR लिहिण्यास किंवा पुनरावलोकन करण्यास सांगा.

## ADR साठी फाईल नाव परंपरा

तुम्ही तुमचे ADR सामान्य मजकूर फाईलींमध्ये तयार करायचे ठरवल्यास, तुम्हाला ADR फाईलींसाठी स्वतःची नाव परंपरा ठरवायची असेल.

आम्ही विशिष्ट स्वरूप असलेली फाईल नाव परंपरा वापरणे पसंत करतो.

उदाहरणे:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

आमची फाईल नाव परंपरा:

  * नावात वर्तमानकाळातील आज्ञार्थी क्रियापद वाक्यांश असतो. यामुळे वाचनीयता वाढते आणि ते आमच्या कमिट संदेशाच्या स्वरूपाशी जुळते.

  * नावात लहान अक्षरे आणि डॅश वापरले जातात (या रिपॉझिटरीप्रमाणे). हा वाचनीयता आणि प्रणालीच्या उपयोगितेतील समतोल आहे.

  * विस्तार markdown आहे. सुलभ स्वरूपणासाठी हे उपयुक्त ठरू शकते.

## चांगले ADR लिहिण्यासाठी सूचना

चांगल्या ADR ची वैशिष्ट्ये:

* तर्क: विशिष्ट AD का घेतला याची कारणे सांगा. यात संदर्भ (खाली पहा), विविध संभाव्य निवडींचे फायदे-तोटे, वैशिष्ट्यांची तुलना, खर्च/लाभ चर्चा आणि बरेच काही असू शकते.

* विशिष्ट: प्रत्येक ADR एका AD बद्दल असावा, अनेक AD बद्दल नाही.

* टाइमस्टॅम्प: ADR मधील प्रत्येक बाब केव्हा लिहिली गेली ते नमूद करा. खर्च, वेळापत्रके, प्रमाण वाढवणे अशा कालांतराने बदलू शकणाऱ्या बाबींसाठी हे विशेषतः महत्त्वाचे आहे.

* अपरिवर्तनीय: ADR मधील अस्तित्वात असलेली माहिती बदलू नका. त्याऐवजी, नवीन माहिती जोडून ADR मध्ये सुधारणा करा, किंवा नवीन ADR तयार करून जुन्या ADR ची जागा घ्या.

ADR मधील चांगल्या "संदर्भ" विभागाची वैशिष्ट्ये:

* तुमच्या संस्थेची परिस्थिती आणि व्यवसायाचे प्राधान्यक्रम स्पष्ट करा.

* तुमच्या संघांची सामाजिक रचना आणि कौशल्य रचना यावर आधारित तर्क आणि विचार समाविष्ट करा.

* संबंधित फायदे-तोटे समाविष्ट करा आणि ते तुमच्या गरजा व उद्दिष्टांशी जुळणाऱ्या शब्दांत वर्णन करा.

ADR मधील चांगल्या "परिणाम" विभागाची वैशिष्ट्ये:

* निर्णय घेतल्यानंतर काय घडते ते स्पष्ट करा. यात परिणाम, निष्पत्ती, उत्पादने, पाठपुरावा आणि बरेच काही असू शकते.

* नंतरच्या कोणत्याही ADR बद्दल माहिती समाविष्ट करा. एका ADR मुळे आणखी ADR ची गरज निर्माण होणे तुलनेने सामान्य आहे, जसे की एखादा ADR मोठी सर्वसमावेशक निवड करतो आणि त्यातून आणखी लहान निर्णयांची गरज निर्माण होते.

* कृतीनंतरच्या कोणत्याही पुनरावलोकन प्रक्रिया समाविष्ट करा. प्रत्येक ADR चे एक महिन्यानंतर पुनरावलोकन करणे आणि शिकण्यासाठी व वाढण्यासाठी ADR माहितीची प्रत्यक्ष व्यवहारात काय घडले त्याच्याशी तुलना करणे संघांसाठी नेहमीचे आहे.

नवीन ADR आधीच्या ADR ची जागा घेऊ शकतो:

* जेव्हा आधीच्या ADR ची जागा घेणारा किंवा त्याला अवैध ठरवणारा AD घेतला जातो, तेव्हा नवीन ADR तयार केला पाहिजे

## ADR उदाहरण साचे

आम्ही नेटवरून गोळा केलेले ADR उदाहरण साचे:

- [Michael Nygard यांचा ADR साचा](साचे/michael-nygard-यांचा-निर्णय-नोंद-साचा/) (साधा आणि लोकप्रिय)

- [Jeff Tyree आणि Art Akerman यांचा ADR साचा](साचे/jeff-tyree-आणि-art-akerman-यांचा-निर्णय-नोंद-साचा/) (अधिक अत्याधुनिक)

- [अलेक्झांड्रियन पॅटर्नसाठी ADR साचा](साचे/अलेक्झांड्रियन-पॅटर्नसाठी-निर्णय-नोंद-साचा/) (संदर्भ तपशीलांसह साधा)

- [व्यवसाय प्रकरणासाठी ADR साचा](साचे/व्यवसाय-प्रकरणासाठी-निर्णय-नोंद-साचा/) (अधिक MBA-केंद्रित, खर्च, SWOT आणि अधिक मतांसह)

- [Markdown Any Decision Records (MADR) प्रकल्पाचा ADR साचा](साचे/madr-प्रकल्पाचा-निर्णय-नोंद-साचा/) (साधी आणि विस्तृत आवृत्ती; नंतरची पर्यायांवर आणि त्यांच्या फायद्या-तोट्यांवर भर देते)

- [Planguage वापरणारा ADR साचा](साचे/planguage-वापरणारा-निर्णय-नोंद-साचा/) (अधिक गुणवत्ता हमी-केंद्रित)

- [Ignacio Larrañaga यांचा महत्त्वाच्या तांत्रिक निर्णयांसाठी (ITD) साचा](साचे/महत्त्वाच्या-तांत्रिक-निर्णयांसाठी-निर्णय-नोंद-साचा/) (सडपातळ आणि निर्णय-प्रथम, जलद कार्यकारी पुनरावलोकनासाठी अनुकूल)

## ADR साठी सांघिक कामाचा सल्ला

तुम्ही तुमच्या संघासह निर्णय नोंदी वापरण्याचा विचार करत असाल, तर अनेक संघांसोबत काम करून आम्ही शिकलेला काही सल्ला येथे आहे.

"काय" सक्तीने लादण्याऐवजी "का" याबद्दल एकत्र बोलून तुमच्या सहकाऱ्यांचे नेतृत्व करण्याची तुम्हाला संधी आहे. उदाहरणार्थ, निर्णय नोंदी म्हणजे संघांना अधिक हुशारीने विचार करण्याचा आणि अधिक चांगला संवाद साधण्याचा मार्ग आहेत; घटना घडून गेल्यानंतर लादलेली कागदपत्रांची आवश्यकता म्हणून असतील तर निर्णय नोंदींना मोल नाही.

काही संघ "ADR" या संक्षेपापेक्षा "निर्णय" हे नाव जास्त पसंत करतात. जेव्हा काही संघ "decisions" हे डिरेक्टरी नाव वापरतात, तेव्हा जणू दिवा पेटतो आणि संघ त्या डिरेक्टरीत अधिक माहिती टाकू लागतो, जसे की विक्रेत्यांचे निर्णय, नियोजनाचे निर्णय, वेळापत्रकाचे निर्णय वगैरे. या सर्व प्रकारच्या माहितीसाठी एकच साचा वापरता येतो. आमचा अंदाज आहे की लोक संक्षेपांपेक्षा ("ADR") शब्दांतून ("निर्णय") जलद शिकतात, आणि "नोंद" हा शब्द काढल्यास लोक चालू कामाचे दस्तऐवज लिहायला अधिक प्रेरित होतात, तसेच काही विकासक आणि काही व्यवस्थापकांना "आर्किटेक्चर" हा शब्द आवडत नाही.

सैद्धांतिकदृष्ट्या, अपरिवर्तनीयता आदर्श आहे. प्रत्यक्षात, परिवर्तनीयता आमच्या संघांसाठी अधिक चांगली ठरली आहे. आम्ही विद्यमान ADR मध्ये नवी माहिती तारखेच्या शिक्क्यासह आणि ती माहिती निर्णयानंतर आली असल्याच्या नोंदीसह घालतो. या दृष्टिकोनातून एक "जिवंत दस्तऐवज" तयार होतो जो आपण सर्व जण अद्ययावत करू शकतो. नवीन सहकाऱ्यांमुळे, नवीन ऑफरमुळे, आमच्या वापराच्या प्रत्यक्ष निकालांमुळे, किंवा विक्रेत्यांच्या क्षमता, किंमत योजना, परवाना करार वगैरे निर्णयानंतरच्या तृतीय-पक्ष बदलांमुळे जेव्हा आम्हाला माहिती मिळते तेव्हा सामान्यतः अद्ययावत केले जाते.

## ADR साठी सांघिक कामाचे प्रश्न

### ADR कोण तयार करू शकतो?

विशिष्ट व्यक्ती, किंवा विशिष्ट भूमिका, किंवा विशिष्ट संघ, किंवा विशिष्ट विभाग अशा क्षेत्रांचा विचार करा; तसेच ADR चे काम सोपवू शकणाऱ्या, म्हणजे दुसरे कोणीतरी लिहील असा ADR मागवू शकणाऱ्या व्यक्ती, भूमिका, संघ किंवा विभाग आहेत का याचाही विचार करा. 

उदाहरण उत्तर: आमच्या संस्थेतील कोणतीही व्यक्ती जिने आर्किटेक्चर निर्णय नोंदीचे README पान वाचले आहे ती ADR सुचवू शकते, म्हणजे ती व्यक्ती तो लिहायला सुरुवात करू शकते आणि संघासोबत वाटून घेऊ शकते.

### ADR सुरू करण्याचे समर्थन कशाने होते?

तुमच्या संस्थेतील संघांच्या कामाच्या पद्धती, तुमच्या सॉफ्टवेअर प्रणालीची रचना, संघांमधील समन्वय, दीर्घकालीन देखभालक्षमता, बाह्य इंटरफेस, कोणाला लाभ द्यायचा आहे इत्यादी क्षेत्रांचा विचार करा. 

उदाहरण उत्तर: आम्ही जे करत आहोत त्यामागचे "का" भविष्यातील विकासकांना समजावे असे आम्हाला वाटते तेव्हा आम्ही ADR तयार करू इच्छितो.

### ADR सुरू न करण्याचे समर्थन कशाने होते?

आर्किटेक्चरबद्दल नसलेले निर्णय, किंवा अत्यल्प धोक्याचे, स्वयंपूर्ण किंवा एकट्या विकासकाचे असे लहान निर्णय, किंवा मानके, धोरणे किंवा दस्तऐवजीकरण अशा इतर ठिकाणी आधीच पूर्णपणे समाविष्ट असलेले निर्णय, किंवा तात्पुरते उपाय, संकल्पना-सिद्धता किंवा प्रयोग अशी तात्पुरती बाब यांसारख्या क्षेत्रांचा विचार करा. 

उदाहरण उत्तर: जेव्हा एखादा निर्णय व्याप्ती, वेळ, धोका आणि खर्च यांत मर्यादित असतो, किंवा इतरत्र आधीच समाविष्ट असतो, तेव्हा आम्ही ADR वगळू इच्छितो.

### ADR चे जीवनचक्र काय आहे?

निर्मिती प्रक्रिया, संशोधन प्रक्रिया, निर्णय प्रक्रिया, अंमलबजावणी प्रक्रिया आणि समाप्ती प्रक्रिया अशा क्षेत्रांचा विचार करा. ADR चे जीवनचक्र कालांतराने कसे ट्रॅक करायचे, म्हणजे ADR एका स्थितीतून पुढच्या स्थितीत कसा न्यायचा, आणि हे भागधारकांना कसे कळवायचे याचाही विचार करा. 

उदाहरण उत्तर: ADR ला पाच जीवनचक्र टप्पे असावेत असे आम्हाला वाटते: सुरुवात → संशोधन → मूल्यमापन → अंमलबजावणी → देखभाल → समाप्ती.

### ADR च्या जीवनचक्र पायऱ्यांचे निकष काय आहेत?

ADR साठी स्वीकृतीचे निकष यांसारख्या क्षेत्रांचा विचार करा, म्हणजे जीवनचक्राच्या एका पायरीवरून पुढच्या पायरीवर जाण्यासाठी तो पुरेसा चांगला आहे हे कसे कळते? समस्या स्पष्टपणे मांडली आहे का? पर्यायांचा विचार केला आहे का? तडजोडी पुरेशा समजल्या आणि नीट नोंदवल्या आहेत का?
सर्व संबंधित संदर्भ उपलब्ध आहे का? सर्व संबंधित भागधारक सहभागी आहेत का? सर्व अभिप्राय समाविष्ट केला आहे का? 

उदाहरण उत्तर: जेव्हा सक्रिय संघाने १) संशोधन पूर्ण केले, २) मूल्यमापन पूर्ण केले, ३) एक आठवड्याच्या कालमर्यादेसह टिप्पण्यांच्या विनंतीसह ADR प्रस्ताव भागधारकांना प्रकाशित केला, ४) सर्व भागधारकांच्या टिप्पण्या समाविष्ट करून हाताळल्या, तेव्हा भागधारकांनी ADR वर मतदान करावे असे आम्हाला वाटते.

### कोणत्या भूमिका आणि जबाबदाऱ्या ADR शी संबंधित आहेत?

प्रस्तावक, संशोधक, मूल्यमापक, पुनरावलोकनकर्ता, मंजुरी देणारा, देखभाल करणारा अशा भूमिकांचा विचार करा. भागधारकांशी संवाद, अपेक्षा पूर्ण होण्याची खात्री, वेबसाइट किंवा इंट्रानेटवर सामायिक करणे आणि कामाचे नियतकालिक पुनरावलोकन, विशेषतः संबंधित बदल घडतात तेव्हा, अशा जबाबदाऱ्यांचा विचार करा.

उदाहरण उत्तर: प्रत्येक ADR ला नेहमी एक प्राथमिक संपर्क व्यक्ती, एक दुय्यम संपर्क व्यक्ती आणि एक जबाबदार संघ असावा असे आम्हाला वाटते; हे संवाद, प्रकाशन, देखभाल, वर्षातून किमान एकदा नियतकालिक पुनरावलोकन आणि गरज पडल्यास अखेरीस समाप्ती यासाठी जबाबदार असतात.

### प्रशासन ADR शी कसे संबंधित आहे?

तुमच्या संस्थेच्या कामाच्या पद्धती, कायदेशीर किंवा मानव संसाधन बाबींसाठी विशेष अनुपालन गरजा, सहमती विरुद्ध संघर्ष विरुद्ध वरिष्ठांकडे नेणे हे तुम्हाला कसे हाताळायचे आहे यांसारख्या क्षेत्रांचा विचार करा. ADR बाबत इतरांपेक्षा अधिक प्रभाव असू शकणारी क्षेत्रे किंवा व्यक्ती किंवा संघ आहेत का, जसे की तो मंजूर करू शकणे, त्यावर मतदान करू शकणे किंवा त्याला नकार देऊ शकणे?

उदाहरण उत्तर: ADR चे प्रशासन या प्राधान्यक्रमात आहे: CEO, CTO, CLO, ADR ची अंमलबजावणी करणारा संघ, AD बद्दल सर्वाधिक जाणकार असलेले संघातील तज्ज्ञ. ADR मध्ये वर्णन केल्याशिवाय इतर कोणाकडे प्रशासन नसते. 

### कोणती तत्त्वे ADR शी संबंधित आहेत?

वेगाने पुढे जाणे विरुद्ध हळू पुढे जाणे, निर्णय सहमती विरुद्ध निर्णय संघर्ष, धोक्याची पसंती विरुद्ध सुरक्षिततेची पसंती, सार्वजनिक चर्चा विरुद्ध खासगी चर्चा इत्यादींचा समावेश असलेल्या तुमच्या संस्थेच्या कामाच्या पद्धती यांसारख्या क्षेत्रांचा विचार करा.

उदाहरण उत्तर: आम्ही कृतीला प्राधान्य, असहमत-पण-वचनबद्ध, सहज पलटवता येण्याजोग्या सहज वेगळ्या करता येण्याजोग्या निर्णयांसाठी ७०% अंदाज पुरेसे असणे ही नेतृत्वतत्त्वे वापरतो, आणि आमच्या संस्थेच्या गोपनीयता कराराप्रमाणे गोपनीय माहिती वगळता सार्वजनिक कामाच्या पद्धती वापरतो.

## ADR साठी पुढील पायरीच्या संकल्पना

[Arc42](https://arc42.org/) दोन प्रश्नांची व्यावहारिक उत्तरे देते आणि तुमच्या विशिष्ट गरजांनुसार जुळवून घेता येते. तुमच्या आर्किटेक्चरबद्दल तुम्ही काय दस्तऐवजीकृत/संवादित करावे? ते कसे दस्तऐवजीकृत/संवादित करावे? Arc42 मध्ये आर्किटेक्चर निर्णय नोंदीव्यतिरिक्त उद्दिष्टे, मर्यादा, संदर्भ, गुणवत्ता, धोके आणि अधिक बाबतीतले मार्गदर्शन समाविष्ट आहे.

[C4 मॉडेल](https://c4model.com/) हा सॉफ्टवेअर आर्किटेक्चर आकृत्या काढण्याचा शिकण्यास सोपा, विकासक-अनुकूल दृष्टिकोन आहे. C4 म्हणजे संदर्भ, कंटेनर, घटक, कोड यांसाठीच्या पदानुक्रमी आकृत्यांचा संच, तसेच प्रणाली परिदृश्य, गतिशील आणि डिप्लॉयमेंट यांसाठी पूरक आकृत्या.

## आर्किटेक्चर आकृत्या, दृश्ये आणि दृष्टिकोन

आर्किटेक्चर आकृतीला "आर्किटेक्चर दृश्य" म्हणतात.

"आर्किटेक्चर दृश्य" हे "आर्किटेक्चर दृष्टिकोना"चे उदाहरण आहे.

"आर्किटेक्चर दृष्टिकोना"चे विशिष्ट प्रेक्षक असतात ज्यांच्या मनात विशिष्ट चिंता असतात.

आर्किटेक्चर दृष्टिकोनांची उदाहरणे, दृश्यांची उदाहरणे आणि आकृत्यांची उदाहरणे:

- व्यवसाय क्षमता (Business Capabilities)

- उच्च-स्तरीय व्यवसाय प्रक्रिया

- [मूल्य प्रवाह (Value Streams)](https://en.wikipedia.org/wiki/Value_stream)

- अनुप्रयोग घटकांशी मॅप केलेली सॉफ्टवेअर कार्ये

- [C4 मॉडेल](https://en.wikipedia.org/wiki/C4_model) संदर्भ आकृती (TO-BE / AS-IS)

- [C4 मॉडेल](https://en.wikipedia.org/wiki/C4_model) कंटेनर आकृती (TO-BE / AS-IS)

- डेटा घटकांना अनुप्रयोग घटकांशी मॅप करण्यासाठी [एंटिटी-रिलेशनशिप आकृती](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD)

- प्रणालींच्या आत आणि एकत्रीकरणासाठी कार्यात्मक प्रवाह वर्णन करण्यासाठी [क्रम आकृत्या (Sequence diagrams)](https://en.wikipedia.org/wiki/Sequence_diagram)

- अनुप्रयोग घटकांमधील डेटा प्रवाह वर्णन करण्यासाठी [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) आकृत्या

- व्यवसाय प्रक्रिया / वापरकर्ता परिस्थिती वर्णन करण्यासाठी [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) आकृत्या

- [ओळख आणि प्रवेश व्यवस्थापन (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) आकृत्या

- प्रत्येक अनुप्रयोग घटकासाठी भूमिकांसह [भूमिका-आधारित प्रवेश नियंत्रण (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) आकृत्या

- प्रत्येक अनुप्रयोग घटकासाठी गुणधर्मांसह [गुणधर्म-आधारित प्रवेश नियंत्रण (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) आकृत्या

- गोपनीयता आकृत्या

संबंधित आकृत्या:

- वापर प्रकरण आकृती (Use Case Diagram) व्यवस्थापन/ग्राहकांना वापर प्रकरणे दाखवते, जी आवश्यकतांच्या आधी येतात, ज्या सॉफ्टवेअर आर्किटेक्चरच्या आधी येतात.

- डिप्लॉयमेंट आकृती (Deployment Diagram) सॉफ्टवेअर घटक ज्यावर डिप्लॉय केले जातात ते भौतिक हार्डवेअर/संगणक दाखवते.
- डेटा प्रवाह आकृती (Data Flow Diagram) डेटा प्रणालीमधून कसा जातो आणि कसा रूपांतरित होतो ते दाखवते.
- क्रम आकृती (Sequence Diagram) HTTP सारखे प्रोटोकॉल वेळेच्या अक्षावर कसे काम करतात हे दाखवण्यासाठी वापरली जाते.

- क्रियाकलाप आकृती (Activity Diagram) NPC AI सारख्या सॉफ्टवेअर प्रणाली करत असलेल्या क्रियाकलापांचा कार्यप्रवाह दर्शवते.

## कोड म्हणून निर्णयांसाठी फिटनेस फंक्शन्स

फिटनेस फंक्शन्स (fitness functions) म्हणजे प्रोग्रामिंग कोडने लिहिलेल्या वस्तुनिष्ठ स्वयंचलित तपासण्या, ज्या निर्णय सांभाळले जात आहेत याची पडताळणी करतात.

- फिटनेस फंक्शन्स निर्णयांना चाचणीयोग्य आणि हमी देण्याजोगे बनवतात.

- निर्णयांसाठीचे फिटनेस फंक्शन्स गुणवत्ता हमी, नियामक प्रक्रिया आणि प्रशासन उद्दिष्टांना मोठी मदत करू शकतात.

### फिटनेस फंक्शन्स निर्णयांशी कसे जोडले जातात

निर्णय नोंद निर्णयाची नोंद करते, तर फिटनेस फंक्शन निर्णयाची हमी देते.

- उदाहरण निर्णय: आम्ही लेखापरीक्षण गरजांसाठी event sourcing वापरतो.

- उदाहरण फिटनेस फंक्शन: सर्व स्थिती बदलांनी इव्हेंट तयार करणे आवश्यक आहे हे तपासण्यासाठी आम्ही सतत एकत्रीकरण सर्व्हर वापरतो.

### फिटनेस फंक्शन्स निर्णयांना का मदत करतात

वस्तुनिष्ठ मोजमापे: फिटनेस फंक्शन्स उत्तीर्ण होतात किंवा अनुत्तीर्ण होतात, त्यामुळे काम दृश्य आणि स्पष्ट असते.

सतत वापर: फिटनेस फंक्शन्स हे तुमचे जिवंत नियम आहेत, जे प्रत्येक कमिट आणि बिल्डवर चालतात.

रिफॅक्टर करण्याचा आत्मविश्वास: फिटनेस फंक्शन्स निर्णय नियमातील चुका आपोआप पकडतात.

प्रमाणक्षम प्रशासन: फिटनेस फंक्शन्स अडथळे निर्माण न करता मानकांची हमी देतात.

### फिटनेस फंक्शन्स AI वापरू शकतात का?

फिटनेस फंक्शन्स तुमच्या कामाबद्दल, जसे की तुमच्या योजना, कोड, स्कीमा, API आणि बरेच काही याबद्दल प्रश्न विचारून निर्णयांसाठी AI LLM चा लाभ घेऊ शकतात:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### आर्किटेक्चर युनिट चाचणी

[ArchUnit](https://www.archunit.org/): कोणत्याही साध्या Java युनिट चाचणी फ्रेमवर्कचा वापर करून Java कोडचे आर्किटेक्चर नियम तपासा.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): Jest, Vitest, Jasmine इत्यादींचा वापर करून TypeScript कोड आणि JavaScript कोडचे आर्किटेक्चर नियम तपासा.

## पुल रिक्वेस्टसाठी निर्णय संरक्षक

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
योग्य निर्णय नोंद योग्य क्षणी आपोआप समोर आणतो — जेव्हा
विकासक त्या निर्णयांनी व्यापलेला कोड सक्रियपणे बदलत असतो. विलीन करण्यापूर्वी विकासकांनी
दस्तऐवज फोल्डर वाचावे अशी आशा करण्याऐवजी, संबंधित संदर्भ थेट
पुल रिक्वेस्टवर दिसतो.

हे प्रत्येक प्रकारच्या निर्णय नोंदीसाठी काम करते: आर्किटेक्चर निर्णय, डेटा
निर्णय, अनुपालन निर्णय, वैद्यकीय आणि नैदानिक निर्णय, सुरक्षा निर्णय आणि बरेच काही.

कोणत्याही CI प्रणालीसह (GitLab, Jenkins, CircleCI) आणि प्री-कमिट हुक म्हणून काम करते.
ओपन सोर्स. MIT परवाना.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) हा GitHub
Action आहे जो निरीक्षित कोड पथ बदलतो आणि आर्किटेक्चर निर्णय नोंद जोडली किंवा अद्ययावत केली जात
नाही तेव्हा पुल रिक्वेस्ट अयशस्वी करतो. सूट स्पष्ट आहेत: कारणासह
`ADR-Exempt:` ओळ गेट पार करू देते आणि जॉब सारांशात नोंदवली जाते.
साचा-निरपेक्ष, शून्य अवलंबित्वे. ओपन सोर्स. MIT परवाना.

## अधिक माहितीसाठी

प्रस्तावना:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

साचे:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

सखोल:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - मोफत मासिक सॉफ्टवेअर आर्किटेक्चर धडा

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

साधने:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

कंपनी-विशिष्ट मार्गदर्शन:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

उदाहरणे:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

व्हिडिओ:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

पॉडकास्ट:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

पुस्तके:

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

हेही पहा:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - स्पष्ट तर्क, गृहीतके, संज्ञानात्मक स्थिती आणि तडजोडींसह निर्णय दर्शवण्यासाठी विक्रेता-तटस्थ, यंत्र-वाचनीय YAML/JSON स्वरूप. निर्णय दस्तऐवजीकरणात संरचित, पडताळण्याजोगा तर्क जोडून ADR ला पूरक ठरते.
