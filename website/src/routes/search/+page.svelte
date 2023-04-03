<script>
	import { searchListStore, searchStore } from '$lib/searchStore';
	import { getDoc, doc, db, rtdb, ref, child, get } from '$lib/firebase.js';
	import { onDestroy } from 'svelte';

	let hits = [];

	searchStore.subscribe((value) => {
		if (value.length === 0) return;
		console.log(value);
		hits = value[0];
	});

	function addToList(i) {
		console.log(hits[i]);
		searchListStore.add(hits[i]);
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
		<!-- Card Design -->
		<div class="w-full border rounded-md shadow-lg overflow-hidden group bg-white">
			<img src={hit.imageUrl} alt={hit.name} class="w-full" />
			<div class="p-5">
				<h2
					class="truncate text-primary text-xl font-sans font-medium group-hover:text-black"
					data-tooltip-target="title"
					data-tooltip-placement="bottom"
					title="{hit.name}"
				>
					{hit.name}
				</h2>
				{#if hit.brand}
					<h2
						class="truncate text-secondary text-sm font-sans font-bold"
						data-tooltip-target="title"
						data-tooltip-placement="bottom"
					>
						{hit.brand}
					</h2>
				{/if}
				<div class="border m-1" />
				<!-- <div class="p-1">
					<div class="flex justify-between">
						<h3 class="text-rich-black font-medium text-md">Store</h3>
						<h3 class="text-rich-black font-medium text-md">{hit.parentCompany}</h3>
					</div>
				</div> -->
				{#if hit.size}
					<div class="p-1">
						<div class="flex justify-between">
							<h3 class="text-rich-black font-medium text-md">Size</h3>
							<h3 class="text-rich-black font-medium text-md">{hit.size}{hit.unit}</h3>
						</div>
					</div>
				{/if}
				<div class="p-1">
					<div class="flex justify-between">
						<h3 class="text-rich-black font-medium text-md">Price</h3>
						<h3 class="text-rich-black font-medium text-md">${hit.data[0].price}</h3>
					</div>
				</div>
				<button
					class="button bg-primary w-full rounded-xl text-white text-sm font-sans font-medium p-2 flex justify-center shadow-md hover:opacity-90 focus:animate-wiggle"
					on:click={() => addToList(i)}>Add to List</button
				>
			</div>
		</div>
	{/each}
</div>
