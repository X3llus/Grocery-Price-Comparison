# Grocery Price Comparison

This project is designed to help users compare prices of groceries at local stores, enabling them to make more informed decisions about where to buy their groceries.

## Features

### Website

The website is built using Sveltekit, Tailwindcss, Firebase, Mapbox, and Algolia. It allows users to search for grocery products and compare prices across multiple local stores.

To run the website, follow these steps:

1. Clone the repository to your local machine
2. Navigate to the website directory: `cd website`
3. Install the necessary dependencies: `npm install`
4. Set up the environment variables by creating a `.env` file in the root directory of the website and filling it with the following:

PUBLIC_MAPBOX_ACCESS_TOKEN=YOUR_MAPBOX_ACCESS_TOKEN
VITE_ALGOLIA_APP_ID=YOUR_ALGOLIA_APP_ID
VITE_ALGOLIA_SEARCH_KEY=YOUR_ALGOLIA_SEARCH_KEY

Make sure to replace `YOUR_MAPBOX_ACCESS_TOKEN`, `YOUR_ALGOLIA_APP_ID`, and `YOUR_ALGOLIA_SEARCH_KEY` with the appropriate values from your Mapbox and Algolia accounts.

5. Set up Firebase credentials by editing `/website/src/lib/firebase.js` with your Firebase credentials.

6. Start the development server: `npm run dev`

The website will be accessible at `http://localhost:5173`.

### Server

The server is built with Python and is responsible for scraping product prices from various websites. The scraped data is stored in a Firebase Firestore database and accessed via the website.

To run the server, follow these steps:

1. Navigate to the `scrapers` directory: `cd scrapers`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Run the scraper: `python ./main.py`

### Issues

If you encounter any issues or have feature requests, please create a new issue in the GitHub repository. We have provided issue templates for both bugs and feature requests to ensure that all necessary information is included.

### Hosting

The website is hosted on Netlify using continuous deployment. Whenever changes are pushed to the main branch of the GitHub repository, the website is automatically rebuilt and redeployed on Netlify.

The data for this project is hosted in a Firebase Firestore database, and user accounts are managed using Firebase Auth. Please see the Firebase documentation for more information on how to set up and manage Firebase services.
