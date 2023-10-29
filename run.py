import json
import requests
from bs4 import BeautifulSoup
from handlers.autotrader import AutotraderHandler
from handlers.html import HTMLHandler

SIZE = 1000

BASE_URL = 'https://www.autotrader.ca/cars/on/ottawa'
PROVINCE = 'Ontario'
CITY = 'Ottawa'
DISTANCE = 25

URL = f'{BASE_URL}/?rcp={SIZE}&rcs=0&srt=4&prx={DISTANCE}&prv={PROVINCE}&loc={CITY}%2C%20ON&hprc=True&wcp=True&inMarket=advancedSearch'

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id='SearchListings')

cars_cards = results.find_all("div", class_="result-item")

listings = []


handler = AutotraderHandler()

for item in cars_cards:
    section = item.select_one(
        '.dealer-split-wrapper'
    )

    left_section = section.select_one(
        '.re-layout-wrapper'
    ).find(
        'a', class_='inner-link'
    ).select_one(
        '.re-layout-inner'
    ).select_one(
        '.detail-center-area'
    )

    region = left_section.select_one(
        '.top-detail-area'
    )

    listing_obj = {
        "name": handler.name(section),
        "price": handler.price(section),
        "region": handler.region(section),
        "kms": handler.kms(region),
        "image": handler.image(section)
    }
    listings.append(listing_obj)

with open("listings.json", "w") as json_file:
    json.dump(listings, json_file, indent=4)

HTMLHandler().generate()