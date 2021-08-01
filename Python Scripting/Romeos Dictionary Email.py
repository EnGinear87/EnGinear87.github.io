# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:31:09 2021

@author: Melvin Wayne Abraham | Module 4_Python Assignment
"""
#Question 1: Using the Romeo data file  download, write a program to open the file and read it line by line.
#For each line, split the line into a list of words using the split function.
#When the program completes, sort and print the resulting words in alphabetical order.
#Need to figure out how to maintain the same order for capital or non-capital words

print(' Question 1:  ')
#Import the data from the folder and then assign it over to a variable called romeo_data
data = "buad5802-m4-python-assignment-data-file-romeo.txt"
#print(data)
romeo_data = open(data)
oh_romeo = list() #Creates an empty list
for line in romeo_data: #Iterates through each line of the data file mentioned above
    find_words = line.split() #Splits the strings into a list of words per line
    #print(find_words) #Verify all the words within the list
    for word in find_words: #Finds each new word in the new list and iterates through
      if word not in oh_romeo: #If the word is not in the original list, append the new one
        oh_romeo.append(word)
        #print(oh_romeo)
      else: #This will ensure it continually loops through all the words and continues
        continue
#Now print the results from the list sorted in alphabetical order
print('The words in alphabetical order (capital or not) are: ',
      sorted(oh_romeo, key=lambda v: (v.upper(), v[0].islower())))
print('   ')

#Question 2: Using the data file from the M3 Python assignment download, 
#write a program that categorizes each email message by which day of the week the email was sent.
#To do this, look for lines that start with "From," then look for the third word 
#and keep a running count of each of the days of the week.
#At the end of the program, print out the contents of your dictionary (order does not matter).

print(' Question 2:  ')
days_dict = {} #Creates an empty dictionary
dayslist = [] #Creates an empty list

with open("buad5802-m3-python-assignment-data-file.txt") as day_of_week: #Open the file and set it to day_of_week
  for line in day_of_week: #Create a for loop and iterate each line
    dayslist = line.split() #Split the strings into a list of words per line
#If the length of words is greater than 3 and the line starts with "From" then keep a running count
    if len(dayslist) > 3 and line.startswith('From'):
      day = dayslist[2]
      if day not in days_dict: #If it is not in the days dictionary, the value equals 1
        days_dict[day] = 1
      else: #Unless it is, then you would count it and then add one as well
        days_dict[day] += 1
#Print out the remaining information for the dictionary in no particular order
  print ('The contents of the dictionary are: ', days_dict)
print('   ')

#Question 3: Revise the program you wrote in Item 2 above, as follows:
#Read and parse the “From” lines and pull out the email addresses from the line.
#Count the number of messages from each person using a dictionary.
#After all the data has been read, print the person with the most emails 
#sent by creating a list of (count, email) tuples from the dictionary.
#Sort the list in reverse order (Z–A) and print out the person with the most emails sent.

print(' Question 3:  ')
#Read the filename or if null use the standard name
name = "buad5802-m3-python-assignment-data-file.txt"
if len(name) < 1 : name = "buad5802-m3-python-assignment-data-file.txt"
data_start = open(name)
    
count = 0 #Set the original count value to zero
email_list = list() #Creates an empty list
person = dict() #Creates an empty dictionary
most_emails = 0 #Set the original count value to zero
quantity_emails = 0 #Set the original count value to zero

for line in data_start: #Create a for loop and iterate each line
  email_list = line.split() #Split the strings into a list of words per line
  #print(email_list) #Verify the email list is correct
#If From is in the email list, then the person equals the previous value plus 1
  if "From" in email_list:
    person[email_list[1]] = person.get(email_list[1],0) + 1
  else:
    continue
 
for key in person: #Create a for loop through each key in the person's email
    if person[key] > quantity_emails : #If the persons email is the greatest quantity
      most_emails = key #Then it equals the most emails
      quantity_emails = person[key] #And the quantity equals the person in the key
print('The following emails have been sorted in reverse order (Z-A)', sorted(person, reverse=True))
print('The person with the most emails is registered to', most_emails, 'in the amount of', quantity_emails, 'emails sent.')
print('   ')

print ('Here is another method finding the solution to Question #3 with less coding than above:'  )
data_file = open('buad5802-m3-python-assignment-data-file.txt') #Opens the data file
counts = dict() #Create an empty dictionary
for line in data_file: #Iterate through each line of the file
    if line.startswith('From:'): #If the line starts with "From" then split it and add the first line to an email
        line = line.split()
        email = line[1]
        counts[email] = counts.get(email,0)+1 #Count the emails from each sender into a dictionary per person
print('The following emails have been sorted in reverse order (Z-A)', sorted(counts, reverse=True))
print('The person with the most emails is registered to', email, 'in the amount of', max(counts.values()), 'emails sent.')
