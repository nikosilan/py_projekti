// Alusta Leaflet-kartta
const map = L.map('map').setView([60.1699, 24.9384], 6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

// LayerGroup lentokentille
let airportLayer = L.layerGroup().addTo(map);

// Kysy käyttäjänimi heti sivun latautuessa
let username = prompt("Anna käyttäjänimesi (niko, juuso, daniel, illia):") || "niko";

// Pelaajan lentojen määrä (voit hakea GameState:sta myöhemmin)
const flight_count = 7;

// Nykyinen sijainti (päivittyy lennon jälkeen)
let currentLocation = null;

// Funktio hakee 3 satunnaista lentokenttää backendistä
function loadRandomDestinations() {
    fetch(`http://127.0.0.1:5000/api/random_destinations/${flight_count}?username=${username}`)
        .then(res => res.json())
        .then(destinations => {
            airportLayer.clearLayers();

            destinations.forEach(ap => {
                const marker = L.marker([ap.lat, ap.lon])
                    .addTo(airportLayer)
                    .bindPopup(`<b>${ap.name}</b><br>ICAO: ${ap.icao}<br>${ap.country}`);

                // Klikkaa markeria -> tallenna valittu kenttä ja laske matka
                marker.on('click', () => {
                    if (!currentLocation) {
                        alert("Nykyistä sijaintia ei löytynyt!");
                        return;
                    }

                    fetch(`http://127.0.0.1:5000/api/set_destination`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ username: username, icao: ap.icao })
                    })
                    .then(res => res.json())
                    .then(data => {
                        if (data.success && data.distance_km !== undefined) {
                            console.log("SERVERIN VASTAUS:", data);
                            alert(
                                `Lähtö: ${currentLocation.name} (${currentLocation.icao})\n` +
                                `Kohde: ${ap.name} (${ap.icao})\n` +
                                `Matka: ${data.distance_km.toFixed(2)} km`
                            );

                            // Päivitä nykyinen sijainti
                            currentLocation = { icao: ap.icao, name: ap.name, lat: ap.lat, lon: ap.lon };
                        } else {
                            alert(`Virhe: ${data.message}`);
                        }
                    })
                    .catch(err => console.error(err));
                });
            });
        })
        .catch(err => console.error("Kohteiden haku epäonnistui:", err));
}

// Hae nykyinen sijainti ja näytä markkeri
fetch(`http://127.0.0.1:5000/api/current_location?username=${username}`)
    .then(res => res.json())
    .then(data => {
        if (data.lat && data.lon) {
            console.log(`Nykyinen sijainti: ${data.name} (${data.icao})`);
            currentLocation = { icao: data.icao, name: data.name, lat: data.lat, lon: data.lon };

            L.marker([data.lat, data.lon], {
                icon: L.icon({ iconUrl: 'current.png', iconSize: [30, 30] })
            }).addTo(map)
              .bindPopup(`Nykyinen sijainti: ${data.name}`);
        }
    })
    .catch(err => console.error(err));

// Hae heti kartan latautuessa
loadRandomDestinations();

// Päivitä, kun nappia klikataan
document.getElementById("refreshBtn").addEventListener("click", loadRandomDestinations);
