<script lang="ts">
	import Delete from 'svelte-material-icons/Delete.svelte';
	import { createEventDispatcher } from 'svelte';
	import { searchListStore } from '$lib/searchStore';

	export let item;
	export let i;

</script>

<li class="bg-white rounded-md shadow-md overflow-hidden">
    <div class="flex p-2">
        <img class="w-16 h-16" src={item.imageUrl ? item.imageUrl : "/productHolder.png"} alt="" />
        <div class="flex flex-col flex-1 pl-2 w-0">
            <span class="text-sm font-medium truncate text-primary hover:text-black" title="{item.name}">{item.name}</span>
            <div class="flex justify-between">
                <span class="text-sm font-medium capitalize">{item.best[0] ? item.best[0].storeName : item.data[0].storeName}</span>
                <span class="text-sm font-medium">${item.best[0] ? item.best[0].price.toFixed(2) : item.data[0].price.toFixed(2)}</span>
            </div>
        </div>
        <button
            class="rounded-full w-10 h-10 flex justify-end"
            aria-label="Remove from cart"
            on:click={() => {
                searchListStore.add((value) => {
                    value.splice(i, 1);
                    return value;
                });
            }}
        >
            <Delete width={24} height={24}/>
        </button >
    </div>
    <div class="flex justify-between">
        <button 
            class="bg-gradient-to-b from-green-700 to-primary text-white w-1/4 font-bold rounded-tr-md"
            on:click={() => {
                // Add logic for subtracting from product quantity
                if (item.quanity <= 1) {
                  return searchListStore.add((value) => {
                    value.splice(i, 1);
                    return value;
                  });
                }

                searchListStore.add((value) => {
                  value[i].quanity -= 1;
                  return value;
                });
            }}
        >
            -
        </button>
        <div class="text-md font-sans font-semibold">
            <!-- This needs to update when you add a product from the search page -->
            {item.quanity}
        </div>
        <button 
            class="bg-gradient-to-b from-green-700 to-primary text-white w-1/4 font-bold rounded-tl-md"
            on:click={() => {
                // Add logic for adding to product quantity
                searchListStore.add((value) => {
                  value[i].quanity += 1;
                  return value;
                });
            }}
        >
            +
        </button>
    </div>
</li>
