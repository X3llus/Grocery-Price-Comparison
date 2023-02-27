interface Location {
  latitude: number;
  longitude: number;
}

const defaultLocation: Location = { latitude: 44.58857, longitude: -79.415588 };

const saveLocation = (position) => {
  const { latitude, longitude } = position.coords;
  const location = { latitude, longitude };
  localStorage.setItem('location', JSON.stringify(location));
}

export const getLocation = (): Location => {
  navigator.geolocation.getCurrentPosition(saveLocation, () => console.warn('Could not get location'));
  const savedLocation: Location = JSON.parse(localStorage.getItem('location'));
  return savedLocation || defaultLocation;
}