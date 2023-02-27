<script>
	import { onDestroy, setContext, beforeUpdate } from 'svelte';
	import { kmToPixels } from '$lib/utils';
	import { mapbox, key } from './mapbox.js';

	setContext(key, {
		getMap: () => map,
	});

	export let lat;
	export let lon;
	export let radius;
	let zoom = 10;
	let container;
	let map;

	$: radiusInPixels = getRadiusInPixels(lat, zoom, radius);

	const getRadiusInPixels = (lat, zoom, radius) => {
		return kmToPixels(lat, zoom, radius);
	};

	function load() {
		map = new mapbox.Map({
			container,
			style: 'mapbox://styles/mapbox/streets-v12',
			center: [lon, lat],
			zoom,
			minZoom: 8,
			maxZoom: 15,
		});

		map.addControl(
			new mapbox.NavigationControl({
				showCompass: false,
				visualizePitch: false,
			})
		);

		map.addControl(new mapbox.GeolocateControl());

		map.on('load', () => {
			// A dot to represent the user's location
			map.addLayer({
				id: 'user-location',
				type: 'circle',
				source: {
					type: 'geojson',
					data: {
						type: 'Feature',
						geometry: {
							type: 'Point',
							coordinates: [lon, lat],
						},
					},
				},
				paint: {
					'circle-radius': 6,
					'circle-color': '#007cbf',
				},
			})

			// A circle to represent the search radius
			map.addLayer({
				id: 'search-radius',
				type: 'circle',
				source: {
					type: 'geojson',
					data: {
						type: 'Feature',
						geometry: {
							type: 'Point',
							coordinates: [lon, lat],
						},
						properties: {
							radius,
						},
					},
				},
				paint: {
					'circle-radius': radiusInPixels,
					'circle-color': '#007cbf',
					'circle-opacity': 0.3,
					'circle-stroke-width': 1,
					'circle-stroke-color': '#007cbf',
					'circle-stroke-opacity': 0.5,
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
