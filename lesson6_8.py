# TODO Дан словарь, ключ - Название страны, значение - список городов, на вход
#  поступает город, необходимо сказать из какой он страны


def find_country(countries, city):
    # result = [country for country, cities in countries.items() if city in cities]
    # return result
    for country, cities in countries.items():
        if city in cities:
            return country
        # else:
        #     raise ValueError('this city is not on the list')


list_countries = {'Belarus': ['Minsk', 'Gomel', 'Brest'], 'Russian': ['Moscow', 'Lytsk'],
                  'Romania': ['Bucharest', 'Brasow']}


print(find_country(list_countries, 'Brasow'))

