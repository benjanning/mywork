# this program reads in a string and stripe
# any leding or trailing spaces.
# It Also converts all the letters to lower case.
# This program lso outputs the length of the original string
# and the normalised one

rawString = input ("please enter a string: ")
normalisedString = rawString.strip() .lower ()

lengthOfRawString = len (rawString)
lengthOfNormalised = len (normalisedString)

print ("That string normalised is : {}" .format (normalisedString))
print ("we reduced the input string from {} to {} characters".format(lengthOfRawString, lengthOfNormalised))