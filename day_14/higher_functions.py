# Day 14 Exercises
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#  Exercise Level 1 

'''Question 1 answer:map() function takes a function and iterable as a parameter,
It repeats the function for each iterable element provided to function.
Filter() function takes a condition and iterable as parameter, it only returns
those specific elements of iterable that return True for condition.
reduce() function takes a function and a iterable, but it only returns one single
value after applying function repeatedly till only one value remains.
'''
#Question 2 answer:
''' Higher order functions is a general term for functions which are those which 
1. take another function as parameter
2. Return a function as its result
3. Define one function inside another
In nested functions, the inside function can access things defined in the outer function
, this is called Closure.
Decorators is a design pattern to make functions that take another function as parameters, it only takes those functions 
defined just after decorator call. decoorators are called using @decorator_name 
'''

# Question 3 
# I do not understand what this question wants me to do

# Question 4 TO 6
for i in countries:
    print(i,end=', ')
print(' ')

for i in names:
    print(i,end=', ')
print(' ')

for i in numbers:
    print(i,end=', ')
print(' ')

# Exercise Level 2
#Question 1 to 3
upper_countries = list(map(lambda x: x.upper(), countries))
print(upper_countries)

squared_nums = list(map(lambda x:x**2,numbers))
print(squared_nums)

upper_names =list(map(lambda x: x.upper(),names))

# Question 4 to 7
def is_land_in_name(country):
    if 'land'in country:
        return True
    return False

land_countries = list(filter(is_land_in_name, countries))
print(land_countries)

def len_check6(country):
    if len(country) == 6:
        return True
    return False

letter6_countries= list(filter(len_check6,countries))
print(letter6_countries)

def len_check(country):
    if len(country) >= 6:
        return True
    return False

long_name_countries = list(filter(len_check,countries))
print(long_name_countries)

def startE(country):
    if country[0]=='E':
        return True
    return False

startE_countries = list(filter(startE, countries))
print(startE_countries)

# Question 8 is of Javascript not python
print("<class 'str'>"==str(type('am')))
# Question 9 
def get_string_lists(in_list):
    def str_check(s):
        if "<class 'str'>"==str(type(s)):
            return True
        return False
    out_list = list(filter(str_check,in_list))

# Question 10
from functools import reduce

strnum_list = list(map(str,numbers))
def strnum(*arg):
    total = 0
    for i in arg:
        total+=int(i)
    return total
total_sum = reduce(strnum,strnum_list)
print(total_sum)

# Question 11
def concat(c,d):
    return str(c) + ', '+str(d)
countries_str = str(reduce(concat,countries[0:-1])) + ' and '+str(countries[-1]) + ' are north European countries'
print(countries_str)

# Question 12
from countries import countries as all_countries
def categorize_countries(pattern):
    def pattern_check(country):
        if pattern in country:
            return True
        return False
    outlist = list(filter(pattern_check,all_countries))
    return outlist

print(categorize_countries('stan'))

# Question 13
from string import ascii_uppercase
def startcountry_dict(in_list):
    dict = {}
    for i in ascii_uppercase:
        dict[i] =0
    for country in in_list:
        dict[country[0]]+=1
    return dict

print(startcountry_dict(all_countries))
        
# Question 14 and 15
def get_first_ten_countries(countries):
    return countries[0:10]

def get_last_ten_countries(countries):
    return countries[-10:0]

# Exercise Level 3
# Question 1 
from countries import countries_data
#Sort by Name
countries_names = []
for country in countries_data:
    countries_names.append(country['name'])

sort_country_names = list(sorted(countries_names))

# Sort by Capital
countries_capital_dict={}
for country in countries_data:
    countries_capital_dict[country['name']]=country['capital']

countries_capital_list = list(sorted(list(countries_capital_dict.items()),key=lambda x:x[1]))
print(countries_capital_list)

# Sort by Population
countries_population_dict={}
for country in countries_data:
    countries_population_dict[country['name']]=country['population']

countries_population_list = list(sorted(list(countries_population_dict.items()),key=lambda x:x[1],reverse = True))
print(countries_population_list)


# I do not understand what the question means by sort 10 most spoken language by location
# Part 3 
print(countries_population_list[0:10])