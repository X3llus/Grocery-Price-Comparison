/* eslint-disable @typescript-eslint/no-explicit-any */
export type Product = {
  SKU: string
  name: string
  brand: string
  imageUrl: string
  packageSize: string
  parentCompany: string
  catagory?: string
}

export type NormalizedPrice = {
  quantity: number
  unit: string
  value: number
}

export type ProductPrice = {
  key: string
  dateExtracted: string
  inStock: boolean
  normalizedPrice: NormalizedPrice
  price: number
}

export type ProductWithPrice = Product & ProductPrice

export type GeoPoint = {
  latitude: number
  longitude: number
}

export type ShortGeoPoint = {
  lat: number
  lon: number
}

export type StoreAddress = {
  line1: string
  town: string
  region: string
  postcode: string
  country: string
  formattedAddress: string
}

export type Store = {
  storeId: string
  type: string
  address: StoreAddress
  geoPoint: GeoPoint
}

export type StorePrice = {
  _geoloc: ShortGeoPoint
  dateExtracted: string
  normalized: NormalizedPrice
  price: number
  storeId: string
  storeName: string
}

export interface Hit extends Record<string, any> {
  _geoloc: ShortGeoPoint[]
  brand: string,
  data: StorePrice[]
  imageUrl: string
  name: string
  objectID: string
  path: string
  size: any
  skus: string[]
  unit: string
}

export { }
