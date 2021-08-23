# -*- coding: utf-8 -*-
"""
Created on Wed May 19 22:37:31 2021

@author: Melvin Wayne Abraham | Module 2_Python Assignment
"""

#Question 1: Write a Python program to find those numbers which are divisible by 7 and a multiple of 5,
#between 1500 and 2700 (both included).
print("Question 1: The numbers that are disvisible by 7 and a multiple of 5 are: ")

numdivis = [] #initialize a random value
for a in range(1500, 2701):
    if (a % 7 == 0) and (a % 5 == 0): #First divide a by 7 and then see if its a multiple of 5
        numdivis.append(str(a)) #append the new values from the range
print (','.join(numdivis))


#Question 2: Write a Python program to construct the following pattern, using a nested for loop.
"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
print("Question 2: Given the pattern above, we constructed the pattern below using a nested for loop: ")

pattern = 6 #Assign a number with a value that is one higher than your desired length

for i in range(12):

    if i <= 5: #If we lower than our value, then subtract the value and place an asterik

        for j in range(i - 1):

            print(" * ",end="")

        print("\n")

    elif i > 5 : #But if we are higher than our value, then subtract the value and place an asterik

        for j in range(pattern - 1):

            print(" * ",end="")

        print("\n")

        pattern = pattern - 1


#Question 3: Write a Python program that prints each item and its corresponding type from the following list.
#List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V',"section":A}]
print("Question 3: The cooresponding type from the following list is: ")

#Copy the datalist over and then create a for loop iterating through each of the items
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]
for items in datalist:
   print (items, " as a ", type(items), "type")
   
   
#Question 4: Write a Python program which iterates the integers from 1 to 50. For multiples of three, print
#"fizz" instead of the number and for the multiples of five, print "buzz." For numbers that are
#multiples of both three and five, print "fizzbuzz."

print("Question 4: Iterating through integers 1 to 50, we have 3 expression which are 'fizz' for multiples of 3\
      , 'buzz' for multiples of 5, and 'fizzbuzz' for multiples of 3 and 5: ")

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0: #First divide by 3 and if you can divide by 5, add fizzbuzz
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0: #If you can divide it by 3 and it doesn't equal zero, continute
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0: #If you can divide by 5, continue and print out buzz
        print("buzz")
        continue
    print(fizzbuzz)





