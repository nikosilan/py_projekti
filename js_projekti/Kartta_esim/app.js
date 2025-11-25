// Luo Leaflet-kartta
var map = L.map('map').setView([60.1699, 24.9384], 6);

// OpenStreetMap layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

// Klikkaus kartalla
map.on('click', async function(e) {
    const lat = e.latlng.lat;
    const lon = e.latlng.lng;

    const res = await fetch("/api/saa", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ lat, lon })
    });

    const data = await res.json();

    document.getElementById("saaInfo").innerText =
        `Sijainti: ${lat.toFixed(2)}, ${lon.toFixed(2)}\n` +
        `Sää: ${data.saa}\n` +
        `Lämpötila: ${data.lampotila} °C`;
});
