<script>
	// import auth and firestore libraries from $lib/firebase.js
	import {
		app,
		getAuth,
		createUserWithEmailAndPassword,
		signInWithEmailAndPassword,
		sendPasswordResetEmail,
		signOut,
		onAuthStateChanged,
		GoogleAuthProvider,
		signInWithPopup,
		doc,
		getDoc,
		db,
		setDoc,
	} from '$lib/firebase';

	import Login from 'svelte-material-icons/Login.svelte';
	import AccountPlus from 'svelte-material-icons/AccountPlus.svelte';
	import Google from 'svelte-material-icons/Google.svelte';
	import { goto } from '$app/navigation';
	import { searchListStore } from '$lib/searchStore';
	import { get } from 'svelte/store';
	import { isEqual } from 'lodash-es';

	// vars
	let email = '';
	let password = '';
	let confirmPassword = '';
	let error = '';
	let success = '';
	let auth = getAuth(app);
	const provider = new GoogleAuthProvider();

	let state = 0; // 0 = initial, 1 = sign in, 2 = register, 3 = reset password, 4 = already signed in

	function arraysEqual(a, b) {
		if (a === b) return true;
		if (a == null || b == null) return false;
		if (a.length !== b.length) return false;

		// If you don't care about the order of the elements inside
		// the array, you should sort both arrays here.
		// Please note that calling sort on an array will modify that array.
		// you might want to clone your array first.

		for (let i = 0; i < a.length; ++i) {
			if (a[i] !== b[i]) return false;
		}
		return true;
	}

	onAuthStateChanged(auth, async (user) => {
		if (!user) {
			// User is signed out
			state = 0;
			return;
		}

		console.log('pogging');

		const uid = user.uid;
		state = 4;
		email = user.email;

		// Attempt to get user data from firestore
		const docRef = doc(db, 'Users', uid);
		const docSnap = await getDoc(docRef);

		if (docSnap.exists()) {
			if (isEqual(docSnap.data().list, get(searchListStore))) return console.log('data matches');
			// return searchListStore.update((value) => {
			// 	console.log([...value, ...docSnap.data().list]);
			// 	return [...value, ...docSnap.data().list];
			// });
			return searchListStore.set(docSnap.data().list);
		}

		// setup base document
		const newDoc = await setDoc(doc(db, 'Users', uid), {
			owner: uid,
			list: [],
		});
	});

	// Sign in with email and password
	async function signinEmail() {
		signInWithEmailAndPassword(auth, email, password);
	}

	// Sign in with Google
	async function signinGoogle() {
		try {
			let result = await signInWithPopup(auth, provider);
			const credential = GoogleAuthProvider.credentialFromResult(result);
			const token = credential.accessToken;
			const user = result.user;
		} catch (e) {
			if (e.code === 'auth/account-exists-with-different-credential') {
				error = 'Account already exists with different credentials';
			} else if (e.code === 'auth/invalid-credential') {
				error = 'Invalid credentials';
			} else if (e.code === 'auth/operation-not-allowed') {
				error = 'Operation not allowed';
			} else if (e.code === 'auth/user-disabled') {
				error = 'User disabled';
			} else if (e.code === 'auth/user-not-found') {
				error = 'User not found';
			} else if (e.code === 'auth/wrong-password') {
				error = 'Wrong password';
			} else {
				error = 'Something went wrong';
			}
		}
	}

	// register new user with email and password
	async function register() {
		if (password !== confirmPassword) {
			return (error = 'Passwords do not match');
		}

		try {
			const userCredential = await createUserWithEmailAndPassword(auth, email, password);
			const user = userCredential.user;
			// await updateProfile(user, { displayName: name });
		} catch (e) {
			if (e.code === 'auth/email-already-in-use') {
				error = 'Email already in use';
			} else if (e.code === 'auth/invalid-email') {
				error = 'Invalid email';
			} else if (e.code === 'auth/weak-password') {
				error = 'Password is too weak';
			} else {
				error = 'Something went wrong';
			}
		}
	}

	// send password reset email
	async function resetPassword() {
		try {
			await sendPasswordResetEmail(auth, email);
			success = 'Password reset email sent';
			error = '';
		} catch (e) {
			if (e.code === 'auth/invalid-email') {
				error = 'Invalid email';
			} else if (e.code === 'auth/user-not-found') {
				error = 'User not found';
			} else {
				error = 'Something went wrong';
			}
		}
	}
	let screenSize;
	let screenSmall = 640;
</script>

<svelte:window bind:innerWidth={screenSize} />

