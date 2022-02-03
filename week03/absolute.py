# Give the abolsute value of a number

# Author: Ben Janning

#In the question, numer is ambiguos but the 
# output implies that we should be dealing with floats
# So I am casting the input to a float

number = float(input("Enter a number:"))
absoluteValue = abs(number)
print ('The Absolute value of {} is {}' .format (number, absoluteValue))