# Microsoft Azure DevOps

Efnisyfirlit:

* [Samantekt](#samantekt)
  * [Vandamál](#vandamál)
  * [Ákvörðun](#ákvörðun)
  * [Staða](#staða)
* [Nánar](#nánar)
  * [Forsendur](#forsendur)
  * [Takmarkanir](#takmarkanir)
  * [Afstöður](#afstöður)
  * [Röksemd](#röksemd)
  * [Afleiðingar](#afleiðingar)
* [Tengt](#tengt)
  * [Tengdar ákvarðanir](#tengdar-ákvarðanir)
  * [Tengdar kröfur](#tengdar-kröfur)
  * [Tengdar afurðir](#tengdar-afurðir)
  * [Tengdar meginreglur](#tengdar-meginreglur)
* [Athugasemdir](#athugasemdir)
  * [Microsoft Devops CI: An Unsatisfying Adventure](#microsoft-devops-ci-an-unsatisfying-adventure)
  * [Helstu atriði úr umræðu á Hacker News](#helstu-atriði-úr-umræðu-á-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Samantekt Edward Thomson (Azure PM)](#samantekt-edward-thomson-azure-pm)


## Samantekt


### Vandamál

Við viljum nota devops til að smíða, samþætta, setja upp og hýsa verkefni okkar. Við erum að íhuga Microsoft Azure DevOps.

  * Við viljum að upplifun þróunaraðila sé hröð og áreiðanleg, bæði við uppsetningu devops, t.d. stillingar, og viðvarandi notkun, t.d. hraðan smíðatíma.
  
  * Við viljum íhuga að nota Microsoft Azure í heild, til að hýsa forrit verkefnisins, gagnagrunna o.s.frv.


### Ákvörðun

Ákveðið var að nota ekki Microsoft Azure DevOps.


### Staða

Ákveðið. Opið fyrir endurskoðun ef/þegar mikilvægar nýjar upplýsingar berast.


## Nánar


### Forsendur

Allar hefðbundnar devops-forsendur, eins og í bókinni Accelerate.

  * Hraðar smíðar eru umtalsverð hjálp. Þær flýta endurgjafarlykkjum.

  * Við getum skipt hlutum inn/út frá öðrum söluaðilum, þ.e. við gætum viljað koma með eigin hraðvirkari smíðaþjóna, eða nota okkar eigið val á útgáfustýringarkerfi, eða samhæfa við samfellda samþættingarþjóna sem við hýsum sjálf.
  
  * Straumlínulagað nothæfi er umtalsverð hjálp fyrir upplifun þróunaraðila og þar með fyrir fínni svið eins og samræmi, skýrleika, öryggi og auðveldan námsferil.

  * Þegar eitthvað er bilað eða vandkvæðum háð viljum við skilvirka leið til að tilkynna vandamálið. Þetta er sérstaklega mikilvægt fyrir öll öryggistengd vandamál.


### Takmarkanir

Engar þekktar. Azure hefur birt skuldbindingu um að vinna vel með ytri verkfærum.


### Afstöður

Við skoðuðum að nota Microsoft Azure Devops á móti AWS sem er fyrir.

Við gerðum tilraunir með Azure DevOps, Azure Pipelines, Azure Repo og uppsetningu nýs þjóns í Azure með Terraform.

Við gerðum tilraunir með að fá stuðning frá fulltrúum Microsoft.

Við öfluðum upplýsinga frá jafningjum á bloggum og Hacker News.


### Röksemd

Azure DevOps auglýsir framúrskarandi safn þjónustu, en þau standast ekki væntingar, vinna ekki vel saman og stuðningur er lélegur.

Okkar eigin reynsla:

  * Uppsetning Azure er óreiða af viðmótum, sum skarast við Microsoft-reikninga, önnur ekki. T.d. er til Azure-innskráning, Microsoft.com-innskráning, Live.com-innskráning o.s.frv. og öll eru í gangi samtímis.

  * Við rákumst á minniháttar öryggisvandamál við uppsetningu og fundum enga lausn. Við reyndum margar leiðir til að tilkynna það, til margra fulltrúa Microsoft, án árangurs. Við tilkynntum það með góðum árangri til öryggisteymis Microsoft, sem svaraði með „verður ekki lagað“.

  * Skjölun er oft annaðhvort röng eða úrelt. Að minnsta kosti hluti af þessu stafar af lélegri leitarvél Microsoft og hluti af undirmáls SEO.
  
  * Uppsetning Terraform er vel skjalfest og virkar. Stuðningur við Terraform er hins vegar veikur samanborið við AWS því Microsoft er að byggja upp viðskiptasambönd við söluaðila til að búa til dæmi um keðjuð Terraform-uppsetningardæmi.

Reynsla jafningja:

  * Eftir að hafa gert okkar eigið blindmat leituðum við að reynslu jafningja. Það sem við fundum staðfesti reynslu okkar.

  * Jafningjar greindu frá frekari vandamálum með smíðatíma og vandamálum með eigin smíðaþjóna. Þessi vandamál eru umtalsvert alvarlegri en viðmótsvandamál, því að framkvæma smíðar er kjarnatilgangur smíðaleiðslu og við gerum ráð fyrir að gera margar á dag.

  * Við fundum framúrskarandi þátttöku Azure-starfsfólks á umræðusvæðum. Hrós til Microsoft fyrir þetta. Við erum sérstaklega hrifin af Edward Thomson, Azure PM og forritara, vegna þátttöku hans, hreinskilni og tæknilegra útskýringa.


### Afleiðingar

Að velja Microsoft Azure DevOps lítur út fyrir að vera dýrara (~3x) í tíma og kostnaði en að velja ekki Azure.


## Tengt


### Tengdar ákvarðanir

Ef við veljum Azure DevOps eru margar tengdar þjónustur, þar á meðal Azure Repo, Azure Pipeline o.s.frv. Við teljum að ef við veljum Azure Devops gæti það auðveldað að nota fleiri eiginleika Azure, eða gert erfiðara að nota eiginleika annarra söluaðila.

Við teljum að Microsoft stígi stór skref í upplifun þróunaraðila og við sjáum Microsoft kaupa stór þróunarverkfæri (t.d. GitHub) og ávirkni (t.d. Citus).

Ef við veljum Azure DevOps gætum við viljað leggja áherslu á að velja þjónustu sem Microsoft hefur keypt, og við gætum einnig viljað nálgast keyptar þjónustur af meiri varkárni/mati vegna hugsanlegrar vefjahafnar, t.d. áhættu á starfsmannaveltu.


### Tengdar kröfur

Við viljum að smíðatími sé mjög hraður. Við sættum okkur við að greiða hátt álag fyrir þetta. Það er vegna þess að við viljum þróa mjög hratt í áföngum.

Við viljum að áreiðanleiki sé mjög mikill. Við sættum okkur við að greiða hátt álag fyrir þetta. Það er vegna þess að við erum að prófa notkunartilvik með mikið verðmæti, þar á meðal fjármálafærslur, trúnaðarfærslur o.s.frv.

Fjórir helstu devops-KPI okkar fela í sér meðaltíma til endurheimtar, sem krefst hraðrar smíði og mikils áreiðanleika.


### Tengdar afurðir

Við viljum að smíðakerfið skili afurðum sem henta til notkunar í öðrum kerfum, svo sem Artifactory.


### Tengdar meginreglur

Auðafturkræft. Við getum metið Azure DevOps samhliða AWS sem er fyrir.


## Athugasemdir


### Microsoft Devops CI: An Unsatisfying Adventure

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Bloggfærsla.

"As a software developer, I know first-hand how difficult it is to build quality products quickly and cheaply. It’s an art form that we sometimes get right, and other times devolves into something akin to the Obama era healthcare government site. Our level of control over the resulting product varies, and blame for failure often falls on the wrong people in the decision-making hierarchy. Microsoft’s Azure DevOps (formerly known as Visual Studio Team Services), despite clearly good intentions, is a perfect storm of bad decisions and poor execution."


### Helstu atriði úr umræðu á Hacker News

https://news.ycombinator.com/item?id=18983586

"We use Azure DevOps extensively at my work and, after having used GitHub, Gitlab, self hosted solutions, Jenkins, TeamCity... Azure DevOps ranks dead last."

"The UI is terribly clunky everywhere. The worst for me are pull requests. Incredibly tough to work with people on a pull request. I can't even point you to "a" particular problem - for us it's broken everywhere."

"Azure Devops is something I want to love. The UI keeps changing, but doesn't fix underlying bugs that have been around for ages."

"The tools are not well integrated, the UI is really slow, there’s no dashboard view of active pull requests, builds, releases, etc for my favorite repos. Build/Deploy times are insanely slow."

"We tried to also use Azure Boards (Work Items, Boards, Backlogs, etc). Ouch. It is a complete UI mess of disjointed ideas. Instead of implementing one thing well, they implemented two dozen things terribly."


### Windows Development MVP

Windows Development MVP here. I feel like I must shoulder some of the responsibility here for not being louder about these issues. But must say, I'm disappointed to hear you're "surprised" about the UX issues. I've been telling your folks the UX is dreadful (e.g. as far back as pre-launch) and kept hearing back "we know, we're fixing it". I'll start formalizing the feedback and push it through the pipes, stay tuned. I'm also local (Bellevue), would love to come in and try to pipeline our relatively simple oss .net/wpf/uwp app. I suspect it'll be an eye opener for the both of us.

Dæmi:

* You can't build a pipeline with a git repo. that contains submodules

* Found it impossible to edit the PATH for some custom tooling

* The New Pipeline experience just doesn't make a lot of sense, new users clicking around will eventually end up at the wrong Docs.


### Samantekt Edward Thomson (Azure PM)

I wrote the code that merges your pull requests. Program Manager for at Microsoft for Azure DevOps; formerly a software engineer on version control tools at GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

Co-maintainer of libgit2. https://libgit2.github.io

Co-host of All Things Git, the Podcast about Git. https://www.allthingsgit.com/

Curator of Developer Tools Weekly, a newsletter about development tools. https://developertoolsweekly.com/
