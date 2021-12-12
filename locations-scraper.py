# Scrape US locations only

'''
Start at dollartree.com/locations
    Loop through each state (class=ga_w2gi_lp)
        Loop through each city (class=ga_w2gi_lp)
            Loop through each store (id="listings")
''' 

import requests
from bs4 import BeautifulSoup
import json

URL = "https://dollartree.com/locations"
page = requests.get(URL)

# MUST encode, or else it won't output
# print(page.text.encode('utf-8'))

soup = BeautifulSoup(page.content, "html.parser")
data = {}

# Find, loop through, and print each state (class=ga_w2gi_lp) 
states = soup.find_all("a", class_="ga_w2gi_lp")
for state in states:
    # print(state, end="\n"*2)

    if state.text == "Home" or state.text == "Store Locator":
        continue

    data[state.text] = []

    # Get link to state page
    pageOfCities = requests.get(state["href"])
    citySoup = BeautifulSoup(pageOfCities.content, "html.parser")

    # Find, loop through, and print each city (class=ga_w2gi_lp) 
    cities = citySoup.find_all("a", class_="ga_w2gi_lp")
    for city in cities:
        # print(city, end="\n"*2)

        # Get link to city page
        pageOfStores = requests.get(city["href"])
        storesSoup = BeautifulSoup(pageOfStores.content, "html.parser")

        # Find, loop through, and print each store (class="schemastore")
        stores = storesSoup.find_all("div", class_="item_div")
        for store in stores:
            # print(store, end="\n"*2)

            # Get name and address of location
            print(store.contents[1].text)
            # print(store.contents[4])
            print("{}, {}, {} {}".format(store.contents[4].contents[1].text, store.contents[4].contents[4].text, store.contents[4].contents[6].text, store.contents[4].contents[8].text))

            name = store.contents[1].text
            address = "{}, {}, {} {}".format(store.contents[4].contents[1].text, store.contents[4].contents[4].text, store.contents[4].contents[6].text, store.contents[4].contents[8].text)

            data[state.text].append({
                "name": name,
                "address": address,
                "base": 1.00
            })

with open('stores.json', 'w') as outfile:
    json.dump(data, outfile)