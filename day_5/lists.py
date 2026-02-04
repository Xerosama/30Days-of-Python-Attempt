# Day 5 Exercise Level 1

# Question 1 to 10
empty_list =[]
list_5 = [1,2,3,4,5]
print(len(list_5))
print(list_5[0::2])
mixed_data_types = ['name', 25, 175, 'single', 'address']
it_companies =['Facebook', 'Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0::len(it_companies)//2])
it_companies[1] = 'OpenAI'
print(it_companies)

# Question 11 to 17
it_companies.append('TCS')
it_companies.insert(len(it_companies)//2, 'Zoom')
print(it_companies)
it_companies[2] =it_companies[2].upper()
print(it_companies)
print('#; '.join(it_companies))
print('Google' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)

# Question 18 to 25

print(it_companies[3:])
print(it_companies[0:len(it_companies)-3])
if  len(it_companies)%2 == 0:
    print(it_companies[0:len(it_companies)/2]+it_companies[2+len(it_companies)/2:])
else:
    print(it_companies[0:len(it_companies)//2]+it_companies[1+len(it_companies)//2:])     
it_companies.pop(0)
print(it_companies)
it_companies.pop(len(it_companies)//2)
it_companies.pop(-1)
it_companies.clear()
del it_companies

# Question 26 to 27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
full_stack[4:4] =['Python', 'SQL']

# Day 5 Exercise level 2
# Question 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
ages.insert(0,min_age)
ages.append(max_age)
median_age = (ages[len(ages)//2] +ages[len(ages)//2 + len(ages)%2])/2
average_age = sum(ages)/len(ages)
print(average_age)
age_range = max_age - min_age
print(range)
print(abs(min_age- average_age)>(max_age - average_age))
print(abs(min_age- average_age)== (max_age - average_age))

#Question 2

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
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
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
  'Montenegro',
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
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
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
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
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
  'Zimbabwe'
]
t_count =len(countries)
print(t_count)
print(countries[(t_count-1)//2 : (t_count//2) +1])

# Question 3 
print(f'{len(countries[0:t_count//2])}, {len(countries[t_count//2:])}')
list1 = countries[0:1+(t_count//2)]
list2 =countries[1+(t_count//2):]
print(len(list1))
print(len(list2))

# Question 4
list_c = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country1, country2, country3, *scandic_countries = list_c
print(f'{country1}, {country2}, {country3}, {scandic_countries}')