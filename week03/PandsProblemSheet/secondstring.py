# a program that asks a user to input a string and 
# outputs every second letter in reverse order.
# Author: Ben Janning

from re import X


A = input ("Enter String: ")

# create empty list:
new_list= []

For: X in A
If: X % 2 !=0
new_list.append(X)

print (new_list)