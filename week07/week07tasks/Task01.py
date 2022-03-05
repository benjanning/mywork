# Write a function that reads in a number from a file that already exists
# (count.txt). test the program by calling the function and outputting the
# number.

#Author: Ben Janning


filename = "count.txt"
def readNumber () :
    with open (filename) as f:
        number = int (f.read () )
        return number

#test it
num = readNumber ()
print (num)