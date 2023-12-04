import json

# Загрузите список стран из [[countries.json]]
with open('countries.json', 'r') as file:
    countries = json.load(file)

# С помощью map() создайте новый список, изменив сделав название каждой страны прописным в списке стран
countries_uppercase = list(map(lambda x: x.upper(), countries))
print(countries_uppercase)

# С помощью filter(), чтобы отфильтровать страны, содержащие 'land'
countries_with_land = list(filter(lambda x: 'land' in x, countries))
print(countries_with_land)

# С помощью filter(), чтобы отфильтровать страны, содержащие ровно шесть символов.
six_letter_countries = list(filter(lambda x: len(x) == 6, countries))
print(six_letter_countries)

# С помощью filter(), чтобы отфильтровать страны, содержащие шесть и более букв в списке стран.
six_or_more_letter_countries = list(filter(lambda x: len(x) >= 6, countries))
print(six_or_more_letter_countries)

# С помощью filter() для отсеивания стран, начинающихся с буквы 'E'.
starting_with_e = list(filter(lambda x: x.startswith('E'), countries))
print(starting_with_e)

# Объединение всех стран с помощью reduce()
from functools import reduce
combined_countries = reduce(lambda x, y: x + ', ' + y, countries) + ' are countries in Northern Europe.'
print(combined_countries)

# Решение предыдущих задач с помощью объединения методов высшего порядка
capitalized_land_countries = list(map(lambda x: x.capitalize(), filter(lambda x: 'land' in x, countries)))
six_letter_e_countries = list(filter(lambda x: len(x) == 6, filter(lambda x: 'e' in x, countries)))
combined_countries = reduce(lambda x, y: x + ', ' + y, filter(lambda x: len(x) >= 6, countries)) + ' are countries in world.'

# Использование каррирования и замыканий для объявления функции categorize_countries():

def categorize_countries(pattern):
    def inner(countries):
        return list(filter(lambda x: pattern in x, countries))
    return inner

land_countries = categorize_countries('land')(countries)
ia_countries = categorize_countries('ia')(countries)
island_countries = categorize_countries('Island')(countries)
stan_countries = categorize_countries('stan')(countries)

print(land_countries)
print(ia_countries)
print(island_countries)
print(stan_countries)

# Используя файл countries-data.json, выполните приведенные задания в функциональной парадигме:
with open('countries-data.json', 'r') as file:
    countries_data = json.load(file)

# Отсортировать страны по названию
sorted_countries_by_name = sorted(countries_data, key=lambda x: x['name'])
print(sorted_countries_by_name)

# Отсортировать страны по столице
sorted_countries_by_capital = sorted(countries_data, key=lambda x: x['capital'])
print(sorted_countries_by_capital)

# Отсортировать страны по численности населения
sorted_countries_by_population = sorted(countries_data, key=lambda x: x['population'])
print(sorted_countries_by_population)

# Выявить произвольное число (начать с 10) наиболее распространенных языков и где их используют.
from collections import Counter
languages = [language for country in countries_data for language in country['languages']]
most_common_languages = Counter(languages).most_common(10)
print(languages)

# Выявить произвольное число (начать с 10) наиболее населенных стран.
most_populated_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]
print(most_populated_countries)
