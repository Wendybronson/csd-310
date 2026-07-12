# ---------------------------------------------------------
# Wendy Bronson
# Module 7.2 Assignment: Test Cases
# Date: 07/08/2026
#
# Purpose:
# Create a function that accepts a city and country,
# with optional population and language parameters,
# and returns a formatted string.
#-----------------------------------------------------------

def city_country(city, country, population=None, language=None):
    """Return a formatted city and country string."""

    formatted_string = f"{city.title()}, {country.title()}"

    if population:
        formatted_string += f" - population {population}"

    if language:
        formatted_string += f", {language.title()}"

    return formatted_string


if __name__ == "__main__":
    print(city_country("santiago", "chile"))
    print(city_country("tokyo", "japan", 37400000))
    print(city_country("madrid", "spain", 3223000, "spanish"))