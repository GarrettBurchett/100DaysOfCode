from random import randint
from art import logo

def compare_guess(guess, number):
    if guess > number:
        print("Too high.\nGuess again.")
    elif guess < number:
        print("Too low.\nGuess again.")
    else:
        print(f"You got it! The answer was {number}. You win!!")

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number = randint(1, 100)
while difficulty not in ['easy', 'hard']:
    print("Invalid response. Please select an appropriate difficulty.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'hard':
    attempts = 5
else:
    attempts = 10
print(f"You have {attempts} attempts remaining to guess the number.")
guess = int(input("Make a guess: "))
compare_guess(guess, number)
while guess != number:
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number.")
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        break
    guess = int(input("Make a guess: "))
    compare_guess(guess, number)