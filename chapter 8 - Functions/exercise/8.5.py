def describe_city(city_name, country='india'):
    print(f"{city_name.title()} is in {country}")

describe_city('delhi')
describe_city(city_name="melbourne", country='Australia')
describe_city('newyork', 'USA')