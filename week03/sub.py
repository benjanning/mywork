# program to subtract one number from another.
#Author Ben Janning

#input reads in a string so we need to convert it into an int
#so we can perform mathematical operations

x = int(input ("Enter first nuber: "))
y = int (input ("Enter second number: "))
answer = x-y
print ("{} minus {} is {} ".format (x , y, answer))