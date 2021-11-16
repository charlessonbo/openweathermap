$(document).ready(function () {
    var lat, lng;
    var map = L.map('map').setView([0,0],1)

    L.tileLayer('https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=iokfUVv9rgeWKrI9Vng4', 
    { 
        attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
    }).addTo(map)
  

    map.on('click', function(e){
        var lt = String(e.latlng.lat),
        lg = String(e.latlng.lng);
        var popup = L.popup()
          .setLatLng(e.latlng)
          .setContent(lt + " " + lg)
          .openOn(map);
      });
     


});


