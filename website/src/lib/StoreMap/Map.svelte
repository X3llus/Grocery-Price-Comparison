<script>
	import { onDestroy, setContext, beforeUpdate } from 'svelte';
	import { kmToPixels } from '$lib/utils';
	import { mapbox, key } from './mapbox.js';
	import { userLocation, searchRadius } from '$lib/stores';

	setContext(key, {
		getMap: () => map,
	});

	let zoom = 10;
	let container;
	let map;

	$: radiusInPixels = kmToPixels($userLocation.latitude, zoom, $searchRadius);

	function load() {
		map = new mapbox.Map({
			container,
			style: 'mapbox://styles/mapbox/streets-v12',
			center: [$userLocation.longitude, $userLocation.latitude],
			zoom,
			minZoom: 6,
			maxZoom: 12,
		});

		map.addControl(
			new mapbox.NavigationControl({
				showCompass: false,
				visualizePitch: false,
			})
		);

		map.addControl(new mapbox.GeolocateControl());

		map.on('load', () => {
			// Circle to represent the search radius
			map.addLayer({
				id: 'search-radius',
				type: 'circle',
				source: {
					type: 'geojson',
					data: {
						type: 'Feature',
						geometry: {
							type: 'Point',
							coordinates: [$userLocation.longitude, $userLocation.latitude],
						},
					},
				},
				paint: {
					'circle-radius': radiusInPixels,
					'circle-color': '#007cbf',
					'circle-opacity': 0.3,
					'circle-stroke-width': 2,
					'circle-stroke-color': '#007cbf',
					'circle-stroke-opacity': 0.75,
				},
			})
		})

		map.on('zoom', () => {
			zoom = map.getZoom();
		});
		map.resize();
	}

	beforeUpdate(() => {
		if (map && map.isStyleLoaded()) {
			map.setPaintProperty('search-radius', 'circle-radius', radiusInPixels);
		}
	})

	onDestroy(() => {
		if (map) {
			map.remove();
		}
	});
</script>

<svelte:head>
	<link rel="stylesheet" href="https://unpkg.com/mapbox-gl/dist/mapbox-gl.css" on:load={load} />
</svelte:head>

<div bind:this={container}>
	{#if map}
		<slot />
	{/if}
</div>

<style>
	div {
		width: 100%;
		height: 100%;
	}
</style>
