<script>
	import Cart from 'svelte-material-icons/Cart.svelte';
	import MapMarker from 'svelte-material-icons/MapMarker.svelte';

	var sideOpen = false;

	function change_address() {
		// TODO: Change address
		console.log('change address');
	}
</script>

<!-- Slide Menu -->
<div
	class="fixed right-0 top-0 h-screen transition-transform z-30 w-80"
	style="transform: translateX({sideOpen ? '0%' : '100%'});"
>
	<div class="h-full bg-background">
		<h2 class="text-2xl text-black py-4 w-full text-center">List/Cart</h2>
	</div>
</div>

{#if sideOpen}
	<div
		class="fixed top-0 left-0 w-full h-full bg-black opacity-50 z-20"
		on:click={() => (sideOpen = false)}
		on:keypress={() => (sideOpen = false)}
	/>
{/if}

<!-- Main Nav Bar -->
<div class="fixed left-0 top-0 w-screen z-10 p-4 flex space-x-4 bg-primary shadow-lg">
	<!-- <button on:click={() => (sideOpen = !sideOpen)}>
		<div class="space-y-2">
			<div class="w-8 h-1 bg-white rounded-sm" />
			<div class="w-8 h-1 bg-white rounded-sm" />
			<div class="w-8 h-1 bg-white rounded-sm" />
		</div>
	</button> -->
	<h1 class="text-3xl text-white leading-normal">Groceriez</h1>
	<div class="flex flex-1">
		<input class="p-2 rounded-lg flex-1" placeholder="Search products" />
		<div class="flex flex-col justify-center">
			<div
				class="flex-initial mx-14 flex hover:cursor-pointer text-white font-medium"
				on:click={change_address}
				on:keypress={change_address}
			>
				<div class="flex flex-col-reverse"><MapMarker width={22} height={22} /></div>
				Random Address
			</div>
		</div>
	</div>
	<button class="rounded-full bg-white w-12 h-12 flex justify-center items-center" on:click={() => (sideOpen = !sideOpen)}>
		<Cart color={'black'} width={24} height={24} />
	</button>
</div>

<div class="z-0 w-screen h-screen pt-20 bg-background">
	<slot />
</div>
