# Day 6 Exercises
# Exercise level 1

# Question 1 to 5
empty_tuple =()
sister=('name1','name2','name3','name4')
brother = ('bro1', 'bro2', 'bro3')

siblings = sister + brother
print(len(siblings))
siblings = list(siblings)
siblings.append('father')
siblings.append('mother')
family_members = siblings
print(family_members)

#Exercise level 2

# Questions 1 to 6
siblings = family_members[0:-2]
parents = family_members[-2:]
print(siblings)
print(parents)

fruits =('Apples','Orange','Pineapple','Guava')
vegetables =('Cauliflower','Potato','Raddish')
dairy = ('Milk','Curd', 'Buttermilk')
food_stuff_tp = fruits + vegetables + dairy
food_stuff_lt = list(food_stuff_tp)
print( food_stuff_lt[len(food_stuff_lt)//2 :(len(food_stuff_lt)//2)+1+ len(food_stuff_lt)%2])
del food_stuff_lt[len(food_stuff_lt)//2 :(len(food_stuff_lt)//2)+1+ len(food_stuff_lt)%2]
print(food_stuff_lt)

del food_stuff_lt[0:3]
del food_stuff_lt[-3:]
print(food_stuff_lt)
del food_stuff_tp

# Question 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)