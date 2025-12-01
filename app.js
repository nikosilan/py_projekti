// Alusta Leaflet-kartta
const map = L.map('map').setView([60.1699, 24.9384], 6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

// LayerGroup lentokentille
let airportLayer = L.layerGroup().addTo(map);

// Pelaajan lentojen määrä
const flight_count = 7;

// Hakee 3 satunnaista lentokenttää backendistä
function loadRandomDestinations() {
    fetch(`http://127.0.0.1:5000/api/random_destinations/${flight_count}`)
        .then(res => res.json())
        .then(destinations => {
            airportLayer.clearLayers();
            destinations.forEach(ap => {
                L.marker([ap.lat, ap.lon])
                    .addTo(airportLayer)
                    .bindPopup(`<b>${ap.name}</b><br>ICAO: ${ap.icao}<br>${ap.country}`);
            });
        })
        .catch(err => console.error(err));
}

// Hae heti kartan latautuessa
loadRandomDestinations();

// Päivitä, kun karttaa liikutetaan
map.on("moveend", loadRandomDestinations);
