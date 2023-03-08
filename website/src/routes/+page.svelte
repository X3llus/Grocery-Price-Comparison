<script>
	import { slide } from 'svelte/transition';
    import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import AOS from 'aos';
	import Magnify from 'svelte-material-icons/Magnify.svelte';
	import Store from 'svelte-material-icons/StoreSearchOutline.svelte';
	import List from 'svelte-material-icons/ListBoxOutline.svelte';
	import Account from 'svelte-material-icons/AccountOutline.svelte';
	import ArrowDown from 'svelte-material-icons/ArrowDownDropCircle.svelte';
	import ArrowUp from 'svelte-material-icons/ArrowUpDropCircleOutline.svelte';

	const images = [
        // {
        //     url: "/walmart.jpg",
        //     description: "Walmart Logo",
        //     content: "Walmart Inc. is an American multinational retail corporation that operates a chain of hypermarkets, discount department stores, and grocery stores."
        // },
        {
            url: "/loblaws.jpg",
            description: "Loblaws Logo",
            content: "Loblaws Inc. is a Canadian supermarket chain and is a subsidiary of Loblaw Companies Limited. It is Canada's largest food distributor."
        },
        {
            url: "/metro.jpg",
            description: "Metro Logo",
            content: "Metro Inc. is a Canadian food retailer operating in the provinces of Quebec and Ontario. The company is based in Montreal, Quebec and is the third largest grocer in Canada."
        }
    ];

    const faq = [
        {
            question: "What products do you support?",
            answer: "It's in our name! Groceriez is strictly a prices comparison platform for groceries."
        },
        {
            question: "Do I need to make an account?",
            answer: "It is only necessary to make an account with us if you want to use our service to save lists or favourite products. Our simple look-up does not require an account."
        },
        {
            question: "Will you be adding more stores?",
            answer: "We are constantly working on expanding the number of stores available to our customers! Sadly we do not have any estimates due to the complexity of the process we have to undertake for each store."
        },
        {
            question: "Do you have a mobile app?",
            answer: "Currently we don't have an app, but our site is fully optimized for mobile browsing!"
        }
    ];

	let showContent = '';
    let search = '';
    
	const handleClick = (/** @type {string} */ payload) => {
		showContent = payload === showContent ? '' : payload;
	};

	onMount(() => {
		AOS.init();
	});
</script>

<svelte:head>
	<!-- Couldn't find a integration with Tailwind and AOS Library so here is a style sheet. I'm not making my own integration. If someone finds one hmu-->
	<link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />
	<title>Groceriez | Home</title>
</svelte:head>

