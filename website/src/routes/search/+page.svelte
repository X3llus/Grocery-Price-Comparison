<script lang="ts">
    import { fly } from 'svelte/transition';
	import { quintOut } from 'svelte/easing';
    import { BaseProductCard } from '$lib/components';
    import { flip } from 'svelte/animate';

    let testProducts = [
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

    const handleAddToCart = (event: CustomEvent<{SKU:string}>) => {
        // This is an example. We will need to add the product to the cart "store" here and remove
        // the product from the list of products that are rendered on the page.
        testProducts = testProducts.filter(product => product.SKU !== event.detail.SKU);
    }

</script>


<svelte:head>
	<title>Groceriez | Search</title>
</svelte:head>

<div class="mx-auto w-2/3 grid grid-cols-3 gap-10 pt-20 place-content-center">
    <!-- For testing. Will need to load data and iterate over it here -->
    {#each testProducts as testProduct (testProduct.SKU)}
        <div 
            transition:fly="{{ x: window.innerWidth, y: -500, duration: 1000, easing: quintOut }}"
            animate:flip="{{ duration: 250 }}"
        >
            <BaseProductCard Props={testProduct} on:addToCart={handleAddToCart} />
        </div>
    {/each}
</div>



<!-- <div class="w-full border rounded-md shadow-lg overflow-hidden group bg-white">
  <img src="https://assets.shop.loblaws.ca/products/20000005/b1/en/front/20000005_front_a01_@2.png" alt="" class="w-full">
  <div class="p-5">
      <h2 class="truncate text-primary text-xl font-sans font-medium group-hover:text-black" data-tooltip-target="title" data-tooltip-placement="bottom">Fresh-Pressed Sweet Apple Cider</h2>
      <h2 class="truncate text-secondary text-sm font-sans font-bold" data-tooltip-target="title" data-tooltip-placement="bottom">President's Choice</h2>
      <div class="border m-1"></div>
      <div class="p-3">
          <div class="flex justify-between">
              <h3 class="text-accent font-bold text-xl group-hover:underline">NoFrills</h3>
              <h3 class="text-accent font-bold text-xl group-hover:underline">$4.70</h3>
          </div>
          <div class="flex justify-between">
              <h3 class="text-rich-black font-medium text-md">Loblaws</h3>
              <h3 class="text-rich-black font-medium text-md">$5.10</h3>
          </div>
          <div class="flex justify-between">
              <h3 class="text-rich-black font-medium text-md">Zeher's</h3>
              <h3 class="text-rich-black font-medium text-md">$5.30</h3>
          </div>
      </div>
      <a href="#" class="button bg-primary w-full rounded-xl text-white text-sm font-sans font-medium p-2 flex justify-center shadow-md hover:opacity-90">Veiw Product Details</a>
  </div>
</div> -->