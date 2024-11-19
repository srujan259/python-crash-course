from city_functions import format_city_function

def test_city_country():
    """ Test format city country function"""
    result = format_city_function('hyderabad', 'india')
    assert result == "Hyderabad, India"

def test_city_country_population():
    """ Test city country and population"""
    result = format_city_function('hyderabad', 'india', '10000000')
    assert result == "Hyderabad, India - Population 10000000"