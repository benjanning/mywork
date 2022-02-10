# A program that prompts the user to guess a number, 
# and tells the user whether the number is too high or too low,
# until the user guesses correctly
# Author: Ben Janning

numberToGuess = 30

guess = int (input ("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("too low")
    else:
        print ("too high")
    guess = int (input ("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess )