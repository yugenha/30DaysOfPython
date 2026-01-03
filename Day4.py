import math
result = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(result)
company = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(company)
print(len(company))
company = company.upper()
print(company)
company = company.lower()
print(company)
company = company.capitalize()
print(company)
company = company.title()
print(company)
company = company.swapcase()
print(company)
company = company.swapcase()
company = company.strip('Coding ')
print(company.strip(' Coding'))
print(company.find('Coding'))
company = 'Coding' + ' ' + company
print(company)
company = company.replace('Coding', 'Python')
print(company)
print(company.split(' '))
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(',')
print(companies)
company = company.replace('Python', 'Coding')
print(company[0])
print(len(company)-1)
print(company[10])
bro = 'Python For Everyone'
bro_abr = bro.replace('or ', '').replace('veryone', '').replace('ython ', '')
print(bro_abr)
company_abr = company.replace('or ', '').replace('ll', '').replace('oding ', '')
print(company_abr)
print(company.index('C'))
print(company.index('F'))
print(company.rindex('l'))
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))
phrase_l = 'You cannot end a sentence with because because because is a conjunction'.split('because because because ')
phrase = ''.join(phrase_l)
print(phrase)
print(f'The sentence starts with "Coding", is {company.startswith('Coding')}')
print(f'The sentence ends with "coding", is {company.endswith('coding')}')
sent = '   Coding For All      '.strip(' ')
print(sent)
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
lst = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
lst_str = '\n'.join(lst)
print(lst_str)
line = 'I am enjoying this challenge.\nI just wonder what is next.'
print(line)
tabbed = 'Name\t\tAge\t\tCountry\t\tCity\nAsabeneh\t250\t\tFinland\t\tHelsinki'
print(tabbed)
radius = 10
pi = 3.14
print(f'radius = {radius}\narea = {pi} * radius ** 2\nThe area of a circle with radius {radius} is {round(pi * radius ** 2)} meters square.')
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6
print(f'{a} + {b} = {a+b}\n{a} - {b} = {a-b}\n{a} * {b} = {a*b}\n{a} / {b} = {a/b:.2f}\n{a} % {b} = {a%b}\n{a} // {b} = {a//b}\n{a} ** {b} = {a**b}')

