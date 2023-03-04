<script lang='ts'>
  import { onMount, createEventDispatcher } from 'svelte';
  import { getCardIcon } from '$lib/utils';
  import type { Product } from '$lib/types';

  export let Props: Product;
  let companyIcon: string;
  const dispatch = createEventDispatcher<{addToCart:{SKU:string}}>();

  onMount(() => {
    companyIcon = getCardIcon(Props.parentCompany);
  });

  const handleAddToCart = () => {
    dispatch('addToCart', {SKU: Props.SKU});
  };

</script>





<div class="relative">
  <div class="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
      <img class="rounded-t-lg" src={Props.imageUrl} alt={Props.name} />
    <div class="p-5">
      <h5 class="truncate text-primary text-xl font-sans font-medium tracking-tight text-gray-800 dark:text-white">
        {Props.name}
      </h5>
      <p class="truncate text-secondary text-sm font-sans font-bold text-gray-500 dark:text-gray-300">
        {Props.brand}
      </p>
      <p class="truncate text-secondary text-xs mb-3 font-sans font-bold text-gray-800 dark:text-gray-400">
        {Props.packageSize}
      </p>
      <div class="border m-1 mb-3" />
      <button 
        class="button bg-primary w-full rounded-xl text-white text-sm font-sans font-medium p-2 flex justify-center shadow-md hover:opacity-90"
        on:click={handleAddToCart}
        on:keypress={handleAddToCart}
      >
        Add to Cart  
      </button>
    </div>
  </div>
  <div class="absolute inline-flex items-center justify-center w-14 h-14 text-xs font-bold text-white bg-red-500 border-2 border-white rounded-full -top-2 -right-2 dark:border-gray-900">
    <img src={companyIcon} alt={Props.parentCompany} title={Props.parentCompany} />
  </div>
</div>