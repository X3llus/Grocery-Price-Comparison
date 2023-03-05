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

export { }
