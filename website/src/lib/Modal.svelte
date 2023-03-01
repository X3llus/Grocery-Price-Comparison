<script>
	import { fly, fade } from 'svelte/transition';
	import Close from 'svelte-material-icons/Close.svelte'
	export let visible = false;
	export let onClose;

	const handleClose = () => {
		onClose();
	};
</script>

{#if visible}
	<div
		class="modal"
		transition:fly={{ y: -150, duration: 250 }}
	>
		<div class="header">
			<h2 class="title">
				<slot name="title" />
			</h2>
			<p class="subtitle">
				<slot name="subtitle" />
			</p>
			<div class="close-container">
			<div class="close-background">
				<div class="close" on:click={handleClose} on:keydown={handleClose}>
					<Close />
				</div>
			</div>
		</div>
		</div>
		
		<slot />

		<slot name="footer" />
	</div>
	<div class="overlay" transition:fade={{ duration: 175 }} />
{/if}

<style>
	.modal {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		width: 70vw;
		height: 70vh;
		padding: 15px;
		background: #fff;
		z-index: 3;
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		border-radius: 6px;
	}

	.overlay {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background: rgba(0, 0, 0, 0.5);
		z-index: 2;
	}

	.header {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: baseline;
		padding: 0.25rem 0.5rem;
		border-bottom: 1px solid #eee;
	}

	.title {
		margin: 0;
		font-size: 1.5rem;
		font-weight: 600;
	}

	.subtitle {
		margin: 0;
		font-size: 0.85rem;
		font-weight: 400;
		font-style: italic;
		margin-right: 10rem;
	}

	.close {
		cursor: pointer;
    color: rgb(28, 30, 33);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 20px;
    height: 20px;
    background-color: transparent;
    z-index: 3;
	}

	.close-background {
    position: absolute;
    top: -5px;
    right: -5px;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background-color: #bdbdbd;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 2;
		transition: background-color 0.2s ease-in-out;
  }

	.close-background:hover {
		background-color: #eeeeee;
	}
	.close-container {
    position: absolute;
    top: 15px;
    right: 15px;
  }

	@media screen and (max-width: 900px) {
		.modal {
			width: 100vw;
			height: 80vh;
		}
	}
</style>
