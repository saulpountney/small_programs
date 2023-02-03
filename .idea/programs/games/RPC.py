import random

playerScore = 0
computerScore = 0

#Start of program stating option.
while True:
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    print("...lizard...")
    print("...spock...")

    #Player is prompted for choice.
    player = input("(Enter your choice): ").lower()
    #Option to quit.
    if player == "quit" or player == "q":
        break

    #Computer choice
    random_num = random.randint(0,4)
    if random_num == 0:
        computer = "rock"
    elif random_num == 1:
        computer = "paper"
    elif random_num == 2:
        computer = "lizard"
    elif random_num == 3:
        computer = "spock"
    else:
        computer = "scissors"

    print(f"Computer plays {computer}" )

    #Working out the equations
    if player == computer:
        print("It's a tie!")
    elif player == "rock" or player == "r":
        if computer == "paper":
            print("Computer wins!")
            computerScore += 1
        elif computer == "spock":
            print("Computer wins!")
            computerScore += 1
        else:
            print("player wins!")
            playerScore += 1

    elif player == "paper" or player == "p":
        if computer == "sissors":
            print("Computer wins!")
            computerScore += 1
        elif computer == "lizard":
            print("Computer wins!")
            computerScore += 1
        else:
            print("player wins!")
            playerScore += 1

    elif player == "scissors" or player == "s":
        if computer == "rock":
            print("Computer wins!")
            computerScore += 1
        elif computer == "spock":
            print("Computer wins!")
            computerScore += 1
        else:
            print("player wins!")
            playerScore += 1

    elif player == "lizard" or player == "l":
        if computer == "rock":
            print("Computer wins!")
            computerScore += 1
        elif computer == "lizard":
            print("Computer wins!")
            computerScore += 1
        else:
            print("player wins!")
            playerScore += 1

    elif player == "spock" or player == "v":
        if computer == "paper":
            print("Computer wins!")
            computerScore += 1
        elif computer == "lizard":
            print("Computer wins!")
            computerScore += 1
        else:
            print("player wins!")
            playerScore += 1

    #Error Correction
    else:
        print("Please enter a valid move!")

    print("player: ", playerScore, "Computer: ", computerScore)

print("Thanks for playing!")