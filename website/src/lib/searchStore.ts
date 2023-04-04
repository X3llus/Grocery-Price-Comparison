import { writable, get, type Updater } from "svelte/store";
import { db, doc, updateDoc, onAuthStateChanged, getAuth } from '$lib/firebase.js';
import { browser } from "$app/environment";

export const searchStore = writable([]);

const auth = getAuth();

function createSearchListStore() {
    const { subscribe, set, update } = writable(browser && (JSON.parse(localStorage.getItem('searchList')) || []));
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
searchListStore.subscribe((value) => browser && localStorage.setItem('searchList', JSON.stringify(value)));