# Program that reads in students percentage 
# and prints out a corresponding grade
# Author: Ben Janning

percentage = float (input ("Enter the percentage: "))
#print (percentage)

if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")
elif percentage < 40: 
    print ("Fail")
elif percentage < 50:
    print ("Pass")
elif percentage < 60:
    print ("Merit1")
elif percentage < 70: 
    print ("Merit 2")
else:
    print ("Distinction")
