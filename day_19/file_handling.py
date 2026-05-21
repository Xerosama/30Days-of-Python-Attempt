# Day 19 Exercises
# Exercise Level 1 
import re
# Question 1
word_def = r'\w+'
def count_words_lines(infile):
    word_list = re.findall(word_def,infile.read())
    infile.seek(0)
    line_list = infile.read().splitlines()
    line_count = len(line_list)
    return line_count, len(word_list)

#Obama
obama_f = open('./day_19/obama_speech.txt','rt')
obama_lines, obama_words = count_words_lines(obama_f)
print(f'For Obama Speech \nNumber of lines :{obama_lines},Number of words: {obama_words}')
obama_f.close()

#Michelle Obama
michelle_f = open('./day_19/michelle_obama_speech.txt','rt')
michelle_lines, michelle_words = count_words_lines(michelle_f)
print(f'For Michelle Obama Speech \nNumber of lines :{michelle_lines},Number of words: {michelle_words}')
michelle_f.close()

#Donald
donald_f = open('./day_19/donald_speech.txt','rt')
donald_lines, donald_words = count_words_lines(donald_f)
print(f'For Donald Speech \nNumber of lines :{donald_lines},Number of words: {donald_words}')

donald_f.close()

#Melina
melina_f = open('./day_19/melina_trump_speech.txt','rt')
melina_lines, melina_words = count_words_lines(melina_f)
print(f'For Melina Speech \nNumber of lines :{melina_lines},Number of words: {melina_words}')

melina_f.close()

# Question 2
import json
def most_spoken_lang(infile,topnum):
    countries_f = open (infile,'r')
    countries_data = json.load(countries_f)
    language_dict={}
    for i in countries_data:
        for j in i['languages']:
            if j in language_dict:
                language_dict[j]+=1
            else:
                language_dict[j]=1
    language_list = list(language_dict.items())
    sorted_lang_list = sorted(language_list,key=lambda x:x[1],reverse=True)
    countries_f.close() 
    return sorted_lang_list[0:topnum][:]

print(most_spoken_lang('./day_19/countries_data.json',15))

# Question 3
def most_populated_countries(filepath,topnum):
    countries_f=open(filepath,'rt')
    countries_data = json.load(countries_f)
    pop_list = [{'country':i['name'],'population':i['population']} for i in countries_data]
    sorted_pop_list = sorted(pop_list,key=lambda x:x['population'], reverse=True)
    countries_f.close()
    return sorted_pop_list[0:topnum]

print(most_populated_countries('./day_19/countries_data.json',15))

# Exercise Level 2
# Question 1
import re
def incoming_emails(filepath):
    file = open(filepath,'r')
    incoming_email_regex=re.compile(r'From\s*([\w\.-]+@[\w\.]+)',re.IGNORECASE)
    email_list = re.findall(incoming_email_regex,file.read())
    unique_email_list = list(set(email_list))
    return unique_email_list

print(incoming_emails('./day_19/email_exchanges_big.txt'))

# Question 2 
def find_most_frequent_words(filepath,topnum):
    text = open(filepath,'r')
    word_count_dict={}
    words = re.findall(r'\w+',text.read().lower())
    for i in words:
        if i in word_count_dict:
            word_count_dict[i]+=1
        else:
            word_count_dict[i]=1
    word_count_list = sorted(list(word_count_dict.items()),key=lambda x:x[1],reverse=True)
    text.close()
    return word_count_list[0:topnum]

#Question 3

#Obama
print('obama speech')
print(find_most_frequent_words('./day_19/obama_speech.txt',10))

#Michelle
print('Michelle Speech')
print(find_most_frequent_words('./day_19/michelle_obama_speech.txt',10))

#Trump
print('Donald Speech')
print(find_most_frequent_words('./day_19/donald_speech.txt',10))

#Melina
print('Melina Speech')
print(find_most_frequent_words('./day_19/melina_trump_speech.txt',10))

# Question 4 
#Using Cosine similarity, count no. of times all unique words have been used in both texts, treat both as a vector. Find its cosine
# angle by doing a dot product and dividing by product of magnitudes of each vector. The solution is in a file named text similarity

# Question 5
#Romeo and Juliet
print('Romeo and Juliet')
print(find_most_frequent_words('./day_19/romeo_and_juliet.txt',10))

# Question 6
import csv 
with open('./day_19/hacker_news.csv','r') as file:
    csv_reader = csv.reader(file,delimiter=',')
    line_count = 0
    python_count=0
    python_count=0
    javascript_count=0
    java_count=0
    for row in csv_reader:
        line_count+=1
        if 'python' in row[1].lower():
            python_count+=1
        elif 'python' in row[2].lower():
            python_count+=1
        if 'javascript' in row[1].lower():
            javascript_count+=1
        elif 'javascript' in row[2].lower():
            javascript_count+=1
        if 'java' in row[1].lower() and 'javascript' not in row[1].lower() :
            java_count+=1
        elif 'java' in row[2].lower() and 'javascript' not in row[2].lower():
            java_count+=1
    print(f'Line Count:{line_count}')
    print(f'Python Line Count:{python_count}')
    print(f'Javascript Line COunt:{javascript_count}')
    print(f'Java Line Count:{java_count}')

        

