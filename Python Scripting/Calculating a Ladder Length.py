# -*- coding: utf-8 -*-
"""te
Created on Sat May 15 17:02:18 2021

@author: Melvin Wayne Abraham Module 1_Python Assignment
"""
#Import the math function
from math import *

#Short description of the program
print('The length of a Ladder calculation')

#Obtain the height and angle from the user and if they enter the value in
#incorrectly, throw an exception error until enter correctly

while True:
    try:
      height = float(input('How high does the ladder need to reach the house (in feet)? '))
      
    except TypeError and ValueError or TypeError as error:
      print('The height entered is not a numerical value, please try again.')
      continue
    
    while True:
      try:
        angle_degree = float(input('What angle (in degress) do you think the ladder ' +\
                        'can sit at? '))
      except TypeError and ValueError or TypeError as error:
        print('The angle entered is not a numerical value, please try again.')
        continue
      #Now we can calculate the length of the ladder after we have both a valid height and length
      else:
        angle_radians = angle_degree * pi / 180 #convert degrees to radians
        length = height / sin(angle_radians) #calculate the length of the ladder
      
        #Display the result for the end user
        print('\nThe minimum length required for your ladder should be ', round(length, 2), \
                'feet because you entered enter a height of ' + str(height) + ' and an angle of ' +\
                  str(angle_degree) + ' degrees')
        break
    break
#%%

#Short description of the program
print("\
      \
      STARTING A NEW PROGRAM \
      \
      ")
print('Now we need to find the average of a series of numbers entered by a user')

#Create a user input value and count the amount of numbers being used
while True:
    try:
      num = int(input('How many numbers are there? The value must be greater than 0: '))
      total_sum = 0
    except TypeError and ValueError or ZeroDivisionError or TypeError as error: #Checks to make sure the value is numerical
      print('The value you enter is not a numerical value, please try again')
      continue      
     #Create a for loop and check to make sure values are numerical and if not, show an error message 
    for n in range(num):
      try:
        numbers = float(input('Enter number : '))
        total_sum += numbers
      except TypeError and ValueError or ZeroDivisionError or TypeError as error:
        print("The value you enter is not a numerical value, please try again")
        break
    else:
      avg = total_sum / num #Calculate average from the user inputted values
      print('Average of ', num, ' numbers is :', avg) 
      break #finalize and stop while loop
