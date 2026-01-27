# Day 3 Exercise

#question 1 to 5
age = 20
height = 168.5
complex_number = complex(2,3)

t_base =float(input('Enter base length of triangle:'))
t_height =float(input('Enter height of triangle:'))
t_area = 0.5*t_base*t_height
print('The area of Triangle is: ',t_area)

t_side1 = float(input("Enter length of side one of triangle:"))
t_side2 = float(input("Enter length of side two of triangle:"))
t_side3 = float(input("Enter length of side three of triangle:"))
t_peri = t_side1+t_side2+t_side3
print("The perimeter of triangle is:",t_peri)

#question 6 and 7
rect_len =float(input('Enter length of rectangle:'))
rect_width =float(input('Enter width of rectangle:'))
rect_area = rect_len*rect_width
rect_peri = 2*(rect_len+rect_width)
print(f'Area of rectangle:{rect_area} \nPerimeter of rectangle is:{rect_peri}')

c_radius = float(input('Enter circle radius'))
c_area = 3.1415*c_radius**2 
c_circum = 3.1415*2*c_radius
print(f"Area of cricle is:{c_area} \nCircumference of circle is:{c_circum}")

#question 9
point_one = [2,2]
point_two = [6,10]

slope = (point_two[1] - point_one[1])/(point_two[0]-point_one[0])
distance = ((point_two[1]-point_one[1])**2 +(point_two[0]-point_one[0])**2)**0.5
print('Slope is:',slope,'\nDistance is:',distance)
#question 12 to 16
print('Length of python is:',len('python'))
print('Length of dragon is:',len('dragon'))
print(len('dragon')!=len('python'))
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print(str(float(len('python'))))

#question 17 to 20
number= int(input('Enter Number'))
if number%2 == 0:
    print('Number is even')
else:
    print('Number is odd')

print(7//3 == int(2.7))
print(type('10')==type(10))
print(int('9.8')==10)

#question 21 and 22
hours = int(input('Enter Hours'))
rate =int(input('Enter rate per hour'))
print(f'Your weekly earning is {hours*rate} ')

years =int(input('Enter number of years you have lived:'))
remain_sec = (100-years)*365*24*60*60
print(f'You can live for {remain_sec} seconds more.')

#question 23
i =1
while i<=5:
    j=0
    print(i,end=" ")
    while j<=3:
        print(i**j, end=" ")
        j+=1
    print('\n')
    i+=1

# Some questions have not been attempted.