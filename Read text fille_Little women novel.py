# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:02:07 2024

@author: Irene Chau
"""

from collections import Counter as Counter
import pandas as pd

# Open the file with utf-8-sig to handle BOM
file = open(r'C:\Users\User\OneDrive\Desktop\Fordham\Programming with Python (CISC-5380-L01)\Little women novel.txt', 'r', encoding='utf-8-sig')
lines = file.readlines()
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
cleaned_words=[]
for line in lines:
    words=line.split()
    for word in words:
        cleaned_word=''
        for char in word:
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

