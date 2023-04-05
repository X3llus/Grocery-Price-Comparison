<script lang="ts">
    import { createEventDispatcher } from "svelte";
	import { userLocation, searchRadius } from '$lib/stores';

    export let hit;
    export let i;
    let best;

    const dispatch = createEventDispatcher();

    function addProduct(i, best) {
		dispatch('product', {i, best});
	}

    function displayFilter(data) {
        data = data.filter((item) => {

        let distance = 6371 * 2 * Math.atan2(Math.sqrt(Math.pow(Math.sin(($userLocation.latitude - item._geoloc.lat) * Math.PI/180 / 2), 2) + 
            Math.cos(item._geoloc.lat * Math.PI/180) * Math.cos($userLocation.latitude * Math.PI/180) * Math.pow(Math.sin(($userLocation.longitude - item._geoloc.lng) * 
            Math.PI/180 / 2), 2)), Math.sqrt(1 - (Math.pow(Math.sin(($userLocation.latitude - item._geoloc.lat) * Math.PI/180 / 2), 2) + 
            Math.cos(item._geoloc.lat * Math.PI/180) * Math.cos($userLocation.latitude * Math.PI/180) * Math.pow(Math.sin(($userLocation.longitude - item._geoloc.lng) * Math.PI/180 / 2), 2))));
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
        best = data[0]
        return data

    }

</script>

<div class="w-full border rounded-md shadow-lg overflow-hidden group bg-white flex flex-col justify-between">
    <img src={hit.imageUrl ? hit.imageUrl : "/productHolder.png"} alt={hit.name} class="w-full" />
    <div class="px-5 pt-5">
        <h2
            class="truncate text-primary text-xl font-sans font-medium hover:text-black"
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
        <div class="border m-1" />
        <div class="p-1">
            {#each displayFilter(hit.data) as data, x}
                {#if x < 3}
                    <div class="flex justify-between">
                        <h3 class="{ x === 0 ? 'text-primary font-bold' : 'text-rich-black font-medium' } text-md capitalize truncate" title="{data.storeName}">{data.storeName}</h3>
                        <h3 class="{ x === 0 ? 'text-primary font-bold' : 'text-rich-black font-medium' } text-md">${data.price}</h3>
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