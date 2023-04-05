import type { Hit } from '$lib/types';

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

interface MapIcon {
  file: string;
  width: number;
  height: number;
}

export const getMapIcon = (storeType: string): MapIcon => {
  const lowerType = storeType.toLowerCase();
  switch (lowerType) {
    case 'walmart':
      return {
        file: 'WalmartMapIcon.png',
        width: 40,
        height: 27,
      }
    case 'loblaws':
      return {
        file: 'LoblawsMapIcon.png',
        width: 32,
        height: 32,
      }
    case 'metro':
      return {
        file: 'MetroMapIcon.png',
        width: 32,
        height: 32,
      }
    default:
      return {
        file: 'LoblawsMapIcon.png',
        width: 32,
        height: 32,
      }
    }
  }

export const getCardIcon = (storeType: string): string => {
  const lowerType = storeType.toLowerCase();
  switch (lowerType) {
    case 'walmart':
      return 'WalmartCardIcon.png';
    case 'loblaws':
      return 'LoblawsCardIcon.png';
    case 'metro':
      return 'MetroCardIcon.png';
    default:
      return 'LoblawsCardIcon.png';
  }
}

export const correctInvalidUnits = (hits: Hit[]): Hit[] => {
  const correctedHits = [];

  for (const hit of hits) {
    const isMl = hit.unit === 'ml';
    const isG = hit.unit === 'g';
    if (isMl || isG) {
      // This was likely intended to be L or Kg
      if (hit.size < 5) {
        hit.unit = isMl ? 'l' : 'kg';
        console.log(`Corrected unit for ${hit.name} to ${hit.unit}`)
      }
      
      // If size for example is 10200ml
      // This was likely intended to be X amount of mL or g
      else if (hit.size > 1000) {
        const asString = hit.size.toString();
        const sizeOfIndividualUnit = asString.substring(asString.length - 3);
        const numUnits = asString.substring(0, asString.length - 3);
        hit.size = `${numUnits} x ${sizeOfIndividualUnit}`
        console.log(`Corrected size for ${hit.name} to ${hit.size}`);
      }
    }
    correctedHits.push(hit);
  }
  return correctedHits;
}