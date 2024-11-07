from getpass import getpass as input

print("More Epic Game Battle")

print()

while True:  # Start the game loop

    print("Select your move (R, P or S, or 'q' to quit)")

    print()

    player1Move = input("Player 1 > ")

    print()

    player2Move = input("Player 2 > ")

    print()

    if player1Move.lower() == 'q' or player2Move.lower() == 'q':
        print("Thanks for playing!")
        break  # Exit the loop

    if player1Move == "R":

        if player2Move == "R":
            print("You both picked Rock, draw!")
        elif player2Move == "S":
            print("Player1 smashed Player2's Scissors into dust with their Rock!")
        elif player2Move == "P":
            print("Player1's Rock is smothered by Player2's Paper!")
        else:
            print("Invalid Move Player 2!")  
    elif player1Move == "P":
        if player2Move == "R":
            print("Player2's Rock is smothered by Player1's Paper!")
        elif player2Move == "S":
            print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
        elif player2Move == "P":
            print("Two bits of paper flap at each other. Dissapointing. Draw.")
        else:
            print("Invalid Move Player 2!")

    elif player1Move == "S":
        if player2Move == "R":
            print("Player 2's Rock makes metal-dust out of Player1's Scissors")
        elif player2Move == "S":
            print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
        elif player2Move == "P":
            print("Player1's Scissors make confetti out of Player2's paper!")
        else:
            print("Invalid Move Player 2!")

    else:
        print("Invalid Move Player 1!")