<!-- give options to either sign in or register -->
<div class="h-screen w-screen align-middle flex content-center justify-around" style={ screenSize > screenSmall ? "background-image: url(../../background.svg);" : "" }>
	<div class="flex flex-col w-min h-min p-1 sm:pb-32 sm:px-24 sm:pt-16 sm:border-2 mx-2 my-auto sm:rounded-3xl sm:shadow-xl sm:m-auto sm:bg-white">
		{#if state === 0}
			<div class="space-y-4">
				<img src="GroceriezLogo.svg" alt="" class="mx-auto">
				<h1 class="text-5xl font-semibold text-black py-4 w-full text-center">Sign In</h1>
				<button
					on:click={() => (state = 1)}
					class="btn btn-primary w-56 mx-10 bg-primary text-white p-4 text-center rounded-full  flex justify-around"
					><Login width={21} height={21} />Sign in with Email</button
				>
				<button
					on:click={signinGoogle}
					class="btn btn-primary w-56 mx-10 bg-primary text-white p-4 text-center rounded-full flex justify-around"
					><Google width={21} height={21} />Sign in with Google</button
				>
				<button
					on:click={() => (state = 2)}
					class="btn btn-primary w-56 mx-10 bg-primary text-white p-4 text-center rounded-full  flex justify-around"
					><AccountPlus width={21} height={21} />Register with Email</button
				>
				<button
					on:click={() => goto('/search')}
					class="btn btn-primary w-56 mx-10 bg-secondary text-white p-4 text-center rounded-full font-semibold flex justify-around"
					>Search</button
				>
			</div>
		{:else if state === 1}
			<!-- Email Sign In -->
			<div class="space-y-4 flex flex-col">
				<h2 class="text-xl font-semibold text-black w-full text-center">Sign In with Email</h2>
				<input
					type="email"
					bind:value={email}
					placeholder="Email"
					class="w-56 h-10 text-lg border-2 rounded-md mx-auto"
				/>
				<input
					type="password"
					bind:value={password}
					placeholder="Password"
					class="w-56 h-10 text-lg border-2 rounded-md mx-auto"
				/>
				<button
					on:click={signinEmail}
					class="btn btn-primary w-56 mx-10 bg-primary text-white p-1 text-center rounded-full"
					>Sign in</button
				>
				<button
					on:click={() => (state = 3)}
					class="btn btn-primary w-56 mx-10 bg-primary text-white p-1 text-center rounded-full"
					>Reset Password</button
				>
				<button
					on:click={() => (state = 0)}
					class="btn btn-primary w-56 mx-10 bg-primary text-white p-1 text-center rounded-full"
					>Back</button
				>
				{#if error}
					<div class="text-red-500 text-center">{error}</div>
				{/if}
			</div>
		{:else if state === 2}
			<!-- Email Register -->
			<div class="space-y-4 flex flex-col">
				<h2 class="text-xl font-semibold text-black w-full text-center">Register with Email</h2>
				<input
					type="email"
					bind:value={email}
					placeholder="Email"
					class="w-56 h-10 text-lg border-2 rounded-md mx-auto"
				/>
				<input
					type="password"
					bind:value={password}
					placeholder="Password"
					class="w-56 h-10 text-lg border-2 rounded-md mx-auto"
				/>
				<input
					type="password"
					bind:value={confirmPassword}
					placeholder="Confirm Password"
					class="w-56 h-10 text-lg border-2 rounded-md mx-auto"
				/>
				<button
					on:click={register}
					class="btn btn-primary w-56 mx-10 bg-primary text-white p-1 text-center rounded-full"
					>Register</button
				>
				<button
					on:click={() => (state = 0)}
					class="btn btn-primary w-56 mx-10 bg-primary text-white p-1 text-center rounded-full"
					>Back</button
				>
				{#if error}
					<div class="text-red-500 text-center">{error}</div>
				{/if}
			</div>
		{:else if state === 3}
			<!-- Reset Password -->
			<div class="space-y-4 flex flex-col">
				<h2 class="text-xl font-semibold text-black w-full text-center">Reset Password</h2>
				<input
					type="email"
					bind:value={email}
					placeholder="Email"
					class="w-56 h-10 text-lg border-2 rounded-md mx-auto"
				/>
				<button
					on:click={resetPassword}
					class="btn btn-primary w-56 mx-10 bg-primary text-white p-1 text-center rounded-full"
					>Reset Password</button
				>
				<button
					on:click={() => (state = 0)}
					class="btn btn-primary w-56 mx-10 bg-primary text-white p-1 text-center rounded-full"
					>Back</button
				>
				{#if error}
					<div class="text-red-500 text-center">{error}</div>
				{/if}
				{#if success}
					<div class="text-primary text-center">{success}</div>
				{/if}
			</div>
		{:else if state === 4}
			<!-- Already Signed In -->
			<div class="space-y-4 flex flex-col">
				<h2 class="text-2xl font-semibold text-black w-full text-center">You are already signed in,</h2>
				<div class="text-lg text-primary font-bold text-center">{email}</div>
				<div class="text-md text-center">
					Your shopping list will be synced automatically across all signed in devices :)
				</div>
				<button
					on:click={() => goto('/search')}
					class="btn btn-primary w-56 mx-10 bg-primary text-white p-1 text-center rounded-full"
					>Go To Search</button
				>
				<button
					on:click={() => signOut(auth)}
					class="btn btn-primary w-56 mx-10 bg-secondary text-white p-1 text-center rounded-full"
					>Sign Out</button
				>
			</div>
		{/if}
	</div>
</div>
