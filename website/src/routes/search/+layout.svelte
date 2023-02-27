<script>
	import { page } from '$app/stores';
	import Cart from 'svelte-material-icons/Cart.svelte';
	import MapMarker from 'svelte-material-icons/MapMarker.svelte';
	import Modal from '$lib/Modal.svelte';
	import StoreMap from './StoreMap/StoreMap.svelte';

	$: q = $page.url.searchParams.get('q') || '';

	let sideOpen = false;
	let locationModalOpen = false;

	const toggleLocationModal = () => {
		locationModalOpen = !locationModalOpen;
	};

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
				on:click|stopPropagation={toggleLocationModal}
				on:keypress|stopPropagation={toggleLocationModal}
			>
				<div class="flex flex-col justify-center"><MapMarker width={22} height={22} /></div>
				<div class="flex flex-col">
					<span>Orillia, ON</span>
					<span class="text-xs">Change Location</span>
				</div>
			</div>
		</div>
	</div>
	<button
		class="rounded-full bg-white w-12 h-12 flex justify-center items-center"
		on:click={() => (sideOpen = !sideOpen)}
	>
		<Cart color={'black'} width={24} height={24} />
	</button>
</div>

<!-- Location Modal -->
<Modal visible={locationModalOpen} onClose={toggleLocationModal}>
	<span slot="title">Change Location</span>
	<StoreMap />
	<span slot="footer">
		<div class="modal-footer">
			<button 
				type="button"
				class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
				on:click={toggleLocationModal}
			>
				Apply
			</button>
		</div>
	</span>
</Modal>

<div class="z-0 w-screen h-screen pt-20 bg-background">
	<slot />
</div>

<style>
		.modal-footer {
		display: flex;
		flex-direction: row;
		justify-content: flex-end;
		align-items: center;
		padding: 1rem;
		border-top: 1px solid #eee;
	}

	.modal-footer button {
		background-color: rgb(26, 110, 216);
	}
</style>
