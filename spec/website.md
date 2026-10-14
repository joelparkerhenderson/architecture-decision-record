# Website

`architecture-decision-record.github.io/`: SvelteKit 3 with
`@sveltejs/adapter-static`, fully prerendered, styled with the Lily Design
System. Live at https://architecture-decision-record.github.io/.

## URL scheme

Every language, English included, is a locale route under its own first path
segment: `/en-001/`, `/de-001/`, `/fr-001/`, `/cy-gb/`, … There is no separate
English site: `/en/` and everything under it (`/en/guide/`, `/en/skills/`, …),
and the old pre-`/en/` URLs (`/guide/`, `/templates/`, `/examples/`, `/skills/`),
return 404 (GitHub Pages serves `404.html`). `en` is not a locale slug.

| URL | Page |
|---|---|
| `/` | Language router (below); nothing else |
| `/<locale>/` | Contents of the locale, or search results for `/<locale>/?<query>` |
| `/<locale>/<section>/` | Section index (templates, examples) when the locale has one |
| `/<locale>/<section>/<dir>/` | One page |

`<locale>` is any directory name under `locales/` that is in `LOCALES`
(see [locales.md](locales.md)); for English it is `en-001`. Search and routing are
specified in [locale-specific-search-picker/](locale-specific-search-picker/index.md).

`/` is the language router: a prerendered static page whose script reads
`navigator.languages` and replaces itself (no extra history entry) with the
visitor's locale route, via `routeForLanguages()` in `src/lib/locales.js`. For
each preference, most preferred first, the first rule that matches wins:

1. the exact locale: `cy_GB` or `cy-GB` goes to `/cy-gb/`, `zh-TW` to `/zh-tw/`,
   `en-US` to `/en-us/`;
2. Chinese by script or region: `zh-Hant`, `zh-HK`, `zh-MO` go to `/zh-tw/`,
   `zh-Hans` to `/zh-cn/`;
3. the language's international `*-001` locale: `en-AU` goes to `/en-001/`,
   `de-DE`, `fr-CA`, `pt-BR`, `fi` go to `/de-001/`, `/fr-001/`, `/pt-001/`,
   `/fi-001/`.

A preference that matches nothing is skipped, and with no match at all the
visitor goes to `/en-001/`. Without JavaScript (and for crawlers) `/` stays a
static page with a link to `/en-001/`, which is its canonical URL.

## Locale landing page

