# Dla chętnych Rozszerzyć skrypt z punktu 7 o przyjmowanie parametru city ,
# który może być przekazywany w wierszu poleceń podczas wykonywania (np.
# python main.py --city=Berlin ). Należy wykorzystać moduł argparse do
# wczytywania przekazywanych parametrów, a w razie przekazania wartości
# ograniczyć pobierane browary do miasta, które zostało wskazane.

class Brawery:
    def __init__(self, id: str, name: str, brewery_type: str, address_1: str, address_2: str, address_3: str, city: str,
                 state_province: str, postal_code: str, country: str, longitude: float, latitude: float, phone: int,
                 website_url: str, state: str, street: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self):
        return f"Brewery ID: {self.id}\nName: {self.name}\nType: {self.brewery_type}\nAddress: {self.address_1}, {self.city}, {self.state_province} {self.postal_code}, {self.country}\nPhone: {self.phone}\nWebsite: {self.website_url}\n"


import requests


def get_breweries(city: str = None):
    url = f"https://api.openbrewerydb.org/v1/breweries?page=1&per_page=20"
    if city:
        url = f"https://api.openbrewerydb.org/v1/breweries?page=1&per_page=20&by_city={city}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return [Brawery(id=el["id"],
                            name=el["name"],
                            brewery_type=el["brewery_type"],
                            address_1=el["address_1"],
                            address_2=el["address_2"],
                            address_3=el["address_3"],
                            city=el["city"],
                            state_province=el["state_province"],
                            postal_code=el["postal_code"],
                            country=el["country"],
                            longitude=el["longitude"],
                            latitude=el["latitude"],
                            phone=el["phone"],
                            website_url=el["website_url"],
                            state=el["state"],
                            street=el["street"]) for el in response.json()]
        else:
            print("Błąd: Nieudane żądanie:", response.status_code)
            return None
    except Exception as e:
        print("Wystąpił błąd podczas żądania API:", e)
        return None


import argparse
import sys

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Użycie: python script.py arg1 arg2 arg3 ...")
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('--city', type=str)

        args = parser.parse_args()
        [print(brewery) for brewery in get_breweries(args.city)]
