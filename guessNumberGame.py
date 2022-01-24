import random
print("=======================")
print("Guessing the right number")
print("=======================")
computerGuess = random.randint(1, 50)
userGuess = 0
print("Guess a number between 1 to 50")
while (userGuess != computerGuess):
    print("=======================")
    userGuess = int(input("Enter number: "))
    print("=======================")

    if(userGuess <= 0 or userGuess > 50):
        print("=======================")
        print("Invalid number ")
        print("=======================")

    elif(userGuess == computerGuess):
        print("=======================")
        print("Congrat!!, you guess right")
        print("=======================")

    elif(userGuess < computerGuess):
        print("=======================")
        print("Guess a higher number")
        print("=======================")

    elif(userGuess > computerGuess):
        print("=======================")
        print("Guess a lower number")
        print("=======================")
