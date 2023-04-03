import { writable } from "svelte/store";
import type firebase from "firebase/app";

const authStore = writable<{
  isLoggedIn: boolean;
  user?: unknown;
  firebaseControlled: boolean;
}>({
  isLoggedIn: false,
  firebaseControlled: false,
});

export default {
  subscribe: authStore.subscribe,
  set: authStore.set,
};