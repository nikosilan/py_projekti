// Alusta Leaflet-kartta
const map = L.map('map').setView([60.1699, 24.9384], 6);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

let airportLayer = L.layerGroup().addTo(map);
let username = prompt("Anna käyttäjänimesi (niko, juuso, daniel, illia):") || "niko";
const flight_count = 7;
let currentLocation = null;
const iframe = document.querySelector("#gameIframe");

// Hae satunnaiset lentokentät
function loadRandomDestinations() {
    fetch(`http://127.0.0.1:5000/api/random_destinations/${flight_count}?username=${username}`)
        .then(res => res.json())
        .then(destinations => {
            airportLayer.clearLayers();

            destinations.forEach(ap => {
                const marker = L.marker([ap.lat, ap.lon])
                    .addTo(airportLayer)
                    .bindPopup(`<b>${ap.name}</b><br>ICAO: ${ap.icao}<br>${ap.country}`);

                marker.on('click', () => {
                    if (!currentLocation) {
                        alert("Nykyistä sijaintia ei löytynyt!");
                        return;
                    }

                    // Lähetä viesti iframe-pelille
                    iframe.contentWindow.postMessage({
                        action: "chooseAirport",
                        from: currentLocation,
                        to: ap
                    }, "*");

                    currentLocation = { icao: ap.icao, name: ap.name, lat: ap.lat, lon: ap.lon };
                });
            });
        })
        .catch(err => console.error("Kohteiden haku epäonnistui:", err));
}

// Hae nykyinen sijainti ja lisää markkeri
fetch(`http://127.0.0.1:5000/api/current_location?username=${username}`)
    .then(res => res.json())
    .then(data => {
        if (data.lat && data.lon) {
            currentLocation = { icao: data.icao, name: data.name, lat: data.lat, lon: data.lon };
            L.marker([data.lat, data.lon], {
                icon: L.icon({ iconUrl: 'current.png', iconSize: [30,30] })
            }).addTo(map)
              .bindPopup(`Nykyinen sijainti: ${data.name}`);
        }
    })
    .catch(err => console.error(err));

loadRandomDestinations();
document.getElementById("refreshBtn").addEventListener("click", loadRandomDestinations);
