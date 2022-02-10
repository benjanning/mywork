#Asks user to input a number and tells if it is odd or even
#Author: Ben Janning

number = int (input("enter an integer:"))

if (number % 2) == 0:
    print ("{} is an even number".format (number))
else:
    print ("{} is an odd number".format(number))
    
    