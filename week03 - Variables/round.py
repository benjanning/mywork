#rounds a number
# be careful of round, it rounds to the nearest even number
# e.g. 4.5 rounds to 4
# but 5.5 rounds to 6 
# so do not use it accuracy is essential
# Author: Ben Janning

numberToRound = float(input("Enter a float nuber:"))
roundedNumber = round (numberToRound)
print  ( '{} rounded is {} '.format(numberToRound,roundedNumber))