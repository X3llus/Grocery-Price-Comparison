import { writable, get } from "svelte/store";
import { db, doc, updateDoc, onAuthStateChanged, getAuth } from '$lib/firebase.js';

export const searchStore = writable([]);

const auth = getAuth();

function createSearchListStore() {
    const { subscribe, set, update } = writable([]);

    function updateFirestore() {
        onAuthStateChanged(auth, (user) => {
            if (user) {
                const userRef = doc(db, "Users", user.uid);
                updateDoc(userRef, {
                    list: get(searchListStore),
                });
            }
        });
    }

    return {
        subscribe,
        set,
        update,
        add: (item: unknown) => {
            update((items) => {
                return [...items, item];
            });
            updateFirestore();
        },
        addMultiple: (items: unknown[]) => {
            update((currentItems) => {
                return [...currentItems, ...items];
            });
            updateFirestore();
        },
        remove: (index: number) => {
            update((items) => {
                return items.filter((_, i) => i !== index);
            });
            updateFirestore();
        }
    }
}

export const searchListStore = createSearchListStore();