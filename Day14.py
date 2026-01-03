from functools import reduce
from countries_data import countries_data
from countries import countries as countries_list
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)
for name in names:
    print(name)
for num in numbers:
    print(num)

countries_upper = map(lambda country: country.upper(), countries)
print(list(countries_upper))

squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))

names_upper = map(lambda name: name.upper(), names)
print(list(names_upper))

def is_land(country):
    if 'land' in country.lower():
        return True
    return False
land_countries = filter(is_land, countries)
print(list(land_countries))

def is_six_chars(country):
    if len(country) == 6:
        return True
    return False
six_char_countries = filter(is_six_chars, countries)
print(list(six_char_countries))

def is_more_than_six_chars(country):
    if len(country) > 6:
        return True
    return False
more_than_six_char_countries = filter(is_more_than_six_chars, countries)
print(list(more_than_six_char_countries))

def starts_with_e(country):
    if country.lower().startswith('e'):
        return True
    return False
e_countries = filter(starts_with_e, countries)
print(list(e_countries))

# arr.map(callback).filter(callback)
sum_cubed_even_numbers = reduce(lambda x, y: x + y, map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, numbers)))
print(sum_cubed_even_numbers)

def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))
mixed_list = [1, 'hello', 3.14, 'world', 42, 'python']
string_list = get_string_lists(mixed_list)
print(string_list)

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
sentence = (reduce(lambda x, y: x + ', ' + y, countries [:-1]) + ' and ' + countries[-1] + ' are north European countries')
print(sentence)

def categorize_countries(dic =countries_data, pattern=''):
    list_of_countries = [country['name'] for country in dic]
    result = filter(lambda country: pattern in country.lower(), list_of_countries)
    return result

print(list(categorize_countries(countries_data, 'island')))
import string
def count_countries_alphabetically(dic=countries_data):
    alphabet = list(string.ascii_lowercase)
    count_list = {}
    list_of_countries = [country['name'] for country in dic]
    for letter in alphabet:
        count = len(list(filter(lambda country: country.lower().startswith(letter), list_of_countries)))
        count_list[letter] = count
    return count_list
print(count_countries_alphabetically(countries_data))

def get_first_ten_countries(lst=countries_list):
    return lst[:10]
print(get_first_ten_countries())

def get_last_ten_countries(lst=countries_list):
    return lst[-10:]
print(get_last_ten_countries())

# Sort countries by name, by capital, by population
# Sort out the ten most spoken languages by location.
# Sort out the ten most populated countries.

def sort_countries_by_key(dic=countries_data, k='name'):
    return sorted(dic, key=lambda country: country[k])
print(sort_countries_by_key(countries_data, 'name'))
print(sort_countries_by_key(countries_data, 'capital'))
print(sort_countries_by_key(countries_data, 'population'))

def get_most_spoken_languages(dic=countries_data, n=10):
    language_count = {}
    for country in dic:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    return sorted(language_count.items(), key=lambda item: item[1], reverse=True)[:n]
print(get_most_spoken_languages(countries_data, 10))

def get_most_populated_countries(dic=countries_data, n=10):
    return sorted(dic, key=lambda country: country['population'], reverse=True)[:n]
print(get_most_populated_countries(countries_data, 10))