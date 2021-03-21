#PyParagraph
import os
import string
import re

#type in a file name at the input prompt
fileinput=input("Type in a filename to process: ")
#paragraph_path = os.path.join("raw_data","paragraph_1.txt")
paragraph_path = os.path.join("raw_data",fileinput)
def load_file(filepath):
    with open(filepath,"r") as textfilehandler:
        return textfilehandler.read()

def Load_list(filepath):
    with open(filepath,"r")as textfilehandler:
        return textfilehandler.read().lower().split()


#get words as a string
textLoaded = load_file(paragraph_path)

SCounted = len(re.findall(r'\.!?',textLoaded))
#Count the sentences in the text blockpp

print(f'--------------------')
print(f'Paragraph Analysis')
print(f'--------------------')
#get textblock as a list
Para_strings = Load_list(paragraph_path)
wordsinparagraph = len(Para_strings)
print(f'Approximate Word Count: {wordsinparagraph}')
print(f'Approximate Sentence Count: {SCounted}')

#get the character for the words
sum = 0
for words in Para_strings:
    ch = len(words)
    sum = sum + ch

print(f'Average Letter Count: {round(sum/wordsinparagraph,2)}')

#get the average number of words per sentence
print(f'Average Sentence Length: {round(wordsinparagraph/SCounted,2)}')






 




