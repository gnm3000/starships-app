import time
import requests
from cacheout import Cache
import logging
# Obtener el logger ya configurado
logger = logging.getLogger(__name__)

class Swapidev:
    
    cache = Cache(maxsize=256, ttl=300, timer=time.time, default=None)
    # class variable

    def __init__(self) -> None:
        pass

    def get_starships(self, **filters):
        logger.info("Fetching starships with filters: %s", filters)
        response = requests.get("https://swapi.dev/api/starships/")
        #we get json from API
        starships = response.json().get("results", [])
        lambda_function = lambda x: all(x.get(key) == value for key,value in filters.items())
        # all() return true if  our object gets true for all filters
        filtered = filter(lambda_function,starships)

        return list(filtered)

    def get_manufacturers(self):
        
        #return form cache if exists
        if 'manufacturers' in self.cache:
            logger.info("Cache hit: Retuen manufacturers from cache")
            return self.cache.get('manufacturers')
        logger.info("Cache API hit: Fetching manufacturers from API")
        response = requests.get("https://swapi.dev/api/starships/")
        starships = response.json().get("results", [])
        manufacturers = {s["manufacturer"] for s in starships}
        manufacturers_list = list(manufacturers)

        self.cache.set('manufacturers', manufacturers_list)
        return manufacturers_list
    
