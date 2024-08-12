import requests


class Swapidev:
    def __init__(self) -> None:
        pass

    def get_starships(self, manufacturer=None):
        response = requests.get("https://swapi.dev/api/starships/")
        starships = response.json().get("results", [])
        if manufacturer:
            starships = (s for s in starships if manufacturer == s["manufacturer"])
        return list(starships)

    def get_manufacturers(self):
        response = requests.get("https://swapi.dev/api/starships/")
        starships = response.json().get("results", [])
        manufacturers = set(s["manufacturer"] for s in starships)
        return list(manufacturers)

