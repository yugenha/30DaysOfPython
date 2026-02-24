import requests as req
import statistics as stats

romeo_and_juliet = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
response = req.get(romeo_and_juliet)
text = response.text

def find_most_common_words_in_text(text, n=10):
    from collections import Counter
    import re

    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    most_common_words = Counter(words).most_common(n)
    return [(count, word) for word, count in most_common_words]
most_common_words = find_most_common_words_in_text(text, n=30)
print(most_common_words)

cats_api = 'https://api.thecatapi.com/v1/breeds'
response = req.get(cats_api)
cats_data = response.json()
cat_weights = [cat['weight']['metric'].split(' - ') for cat in cats_data if 'weight' in cat]
cat_lifespans = [cat['life_span'].split(' - ') for cat in cats_data if 'life_span' in cat]

cat_weights = [ (float(w[0]), float(w[1])) for w in cat_weights ]
cat_lifespans = [ (float(l[0]), float(l[1])) for l in cat_lifespans ]
cat_weights = [ (w[0] + w[1]) / 2 for w in cat_weights ]
cat_lifespans = [ (l[0] + l[1]) / 2 for l in cat_lifespans ]

wmin, wmax, wmean, wmedian, wstandard_deviation = min(cat_weights), max(cat_weights), stats.mean(cat_weights), stats.median(cat_weights), stats.stdev(cat_weights)
lmin, lmax, lmean, lmedian, lstandard_deviation = min(cat_lifespans), max(cat_lifespans), stats.mean(cat_lifespans), stats.median(cat_lifespans), stats.stdev(cat_lifespans)

print(f'Cat Weights (kg): Min={wmin}, Max={wmax}, Mean={wmean}, Median={wmedian}, Standard Deviation={wstandard_deviation}')
print(f'Cat Lifespans (years): Min={lmin}, Max={lmax}, Mean={lmean}, Median={lmedian}, Standard Deviation={lstandard_deviation}')

def frequency_table_of_country_and_breed(cats_data):
    from collections import Counter

    country_counts = Counter()

    for cat in cats_data:
        country = cat.get('origin', 'Unknown')
        breed = cat.get('name', 'Unknown')
        country_counts[country] += 1
    return country_counts

country_freq = frequency_table_of_country_and_breed(cats_data)
print('Country Frequency:')
for country, count in country_freq.most_common(5):
    print(f'{country}: {count}')

countries_api = 'https://www.apicountries.com/countries'
response = req.get(countries_api)
response.raise_for_status()   # fail fast if request is bad

countries_data = response.json()

def the_biggest_countries(countries_data, n=10):
    # filter out countries without area to avoid KeyError / None issues
    valid = [c for c in countries_data if c.get('area')]

    sorted_countries = sorted(
        valid,
        key=lambda x: x['area'],
        reverse=True
    )
    return [(c['name'], c['area']) for c in sorted_countries[:n]]

print('The biggest countries by area:')
biggest_countries = the_biggest_countries(countries_data, n=10)

for country, area in biggest_countries:
    print(f'{country}: {area:,} sq km')
