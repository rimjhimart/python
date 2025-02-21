import random

options = ("ROCK", "PAPER", "SCISSOR")

playing = True

while playing:
    player=None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice: ").upper()

    print(f"player: {player}")
    print(f"computer: {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == "ROCK" and computer == "SCISSOR":
        print("You win!")
    elif player == "PAPER" and computer == "ROCK":
        print("You win!")
    elif player == "SCISSOR" and computer == "PAPER":
        print("You win!")
    else:
        print("You lose!")
    if not input("Play again? (Y/N): ").lower():
        playing = False


print("Hope you enjoyed...")  


