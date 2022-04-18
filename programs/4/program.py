# To write a python program to find the most frequent words in a
# text file.

import string

# open the file in read mode

text = open("fruit.txt", "r")

# create a empty dictionary

d = {}

# loop through the file

for line in text:

    # remove the leading and trailing spaces

    line = line.strip()

    # split the line into lower case words

    line = line.lower()

    # remove the punctuation marks

    line = line.translate(str.maketrans('', '', string.punctuation))

    # split the line into words

    words = line.split()

    # loop through the words

    for word in words:
            
            # if the word is already in the dictionary
    
            if word in d:
    
                # increment the count
    
                d[word] += 1
    
            else:
    
                # add the word to the dictionary
    
                d[word] = 1


# print the dictionary
# 
print(d)

for key in d:
    
    print(key, ":", d[key]) 
