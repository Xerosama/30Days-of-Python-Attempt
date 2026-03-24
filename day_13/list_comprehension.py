# Day 13 Exercise

# Question 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

neg_num = [i for i in numbers if i<=0]
print(neg_num)

# Question 2
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in list_of_lists for num in row]
print(flat_list)

#Question 3
num_list = [(i,1,i,i**2,i**3,i**4,i**5) for i in range(11)]
print(num_list)

# Question 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_country = [[row[0][0].upper(), row[0][0][0:3].upper(),row[0][1].upper()] for row in countries]
print(flat_country)

# Question 5
country_dict = [{'country':row[0][0].upper(),'city':row[0][1].upper()} for row in countries]
print(country_dict)

# Question 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concat_names = [row[0][0]+' '+row[0][1] for row in names]
print(concat_names)

# Question 7
slope = lambda a,b,c:-a/b
yintercept = lambda a,b,c:-c/a
