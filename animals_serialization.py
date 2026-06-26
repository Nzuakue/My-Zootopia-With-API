import json
import requests

URL = "https://api.api-ninjas.com/v1/animals"
x_api_key = "kArkhiDb1WMk1lltdFoSehl8MgpS8fYBzWYg28Gz"

def fetch_data(animal):
    """Fetches animals data from Ninjas API.

    Args:
        animal (str): Animal to be fetched
    Returns (list): JSON data from Ninjas API
    """
    parameters = {"name": animal}
    headers_params = {"x-api-key": x_api_key}
    res = requests.get(URL, params=parameters, headers=headers_params).json()
    return res


def get_serialized_animals(skin_type):
    """Serializes animals from a json-file into HTML.

    Args:
        skin_type (str): Skin type of the animal object

    Returns:
        Str: Serialized animals
    """
    animals_data = fetch_data("fox")
    serialized_animals = ""

    for animal_data in animals_data:
        serialized_animals += serialize_animal(animal_data, skin_type)

    return serialized_animals


def serialize_animal(animal_obj, skin_type):
    """Serialize an animal object into HTML.

    Args:
        animal_obj (dict): Animal object to be serialized
        skin_type (str): Skin type of the animal object

    Returns:
        Str: Serialized animal object
    """
    output = ""
    if animal_obj.get('characteristics', {}).get('skin_type') == skin_type:
        output += "<li class=\"cards__item\">\n"
        output += f"<div class=\"card__title\">{animal_obj.get('name')}</div> \n"
        output += "<div class=\"card__text\">\n"
        output += "<ul>\n"
        output += f"<li><strong>Diet:</strong> {animal_obj.get('characteristics', {}).get('diet')}</li>\n"
        output += f"<li><strong>Skin type:</strong> {animal_obj.get('characteristics', {}).get('skin_type')}</li>\n"
        output += f"<li><strong>Location:</strong> {animal_obj.get('locations')[0]}</li>\n"
        if 'type' in animal_obj.get('characteristics', {}).keys():
            output += f"<li><strong>Type:</strong> {animal_obj.get('characteristics', {}).get('type')}</li>\n"
        output += f"<li><strong>Scientific name:</strong> {animal_obj.get('taxonomy', {}).get('scientific_name')}</li>\n"
        output += "</ul>\n"
        output += "</div>\n"
        output += "</li>\n\n"
    elif skin_type == "":
        output += "<li class=\"cards__item\">\n"
        output += f"<div class=\"card__title\">{animal_obj.get('name')}</div> \n"
        output += "<div class=\"card__text\">\n"
        output += "<ul>\n"
        output += f"<li><strong>Diet:</strong> {animal_obj.get('characteristics', {}).get('diet')}</li>\n"
        output += f"<li><strong>Skin type:</strong> {animal_obj.get('characteristics', {}).get('skin_type')}</li>\n"
        output += f"<li><strong>Location:</strong> {animal_obj.get('locations')[0]}</li>\n"
        if 'type' in animal_obj.get('characteristics', {}).keys():
            output += f"<li><strong>Type:</strong> {animal_obj.get('characteristics', {}).get('type')}</li>\n"
        output += f"<li><strong>Scientific name:</strong> {animal_obj.get('taxonomy', {}).get('scientific_name')}</li>\n"
        output += "</ul>\n"
        output += "</div>\n"
        output += "</li>\n\n"

    return output

