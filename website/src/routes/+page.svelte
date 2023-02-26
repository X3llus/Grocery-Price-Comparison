<script>
	import { browser } from '$app/environment';
	import { slide } from 'svelte/transition';
	import { onMount } from 'svelte';
	import AOS from 'aos';
	import Magnify from 'svelte-material-icons/Magnify.svelte';
	import Store from 'svelte-material-icons/StoreSearchOutline.svelte';
	import List from 'svelte-material-icons/ListBoxOutline.svelte';
	import Account from 'svelte-material-icons/AccountOutline.svelte';
	import ArrowDown from 'svelte-material-icons/ArrowDownDropCircle.svelte';
	import ArrowUp from 'svelte-material-icons/ArrowUpDropCircleOutline.svelte';

	const images = [
		{
			url: '/walmart.jpg',
			description: 'Walmart Logo',
			content: 'Walmart Logo',
		},
		{
			url: '/loblaws.jpg',
			description: 'Loblaws Logo',
			content: 'Loblaws Logo',
		},
	];

	const faq = [
		{
			question: 'What products do you support?',
			answer:
				'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis mollis odio et viverra congue. Quisque non ligula nulla.',
		},
		{
			question: 'Do I need to make an account?',
			answer:
				'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis mollis odio et viverra congue. Quisque non ligula nulla.',
		},
		{
			question: 'Will you be adding more stores?',
			answer:
				'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis mollis odio et viverra congue. Quisque non ligula nulla.',
		},
	];

	let showContent = '';
	const handleClick = (/** @type {string} */ payload) => {
		showContent = payload === showContent ? '' : payload;
	};

	let search = '';

	onMount(() => {
		AOS.init();
	});
</script>

<svelte:head>
	<!-- Couldn't find a integration with Tailwind and AOS Library so here is a style sheet. I'm not making my own integration. If someone finds one hmu-->
	<link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />
	<title>Groceriez | Home</title>
</svelte:head>

<div class="mx-auto text-center pt-20">
	<!-- To be replaced with SVG Art and Logo-->
	<div class="py-40">
		<h1 class="text-9xl text-secondary font-sans font-thin">Groceriez</h1>
	</div>
	<!-- Welcome -->
	<!-- To add Search Page, Login buttons -->
	<div class="bg-rich-black py-20">
		<div data-aos="fade-up" data-aos-once="true">
			<h2 class="text-7xl pb-10 text-white font-sans font-extrabold">
				Savings are just a click away!
			</h2>
			<div id="search-bar" class="flex justify-center p-10">
				<input
					bind:value={search}
					class="p-2 rounded-l-lg w-2/3 border-y border-l-2 border-accent shadow-md bg-gradient-to-b focus:outline-none"
					placeholder="Search our Products"
				/>
				<a
					href="/search?q={search}"
					class="p-2 rounded-r-lg border-y border-r-2 border-accent bg-accent bg-grad shadow-md w-16 flex justify-center"
					><Magnify color={'white'} width={24} height={24} /></a
				>
			</div>
			<p class="text-2xl px-60 font-sans font-medium text-background">
				Tired of taking time and always looking for the best price when grocery shopping? Look no
				further. Groceriez is your go-to App for price comparison at your local chain, Ontarian
				grocers. Never overpay for groceries again, and simplify your shopping experience with our
				one-of-a-kind App!
			</p>
		</div>
	</div>
	<div class="bg-secondary py-20 px-60">
		<!-- App Features -->
		<div data-aos="fade-up" data-aos-once="true">
			<h2 class="text-6xl p-5 font-sans font-bold text-white">Our Dev Map</h2>
			<div class="mx-auto justify-center gap-10 flex px-5 pb-10 items-center">
				<div class="flex w-1/3 items-center">
					<Store color={'white'} width={200} height={200} />
					<p class=" text-xl text-white font-sans font-medium">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis mollis odio et viverra
						congue. Quisque non ligula nulla.
					</p>
				</div>
				<div class="border-x-2 border-white h-24" />
				<div class="flex w-1/3 items-center">
					<List color={'white'} width={200} height={200} />
					<p class=" text-xl text-white font-sans font-medium">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis mollis odio et viverra
						congue. Quisque non ligula nulla.
					</p>
				</div>
				<div class="border-x-2 border-white h-24" />
				<div class="flex w-1/3 items-center">
					<Account color={'white'} width={200} height={200} />
					<p class=" text-xl text-white font-sans font-medium">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis mollis odio et viverra
						congue. Quisque non ligula nulla.
					</p>
				</div>
			</div>
		</div>
		<!-- Supported Stores-->
		<div data-aos="fade-up" data-aos-once="true">
			<h2 class="text-6xl p-5 font-sans font-bold text-white">Our Supported Stores</h2>
			<div class="mx-auto flex flex-wrap gap-10 justify-center px-5 py-10">
				{#each images as src}
					<div
						class="p-2 rounded-xl bg-gradient-to-b from-rich-black to-primary shadow-xl flex justify-center items-center group"
					>
						<img
							class="h-auto max-w-sm rounded-xl duration-300 group-hover:blur-sm group-hover:opacity-20"
							src={src.url}
							alt={src.description}
						/>
						<p class="absolute opacity-0 group-hover:opacity-100 duration-500 text-white">
							{src.content}
						</p>
					</div>
				{/each}
			</div>
		</div>
	</div>
	<!-- FAQ -->
	<div class="bg-primary py-10">
		<div data-aos="fade-up" data-aos-once="true">
			<div class=" flex justify-center">
				<div class="w-1/2">
					<h2 class="text-6xl p-5 font-sans font-medium text-white text-left">FAQ</h2>
					<div class="w-3/4 mx-auto">
						{#each faq as q, i}
							<div class="flex justify-between items-center">
								<h3 class="text-3xl p-5 font-sans font-medium text-background text-left">
									{q.question}
								</h3>
								{#if showContent === q.question}
									<button type="button" on:click={() => handleClick(q.question)}
										><ArrowUp color={'white'} width={40} height={40} /></button
									>
								{:else}
									<button type="button" on:click={() => handleClick(q.question)}
										><ArrowDown color={'white'} width={40} height={40} /></button
									>
								{/if}
							</div>
							{#if showContent === q.question}
								<p
									transition:slide={{ duration: 300 }}
									class="text-l pb-10 font-sans font-normal text-background text-left"
								>
									{q.answer}
								</p>
							{/if}
							{#if i < faq.length - 1}
								<div class="p-0.5 bg-white" />
							{/if}
						{/each}
					</div>
				</div>
			</div>
			<div class="bg-primary pt-20 pb-5 flex gap-5 justify-center">
				<a
					href="#"
					class="text-xl pb-10 font-sans font-medium text-background underline hover:no-underline"
					>Terms of Service</a
				>
				<a
					href="#"
					class="text-xl pb-10 font-sans font-medium text-background underline hover:no-underline"
					>Privacy Policy</a
				>
			</div>
		</div>
	</div>
</div>
