# TODO Дан словарь, ключ - Название страны, значение - список городов, на вход
#  поступает город, необходимо сказать из какой он страны


def find_country(countries: dict[str, list[str]], city: str) -> str:
    for country, cities in countries.items():
        if city not in cities:
            ValueError("this city is not on the list")
        else:
            return country


list_countries = {'Belarus': ['Minsk', 'Gomel', 'Brest'], 'Russian': ['Moscow', 'Lytsk'],
                    'Romania': ['Bucharest', 'Brasow']}

print(find_country(list_countries, 'Bucharest'))
