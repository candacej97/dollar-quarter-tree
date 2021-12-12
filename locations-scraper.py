# Scrape US locations only

'''
Start at dollartree.com/locations
    Loop through each state (class=ga_w2gi_lp)
        Loop through each city (class=ga_w2gi_lp)
            Loop through each store (id="listings")
''' 

import requests
from bs4 import BeautifulSoup

URL = "https://dollartree.com/locations"
page = requests.get(URL)

# MUST encode, or else it won't output
# print(page.text.encode('utf-8'))

soup = BeautifulSoup(page.content, "html.parser")

# Find, loop through, and print each state (class=ga_w2gi_lp) 
states = soup.find_all("a", class_="ga_w2gi_lp")
for state in states:
    # print(state, end="\n"*2)
    
    # Get link to state page
    pageOfCities = requests.get(state["href"])
    citySoup = BeautifulSoup(pageOfCities.content, "html.parser")

    # Find, loop through, and print each city (class=ga_w2gi_lp) 
    cities = citySoup.find_all("a", class_="ga_w2gi_lp")
    for city in cities:
        print(city, end="\n"*2)

        # Get link to city page
        pageOfStores = requests.get(city["href"])
        storesSoup = BeautifulSoup(pageOfStores.content, "html.parser")

        # Find, loop through, and print each store (id="listings")
        stores = pageOfStores.find_all("a", id="listings")
        for store in stores:
            print(store, end="\n"*2)
