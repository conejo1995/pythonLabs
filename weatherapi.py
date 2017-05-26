# # {
# "coord": {
# "lon": -0.13,
# "lat": 51.51
# },
# "weather": [
# {
# "id": 800,
# "main": "Clear",
# "description": "clear sky",
# "icon": "01n"
# }
# ],
# "base": "stations",
# "main": {
# "temp": 288.51,
# "pressure": 1022,
# "humidity": 72,
# "temp_min": 286.15,
# "temp_max": 290.15
# },
# "visibility": 10000,
# "wind": {
# "speed": 4.6,
# "deg": 80
# },
# "clouds": {
# "all": 0
# },
# "dt": 1495749000,
# "sys": {
# "type": 1,
# "id": 5091,
# "message": 0.0042,
# "country": "GB",
# "sunrise": 1495684474,
# "sunset": 1495742482
# },
# "id": 2643743,
# "name": "London",
# "cod": 200
# }
"""
As a user I want to be able to enter my city or zip code
and recieve my temp in C or F.

As a user I want to know what condition it is outside.
"""
#
# print(r.url)
# print(json_data)
# print(r)

import requests

# package = {
#     'APPID': "b9774e52499b96ea73c942621f4efce3",
#      'q': 'london',
#     'zip' : '97030'
# }
searching = True
while searching:
    want_to_search = True
    zip_or_city = ''
    while want_to_search:
        answer = input("Would you like to search? (yes or no) ")
        answer = answer.lower()
        if answer == 'yes':
            want_to_search = False
            type_of_search = True
            while type_of_search:
                zip_or_city = input("Search by zip or by city?")
                zip_or_city = zip_or_city.lower()
                if zip_or_city == 'zip':
                    type_of_search = False
                    print("Search by zip code: ")
                elif zip_or_city == 'city':
                    type_of_search = False
                    zip_or_city = 'q'
                    print("Search by city: ")
                else:
                    print("Enter a valid response ")

        elif answer == 'no':
            quit()
        else:
            print("Enter a valid response ")

    package = {
        'APPID': "b9774e52499b96ea73c942621f4efce3",
    }
    search_value = input()
    if zip_or_city == 'zip':
        package[zip_or_city] = search_value
    elif zip_or_city == 'q':
        package[zip_or_city] = search_value
    r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)
    json_data = r.json()

    print("The weather is: " + str(json_data['main']['temp']) + "Kelvin")
    celsius = int(json_data['main']['temp']) - 273
    farenheit = (9/5) * celsius + 32


    print(str(celsius) + " Celsius")
    print(str(farenheit) + "Farenheit")
    # print(r.url)
    # print(json_data)
    # print(r)

    del package[zip_or_city]
