var mymap = L.map('mapid').setView([60.1699, 24.9384], 6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 4,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors'
}).addTo(mymap);

L.marker([60.1699, 24.9384]).addTo(mymap);
L.marker([59.3293, 18.0686]).addTo(mymap);
L.marker([59.9139, 10.7522]).addTo(mymap);
L.marker([46.8182, 8.2275]).addTo(mymap);