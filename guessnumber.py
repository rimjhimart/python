
import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num,highest_num)
guesses = 0

is_running = True
print("Welcome to the Python Number Guessing Game")
print(f"Guess a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your Guess: ")
    if guess .isdigit():
        guess = int(guess)
        guesses += 1
        if guess<lowest_num or guess>highest_num:
            print("The number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess<answer:
            print("your guess is too low!")
        elif guess>answer:
            print("your guess is too high!")
        else:
            print(f"Correct! the answer was {answer}")
            print(f"The number of guesses is {guesses}")
            is_running=False
    else:
        print(f"Invalid guess")
        print(f"Please select a valid number")

