<script>
	import { page } from '$app/state';
	import { queryFromSearch } from '#lib/search.js';
	import { isRtlSlug, slugToTag } from '#lib/locales.js';
	import SearchResults from '#lib/components/SearchResults.svelte';
	import { HERO, ENDONYMS } from '#lib/data/hero.js';

	let { data } = $props();

	const slug = $derived(data.locale);
	const rtl = $derived(isRtlSlug(slug));
	const hero = $derived(HERO[slug]);
	// location.search exists only in the browser; prerendering shows the contents.
	let query = $state('');
	$effect(() => {
		query = queryFromSearch(page.url.search);
	});
</script>

<svelte:head>
	<title>{query ? `${query} · ${slug}` : slug}</title>
	{#if query || slug === 'en-gb' || slug === 'en-us'}<meta name="robots" content="noindex" />{/if}
</svelte:head>

<section class="locale-search" lang={slugToTag(slug)} dir={rtl ? 'rtl' : 'ltr'}>
	{#if query}
		<h1>{query}</h1>
		<p class="locale-label">{slug}</p>
		<SearchResults {slug} />
	{:else if data.landing}
		<div class="intro">
			<h1>{data.landing.hero.title}</h1>
			{#if hero}<p class="hero-subheadline">{hero.tagline}</p>{/if}
			<p>{data.landing.hero.text}</p>
			{#if hero}
				<p class="hero-translations">
					{hero.translations}{#each Object.entries(ENDONYMS).filter(([c]) => c.endsWith('-001')) as [code, name], i (code)}{i ? ', ' : ''}<a
							href="/{code}/"
							lang={slugToTag(code)}
							aria-current={code === slug ? 'page' : undefined}>{name}</a
						>{/each}
				</p>
			{/if}
		</div>
		<ul class="card-grid landing-cards">
			{#each data.landing.cards as card (card.href)}
				<li class="card">
					<a class="card-title" href={card.href}>{card.title}</a>
					{#if card.text}<p class="card-description">{card.text}</p>{/if}
				</li>
			{/each}
		</ul>
		<div class="prose">{@html data.landing.html}</div>
	{:else}
		<h1>{slug}</h1>
		{#each data.sections as section (section.dir)}
			<h2>
				{#if section.hasIndex}<a href="/{slug}/{section.dir}/">{section.title}</a>{:else}{section.title}{/if}
			</h2>
			<ul>
				{#each section.pages as page (page.dir)}
					<li><a href="/{slug}/{section.dir}/{page.dir}/">{page.title}</a></li>
				{/each}
			</ul>
		{/each}
	{/if}
</section>

<style>
	.hero-subheadline {
		font-size: 1.25em;
		font-weight: 600;
	}
	.hero-translations {
		font-size: 0.9em;
	}
	.hero-translations a[aria-current='page'] {
		font-weight: 700;
		text-decoration: none;
	}
</style>
