<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import Magnify from 'svelte-material-icons/Magnify.svelte';
	import Cart from 'svelte-material-icons/Cart.svelte';
	import MapMarker from 'svelte-material-icons/MapMarker.svelte';
	import Modal from '$lib/Modal.svelte';
	import StoreMap from '$lib/StoreMap/StoreMap.svelte';
	import { userLocation, updateUserLocation } from '$lib/stores';
	import algoliasearch from 'algoliasearch/lite';
	import { goto } from '$app/navigation';
	import { searchStore } from '$lib/searchStore';

	$: q = $page.url.searchParams.get('q') || '';

	let search = '';
	let sideOpen = false;
	let locationModalOpen = false;
	const client = algoliasearch(
		import.meta.env.VITE_ALGOLIA_APP_ID,
		import.meta.env.VITE_ALGOLIA_SEARCH_KEY
	);
	const index = client.initIndex('ITEMS');

	onMount(async () => {
		// saves the user's location to the store & local storage
		// then, since localStores is a derived store, it will trigger an update for the localStores
		await updateUserLocation();
		if (q) {
			search = q;
			searchItems();
		}
	});

	const toggleLocationModal = () => {
		locationModalOpen = !locationModalOpen;
	};

	async function searchItems() {
		let hits = await index.search(search, {
			hitsPerPage: 25
		});
		console.log(hits);
		searchStore.set(hits.hits);

		$page.url.searchParams.set('q', search);
		goto(`?${$page.url.searchParams.toString()}`);
		
	}
</script>

<!-- Slide Menu -->
<div
	class="fixed right-0 top-0 h-screen transition-transform z-30 w-80"
	style="transform: translateX({sideOpen ? '0%' : '100%'});"
>
	<div class="h-full bg-background">
		<h2 class="text-2xl text-black py-4 w-full text-center">List/Cart</h2>
	</div>
</div>

{#if sideOpen}
	<div
		class="fixed top-0 left-0 w-full h-full bg-black opacity-50 z-20"
		on:click={() => (sideOpen = false)}
		on:keypress={() => (sideOpen = false)}
	/>
{/if}

<!-- Main Nav Bar -->
<div
	class="fixed left-0 top-0 w-screen z-10 p-1 md:p-4 flex space-x-2 md:space-x-4 bg-primary shadow-lg"
>
	<!-- <button on:click={() => (sideOpen = !sideOpen)}>
		<div class="space-y-2">
			<div class="w-8 h-1 bg-white rounded-sm" />
			<div class="w-8 h-1 bg-white rounded-sm" />
			<div class="w-8 h-1 bg-white rounded-sm" />
		</div>
	</button> -->
	<h1 class="text-3xl text-white leading-normal"><a href="/">Groceriez</a></h1>
	<div class="flex flex-1">
		<form on:submit|preventDefault={() => searchItems()} class="flex p-2 rounded-lg flex-1">
			<input
				bind:value={search}
				class="p-2 rounded-l-lg w-3/4 border-y border-l-2 border-accent shadow-md bg-gradient-to-b focus:outline-none"
				placeholder="Search our Products"
			/>
			<button
				type="submit"
				class="p-2 rounded-r-lg border-y border-r-2 border-accent bg-accent bg-grad shadow-md w-16 flex justify-center"
			>
				<Magnify color={'white'} width={24} height={24} />
			</button>
		</form>
		<div class="flex flex-col justify-center">
			<button
				class="flex-initial mx-14 flex hover:cursor-pointer text-white font-medium"
				on:click|stopPropagation={toggleLocationModal}
				on:keypress|stopPropagation={toggleLocationModal}
				aria-label="Change Location"
			>
				<div class="flex flex-col justify-center"><MapMarker width={22} height={22} /></div>
				<div class="flex flex-col items-start">
					<span>{$userLocation.city}, {$userLocation.province}</span>
					<span class="text-xs">Change Location</span>
				</div>
			</button>
		</div>
	</div>
	<button
		class="rounded-full bg-white w-12 h-12 flex justify-center items-center"
		on:click={() => (sideOpen = !sideOpen)}
		aria-label="Cart"
	>
		<Cart color={'black'} width={24} height={24} />
	</button>
</div>

<!-- Location Modal -->
<Modal visible={locationModalOpen} onClose={toggleLocationModal}>
	<span slot="title">Change Location</span>
	<span slot="subtitle">Click and drag the marker to set a new location</span>
	<StoreMap />
</Modal>

<div class="z-0 w-screen h-screen pt-20 bg-background">
	<slot />
</div>
