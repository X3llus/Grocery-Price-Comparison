import { findLatLonRange } from '$lib/utils';
import { db, collection, query, where, getDocs } from '$lib/firebase';
import type { Store } from '$lib/types';

export const setRegionalStores = async (lat: number, lon: number, radius: number): Promise<Store[]> => {
  if (haveStoresAlready(lat, lon, radius)) {
    const stores = getRegionalStores(lat, lon, radius);
    return stores;
  } else {
    const stores = await fetchRegionalStores(lat, lon, radius);
    addStoresToLocalStorage(stores);
    return stores;
  }
}

// Get stores from local storage that are within the given radius around the user's location
export const getRegionalStores = (lat: number, lon: number, radius: number): Store[] => {
  const savedStores = localStorage.getItem('regionalStores');
  if (!savedStores) return [];

  const regionalStores = JSON.parse(savedStores) as Store[];
  const { latMin, lonMin, latMax, lonMax } = findLatLonRange(lat, lon, radius);

  return regionalStores.filter((store) => {
    return store.geoPoint.latitude >= latMin
    && store.geoPoint.latitude <= latMax
    && store.geoPoint.longitude >= lonMin
    && store.geoPoint.longitude <= lonMax;
  });
}

const fetchRegionalStores = async (lat: number, lon: number, radius: number): Promise<Store[]> => {
  const { latMin, lonMin, latMax, lonMax } = findLatLonRange(lat, lon, radius);

  const q = query(
    collection(db, 'Stores'),
    where('geoPoint.longitude', '>=', lonMin),
    where('geoPoint.longitude', '<=', lonMax)
  );
  const querySnapshot = await getDocs(q);

  const stores = querySnapshot.docs.map((doc) => doc.data() as Store);
  return stores.filter((store) => {
    return store.geoPoint.latitude >= latMin && store.geoPoint.latitude <= latMax;
  });
};

// Returns true if the local storage stores are within the given radius of the user's location
const haveStoresAlready = (lat: number, lon: number, radius: number) => {
  try {
    const savedRegionalStores = JSON.parse(localStorage.getItem('regionalStores'));
    const { latMin, latMax, lonMin, lonMax } = findLatLonRange(lat, lon, radius);
    return savedRegionalStores.every((store: Store) => {
      return store.geoPoint.latitude >= latMin
        && store.geoPoint.latitude <= latMax
        && store.geoPoint.longitude >= lonMin
        && store.geoPoint.longitude <= lonMax;
    });
  } catch (error) {
    return false;
  }
}

const addStoresToLocalStorage = (stores: Store[]) => {
  try {
    const savedStores = JSON.parse(localStorage.getItem('regionalStores'));
    const newStores = savedStores.concat(stores);
    const uniqueStores = newStores.filter((store, index, self) => {
      return self.findIndex((s) => s.storeId === store.storeId) === index;
    });

    localStorage.setItem('regionalStores', JSON.stringify(uniqueStores));
  } catch (error) {
    localStorage.setItem('regionalStores', JSON.stringify(stores));
  }
};
