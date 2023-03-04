<script lang="ts">
	import { onDestroy } from 'svelte';
	import { tweened } from 'svelte/motion';
	import { cubicOut } from 'svelte/easing';
	import Map from './Map.svelte';
	import MapMarker from './MapMarker.svelte';
	import { userLocation, searchRadius, localStores } from '$lib/stores';

	let numStores = 0;
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
</script>

<svelte:head>
	<link href="https://api.mapbox.com/mapbox-gl-js/v2.8.1/mapbox-gl.css" rel="stylesheet" />
</svelte:head>

<div class="container">
		<div class="info-container">
			<div class="radius-container">
				<p style="font-size: 1.2rem">Search radius: <span style="font-size: 1.25rem; font-weight: 600">{$searchRadius}km</span></p>
				<div style="display: flex; align-items: flex-end">
					<label for="radius" style="margin-right: 0.5rem; font-size: 0.85rem; align-self: flex-start">Set radius</label>
					<input
						type="range"
						bind:value={$searchRadius}
						min="3"
						max="75"	
					>
				</div>
			</div>
			{#if numStores > 0}
				<p class="store-counter">
					<span style="font-weight: 600">{Math.round($animatedNumStores)}</span>
					 stores selected for comparison
				</p>
			{:else}
				<p class="store-counter" style="font-weight: 600; color: red">No stores selected for comparison</p>
			{/if}
		</div>
	<Map>
		<MapMarker lat={$userLocation.latitude} lon={$userLocation.longitude} draggable={true} type="You" />
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
		justify-content: space-between;
		align-items: center;
		padding: 1rem;
	}

	.radius-container {
		display: flex;
		flex-direction: column;
	}

	.store-counter {
		font-size: 1.25rem;
	}

	@media screen and (max-width: 500px) {
		.info-container {
			padding: 0 0.5rem 0.25rem 0.5rem;
		}

		.store-counter {
			font-size: 1rem;
			margin-left: 1rem;
		}
	}
</style>
