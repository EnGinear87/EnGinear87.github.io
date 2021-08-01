# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:57:33 2021

@author: Melvin Wayne Abraham | Module 3_Python Assignment
"""

#Question 1:
  
#Assign a random string evaluation
string = 'X-DSPAM-Confidence: 0.8475'

#Find the colon character, extract the remaining value and convert to floating point number
colon_char = string.find(':')
number = string[colon_char + 1:]
confidence_val = float(number)
print('The confidence value is:', confidence_val)



#Question 2:
  
#Initialize the value, assign the datafile over and create a list of lines
spam = []
findingwords = "buad5802-m3-python-assignment-data-file.txt"
with open(findingwords, 'r') as fh:
    for line in fh.read().split('\n'):
        if line.startswith('X-DSPAM-Confidence:'):
            spam.append(line.replace('X-DSPAM-Confidence: ', ''))

#Convert the string to float values
spam = [float(i) for i in spam]
print('The average spam confidence is : %f' % float( sum(spam) / len(spam)))
