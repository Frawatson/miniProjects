import random;

while True:
    print("++++++++++++++++++++++++")
    print("Rock Paper Scissors")
    print("++++++++++++++++++++++++")
    print("Pick a number, 1 for Rock, 2 for Paper, 3 for Scissors")
    print("++++++++++++++++++++++++")

    UserPick = int(input("Enter pick: ",  ))
    print("++++++++++++++++++++++++")

    CompPick = random.randint(1,3)

    if UserPick == CompPick:
        print("Tie")
    elif UserPick == 1 and CompPick == 2:
        print("You Lose, Computer picked Paper")
    elif UserPick == 1 and CompPick == 3:
        print("You Win, Computer picked Scissors")
    elif UserPick == 2 and CompPick == 1:
        print("You Win, Computer picked Rock")
    elif UserPick == 2 and CompPick == 3:
        print("You Lose, Computer picked Scissors")
    elif UserPick == 3 and CompPick == 1:
        print("You lose, Computer picked Rock")
    elif UserPick == 3 and CompPick == 2:
        print("You Win, Computer picked Paper")
    else:
        print("Invalid: Chose 1 for Rock, 2 for Paper, and 3 for Scissors")

    play_again = input("Play again? (y/n)")
    if play_again.lower() != "y":
        break