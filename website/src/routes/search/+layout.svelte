<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import Magnify from 'svelte-material-icons/Magnify.svelte';
	import ListBox from 'svelte-material-icons/ListBox.svelte';
	import MapMarker from 'svelte-material-icons/MapMarker.svelte';
	import Arrow from 'svelte-material-icons/ArrowRight.svelte';
	import Account from 'svelte-material-icons/Account.svelte';
	import { Modal, StoreMap } from '$lib/components';
	import { userLocation, updateUserLocation, searchRadius } from '$lib/stores';
	import algoliasearch from 'algoliasearch/lite';
	import { goto } from '$app/navigation';
	import { searchListStore, searchStore } from '$lib/searchStore';
	import { CartCard } from '$lib/components';
	import { get } from 'svelte/store';
	import { browser } from '$app/environment';

	$: q = $page.url.searchParams.get('q') || '';

	let search = '';
	let sideOpen = false;
	let locationModalOpen = false;
	const client = algoliasearch(
		import.meta.env.VITE_ALGOLIA_APP_ID,
		import.meta.env.VITE_ALGOLIA_SEARCH_KEY
	);
	const index = client.initIndex('Products');

	onMount(async () => {
		// saves the user's location to the store & local storage
		// then, since localStores is a derived store, it will trigger an update for the localStores
		await updateUserLocation();
		if (q) {
			search = q;
			searchItems();
		}
		console.log(get(searchListStore));
	});

	const toggleLocationModal = () => {
		locationModalOpen = !locationModalOpen;
	};

	async function searchItems() {
		let hits = await index.search(search + ' ', {
			hitsPerPage: 30,
			aroundLatLng: `${$userLocation.latitude}, ${$userLocation.longitude}`,
			aroundRadius: $searchRadius * 1000,
		});

		if (typeof hits.hits == 'object') {
			hits.hits = [hits.hits];
		}
		searchStore.set(hits.hits);

		$page.url.searchParams.set('q', search);
		goto(`?${$page.url.searchParams.toString()}`);
	}

	let screenSize;
	let screenSmall = 640;
</script>

<svelte:window bind:innerWidth={screenSize} />

<!-- Slide Menu -->
{#if browser}
<div
	class="fixed right-0 top-0 h-screen transition-transform z-30 sm:w-96 w-screen"
	style="transform: translateX({sideOpen ? '0%' : '100%'});"
>
	<div class="h-full bg-background flex flex-col">
		<div class="grid grid-cols-3">
			<button class="ml-2" on:click={() => (sideOpen = !sideOpen)}>
				<Arrow color={'black'} width={32} height={32} />
			</button>
			<h2 class="text-4xl font-semibold text-black py-4 w-full text-center">List</h2>
		</div>
		<ul class="flex-1 space-y-2 p-2 overflow-auto overscroll-contain">
			{#each $searchListStore as item, i}
				<CartCard item={item} i={i} />
			{/each}
		</ul>
		<div class="text-3xl p-8 flex justify-between">
			<span>Total Price:</span>
			<!-- Gets the sum of prices for all items *needs to multiply price by the quantity before it is added-->
			<span
				>${((list) => {
					return list.reduce((m, v) => m + +v.data[0].price*v.quanity, 0);
				})($searchListStore).toFixed(2)}</span
			>
		</div>
	</div>
</div>
{/if}

{#if sideOpen}
	<div
		class="fixed top-0 left-0 w-full h-full bg-black opacity-50 z-20"
		on:click={() => (sideOpen = false)}
		on:keypress={() => (sideOpen = false)}
	/>
{/if}
<!-- Slide Menu End -->

<!-- Main Nav Bar -->
<div
	class="fixed left-0 top-0 w-screen z-10 py-1 px-4 md:py-4 md:px-6 flex space-x-2 md:space-x-4 bg-primary shadow-lg items-center"
>
	{#if screenSize > screenSmall}
		<h1 class="text-3xl text-white leading-normal"><a href="/">Groceriez</a></h1>
	{:else}
		<h1 class="text-3xl text-white leading-normal"><a href="/">G</a></h1>
	{/if}
	<div class="flex grow">
		<form on:submit|preventDefault={() => searchItems()} class="flex p-2 rounded-lg flex-1">
			<input
				bind:value={search}
				class="p-2 rounded-l-lg w-3/4 border-y border-l-2 border-accent shadow-md bg-gradient-to-b focus:outline-none grow md:grow-0"
				placeholder="Search our Products"
			/>
			<button
				type="submit"
				class="p-2 rounded-r-lg border-y border-r-2 border-accent bg-accent bg-grad shadow-md md:w-16 flex justify-center"
			>
				<Magnify color={'white'} width={24} height={24} />
			</button>
		</form>
	</div>
	{#if screenSize > screenSmall}
		<div class="flex flex-col justify-center">
			<button
				class="flex-initial flex hover:cursor-pointer text-white font-medium md:mx-14"
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
		<a
			class="rounded-full bg-white w-12 h-12 flex justify-center items-center"
			href="/signin"
			aria-label="Account"
		>
			<Account color={'black'} width={24} height={24} />
	</a>
	{:else}
		<div class="flex flex-col justify-center">
			<button
				class="flex-initial flex hover:cursor-pointer text-white font-medium md:mx-14"
				on:click|stopPropagation={toggleLocationModal}
				on:keypress|stopPropagation={toggleLocationModal}
				aria-label="Change Location"
			>
				<div
					class="flex flex-col justify-center"
					title="{$userLocation.city}, {$userLocation.province}"
				>
					<MapMarker width={22} height={22} />
				</div>
			</button>
		</div>
		<a href="/signin" aria-label="Cart">
			<Account color={'white'} width={24} height={24} />
		</a>
	{/if}
</div>

<!-- Location Modal -->
<Modal visible={locationModalOpen} onClose={toggleLocationModal}>
	<span slot="title">Change Location</span>
	<StoreMap closeModal={toggleLocationModal} />
</Modal>

<div class="z-0 min-h-screen pt-20 bg-background">
	<slot />
</div>

<button
	class="fixed bottom-4 right-4 rounded-full bg-primary w-12 h-12 flex justify-center items-center"
	on:click={() => (sideOpen = !sideOpen)}
	aria-label="Cart"
>
	<ListBox color={'white'} width={24} height={24} />
</button>
