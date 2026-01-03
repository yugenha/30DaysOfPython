it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print('The size of it_companies set is:',len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update({'Uber', 'Netflix'})
print(it_companies)
it_companies.remove('Uber')
print(it_companies)
it_companies.discard('Netflix')
print(it_companies)
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
A.update(B)
print(A)
B.update(A)
print(B)
print(A.symmetric_difference(B))
del A
del B
age_set = set(age)
print(age_set == age)
print(age_set.issubset(age))
print(age_set.intersection(age))
sent = 'I am a teacher and I love to inspire and teach people.'
splitted = sent.split(' ')
splitted = set(splitted)
print('The amount of unique words is', len(splitted), 'in', splitted)
