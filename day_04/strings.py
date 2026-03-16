# Exercise Day 4

#Question 1 to 8
list1 = ['Thirty', 'Days', 'Of', 'Python']
print(" ".join(list1))
list2 =['Coding', 'For' , 'All']
print(" ".join(list2))
company ="Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())


# Question 9 to 17
print(company[6:])
print(company.find('Coding'))
print(company.replace('Coding', "Python"))

print("Python for Everyone".replace('Everyone', "All"))
print(company.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
print(company[0])
print(company[-1])
print(company[10])

#Question 18 to 19
s_split = 'Python For Everyone'.split()
i=0

while i<=(len(s_split)-1):
    print(s_split[i][0],end=".")
    i+=1
    
print("")    


c_split =company.split()
i=0
while i<=(len(c_split)-1):
    print(c_split[i][0],end=".")
    i+=1
print("")

#Question 20 to 30
print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

sentence ='You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.rfind('because'))
print(sentence.rindex('because'))
print(sentence[0:sentence.index('because')]+sentence[sentence.rindex('because')+len('because'):])

print(company.startswith('Coding'))
print(company.endswith('coding'))
print('   Coding For All      '.strip(' ') )

# Question 31: Correct answer is thirty_days_of_python
#Question 32 to 36
list3 =['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list3))
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity \nAsabeneh\t250\tFinland\tHelsinki')

print('radius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is 314 meters square.')

num1 =8
num2 =6
print(f'{num1} + {num2} ={num1+num2} ')
print(f'{num1} - {num2} ={num1-num2} ')
print(f'{num1} * {num2} ={num1*num2} ')
print(f'{num1} / {num2} ={num1/num2:.2f} ')
print(f'{num1} % {num2} ={num1%num2} ')
print(f'{num1} // {num2} ={num1//num2} ')
print(f'{num1} ** {num2} ={num1**num2} ')
