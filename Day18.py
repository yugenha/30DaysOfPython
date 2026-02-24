import re
from collections import Counter
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = re.findall(r'\b[A-Za-z]+\b', paragraph)
counts = Counter(words)
result = sorted([(count, word) for word, count in counts.items()], reverse=True)
print(result)
# [('love', 6), ('can', 3), ('you', 3),
txt = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."  
numbers = re.findall(r'-?\d+', txt)
int_numbers = [int(num) for num in numbers]
distance = max(int_numbers) - min(int_numbers)
print(int_numbers)
print(distance)

def is_valid_variable(var):
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    print(re.match(pattern, var) is not None)

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True

def most_frequent_words(text):
    words = re.findall(r'\b[A-Za-z]+\b', text)
    counts = Counter(words)
    result = sorted([(count, word) for word, count in counts.items()], reverse=True)
    return result
def clean_text(text):
    cleaned = re.sub(r'[%$@&#;]', '', text)
    return cleaned
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
cleaned_text = clean_text(sentence)
print(cleaned_text)

print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]