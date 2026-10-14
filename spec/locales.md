# Locales

## Codes

Every directory under `locales/` is named lowercase `<language>-<region>`
(e.g. `en-001`, `cy-gb`, `zh-tw`). Two-letter, region-less directories such as
`locales/en/` do not exist and must not be created. `-001` means "world" (UN
M.49), used for a language-wide translation. Regional variants exist for Welsh
(`cy-gb`), English (`en-gb`, `en-us`) and Chinese (`zh-cn`, `zh-tw`).

`en-001` is the English source of truth: edit English there, then translate.
Links to English content use `locales/en-001/`.

The picker uses `_` and mixed case instead (`en_GB`, `zh_TW`, `da_001`); its
bare value `en` means `en-001`. A directory name is also the locale's route
(`/<code>/`) and its search-index name (`static/search/<code>.json`). The
website has no separate `/en/` site: English is the `/en-001/` locale route
(`/en/` returns 404); see [website.md](website.md#url-scheme). Only locale directories live in
`locales/`; stray or duplicate directories (for example a copy of a locale
under another name) fail the audit and the sync, and are deleted.

## The 61 locales

| Directory and route | Picker value | Endonym (Intl) |
|---|---|---|
| `ar-001` | `ar_001` | العربية (العالم) |
| `bn-001` | `bn_001` | বাংলা (পৃথিবী) |
| `cy-001` | `cy_001` | Cymraeg (Y Byd) |
| `cy-gb` | `cy_GB` | Cymraeg (Y Deyrnas Unedig) |
| `da-001` | `da_001` | dansk (Verden) |
| `da-dk` | `da_DK` | dansk (Danmark) |
| `de-001` | `de_001` | Deutsch (Welt) |
| `de-at` | `de_AT` | Deutsch (Österreich) |
| `de-de` | `de_DE` | Deutsch (Deutschland) |
| `el-001` | `el_001` | Ελληνικά (Κόσμος) |
| `el-cy` | `el_CY` | Ελληνικά (Κύπρος) |
| `el-gr` | `el_GR` | Ελληνικά (Ελλάδα) |
| `en-001` | `en` | English |
| `en-gb` | `en_GB` | English (United Kingdom) |
| `en-ie` | `en_IE` | English (Ireland) |
| `en-us` | `en_US` | English (United States) |
| `es-001` | `es_001` | español (Mundo) |
| `es-es` | `es_ES` | español (España) |
| `et-001` | `et_001` | eesti (maailm) |
| `et-ee` | `et_EE` | eesti (Eesti) |
| `fi-001` | `fi_001` | suomi (maailma) |
| `fi-fi` | `fi_FI` | suomi (Suomi) |
| `fr-001` | `fr_001` | français (Monde) |
| `fr-fr` | `fr_FR` | français (France) |
| `fr-lu` | `fr_LU` | français (Luxembourg) |
| `hi-001` | `hi_001` | हिन्दी (विश्व) |
| `hi-in` | `hi_IN` | हिन्दी (भारत) |
| `id-001` | `id_001` | Indonesia (Dunia) |
| `id-id` | `id_ID` | Indonesia (Indonesia) |
| `is-001` | `is_001` | íslenska (heimurinn) |
| `is-is` | `is_IS` | íslenska (Ísland) |
| `it-001` | `it_001` | italiano (Mondo) |
| `it-it` | `it_IT` | italiano (Italia) |
| `ja-001` | `ja_001` | 日本語 (世界) |
| `ko-001` | `ko_001` | 한국어(세계) |
| `nl-001` | `nl_001` | Nederlands (wereld) |
| `nl-be` | `nl_BE` | Nederlands (België) |
| `nl-nl` | `nl_NL` | Nederlands (Nederland) |
| `pl-001` | `pl_001` | polski (świat) |
| `pl-pl` | `pl_PL` | polski (Polska) |
| `pt-001` | `pt_001` | português (Mundo) |
| `pt-pt` | `pt_PT` | português (Portugal) |
| `ro-001` | `ro_001` | română (Lume) |
| `ro-ro` | `ro_RO` | română (România) |
| `ru-001` | `ru_001` | русский (весь мир) |
| `sv-001` | `sv_001` | svenska (världen) |
| `sv-se` | `sv_SE` | svenska (Sverige) |
| `sw-001` | `sw_001` | Kiswahili (Dunia) |
| `sw-tz` | `sw_TZ` | Kiswahili (Tanzania) |
| `th-001` | `th_001` | ไทย (โลก) |
| `th-th` | `th_TH` | ไทย (ประเทศไทย) |
| `tr-001` | `tr_001` | Türkçe (Dünya) |
| `tr-tr` | `tr_TR` | Türkçe (Türkiye) |
| `ur-001` | `ur_001` | اردو (دنیا) |
| `vi-001` | `vi_001` | Tiếng Việt (Thế giới) |
| `vi-vn` | `vi_VN` | Tiếng Việt (Việt Nam) |
| `zh-001` | `zh_001` | 中文（世界） |
| `zh-cn` | `zh_CN` | 中文（中国） |
| `zh-tw` | `zh_TW` | 中文（台灣） |

Counts: 61 locales, of which `en-001` is the source and 60 are translations or
variants (`en-gb` and `en-us` follow English; `cy-gb` is a copy of `cy-001`;
`hi-in` is a copy of `hi-001`; `sv-se` is a copy of `sv-001`; `tr-tr` is a copy of `tr-001`; `nl-nl`, `is-is`, `et-ee`, `id-id`, `fi-fi`, `it-it`, `th-th` and `vi-vn` are copies of their `-001` locales; `da-dk`, `de-de`, `de-at`, `es-es`, `fr-fr`, `fr-lu`, `pt-pt` and `nl-be` are copies of `da-001`, `de-001`, `es-001`, `fr-001`, `pt-001` and `nl-001`; `en-ie` is a copy of `en-gb`; `pl-pl` is a copy of `pl-001`; `ro-ro` is a copy of `ro-001`; `sw-tz` is a copy of `sw-001`; `el-gr` is a copy of `el-001`; `el-cy` is a copy of `el-001`). Every one is complete: 205 files, 63 pages, and a root index.

`locales/index.md` lists each locale as `* [<Endonym> (<World>)](<code>/)`.
`locales/locales-by-priority.md` records the translation order (all are
done).

Turkish: `tr-001` (the world locale) and `tr-tr` (identical content, kept for
the regional name, like `cy-gb`) are complete. Turkish headings use "Bağlantılı"
(related) rather than "İlgili": Turkish "İ" lowercases to "i" plus a combining
dot, which breaks `#ilgili`-style anchors on the site.

## Translating directory names

Everything under `locales/<code>/` is translated, including directory names:
the three section directories and every content directory. Slugs are
lowercase, hyphen-separated, keep Latin-script product names, and have no
punctuation other than `-` (no underscores, spaces, or middle dots; Latin
letters inside CJK names are lowercased and split with `-`, e.g.
`google-cloud-platform`). A slug may equal the English one only when it is a
product name or a genuine cognate in that language (listed in
`scripts/audit-locales.py`). Link targets must match the translated directory
names exactly. The English-to-local slug mapping is kept as a three-column
TSV (section, English slug, localized directory) while translating.

## Root index (the translated README)

`locales/<code>/index.md` is the locale's translation of the top-level
`README.md`, and the locale's landing page on the website. `README.md` beside it
is a symlink. It has this fixed structure (the website and the audit rely on it):

1. `# <title>` and one intro paragraph (the hero), then the "Important" note
   (`> [!IMPORTANT]`), then the Contents list, the Templates list (13 entries),
   and the Examples list (8 entries plus "many more"). Links are relative to
   the locale root, for example `templates/<dir>/`.
2. Exactly **15 `##` sections**, in this order: what is an ADR; how to start;
   how to start with tools; how to start with git; Claude Code skills; file name
   conventions; suggestions for writing good ADRs; ADR example templates;
   teamwork advice; teamwork questions; next step concepts; architecture
   diagrams, views and viewpoints; fitness functions; decision guardrails for
   pull requests; for more information.
3. Sections that exist as documents (all except skills, example templates, next
   step, diagrams, guardrails, more information) are the locale's own translated
   documents, with headings shifted so each starts at `##`. The other five are
   translated from the README. "For more information" keeps the English titles
   and URLs of external works and translates only the group labels and two
   phrases. The teamwork questions document has no title of its own, so its
   `##` title is added.
4. Contents anchors are the heading slugs defined in
   [repository.md](repository.md#verification). Headings must not start with a
   capital "İ" (Turkish), whose lowercase form breaks anchors.

`locales/en-001/index.md` is built the same way from English, and the top-level
`README.md` stays the canonical English overview. A few README passages differ
slightly from the documents they include (for example an extra tool bullet); the
locale roots follow the documents.

## Translation workflow (per locale, serial)

1. Translate 12 documents, 11 templates, 40 examples, plus the three section
   index pages.
2. Write the root `index.md` (above) and make each directory's `README.md` a symlink to its `index.md`; copy `.locale-peer-id`
   files from `locales/en-001`; copy `LICENSE.md` files unchanged.
3. Run the verification in [repository.md](repository.md#verification).
4. Append `* [<Endonym> (<World>)](<code>/)` to `locales/index.md`.
5. Add the code to `LOCALES` in the website's `src/lib/locales.js`, keeping the
   array sorted by code.
6. Commit, push, publish the website subtree, verify.

Translations are produced without native-reader review unless stated.

## Picker labels

The endonym comes from `Intl.DisplayNames`. For `*_001` the region is
dropped (`Deutsch`); for other regions it becomes ` - `
(`English - United States`). The first letter of each part is capitalized.

## Welsh terminology (`cy-001`, `cy-gb`)

Welsh translations follow the Welsh Government's TermCymru terminology list
(`2026-07-02 - TermCymru.csv`) wherever it has an entry. Both Welsh locales
hold identical content (`cy-gb` is a copy of `cy-001`). Terms used throughout:

| English | Welsh | Source |
|---|---|---|
| architecture (software) | saernïaeth | TermCymru (ICT) |
| architect | pensaer | TermCymru |
| decision | penderfyniad | |
| record | cofnod | TermCymru |
| template | templed (pl. templedi) | TermCymru |
| context | cyd-destun | TermCymru |
| status | statws | |
| consequence(s) | canlyniad(au) | |
| requirement | gofyniad | TermCymru |
| stakeholder | rhanddeiliad | TermCymru |
| criteria / criterion | meini prawf / maen prawf | TermCymru |
| teamwork | gwaith tîm | TermCymru |
| sustainability / sustainable | cynaliadwyedd / cynaliadwy | TermCymru |
| governance | llywodraethiant | TermCymru |
| compliance | cydymffurfedd | TermCymru |
| lifecycle | cylch oes | TermCymru |
| repository | ystorfa | TermCymru |
| pipeline | piblinell | TermCymru |
| compatibility | cydweddoldeb | TermCymru |
| scalability | graddadwyedd | |
| rationale | sail resymegol | TermCymru |
| timestamp | stamp amser | |
| front end / back end | pen blaen / pen ôl | |

Conventions: ADR plurals are "ADRau"; acronyms (ADR, AD, ADL, ASR, AKM) are kept;
product names, code, and URLs stay in English; "deprecated" is "anghymeradwy",
"superseded" "wedi'i ddisodli". The English acronym expansion
"architecture decision record" is "cofnod penderfyniad saernïaeth".
Directory names are Welsh slugs (`dogfennau`, `templedi`, `enghreifftiau`).
