import random

randNumber= random.randint(1,1000)
print(randNumber)
usersGuess= None
guesses=0

while(usersGuess != randNumber):
    usersGuess=int(input("Enter your Guess:"))
    if(usersGuess==randNumber):
        print("your Guess number is right ! ")
    else:
        print("your Guess number is wrong !")

print(f"You Guessed the number in {guesses} guesses")