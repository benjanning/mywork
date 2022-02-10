# A program that prompts the user to guess a number, 
# until the user guesses correctly
# Author: Ben Janning

numberToGuess = 30

guess = int (input ("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int (input ("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess )


