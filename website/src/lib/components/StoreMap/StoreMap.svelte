<script lang="ts">
	import { onDestroy } from 'svelte';
	import { tweened } from 'svelte/motion';
	import { cubicOut } from 'svelte/easing';
	import MapMarkerIcon from 'svelte-material-icons/MapMarker.svelte';
	import Map from './Map.svelte';
	import MapMarker from './MapMarker.svelte';
	import { userLocation, searchRadius, localStores, updateUserLocation } from '$lib/stores';
	import { PUBLIC_MAPBOX_ACCESS_TOKEN } from '$env/static/public';

	let screenSize;
	let numStores = 0;
	let autoFillResponse = null;
	const animatedNumStores = tweened(numStores, {
		duration: 600,
		delay: 0,
		easing: cubicOut,
	});

	const unsubscribe = localStores.subscribe(async (stores) => {
		const activeStores = await stores;
		numStores = activeStores.length;
		animatedNumStores.set(numStores);
	});

	onDestroy(() => {
		unsubscribe();
	});

	const initAutofill = () => {
		const elements = document.querySelectorAll('mapbox-address-autofill');
		for (const autofill of elements as any) {
			autofill.accessToken = PUBLIC_MAPBOX_ACCESS_TOKEN;

			autofill.addEventListener('retrieve', (event) => {
				try {
					const featureCollection = event.detail;
					const { properties, geometry } = featureCollection.features[0];
					const city = properties.place;
					const state = properties.region_code;
					const { coordinates } = geometry;
					const [longitude, latitude] = coordinates;
					autoFillResponse = {
						city,
						state,
						latitude,
						longitude,
					};
				} catch (error) {
					console.error(error);
				}
			});
		}
	};

	const handleAddressClick = async () => {
		if (autoFillResponse) {
			await updateUserLocation(autoFillResponse);
		}
	};
</script>

<svelte:window bind:innerWidth={screenSize} />

<svelte:head>
	<!-- Load a bunch of different Mapbox scripts -->
	<link href="https://api.mapbox.com/mapbox-gl-js/v2.8.1/mapbox-gl.css" rel="stylesheet" />
	<link href="https://api.mapbox.com/mapbox-assembly/v1.3.0/assembly.min.css" rel="stylesheet" />
	<script
		id="search-js"
		defer
		src="https://api.mapbox.com/search-js/v1.0.0-beta.14/web.js"
		on:load={initAutofill}
	></script>
</svelte:head>

<div class="container">
	<div class="info-container">
		<form class="location-input-container">
			<label
				for="input-group-1"
				class="block mb-1 text-xs font-medium text-gray-900 dark:text-white"
			>
				Enter an address
				{#if screenSize > 640}
					or drag the map marker to a new location
				{/if}
				to update store search area
			</label>
			<div class="relative mb-4">
				<div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
					<MapMarkerIcon color={'gray'} width={24} height={24} />
				</div>
				<mapbox-address-autofill>
					<input
						type="text"
						id="mapbox-autofill"
						name="postcode"
						class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
						autocomplete="shipping postal-code"
					/>
				</mapbox-address-autofill>
				<div class="absolute inset-y-0 right-0 flex items-center">
					<button
						type="button"
						class="text-white h-full p-2 rounded-r-lg border-y border-r-2 border-accent bg-blue-400 hover:bg-blue-500 bg-accent bg-grad shadow-md md:w-16 flex justify-center"
						on:click|stopPropagation={handleAddressClick}
					>
						Apply
					</button>
				</div>
			</div>
		</form>
		<div class="radius-container">
			<p style="font-size: 1.1rem; align-self: flex-end;">
				Search radius: <span style="font-size: 1.25rem; font-weight: 600;">{$searchRadius}km</span>
			</p>
			<div style="display: flex; flex-direction: column; margin-left: 1rem">
				<label for="radius" style="margin-right: 0.5rem; font-size: 0.85rem;">Set radius</label>
				<input type="range" bind:value={$searchRadius} min="3" max="75" />
			</div>
		</div>
		{#if numStores > 0}
			<p class="store-counter">
				<span style="font-weight: 600">{Math.round($animatedNumStores)}</span>
				stores selected for comparison
			</p>
		{:else}
			<p class="store-counter" style="font-weight: 600; color: red">
				No stores selected for comparison
			</p>
		{/if}
	</div>
	<Map>
		<MapMarker
			lat={$userLocation.latitude}
			lon={$userLocation.longitude}
			draggable={true}
			type="You"
		/>
		{#await $localStores then localStores}
			{#each localStores as store}
				<MapMarker
					lat={store.geoPoint.latitude}
					lon={store.geoPoint.longitude}
					type={store.type}
					address={store.address.formattedAddress}
				/>
			{/each}
		{/await}
	</Map>
</div>

<style>
	.container {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
	}

	.info-container {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		align-items: center;
		padding: 0.5rem 0.5rem 0.1rem 0.5rem;
	}

	.location-input-container {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		width: 80%;
		margin-right: auto;
	}

	.radius-container {
		display: flex;
		width: 100%;
		margin-bottom: 1rem;
	}

	.store-counter {
		font-size: 0.9rem;
		width: 100%;
	}

	@media screen and (max-width: 500px) {
		.info-container {
			padding: 0 0.5rem 0.25rem 0.5rem;
		}

		.store-counter {
			font-size: 1rem;
			margin-left: 1rem;
		}

		.radius-container {
			justify-content: space-around;
		}
	}
</style>
