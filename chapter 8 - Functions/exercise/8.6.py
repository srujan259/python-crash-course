def city_country(city, country):
    """" City country function """
    fmt = f"{city}, {country}"
    return fmt.title()

city = city_country('delhi', "india")
print(city)
