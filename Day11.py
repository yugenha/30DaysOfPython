import math
from Data.countries_data import countries_data
Winter = ('december', 'january', 'february')
Spring = ('march', 'april', 'may')
Summer = ('june', 'july', 'august')
Autumn = ('september', 'october', 'november')

def add_two_numbers(a, b):
    return a+b
print(add_two_numbers(10, 11))

def area_of_circle(r):
    print(f'Area of a circle with radius {r} is: {math.pi * r ** 2}')
area_of_circle(5)

def add_all_nums(*nums):
    sum = 0
    for i in nums:
        if type(i) != int and type(i) != float:
            print('There are some invalid data in nums!')
            break
        sum += i
    return sum
print(add_all_nums(1.5, 14))

def convert_celsius_to_farenheit(c):
    return (c*9/5) + 32
print(convert_celsius_to_farenheit(15))

def check_season(month):
    if month.lower() in Summer:
        return 'Summer'
    elif month.lower() in Spring:
           return 'Spring'
    elif month.lower() in Winter:
           return 'Winter'
    elif month.lower() in Autumn:
           return 'Autumn'
print('It is ' + check_season('december'))

def calculate_slope(p1, p2):
     return (p2[1] - p1[1]) / (p2[0] - p1[0])
print(f"m = {calculate_slope([3, 2], [4, 6])}")

def solve_quadratic_eqn(a, b, c):
    D = (b)**2 - (4*a*c)
    if D == 0:
        x = -b / 2 * a
        print(f"The root is: {x}")
    elif D > 0:
        x_1 = (-b + math.sqrt(D)) / 2 * a
        x_2 = (-b - math.sqrt(D)) / 2 * a
        print(f"The roots are: {x_1}, {x_2}")
    
solve_quadratic_eqn(1, 4, 4)
         
def print_list(l):
    answer = ""
    for i in l:
        answer += i + ' '
    print(answer)
print_list( ["I", "am", "gay", "for", "real"] )

def reverse_list(l):
    h = len(l)
    for i in range(h):
        l.append(l[-(i+1) - i])
    for i in range(h):
        l.remove(l[i])
    return l
print(reverse_list(["A", "B", "C"]))

def capitalize_list_items(l):
    rl = []
    for i in l:
        rl.append(i.upper())
    return rl
ls = ["I", "am", "gay", "for", "real"]
print(capitalize_list_items(ls))

def add_item(l, item):
    l.append(item)
    return l
print(add_item(ls, "haha"))


def remove_item(l, item):
    l.remove(item)
    return l

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']; 
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

def sum_of_numbers(n):
    r = 0
    for i in range(n+1):
        r += i
    return r   
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

def sum_of_odds(n):
    r = 0
    for i in range(n+1):
        if i % 2 == 1:
            r += i
    return r   

print(sum_of_odds(5))  
print(sum_of_odds(100))

def sum_of_even(n):
    r = 0
    for i in range(n+1):
        if i % 2 == 0:
            r += i
    return r  
print(sum_of_even(5))  
print(sum_of_even(100))

def evens_and_odds(n):
    ceven = 0
    codd = 0
    for i in range(n+1):
        if i % 2 == 0:
            ceven += 1
        else:
            codd += 1
    r = [codd, ceven]
    return r

print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.

def factorial(n):
    r = 1
    for i in range(n):
        r *= i + 1
    return r   

print(factorial(10))

def is_empty(p):
    if p is not "":
        print(f"parameter is not empty it is - {p}!")
    else:
        print("parameter is empty")

is_empty("")

def calculate_mean(l):
    n = len(l)
    summ = 0
    for i in range(n):
        summ += l[i]
    mean = summ / n
    return mean
def calculate_square_mean(l):
    n = len(l)
    summ = 0
    for i in range(n):
        summ += l[i]**2
    mean = summ / n
    return mean
def calculate_median(l):
    n = len(l)
    if n % 2 == 1:
        i = round(n / 2) - 1
        median = l[i]
    elif n % 2 == 0:
        i = int(n/2) - 1
        median = (l[i] + l[i+1]) / 2
    return median
def calculate_mode(l):
    mode = max(set(l), key=l.count)
    return mode
def calculate_range(l):
    range = max(l) - min(l)
    return range
def calculate_variance(l):
    variance = calculate_square_mean(l) - calculate_mean(l)**2
    return variance
def calculate_std(l):
    n = len(l)
    summ = 0
    for i in range(n):
        summ += (l[i] - calculate_mean(l))**2
    deviation = math.sqrt(summ / n)
    return deviation
ls = [4, 52, 1, 4, 3, 2, 2, 2, 1, 14, 10, 11, 11, 12, 23, 1, 1, 1, 1, 1]
print(f"Mean = {calculate_mean(ls)}")
print(f"Median = {calculate_median(ls)}")
print(f"Mode = {calculate_mode(ls)}")
print(f"Range = {calculate_range(ls)}")
print(f"Variance = {calculate_variance(ls)}")
print(f"Deviation = {calculate_std(ls)}")


def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True
print(is_prime(25))
s = list(set(ls))
def is_all_unique(l):
    return len(l) == len(set(l))

print(is_all_unique(ls))
lss = [4, 52, 1, 4, 3, 2, 2, 2, 1, 14, 10, 11, 11, 12, 23, 1, 1, 1, 1, 1, True]
def is_data_same(l):
    for i in range(1, len(l)):
        if type(l[i]) != type(l[0]):
            return False
    return True
print(is_data_same(lss))

def is_variable_valid(v):
    return v.isidentifier()

        
print(is_variable_valid("1point_"))

def the_most_spoken_languages(countries):
    lang_count = {}
    for country in countries:
        for lang in country['languages']:
            if lang in lang_count:
                lang_count[lang] += 1
            else:
                lang_count[lang] = 1
    sorted_langs = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_langs[:10]

print(the_most_spoken_languages(countries_data))

def most_populated_countries(countries):
    pop_count = {}
    for country in countries:
        pop_count[country['name']] = country['population']
    sorted_pops = sorted(pop_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_pops[:10]
print(most_populated_countries(countries_data))
    