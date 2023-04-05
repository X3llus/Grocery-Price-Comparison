<script lang="ts">
	import { searchRadius, userLocation } from '$lib/stores';
	import type { Hit, StorePrice } from '$lib/types';
	import { createEventDispatcher } from 'svelte';

	export let hit: Hit;
	export let i: number;
	let best: StorePrice;
	let activePricePopover: number = null;

	const dispatch = createEventDispatcher();

	function addProduct(i: number, best: StorePrice) {
		dispatch('product', { i, best });
	}

	function displayFilter(data: StorePrice[]): StorePrice[] {
		data = data.filter((item) => {
			let distance =
				6371 *
				2 *
				Math.atan2(
					Math.sqrt(
						Math.pow(
							Math.sin((($userLocation.latitude - item._geoloc.lat) * Math.PI) / 180 / 2),
							2
						) +
							Math.cos((item._geoloc.lat * Math.PI) / 180) *
								Math.cos(($userLocation.latitude * Math.PI) / 180) *
								Math.pow(
									Math.sin((($userLocation.longitude - item._geoloc.lng) * Math.PI) / 180 / 2),
									2
								)
					),
					Math.sqrt(
						1 -
							(Math.pow(
								Math.sin((($userLocation.latitude - item._geoloc.lat) * Math.PI) / 180 / 2),
								2
							) +
								Math.cos((item._geoloc.lat * Math.PI) / 180) *
									Math.cos(($userLocation.latitude * Math.PI) / 180) *
									Math.pow(
										Math.sin((($userLocation.longitude - item._geoloc.lng) * Math.PI) / 180 / 2),
										2
									))
					)
				);
			return distance <= $searchRadius;
		});
		data = data.reduce((acc, item) => {
			const index = acc.findIndex((a) => a.storeName === item.storeName);
			if (index === -1) {
				acc.push(item);
			}
			return acc;
		}, []);
		data = data.sort((a, b) => a.price - b.price);
		best = data[0];
		return data;
	}
</script>

<div
	class="w-full border rounded-md shadow-lg overflow-hidden group bg-white flex flex-col justify-between"
>
	<img src={hit.imageUrl ? hit.imageUrl : '/productHolder.png'} alt={hit.name} class="w-full" />
	<div class="px-5 pt-5">
		<h2
			class="truncate text-primary text-xl font-sans font-medium hover:text-black"
			data-tooltip-target="title"
			data-tooltip-placement="bottom"
			title={hit.name}
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
		{#if hit.size}
			<div class="p-1">
				<div class="flex justify-between">
					<h3 class="text-rich-black font-medium text-md">Size</h3>
					<h3 class="text-rich-black font-medium text-md">{hit.size}{hit.unit}</h3>
				</div>
			</div>
		{/if}
		<div class="border m-1" />
		<div class="p-1">
			{#each displayFilter(hit.data) as data, x}
				{#if x < 3}
					<div class="flex justify-between">
						<h3
							class="flex items-center {x === 0
								? 'text-primary font-bold'
								: 'text-rich-black font-medium'} text-md capitalize truncate"
						>
							{data.storeName}
							<button
								on:focus={() => (activePricePopover = x)}
								on:mouseover={() => (activePricePopover = x)}
								type="button"
							>
								<svg
									class="w-4 h-4 ml-2 text-gray-400 hover:text-gray-500"
									aria-hidden="true"
									fill="currentColor"
									viewBox="0 0 20 20"
									xmlns="http://www.w3.org/2000/svg"
								>
									<path
										fill-rule="evenodd"
										d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z"
										clip-rule="evenodd"
									/>
								</svg>
								<span class="sr-only">Show information</span>
							</button>
						</h3>
						<div
							id="popover-description"
							role="tooltip"
							on:mouseleave={() => (activePricePopover = null)}
							class="{activePricePopover === x
								? 'visible'
								: 'invisible'} absolute z-10 inline-block text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-sm w-72 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-400"
						>
							<div class="p-3 space-y-1">
								<h3 class="font-semibold text-gray-900 dark:text-white">Price last updated at</h3>
								<p>{data.dateExtracted}</p>
								<h3 class="font-semibold text-gray-900 dark:text-white">Normalized Price</h3>
								<p>
									${data.normalized.value} per {data.normalized.quantity}
									{' '}
									{data.normalized.unit}
								</p>
							</div>
							<div data-popper-arrow />
						</div>

						<h3
							class="{x === 0 ? 'text-primary font-bold' : 'text-rich-black font-medium'} text-md"
						>
							${data.price}
						</h3>
					</div>
				{/if}
			{/each}
		</div>
	</div>
	<div class="px-5 pb-5">
		<button
			class="button bg-primary w-full rounded-xl text-white text-sm font-sans font-medium p-2 flex justify-center shadow-md hover:opacity-90 focus:animate-wiggle"
			on:click={() => addProduct(i, best)}>Add to List</button
		>
	</div>
</div>
