""" age = input('Enter your age: ')
age = int(age)
if age >= 18:
    print('You are old enough to drive!')
else:
    print(f'You need {18 - age} years old to drive!')
your_age = int(input('Enter your age: '))
my_age = 18
if your_age > my_age:
    if your_age - my_age == 1:
        print(f'You are older than me by just a year!')
    else:
        print(f'You are older than me by {your_age - my_age} years!')
elif your_age < my_age:
    if my_age - your_age == 1:
        print(f'You are younger than me by just a year!')
    else:
        print(f'You are younger than me by {my_age - your_age} years!')
else:
    print(f'You are the same age as me!')
a = int(input('Enter number for a: '))
b = int(input('Enter number for b: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is lesser than {b}')
elif a == b:
    print(f'{a} is equal to {b}')
else:
    print('Invalid input')
score = int(input('Enter your score: '))
if 80 <= score <= 100:
    print('Your grade is A')
elif 70 <= score < 80:
    print('Your grade is B')
elif 60 <= score < 70:
    print('Your grade is C')
elif 50 <= score < 60:
    print('Your grade is D')
elif 0 <= score < 50:
    print('Your grade is F')
else:
    print('Invalid score')
month = input('Enter month: ').strip().lower()
Autumn = {'september', 'october', 'november'}
Winter = {'december', 'january', 'february'}
Spring = {'march', 'april', 'may'}
Summer = {'june', 'july', 'august'}
if month in Autumn:
    print('It is Autumn')
elif month in Winter:
    print('It is Winter')
elif month in Spring:
    print('It is Spring')
elif month in Summer:
    print('It is Summer')
else:
    print('Invalid input') """

""" fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
fruit = input('Enter a fruit to add to the list: ').strip().lower()
if fruit in fruits:
    print('This fruit is already in the list!')
else:
    fruits.append(fruit)
print(fruits) """

person={
    'first_name': 'Yura',
    'last_name': 'Kainskyi',
    'age': 18,
    'country': 'Ukraine',
    'is_marred': False,
    'skills': ['Node', 'JavaScript', 'Html', 'MongoDB', 'C++', 'Python', 'MySQL'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    skills = person['skills']
    middle_index = len(person['skills']) // 2
    print(skills[middle_index])
if 'skills' in person:
    if 'Python' in skills:
        print('Person knows Python!')
if 'JavaScript' and 'React' in skills:
    print('He is a front end developer')
elif 'Node' and 'Python' and 'MongoDB' in skills:
    print('He is a backend developer')
elif 'React' and 'Node' and 'MongoDB' in skills:
    print('He is a fullstack developer')
else: print('unknown title')

if person['is_marred'] and person['country'] == 'Finland':
    print(f'{person["first_name"]} lives in {person["country"]}. He is married.')