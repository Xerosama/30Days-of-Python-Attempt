# Day 12 Exercises

# Exercise Level 1

# Question 1
import string
import random
alphabets = string.ascii_letters
nums = string.digits
alphanum = alphabets + nums
id_length = 6
userid = ''
for i in range(id_length):
    rand_num = int(random.random() * (len(alphanum)-1))
    userid+=alphanum[rand_num]

print(userid)

# Question 2

def user_id_gen_by_user(id_length,num_of_id):
    id_list=[]
    for n in range(num_of_id):
        userid = ''
        for i in range(id_length):
            rand_num = int(random.random() * len(alphanum))
            userid+=alphanum[rand_num]
        id_list.append(userid)
    return id_list 

print(user_id_gen_by_user(10,4))

# Question 3
def rgb_color_gen():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return f'rgb({red},{green},{blue})'

print(rgb_color_gen())

# Exercise Level 2

def list_of_hexa_colors(num_of_hexcol):
    hexadecimal = '0123456789ABCDEF'
    hexcolor_list = []
    for n in range(num_of_hexcol):
        hexcolor = '#'
        for i in range(6):
            rand_num = int(random.random() * 15)
            hexcolor+=hexadecimal[rand_num]
        hexcolor_list.append(hexcolor)
    return hexcolor_list

print(list_of_hexa_colors(6))

# Question 2
def list_of_rgb_colors(num_of_color):
    color_list =[]
    
    for n in range(num_of_color):
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        color_list.append(color)
    return color_list
print(list_of_rgb_colors(4))

# Question 3
def generate_colors(type, num_of_color):
    if type == 'rgb':
        color_list= list_of_rgb_colors(num_of_color)
        return color_list
    if type == 'hexa':
        color_list = list_of_hexa_colors(num_of_color)
        return color_list
    else: 
        print('error, type is neither hexa nor rgb')


# Exercise Level 3
def shuffle_list(in_list):
    length = len(in_list)
    outlist = []
    index =[]
    for i in range(length):
        outlist.append(0)
    for i in range(length):
        while 1 ==1 :
            rand_num = random.randint(0,length-1)
            if rand_num not in index:
                outlist[rand_num] = in_list[i]
                index.append(rand_num)
                break
            else:
                continue
    return outlist

#Exercise Level 3
# Question 1
print(shuffle_list([0,1,1,2,3,4,'A']))

# Question 2
def random_num_generate():
    num_list = []
    for i in range(7):
        while 1==1 :
            rand_num = random.randint(0,9)
            if rand_num not in num_list:
                num_list.append(rand_num)
                break
            else:
                continue

    return num_list    


print(random_num_generate())