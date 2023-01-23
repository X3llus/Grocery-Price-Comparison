<script>
	import '../app.css';

	var sideOpen = false;
</script>

<!-- Slide Menu -->
<div
	class="fixed left-0 top-0 w-64 h-screen transition-transform z-20"
	style="transform: translateX({sideOpen ? '0%' : '-100%'});"
>
	<div class="h-full bg-background">
		<h2 class="text-2xl text-black py-4 w-full text-center">Test</h2>
	</div>
</div>

<!-- Main Nav Bar -->
<div class="fixed left-0 top-0 w-screen z-10 p-4 flex space-x-4 bg-primary shadow-lg">
	<button on:click={() => (sideOpen = !sideOpen)}>
		<div class="space-y-2">
			<div class="w-8 h-1 bg-white rounded-sm" />
			<div class="w-8 h-1 bg-white rounded-sm" />
			<div class="w-8 h-1 bg-white rounded-sm" />
		</div>
	</button>
	<h1 class="text-3xl text-secondary">Groceriez</h1>
</div>

<div class="z-0 w-screen h-screen pt-16 bg-background">
	{#if sideOpen}
		<div
			class="fixed top-0 left-0 w-full h-full bg-black opacity-50"
			on:click={() => (sideOpen = false)} on:keypress={() => (sideOpen = false)}
		/>
	{/if}
	<slot />
</div>
