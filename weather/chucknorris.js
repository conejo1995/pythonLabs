// function getMeAJoke() {
//     $.ajax({
//         url: "http://api.icndb.com/jokes/random",
//         type: "GET",
//         success: function (data) {
//             $('#jokeNum').fadeOut(500, function () {
//                 $(this).text(data.value.id).fadeIn(500);
//             });
//             $('#jokeText').fadeOut(500, function () {
//                 $(this).text(data.value.joke).fadeIn(500)
//             })
//         }
//     });
// }
//
// $('#jokeButton').click(getMeAJoke);
//
// getMeAJoke();

var weatherConditions = {
    "clear sky":"url('http://media.istockphoto.com/photos/clear-sky-picture-id182355595?k=6&m=182355595&s=612x612&w=0&h=5JSpbxQLc71sEVOkGh0o1ypZGzr01KWR1QTJ6r3Gfz0=')",
    "few clouds":"url('http://canitbesaturdaynow.com/images/fpics/1679/033120bd5d2cfd5c05653a107622e41d.jpg')",
    "scattered clouds":"url('https://i.ytimg.com/vi/z2UDZMu2GLU/maxresdefault.jpg')",
    "broken clouds":"url('http://img13.deviantart.net/fa39/i/2015/052/6/1/broken_clouds_by_leo_6tos-d8ixdlv.jpg')",
    "shower rain":"url('http://www.mikeafford.com/store/store-images/re01_example_light_rain_showers.jpg')",
    "moderate rain":"url('http://legendsnation.com/wp-content/uploads/2016/05/rain-06.jpg')",
    "thunderstorm":"url('http://cdn.pcwallart.com/images/thunderstorm-rain-wallpaper-3.jpg')",
    "snow":"url('http://cdn2.hercampus.com/2016/01/17/snow1.jpg')",
    "mist":"url('https://vignette1.wikia.nocookie.net/demigodshaven/images/f/f5/Mist.jpg/revision/latest?cb=20110102163040')"

};

function searchByZip(zipCode) {
    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather",
        data: {
            zip: zipCode,
            APPID: 'b9774e52499b96ea73c942621f4efce3'
        },
        dataType: "jsonp",
        type: "post",
        success: function (data) {
            console.log(data)
            document.getElementById("body").style.backgroundImage = weatherConditions[data.weather[0].description];
            $('#kelvin').html(data.main.temp);
            var cel = data.main.temp - 273.15;
            $('#celsius').html(cel);
            var fah = cel * (9.0/5.0) + 32;
            $('#fahrenheit').html(fah);
        }
    });

}

function searchByCity(cityName) {
    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather",
        data: {
            q: cityName,
            APPID: 'b9774e52499b96ea73c942621f4efce3'
        },
        dataType: "jsonp",
        type: "post",
        success: function (data) {
            console.log(data)
            document.getElementById("body").style.backgroundImage = weatherConditions[data.weather[0].description];
            $('#kelvin').html(data.main.temp);
            var cel = data.main.temp - 273.15;
            $('#celsius').html(cel);
            var fah = cel * (9.0/5.0) + 32;
            $('#fahrenheit').html(fah);
        }
    });

}


document.getElementById('submit').addEventListener('click', function(){
    event.preventDefault();
    var cityOrZip = document.getElementById('cityOrZip').value;
    var searchValue = document.getElementById('searchValue').value;
    if(cityOrZip == 'zip'){
        searchByZip(searchValue);
    }
    if(cityOrZip == 'city'){
        searchByCity(searchValue);
    }
});