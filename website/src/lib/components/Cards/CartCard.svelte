<script lang="ts">
    
	import Delete from 'svelte-material-icons/Delete.svelte';
    import { createEventDispatcher } from "svelte";
	import { searchListStore} from '$lib/searchStore';

    export let item;
    export let i;

</script>

<li class="pt-3 bg-white rounded-md shadow-md overflow-hidden">
    <div class="flex">
        <img class="w-16 h-16" src={item.imageUrl} alt="" />
        <div class="flex flex-col flex-1 pl-3">
            <span class="text-sm font-medium truncate text-primary hover:text-black" title="{item.name}">{item.name}</span>
            <div class="flex justify-between">
                <span class="text-sm font-medium capitalize">{item.data[0].storeName}</span>
                <span class="text-sm font-medium">${item.data[0].price}</span>
            </div>
        </div>
        <button
            class="rounded-full w-10 h-10 flex justify-center"
            aria-label="Remove from cart"
            on:click={() => {
                searchListStore.update((value) => {
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
                
            }}
        >
            +
        </button>
    </div>
</li>