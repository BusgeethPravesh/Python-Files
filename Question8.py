"""Write a Python program to make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)
Remember the rules: 1.Rock beats scissors
                    2.Scissors beats paper
                    3.Paper beats rock
"""
count="yes"
while count.lower()=="yes":
    print("Choose between: \n1.Rock\n2.Paper\n3.Scissors")
    player1 = input("\nChoice of Player 1:")
    print("Player 1 chose:", player1)

    player2 = input("\nChoice of Player 2:")
    print("Player 2 chose:", player2)


    if (player1.lower() =="rock" and player2.lower() =="scissors"):
        print("\nCongratulations to Player 1. You won the game.")

    elif (player1.lower() =="scissors" and player2.lower()=="rock"):
        print("\nCongratulations to Player 2. You won the game.")

    elif (player1.lower() =="scissors" and player2.lower() =="paper"):
        print("\nCongratulations to Player 1. You won the game.")

    elif (player1.lower() =="paper" and player2.lower() =="scissors"):
        print("\nCongratulations to Player 2. You won the game.")

    elif (player1.lower() =="paper" and player2.lower() =="rock"):
        print("\nCongratulations to Player 1. You won the game.")

    elif (player1.lower() == "rock" and player2.lower() == "paper"):
        print("\nCongratulations to Player 2. You won the game.")

    else:
        print("Invalid inputs.")

    count=input("\nTry again? Yes/No?")
    if count =="no":
        break