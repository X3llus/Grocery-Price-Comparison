<script lang="ts">
    import { createEventDispatcher } from "svelte";

    export let hit;
    export let i;

    const dispatch = createEventDispatcher();

    function addProduct(i) {
		dispatch('product', {i});
	}

</script>

<div class="w-full border rounded-md shadow-lg overflow-hidden group bg-white flex flex-col justify-between">
    <img src={hit.imageUrl ? hit.imageUrl : "/productHolder.png"} alt={hit.name} class="w-full" />
    <div class="p-5">
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
        <div class="border m-1" />
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
        <div class="p-1">
            <div class="flex justify-between">
                <h3 class="text-rich-black font-medium text-md">Price</h3>
                <h3 class="text-rich-black font-medium text-md">${hit.data[0].price}</h3>
            </div>
        </div>
        <button
            class="button bg-primary w-full rounded-xl text-white text-sm font-sans font-medium p-2 flex justify-center shadow-md hover:opacity-90 focus:animate-wiggle"
            on:click={() => addProduct(i)}>Add to List</button
        >
    </div>
</div>