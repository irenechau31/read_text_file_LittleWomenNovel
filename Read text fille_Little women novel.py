# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:02:07 2024

@author: Irene Chau
"""

from collections import Counter as Counter
import pandas as pd

# Open the file with utf-8-sig to handle BOM '\theff'
file = open(r'C:\Users\User\OneDrive\Desktop\Fordham\Programming with Python (CISC-5380-L01)\Little women novel.txt', 'r', encoding='utf-8-sig')
lines = file.readlines() #using readlines() in stead of readline() to read multiple lines
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

#create an empty list of cleaned_words to store cleaned words without punctuations
cleaned_words=[]
for line in lines: #read each line in lines 
    words=line.split() #splitting words in that line, output a list of words
    for word in words: #for each word in that list of words
    
        #create an empty str to store the cleaned word after checking each of characters in the word
        cleaned_word='' 
        for char in word: #for each char in that word
        #if the character is not punctuation -> add the char to empty str cleaned_word
            if char not in punctuation:
                cleaned_word+=char
                
#code may add empty strings to cleaned_words, especially if any words consist only of punctuation.
        if cleaned_word: # Only add non-empty cleaned words
            cleaned_words.append(cleaned_word.lower())
            
file.close()
print(cleaned_words)
# Count the total number of the words
print(f'\nTotal number of words: {len(cleaned_words)}')


# the number of times each word is used and print out the top 10 most frequently used words.
word_frequency=Counter(cleaned_words).most_common(10)
# Convert the list of tuples into a DataFrame
df_word_frequency = pd.DataFrame(word_frequency, columns=['Word', 'Frequency'])
# Display the DataFrame
print('\nTop 10 most common words in Little Women:')
print(df_word_frequency)

