import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if player_choice == 0:
        print(rock)
        break
    elif player_choice == 1:
        print(paper)
        break
    elif player_choice == 2:
        print(scissors)
        break
    else:
        print("Please select a valid input")

print('Computer chose:')
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if player_choice == computer_choice:
    print("It's a draw")
elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose")
