from art import logo, vs
from game_data import data
from random import choice
import os

def get_random_choice(data):
    return choice(data)

def is_correct(guess, followers_a, followers_b):
    if guess == 'A':
        if followers_a > followers_b:
            return True
        return False
    elif guess == 'B':
        if followers_b > followers_a:
            return True
        return False
    
def screen(score, a, b):
    print(logo)
    if score > 0:
        print(f"That's correct! Current score: {score}.")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

score = 0
a = get_random_choice(data)
b = get_random_choice(data)
screen(score, a, b)
guess = input("Who has more followers? Type 'A' or 'B': ").upper()
while guess not in ['A', 'B']:
    print("Invalid response. Try again.")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
correct = is_correct(guess, a['follower_count'], b['follower_count'])
while correct:
    score += 1
    a = b
    b = get_random_choice(data)
    os.system('cls')
    screen(score, a, b)
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    correct = is_correct(guess, a['follower_count'], b['follower_count'])
os.system('cls')
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")