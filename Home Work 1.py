#Question 1:
word = 'banana'
new_word = word.replace('a', 'i')
print (new_word)
print (40*'-')

#Question 2:
n = int(input('Please enter a positive integer: '))
i = 0
j = 0

while i < n:
    i += 1
    while j < n:
        j += 1
        print (i, '*', j, '=', i*j)
    else:
        j = 0
print (40*'-')

#Question 3:
str = input('Please enter a sentence: ')
list = str.split(sep = ' ')
def len_list(list):
      return [(len(s), s) for s in list]
print(sorted((len_list(list)), key=lambda k: k[0]))
print (40*'-')

#Question 4:
with open('question4.txt', 'r') as file:
        text = file.read().splitlines()
        words = []
        for i in range(len(text)):
            words += text[i].split()       
from collections import Counter
counts = Counter(words)
print (counts.most_common(5))
print (40*'-')

#Question 5:
import re

def date_regex(date):
    test = r'\d{4}\-(?:0[1-9]|1[012])\-(?:0[1-9]|[12][0-9]|3[01])'
    check = re.compile(test)
    return check.findall(date)

def zipcode_regex(zipcode):
    regex = r'[0-9]{5}(?:-[0-9]{4})?'
    check = re.compile(regex)
    return check.findall(zipcode)

def email_regex(email):
    regex = r'\w+\@\w+\w*\.com'
    check = re.compile(regex)
    return check.findall(email)

text = input('Please enter a sentence: ')
datetime = date_regex(text)
zipcode = zipcode_regex(text)
email = email_regex(text)
print ("Dates: ")
print (datetime)
print ("Zipcodes: ")
print (zipcode)
print ("Emails: ")
print (email)
print (40*'-')

#Question 6:
import numpy as np
a = np. array ([1, 2, 3, 2])
b = np. array ([2, 2, 2, 2])
result = [ ]
for i in range (len(a)):
    if a[i] == b[i]:
        result.append(i)
print (result)
print (40*'-')