#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Twinkle, twinkle, little star");
print('        '"How I wonder what you are");
print('\t\t' "Up above the world so high");
print('\t\t' "Up above the world so high,");
print("Twinkle, twinkle, little star");
print('        '"How I wonder what you are");


# In[2]:


# Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[3]:


# Write a Python program which accepts the radius of a circle from the user and compute
# the area.

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[4]:


# Write a Python program to display the current date and time.

import datetime
x = datetime.datetime.now()
print(x)


# In[5]:


# Write a Python program to get the Python version you are using

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[6]:


# Write a python program which takes two inputs from user and print them addition

a = int(input("enter first number: "))
b = int(input("enter second number: "))
 
sum = a + b
 
print("sum:", sum)


# In[7]:


# Write a program which take input from user and identify that the given number is even
# or odd?

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[8]:


# Write a program which print the length of the list?

ListName = ["Hello", "World", 1, 2, 3]
print ("Number of items in the list = ", len(ListName))


# In[9]:


# 10.Write a Python program to sum all the numeric items in a list?


total = 0
ele = 0

# creating a list
list1 = [11, 5, 17, 18, 23]

while(ele < len(list1)):
    total = total + list1[ele]
    ele += 1

print("Sum of all elements in given list: ", total)


# In[10]:


print("MARK_SHEET:")
print("Enter your Math Mark:")
markOne = int(input())
print("Enter your Computer Mark:")
markTwo = int(input())
print("Enter your Urdu Mark:")
markThree = int(input())
print("Enter your Islamiat:")
markFour = int(input())
print("Enter your English:")
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg>=41 and avg<51:
    print("Your Grade is C2")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E1")
elif avg>=0 and avg<21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")


# In[ ]:




