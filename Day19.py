import re
import json

with open('./Data/obama_speech.txt', 'r', encoding='utf-8') as f:
    obama_speech = f.read()
with open('./Data/michelle_obama_speech.txt', 'r', encoding='utf-8') as f:
    michelle_obama_speech = f.read()
with open('./Data/donald_speech.txt', 'r', encoding='utf-8') as f:
    donald_speech = f.read()
with open('./Data/melina_trump_speech.txt', 'r', encoding='utf-8') as f:
    melina_trump_speech = f.read()

def print_count_words_lines(speech):
    words = len(re.findall(r'\b\w+\b', speech))
    print(f'The speech has {words} words.')
    lines = len(speech.splitlines())
    print(f'The speech has {lines} lines.')

print('Obama Speech:')
print_count_words_lines(obama_speech)
print('\nMichelle Obama Speech:')
print_count_words_lines(michelle_obama_speech)
print('\nDonald Speech:')
print_count_words_lines(donald_speech)
print('\nMelina Trump Speech:')
print_count_words_lines(melina_trump_speech)


def most_spoken_languages(filename='./Data/countries_data.json', n=10):
    from collections import Counter

    with open(filename, 'r', encoding='utf-8') as f:
        countries_data = json.load(f)
    languages = []
    for country in countries_data:
        languages.extend(country.get('languages', ()))
    most_common_languages = Counter(languages).most_common(n)
    return [(count, language) for language, count in most_common_languages]

def most_populated_countries(filename='./Data/countries_data.json', n=10):
    with open(filename, 'r', encoding='utf-8') as f:
        countries_data = json.load(f)
    countries_population = [(country['name'], country['population']) for country in countries_data]
    countries_population.sort(key=lambda x: x[1], reverse=True)
    return countries_population[:n]


print(most_spoken_languages(n=3))
print(most_populated_countries(n=3))

# with open('./Data/email_exchanges_big.txt', 'r', encoding='utf-8') as f:
#     email_exchanges = f.readlines()
# emails = [line.split()[1] for line in email_exchanges if line.startswith('From ')]
# print(emails)

def find_most_common_words(filename, n=10):
    from collections import Counter

    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    words = re.findall(r'\b\w+\b', text)
    most_common_words = Counter(words).most_common(n)
    return [(count, word) for word, count in most_common_words]

print(find_most_common_words('./Data/obama_speech.txt', n=10))
print(find_most_common_words('./Data/michelle_obama_speech.txt', n=10))
print(find_most_common_words('./Data/donald_speech.txt', n=10))
print(find_most_common_words('./Data/melina_trump_speech.txt', n=10))

import Day19_app as app
similarity1 = app.text_similarity(obama_speech, michelle_obama_speech)
similarity2 = app.text_similarity(donald_speech, melina_trump_speech)

print(f'Similarity between Obama and Michelle Obama speeches: {similarity1:.4f}')
print(f'Similarity between Donald and Melina Trump speeches: {similarity2:.4f}')

print(find_most_common_words('./Data/romeo_and_juliet.txt', n=10))

def count_lines(filename, keyword):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    count = sum(1 for line in lines if keyword.lower() in line.lower())
    return count
print(count_lines('./Data/hacker_news.csv', 'Python'))