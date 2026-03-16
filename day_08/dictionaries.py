# Day 8 Exercise

# Question 1 to 4
dog = {}
dog['name'] = 'Tommy'
dog['color'] = 'Black'
dog['breed'] = 'Rotwheeler'
dog['legs'] = 4
dog['age'] = 6

student = {}
student['first_name'] = 'John'
student['last_name'] = 'Doe'
student['gender'] = 'male'
student['age'] = 14
student['marital_status']= 'Single'
student['skills'] = ['Python', 'Accounting',' Excel']
student['country'] = 'Germany'
student['city'] = 'Frankfurt'
student['address'] = 'Kapersburgstr. 9, 61191 Frankfurt, DEU'

print(len(student))

# Question 5 to 11
print(student['skills'])
print(type(student['skills']))

student['skills'].append('SQL')
print(student['skills'])

print(student.keys())

print(student.values())

print(student.items())

student.pop('address')
print(student)

del student