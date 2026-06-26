import animals_serialization as aser

RED = "\033[0;31m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"


def load_template_file():
    """Loads a template file"""
    with open("animals_template.html") as f:
        return f.read()


def get_skin_types():
    """Gets all available skin types for animals.

    Returns:
        skin_type (set): List of skin types available for animals.
    """
    skin_types = set()
    animals_data = aser.fetch_data("fox")
    for animal_data in animals_data:
        skin_types.add(animal_data.get('characteristics', {}).get('skin_type'))

    return skin_types


def create_template(skin_type):
    """Creates a template file"""
    with open("animals.html", "w") as f:
        f.write(load_template_file().replace("__REPLACE_ANIMALS_INFO__", aser.get_serialized_animals(skin_type)))


def main():
    """Main function"""
    skin_types = get_skin_types()

    while True:
        try:  # Select a skin type to only display animal with this type or press enter to display all available animals
            print(f"{GREEN}Enter a skin type from the list or press \"Enter\": {RESET}")
            for skin_type in skin_types:
                print(skin_type)
            print("")
            user_choice = input()
            if not (user_choice == "" or user_choice in skin_types):
                raise ValueError(f"{RED}Enter available skin types or press \"Enter\"{RESET}")
            break
        except ValueError as e:
            print(e)

    create_template(user_choice)


if __name__ == "__main__":
    main()