`/<locale>/` renders the locale's root `index.md`, its translated README
([locales.md](locales.md#root-index-the-translated-readme)), loaded by
`landingOf()` in `src/lib/server/locale-pages.js`:

- **Hero**: the README's `#` title (headline), a one-sentence subheadline, the README's first paragraph (introduction), and a "Translations: " sentence listing every locale's endonym as a link to `/<locale>/`. The subheadline and the translated "Translations" label are hand-authored in `src/lib/data/hero.js`.
- **Six cards**, linking to anchors further down the same page: the sections "What
  is an ADR?", "How to start using ADRs", "Suggestions for writing good ADRs",
  "ADR example templates", "Teamwork advice for ADRs", and "Fitness functions"
  (sections 1, 2, 7, 8, 9 and 13 of the 15). A card shows the section's title
  and its first prose paragraph (its first list item when it has none), clipped
  to about 170 characters.
- **Body**: the rest of the README, rendered with `marked` (GitHub alert markers
  such as `> [!IMPORTANT]` are dropped), with relative links resolved to site
  URLs.

With a query (`/<locale>/?<query>`) the hero, cards and body are replaced by
search results. A locale without a root `index.md` falls back to a plain list of
its pages. English variants `en-gb` and `en-us` are `noindex`. Cards use the
theme's `.card-grid`, `.card`, and `.intro` styles.

## Accessibility

The site is checked with axe-core (WCAG 2.2 AA and best-practice rules; `pnpm run a11y`, run by CI) and passes
with zero violations on the home router, landing pages, documents, templates,
examples, and search results, in left-to-right and right-to-left locales, at
desktop and 390px widths. Rules that keep it so:

- **Contrast in every theme.** The 45 Lily themes differ widely, and their accent
  (`--color-primary`) and "muted" text colours fail AA contrast in about half of
  them. Links and card titles therefore use the theme's text colour
  (`--color-base-content`), underlined; muted-looking paragraphs use the same
  colour. Do not reintroduce `--color-primary` or `--lily-text-muted` for text.
  Verified on all 45 themes (landing page and a document).
- **Phone search.** At 40rem and below, the search field opens over the row of
  picker buttons, full width, inside the header (`src/lib/styles/theme.css`, plain
  class selectors; the theme positions the panel inside `:where()`, so they win),
  and the other pickers are hidden only while it is open.
- **Keyboard.** Tab order follows the visual order; Enter opens search with the field
  focused, Enter submits, Escape closes it and returns focus to the button. Code
  blocks (`<pre>`) have `tabindex="0"` because they scroll sideways on narrow screens.

## Generated vs hand-authored

| Path | Kind |
|---|---|
| `src/routes/+page.svelte` | Hand-authored; the `/` language router |
| `src/lib/components/Header.svelte` | Hand-authored; picker bar and search wiring |
| `src/content/locales/` (pages and each locale's root `index.md`), `src/lib/locale-pages.json`, `src/lib/locale-peers.json`, `src/lib/locale-sections.json` | Generated by `scripts/sync-locales.mjs` from `locales/` (run by `content`); committed; translated pages per locale |
| `static/search/<locale>.json` | Generated by `scripts/generate-search-index.mjs` from `locales/` (run by `content`); committed; one file per locale |
| `src/lib/locales.js` | Hand-authored; picker locale list and slug rules |
| `static/sitemap.xml` | Generated by `scripts/generate-sitemap.mjs` from `src/lib/locale-pages.json` (all URLs end in `/`); never hand-edit |
| `static/llms.txt`, `static/llms.json` | Generated by `scripts/generate-llms.mjs` from the `en-001` pages, template index and root README, and `LOCALES` in `src/lib/locales.js`; never hand-edit |

Every page is a locale page copied from `locales/<code>/` by `scripts/sync-locales.mjs`;
there is no separate English content pipeline (English is `en-001`).

Everything the built site needs must live inside the site directory; nothing
may reference `../` at runtime, because the directory is published alone.

## Commands

`pnpm run content` regenerates content and manifest. `pnpm run check` must
report 0 errors before committing changes to `src/`. `pnpm run build`
produces `build/`.

## Dependencies

- `typescript` stays on 6.x; SvelteKit 3 requires TypeScript's JS API, which
  7.x lacks.
- `@lilydesignsystem/*` packages track latest; pnpm's release-age policy may
  hold back versions younger than about a day.

## Themes

`static/themes/<id>.css` are Lily's own generated theme files (45), copied
unmodified from
`https://raw.githubusercontent.com/lilydesignsystem/lilydesignsystem/main/themes/<id>.css`.
Refresh all 45 whenever `@lilydesignsystem/*` packages are upgraded: a package
that adds elements (e.g. `*-picker-tooltip`, `search-picker-*` in picker-bar
0.2.0, `link-picker-*` in picker-bar 0.3.0) is unstyled by older theme files, which breaks the header layout. Do
not hand-edit them; site-specific styles go in `src/lib/styles/theme.css`.

## Link picker

The picker bar's leftmost button is Lily's link picker (a home icon, picker-bar 0.3.0).
It opens four links: **Home** (the locale's landing page), **Templates** and
**Examples** (the locale's section indexes), and **GitHub** (the repository, in a new
tab). Hrefs follow the locale being viewed, because section directory names are
translated: `src/lib/locale-sections.json` (generated by `sync-locales.mjs`; locale to
`{templates, examples}` directory) supplies them. The current page is marked
`aria-current="page"`, and a plain click navigates client-side with `goto`. The labels
are English, like the other picker labels. The text links in the header nav
(Documents, Templates, Examples, GitHub) are separate.

## Language picker

Choosing a locale sets `lang`/`dir` on `<html>`, persists the choice in
`localStorage` (`adr-locale`), and **navigates to the same page in that
locale**:

- Pages are matched through the shared `.locale-peer-id` of each page
  (`src/lib/locale-peers.json`, generated by `scripts/sync-locales.mjs`;
  loaded only when a locale is chosen). `src/lib/locale-nav.js` implements it.
- From any locale's page (English is `en-001`), the target is `/<slug>/<section>/<dir>/` in
  the chosen locale.
- Choosing English (`en`) is like any locale: it goes to the `en-001` page, or `/en-001/`.
- If the chosen locale has no equivalent page (a locale that lacks that page), or the
  current page is not a content page (home, skills), it goes to `/<slug>/`,
  the locale's contents page.
- Only a user selection navigates. The picker's initial call must not, so a
  fresh load never redirects.
- `en` and `en_001` are one entry ("English"); `en_001` is not listed.
- The picker shows the language of the page being viewed: on a locale route
  (`/de-001/...`) its value is that locale, so a shared link shows it (and
  persists it as the stored choice); on every English-site page it is
  `English`. A value that matches the URL's own locale never triggers
  navigation; only a user selection does. The server-rendered HTML already
  carries the right value.

Search goes to `/<locale>/?<query>` (see
[locale-specific-search-picker/](locale-specific-search-picker/index.md)).
Entries follow [locales.md](locales.md#picker-labels).

## Publishing

```sh
git subtree push --prefix=architecture-decision-record.github.io \
  git@github.com:architecture-decision-record/architecture-decision-record.github.io.git main
```
