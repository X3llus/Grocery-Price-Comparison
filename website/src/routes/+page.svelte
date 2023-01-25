<script>
    import Carousel from 'svelte-carousel';

    const nums = [1,2,3,4,5];
</script>
<div class="mx-auto text-center pt-20">
    <h1 class="text-7xl text-gray-600">Groceriez</h1>
    <p>
        Tired of taking time and always looking for the best price when grocery shopping? Look no further. 
        Groceriez is the go-to App for price comparison at your local chain, Ontarian grocers. 
        Never overpay for groceries again, and simplify your shopping experience with our one-of-a-kind App!
    </p>
    <h2>Our Supported Stores</h2>
    <div class="">
        <!-- Image Carousel -->
        <Carousel>
            {#each nums as num}
                <div>{num}</div>
            {/each}
            
        </Carousel>

    </div>
    <p>
        <!-- Copy about supported Stores -->
    </p>
    <h2>Search our Database Now!</h2>
    <div class="">
        <!-- Search bar -->
    </div>
    <!-- Coming features Copy? -->
</div>

