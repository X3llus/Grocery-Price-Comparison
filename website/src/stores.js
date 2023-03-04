import { writable, derived } from "svelte/store";
import { getLocation, setLocation } from "$lib/location";
import { setRegionalStores } from "$lib/localStores";

export const userLocation = writable(getLocation());
export const searchRadius = writable(15);
export const localStores = derived([userLocation, searchRadius], async ([$userLocation, $searchRadius]) => {
  const { latitude, longitude } = $userLocation;
  const stores = await setRegionalStores(latitude, longitude, $searchRadius);
  return stores;
});

export const updateUserLocation = async (location = null) => {
  if (!location) 
    location = getLocation();
  
  // set in localStorage
  const newLocation = await setLocation(location);
  // set in store
  userLocation.set(newLocation);
};
