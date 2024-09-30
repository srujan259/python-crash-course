def car_details(manufacturer, model_name, **car_info):
    """ Function to define car details """
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

details = car_details('suzuki', 'baleno', color = 'blue', sku = 'alpha')
print(details)
