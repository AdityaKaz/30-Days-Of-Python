# Day 5: 30 Days of python programming

# lst = list()
# lst = []

# fruits = ["mango", "banana", "apple", "grape", "pineapple"]
# fruits = list(["mango", "banana", "apple", "grape", "pineapple"])
# fruits_count = len(fruits)
# print(fruits_count)
# start = 0
# middle = (fruits_count)//2
# end = -1
# print(fruits[start], fruits[middle], fruits[end] )

mixed_data_types = ["aditya", 23, 183, "single", "mumbai"]

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']

# print(it_companies)

num_of_companies = len(it_companies)
# print(num_of_companies)

start = 0
middle = num_of_companies // 2
end = -1
# print(it_companies[start], it_companies[middle], it_companies[end])

it_companies[0] = "Tesla"
# print(it_companies)

it_companies.append("Facebook")
# print(it_companies)

it_companies.insert( middle, "Nvidia")
# print(it_companies)

it_companies[0] = it_companies[0].upper()
# print(it_companies)

# print(" ".join(it_companies))

company = "ibm"
# print(company in it_companies)

it_companies.sort()
# print(it_companies)

it_companies.sort(reverse=True)
# print(it_companies)

# print(it_companies[0:3])

# print(it_companies[-1:-4:-1])

# it_companies.pop()
# print(it_companies)
# length = len(it_companies)
# half = length // 2
# if length % 2 == 0:
#   print(it_companies[ half - 1 : half + 1])
# else:
#   print(it_companies[ half : half + 1])

# print(it_companies.pop(0))
# del it_companies[0]
# print(it_companies)

# it_companies.pop()
# print(it_companies)
# length = len(it_companies)
# half = length // 2
# if length % 2 == 0:
#   it_companies.pop(half - 1)
#   it_companies.pop(half - 1)
#   print(it_companies)
# else:
#   it_companies.pop(half)
#   print(it_companies)

# it_companies.pop()
# del it_companies[-1]

# print(it_companies)
# del it_companies[:]
# print(it_companies)

# del it_companies
# print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
# full_stack = front_end + back_end

# full_stack = front_end.copy()
# full_stack.extend(back_end)

# full_stack = [*front_end, *back_end]

# front_len = len(front_end)
# full_stack.insert(front_len, "Python")
# full_stack.insert(front_len + 1, "SQL")
# print(full_stack)

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# ages.sort()

# min_age = ages[0]

# max_age = ages[-1]

# ages.append(min_age)
# ages.append(max_age)
# ages.sort()

# num_of_students = len(ages)
# middle = num_of_students // 2
# if num_of_students % 2 == 0:
#   print(((ages[middle - 1]) + (ages[middle]))/2)
# else:
#   print(ages[middle])

# total = 0
# for age in ages:
#   total += age
# average_age = total / num_of_students
# print(average_age)

# print(max_age - min_age)

# if abs(min_age - average_age) > abs(max_age - average_age):
#     print("Minimum is farther from the average.")
# elif abs(min_age - average_age) < abs(max_age - average_age):
#     print("Maximum is farther from the average.")
# else:
#     print("Both are equally far from the average.")

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
# num_of_countries = len(countries)
# middle = num_of_countries // 2

# if num_of_countries % 2 == 0:
#   print(countries[middle - 1], countries[middle])
# else:
#   print(countries[middle])

# if num_of_countries % 2 == 0:
#   first_half = countries[:middle]
#   second_half = countries[middle:]
#   print(first_half, second_half)
# else:
#   first_half = countries[:middle + 1]
#   second_half = countries[middle + 1:]
#   print(first_half, second_half)

countries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# first_country, second_country,third_country, *scandic = countries2
# print(first_country)
# print(second_country)
# print(third_country)
# print(scandic)
