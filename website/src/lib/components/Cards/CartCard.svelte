<script lang="ts">
    
	import Delete from 'svelte-material-icons/Delete.svelte';
    import { createEventDispatcher } from "svelte";
	import { searchListStore} from '$lib/searchStore';

    export let item;
    export let i;

</script>

<li class="py-3 sm:pb-4 px-0.5 flex bg-white rounded-md shadow-md">
    <img class="w-16 h-16" src={item.imageUrl} alt="" />
    <div class="flex flex-col flex-1">
        <span class="text-sm font-medium">{item.name} - {item.data[0].storeName}</span>
        <span class="text-sm font-medium">${item.data[0].price}</span>
    </div>
    <button
        class="rounded-full w-10 h-10 flex justify-center items-center"
        aria-label="Remove from cart"
        on:click={() => {
            searchListStore.update((value) => {
                value.splice(i, 1);
                return value;
            });
        }}
    >
        <Delete width={24} height={24} />
    </button>
</li>