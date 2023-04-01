<script>
	import { searchListStore, searchStore } from '$lib/searchStore';
	import { getDoc, doc, db, rtdb, ref, child, get } from '$lib/firebase.js';
	import { onDestroy } from 'svelte';
	import { SearchCard } from '$lib/components';

	let hits = [];

	searchStore.subscribe((value) => {
		if (value.length === 0) return;
		console.log(value);
		hits = value[0];
	});

	function addToList(event) {
		searchListStore.update((value) => [...value, hits[event.detail.i]]);
	}

	onDestroy(() => {
		hits = [];
		searchStore.set([]);
	});
</script>

<svelte:head>
	<title>Groceriez | Search</title>
</svelte:head>

<div class="mx-auto w-2/3 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5 gap-10 pt-20 place-content-center">
	{#each hits as hit, i}
		<SearchCard hit={hit} i={i} on:product={addToList}/>
	{/each}
</div>
