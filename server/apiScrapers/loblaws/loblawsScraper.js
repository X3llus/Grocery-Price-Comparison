const fs = require("fs");
const path = require("path");
const { catagories, getClosestStore } = require("./common");
const { storeLocations } = require("./data/loblaws-locations-canada");
const filePath = "./data/test-extraction-data.json";


// Variables
const lat = 44.58857;  // Lakehead Orillia latitude
const lng = -79.415588;  // Lakehead Orillia longitude
const category = "preparedMeals";
const timeBetweenRequests = 5000;  // Time between requests in milliseconds (so I don't get IP banned by Galen Weston Jr.)
const closestStore = getClosestStore(lat, lng, storeLocations);

const requestHeaders = {
  "Content-Type": "application/json",
  "x-apikey": "1im1hL52q9xvta16GlSdYDsTsG0dmyhF"  // Api key for the loblaws api... was not hidden in their public api calls
};

const baseRequestBody = {
  "storeId": closestStore.id,
  "banner": closestStore.storeBannerId,
  "lang": "en",
  "pickupType": "STORE",
  "date": new Date().toLocaleDateString("en-GB").replace(/\//g, ""), // Date in the format DDMMYYYY
  "offerType": "ALL",
  "cartId": "c807d16d-1138-4236-b555-c90793f37353",   // I think this is just a random uuid
  "categoryId": catagories[category],
};

const sleep = (milliseconds) => {
  return new Promise(resolve => setTimeout(resolve, milliseconds));
};

const getProducts = async (page = 0) => {
  const requestBody = {
    ...baseRequestBody,
    "pagination": {
      "from": page,  // page seems to be 0 indexed
      "size": 48
    }
  };

  const response = await fetch("https://api.pcexpress.ca/product-facade/v3/products/category/listing", {
    method: "POST",
    headers: requestHeaders,
    body: JSON.stringify(requestBody)
  });

  const data = await response.json();
  console.log(`Got ${data.results.length} products for page ${page}`);
  return data;
};

const getProductsForCategory = async () => {
  let page = 0;
  let products = [];

  const { results, pagination } = await getProducts(page);
  console.log(`Total products: ${pagination.totalResults}`)
  products = products.concat(results);

  while (products.length < pagination.totalResults) {
    page++;
    await sleep(timeBetweenRequests);
    const { results } = await getProducts(page);
    products = products.concat(results);
  }
  return products;
};

const main = async () => {
  const products = await getProductsForCategory();
  const existingFile = fs.readFileSync(path.resolve(__dirname, filePath), "utf8");

  if (existingFile.length === 0) {
    fs.writeFileSync(path.resolve(__dirname, filePath), JSON.stringify({ [category]: products }, null, 2)); 
  } else {
    const existingData = JSON.parse(existingFile);
    const data = {
      ...existingData,
      [category]: products
    };
    fs.writeFileSync(path.resolve(__dirname, filePath), JSON.stringify(data, null, 2));
  }
};

main();







