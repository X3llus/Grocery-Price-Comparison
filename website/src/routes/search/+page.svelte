<script>
	import { searchStore } from '$lib/searchStore';
	import { getDoc, doc, db, rtdb, ref, child, get } from '$lib/firebase.js';
	import { onDestroy } from 'svelte';

	let hits = [];
	$: console.log(hits);

	searchStore.subscribe((value) => {
		if (value.length === 0) return;
		hits = [];

		// read the documents from firestore
		const docs = value.map((doc) => doc.path);
		docs.forEach(async (path) => {
			const _doc = await getDoc(doc(db, path));
			// get the store from realtime database
			// TODO: append space to end of query, add items to a list to show where to get what items
			const _ref = ref(rtdb);
			let snapshot;

			switch (_doc.data().parentCompany) {
				case 'Loblaws':
					snapshot = await get(child(_ref, `store-prices/zehrs-0559-${_doc.data().SKU}`));
					break;

				case 'Metro':
					snapshot = await get(child(_ref, `store-prices/Metro-0000-${_doc.data().SKU}`));
					break;

				default:
					break;
			}

			// if (snapshot.exists()) {
			// 	console.log(snapshot.val());
			// } else {
			// 	console.log('No data available');
			// }

			const price = snapshot.exists()? snapshot.val().price : null
			if (price === null) return;

			// add to hits
			hits = [
				...hits,
				{
					id: _doc.id,
					..._doc.data(),
					price
				},
			];
		});
	});

	onDestroy(() => {
		hits = [];
		searchStore.set([]);
	});
</script>

<svelte:head>
	<title>Groceriez | Search</title>
</svelte:head>

<div class="mx-auto w-2/3 grid grid-cols-5 gap-10 pt-20 place-content-center">
	{#each hits as hit}
		<!-- Card Design -->
		<div class="w-full border rounded-md shadow-lg overflow-hidden group bg-white">
			<img src={hit.imageUrl} alt={hit.name} class="w-full" />
			<div class="p-5">
				<h2
					class="truncate text-primary text-xl font-sans font-medium group-hover:text-black"
					data-tooltip-target="title"
					data-tooltip-placement="bottom"
				>
					{hit.name}
				</h2>
				{#if hit.brand}
					<h2
						class="truncate text-secondary text-sm font-sans font-bold"
						data-tooltip-target="title"
						data-tooltip-placement="bottom"
					>
						{hit.brand}
					</h2>
				{/if}
				<div class="border m-1" />
				<div class="p-3">
					<div class="flex justify-between">
						<h3 class="text-rich-black font-medium text-md">Store</h3>
						<h3 class="text-rich-black font-medium text-md">{hit.parentCompany}</h3>
					</div>
				</div>
				{#if hit.packageSize}
					<div class="p-3">
						<div class="flex justify-between">
							<h3 class="text-rich-black font-medium text-md">Size</h3>
							<h3 class="text-rich-black font-medium text-md">{hit.packageSize}</h3>
						</div>
					</div>
				{/if}
				<div class="p-3">
					<div class="flex justify-between">
						<h3 class="text-rich-black font-medium text-md">Price</h3>
						<h3 class="text-rich-black font-medium text-md">${hit.price}</h3>
					</div>
				</div>
				<!-- <div class="p-3">
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
			</div> -->
				<a
					href="/product/{hit.id}"
					class="button bg-primary w-full rounded-xl text-white text-sm font-sans font-medium p-2 flex justify-center shadow-md hover:opacity-90"
					>Veiw Product Details</a
				>
			</div>
		</div>
	{/each}
</div>
