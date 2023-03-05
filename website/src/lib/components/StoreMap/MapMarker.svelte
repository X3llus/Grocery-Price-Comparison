<script>
	import { getContext } from 'svelte';
	import { mapbox, key } from './mapbox.js';
	import { updateUserLocation } from '../../stores';
	import { getMapIcon } from '$lib/utils';

	const { getMap } = getContext(key);
	const map = getMap();

	export let lat;
	export let lon;
	export let type;
	export let address = null;
	export let draggable = false;

	const popup = new mapbox.Popup({ offset: 25 })

	if (address) {
		// TODO: add styling to the popup
		popup.setHTML(`<h3>${type}</h3><p>${address}</p>`);
	} else {
		popup.setHTML(`<h3>${type}</h3>`)
	}

	let marker;

	if (type === 'You') {
		marker = new mapbox.Marker({ draggable })
	} else {
		const { file, width, height } = getMapIcon(type);
		const el = document.createElement('div');
		el.className = 'marker';
		el.style.backgroundImage = `url(${file})`;
		el.style.width = `${width}px`;
		el.style.height = `${height}px`;
		el.style.backgroundSize = 'cover';
		marker = new mapbox.Marker(el)
	}

	marker.setLngLat([lon, lat])
			.setPopup(popup)
			.addTo(map);

	const onDragEnd = async () => {
		const lngLat = marker.getLngLat();

		// Update the radius circle position
		map.getSource('search-radius').setData({
			type: 'Feature',
			geometry: {
				type: 'Point',
				coordinates: [lngLat.lng, lngLat.lat],
			},
		});

		await updateUserLocation({
			latitude: lngLat.lat,
			longitude: lngLat.lng
		});
	};

	if (draggable) {
		marker.on('dragend', onDragEnd);
	}
</script>