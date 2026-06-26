import requests
import os
from dotenv import load_dotenv

load_dotenv() # load environment variables file

URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal):
    """Fetches animals data from Ninjas API.

    Args:
        animal (str): Animal to be fetched
    Returns (list): JSON data from Ninjas API
    """
    parameters = {"name": animal}
    headers_params = {"x-api-key": os.getenv("API_KEY")}
    response = requests.get(URL, params=parameters, headers=headers_params).json()

    return response
