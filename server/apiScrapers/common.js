const distanceBetweenCoords = (lat1, lon1, lat2, lon2, unit) => {
  var radlat1 = Math.PI * lat1/180
  var radlat2 = Math.PI * lat2/180
  var theta = lon1-lon2
  var radtheta = Math.PI * theta/180
  var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
  if (dist > 1) {
      dist = 1;
  }
  dist = Math.acos(dist)
  dist = dist * 180/Math.PI
  dist = dist * 60 * 1.1515
  if (unit=="K") { dist = dist * 1.609344 } // convert to kilometers
  if (unit=="N") { dist = dist * 0.8684 }  // convert to nautical miles
  return dist;
};

const getClosestStore = (userLat, userLng, stores) => {
  let closestStore = null;
  let closestDistance = Infinity;

  for (const store of stores) {
    const distance = distanceBetweenCoords(userLat, userLng, store.geoPoint.latitude, store.geoPoint.longitude, "K");
    if (distance < closestDistance) {
      closestDistance = distance;
      closestStore = store;
    }
  }

  // properties of Loblaws stores
  if (closestStore.storeBannerId && closestStore.name) {
    console.log(`Closest store is a ${closestStore.storeBannerId} in ${closestStore.name} at ${closestDistance}km away`);
  } else {
    console.log(`Closest store is ${closestDistance}km away`);
  }

  return closestStore;
};

module.exports = {
  catagories,
  getClosestStore,
};