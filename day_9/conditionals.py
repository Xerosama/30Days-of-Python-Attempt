# Day 9 Exercises

#Exercise Level 1
# Question 1
age = int(input('Enter your age: '))
if age >=18 :
    print('YOu are old enough to drive')
else:
    
    print(f'Wait for {18-age} more years to learn to drive')

#Question 2
my_age = 20 
if my_age == age:
    print('You are same age as me')
elif my_age > age:
    if (my_age- age) ==1 :
        print('You are 1 year younger than me')
    else:
        print(f'You are {my_age-age} years younger than me.')
else:
    if (age - my_age) ==1:
        print('You are 1 year older than me')
    else:
        print(f'You are {age - my_age} years older than me.')

# Question 3
num1 = float(input('Enter first number:'))
num2 = float(input('Enter Second Number:'))
if num1 > num2:
    print(f'{num1} is greater than {num2}')
elif num2 > num1 :
    print (f'{num2} is greater than {num1}')
else:
    print(f'Both Numbers are equal')


#Exercise Level 2
#Question 1
grades = [(90,100,'A'),(80,89,'B'),(70,79,'C'),(60,69,'D'),(0,59,'F')]
score = int(input('Enter your marks:'))
i=0
while i<= len(grades) -1 :
    if score >=grades[i][0] and score <=grades[i][1]:
        print(f'The grade of student is {grades[i][2]}')
        break
    i+=1

#Question 2
winter_months = ['December','January', 'February']
spring_months = ['March','April','May']
summer_months = ['June','July','August']
autumn_months = ['September','October','November']
month= input('Enter your month')

if month in winter_months:
    print('The season is Winter.')
elif month in spring_months:
    print('The season is Spring.')
elif month in summer_months:
    print('The season is Summer.')
elif month in autumn_months:
    print('The season is Autumn.')

# Question 3
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Enter a new fruit name')
if new_fruit not in fruits:
    fruits.append(new_fruit)
    print(fruits)
else:
    print('That fruit already exist in the list')

#Exercise Level 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
skill_num = len(person['skills'])
if 'skills' in person.keys() :
    print(person['skills'][skill_num//2 + skill_num%2 -1:skill_num//2 +1])
    if 'Python' in person['skills']:
        print('Asabeneh has Python skills.')
    else:
        print('Asabeneh does not have Python skills.')
else:
    print('No skill section in dictionary')

skill_set = set(person['skills'])

if skill_set == {'JavaScript','React'}:
    print('He is a front end developer')
elif  {'Node', 'Python', 'MongoDB'} <= skill_set :
    print('He is a backend developer.')
if {'React','Node','MongoDB'} <= skill_set:
    print('He is a fullstack developer.')
else:
    print('Unknown Title')

if person['is_married']== True and person['country']=='Finland' :
    print(
        f"{person['first_name']} {person['last_name']} lives in {person['country']}.",
        "He is married."
    )