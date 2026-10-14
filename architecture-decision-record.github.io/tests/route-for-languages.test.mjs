// Unit tests for the "/" language router rules (spec/website.md "URL scheme").
//   pnpm test
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { routeForLanguages as route, localeToSlug, LOCALES, LOCALE_SLUGS } from '../src/lib/locales.js';

const cases = [
	// exact locale, either separator, any case
	[['cy_GB'], '/cy-gb/'],
	[['cy-GB'], '/cy-gb/'],
	[['EN_us'], '/en-us/'],
	[['en-GB'], '/en-gb/'],
	[['hi-IN'], '/hi-in/'],
	[['tr-TR'], '/tr-tr/'],
	[['zh-TW'], '/zh-tw/'],
	[['zh-CN'], '/zh-cn/'],
	// Chinese by script or region
	[['zh-Hant'], '/zh-tw/'],
	[['zh-HK'], '/zh-tw/'],
	[['zh-MO'], '/zh-tw/'],
	[['zh-Hans-CN'], '/zh-cn/'],
	[['zh'], '/zh-001/'],
	// the language's international *-001 locale
	[['en-AU'], '/en-001/'],
	[['en'], '/en-001/'],
	[['de-DE'], '/de-de/'],
	[['de-AT'], '/de-at/'],
	[['de-CH'], '/de-001/'],
	[['pl'], '/pl-001/'],
	[['pl-PL'], '/pl-pl/'],
	[['ro'], '/ro-001/'],
	[['ro-RO'], '/ro-ro/'],
	[['sw-TZ'], '/sw-tz/'],
	[['pt-BR'], '/pt-001/'],
	[['fi'], '/fi-001/'],
	[['es-419'], '/es-001/'],
	[['tr-CY'], '/tr-001/'],
	// first usable preference wins; unmatched ones are skipped
	[['xx', 'fr-CA'], '/fr-001/'],
	[['am', 'am-ET', 'ja'], '/ja-001/'],
	// nothing matches: English
	[['am-ET'], '/en-001/'],
	[['nb-NO'], '/en-001/'],
	[[], '/en-001/'],
	[[''], '/en-001/']
];

for (const [languages, expected] of cases) {
	test(`${JSON.stringify(languages)} -> ${expected}`, () => assert.equal(route(languages), expected));
}

test('every route the router can return is a real locale route', () => {
	for (const [languages] of cases) assert.ok(LOCALE_SLUGS.includes(route(languages).replaceAll('/', '')));
});

test('picker values map to unique, hyphenated slugs', () => {
	assert.equal(localeToSlug('en'), 'en-001');
	assert.equal(localeToSlug('cy_GB'), 'cy-gb');
	assert.equal(new Set(LOCALES.map(localeToSlug)).size, LOCALES.length);
	for (const slug of LOCALE_SLUGS) assert.match(slug, /^[a-z]{2}-[a-z0-9]{2,3}$/);
});