<div class="mx-auto text-center">
    <div style="background-image: url(../../background.svg);" class="bg-center bg-cover">
        <img src="GroceriezLogo.svg" alt="" class="mx-auto py-32 w-2/3 lg:w-1/3 ">
    </div>
    <!-- Welcome -->
    <!-- To add Search Page, Login buttons -->
    <div class="bg-rich-black py-20 px-10 md:px-30 xl:px-60">
        <div data-aos="fade-up" data-aos-once="true">
            <h2 class="text-7xl pb-10 text-white font-sans font-extrabold">Savings are just a click away!</h2>
                <form on:submit|preventDefault={() => goto(`/search?q=${search}`)} class="flex justify-center py-10">
                    <input 
                        bind:value={search}
                        class="p-2 rounded-l-lg w-2/3 border-y border-l-2 border-accent shadow-md bg-gradient-to-b focus:outline-none"
                        placeholder="Search our Products"
                    />
				<button type="submit" class="p-2 rounded-r-lg border-y border-r-2 border-accent bg-accent bg-grad shadow-md w-16 flex justify-center">
                    <Magnify color={'white'} width={24} height={24} />
                </button>
            </form>
            <p class="text-2xl font-sans font-medium text-background">
                Tired of taking time and always looking for the best price when grocery shopping? Look no
                further. Groceriez is your go-to App for price comparison at your local chain, Ontarian grocers.
                Never overpay for groceries again, and simplify your shopping experience with our one-of-a-kind
                App!
            </p>
        </div>
    </div>
    <div class="bg-secondary py-20 px-10 md:px-30 lg:px-60">
        <!-- App Features -->
        <div data-aos="fade-up" data-aos-once="true">
            <h2 class="text-6xl p-5 font-sans font-bold text-white">Our Dev Map</h2>
            <div class="mx-auto justify-center gap-10 flex flex-col xl:flex-row px-5 pb-10 items-center">
                <div class="flex w-3/4 lg:w-1/3 items-center">
                    <Store color={'white'} width={200} height={200} />
                    <p class=" text-xl text-white font-sans font-medium">
                        Searching our database for generic or specific brands of products and finding the best deal that is local to you.
                    </p>
                </div>
                <div class="border-y-2 xl:border-y-0 xl:border-x-2 border-white w-1/2 xl:w-0 xl:h-24"/>
                <div class="flex w-3/4 xl:w-1/3 items-center">
                    <List color={'white'} width={240} height={200} />
                    <p class=" text-xl text-white font-sans font-medium">
                        Making your life easier by letting you create and add items to custom grocery lists. 
                        These lists will let you decide which stores to shop at.
                    </p>
                </div>
                <div class="border-y-2 xl:border-y-0 xl:border-x-2 border-white w-1/2 xl:w-0 xl:h-24"/>
                <div class="flex w-3/4 xl:w-1/3 items-center">
                    <Account color={'white'} width={200} height={200} />
                    <p class=" text-xl text-white font-sans font-medium">
                        The creation of user accounts lets you see your search history, enables you to save lists and favourite products.
                    </p>
                </div>
            </div>
        </div>
        <!-- Supported Stores-->
        <div data-aos="fade-up" data-aos-once="true">
            <h2 class="text-6xl p-5 font-sans font-bold text-white">Our Supported Stores</h2>
            <div class="mx-auto flex flex-wrap gap-10 justify-center px-5 py-10">
                {#each images as src}
                    <div class="p-2 rounded-xl bg-gradient-to-b from-rich-black to-primary shadow-xl flex justify-center items-center group">
                        <img class="h-auto max-w-xs sm:max-w-sm rounded-xl duration-300 group-hover:blur-sm group-hover:opacity-20" src={src.url} alt={src.description}/>
                        <p class="absolute opacity-0 group-hover:opacity-100 duration-500 text-white max-w-xs sm:max-w-sm text-sm sm:text-base">{src.content}</p>
                    </div>
                {/each}
            </div>
        </div>
    </div>
    <!-- FAQ -->
    <div class="bg-primary py-10">
        <div data-aos="fade-up" data-aos-once="true">
            <div class=" flex justify-center">
                <div class="w-7/8 md:w-3/4 xl:w-1/2">
                    <h2 class="text-6xl p-5 font-sans font-medium text-white sm:text-left text-center">FAQ</h2>
                    <div class="w-3/4 mx-auto">
                        {#each faq as q, i}
                        <div class="flex justify-between items-center">
                            <h3 class="text-3xl p-5 font-sans font-medium text-background text-left">{q.question}</h3>
                            {#if showContent === q.question}
                                <button type="button" on:click={() => handleClick(q.question)}><ArrowUp color={'white'} width={40} height={40} /></button>
                            {:else}
                                <button type="button" on:click={() => handleClick(q.question)}><ArrowDown color={'white'} width={40} height={40} /></button>
                            {/if}
                        </div>
                            {#if showContent === q.question}
                                <p transition:slide={{ duration: 300}} class="text-l pb-10 font-sans font-normal text-background text-left">{q.answer}</p>
                            {/if}
                            {#if i < faq.length-1}
                                <div class="p-0.5 bg-white"/>
                            {/if}
                        {/each}
                    </div>
                </div>
            </div>
            <div class="bg-primary pt-20 pb-5 flex gap-5 justify-center">
                <a href="/tos" class="text-xl pb-10 font-sans font-medium text-background underline hover:no-underline">Terms of Service</a>
                <a href="/privacy" class="text-xl pb-10 font-sans font-medium text-background underline hover:no-underline">Privacy Policy</a>
            </div>
        </div>
    </div>
</div>
