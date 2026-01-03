from countries import countries
from countries_data import countries_data

for number in range(11):
    print(number)
count = 0
while count != 11:
    print(count)
    count += 1

symbol = '#'
for i in range(7):
    print(symbol)
    symbol += '#'

print()
symbol = '#'
for i in range(8):
    print(symbol+' ', end="",)
    for j in range(7):
        print(symbol+' ', end="")
    print()

print()
for i in range(11):
    print(f"{i} x {i} = {i**2}")

programming_langs = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in programming_langs:
    print(language)

for i in range(0, 101, 2):
    print(i)
for i in range(101):
    if i % 2 == 1:
        print(i)

sum = 0
for i in range(101):
    sum += i
else:
    print(f'Sum of numbers 0 to 100 = {sum}')

sum_even = 0
sum_odd = 0
for i in range(0, 101, 2):
    sum_even += i
else:
    print(f'Sum of even numbers 0 to 100 = {sum_even}')

for i in range(101):
    if i % 2 == 1:
        sum_odd += i
else: 
    print(f'Sum of odd numbers 0 to 100 = {sum_odd}')

countries_land = []
for country in countries:
    if 'land' in country:
      countries_land.append(country)
print(countries_land)

fruits = ['banana', 'orange', 'mango', 'lemon']
temp = [] 
for i in range(len(fruits)):
    temp.append(fruits[-1])
    fruits.pop()
fruits = temp
print(fruits)

all_languages = set()
count = 0
for i in range(len(countries_data)):
    for key in countries_data[i]:
        if key == "languages":
            for language in countries_data[i]['languages']:
                count += 1
                all_languages.add(language)
print(f'The total amount of languages in data = {count}')

count_languages = dict.fromkeys(all_languages, 0)


for i in range(len(countries_data)):
    for key in countries_data[i]:
        if key == "languages":
            for language in countries_data[i]['languages']:
                if language in count_languages:
                    count_languages[language] += 1

values = count_languages.values()

top_10 = set()
svalues = sorted(values, reverse=True)
for i in range(len(values)):
    if len(svalues) > 10:
        svalues.pop()
print(svalues)

for lang in count_languages:
    if len(top_10) > 9: break
    else:
        if count_languages[lang] in svalues:
            top_10.add(lang)
print(top_10)

countries_pop = {
    c.get('name'): c.get('population')
    for c in countries_data
    if c.get('name') is not None and 'population' in c
}
print(countries_pop)
# Top 10 most populated countries
# Sort items by population (treat missing/None as 0) and take top 10
def pop_value(kv):
    val = kv[1]
    if isinstance(val, (int, float)) and val is not None:
        return val
    return 0

top_pop = sorted(countries_pop.items(), key=pop_value, reverse=True)
top_10_pop = top_pop[:10]
print(top_10_pop)