# Day 7 Exercises

# Exercise Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('twitter')
it_companies.update(['Facebook', 'Google', 'Tencent', 'Huawei'])
print(it_companies)
it_companies.remove('Oracle')
print(it_companies)
# If object is not in the set, them remove will give error,
# but discard will not give error.

# Exercise Level 2
C = A.union(B)
print(C)
D = A.intersection(B)
print(A.issubset(B))
print(A.isdisjoint(B))
ba = B | A
print(ba ==C)
sym_diff = A.symmetric_difference(B)
print(sym_diff)
del A, B, it_companies

#Exercise Level 3
age_set = set(age)
print(age == age_set)
# the length of a set made from a list will always be less than or equal to length of the list.

''' 
string= ordered and mutable collection of characters
list = ordered and mutable collection of objects,  duplicate items possible.
tuple = ordered and immutable collection of objects, duplicate items possible.
set = unordered and mutable collection of objects, duplicate items not possible.
'''

string1 = 'I am a teacher and I love to inspire and teach people.'
list2 = string1.split()
string_set = set(list2)
print(f'the number of unique words in string is: {len(string_set)}')