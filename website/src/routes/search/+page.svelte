<script>
	import { searchStore } from "$lib/searchStore";
	import { getDoc, doc, db } from "$lib/firebase.js";

    let hits = [];

    searchStore.subscribe((value) => {
        if (value.length === 0) return;
        hits = [];

        // read the documents from firestore
        const docs = value.map((doc) => doc.path);
        docs.forEach(async (path) => {
            const _doc = await getDoc(doc(db, path));
            hits = [...hits, {
                id: _doc.id,
                ..._doc.data()
            }]
        });
    });
</script>

<svelte:head>
	<title>Groceriez | Search</title>
</svelte:head>

<div class="mx-auto w-2/3 grid grid-cols-5 gap-10 pt-20 place-content-center">
	{#each hits as hit}
        <!-- Card Design -->
	<div class="w-full border rounded-md shadow-lg overflow-hidden group bg-white">
		<img
			src="{hit.imageUrl}"
			alt="{hit.name}"
			class="w-full"
		/>
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
