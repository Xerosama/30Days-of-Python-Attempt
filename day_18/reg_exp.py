# Day 18 Exercises
import re

# Exercise Level 1
# Question 1
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

def word_freq(paragraph):
    words = re.findall(r'\w+',paragraph.lower())
    count_dict={}
    for i in words:
        if i in count_dict:
            count_dict[i]+=1
        else:
            count_dict[i]=1

    count_list = sorted(list(count_dict.items()),reverse=True, key = lambda x:x[1])
    return count_list
print(word_freq(paragraph))

# Question 2
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points = [int(re.findall(r'-?\d+',i)[0]) for i in points]
print(sorted_points)
difference = max(sorted_points) - min(sorted_points)
print(difference)

# Exercise Level 2
import keyword
var_pattern = r'^[A-Za-z_][a-zA-Z0-9_]*$'
def is_valid_variable(name):
    if not re.fullmatch(var_pattern,name):
        return False
    if keyword.iskeyword(name):
        return False
    return True


# Exercise Level 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

clean_sentence = re.sub(r'%|@|\$|&|#|;|\!','',sentence)
print(clean_sentence)
print(word_freq(clean_sentence)[0:3])
