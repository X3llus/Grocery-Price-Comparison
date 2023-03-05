import mapbox from 'mapbox-gl';
import { PUBLIC_MAPBOX_ACCESS_TOKEN } from "$env/static/public";

mapbox.accessToken = PUBLIC_MAPBOX_ACCESS_TOKEN;

const key = Symbol();

export { mapbox, key };