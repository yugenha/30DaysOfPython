dog = dict()
print(dog)
dog['Name'] = 'Pushok'
dog['Color'] = 'brown'
dog['Breed'] = 'Labrador'
dog['Legs'] = 4
dog['Age'] = 18
print(dog)
#Delete one of the items in the dictionary
#Delete one of the dictionaries
student = {'first_name':'Yura', 'last_name':'Kainskyi', 'gender':'male', 'age':'18', 'marital_status':False, 'skills':['C++','Python'], 'country':'Ukraine', 'city':'Lviv', 'address':'Shevchenkivskyi rayon'}
print(student)
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('SQL')
print(student)
keys = student.keys()
print(keys)
values = student.values()
print(values)
tpl = student.items()
print(tpl)
del student['gender']
print(student)
del dog
