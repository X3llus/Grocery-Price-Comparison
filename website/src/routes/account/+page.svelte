<script>
    import { onMount } from 'svelte';
    import { getAuth, onAuthStateChanged, signOut } from '$lib/firebase';
    
    let auth = getAuth();
    
    onMount(() => {
        onAuthStateChanged(auth, (user) => {
        if (user) {
            // User is signed in, see docs for a list of available properties
            // https://firebase.google.com/docs/reference/js/firebase.User
            const uid = user.uid;
            console.log(uid);
            // ...
        } else {
            // User is signed out
            // ...
        }
        });
    });
</script>

<!-- signout button -->
<button on:click={() => signOut(auth)}>Sign out</button>