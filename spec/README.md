# Specification

Single source of truth for the Architecture Decision Record repository.
Everything else (READMEs, `AGENTS.md`, skills, `llms.txt`, the website) must
agree with these files; when they disagree, fix them to match the spec, or
change the spec first.

| File | Governs |
|---|---|
| [repository.md](repository.md) | Directory layout, file conventions, counts |
| [content.md](content.md) | Documents, templates, examples: what must exist and how it is written |
| [locales.md](locales.md) | Locale codes, directory-name translation, translation workflow, locale list |
| [website.md](website.md) | The SvelteKit site: build, generated files, picker, publishing |
| [locale-specific-search-picker/](locale-specific-search-picker/index.md) | Per-locale site search: picker form, `/<locale>/?<query>` route, per-locale index |
| [agents.md](agents.md) | Skills, `llms.txt`, `AGENTS.md` rules for AI agents |

Counts in this spec (12 documents, 11 templates, 40 examples, 89 locales)
are verified by the checks listed in [repository.md](repository.md#verification).
