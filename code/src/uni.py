import requests
from config import Config
from src.reposetories import get_cache, is_cache_alive, to_cache


WEATHER_API_URL = Config.WEATHER_API_URL


def get_response():
    if is_cache_alive() == True:
        data = get_cache()
        return data
    else:
        response = requests.get(WEATHER_API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        to_cache(data)
    
    return data

