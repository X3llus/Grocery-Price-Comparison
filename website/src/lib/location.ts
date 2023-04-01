import { PUBLIC_MAPBOX_ACCESS_TOKEN } from "$env/static/public";

interface Location {
  latitude: number;
  longitude: number;
  city?: string;
  province?: string;
}

interface ReverseGeocodeResponse {
  city: string;
  province: string;
}

export const defaultLocation: Location = { 
  latitude: 44.58857,
  longitude: -79.415588,
  city: 'Orillia',
  province: 'ON'
};

// Get the user's location from local storage or navigator.geolocation
export const getLocation = (): Location => {
  try {
    navigator.geolocation.getCurrentPosition(setLocation, () => console.warn('Could not get location'));
    const savedLocation: Location = JSON.parse(localStorage.getItem('location'));
    return savedLocation || defaultLocation;
  } catch (error) {
    return defaultLocation;
  }
}

// Save the user's location to local storage with city and province
export const setLocation = async (position): Promise<Location> => {
  if (position.coords) {
    position.latitude = position.coords.latitude;
    position.longitude = position.coords.longitude;
  }

  if (!position.latitude && !position.longitude) {
    return defaultLocation;
  }

  const { latitude, longitude } = position;
  const location: Location = { latitude, longitude };

  if (position.city && position.province) {
    location.city = position.city;
    location.province = position.province;
  } else {
    try {
      const reverseGeocode = await getReverseGeocode(latitude, longitude);
      if (reverseGeocode) {
        const { city, province } = reverseGeocode;
        location.city = city;
        location.province = province;
      }
    } catch (error) {
      console.warn('Could not get user city and province');
    }
  }

  localStorage.setItem('location', JSON.stringify(location));
  return location;
}

const getReverseGeocode = async (lat: number, lng: number): Promise<ReverseGeocodeResponse> => {
  const url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${lng},${lat}.json?limit=1&access_token=${PUBLIC_MAPBOX_ACCESS_TOKEN}`;
  const response = await fetch(url);
  const data = await response.json();
  
  try {
    const place = data.features[0];
    const city = place.context.find((item) => item.id.includes('place')).text;
    const province = place.context.find((item) => item.id.includes('region')).text;
    const shortFormProvince = getStateShortForm(province);
    return {
      city,
      province: shortFormProvince,
    }
  } catch (error) {
    return {
      city: '',
      province: '',
    }
  }
}

const getStateShortForm = (state: string) => {
  const lowerCaseState = state.toLowerCase();
  if (lowerCaseState === 'ontario') return 'ON';
  if (lowerCaseState === 'quebec') return 'QC';
  if (lowerCaseState === 'nova scotia') return 'NS';
  if (lowerCaseState === 'new brunswick') return 'NB';
  if (lowerCaseState === 'manitoba') return 'MB';
  if (lowerCaseState === 'british columbia') return 'BC';
  if (lowerCaseState === 'prince edward island') return 'PE';
  if (lowerCaseState === 'saskatchewan') return 'SK';
  if (lowerCaseState === 'alberta') return 'AB';
  if (lowerCaseState === 'newfoundland and labrador') return 'NL';
  if (lowerCaseState === 'northwest territories') return 'NT';
  if (lowerCaseState === 'yukon') return 'YT';
  if (lowerCaseState === 'nunavut') return 'NU';
  return state;
}