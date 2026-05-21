import stop_words
import re
import os

# Question 4 
#Using Cosine similarity, count no. of times all unique words have been used in both texts, treat both as a vector. Find its cosine
# angle by doing a dot product and dividing by product of magnitudes of each vector.
def get_text(input):
    if os.path.isfile(input):
        with open(input,'r') as file:
            return file.read()
    else:
        print('Not valid file path, treating it as input text')
        return input
    
stop = stop_words.stop_words


def clean_text(text):
    text=text.lower()
    clean_text = re.sub(r'[^\w\s0-9]','',text)
    return clean_text

stop = [clean_text(word) for word in stop]
support_words = '|'.join(stop)
support_words_regex = rf'\b({support_words})\b'
def remove_support_words(text):

    final_text=re.sub(support_words_regex,'',text)
    return final_text

import collections

def check_text_similarity(text1,text2):
    text1_list = text1.split()
    text2_list = text2.split()

    count1 = collections.Counter(text1_list)
    count2 = collections.Counter(text2_list)

    all_unique_words =list(set(count1.keys()).union(set(count2.keys())))

    dot_product = sum(count1.get(word,0)*count2.get(word,0) for word in all_unique_words)
    magnitude1 = sum(count1.get(word,0)**2 for word in all_unique_words)
    magnitude2 = sum(count2.get(word,0)**2 for word in all_unique_words)
    if magnitude1*magnitude2 == 0:
        return 0
    else:
        similarity_coefficient = dot_product/((magnitude1*magnitude2)**0.5)
        return similarity_coefficient

#-----------Now we execute

speech1 = get_text('./day_19/michelle_obama_speech.txt')
speech2 = get_text('./day_19/melina_trump_speech.txt')

speech1 = clean_text(speech1)
speech2 = clean_text(speech2)

speech1_filtered = remove_support_words(speech1)
speech2_filtered = remove_support_words(speech2)

coefficient =check_text_similarity(speech1_filtered,speech2_filtered)

print(f'Cosine Similarity Coefficient for the 2 texts is :{coefficient}')







