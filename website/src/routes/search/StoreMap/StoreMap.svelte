<script lang="ts">
	import { onMount } from 'svelte';
	import Map from './Map.svelte';
	import MapMarker from './MapMarker.svelte';
	import type { Store } from '$lib/types';
	import { getLocation } from '$lib/location';
	import { getLocalStores } from './getLocalStores';

	let stores: Store[] = [];
	let radius = 15;
	const userLocation = getLocation();

	onMount(async () => {
		// extend a bit beyond the user's radius to show stores that are just outside
		stores = await getLocalStores(userLocation.latitude, userLocation.longitude, radius + 25);
	});

</script>

<svelte:head>
	<link href="https://api.mapbox.com/mapbox-gl-js/v2.8.1/mapbox-gl.css" rel="stylesheet" />
</svelte:head>

<div class="container">
		<div class="radius-container">
			<label for="radius">Radius</label>
			<input type="range" bind:value={radius}>
		</div>
	{#await stores}
		<div>loading...</div>
	{:then stores}
	<Map lat={userLocation.latitude} lon={userLocation.longitude} radius={radius}>
		{#each stores as store}
			<MapMarker lat={store.geoPoint.latitude} lon={store.geoPoint.longitude} label={store.type} />
		{/each}
	</Map>
	{:catch error}
		<div>{error.message}</div>
	{/await}
</div>

<style>
	.container {
		width: 100%;
		height: 100%;
		display: flex;
		flex-basis: 80%;
		flex-direction: column;
	}

	.radius-container {
		display: flex;
		align-items: center;
		padding: 1rem;
	}

</style>
