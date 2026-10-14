// Picker locale values (sorted by code). A value is "ll_RR" (or bare "en");
// its URL slug and source directory under ../locales/ is the lowercase form
// with "_" replaced by "-" ("de_001" -> "de-001"). The bare "en" has no
// directory of its own and maps to the source-of-truth locale "en-001" (so
// "en_001" is not listed separately: it would be a duplicate "English").
// See spec/locale-specific-search-picker/index.md.
export const LOCALES = [
	'ar_001', 'bg_001', 'bg_BG', 'bn_001', 'cs_001', 'cs_CZ', 'cy_001', 'cy_GB', 'da_001', 'da_DK', 'de_001', 'de_AT',
	'de_DE', 'el_001', 'el_CY', 'el_GR', 'en', 'en_GB', 'en_IE', 'en_US', 'es_001', 'es_ES', 'et_001', 'et_EE',
	'fi_001', 'fi_FI', 'fr_001', 'fr_FR', 'fr_LU', 'hi_001', 'hi_IN', 'hu_001', 'hu_HU', 'id_001', 'id_ID', 'is_001',
	'is_IS', 'it_001', 'it_IT', 'ja_001', 'ja_JP', 'ko_001', 'ko_KR', 'nl_001', 'nl_BE', 'nl_NL', 'pl_001', 'pl_PL',
	'pt_001', 'pt_PT', 'ro_001', 'ro_RO', 'ru_001', 'sv_001', 'sv_SE', 'sw_001', 'sw_TZ', 'th_001', 'th_TH', 'tr_001',
	'tr_TR', 'ur_001', 'vi_001', 'vi_VN', 'zh_001', 'zh_CN', 'zh_TW'
];

export const DEFAULT_LOCALE = 'en';

/** @param {string} value picker locale value @returns {string} URL slug */
export function localeToSlug(value) {
	if (!value || value === 'en') return 'en-001';
	return value.toLowerCase().replace(/_/g, '-');
}

/** Every URL slug that has a locale route, deduplicated. */
export const LOCALE_SLUGS = [...new Set(LOCALES.map(localeToSlug))];

/** BCP 47 tag for a slug ("zh-tw" -> "zh-TW", "de-001" -> "de-001"). @param {string} slug */
export function slugToTag(slug) {
	const [lang, region] = slug.split('-');
	return region ? `${lang}-${region.length === 2 ? region.toUpperCase() : region}` : lang;
}

const RTL = new Set(['ar', 'ur', 'he', 'fa']);
/** @param {string} slug */
export function isRtlSlug(slug) {
	return RTL.has(slug.split('-')[0]);
}

/**
 * The route to send a visitor to, from the browser's language preferences
 * (`navigator.languages`, most preferred first). Used by the "/" page.
 *
 * Per preference, the first rule that matches wins:
 *  1. the exact locale ("cy_GB" or "cy-GB" -> "cy-gb", "zh-TW" -> "zh-tw");
 *  2. Chinese by script or region ("zh-Hant", "zh-HK", "zh-MO" -> "zh-tw"; "zh-Hans" -> "zh-cn");
 *  3. the language's international *-001 locale ("en-AU", "de-DE", "pt-BR", "fi" -> "en-001", "de-001", "pt-001", "fi-001").
 * Preferences that match nothing are skipped; with no match at all the result
 * is "/en-001/". See spec/website.md.
 * @param {readonly string[]} languages
 * @returns {string} a path such as "/cy-gb/" or "/en-001/"
 */
export function routeForLanguages(languages) {
	for (const raw of languages) {
		const parts = String(raw).trim().replace(/_/g, '-').toLowerCase().split('-').filter(Boolean);
		const lang = parts[0];
		if (!lang) continue;
		const script = parts.find((p, i) => i > 0 && /^[a-z]{4}$/.test(p));
		const region = parts.find((p, i) => i > 0 && /^([a-z]{2}|\d{3})$/.test(p));

		if (region && LOCALE_SLUGS.includes(`${lang}-${region}`)) return `/${lang}-${region}/`;
		if (lang === 'zh' && (script === 'hant' || region === 'hk' || region === 'mo')) return '/zh-tw/';
		if (lang === 'zh' && script === 'hans') return '/zh-cn/';
		if (LOCALE_SLUGS.includes(`${lang}-001`)) return `/${lang}-001/`;
	}
	return '/en-001/';
}
