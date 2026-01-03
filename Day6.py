tpl = ()
print(tpl)
brothers = ('Andrew', 'Mathew')
sisters = ('Julia' , 'Stacy')
siblings = brothers + sisters
print(siblings)
print(f'I have {len(siblings)} siblings')
parents = ('Victor', 'Mariana')
family = siblings + parents
print(family)
siblings = family[0:4]
parents = family[4:]
print(siblings)
print(parents)
fruits = ('apple', 'banana', 'orange')
vegetables = ('corn', 'cucumber', 'tomato')
animal_prod = ('pork', 'beef', 'egg')
food_stuff_tp = fruits + vegetables + animal_prod
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
food_stuff_lt.remove(food_stuff_tp[round((len(food_stuff_tp)-1)/2)])
print(food_stuff_lt)
del food_stuff_lt[0:3]
del food_stuff_lt[-3:]
print(food_stuff_lt)
del food_stuff_lt
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)