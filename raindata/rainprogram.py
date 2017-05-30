import requests
from bs4 import BeautifulSoup
import csv
import re
# r  = requests.post("https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain")
# print(r.url)
# print(r)
#
# soup = BeautifulSoup(r.text, "html.parser")
#
# print(soup.prettify())
#
#
# with open('saved_data2.txt', 'w') as new_file:
#     new_file.write(soup.prettify())

months = ['JAN', 'FEB', 'MAR', 'APR', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

running = True
while running:

    list_of_locations = []
    rain_data_by_date = {}

    r  = requests.post("https://or.water.usgs.gov/non-usgs/bes/")
    soup = BeautifulSoup(r.text, "html.parser")
    print("The available locations are: ")
    for link in soup.findAll('a'):
        if '.rain' in link.get('href'):
            print(link.get('href'))
            list_of_locations.append(link.get('href'))

    user_input = input("Which location would you like to see data for? (enter full name) ")
    for index in list_of_locations:
        if user_input in index:
            r  = requests.post("https://or.water.usgs.gov/non-usgs/bes/" + str(index))
            soup = BeautifulSoup(r.text, "html.parser")
            with open('saved_data.txt', 'w') as new_file:
                new_file.write(soup.prettify())



    f = open("saved_data.txt")
    for i, line in enumerate(f):
        if i > 12:
            str = line.strip(' ')
            print(str)
            # for value in str:
            #     for month in months:
            #         if month in value:
            #             print(value)
