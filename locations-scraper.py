# Scrape US locations only
# Check on the 1st of every month for new locations
# 
'''
Start at dollartree.com/locations
    Loop through each state (class=ga_w2gi_lp)
        Loop through each city (class=ga_w2gi_lp)
            Loop through each store (id="listings")
                Get information as csv? (Store #, Name, Address, Hours, Phone Number)
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
    print(state, end="\n"*2)

