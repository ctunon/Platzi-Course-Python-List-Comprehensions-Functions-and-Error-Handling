
def get_population(country_dictionary):
    population_dict = {
    '2022': int(country_dictionary['2022 Population']),
    '2020': int(country_dictionary['2020 Population']),
    '2015': int(country_dictionary['2015 Population']),
    '2010': int(country_dictionary['2010 Population']),
    '2000': int(country_dictionary['2000 Population']),
    '1990': int(country_dictionary['1990 Population']),
    '1980': int(country_dictionary['1980 Population']),
    '1970': int(country_dictionary['1970 Population'])
  }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values


def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result