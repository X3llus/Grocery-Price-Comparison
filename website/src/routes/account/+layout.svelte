<script>
    import { onMount } from 'svelte';
    import { getAuth, onAuthStateChanged, signOut, getDoc, doc, db, collection, addDoc, setDoc } from '$lib/firebase';
	import { goto } from '$app/navigation';

    let auth = getAuth();

    onMount(() => {
        onAuthStateChanged(auth, async (user) => {
        if (user) {
            const uid = user.uid;
            
            // Attempt to get user data from firestore
            const docRef = doc(db, 'Users', uid);
            const docSnap = await getDoc(docRef);
            if (docSnap.exists()) {
                console.log('Document data:', docSnap.data());
                // add data to user store and load list

            } else {
                // setup base document
                console.log('No such document!');
                const newDoc = await setDoc(doc(db, 'Users', uid), {
                    owner: uid,
                    list: [],
                });
            }

        } else {
            // User is signed out
            console.log('signed out');
        }
        });
    });

    // Sign out
    function signout() {
        signOut(auth);
        goto('/account/signin');
    }
</script>

<!-- basic head bar -->
<header class="flex">
    <h1>Account</h1>
    <nav>
        <a href="/account">Home</a>
        <a href="/account/profile">Profile</a>
        <a href="/account/settings">Settings</a>
        <button on:click={signout}>Sign out</button>
    </nav>
</header>

<slot />