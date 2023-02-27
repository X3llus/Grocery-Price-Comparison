import mapbox from 'mapbox-gl';

mapbox.accessToken = 'pk.eyJ1IjoidHlsZXJmcmV0eiIsImEiOiJjbGVrY29iNDUwa2czNDRwYnZ4am54MnV4In0.Hv122UgQk9YVD-R5u54UAw'
import.meta.env.MAPBOX_ACCESS_TOKEN;

const key = Symbol();

export { mapbox, key };