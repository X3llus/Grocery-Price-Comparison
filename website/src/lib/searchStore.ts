import { writable, get } from "svelte/store";
import { db, doc, updateDoc, onAuthStateChanged, getAuth } from '$lib/firebase.js';

export const searchStore = writable([]);
// export const searchListStore = writable([]);

const auth = getAuth();

function createSearchListStore() {
    const { subscribe, set, update } = writable([]);

    return {
        subscribe,
        set,
        update,
        add: (item: unknown) => {
            update((items) => {
                return [...items, item];
            });
            onAuthStateChanged(auth, (user) => {
                if (user) {
                    const userRef = doc(db, "Users", user.uid);
                    updateDoc(userRef, {
                        list: get(searchListStore),
                    });
                }
            });
        },
        remove: (index: number) => {
            update((items) => {
                return items.filter((_, i) => i !== index);
            });
            onAuthStateChanged(auth, (user) => {
                if (user) {
                    const userRef = doc(db, "Users", user.uid);
                    updateDoc(userRef, {
                        list: get(searchListStore),
                    });
                }
            });
        }
    }
}

export const searchListStore = createSearchListStore();