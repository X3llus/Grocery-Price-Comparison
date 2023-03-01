export const findLatLonRange = (centerLat: number, centerLon: number, radiusKm: number) => {
  const d_lat = radiusKm / 111.045
  const latitude_min = centerLat - d_lat
  const latitude_max = centerLat + d_lat
  
  const dlon = radiusKm / (111.045 * Math.cos(centerLat * (Math.PI/180)))
  const lonitude_min = centerLon - dlon
  const lonitude_max = centerLon + dlon
  
  return  {
    "latMin": latitude_min,
    "latMax": latitude_max,
    "lonMin": lonitude_min,
    "lonMax": lonitude_max
  }
}

// http://wiki.openstreetmap.org/wiki/Zoom_levels
const metersPerPixel = (lat, zoom) => {
  const earthCircumference = 40_075_016.686; // in meters
  const latitudeRadians = (lat * Math.PI) / 180;
  return (earthCircumference * Math.cos(latitudeRadians)) / Math.pow(2, zoom + 8);
}

export const kmToPixels = (lat, zoom, km) => {
  const meters = km * 1000;
  const pixels = meters / metersPerPixel(lat, zoom);
  return pixels * 2;
}