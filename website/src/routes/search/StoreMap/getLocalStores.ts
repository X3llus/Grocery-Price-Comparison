import { findLatLonRange } from '$lib/utils';
import { db, collection, query, where, getDocs } from '$lib/firebase';
import type { Store } from '$lib/types';

export const getLocalStores = async (lat: number, lon: number, radius: number): Promise<Store[]> => {
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
