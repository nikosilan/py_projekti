// Leaflet-kartan alustus
const map = L.map('map').setView([60.1699, 24.9384], 6);

// OpenStreetMap-laatta
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

// Käyttäjän sijainti markerina
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(pos => {
        const lat = pos.coords.latitude;
        const lon = pos.coords.longitude;

        L.marker([lat, lon], { title: "Sijaintisi" })
            .addTo(map)
            .bindPopup("📍 Olet tässä");

        map.setView([lat, lon], 9);
    });
}

// Hae lentokentät backendista
fetch("http://127.0.0.1:5000/api/airports")
    .then(res => res.json())
    .then(airports => {
        airports.forEach(ap => {
            L.marker([ap.lat, ap.lon])
                .addTo(map)
                .bindPopup(`<b>${ap.name}</b><br>ICAO: ${ap.icao}<br>Maa: ${ap.country}`);
        });
    })
    .catch(err => console.error("Lentokenttien haku epäonnistui:", err));
