# رکورد تصمیم معماری (ADR)

رکورد تصمیم معماری (ADR) سندی است که یک تصمیم مهم معماری را همراه با زمینه و پیامدهای آن ثبت می‌کند.

> [!IMPORTANT]
> پیش از استفاده از این منابع در هر سیستم حیاتی، بررسی دقیق و مستقل خود را انجام دهید.

فهرست مطالب:

- [رکورد تصمیم معماری چیست؟](#رکورد-تصمیم-معماری-چیست)
- [چگونه استفاده از ADR را شروع کنیم](#چگونه-استفاده-از-adr-را-شروع-کنیم)
- [چگونه استفاده از ADR را با ابزارها شروع کنیم](#چگونه-استفاده-از-adr-را-با-ابزارها-شروع-کنیم)
- [چگونه استفاده از ADR را با git شروع کنیم](#چگونه-استفاده-از-adr-را-با-git-شروع-کنیم)
- [مهارت‌های Claude Code برای ADR](#مهارتهای-claude-code-برای-adr)
- [قراردادهای نامگذاری فایل برای ADR](#قراردادهای-نامگذاری-فایل-برای-adr)
- [پیشنهادهایی برای نوشتن ADR خوب](#پیشنهادهایی-برای-نوشتن-adr-خوب)
- [قالب‌های نمونهٔ ADR](#قالبهای-نمونهٔ-adr)
- [نکات کار تیمی برای ADR](#نکات-کار-تیمی-برای-adr)
- [سوالات کار تیمی برای ADR](#سوالات-کار-تیمی-برای-adr)
- [مفاهیم گام بعدی برای ADR](#مفاهیم-گام-بعدی-برای-adr)
- [نمودارها و نماها و دیدگاه‌های معماری](#نمودارها-و-نماها-و-دیدگاههای-معماری)
- [توابع تناسب برای تصمیمات به‌عنوان کد](#توابع-تناسب-برای-تصمیمات-بهعنوان-کد)
- [نرده‌های محافظ تصمیم برای درخواست‌های ادغام (Pull Request)](#نردههای-محافظ-تصمیم-برای-درخواستهای-ادغام-pull-request)
- [برای اطلاعات بیشتر](#برای-اطلاعات-بیشتر)

قالب‌ها:

- [قالب رکورد تصمیم از Jeff Tyree و Art Akerman](قالبها/قالب-رکورد-تصمیم-جف-تایری-و-آرت-آکرمن/)
- [قالب رکورد تصمیم از Michael Nygard](قالبها/قالب-رکورد-تصمیم-مایکل-نایگارد/)
- [قالب رکورد تصمیم از EdgeX](قالبها/قالب-رکورد-تصمیم-edgex/)
- [قالب رکورد تصمیم از arc42](قالبها/قالب-رکورد-تصمیم-arc42/)
- [قالب رکورد تصمیم برای الگوی الکساندری](قالبها/قالب-رکورد-تصمیم-برای-الگوی-الکساندری/)
- [قالب رکورد تصمیم برای طرح توجیهی کسب‌وکار](قالبها/قالب-رکورد-تصمیم-برای-طرح-توجیهی-کسب-و-کار/)
- [قالب رکورد تصمیم پروژهٔ MADR](قالبها/قالب-رکورد-تصمیم-پروژه-madr/)
- [قالب رکورد تصمیم با Planguage](قالبها/قالب-رکورد-تصمیم-با-planguage/)
- [قالب رکورد تصمیم از Paulo Merson](https://github.com/pmerson/ADR-template)
- [قالب رکورد تصمیم از Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [قالب رکورد تصمیم از Gareth Morgan](قالبها/قالب-رکورد-تصمیم-گرث-مورگان/)
- [قالب رکورد تصمیم از GIG Cymru NHS Wales](قالبها/قالب-رکورد-تصمیم-gig-cymru-nhs-wales/)
- [قالب رکورد تصمیم برای تصمیمات فنی مهم (ITD) از Ignacio Larrañaga](قالبها/قالب-رکورد-تصمیم-برای-تصمیمات-فنی-مهم/)

نمونه‌ها:

- [چارچوب CSS](مثالها/چارچوب-css/)
- [پیکربندی متغیرهای محیطی](مثالها/پیکربندی-متغیرهای-محیطی/)
- [متریک، مانیتور، هشدار](مثالها/متریک-مانیتور-هشدار/)
- [Microsoft Azure DevOps](مثالها/microsoft-azure-devops/)
- [مونوریپو یا مولتی‌ریپو](مثالها/مونوریپو-یا-مولتی-ریپو/)
- [زبان‌های برنامه‌نویسی](مثالها/زبان-های-برنامه-نویسی/)
- [ذخیره‌سازی اطلاعات محرمانه](مثالها/ذخیره-سازی-اطلاعات-محرمانه/)
- [فرمت برچسب زمانی](مثالها/فرمت-برچسب-زمانی/)
- [و بسیار بیشتر...](مثالها/)

## رکورد تصمیم معماری چیست؟

**رکورد تصمیم معماری** (ADR) سندی است که یک تصمیم مهم معماری را همراه با زمینه و پیامدهای آن ثبت می‌کند.

**تصمیم معماری** (AD) انتخابی در طراحی نرم‌افزار است که یک نیازمندی مهم را برآورده می‌کند.

**گزارش تصمیمات معماری** (ADL) مجموعهٔ همهٔ ADRهایی است که برای یک پروژه (یا سازمان) مشخص ایجاد و نگهداری می‌شوند.

**نیازمندی مهم از نظر معماری** (ASR) نیازمندی‌ای است که تأثیر قابل اندازه‌گیری بر معماری یک سیستم نرم‌افزاری دارد.

همهٔ این‌ها در حوزهٔ **مدیریت دانش معماری** (AKM) قرار می‌گیرند.

هدف این سند ارائهٔ مرور سریعی از ADRها، روش ایجاد آن‌ها و محل یافتن اطلاعات بیشتر است.

مخفف‌ها:

  * **AD**: تصمیم معماری

  * **ADL**: گزارش تصمیمات معماری

  * **ADR**: رکورد تصمیم معماری

  * **AKM**: مدیریت دانش معماری

  * **ASR**: نیازمندی مهم از نظر معماری

## چگونه استفاده از ADR را شروع کنیم

برای شروع استفاده از ADR، با هم‌تیمی‌های خود دربارهٔ این حوزه‌ها گفتگو کنید.

شناسایی تصمیم:

  * AD چقدر فوری و چقدر مهم است؟

  * آیا باید همین حالا گرفته شود یا می‌توان تا کسب اطلاعات بیشتر صبر کرد؟

  * تجربهٔ شخصی و جمعی، و همچنین روش‌ها و شیوه‌های طراحی شناخته‌شده، می‌توانند به شناسایی تصمیم کمک کنند.

  * در حالت ایدئال یک فهرست کارهای مربوط به تصمیم‌ها نگه دارید که مکمل فهرست کارهای محصول باشد.

تصمیم‌گیری:

  * تکنیک‌های متعددی برای تصمیم‌گیری وجود دارد، هم عمومی و هم ویژهٔ معماری نرم‌افزار، برای مثال نگاشت گفتگو (dialogue mapping).

  * تصمیم‌گیری گروهی یک موضوع پژوهشی فعال است.

اجرا و الزام تصمیم:

  * ADها در طراحی نرم‌افزار به کار می‌روند؛ بنابراین باید به ذی‌نفعان سیستم، یعنی کسانی که آن را تأمین مالی، توسعه و بهره‌برداری می‌کنند، اطلاع داده شوند و مورد پذیرش آن‌ها قرار گیرند.

  * سبک‌های کدنویسی که معماری در آن‌ها آشکار است و بازبینی‌های کدی که بر دغدغه‌ها و تصمیم‌های معماری تمرکز دارند، دو شیوهٔ مرتبط هستند.

  * هنگام نوسازی یک سیستم نرم‌افزاری در جریان تکامل نرم‌افزار نیز باید ADها (دوباره) در نظر گرفته شوند.

اشتراک‌گذاری تصمیم (اختیاری):

  * بسیاری از ADها در پروژه‌های مختلف تکرار می‌شوند.

  * از این رو، هنگام به‌کارگیری راهبرد صریح مدیریت دانش، تجربه‌های مربوط به تصمیم‌های گذشته، چه خوب و چه بد، می‌توانند دارایی‌های ارزشمند و قابل استفادهٔ مجدد باشند.

مستندسازی تصمیم:

  * قالب‌ها و ابزارهای فراوانی برای ثبت تصمیم وجود دارد.

  * به جوامع چابک (agile) نگاه کنید، برای مثال ADRهای M. Nygard.

  * به فرایندهای سنتی مهندسی نرم‌افزار و طراحی معماری نگاه کنید، برای مثال طرح‌بندی‌های جدولی که IBM UMF و Tyree و Akerman از CapitalOne پیشنهاد کرده‌اند.

برای اطلاعات بیشتر:

  * مراحل بالا از مدخل ویکی‌پدیا دربارهٔ [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision) برگرفته شده است

## چگونه استفاده از ADR را با ابزارها شروع کنیم

- [MySpec](https://myspec.dev) — پلتفرم خودکار برای مشخصات و تصمیمات معماری که قانون اساسی پروژه، معماری فنی و ADRها را در Markdown مرتب ساختاردهی می‌کند و از طریق MCP ارائه می‌دهد.

می‌توانید استفاده از ADR را با ابزارها به هر شکلی که می‌خواهید شروع کنید.

برای مثال:

  * اگر از Google Drive و ویرایش آنلاین خوشتان می‌آید، می‌توانید یک Google Doc یا Google Sheet ایجاد کنید.

  * اگر از کنترل نسخهٔ کد منبع مانند git استفاده می‌کنید، می‌توانید برای هر ADR یک فایل ایجاد کنید.

  * اگر از ابزارهای برنامه‌ریزی پروژه مانند Atlassian Jira استفاده می‌کنید، می‌توانید از ردیاب برنامه‌ریزی آن ابزار استفاده کنید.

  * اگر از ویکی‌ها مانند MediaWiki استفاده می‌کنید، می‌توانید یک ویکی ADR ایجاد کنید.

## چگونه استفاده از ADR را با git شروع کنیم

اگر از کنترل نسخهٔ git استفاده می‌کنید، این روشی است که ما برای شروع استفاده از ADR با git در یک پروژهٔ نرم‌افزاری معمولی دارای کد منبع ترجیح می‌دهیم.

یک پوشه برای فایل‌های ADR ایجاد کنید:

```sh
$ mkdir adr
```

برای هر ADR یک فایل متنی ایجاد کنید، مثلاً `choose-database.md`:

```sh
$ vi choose-database.md
```

هر چیزی که می‌خواهید در ADR بنویسید. برای ایده گرفتن، قالب‌های این مخزن را ببینید.

ADR را در مخزن git خود کامیت کنید.

## مهارت‌های Claude Code برای ADR

این مخزن دو مهارت [Claude Code](https://claude.com/claude-code) را زیر [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) ارائه می‌دهد، تا یک عامل کدنویسی هوش مصنوعی بتواند ADR را همان‌گونه که این پروژه توصیه می‌کند بنویسد و نگهداری کند:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — همه‌منظوره، برای هر کسی که در هر پروژه‌ای ADR می‌نویسد. به تصمیم‌گیری دربارهٔ اینکه آیا تصمیمی به ADR نیاز دارد کمک می‌کند، پوشهٔ `adr/` یا `decisions/` را راه‌اندازی می‌کند، فایل را نام‌گذاری می‌کند، قالبی را از میان یازده اسکلت همراه برمی‌گزیند و بخش‌های زمینه/تصمیم/پیامدها را به‌خوبی می‌نویسد.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — ویژهٔ نگهدارندگان همین مخزن. چیدمان مخزن، قرارداد بازتاب README/زبان‌ها (locales) و گام‌های دقیق افزودن قالب، نمونه یا پیوند ابزار جدید را مستند می‌کند.

برای استفاده از یک مهارت، پوشهٔ آن را در ریشهٔ مخزنی که روی آن کار می‌کنید در `.claude/skills/` کپی کنید (یا در `~/.claude/skills/` تا در هر پروژه در دسترس باشد)، سپس از Claude Code بخواهید یک ADR بنویسد یا بازبینی کند.

## قراردادهای نامگذاری فایل برای ADR

اگر تصمیم دارید ADRهای خود را با فایل‌های متنی معمولی ایجاد کنید، ممکن است بخواهید قرارداد نامگذاری فایل ADR مخصوص خودتان را تعیین کنید.

ما ترجیح می‌دهیم از قراردادی برای نامگذاری فایل استفاده کنیم که قالب مشخصی دارد.

نمونه‌ها:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

قرارداد نامگذاری فایل ما:

  * نام شامل یک عبارت فعلی امری در زمان حال است. این کار خوانایی را بهبود می‌دهد و با قالب پیام‌های کامیت ما همخوان است.

  * نام از حروف کوچک و خط تیره استفاده می‌کند (مانند همین مخزن). این تعادلی میان خوانایی و قابلیت استفاده در سیستم است.

  * پسوند markdown است. این می‌تواند برای قالب‌بندی آسان مفید باشد.

## پیشنهادهایی برای نوشتن ADR خوب

ویژگی‌های یک ADR خوب:

* دلیل و منطق: دلایل اتخاذ آن AD مشخص را توضیح دهید. این می‌تواند شامل زمینه (پایین‌تر ببینید)، مزایا و معایب گزینه‌های مختلف، مقایسهٔ ویژگی‌ها، بحث هزینه/فایده و موارد دیگر باشد.

* مشخص بودن: هر ADR باید دربارهٔ یک AD باشد، نه چند AD.

* برچسب زمانی: مشخص کنید هر مورد در ADR چه زمانی نوشته شده است. این امر به‌ویژه برای جنبه‌هایی که ممکن است با گذشت زمان تغییر کنند، مانند هزینه‌ها، زمان‌بندی‌ها، مقیاس‌پذیری و مانند آن‌ها اهمیت دارد.

* تغییرناپذیری: اطلاعات موجود در ADR را تغییر ندهید. در عوض، با افزودن اطلاعات جدید ADR را اصلاح کنید، یا با ایجاد ADR جدید آن را جایگزین کنید.

ویژگی‌های یک بخش «زمینه» خوب در ADR:

* وضعیت سازمان و اولویت‌های کسب‌وکار خود را توضیح دهید.

* دلایل و ملاحظاتی را که بر ترکیب اجتماعی و مهارتی تیم‌های شما مبتنی است، بگنجانید.

* مزایا و معایب مرتبط را بگنجانید و آن‌ها را به شکلی توصیف کنید که با نیازها و اهداف شما همسو باشد.

ویژگی‌های یک بخش «پیامدها» خوب در ADR:

* توضیح دهید که از اتخاذ تصمیم چه چیزی نتیجه می‌شود. این می‌تواند شامل اثرات، نتایج، خروجی‌ها، پیگیری‌ها و موارد دیگر باشد.

* اطلاعاتی دربارهٔ ADRهای بعدی بگنجانید. نسبتاً رایج است که یک ADR نیاز به ADRهای بیشتری ایجاد کند، مثلاً وقتی یک ADR انتخاب بزرگ و فراگیری انجام می‌دهد که به‌نوبهٔ خود نیاز به تصمیم‌های کوچک‌تر بیشتری ایجاد می‌کند.

* هر فرایند بازبینی پس از اقدام را بگنجانید. برای تیم‌ها معمول است که هر ADR را یک ماه بعد مرور کنند تا اطلاعات ADR را با آنچه در عمل رخ داده مقایسه کنند و یاد بگیرند و رشد کنند.

یک ADR جدید ممکن است جای ADR قبلی را بگیرد:

* وقتی AD‌ای اتخاذ می‌شود که ADR قبلی را جایگزین یا بی‌اعتبار می‌کند، باید یک ADR جدید ایجاد شود

## قالب‌های نمونهٔ ADR

قالب‌های نمونهٔ ADR که از اینترنت گردآوری کرده‌ایم:

- [قالب ADR از Michael Nygard](قالبها/قالب-رکورد-تصمیم-مایکل-نایگارد/) (ساده و محبوب)

- [قالب ADR از Jeff Tyree و Art Akerman](قالبها/قالب-رکورد-تصمیم-جف-تایری-و-آرت-آکرمن/) (پیچیده‌تر)

- [قالب ADR برای الگوی الکساندری](قالبها/قالب-رکورد-تصمیم-برای-الگوی-الکساندری/) (ساده با جزئیات زمینه)

- [قالب ADR برای طرح توجیهی کسب‌وکار](قالبها/قالب-رکورد-تصمیم-برای-طرح-توجیهی-کسب-و-کار/) (بیشتر MBA‌محور، با هزینه‌ها، SWOT و نظرات بیشتر)

- [قالب ADR پروژهٔ Markdown Any Decision Records (MADR)](قالبها/قالب-رکورد-تصمیم-پروژه-madr/) (هم نسخهٔ ساده و هم تفصیلی؛ نسخهٔ تفصیلی بر گزینه‌ها و مزایا و معایبشان تأکید دارد)

- [قالب ADR با Planguage](قالبها/قالب-رکورد-تصمیم-با-planguage/) (بیشتر تضمین‌کیفیت‌محور)

- [قالب تصمیمات فنی مهم (ITD) از Ignacio Larrañaga](قالبها/قالب-رکورد-تصمیم-برای-تصمیمات-فنی-مهم/) (ناب و تصمیم‌محور، بهینه برای بازبینی سریع مدیران اجرایی)

## نکات کار تیمی برای ADR

اگر در نظر دارید با تیم خود از رکوردهای تصمیم استفاده کنید، این‌ها نکاتی است که از کار با تیم‌های متعدد آموخته‌ایم.

شما فرصت دارید هم‌تیمی‌های خود را رهبری کنید؛ به جای تحمیل «چه چیزی»، با هم دربارهٔ «چرا» گفتگو کنید. برای مثال، رکوردهای تصمیم راهی هستند تا تیم‌ها هوشمندانه‌تر فکر کنند و بهتر ارتباط برقرار کنند؛ اگر رکوردهای تصمیم فقط یک الزام کاغذبازی تحمیلی پس از وقوع باشند، ارزشمند نیستند.

برخی تیم‌ها نام «تصمیمات» (decisions) را بسیار به مخفف «ADR» ترجیح می‌دهند. وقتی برخی تیم‌ها از نام پوشهٔ «decisions» استفاده می‌کنند، انگار چراغی روشن می‌شود و تیم شروع به قرار دادن اطلاعات بیشتری در آن پوشه می‌کند، مانند تصمیمات تأمین‌کننده، تصمیمات برنامه‌ریزی، تصمیمات زمان‌بندی و غیره. همهٔ این انواع اطلاعات می‌توانند از یک قالب یکسان استفاده کنند. فرض ما این است که مردم با کلمات («decisions») سریع‌تر از مخفف‌ها («ADR») یاد می‌گیرند، با حذف کلمهٔ «رکورد» انگیزهٔ بیشتری برای نوشتن مستندات در حال انجام دارند، و برخی توسعه‌دهندگان و برخی مدیران نیز از کلمهٔ «معماری» خوششان نمی‌آید.

در تئوری، تغییرناپذیری ایده‌آل است. در عمل، تغییرپذیری برای تیم‌های ما بهتر جواب داده است. ما اطلاعات جدید را با یک مهر تاریخ و یادداشتی مبنی بر اینکه این اطلاعات پس از تصمیم رسیده است، در ADR موجود درج می‌کنیم. این رویکرد به یک «سند زنده» منتهی می‌شود که همهٔ ما می‌توانیم آن را به‌روزرسانی کنیم. به‌روزرسانی‌های معمول زمانی رخ می‌دهد که اطلاعات را به لطف هم‌تیمی‌های جدید، پیشنهادهای جدید، نتایج واقعی استفاده‌های ما، یا تغییرات شخص ثالث پس از تصمیم، مانند قابلیت‌های تأمین‌کننده، طرح‌های قیمت‌گذاری، قراردادهای مجوز و غیره به دست می‌آوریم.

## سوالات کار تیمی برای ADR

### چه کسی می‌تواند ADR ایجاد کند؟

حوزه‌هایی مانند افراد مشخص، نقش‌های مشخص، تیم‌های مشخص یا بخش‌های مشخص را در نظر بگیرید؛ همچنین در نظر بگیرید که آیا افراد، نقش‌ها، تیم‌ها یا بخش‌هایی هستند که می‌توانند سفارش یک ADR را بدهند، یعنی ADR‌ای را درخواست کنند که شخص دیگری آن را تألیف خواهد کرد.

نمونه پاسخ: هر فردی در سازمان ما که صفحهٔ README رکورد تصمیم معماری را خوانده باشد می‌تواند یک ADR پیشنهاد دهد، یعنی می‌تواند نوشتن آن را آغاز کند و آن را با تیم به اشتراک بگذارد.

### چه چیزی ایجاد یک ADR را توجیه می‌کند؟

حوزه‌هایی مانند شیوه‌های کار تیمی در سازمان شما، ساختار سیستم نرم‌افزاری شما، هماهنگی بین تیمی، قابلیت نگهداری بلندمدت، رابط‌های بیرونی، اینکه می‌خواهید چه کسی سود ببرد، و مانند این‌ها را در نظر بگیرید.

نمونه پاسخ: وقتی می‌خواهیم توسعه‌دهندگان آینده «چرایی» کارهایی را که انجام می‌دهیم بفهمند، ADR ایجاد می‌کنیم.

### چه چیزی ایجاد نکردن ADR را توجیه می‌کند؟

حوزه‌هایی مانند تصمیم‌هایی که دربارهٔ معماری نیستند، یا بسیار کوچک‌اند مانند کم‌خطر، مستقل یا مربوط به یک توسعه‌دهنده، یا پیش‌تر در جای دیگری به‌طور کامل پوشش داده شده‌اند مانند استانداردها، سیاست‌ها یا مستندات، یا موقتی‌اند مانند راه‌حل‌های موقت، اثبات مفهوم یا آزمایش‌ها را در نظر بگیرید.

نمونه پاسخ: وقتی دامنهٔ تصمیم، زمان، خطر و هزینهٔ آن محدود است، یا پیش‌تر در جای دیگری پوشش داده شده است، ADR را رد می‌کنیم.

### چرخهٔ عمر یک ADR چیست؟

حوزه‌هایی مانند فرایند ایجاد، فرایند پژوهش، فرایند تصمیم‌گیری، فرایند اجرا و فرایند بازنشستگی را در نظر بگیرید. در نظر بگیرید که چگونه چرخهٔ عمر ADR را در طول زمان پیگیری کنید، مانند اینکه ADR را چگونه از یک وضعیت به وضعیت بعدی ببرید، و همچنین چگونه این را به ذی‌نفعان اطلاع دهید.

نمونه پاسخ: می‌خواهیم یک ADR پنج مرحلهٔ چرخهٔ عمر داشته باشد: آغاز ← پژوهش ← ارزیابی ← اجرا ← نگهداری ← بازنشستگی.

### معیارهای مراحل چرخهٔ عمر یک ADR چیست؟

حوزه‌هایی مانند معیارهای پذیرش یک ADR را در نظر بگیرید، یعنی از کجا می‌دانید که برای پیشرفت از یک مرحلهٔ چرخهٔ عمر به مرحلهٔ بعدی به‌اندازهٔ کافی خوب است؟ آیا مسئله به‌روشنی بیان شده است؟ آیا گزینه‌های جایگزین بررسی شده‌اند؟ آیا مصالحه‌ها به‌اندازهٔ کافی درک و مستند شده‌اند؟
آیا همهٔ زمینهٔ مرتبط فراهم است؟ آیا همهٔ ذی‌نفعان مرتبط درگیر هستند؟ آیا همهٔ بازخوردها اعمال شده‌اند؟

نمونه پاسخ: می‌خواهیم وقتی تیم فعال 1) پژوهش خود را تکمیل کرده، 2) ارزیابی خود را تکمیل کرده، 3) پیشنهاد ADR را با درخواست نظر و مهلت یک هفته برای ذی‌نفعان منتشر کرده، 4) همهٔ نظرات ذی‌نفعان اعمال و پاسخ داده شده باشد، ذی‌نفعان دربارهٔ ADR رأی بدهند.

### چه نقش‌ها و مسئولیت‌هایی با یک ADR تعامل دارند؟

نقش‌هایی مانند پیشنهاددهنده، پژوهشگر، ارزیاب، بازبین، تأییدکننده، نگهدارنده و مانند این‌ها را در نظر بگیرید. مسئولیت‌هایی مانند ارتباط با ذی‌نفعان، اطمینان از برآورده شدن انتظارات، اشتراک‌گذاری در وب‌سایت یا اینترانت، و بازبینی دوره‌ای کار، به‌ویژه هنگام رخ دادن تغییرات مرتبط را در نظر بگیرید.

نمونه پاسخ: می‌خواهیم هر ADR همیشه یک فرد تماس اصلی، یک فرد تماس فرعی و یک تیم پاسخگو داشته باشد؛ این‌ها مسئول ارتباطات، انتشار، نگهداری، بازبینی دوره‌ای دست‌کم سالی یک‌بار و در صورت نیاز بازنشستگی نهایی هستند.

### حکمرانی چگونه با یک ADR تعامل دارد؟

حوزه‌هایی مانند شیوه‌های کار سازمان شما، هر نیاز ویژهٔ انطباق مانند جنبه‌های حقوقی یا منابع انسانی، و اینکه می‌خواهید اجماع در برابر تعارض در برابر ارجاع به سطح بالاتر را چگونه مدیریت کنید، را در نظر بگیرید. آیا حوزه‌ها، افراد یا تیم‌هایی هستند که می‌توانند دربارهٔ یک ADR نفوذ بیشتری نسبت به دیگران داشته باشند، مانند توانایی تأیید آن، رأی دادن به آن یا وتو کردن آن؟

نمونه پاسخ: حکمرانی یک ADR به این ترتیب اولویت است: مدیرعامل، مدیر فناوری، مدیر حقوقی، تیمی که ADR را اجرا می‌کند، و کارشناسان تیم که بیشترین آگاهی را دربارهٔ AD دارند. هیچ‌کس دیگر حکمرانی ندارد مگر آنکه در ADR توضیح داده شده باشد.

### چه اصولی با یک ADR تعامل دارند؟

حوزه‌هایی مانند شیوه‌های کار سازمان شما را که شامل سریع حرکت کردن در برابر آهسته حرکت کردن، اجماع تصمیم در برابر تعارض تصمیم، ترجیحات ریسک در برابر ترجیحات ایمنی، بحث عمومی در برابر بحث خصوصی و مانند این‌هاست، در نظر بگیرید.

نمونه پاسخ: ما از اصول رهبری گرایش به عمل، مخالفت و تعهد (disagree-and-commit)، کافی بودن برآوردهای 70 درصدی برای تصمیم‌های به‌آسانی برگشت‌پذیر و به‌آسانی قابل‌ایزوله‌شدن، و شیوه‌های کار عمومی به‌جز اطلاعات محرمانه طبق توافق‌نامهٔ محرمانگی سازمان خود استفاده می‌کنیم.

## مفاهیم گام بعدی برای ADR

[Arc42](https://arc42.org/) به دو پرسش به‌شیوه‌ای عمل‌گرایانه پاسخ می‌دهد و می‌توان آن را با نیازهای خاص شما تطبیق داد. دربارهٔ معماری خود چه چیزی را باید مستند/منتقل کنید؟ چگونه باید مستند/منتقل کنید؟ Arc42 شامل رکوردهای تصمیم معماری به‌علاوهٔ راهنمایی دربارهٔ اهداف، محدودیت‌ها، زمینه‌ها، کیفیت، ریسک‌ها و موارد دیگر است.

[مدل C4](https://c4model.com/) رویکردی آسان برای یادگیری و توسعه‌دهنده‌پسند برای نمودارسازی معماری نرم‌افزار است. C4 مجموعه‌ای از نمودارهای سلسله‌مراتبی برای زمینه، کانتینرها، مؤلفه‌ها و کد است، به‌علاوهٔ نمودارهای پشتیبان برای چشم‌انداز سیستم، پویا و استقرار.

## نمودارها و نماها و دیدگاه‌های معماری

یک نمودار معماری «نمای معماری» نامیده می‌شود.

«نمای معماری» نمونه‌ای از یک «دیدگاه معماری» است.

«دیدگاه معماری» مخاطب مشخصی با دغدغه‌های مشخص را در نظر دارد.

نمونه‌های دیدگاه معماری، نمونه‌های نما و نمونه‌های نمودار:

- قابلیت‌های کسب‌وکار (Business Capabilities)

- فرایندهای کسب‌وکار سطح بالا

- [جریان‌های ارزش (Value Streams)](https://en.wikipedia.org/wiki/Value_stream)

- کارکردهای نرم‌افزاری نگاشت‌شده به مؤلفه‌های برنامه

- نمودار زمینهٔ [مدل C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- نمودار کانتینر [مدل C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- [نمودار موجودیت-رابطه (Entity-relationship Diagram)](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) برای نگاشت موجودیت‌های داده به مؤلفه‌های برنامه

- [نمودارهای توالی (Sequence Diagrams)](https://en.wikipedia.org/wiki/Sequence_diagram) برای توصیف جریان‌های کارکردی درون سیستم‌ها و برای ادغام‌ها

- نمودارهای [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) برای توصیف جریان‌های داده در مؤلفه‌های برنامه

- نمودارهای [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) برای توصیف فرایندهای کسب‌وکار / سناریوهای کاربر

- نمودارهای [مدیریت هویت و دسترسی (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM)

- نمودارهای [کنترل دسترسی مبتنی بر نقش (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) با نقش‌ها به‌ازای هر مؤلفهٔ برنامه

- نمودارهای [کنترل دسترسی مبتنی بر ویژگی (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) با ویژگی‌ها به‌ازای هر مؤلفهٔ برنامه

- نمودارهای حریم خصوصی

نمودارهای مرتبط:

- نمودار مورد استفاده (Use Case Diagram) موارد استفاده را به مدیریت/مشتریان نشان می‌دهد، که پیش از نیازمندی‌ها می‌آید، که پیش از معماری نرم‌افزار می‌آید.

- نمودار استقرار (Deployment Diagram) سخت‌افزار/رایانه‌های فیزیکی را نشان می‌دهد که مؤلفه‌های نرم‌افزاری روی آن‌ها مستقر می‌شوند.
- نمودار جریان داده (Data Flow Diagram) نشان می‌دهد داده چگونه در سیستم حرکت می‌کند و تبدیل می‌شود.
- نمودار توالی (Sequence Diagram) برای نشان دادن اینکه پروتکل‌هایی مانند HTTP روی محور زمان چگونه کار می‌کنند استفاده می‌شود.

- نمودار فعالیت (Activity Diagram) گردش کار فعالیت‌هایی را که یک سیستم نرم‌افزاری انجام می‌دهد، مانند یک NPC AI، نشان می‌دهد.

## توابع تناسب برای تصمیمات به‌عنوان کد

توابع تناسب (fitness functions) بررسی‌های خودکار و عینی هستند که با کد برنامه‌نویسی نوشته می‌شوند و تأیید می‌کنند که تصمیم‌ها رعایت می‌شوند.

- توابع تناسب تصمیم‌ها را قابل آزمون و قابل اطمینان می‌کنند.

- توابع تناسب برای تصمیم‌ها می‌توانند به‌شدت به تضمین کیفیت، فرایندهای نظارتی و اهداف حکمرانی کمک کنند.

### توابع تناسب چگونه به تصمیم‌ها مرتبط می‌شوند

رکورد تصمیم، تصمیم را مستند می‌کند، در حالی که تابع تناسب، تصمیم را تضمین می‌کند.

- نمونه تصمیم: برای الزامات ممیزی از event sourcing استفاده می‌کنیم.

- نمونه تابع تناسب: از سرور یکپارچه‌سازی پیوسته برای آزمودن این استفاده می‌کنیم که همهٔ تغییرات وضعیت باید رویداد تولید کنند.

### چرا توابع تناسب به تصمیم‌ها کمک می‌کنند

اندازه‌گیری‌های عینی: توابع تناسب یا موفق می‌شوند یا شکست می‌خورند، بنابراین کار قابل‌مشاهده و روشن است.

استفادهٔ پیوسته: توابع تناسب قوانین زندهٔ شما هستند که روی هر کامیت و ساخت اجرا می‌شوند.

اطمینان برای بازآرایی: توابع تناسب خطاهای قوانین تصمیم را به‌صورت خودکار می‌گیرند.

حکمرانی مقیاس‌پذیر: توابع تناسب استانداردها را بدون ایجاد گلوگاه تضمین می‌کنند.

### آیا توابع تناسب می‌توانند از هوش مصنوعی استفاده کنند؟

توابع تناسب می‌توانند با پرسیدن سؤال دربارهٔ کار شما، مانند برنامه‌ها، کد، طرح‌واره‌ها، API‌ها و موارد دیگر، از مدل‌های زبانی بزرگ هوش مصنوعی برای تصمیم‌ها بهره ببرند:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### آزمون واحد معماری

[ArchUnit](https://www.archunit.org/): قوانین معماری کد Java را با استفاده از هر چارچوب ساده آزمون واحد Java بررسی کنید.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): قوانین معماری کد TypeScript و کد JavaScript را با استفاده از Jest، Vitest، Jasmine و غیره بررسی کنید.

## نرده‌های محافظ تصمیم برای درخواست‌های ادغام (Pull Request)

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
رکوردهای تصمیم درست را در لحظهٔ درست به‌طور خودکار نمایان می‌کند — وقتی
توسعه‌دهنده‌ای فعالانه کدی را که آن تصمیم‌ها پوشش می‌دهند تغییر می‌دهد. به‌جای
امید بستن به اینکه توسعه‌دهندگان پیش از ادغام پوشهٔ مستندات را بخوانند، زمینهٔ مرتبط
مستقیماً روی درخواست ادغام ظاهر می‌شود.

این برای هر نوع رکورد تصمیم کار می‌کند: تصمیم‌های معماری، تصمیم‌های داده،
تصمیم‌های انطباق، تصمیم‌های بالینی و پزشکی، تصمیم‌های امنیتی
و موارد دیگر.

با هر سیستم CI (GitLab، Jenkins، CircleCI) و به‌عنوان hook پیش از کامیت کار می‌کند.
متن‌باز. مجوز MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) یک GitHub
Action است که وقتی مسیرهای کد زیر نظر تغییر کنند و
رکورد تصمیم معماری افزوده یا به‌روزرسانی نشود، درخواست ادغام را ناموفق می‌کند. معافیت‌ها صریح‌اند: یک
خط `ADR-Exempt:` همراه با دلیل، گیت را عبور می‌دهد و در
خلاصهٔ کار نوشته می‌شود.
مستقل از قالب، بدون وابستگی. متن‌باز. مجوز MIT.

## برای اطلاعات بیشتر

مقدمه:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

قالب‌ها:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

عمیق‌تر:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - درس ماهانهٔ رایگان معماری نرم‌افزار

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

ابزارها:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

راهنمایی ویژهٔ شرکت‌ها:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

نمونه‌ها:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

ویدیوها:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

پادکست‌ها:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

کتاب‌ها:

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

همچنین ببینید:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - قالب YAML/JSON خنثی نسبت به تأمین‌کننده و قابل‌خواندن توسط ماشین برای نمایش تصمیم‌ها با استدلال صریح، فرضیات، وضعیت شناختی و مصالحه‌ها. با افزودن استدلال ساختاریافته و قابل‌اعتبارسنجی به مستندسازی تصمیم، مکمل ADRها است.
