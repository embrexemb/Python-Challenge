import os
import string
import pickle
import re
import nltk
nltk.download('punkt')

from collections import Counter

paragraph_path = os.path.join("raw_data","paragraph_1.txt")

def load_file(filepath):
    with open(filepath,"r") as textfilehandler:
        return textfilehandler.read().lower().split()

#get word list
word_list = load_file(paragraph_path)
sentence_data = load_file(paragraph_path)

#sentence = re.split("(?<=[.!?]) +", sentence_data)
#print(sentence)


#word set 
parag = set()


#remove trailing punctuation
for token in word_list:
    parag.add(token.split(',')[0].split('.')[0])
#check
print(parag)

word_count = {}.fromkeys(word_list,0)
for word in word_list:
     word_count[word] += 1
#print(word_count)

#word_counter = Counter(parag)
#print(word_counter)


