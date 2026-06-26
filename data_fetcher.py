import requests

URL = "https://api.api-ninjas.com/v1/animals"
X_API_KEY = "kArkhiDb1WMk1lltdFoSehl8MgpS8fYBzWYg28Gz"


def fetch_data(animal):
    """Fetches animals data from Ninjas API.

    Args:
        animal (str): Animal to be fetched
    Returns (list): JSON data from Ninjas API
    """
    parameters = {"name": animal}
    headers_params = {"x-api-key": X_API_KEY}
    response = requests.get(URL, params=parameters, headers=headers_params).json()

    return response
