############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

def calculate_score(cards):
    score = sum(cards)
    if (score > 21) and (11 in cards):
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def deal_card(choices, number_needed):
    #if number_needed == 1:
        #return random.choice(choices)
    return random.sample(choices, number_needed)

print(logo)
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while play == 'y':
    choices = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    players_cards = deal_card(choices, 2)
    computers_cards = deal_card(choices, 2)
    players_score = calculate_score(players_cards)
    computers_score = calculate_score(computers_cards)
    print(f"Your cards: {players_cards}, current_score: {players_score}")
    print("Computer's first card: ", computers_cards[0])
    if computers_score == 21:
        print(f"Your final hand: {players_cards}, final score: {players_score}")
        print(f"Computer's final hand: {computers_cards}, final score: {computers_cards}")
        print("Opponent has Blackjack. You lose")
        break
    hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while hit not in ['y', 'n']:
        print("Not a valid option. Try again.")
        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while hit == 'y' and players_score <= 21:
        players_cards.extend(deal_card(choices, 1))#players_cards.append(deal_card(choices, 1))
        players_score = calculate_score(players_cards)
        if players_score > 21:
            break
        print(f"Your cards: {players_cards}, current_score: {players_score}")
        print("Computer's first card: ", computers_cards[0])
        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while computers_score < 17:
        if players_score > 21:
            break
        computers_cards.extend(deal_card(choices, 1))#computers_cards.append(deal_card(choices, 1))
        computers_score = calculate_score(computers_cards)
    print(f"Your final hand: {players_cards}, final score: {players_score}")
    print(f"Computer's final hand: {computers_cards}, final score: {computers_score}")
    if players_score > 21:
        print("You went over. You lose")
    elif computers_score > 21:
        print("Opponent went over. You win!")
    elif players_score < computers_score:
        print("Opponent has a higher score. You lose")
    elif players_score == computers_score:
        print("Both you and the computer have the same score. It's a draw.")
    elif players_score > computers_score:
        print("Your score is higher. You win!")
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()   