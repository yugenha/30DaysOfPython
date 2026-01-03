# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# not_positive_numbers = [i for i in numbers if i <= 0]
# print(not_positive_numbers) # Output: [-4, -3, -2, -1, 0]
# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# flattened_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
# print(flattened_list) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# result = [(n, *(n ** p for p in range(6))) for n in range(11)]
# print(result)
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# flat_countries = [[country.upper(), country[:3].upper(), capital.upper()] for [(country, capital)] in countries]
# print(flat_countries)
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output = [{'country': country.upper(), 'city': capital.upper()} for [(country, capital)] in countries]
# print(output)
# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# full_names = [f'{first_name} {last_name}' for [(first_name, last_name)] in names]
# print(full_names)
slope = lambda x1, y1, x2, y2: None if x1 == x2 else (y2 - y1) / (x2 - x1)
print(slope(2, 2, 2, 2))