# Repository

Monorepo `architecture-decision-record`, remotes pushed together by
`git push origin main` (4 push URLs).

## Layout

```
README.md                         canonical English overview (also parsed for the site guide)
spec/                             this specification
skills/                           Claude Code skills (see agents.md)
locales/index.md                  locale index; locales/README.md is a symlink to it
locales/<code>/                   one directory per locale (see locales.md)
architecture-decision-record.github.io/   website, published via git subtree (see website.md)
```

Every directory under `locales/` is named `<language>-<region>` (lowercase, a
hyphen, e.g. `en-001`, `cy-gb`, `zh-tw`); two-letter, region-less directories
such as `locales/en/` do not exist. `en-001` is the English source of truth, so
links to English content use `locales/en-001/`.

## Per-locale layout

Each locale holds three section directories (names translated per
[locales.md](locales.md)): documents, templates, examples. Every content
directory contains `index.md` and a `README.md` that is a **symlink to `index.md`**
(`ln -s index.md README.md`; never a copy, so the two cannot differ). Locale
directories carry `.locale-peer-id` files (67 per locale: one per content
directory plus section and locale roots); these are opaque, copied unchanged
from `locales/en-001`, and never hand-edited. Template `LICENSE.md` files are
copied unchanged and never translated. A new page gets one freshly generated
32-character hex id in `locales/en-001`, copied to its translation in every
locale (the nine newest pages were given ids this way).

Each locale also has a root `index.md` (with a `README.md` symlink): its
translated top-level README, which is the locale's landing page on the website
(see [locales.md](locales.md#root-index-the-translated-readme)).

A complete locale has exactly **205 files**.

## Counts

| Item | Count |
|---|---|
| Documents | 12 |
| Templates | 11 |
| Examples | 40 |
| Locales (hyphenated dirs, incl. `en-001`) | 66 |

## Commits

Commits are SSH-signed. Trailer: `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`
for Claude-assisted commits. Titles are present-tense imperative phrases.

## Delivery: automatically commit, push, publish

When an agent finishes a change, it delivers it without waiting to be asked:

1. **Verify** with the checks below that apply to the change (for site changes,
   `pnpm run check` and `pnpm run build`). If any check fails, stop: do not
   commit, and report the failure.
2. **Commit** the files belonging to the task, staged by path, signed, with
   the trailer above. Do not sweep in unrelated changes; report them instead.
3. **Push** with `git push origin main` (4 push URLs).
4. **Publish** the website with `git subtree push` (see
   [website.md](website.md#publishing)) whenever anything under
   `architecture-decision-record.github.io/` changed in the commit.
5. **Report** the commit hash, the push result, and the subtree range. Do not
   claim the site redeployed unless it was checked.

Limits: never force-push, rewrite history, skip signing or hooks, or delete
remote branches automatically; those still require an explicit request.
If a push or publish fails, stop and report; do not retry destructively.
A user instruction to hold off (for example "don't push yet") overrides this
rule for that task.

## Verification

1. `find locales/<code> \( -type f -o -type l \) | wc -l` is 205 (excluding `.DS_Store`).
2. Every relative link resolves. Known, accepted failures: four `0005-example.md`
   placeholders in the MADR template (`README.md` and `index.md`, two each).
3. Every `#fragment` link matches a heading slug (letters, marks, numbers,
   `-` and `_` kept; spaces become `-`; duplicate headings get `-N`).
4. `python3 scripts/audit-locales.py` exits 0: every locale has every page and file
   (205 files), every `README.md` is a symlink to its `index.md` (the only symlinks allowed), no stray files,
   every slug is translated and clean, and all links and anchors resolve.
5. In the website directory: `pnpm run content` leaves no uncommitted changes (the
   generated files are current), `pnpm test` passes (the `/` language router
   rules), and `pnpm run check` reports 0 errors.
6. After `pnpm run build`, `pnpm run verify` crawls the prerendered pages and
   reports 0 broken links or anchors (the MADR `0005-example.md` sample is the
   only link it ignores).

7. `pnpm run a11y` (after the build) runs axe-core in a browser on key pages at
   desktop and 390px width, with the phone search panel open, and checks colour
   contrast on all 45 themes: 0 violations. Set `PW_CHANNEL=chrome` to use an
   installed Chrome (CI does, so it downloads no browser).

CI (`.github/workflows/ci.yml`) runs checks 4 to 7 on every push to `main` and
every pull request, so a change that breaks any of them is caught before it is
published. Run them locally before committing.
