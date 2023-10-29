import json


class HTMLHandler:

    def __init__(self) -> None:
        self.listings = []

        self.get_listings()

    def get_listings(self):
        with open('listings.json', 'r') as file:
            self.listings = json.load(file)

    def generate(self):
        listings_section = ''

        for listing in self.listings:
            image = f'<img src={listing["image"]} alt={listing["name"][:10]}/>' if listing["image"] else ''
            listings_section += f'''
                <tr>
                    <td>{image}</td>
                    <td>{listing["name"]}</td>
                    <td>{listing["price"]}</td>
                </tr>
            '''
        html = f'''
            <style>
            table, th, td {{
                border: 1px solid black;
                border-collapse: collapse;
            }}
            img {{
                width: 300px;
                height: 300px;
                min-width: 300px;
                min-height: 300px;
            }}
            </style>
            <body>
                <h1>
                    Autotrader
                    <br/>
                    <table>
                        <tbody>
                            {listings_section}
                        </tbody>
                    </table>
                </h1>
            </body>
        '''
        with open("listings.html", "w") as file:
            file.write(html)
