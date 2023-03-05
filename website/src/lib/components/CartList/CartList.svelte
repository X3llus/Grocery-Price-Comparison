<script lang='ts'>
  import Delete from 'svelte-material-icons/Delete.svelte';
  // import { cart } from '$lib/stores';
  import type { Product } from '$lib/types';

  let testProducts: Product[] = [
    {
        SKU: '20303218010_C06',
        name: 'G2, Fruit Punch',
        brand: 'Gatorade',
        packageSize: '6x591.0 ml',
        imageUrl: 'https://assets.shop.loblaws.ca/products/20303218010/b1/en/front/20303218010_front_a01_@2.png',
        parentCompany: 'Loblaws',
    },
    {
        SKU: '059749902755',
        name: 'Dry Roasted Seasoned Peanuts',
        brand: 'Selection',
        packageSize: '700 g',
        imageUrl: 'https://product-images.metro.ca/images/h63/h9c/10715197767710.jpg',
        parentCompany: 'Metro',
    },
    {
        SKU: '6000198648175',
        name: 'Great Value Cheese Jalapeno Smokie Sausage',
        brand: 'Great Value',
        packageSize: '175 g',
        imageUrl: 'https://i5.walmartimages.ca/images/Thumbnails/243/082/6000200243082.jpg',
        parentCompany: 'Walmart',
    }
  ]
</script>


<ul class="max-w-md divide-y divide-gray-200 dark:divide-gray-700">
  {#each testProducts as product (product.SKU)}
    <li class="pb-3 sm:pb-4 px-0.5">
      <div class="flex items-center space-x-4">
        <div class="flex-shrink-0">
          <img class="w-10 h-10 rounded-full" src={product.imageUrl} alt={product.name} />
        </div>
        <div class="flex-1 min-w-0">
          <p class="font-semibold text-gray-900 truncate dark:text-white">
            {product.name}
          </p>
          <p class="text-sm font-semibold text-gray-700 truncate dark:text-gray-400">
            {product.parentCompany} - {product.brand}
          </p>
          <p class="text-sm text-gray-500 truncate dark:text-gray-400">
            {product.packageSize}
          </p>
        </div>
        <button 
          class="rounded-full w-10 h-10 flex justify-center items-center"
          on:click={() => testProducts = testProducts.filter(p => p.SKU !== product.SKU)}
          aria-label="Remove from cart"  
        >
          <Delete width={24} height={24} />
        </button>
      </div>
    </li>
  {/each}
</ul>