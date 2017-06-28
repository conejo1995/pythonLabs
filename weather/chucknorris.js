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
    "01d":"url('http://openweathermap.org/img/w/01d.png')",
    "02d":"url('http://openweathermap.org/img/w/02d.png')",
    "03d":"url('http://openweathermap.org/img/w/03d.png')",
    "04d":"url('http://openweathermap.org/img/w/04d.png')",
    "09d":"url('http://openweathermap.org/img/w/09d.png')",
    "10d":"url('http://openweathermap.org/img/w/10d.png')",
    "11d":"url('http://openweathermap.org/img/w/11d.png')",
    "13d":"url('http://openweathermap.org/img/w/13d.png')",
    "50d":"url('http://openweathermap.org/img/w/50d.png')",
    "01n":"url('http://openweathermap.org/img/w/01n.png')",
    "02n":"url('http://openweathermap.org/img/w/02n.png')",
    "03n":"url('http://openweathermap.org/img/w/03n.png')",
    "04n":"url('http://openweathermap.org/img/w/04n.png')",
    "09n":"url('http://openweathermap.org/img/w/09n.png')",
    "10n":"url('http://openweathermap.org/img/w/10n.png')",
    "11n":"url('http://openweathermap.org/img/w/11n.png')",
    "13n":"url('http://openweathermap.org/img/w/13n.png')",
    "50n":"url('http://openweathermap.org/img/w/50n.png')"

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
            var id = data.weather[0].id;


            document.getElementById("body").style.backgroundImage = weatherConditions[data.weather[0].icon];
            $("#weather").html(data.weather[0].description);



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