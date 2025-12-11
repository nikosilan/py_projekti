// Alusta Leaflet-kartta
const map = L.map('map').setView([60.1699, 24.9384], 6);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

let airportLayer = L.layerGroup().addTo(map);
let username = prompt("Anna käyttäjänimesi (niko, juuso, daniel, illia):") || "niko";
let currentLocation = null;
let currentLocationMarker = null;
/* const iframe = document.querySelector("#gameIframe"); */

// Hae satunnaiset lentokentät
function loadGameDestinations() {
    fetch(`http://127.0.0.1:5001/api/current_destinations`)
        .then(res => res.json())
        .then(destinations => {
            airportLayer.clearLayers();

            destinations.forEach(ap => {
                const marker = L.marker([ap.lat, ap.lon])
                    .addTo(airportLayer)
                    .bindPopup(`<b>${ap.name}</b><br>ICAO: ${ap.icao}<br>${ap.country}`);

                /* marker.on('click', () => {
                    if (!currentLocation) {
                        alert("Nykyistä sijaintia ei löytynyt!");
                        return;
                    }

                    iframe.contentWindow.postMessage({
                        action: "chooseAirport",
                        from: currentLocation,
                        to: ap
                    }, "*");

                    currentLocation = { icao: ap.icao, name: ap.name, lat: ap.lat, lon: ap.lon };
                }); */
            });
        })
        .catch(err => console.error("Kohteiden haku epäonnistui:", err));
}

// Hae nykyinen sijainti ja lisää markkeri
function mycurrentLocation() {
    fetch(`http://127.0.0.1:5001/api/current_location?username=${username}`)
        .then(res => res.json())
        .then(data => {
            if (data.lat && data.lon) {
                currentLocation = {icao: data.icao, name: data.name, lat: data.lat, lon: data.lon};
                if (currentLocationMarker) {
                    map.removeLayer(currentLocationMarker);
                }
                currentLocationMarker = L.marker([data.lat, data.lon], {
                    icon: L.icon({iconUrl: 'static/Images/current.png', iconSize: [30, 30]})
                }).addTo(map)
                    .bindPopup(`Nykyinen sijainti: ${data.name}`);
            }
        })
        .catch(err => console.error(err));
}

loadGameDestinations();
mycurrentLocation();

document.getElementById("refreshBtn").addEventListener("click", () => {
    loadGameDestinations();
    mycurrentLocation();
});
