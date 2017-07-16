from matplotlib import pyplot as plt
from countries_codes import get_country_code
import json


def print_json_data():
    filename = 'population_data.json'
    with open(filename) as f:
        pop_data = json.load(f)

    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                print(code + " : " + str(population))
            else:
                print('Error - ' + country_name)


print_json_data()
