def format_city_function(city, country, population=''):
    """ Function to return city and country in same string """
    if population:
        formatted_name = f"{city}, {country} - population {population}"
    else:
        formatted_name = f"{city}, {country}"
    return formatted_name.title()

#print(format_city_function('hyderabad', 'india', ' 1 core'))