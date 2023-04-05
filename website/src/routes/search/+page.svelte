<script lang="ts">
	import { searchListStore, searchStore } from '$lib/searchStore';
	import { onDestroy } from 'svelte';
	import { SearchCard } from '$lib/components';

	let hits = [];

	searchStore.subscribe((value) => {
		if (value.length === 0) return;
		hits = value;
	});

	function addToList(event) {
        const updateList = (value) => [
            ...value,
            { ...hits[event.detail.i], quanity: 1, best: [event.detail.best] },
        ];

        if ($searchListStore.length === 0) {
            return searchListStore.add(updateList);
        }

        const foundIndex = $searchListStore.findIndex(
            (element) => element.objectID === hits[event.detail.i].objectID
        );

        if (foundIndex >= 0) {
            $searchListStore[foundIndex].quanity++;
            searchListStore.add((value) => value);
        } else {
            searchListStore.add(updateList);
        }
    }

	onDestroy(() => {
		hits = [];
		searchStore.set([]);
	});
</script>

<svelte:head>
	<title>Groceriez | Search</title>
</svelte:head>

<div
	class="mx-auto pb-10 w-2/3 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5 gap-10 pt-20 place-content-center"
>
	{#each hits as hit, i}
		<SearchCard {hit} {i} on:product={addToList} />
	{/each}
</div>
