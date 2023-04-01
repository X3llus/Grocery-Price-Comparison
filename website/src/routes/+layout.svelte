<script>
	import { onMount } from 'svelte';
    import '../app.css';

    onMount(() => {
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register("/service-worker.js");
        }
    });
</script>

<div class="z-0 bg-background">
	<slot />
</div>