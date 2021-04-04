def make_car(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info


cars = make_car('suburu', 'outback', color = 'blue', tow_package = True)
print(cars)