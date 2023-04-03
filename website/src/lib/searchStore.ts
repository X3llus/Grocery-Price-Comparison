import { writable, get, type Updater } from "svelte/store";
import { db, doc, updateDoc, onAuthStateChanged, getAuth } from '$lib/firebase.js';

export const searchStore = writable([]);

const auth = getAuth();

function createSearchListStore() {
    const { subscribe, set, update } = writable([]);
    let uid;

    onAuthStateChanged(auth, (user) => {
        if (user) {
            uid = user.uid;
        }
    });


    function updateFirestore() {
        const userRef = doc(db, "Users", uid);
        updateDoc(userRef, {
            list: get(searchListStore),
        });
    }

    return {
        subscribe,
        set,
        update,
        add: (updater: Updater<any[]>) => {
            update(updater);
            updateFirestore();
        },
    }
}

export const searchListStore = createSearchListStore();