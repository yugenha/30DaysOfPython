lst = []
print(lst)
my_lst = [1, 2, 3, 4, 5]
print(my_lst)
print(len(my_lst))
print(my_lst[0])
print(my_lst[2])
print(my_lst[-1])
mixed_data_types = ['Yura', 18, 178.1, False, 'Lviv']
print(mixed_data_types)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print('Number of companies: ', len(it_companies))
print(it_companies[0])
print(it_companies[round((len(it_companies)-1)/2)])
print(it_companies[-1])
it_companies.insert(0, 'Google')
print(it_companies)
it_companies.append('Uber')
print(it_companies)
it_companies.insert(round((len(it_companies)-1)/2), 'PornHub')
print(it_companies)
it_companies[3] = it_companies[3].upper()
print(it_companies)
it_companies.append('#;  ')
print(it_companies)
print(it_companies.count('Google'))
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
del it_companies[0:2]
print(it_companies)
del it_companies[-3:]
print(it_companies)
del it_companies[round((len(it_companies)-1)/2):len(it_companies) -2]
print(it_companies)
it_companies.pop(0)
print(it_companies)
it_companies.pop(round((len(it_companies)-1)/2))
print(it_companies)
it_companies.pop((len(it_companies)-1))
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
programming = front_end + back_end
print(programming)
programming.insert(programming.index('Redux')+1, 'Python')
programming.insert(programming.index('Redux')+2, 'SQL')
print(programming)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(max(ages))
print(min(ages))
ages.append(max(ages))
ages.append(min(ages))
ages.sort()
print(ages)
print(int((ages[round((len(ages)-1)/2)] + ages[round((len(ages)-1)/2)+1])/2))
avg = sum(ages)/len(ages)
print('AVG:', avg)
print('RNG:', max(ages)-min(ages) )
print('Difference:', abs(min(ages)-avg) - abs(max(ages) - avg))
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print(countries[round((len(countries)-1)/2)])
first_half = countries.copy()
print(len(countries))
del first_half[round((len(first_half)-1)/2)+1:]
print(first_half)
print(len(first_half))
second_half = countries.copy()
del second_half[:round((len(second_half)-1)/2)+1]
print(second_half)
print(len(second_half))
CH, RU, USA, FN, *scand = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(CH, RU, USA, FN, *scand)
print(type(scand))
print(scand)