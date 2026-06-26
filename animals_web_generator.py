import data_fetcher as df

RED = "\033[0;31m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"

animals_data = {}
animal = ""


def load_template_file():
    """Loads a template file"""
    with open("animals_template.html") as f:
        return f.read()


def get_skin_types(animals_data):
    """Gets all available skin types for animals.

    Returns:
        skin_type (set): List of skin types available for animals.
    """
    skin_types = set()
    for animal_data in animals_data:
        skin_types.add(animal_data.get('characteristics', {}).get('skin_type'))

    return skin_types


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


def create_content(data, skin_type):
    """
    Creates HTML content for animals

    Args:
        data (list): Animals data used to create the content
        skin_type (str): Skin type of the animal object

    Returns (str): content for HTML template
    """
    content = ""
    if len(data) == 0:
        content = f"<h2 style=\"text-align: center ;\">The animal \"{animal}\" doesn't exist.</h2>"
    else:
        for animal_data in data:
            content += serialize_animal(animal_data, skin_type)

    return content


def create_template(content):
    """Creates a template file
    Args:
        content (str): Template content
    """
    with open("animals.html", "w") as f:
        f.write(load_template_file().replace("__REPLACE_ANIMALS_INFO__", content))


def main():
    """Main function"""

    skin_type = ""
    global animal
    global animals_data
    # Fetch animals data
    while True:
        try:
            animal = input(f"{GREEN}Enter animal name: {RESET}")
            if animal == "":
                raise ValueError(f"{RED}Input is empty{RESET}")
            animals_data = df.fetch_data(animal)
            break
        except ValueError as e:
            print(e)

    # Retrieves skin types
    while True:
        try:
            if len(animals_data) == 0:
                break
            else:
                print(f"{GREEN}Enter skin type from list or press \"Enter\":{RESET}")
                for skin_type in get_skin_types(animals_data):
                    print(skin_type)
                print("")
                skin_type = input()
                if not (skin_type == "" or skin_type in get_skin_types(animals_data)):
                    raise ValueError("")
            break
        except ValueError as e:
            print(e)

    create_template(create_content(animals_data, skin_type))
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
