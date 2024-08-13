import time
import requests
from cacheout import Cache
import logging
# Get the logger already setup
logger = logging.getLogger(__name__)

class Swapidev:
    
    #Class variable to store cache maxsize 256 and TTL 5 min
    cache = Cache(maxsize=256, ttl=300, timer=time.time, default=None)
    

    def __init__(self) -> None:
        pass

    def get_starships(self, **filters):
        """
        Fetches starships from the API and then it filters based on filters received

        Args:
        - filters: argument for filtering starships

        Return a list with starships that match the filter
        """
        logger.info("Fetching starships with filters: %s", filters)
        response = requests.get("https://swapi.dev/api/starships/")
        #we get json from API
        starships = response.json().get("results", [])

        # this lambda function will receive a starship from filter function
        # and then verify if it has equal parameters-values as the search
        # all() return true if  our object gets true for all filters
        
        lambda_function = lambda x: all(x.get(key) == value for key,value in filters.items())
        
        # apply the lambda function to each element
        filtered = filter(lambda_function,starships)

        return list(filtered)



    def get_manufacturers(self):
        """
        Fetches manufacturers from the API
        As there isn't special endpoint avaiiable, this function get all manufacturers from the API
        and as it could be potentially an expensive call
        cache was implemented
        """
        
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
    
