import json
import requests
from bs4 import BeautifulSoup
from utils import format_string

URL = 'https://www.autotrader.ca/cars/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id='SearchListings')

cars_cards = results.find_all("div", class_="result-item")

listings = []

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

    name = left_section.find('span', class_='title-with-trim')

    right_section = section.select_one(
        '.detail-price-area'
    ).select_one(
        '.price'
    ).find('span', class_='price-amount').text

    region = left_section.select_one(
        '.top-detail-area'
    )
    price = right_section

    kms = region.select_one(
        '.kms'
    )
    kms_value = None

    if kms:
        kms_value = kms.select_one(
            '.odometer-proximity'
        ).text

    listing_obj = {
        "name": format_string(name.text),
        "price": right_section,
        "kms": kms_value
    }
    listings.append(listing_obj)

with open("listings.json", "w") as json_file:
    json.dump(listings, json_file, indent=4)
